# AGENTS.md — the rules file the dreaming loop proposes changes to.

These rules steer every run of the loops in this repo. An improvement loop
(the "dreaming" loop) reads past failures and proposes the SMALLEST change to
this file that would have prevented them. Nothing changes in this file unless
a human merges the proposal's PR — a loop that guesses is worse than no loop.

## Rules
1. Never commit directly to main — work on a `claude/*` branch and open a PR.
2. Run the test suite before reporting any fix as done.
3. Append a dated entry to progress.md every run.
4. Always pin dependency versions with an exact version number.