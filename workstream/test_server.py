#!/usr/bin/env python3
"""Tests for workstream/server.py's access controls and publish safety.

Run: python3 -I workstream/test_server.py   (any cwd)
Spins the real server in-process on a loopback port against a throwaway git repo
with a local bare remote, so nothing touches the real repo or network.
"""
import http.client
import json
import socket
import subprocess
import sys
import tempfile
import threading
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import server  # noqa: E402


def free_port():
    with socket.socket() as s:
        s.bind(("localhost", 0))
        return s.getsockname()[1]


def git(cwd, *args):
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


class ServerTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        base = Path(self.tmp.name)
        remote, self.repo = base / "remote.git", base / "repo"
        git(base, "init", "-q", "--bare", "-b", "main", str(remote))
        git(base, "clone", "-q", str(remote), str(self.repo))
        git(self.repo, "config", "user.name", "Test")
        git(self.repo, "config", "user.email", "test@example.com")
        git(self.repo, "checkout", "-q", "-b", "main")
        (self.repo / "workstream").mkdir()
        (self.repo / "workstream" / "index.html").write_text("<html>dash</html>")
        (self.repo / "secret.txt").write_text("nope")
        for name in server.ROOT_JSON:
            (self.repo / name).write_text("{}\n")
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", "init")
        git(self.repo, "push", "-q", "-u", "origin", "main")

        self.port = free_port()
        self.srv = server.make_server(self.port, self.repo, token="tok123")
        threading.Thread(target=self.srv.serve_forever, daemon=True).start()

    def tearDown(self):
        self.srv.shutdown()
        self.srv.server_close()
        self.tmp.cleanup()

    def req(self, method, path, body=None, headers=None, host=None):
        c = http.client.HTTPConnection("localhost", self.port, timeout=10)
        h = {"Host": host or f"localhost:{self.port}"}
        h.update(headers or {})
        c.request(method, path, body=body, headers=h)
        r = c.getresponse()
        data = r.read()
        c.close()
        return r, data

    def save(self, headers=None, payload=None):
        h = {"Content-Type": "application/json", "X-Workstream-Token": "tok123"}
        h.update(headers or {})
        body = json.dumps(payload or {"classification": {"a": {"workstream": "OADP", "note": "n"}}, "layout": {"laneOrder": ["OADP"]}})
        return self.req("POST", "/api/save", body, h)

    # -- read side ----------------------------------------------------------
    def test_health_gives_token_and_no_cors(self):
        r, data = self.req("GET", "/api/health")
        self.assertEqual(r.status, 200)
        self.assertEqual(json.loads(data)["token"], "tok123")
        self.assertIsNone(r.getheader("Access-Control-Allow-Origin"))

    def test_foreign_host_rejected(self):  # DNS rebinding
        for path in ("/api/health", "/workstream/index.html"):
            r, _ = self.req("GET", path, host="evil.example")
            self.assertEqual(r.status, 403, path)

    def test_only_dashboard_files_served(self):
        self.assertEqual(self.req("GET", "/workstream/index.html")[0].status, 200)
        self.assertEqual(self.req("GET", "/open-prs.json")[0].status, 200)
        for path in ("/.git/config", "/.git/HEAD", "/secret.txt", "/workstream/../secret.txt", "/%2e%2e/secret.txt", "/workstream/.hidden"):
            self.assertEqual(self.req("GET", path)[0].status, 404, path)

    def test_options_never_approved(self):
        r, _ = self.req("OPTIONS", "/api/save", headers={"Origin": "http://evil.example", "Access-Control-Request-Method": "POST"})
        self.assertEqual(r.status, 405)
        self.assertIsNone(r.getheader("Access-Control-Allow-Origin"))

    # -- write side ---------------------------------------------------------
    def test_cross_origin_post_rejected(self):
        r, _ = self.save({"Origin": "http://evil.example"})
        self.assertEqual(r.status, 403)

    def test_simple_request_content_type_rejected(self):  # the no-preflight attack shape
        r, _ = self.save({"Content-Type": "text/plain"})
        self.assertEqual(r.status, 415)

    def test_token_required(self):
        self.assertEqual(self.save({"X-Workstream-Token": ""})[0].status, 403)
        self.assertEqual(self.save({"X-Workstream-Token": "wrong"})[0].status, 403)
        self.assertEqual(git(self.repo, "rev-list", "--count", "@{u}..HEAD"), "0")

    def test_foreign_host_post_rejected(self):
        r, _ = self.req("POST", "/api/save", "{}", {"Content-Type": "application/json", "X-Workstream-Token": "tok123"}, host="evil.example")
        self.assertEqual(r.status, 403)

    def test_save_commits_only_its_two_files_and_pushes(self):
        (self.repo / "unrelated.txt").write_text("staged by someone else")
        git(self.repo, "add", "unrelated.txt")
        r, data = self.save({"Origin": f"http://localhost:{self.port}"})
        self.assertEqual(r.status, 200, data)
        self.assertTrue(json.loads(data)["committed"])
        changed = git(self.repo, "show", "--name-only", "--format=", "HEAD").splitlines()
        self.assertEqual(sorted(changed), [server.CLASSIFICATION_NAME, server.LAYOUT_NAME])
        self.assertIn("Signed-off-by:", git(self.repo, "log", "-1", "--format=%B"))
        self.assertIn("unrelated.txt", git(self.repo, "diff", "--staged", "--name-only"))  # still staged, not committed
        self.assertEqual(git(self.repo, "rev-list", "--count", "@{u}..HEAD"), "0")  # pushed

    def test_refuses_off_main_branch(self):
        git(self.repo, "checkout", "-q", "-b", "feature")
        r, _ = self.save()
        self.assertEqual(r.status, 409)

    def test_refuses_when_unpushed_commits_would_ride_along(self):
        (self.repo / "wip.txt").write_text("wip")
        git(self.repo, "add", "wip.txt")
        git(self.repo, "commit", "-q", "-m", "unreviewed local work")
        r, _ = self.save()
        self.assertEqual(r.status, 409)
        self.assertEqual(git(self.repo, "rev-list", "--count", "@{u}..HEAD"), "1")

    def test_oversized_body_rejected(self):
        # Declare an oversized body; the server must refuse on the header without reading it.
        r, _ = self.req("POST", "/api/save", "{}", {"Content-Type": "application/json", "X-Workstream-Token": "tok123",
                                                   "Content-Length": str(server.MAX_BODY + 1)})
        self.assertEqual(r.status, 400)


if __name__ == "__main__":
    unittest.main()
