#!/bin/bash

for issue in issue-a issue-b issue-c; do
  (
    git worktree add "wt-$issue" -b "fix-$issue"

    cd "wt-$issue"

    opencode run "read ../issues/$issue.md and draft a fix"

    opencode run "@reviewer grade the diff, reply PASS or FAIL"
  ) &
done

wait


