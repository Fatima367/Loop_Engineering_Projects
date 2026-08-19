# 04 — A Fix Loop with a Real Checker

**Project 4 of the Loop Engineering Series**
Difficulty: medium–hard · Time: 1–2 hrs · Concepts: Worktree, Skill, Maker-Checker

---

## Goal

Build an implementer-reviewer loop: a fix gets drafted in an isolated worktree, a separate reviewer grades it, and a PR opens only on PASS.

---

## What This Project Demonstrates

- Using a **worktree** (Concept 8) to draft a fix in isolation without touching the main checkout
- Writing a **skill** (Concept 9) that codifies the fix steps into repeatable instructions
- Running a **maker-checker** loop (Concept 11) where the implementer drafts and the reviewer grades independently
- Opening a PR only when the reviewer returns **PASS** — a checker that approves everything is no checker

---

## Files

| File | Purpose |
|------|---------|
| `math_utils.py` | Contains the buggy `divide()` function (uses `//` instead of `/`) and a planted bad fix `division()` to test the checker |
| `test_math_utils.py` | Tests both functions: `divide(7, 2) == 3.5` and `division(7, 2) == 3.5` |
| `.claude/skills/fix-steps/SKILL.md` | Skill that defines the 4-step fix process |
| `.claude/agents/reviewer.md` | Reviewer agent that grades diffs and replies PASS or FAIL |
| `output.md` | Full transcript of the loop: bug reproduction, fix, reviewer grading, PR creation, and the bad-fix check |

---

## How It Works

### 1. The bug

```python
def divide(a, b):
    return a // b   # bug: integer division silently truncates
```

`divide(7, 2)` returns `3` instead of `3.5`. The fix: change `//` to `/`.

### 2. The planted bad fix

```python
def division(a, b):
    return a / b if b != 0 else 999   # silently wrong on b==0, not a real fix
```

This looks like it works for normal inputs, but silently returns `999` on division by zero instead of raising an error. A soft checker would miss this.

### 3. The fix-steps skill

```
.claude/skills/fix-steps/SKILL.md
```

Defines four rules for the implementer:
1. Reproduce the bug by running the failing test first
2. Make the smallest possible change that fixes it
3. Do not touch test files
4. Run the full test suite before reporting done

### 4. The reviewer agent

```
.claude/agents/reviewer.md
```

A strict, read-only agent that:
- Runs the tests
- Checks the diff is the smallest possible fix
- Verifies no test files were touched
- Replies with exactly **PASS** or **FAIL** plus one line of reasons

---

## The Loop in Action

### Step 1 — Draft the fix in a worktree

```
/goal Draft a fix for the divide() bug in a new worktree using the fix-steps skill.
Have the reviewer subagent grade the diff. Open a PR only on PASS.
Stop after 3 review rounds.
```

### Step 2 — Implementer creates the fix

```bash
git worktree add .claude/worktrees/fix-divide-bug -b fix-divide-bug
cd .claude/worktrees/fix-divide-bug/04_fix_loop_with_checker

# Reproduce
python -m pytest test_math_utils.py -v   # FAIL: assert 3 == 3.5

# Fix
# Change: return a // b
# To:     return a / b

# Verify
python -m pytest test_math_utils.py -v   # PASSED
```

### Step 3 — Reviewer grades the diff

```
@reviewer grade the diff in this worktree against the spec and tests, reply PASS or FAIL
```

### Step 4 — PR opens only on PASS

```bash
gh pr create --title "fix: use true division in divide()" --body "..."
```

---

## What "Done" Looks Like

**Good fix → PASS + PR:**

```
Reviewer result: PASS
The diff is a single-character change (// to /) in math_utils.py only —
no test files touched, and the test passes.
```

**Bad fix → FAIL with reasons:**

```
Reviewer result: FAIL
The fix did not change // to / in divide(), so test_divide still fails.
It also touched test_math_utils.py and added a new division function
instead of fixing the existing one.
```

Both conditions must be true:
1. ✅ A good fix gets **PASS** and a PR
2. ✅ A planted bad fix gets **FAIL** with reasons

---

## Key Commands

| Command | What it does |
|---------|--------------|
| `/goal <prompt>` | Set a session goal with auto-check condition |
| `git worktree add <path> -b <branch>` | Create an isolated worktree for the fix |
| `/fix-steps` | Load the fix-steps skill |
| `@reviewer` | Invoke the reviewer agent to grade the diff |
| `gh pr create` | Open a pull request (only after PASS) |

---

## Concept: Maker-Checker

The **maker-checker** pattern (Concept 11) separates the person writing code from the person approving it — even when both are AI agents:

1. **Maker (implementer)** — Drafts the fix in an isolated worktree following the skill's steps
2. **Checker (reviewer)** — Grades the diff independently: runs tests, checks scope, verifies minimality
3. **Gate** — The PR only opens if the checker returns PASS; FAIL blocks the PR and gives reasons
4. **Iterate** — If FAIL, the implementer revises and resubmits for another review round

This prevents the most dangerous failure mode: an AI that approves its own work without scrutiny.

---

## Completion Criteria

✅ Bug (`divide()` using `//`) is reproduced by running the failing test

✅ Fix is drafted in an isolated worktree — main checkout untouched

✅ Fix follows the skill: smallest possible change, no test files touched

✅ Reviewer grades the good fix as **PASS**

✅ PR is opened on PASS

✅ Planted bad fix (`division()`) is graded as **FAIL** with reasons

✅ The checker is strict enough that it does not approve everything

---

*Part of the [Loop Engineering Projects](../) series — learning Claude Code's `/loop` skill through practical examples.*
