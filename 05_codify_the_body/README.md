# 05 — Codify the Body

**Project 5 of the Loop Engineering Series**
Difficulty: medium–hard · Time: 1–1.5 hrs · Concepts: Dynamic Workflows, 8, 11

---

## Goal

Turn Project 4's manual orchestration into one re-runnable unit, then prove it has no memory — it is an engine, not a loop.

---

## What This Project Demonstrates

- Codifying a fix-and-review pattern into a **dynamic workflow** (one command runs everything)
- Using **parallel worktrees** so agents never step on each other's diffs
- Proving the workflow **remembers nothing** between runs — no accumulated state, no learning
- Naming the two missing pieces that would turn an engine into a **loop**: a heartbeat and a progress file

---

## Files

| File | Purpose |
|------|---------|
| `math_utils.py` | The buggy source — three functions, each with a planted defect. |
| `test_math_utils.py` | Seven tests: 6 fail against the bugs, 1 passes. Never modified. |
| `issues/issue-a.md` | Issue A: off-by-one in `total()` when list has 1 item. |
| `issues/issue-b.md` | Issue B: `is_even()` logic inverted. |
| `issues/issue-c.md` | Issue C: `divide()` truncates with integer division. |
| `.claude/skills/fix-steps/SKILL.md` | Skill loaded by every fix agent — the four-step process. |
| `.claude/agents/reviewer.md` | Reviewer agent definition — grades a diff, never edits. |
| `output.md` | Full transcript of the workflow run. |

---

## The Bugs

```python
def total(items):
    return sum(items) - 1      # Issue A: off-by-one

def is_even(n):
    return n % 2 == 1          # Issue B: logic inverted

def divide(a, b):
    return a // b              # Issue C: integer division
```

---

## How It Works

### 1. Confirm the failures

```bash
cd 05_codify_the_body
python -m pytest test_math_utils.py -v
```

Six tests fail, one passes. This is the baseline.

### 2. Describe the workflow in plain words

In Claude Code, you say:

> Use a workflow to draft fixes for issues A, B, and C in parallel worktrees, and have a reviewer subagent grade each one.

Claude writes and runs the orchestration script itself — no step-by-step prompting from you.

### 3. What the workflow does internally

```
Phase 1 — Fix (3 agents in parallel, each in its own worktree)
  fix:A  →  removes "- 1" from total()
  fix:B  →  flips "==" to "==" in is_even()
  fix:C  →  swaps "//" for "/" in divide()

Phase 2 — Review (3 agents, one per fix)
  reviewer  →  runs tests, checks diff is minimal, grades PASS or FAIL
```

Each fix agent follows the **fix-steps** skill:
1. Reproduce the bug by running the failing test first.
2. Make the smallest possible change that fixes it.
3. Do not touch test files.
4. Run the full test suite before reporting done.

Each reviewer is the **reviewer** agent — it reads the diff, runs the tests, and replies with exactly `PASS` or `FAIL` plus one line of reasons.

### 4. Save the workflow

From the `/workflows` view, press `s` to save it as a slash command:

```
/fix-and-grade-batch
```

Now it is one command. Run it again anytime — same issues, same verdicts, no accumulated knowledge.

### 5. Prove it has no memory

Start a fresh Claude Code session. Run the workflow again. It produces identical results — no reference to prior fixes unless read from a file. The workflow is stateless between runs.

---

## What "Done" Looks Like

```
● Workflow complete — all 6 agents finished. Here are the results:

Phase 1 — Fixes (parallel worktrees)

  │ Issue │ Fix                                                        │ Target tests          │
  │ A     │ Removed - 1 from return sum(items) - 1 → sum(items)       │ 3/3 total() pass      │
  │ B     │ Changed n % 2 == 1 → n % 2 == 0 in is_even()             │ 2/2 is_even pass      │
  │ C     │ Changed a // b → a / b in divide()                        │ 2/2 divide pass       │

Phase 2 — Reviews (parallel grading)

  │ Fix   │ Grade │ Verdict                                            │
  │ A     │ PASS  │ Correct minimal change. 3 total() tests pass.      │
  │ B     │ PASS  │ Correct minimal change. 2 is_even tests pass.      │
  │ C     │ PASS  │ Correct minimal change. 2 divide tests pass.       │
```

---

## Key Commands

| Command | What it does |
|---------|--------------|
| `Workflow({...})` | Run a dynamic workflow inline — Claude writes the script |
| `/workflows` | View, save, or re-run dynamic workflows |
| `/fix-and-grade-batch` | Re-run the saved workflow as a slash command |
| `python -m pytest test_math_utils.py -v` | Run the test suite to confirm pass/fail |

---

## Concept: Engine vs. Loop

This workflow is an **engine**: it runs once, produces a result, and forgets everything. It has no state between runs.

To become a **loop**, it would need two things:

1. **A heartbeat** — a recurring trigger (CronCreate, CI schedule, file-watcher) that fires the workflow at regular intervals.
2. **A progress file** — a persistent log its agents write to after each run, so the next run can see what was already tried and what passed.

Without those two pieces, you are running the same engine over and over. With them, you have a loop that accumulates knowledge and self-improves.

The engine is the body. The heartbeat and the progress file are what make it alive.

---

## Completion Criteria

✅ One command runs the entire draft-and-review body with no step-by-step prompting

✅ Three fixes applied in parallel worktrees with no conflicts

✅ Three reviewer agents grade each fix independently (PASS/FAIL)

✅ Workflow is saved and re-runnable via `/fix-and-grade-batch`

✅ Fresh session confirms the workflow remembers nothing from its last run

✅ You can name the two missing pieces: a heartbeat and a progress file

---

## Skills Used

| Skill | Where |
|-------|-------|
| `fix-steps` | Loaded by every fix agent — the four-step bug-fixing process |
| `reviewer` agent | Grades diffs — reads, runs tests, replies PASS or FAIL |

---

*Part of the [Loop Engineering Projects](../) series — learning Claude Code's `/loop` skill through practical examples.*
