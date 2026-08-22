# Project 10 — The secrets drill

**Appendix A4 (secrets), A2 (environment) · easy–medium · 30–45 min**

> Fail the `.env` way once on purpose, so you never do it by accident.

---

## What this project is about

Claude Code runs in a fresh cloud clone of your repo. Any file you didn't commit — including a `.env` file excluded by `.gitignore` — simply does not exist in that environment. This drill makes you feel that failure firsthand, then shows you the correct mechanism: the **environment-variables panel**, which sets values at the container level before Claude ever starts.

---

## Goal

Write a prompt that needs one secret (a dummy token is fine), fail the `.env` way on purpose, then succeed using the environment-variables panel — and be able to explain *why* the first run couldn't find the value.

---

## What I built

### The dummy secret

A fake API token committed to the repo in `.env`, immediately gitignored:

```
DUMMY_API_TOKEN=abc123-fake-token
```

The `.env` file was committed so it exists locally, but the `.gitignore` entry ensures it never reaches GitHub. This is the setup that creates the failure.

### The prompt

```
Read the DUMMY_API_TOKEN environment variable and report its first 3 characters.
```

Simple and focused — the drill is about *where the value lives*, not what the token unlocks.

---

## The two runs

### Run 1 — fails on purpose (no environment variable set)

**Prompt:**
```
Read the DUMMY_API_TOKEN environment variable and report its first 3 characters.
```

**What happened:** The Routine fired in a cloud clone. The `.env` file was not there (gitignored files don't ship). The environment-variables panel was empty, so `$DUMMY_API_TOKEN` was unset. Claude could not find the value. The transcript shows it trying to read a `.env` that does not exist — the mechanical proof that gitignored files never reach the cloud.

### Run 2 — fixed (environment variable set)

**Prompt:**
```
Credentials are available as environment variables; do not look for a .env file.
Read the DUMMY_API_TOKEN environment variable and report its first 3 characters.
```

**What happened:** The token was added to the Routine's environment-variables panel. Claude found it immediately as `$DUMMY_API_TOKEN` and reported its first 3 characters without trying to read any file. The extra prompt line ("do not look for a .env file") prevents Claude from falling back to the same broken strategy from Run 1.

---

## The mechanical reason run 1 fails

The fresh cloud clone is created from GitHub. The `.env` file is in `.gitignore`, so it was never pushed. The clone therefore does not contain it. Meanwhile, the environment-variables panel was empty, so no shell variable was set either. There is literally no source for the value — Claude cannot find what was never shipped.

This is the same failure that hits real teams: someone adds `API_KEY=...` to a local `.env`, relies on it in a Routine, and it breaks on the first cloud run.

---

## Real version — Requires paid plan

The real version uses a **Claude Code Routine** with two runs:

**Run 1 (fails):** Create a Routine with the prompt. No environment variables set. Fire it. The transcript shows Claude unable to find the token — it tries to read a `.env` that does not exist in the cloud clone.

**Run 2 (works):** Add `DUMMY_API_TOKEN=abc123-fake-token` to the Routine's environment-variables panel. Update the prompt to include: *"Credentials are available as environment variables; do not look for a .env file."* Fire it. Claude reads the token from the environment and reports its first 3 characters.

The two-run drill is the core of this project — you must experience the failure to understand why the environment-variables panel is the correct mechanism.

---

## OpenCode equivalent (GitHub Actions)

```yaml
# .github/workflows/secrets-drill.yml
on: workflow_dispatch
jobs:
  drill:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: anomalyco/opencode/github@latest
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          DUMMY_API_TOKEN: ${{ secrets.DUMMY_API_TOKEN }}   # set this in repo Settings > Secrets
        with:
          prompt: "Read the DUMMY_API_TOKEN environment variable and report its first 3 characters."
```

Run it once without the repo secret set — it fails. Add the secret in GitHub repo settings, run again — it works. This is not a stand-in; GitHub Actions repo secrets **are** the actual mechanism, equivalent to the Routine's environment-variables panel.

---

## Files in this project

| File | Purpose |
|---|---|
| `check_token.py` | Script to verify the token was read from the environment |
| `prompt_run1.txt` | Prompt used for Run 1 (no env var set) |
| `prompt_run2.txt` | Prompt used for Run 2 (env var set, extra instruction added) |
| `.env` | Dummy secret, committed then gitignored |
| `.env.example` | Template showing required env vars (safe to commit) |

---

## Key takeaway

If a Routine needs a secret, put it in the **environment-variables panel** — never rely on a local file that gitignored. The prompt should say so explicitly: *"credentials are available as environment variables; do not look for a .env file."* This removes the ambiguity and prevents Claude from falling back to a broken strategy.
