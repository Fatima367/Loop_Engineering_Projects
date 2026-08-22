# 08 — Your Own Daily Loop (Capstone)

**Project 8 of the Loop Engineering Series**
Difficulty: capstone · Time: 2–4 hrs · Concepts: All Six Parts

---

## Goal

Build the **full six-part loop** on a real, boring, recurring chore — trusted enough to run unattended. The chore for this capstone: **flag TODO/FIXME comments in the repo that are older than 30 days.**

---

## What This Project Demonstrates

Every loop needs six parts. This project wires all of them into one loop:

| # | Part | Where in this project |
|---|------|------------------------|
| 1 | **Heartbeat** | What wakes the loop — here, a scheduled `on: schedule` / hand-run pass |
| 2 | **Worktree** | Each run edits in its own checkout (branch or worktree) — main stays clean |
| 3 | **Skill** | `todo-sweep` SKILL.md codifies the chore's steps |
| 4 | **Maker-checker** | Implementer drafts · reviewer grades · PR only on PASS |
| 5 | **Connector** | An actual PR (or a summary in `progress.md`) reaches the outside world |
| 6 | **Spine** | `progress.md` — updated every run, read every run |

Plus **budget guards**: a fixed hand-run cadence, a 1-review-round cap, and a stop clause — so nothing ever runs away on the free tier.

---

## Files

| File | Purpose |
|------|---------|
| `todo_sweep.py` | **The checker.** Deterministic: finds TODO/FIXME in `sample_code/` older than 30 days, appends new ones to `progress.md`, exit 1 if there's new work. |
| `run_daily_pass.sh` | Hand-run driver for the loop body (free-tier version of a daily schedule). |
| `sample_code/stale_module.py` | Deliberately stale TODO + FIXME (commit with an old `--date` so it's flagged). |
| `sample_code/fresh_module.py` | Recent TODO — correctly **not** flagged by the 30-day window. |
| `progress.md` | The spine — dated entries proving the loop builds on its own memory. |
| `.claude/skills/todo-sweep/SKILL.md` | The chore's skill (Claude Code). |
| `.claude/agents/reviewer.md` | The reviewer (Claude Code) — grades the diff, replies PASS/FAIL. |
| `.opencode/skills/todo-sweep/SKILL.md` · `.opencode/agents/reviewer.md` | The same for opencode. |
| `README.md` · `output.md` | This doc · template transcript. |

---

## How It Works

### 1. Make the mock data believably stale

```bash
git add sample_code/stale_module.py
git commit -m "add stale module with old TODO/FIXME" --date "2026-07-01T09:00:00"
GIT_COMMITTER_DATE="2026-07-01T09:00:00" git commit --amend --no-edit
```

Now `stale_module.py` is older than 30 days, and `todo_sweep.py` will trust the git date (not your mtime). `fresh_module.py` stays recent, so its TODO is ignored — proving the window logic.

### 2. Run the checker once (the maker's first step)

```bash
python todo_sweep.py
```

A **command** — not the agent — decides if there's work. New stale candidates get logged to `progress.md` and the exit code says "hand to the reviewer."

### 3. Run the full loop on the Claude Code path

```
/goal Following the todo-sweep skill, do today's pass, have the reviewer grade it, open a PR only on PASS, and update progress.md. Stop after 1 review round.
```

On the opencode path:

```bash
opencode run "using the todo-sweep skill, run python todo_sweep.py, review the stale items, fix them, have @reviewer grade the diff, open a PR only on PASS"
```

### 4. Repeat by hand for a few "days"

Free-tier scope-down: a real daily cloud schedule burns quota fast. Instead run the same body 3–4 times over a few days:

```bash
for i in 1 2 3 4; do ./run_daily_pass.sh; sleep 2; done
```

Each "day" is one beat of the heartbeat — you are the scheduled trigger. The task: **flag TODO/FIXME comments older than 30 days, fix them via maker-checker, open a PR on PASS, update `progress.md`.**

### 5. Trust it because you read it

At the end, read `progress.md`. You should trust what the loop shipped *because you read it*, not because you stopped reading. If you don't understand its changes, slow the loop down.

---

## What "Done" Looks Like

```
=== todo_sweep pass @ 2026-08-20 09:00:01 ===
Found 2 new stale TODO/FIXME (older than 30 days):
  - sample_code/stale_module.py:9  [50d] TODO: add input validation here
  - sample_code/stale_module.py:16 [50d] FIXME: off-by-one in the retry loop below

Logged 2 new entries to progress.md.

[reviewer] PASS — diff fixes both stale comments, no test files touched.

PR opened: fix stale TODO/FIXME in sample_code

[second run] No new stale TODO/FIXME comments to report (or already logged).
```

*(Paste your real per-day output after running.)*

```
{{PASTE_RUN_1}}
{{PASTE_RUN_2}}
{{PASTE_RUN_3}}
```

---

## Key Commands

| Command | What it does |
|---------|--------------|
| `python todo_sweep.py` | The checker — finds stale TODO/FIXME, writes the spine |
| `./run_daily_pass.sh` | One hand-run beat of the loop |
| `/goal <prompt>` | Claude Code loop with a self-written "stop after" clause |
| `opencode run "<prompt>"` | OpenCode equivalent |
| `@reviewer` | Grade the diff (PASS/FAIL) |
| `git worktree add <path> -b <branch>` | Isolate a run's edits (part 2: worktree) |

---

## Real Version (paid tier)

Set it all up as one **live cloud Routine** on a **daily** schedule: repo attached, `.claude/skills/todo-sweep/` and `.claude/agents/reviewer.md` committed, **Allow unrestricted branch pushes off** (pushes only to `claude/*`), the spine = `progress.md` in the repo. Let it fire **2–3 times on its actual schedule** (not Run-now), read the results, then pause the schedule once the six parts hold together. You don't need a full week to learn the lesson.

---

## Completion Criteria

✅ All six parts (heartbeat, worktree, skill, maker-checker, connector, spine) are present and named
✅ A command (`todo_sweep.py`), not the agent, decides when there's work
✅ Old TODO/FIXME get flagged; recent ones don't
✅ The maker-checker gate blocks a PR until the reviewer says PASS
✅ `progress.md` is read every run and updated every run (no repeated entries)
✅ It has run by hand multiple times and you read — and understood — what it shipped

---

*Part of the [Loop Engineering Projects](../) series — learning Claude Code's `/loop` skill through practical examples.*