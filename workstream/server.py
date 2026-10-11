#!/usr/bin/env python3
"""Local review/edit server for the /workstream/ dashboard.

Serves the dashboard and the JSON files it reads (so relative fetches like
../open-prs.json match production) and exposes one write endpoint,
POST /api/save, used by the dashboard's "Save & Publish" button. That
endpoint writes workstream-classification.json and workstream-layout.json
to disk, then commits (signed off) and pushes -- so an edit made here shows
up on the live GitHub Pages site once pushed. It never touches the files
owned by the scheduled Actions workflows (open-prs.json, open-issues.json,
activity.json, workstream-archive.json).

Because the write endpoint commits and pushes with the user's credentials,
it must only ever be reachable by the dashboard page this server itself
serves, never by an arbitrary website the user happens to have open:

  * no CORS headers, and non-simple cross-origin requests are refused;
  * Host must be a loopback name:port (defeats DNS rebinding);
  * POST needs a same-origin Origin (if sent), a JSON content type, and a
    random per-run token that only a same-origin read of /api/health returns;
  * only the dashboard and its JSON inputs are served -- never .git/ or
    anything else in the repo.

Usage: python3 workstream/server.py [port]
"""
import hmac
import json
import secrets
import subprocess
import sys
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parent.parent
CLASSIFICATION_NAME = "workstream-classification.json"
LAYOUT_NAME = "workstream-layout.json"
SAVE_BRANCH = "main"  # edits only go live from here, so refuse to publish elsewhere
MAX_BODY = 2 * 1024 * 1024

# Root-level files the dashboard fetches; everything else outside workstream/ is off limits.
ROOT_JSON = {
    "open-prs.json", "open-issues.json", "activity.json", "workstream-archive.json",
    CLASSIFICATION_NAME, LAYOUT_NAME,
}


def make_handler(repo_root, port, token):
    root = Path(repo_root).resolve()
    allowed_hosts = {f"localhost:{port}", f"127.0.0.1:{port}", f"[::1]:{port}"}
    allowed_origins = {f"http://{h}" for h in allowed_hosts}

    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(root), **kwargs)

        def log_message(self, fmt, *args):
            sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

        # -- responses ------------------------------------------------------
        def _send_json(self, status, payload):
            body = json.dumps(payload).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            self.wfile.write(body)

        def _refuse(self, status, message):
            self._send_json(status, {"ok": False, "error": message})

        # -- request gating -------------------------------------------------
        def _host_ok(self):
            return self.headers.get("Host", "").lower() in allowed_hosts

        def _path_allowed(self):
            """Static allowlist: the dashboard itself plus its JSON inputs."""
            path = self.path.split("?", 1)[0].split("#", 1)[0]
            if "\\" in path or "//" in path.lstrip("/"):
                return False
            parts = [p for p in path.split("/") if p]
            if any(p in (".", "..") or p.startswith(".") for p in parts):
                return False
            if not parts:
                return True  # "/" -> handled below as a redirect
            if parts[0] == "workstream":
                return True
            return len(parts) == 1 and parts[0] in ROOT_JSON

        def do_GET(self):
            if not self._host_ok():
                self._refuse(403, "bad host")
                return
            if self.path == "/api/health":
                # Same-origin only (no CORS headers): this is how the dashboard learns the token.
                self._send_json(200, {"ok": True, "token": token})
                return
            if self.path.split("?", 1)[0] == "/":
                self.send_response(302)
                self.send_header("Location", "/workstream/")
                self.end_headers()
                return
            if not self._path_allowed():
                self._refuse(404, "not found")
                return
            super().do_GET()

        def do_HEAD(self):
            if not self._host_ok() or not self._path_allowed():
                self._refuse(404, "not found")
                return
            super().do_HEAD()

        def do_OPTIONS(self):
            # No preflight is ever approved, so browsers block cross-origin non-simple requests.
            self._refuse(405, "method not allowed")

        def do_POST(self):
            if not self._host_ok():
                self._refuse(403, "bad host")
                return
            if self.path != "/api/save":
                self._refuse(404, "not found")
                return
            origin = self.headers.get("Origin")
            if origin is not None and origin.lower() not in allowed_origins:
                self._refuse(403, "bad origin")
                return
            if self.headers.get("Content-Type", "").split(";")[0].strip().lower() != "application/json":
                self._refuse(415, "content type must be application/json")
                return
            if not hmac.compare_digest(self.headers.get("X-Workstream-Token", ""), token):
                self._refuse(403, "missing or bad token")
                return

            try:
                length = int(self.headers.get("Content-Length", 0))
                if not 0 < length <= MAX_BODY:
                    raise ValueError("body must be 1 byte to 2 MiB")
                payload = json.loads(self.rfile.read(length))
            except (ValueError, json.JSONDecodeError) as e:
                self._refuse(400, f"bad request body: {e}")
                return

            classification = payload.get("classification") if isinstance(payload, dict) else None
            layout = payload.get("layout") if isinstance(payload, dict) else None
            if not isinstance(classification, dict) or not isinstance(layout, dict):
                self._refuse(400, "expected {classification: {...}, layout: {...}}")
                return
            self._save_and_publish(classification, layout)

        # -- publishing -----------------------------------------------------
        def _git(self, *args, check=True):
            return subprocess.run(["git", *args], cwd=root, check=check, capture_output=True, text=True)

        def _save_and_publish(self, classification, layout):
            files = [CLASSIFICATION_NAME, LAYOUT_NAME]
            try:
                branch = self._git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
                if branch != SAVE_BRANCH:
                    self._refuse(409, f"refusing to publish from '{branch}'; edits only go live from '{SAVE_BRANCH}'")
                    return
                ahead = self._git("rev-list", "--count", "@{u}..HEAD").stdout.strip()
                if ahead != "0":
                    self._refuse(409, f"{ahead} local commit(s) are not pushed yet; push or review them first so they don't ride along")
                    return

                (root / CLASSIFICATION_NAME).write_text(json.dumps(classification, indent=2, sort_keys=True) + "\n", encoding="utf-8")
                (root / LAYOUT_NAME).write_text(json.dumps(layout, indent=2) + "\n", encoding="utf-8")

                self._git("add", "--", *files)
                if self._git("diff", "--staged", "--quiet", "--", *files, check=False).returncode == 0:
                    self._send_json(200, {"ok": True, "committed": False, "message": "no changes to commit"})
                    return
                # Pathspec commit: only these two files, even if other things are staged.
                self._git("commit", "-s", "-m", "workstream: update annotations/layout", "--", *files)
                self._git("push", "origin", f"HEAD:{SAVE_BRANCH}")
                sha = self._git("rev-parse", "--short", "HEAD").stdout.strip()
                self._send_json(200, {"ok": True, "committed": True, "sha": sha})
            except subprocess.CalledProcessError as e:
                self._send_json(500, {"ok": False, "error": f"git command failed: {' '.join(e.cmd)}", "stderr": e.stderr or ""})

    return Handler


def make_server(port=8420, repo_root=DEFAULT_ROOT, token=None):
    token = token or secrets.token_urlsafe(32)
    server = ThreadingHTTPServer(("localhost", port), make_handler(repo_root, port, token))
    server.token = token
    return server


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8420
    server = make_server(port)
    print(f"workstream server: http://localhost:{port}/workstream/  (repo root: {DEFAULT_ROOT})")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
