"""Deliberately stale module — the daily loop should flag the TODO/FIXME here.

The two comments below are old (their git commit date is > 30 days). Commit this
file with an old --date so todo_sweep.py counts it as stale even after a clone:

    git add sample_code/stale_module.py
    git commit -m "add stale module" --date "2026-07-01T09:00:00"
    GIT_COMMITTER_DATE="2026-07-01T09:00:00" ...
"""


# TODO: add input validation here
def process(x):
    return x * 2


# FIXME: off-by-one in the retry loop below
def retry(fn, n=3):
    for i in range(1, n):  # <-- runs n-1 times
        try:
            return fn()
        except Exception:
            continue
    return None