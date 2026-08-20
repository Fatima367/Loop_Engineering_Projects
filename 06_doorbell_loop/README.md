# 06 — The Doorbell Loop

**Project 6 of the Loop Engineering Series**
Difficulty: medium · Time: 45–60 min · Concepts: Event-Driven, Connector

---

## Goal

A PR gets reviewed with **no prompt typed, by nobody watching**. You open a PR, the doorbell rings, and a reviewer comments all by itself — powered by the event heartbeat.

---

## What This Project Demonstrates

- The **event-driven heartbeat** (Concept 7): a `pull_request` event is what wakes the loop — no schedule, no terminal watching
- A **connector** (Concept 10): GitHub Actions plugs your repo into the review workflow
- A **deterministic, non-AI review**: the workflow needs no Anthropic key and no opencode key — only the built-in `GITHUB_TOKEN`
- Running tests **only for the files changed in the PR**, never the whole repo
- The **re-fire**: pushing a second commit fires the workflow again through the `synchronize` event — proof the event heartbeat keeps pumping
- Completing all four heartbeats: in-session (P1), conditional (P2), scheduled (P3), and now **event-driven** (P6)

---

## Files

| File | Purpose |
|------|---------|
| `total.py` | Mock module with ONE planted bug (`sum(items[1:])` silently drops the first item). |
| `test_total.py` | The test guard — `test_total_multiple` fails against the planted bug. |
| `.github/workflows/review.yml` | The doorbell. Lives at the **repo root** (GitHub only runs workflows from the default branch's root `.github/workflows/`). Triggers on `opened` + `synchronize`. |
| `README.md` | This document. |


---

## How It Works

### 1. Plant a bug on a branch

```bash
git checkout -b bad-total
```

Edit `total.py` so it contains the planted bug:

```python
def total(items):
    return sum(items[1:])   # planted bug: silently drops the first item
```

```bash
git add 06_doorbell_loop/total.py
git commit -m "update total()"
git push -u origin bad-total
```

### 2. Open the PR — the doorbell rings

```bash
gh pr create --title "update total()" --body "Implements the new total() behaviour."
```

The moment the PR becomes valid, GitHub fires the `pull_request` **opened** event. GitHub Actions starts the `pr-review` workflow — **you did not type a single prompt**.

### 3. The workflow reviews changed files only

Inside the workflow:

1. It checks out the repo (full history).
2. It diffs `base.sha...head.sha` to find **exactly which files changed in this PR** — using the event's own SHAs, so it works even on the very first PR.
3. It runs `pytest` **only** on the changed test files (or on suites in the changed source directories). The rest of the repo is never touched.
4. It posts one clean, human-readable review comment and sets a commit status.

### 4. Push a second commit — the synchronize re-fire

```bash
echo "# tweak" >> 06_doorbell_loop/README.md
git add 06_doorbell_loop/README.md
git commit -m "tweak docs"
git push
```

The `synchronize` event fires the workflow **again**. This re-fire is the event heartbeat in action: each push = one new beat. (The `concurrency` block cancels the superseded run so the new beat always reflects the latest commit.)

### 5. Optional: fix the bug and let the review turn green

Change `return sum(items[1:])` to `return sum(items)`, commit, and push. The next `synchronize` beat runs the same tests — now passing — and posts a ✅ PASS review.

---

## What "Done" Looks Like

A review comment you never asked for appears on the PR. On the first push (with the planted bug):

```text
## 🤖 Automated PR Review

Triggered by the pull_request opened / synchronize events (the PR doorbell).
No prompt was typed and nobody watched the run.

### Files changed in this PR
06_doorbell_loop/total.py

### ❌ Tests for changed files: FAIL

### Test output
FAILED test_total.py::test_total_single - assert 0 == 5
FAILED test_total.py::test_total_multiple - assert 5 == 6

### 🐛 Likely planted bug (heuristic)

The changed source lines below look like an off-by-one / dropped-first-element pattern:

+    return sum(items[1:])   # planted bug: silently drops the first item

If the test output shows an assertion like assert total([1, 2, 3]) == 6 failing
with 5 == 6, this is the planted bug: sum(items[1:]) silently drops the first item.
```


---

## Key Commands

| Command | What it does |
|---------|--------------|
| `git checkout -b <branch>` | Start the PR branch |
| `gh pr create --title "..." --body "..."` | Open the PR — rings the doorbell |
| `git push` (after a new commit) | Fires the `synchronize` event — one more beat |
| `gh pr view` | Read the review comment GitHub posted |
| `git diff base...head --name-only` | The exact "changed files only" logic the workflow uses |

---

## Concept: Event-Driven Loop + Connector

The first three projects gave you three heartbeats: **in-session** (`/loop`, P1), **conditional** (`/goal`, P2), and **scheduled** (`/schedule`/cron, P3). This project adds the fourth:

```
┌──────────────┐      ┌──────────────────────┐      ┌──────────────────┐
│ PR opened or │ ───► │ GitHub Actions fires  │ ───► │ Review comment   │
│ push lands   │  on: │ the pr-review workflow│      │ posted on the PR │
│ (event)      │  PR  │ (the connector)       │      │ (the response)   │
└──────────────┘      └──────────────────────┘      └──────────────────┘
        ▲                                                        │
        └────────────── next synchronize = next beat ────────────┘
```

The **event** replaces the clock: instead of asking "is it time yet?", the loop asks "did something happen?" — and it happens instantly, the moment a PR opens or a new commit lands.

The **connector** is the plumbing that makes the event reach your code: GitHub Actions reads `.github/workflows/review.yml` on the default branch and subscribes it to the `pull_request` event. No server, no cron, no API key.

---

## Completion Criteria

✅ A PR with a planted bug gets an unasked-for review
✅ The review flags the planted bug (`sum(items[1:])` → `assert 5 == 6`)
✅ Tests run for **changed files only** — the rest of the repo is untouched
✅ Pushing a second commit re-fires the review via the `synchronize` event
✅ No prompt was typed, nobody watched
✅ The review needs no Anthropic key and no opencode key — `GITHUB_TOKEN` only

---

## Skills Used

| Artifact | Where |
|----------|-------|
| `pr-review` GitHub workflow | `.github/workflows/review.yml` (repo root) |
| `actions/github-script` | Posts the comment + commit status |

---

*Part of the [Loop Engineering Projects](../) series — learning Claude Code's `/loop` skill through practical examples.*