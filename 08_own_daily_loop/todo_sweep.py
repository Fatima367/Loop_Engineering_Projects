#!/usr/bin/env python3
"""todo_sweep.py — deterministic checker for Project 8's daily loop.

Looks for TODO / FIXME comments in the repo's Python files, keeps only those
older than STALE_DAYS (30), compares them against what is already logged in
progress.md, appends a dated entry with the NEW stale candidates, and exits
non-zero if there are new candidates to act on.

This is the *checker*, the thing a command (not the agent) runs to decide
whether today's pass found work. Staleness comes from the file's git commit
date when available (so committed old files count as stale even after a fresh
clone), falling back to the file's mtime.

Usage:
    python todo_sweep.py            # one pass, appends to progress.md
"""

import os
import re
import subprocess
import sys
from datetime import datetime, timedelta

STALE_DAYS = 30
PROGRESS_FILE = "progress.md"
SCAN_DIRS = ["sample_code"]

TODO_RE = re.compile(r"#\s*(TODO|FIXME)\s*:\s*(.*)")


def file_date(path: str) -> datetime:
    """Best-available date for a file: last git commit date, else mtime."""
    try:
        out = subprocess.check_output(
            ["git", "log", "-1", "--format=%cI", "--", path],
            cwd=os.path.dirname(os.path.abspath(path)),
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
        if out:
            return datetime.fromisoformat(out.replace("Z", "+00:00")).replace(tzinfo=None)
    except Exception:
        pass
    return datetime.fromtimestamp(os.path.getmtime(path))


def scan_for_todos(root: str) -> list:
    """Return list of (path, lineno, age_days, kind, text) for every TODO/FIXME."""
    found = []
    for dirpath, _dirs, files in os.walk(root):
        for name in files:
            if not name.endswith(".py"):
                continue
            path = os.path.join(dirpath, name)
            try:
                with open(path, encoding="utf-8") as fh:
                    for lineno, line in enumerate(fh, 1):
                        m = TODO_RE.search(line)
                        if m:
                            age = round((datetime.now() - file_date(path)).days, 1)
                            found.append((path, lineno, age, m.group(1), m.group(2)))
            except OSError as exc:
                print(f"[!] could not read {path}: {exc}", file=sys.stderr)
    return found


def load_logged(progress_file: str) -> set:
    """Return a set of 'path:lineno' strings already recorded in progress.md."""
    logged = set()
    if not os.path.exists(progress_file):
        return logged
    with open(progress_file, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.strip()
            # logged entries look like: `- sample_code/stale_module.py:5 ...`
            if line.startswith("- ") and ": " in line:
                rest = line[2:]
                path_part, _, rest_after = rest.partition(":")
                key = f"{path_part}:{rest_after.split()[0]}"
                if "/" in path_part or path_part.endswith(".py"):
                    logged.add(key)
    return logged


def main() -> int:
    candidates = []
    for dirpath in SCAN_DIRS:
        if os.path.isdir(dirpath):
            candidates.extend(scan_for_todos(dirpath))

    logged = load_logged(PROGRESS_FILE)
    stale = []
    for path, lineno, age, kind, text in candidates:
        if age < STALE_DAYS:
            continue
        if f"{path}:{lineno}" in logged:
            continue
        stale.append((path, lineno, age, kind, text))

    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"=== todo_sweep pass @ {today} ===")
    if not stale:
        print("No new stale TODO/FIXME comments to report (or already logged). Nothing to do.")
        return 0

    print(f"Found {len(stale)} new stale TODO/FIXME (older than {STALE_DAYS} days):")
    for path, lineno, age, kind, text in sorted(stale):
        print(f"  - {path}:{lineno} [{age:.0f}d] {kind}: {text}")

    with open(PROGRESS_FILE, "a", encoding="utf-8") as fh:
        fh.write(f"\n## {today}\n")
        for path, lineno, age, kind, text in sorted(stale):
            fh.write(f"- {path}:{lineno} — {kind}: {text}\n")
    print(f"\nLogged {len(stale)} new entry/entries to {PROGRESS_FILE}.")
    return 1  # non-zero = new work found for the maker-checker to grade


if __name__ == "__main__":
    sys.exit(main())