export const meta = {
  name: 'fix-and-grade',
  description: 'Fix issues A, B, C in parallel worktrees, then have a reviewer grade each fix',
  phases: [
    { title: 'Fix', detail: 'Apply minimal fix for each issue in its own worktree' },
    { title: 'Review', detail: 'Reviewer grades each fix: PASS or FAIL' },
  ],
}

// Phase 1: Fix all three issues in parallel worktrees
const fixes = await parallel([
  () => agent(
    `You are a bug fixer. Follow these steps EXACTLY:

SKILL (fix-steps):
1. Reproduce the bug by running the failing test first.
2. Make the smallest possible change that fixes it.
3. Do not touch test files.
4. Run the full test suite before reporting done.

ISSUE: Issue A — off-by-one in total() when list has 1 item

FILE: math_utils.py contains:
def total(items):
    return sum(items) - 1  # off-by-one bug

TEST FILE: test_math_utils.py contains:
def test_total_single_item():
    assert total([5]) == 5
def test_total_multiple_items():
    assert total([1, 2, 3]) == 6
def test_total_empty():
    assert total([]) == 0

YOUR TASK:
1. You are in an isolated worktree. The project is at: D:\\Documents\\Loop_Engineering_Projects\\05_codify_the_body
2. Read math_utils.py to see the current code.
3. Fix the bug — make the smallest possible change to total(). Do NOT touch test_math_utils.py.
4. Run: cd D:\\Documents\\Loop_Engineering_Projects\\05_codify_the_body && python -m pytest test_math_utils.py -v
5. Report your final answer as a JSON object on the last line:
{"issue":"A","fix":"<one-line description>","tests_pass":true,"test_output":"<full pytest output>"}`,
    { label: 'fix:A', phase: 'Fix', isolation: 'worktree' }
  ),
  () => agent(
    `You are a bug fixer. Follow these steps EXACTLY:

SKILL (fix-steps):
1. Reproduce the bug by running the failing test first.
2. Make the smallest possible change that fixes it.
3. Do not touch test files.
4. Run the full test suite before reporting done.

ISSUE: Issue B — is_even() logic inverted

FILE: math_utils.py contains:
def is_even(n):
    return n % 2 == 1

TEST FILE: test_math_utils.py contains:
def test_is_even_true():
    assert is_even(4) == True
def test_is_even_false():
    assert is_even(3) == False

YOUR TASK:
1. You are in an isolated worktree. The project is at: D:\\Documents\\Loop_Engineering_Projects\\05_codify_the_body
2. Read math_utils.py to see the current code.
3. Fix the bug — make the smallest possible change to is_even(). Do NOT touch test_math_utils.py.
4. Run: cd D:\\Documents\\Loop_Engineering_Projects\\05_codify_the_body && python -m pytest test_math_utils.py -v
5. Report your final answer as a JSON object on the last line:
{"issue":"B","fix":"<one-line description>","tests_pass":true,"test_output":"<full pytest output>"}`,
    { label: 'fix:B', phase: 'Fix', isolation: 'worktree' }
  ),
  () => agent(
    `You are a bug fixer. Follow these steps EXACTLY:

SKILL (fix-steps):
1. Reproduce the bug by running the failing test first.
2. Make the smallest possible change that fixes it.
3. Do not touch test files.
4. Run the full test suite before reporting done.

ISSUE: Issue C — divide() truncates with integer division

FILE: math_utils.py contains:
def divide(a, b):
    return a // b

TEST FILE: test_math_utils.py contains:
def test_divide_normal():
    assert divide(7, 2) == 3.5
def test_divide_exact():
    assert divide(10, 2) == 5.0

YOUR TASK:
1. You are in an isolated worktree. The project is at: D:\\Documents\\Loop_Engineering_Projects\\05_codify_the_body
2. Read math_utils.py to see the current code.
3. Fix the bug — make the smallest possible change to divide(). Do NOT touch test_math_utils.py.
4. Run: cd D:\\Documents\\Loop_Engineering_Projects\\05_codify_the_body && python -m pytest test_math_utils.py -v
5. Report your final answer as a JSON object on the last line:
{"issue":"C","fix":"<one-line description>","tests_pass":true,"test_output":"<full pytest output>"}`,
    { label: 'fix:C', phase: 'Fix', isolation: 'worktree' }
  ),
])

// Phase 2: Grade each fix with a reviewer agent
const reviews = await parallel(fixes.map(fix => () =>
  agent(
    `You are a strict code reviewer. You do NOT make changes. Your job is to grade a bug fix.

ORIGINAL math_utils.py (before any fix):
def total(items):
    return sum(items) - 1
def is_even(n):
    return n % 2 == 1
def divide(a, b):
    return a // b

THE FIXER REPORTED:
${JSON.stringify(fix, null, 2)}

REVIEW STEPS:
1. Read the CURRENT math_utils.py at D:\\Documents\\Loop_Engineering_Projects\\05_codify_the_body\\math_utils.py to see what changed.
2. Run the full test suite: cd D:\\Documents\\Loop_Engineering_Projects\\05_codify_the_body && python -m pytest test_math_utils.py -v
3. Check that test_math_utils.py was NOT modified.
4. Verify the fix is the SMALLEST possible change (only the broken line changed).

GRADING CRITERIA:
- All 7 tests pass? (6 were failing, 1 was passing)
- Change is minimal (only the one broken expression changed)?
- No test files touched?

Reply with exactly:
PASS — <one reason>
or
FAIL — <one reason>`,
    { label: `review:${fix.issue}`, phase: 'Review' }
  )
))

return { fixes, reviews }
