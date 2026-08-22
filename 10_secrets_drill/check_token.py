#!/usr/bin/env python3
"""check_token.py — the second-run proof for Project 10.

Reads DUMMY_API_TOKEN from the environment and prints its first 3 characters.
On the free-tier substitute this proves the env var is available; on the real
Routine it proves the environment-variables panel wiring worked.

Run 1 (fails):   DUMMY_API_TOKEN is not set anywhere            -> KeyError
Run 2 (works):   token is in the env / env-variables panel      -> first 3 chars
"""

import os

token = os.environ["DUMMY_API_TOKEN"]
print("first 3 chars:", token[:3])
print("(we only print the first 3 to prove we found it without leaking it)")