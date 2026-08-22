# 08 — Your Own Daily Loop (Capstone)

**Project 8 of the Loop Engineering Series**
Difficulty: capstone · Time: 2–4 hrs · Concept: The Full Six-Part Loop

---

## Goal

Build the complete six-part loop on a real, boring, recurring chore — trusted enough to run unattended.

---

## What This Project Demonstrates

- Wiring **all six parts** of a loop into a single workflow: heartbeat, worktree, skill, maker-checker, connector, and spine
- Writing a **deterministic checker** (`todo_sweep.py`) that decides whether there is new work — the agent doesn't guess
- Using a **skill** (`SKILL.md`) to encode the chore's steps once, so every run follows the same instructions
- Running a **maker-checker** pattern: the implementer does the work, a reviewer agent grades it, and a PR opens only on PASS
- Updating a **spine** (`progress.md`) every run — the run history lives in one file that the next run reads before starting
- Driving the loop **by hand** on a free-tier budget instead of a live schedule, while proving the same six-part shape holds

---

## Files

| File | Purpose |
|------|---------|
| `todo_sweep.py` | The deterministic checker — scans `sample_code/` for TODO/FIXME comments older than 30 days, appends new candidates to `progress.md`, and exits non-zero when there is work to do. |
| `run_daily_pass.sh` | Bash wrapper that drives one pass by hand: runs the checker, logs timestamps to `run_log.txt`, and propagates the exit code. |
| `progress.md` | The spine — a dated log of every run. Each entry records what was found (or not) and whether the reviewer passed or failed the diff. |
| `run_log.txt` | Raw timestamps of each manual pass (start/end). Proves the loop ran multiple times. |
| `output.md` | Full transcript of a live Claude session running the loop end-to-end: checker → fix → reviewer → PR → spine update. |
| `sample_code/stale_module.py` | Test fixture — a module with old TODO/FIXME comments (committed with a backdated `--date`) so the checker flags them. |
| `sample_code/fresh_module.py` | Test fixture — a module with a recent TODO that the checker correctly ignores (< 30 days). |
| `.claude/skills/todo-sweep/SKILL.md` | The skill — step-by-step instructions for the chore, invoked by name each run. |
| `.claude/agents/reviewer.md` | The reviewer agent — grades a diff as PASS or FAIL. Never edits files. |

---

## How It Works

### The Six Parts

| Part | What it is here | Where it lives |
|------|----------------|----------------|
| **Heartbeat** | A deterministic checker (`todo_sweep.py`) that runs on a schedule (or by hand) and decides if there is work | `todo_sweep.py` + `run_daily_pass.sh` |
| **Worktree** | Each run isolates its edits in a git worktree so one pass can't clobber another | Branch `fix/stale-todo-fixme` (created per run) |
| **Skill** | The chore's steps written once in `SKILL.md`, so the agent follows the same procedure every time | `.claude/skills/todo-sweep/SKILL.md` |
| **Maker-checker** | The implementer does the sweep and fix; a reviewer agent grades the diff before anything ships | `.claude/agents/reviewer.md` |
| **Connector** | On PASS, the loop opens a real PR on GitHub — not a dry run | `gh pr create` in the output transcript |
| **Spine** | `progress.md` is updated every run and read every run — the loop's memory across days | `progress.md` |

### 1. The Checker (`todo_sweep.py`)

The checker is a plain Python script — no agent needed to run it. It:

1. Walks `sample_code/` for `.py` files containing `# TODO:` or `# FIXME:` comments
2. Determines staleness from each file's git commit date (falling back to mtime), using a 30-day threshold
3. Compares found items against what is already logged in `progress.md`
4. Appends a new dated entry to `progress.md` with any newly discovered stale candidates
5. Exits **0** (nothing to do) or **1** (new work found — hand off to the maker-checker)

This is the key insight: a **command** decides whether there is work, not the agent. The agent only acts when the checker says there is something to do.

### 2. The Skill (`SKILL.md`)

The skill encodes the chore's steps once:

```
1. Run python todo_sweep.py
2. Read the candidates. For each stale item, make the smallest sensible change.
3. Do not touch test files.
4. Have the reviewer agent grade the diff — open a PR only on PASS.
5. Confirm progress.md picked up the run, and stop after 1 review round.
```

Every run invokes the same skill. The agent doesn't reinvent the procedure each time.

### 3. The Maker-Checker

- **Maker**: The agent runs the checker, reads the candidates, makes the smallest fix, and stages the diff.
- **Checker (reviewer)**: A separate agent (`reviewer.md`) grades the diff. It checks that tests pass, the fix is minimal, and no test files were touched. It replies **PASS** or **FAIL** with reasons.
- A PR is opened **only on PASS**. On FAIL, the loop stops and logs the failure to `progress.md`.

### 4. The Connector

On PASS, the loop runs:

```bash
git push -u origin fix/stale-todo-fixme
gh pr create --base master --head fix/stale-todo-fixme
```

This opens a real, mergeable PR on GitHub — not a simulation. In the live run, this produced [PR #5](https://github.com/Fatima367/Loop_Engineering_Projects/pull/5).

### 5. The Spine (`progress.md`)

Every run appends a timestamped section to `progress.md`. The next run reads it first to avoid re-reporting the same stale items. The spine is the loop's memory across days.

Example entries:

```
## 2026-08-19 09:00:00
- sample_code/stale_module.py:5 — TODO: implement caching
- sample_code/stale_module.py:12 — FIXME: handle edge case

## 2026-08-22 12:50:00
No new stale items. Sweep clean.
- reviewer: PASS — PR #5 opened
```

---

## Running It

### By Hand (Free-Tier Version)

Run the daily pass 3–4 times over a few days to prove the six-part shape:

```bash
# One pass
./run_daily_pass.sh

# Four fake "days" in sequence
for i in 1 2 3 4; do ./run_daily_pass.sh; sleep 2; done
```

Each pass runs the checker, logs timestamps, and the agent follows the skill to do the rest.

### Full Loop via Claude Code

Invoke the skill directly:

```
/todo-sweep
```

Or run the goal prompt:

```
Following the todo-sweep skill, do today's pass, have the reviewer grade it, open a PR only on PASS, and update progress.md. Stop after 1 review round.
```

This triggers the full chain: checker → fix → reviewer → PR → spine update.

---

## What "Done" Looks Like

```
● Running today's sweep.
  ⎿  === todo_sweep pass @ 2026-08-22 12:50:52 ===
     No new stale TODO/FIXME comments to report (or already logged). Nothing to do.

● Sweep is clean — no stale items remain. I'll update progress.md for today.

  ⎿  Edit progress.md — appended "## 2026-08-22 12:50:00" entry

● Reviewer returned PASS. Opening the PR now.

  ⎿  Bash: git push -u origin fix/stale-todo-fixme → SUCCESS
     Bash: gh pr create --base master --head fix/stale-todo-fixme → PR #5 opened

● All steps complete:
  ┌──────────────────┬─────────────────────────────────────────┐
  │       Step       │                Result                   │
  ├──────────────────┼─────────────────────────────────────────┤
  │ todo_sweep.py    │ No new stale TODO/FIXME — sweep clean   │
  │ Reviewer grade   │ PASS                                    │
  │ PR opened        │ #5 — MERGEABLE                          │
  │ progress.md      │ 2026-08-22 entry + PR #5 recorded       │
  └──────────────────┴─────────────────────────────────────────┘

✔ Goal achieved (9m · 1 turn)
```

---

## Key Commands

| Command | What it does |
|---------|--------------|
| `./run_daily_pass.sh` | Drive one daily pass by hand (checker + logging) |
| `python todo_sweep.py` | Run the checker alone — returns 0 (clean) or 1 (new work) |
| `/todo-sweep` | Invoke the full skill via Claude Code |
| `gh pr view 5` | Check the PR the loop opened |
| `cat progress.md` | Read the spine — the loop's run history |

---

## Concept: The Full Loop

The capstone brings together every concept from the series:

1. **Heartbeat** (Project 1) — a recurring check that decides if there is work
2. **Worktree isolation** (Project 2) — each run edits in its own branch
3. **Skill-driven execution** (Project 3) — the chore's steps are written once, not re-invented
4. **Maker-checker** (Project 5) — implementer and reviewer are separate agents with separate incentives
5. **Connector** (Project 6) — the loop talks to the real world (GitHub PRs)
6. **Spine** (Project 7) — `progress.md` is the loop's memory, read before every run

The difference between this and earlier projects: nothing here is simulated. The checker is a real script. The PR is a real PR. The spine is a real file that accumulates history across days. The loop runs unattended because you trust the **shape**, not because you watched it.

---

## Completion Criteria

✅ Deterministic checker (`todo_sweep.py`) decides whether there is work — the agent doesn't guess

✅ Skill (`SKILL.md`) encodes the chore's steps once, invoked by name every run

✅ Maker-checker pattern: implementer fixes, reviewer grades PASS/FAIL

✅ Connector: a real PR opens on GitHub only on PASS

✅ Spine (`progress.md`) is updated every run and read every run

✅ Run log (`run_log.txt`) proves the loop ran multiple times

✅ You trust what it ships because you read it, not because you stopped reading

---

## Practice Version (This Run)

This version scopes the chore small and runs by hand 3–4 times over a few days instead of via a live schedule, to prove the six-part shape without sustained cloud usage.

---

## Real Version (Requires Paid Plan)

The course's actual capstone is a live cloud Routine on a daily schedule, left running unattended for roughly a week, with every part (worktree, skill, maker-checker, connector, spine) wired into one Routine config rather than run by hand.

To see the real thing at least once:

1. **Set it up** exactly as above but as a Routine with a daily trigger
2. **Let it fire 2–3 times** on its actual schedule (not Run-now) — confirm the six parts hold together across real unattended runs
3. **Pause it** once you've confirmed the shape (the pause toggle stops the schedule without deleting the config)

You don't need a full week to learn the lesson — a few real unattended fires is enough to feel the difference from the hand-run version.

---

*Part of the [Loop Engineering Projects](../) series — learning Claude Code's `/loop` skill through practical examples.*
