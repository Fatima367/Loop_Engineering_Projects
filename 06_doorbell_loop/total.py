"""Mock module for Project 6 — contains ONE planted bug.

The workflow in .github/workflows/review.yml should flag this on the PR.
"""


def total(items):
    # planted bug: silently drops the first item, so total([1, 2, 3]) is 5, not 6
    return sum(items[1:])