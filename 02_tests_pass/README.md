# 02 — Make the Tests Pass, Then Stop

**Project 2 of the Loop Engineering Series**
Difficulty: easy–medium · Time: 30–45 min · Concept: Conditional Loop

---

## Goal

Build a loop that keeps fixing failing tests until they pass — but let the test runner, not the agent, decide when the work is done.

---

## What This Project Demonstrates

- Setting up a **conditional loop** that runs until a command succeeds
- Using `/goal` with a stop condition tied to test results
- Letting an external tool (pytest) be the judge of completion
- Stopping the loop when tests genuinely pass — not when the agent gives up

---

## Files

| File | Purpose |
|------|---------|
| `math_utils.py` | Two buggy functions (`add` and `is_even`) that need fixing |
| `test_math_utils.py` | Two failing tests that define what "done" means |
| `output.md` | Transcript of the loop in action — shows the fix and the passing tests |
| `media/` | Screenshots documenting the project |

---

## How It Works

### 1. Confirm the tests fail first

```bash
pytest test_math_utils.py -v
```

Both tests should fail — that's the starting point.

### 2. Set up the stop condition

```
/goal All tests in 02_tests_pass/test_math_utils.py pass. Stop after 3 tries.
```

This tells Claude Code:
- Keep trying to fix the tests
- Stop **only when all tests pass**
- Give up after **3 attempts** if they still don't pass

### 3. Let the loop work

The agent reads the failing tests, finds the bugs, fixes them, and re-runs the tests. This repeats until:
- ✅ All tests pass → loop stops (success)
- ❌ 3 tries with no fix → loop stops (cap hit)

### 4. What "Done" Looks Like

```
● Goal acknowledged. Let me examine the test file and start working toward passing tests.

● Both tests fail. Reading the source file.

● Now fixing the two bugs.
  ⎿  Updated math_utils.py
  ⎿  Updated math_utils.py

● Running tests to verify.

● All tests pass (2/2). Two fixes applied:

  1. add — changed a - b → a + b
  2. is_even — changed n % 2 == 1 → n % 2 == 0
```

---

## Key Commands

| Command | What it does |
|---------|--------------|
| `/goal <condition>` | Set a stop condition for the current session |
| `pytest <file> -v` | Run tests and show pass/fail for each |
| `/goal clear` | Clear the current goal early |

---

## The Lesson

The loop should stop because the **tests actually passed**, not because it hit the retry cap.

If it keeps hitting the cap:
- Your **stop condition** might be wrong
- Your **prompt** might not be clear enough
- The **bugs** might be too complex for the agent to fix in N tries

That's the point — learn to write conditions that work.

---

## Completion Criteria

✅ Two failing tests exist in `test_math_utils.py`
✅ The agent reads the source file before fixing
✅ The agent fixes the bugs in `math_utils.py`
✅ All tests pass after the fix
✅ The loop stops because tests pass — not because of the cap

---

*Part of the [Loop Engineering Projects](../) series — learning Claude Code's `/loop` skill through practical examples.*
