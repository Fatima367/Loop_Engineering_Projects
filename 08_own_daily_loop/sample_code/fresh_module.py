"""Recent module — the daily loop should NOT flag the TODO here.

Commit this file today (or keep its mtime recent). The TODO is new, so
todo_sweep.py's 30-day staleness window ignores it.
"""


def fresh_fn(items):
    # TODO: cache the result of this call (added recently, not stale yet)
    return sum(items)