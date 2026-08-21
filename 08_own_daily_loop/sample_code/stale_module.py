"""Deliberately stale module — the daily loop should flag the TODO/FIXME here.

The two comments below are old (their git commit date is > 30 days). Commit this
file with an old --date so todo_sweep.py counts it as stale even after a clone:

    git add sample_code/stale_module.py
    git commit -m "add stale module" --date "2026-07-01T09:00:00"
    GIT_COMMITTER_DATE="2026-07-01T09:00:00" ...
"""


def process(x):
    if not isinstance(x, (int, float)):
        raise TypeError("x must be a number")
    return x * 2


def retry(fn, n=3):
    for i in range(n):  # runs exactly n times
        try:
            return fn()
        except Exception:
            continue
    return None