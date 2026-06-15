# LLM Policy

This document describes how I, Tiger Kaovilai ([@kaovilai](https://github.com/kaovilai)), use AI/LLM tooling when contributing to other repositories. It exists so maintainers know what to expect from me before, during, and after a contribution.

## Declaration

- Some of my contributions (code, commits, and pull requests) may be **co-authored with AI**.
- Some of my responses (issue comments, review replies, and discussions) may be **generated with AI**.

When AI co-authors a commit, it is attributed via a `Co-authored-by:` trailer. When a response is AI-generated, I mark it inline, for example:

> [!NOTE]
> Responses generated with Claude

If a repository prohibits the `Co-authored-by:` trailer, I will omit it. In those cases the repository often requires the pull request description to declare which AI was used, so the declaration will appear in the pull request description itself instead.

## Commitment to transparency

I am committed to being transparent about my use of AI:

- **Attribution.** AI-assisted commits carry a `Co-authored-by:` trailer, and AI-generated comments/replies carry a visible note (see above).
- **Disclosure on request.** If a maintainer asks whether AI was involved in a given contribution, I will answer honestly.
- **Sign-off and ownership.** I sign my commits (`git commit -s`, DCO) and take full responsibility for everything I submit, regardless of how it was drafted.

## Human review

Every pull request and reply I send — **including those that carry a note indicating an AI-generated response** — is thoroughly reviewed by me before it goes out. The AI note appears on *every* comment my AI generates, even ones I have manually reviewed; it signals *how the draft was produced*, not that the content went out unreviewed. I read, verify, and stand behind each contribution.

This level of disclosure goes beyond what many other people do when using AI. Plenty of contributors use AI without any attribution at all; my aim is to be more transparent than the norm, not less.

## Exception: agentic workflows on my own repositories

The human-review commitment above applies to my contributions to **other people's repositories**. I run an exception in **my own repositories** where I am experimenting with **agentic workflows** — for example [GitHub Agentic Workflows (GH-AW)](https://github.com/githubnext/gh-aw). GH-AW is the current experiment, but this exception applies equally to **any other agentic workflow tooling I may adopt in the future**, not just GH-AW.

- This exception is limited to **repositories I own** (e.g. under [`github.com/kaovilai`](https://github.com/kaovilai)). It does **not** apply to repositories owned by others that I contribute to — those always receive the full human review described above.
- Within these experiments, AI agents may open issues, commits, and pull requests **autonomously**, and some of that output may be merged with **lighter human review than I apply elsewhere** — that is the point of the experiment.
- AI-produced contributions from these workflows remain attributed (via `Co-authored-by:` trailers and/or AI-generated notes) so it stays clear which work came from an agent.
- I remain responsible for everything that lands in my own repositories.

## Respecting repository policies

I respect each repository's own rules on AI usage.

- If a repository publishes an `LLM_POLICY` (or equivalent) that **prohibits any meaningful use of AI**, I will most likely **not contribute** to that repository, rather than attempt to work around the policy.
- Where a repository permits AI use under certain conditions (disclosure, attribution, review, etc.), I will follow those conditions.

If you maintain a repository and have questions about how I work, please reach out before or during review — I'm happy to clarify.
