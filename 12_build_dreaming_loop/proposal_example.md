# proposal_example.md — what a dreaming-loop PR description should look like

This is a **mock** of the PR the dreaming loop opens. It traces every proposed
change to *cited dated log entries* — a guess would not be acceptable.

---

## Proposed change to AGENTS.md

**Add rule:** `Always check that config.yaml exists before reading it.`

**Evidence (each repeat cited from progress.md):**

| Run (dated entry) | What failed |
|-------------------|-------------|
| `2026-08-15` | tried to read config.yaml — file not found |
| `2026-08-16` | tried to read config.yaml — file not found |
| `2026-08-17` | tried to read config.yaml — file not found |

That is the **same failure 3 runs in a row**. The smallest rule that would have
stopped all three is a guard before reading `config.yaml`:

```diff
## Rules
+1. Always check that config.yaml exists before reading it.
 2. Never commit directly to main — work on a `claude/*` branch and open a PR.
```

**Proposed deletion:** remove rule **"Always pin dependency versions with an
exact version number."** It has not been exercised by any run since
`2026-08-14` (nothing in progress.md references dependency pinning) — it is a
rule no recent run needed.

---

## Why this is evidence, not a guess

- Each cited entry is a **real dated line** in `progress.md` — not a plausible-sounding pattern.
- The proposed change is the **smallest** one that prevents the repeated failure.
- The deletion is justified by absence: no recent run needed that rule.
- Nothing in `AGENTS.md` changes until **you merge the PR**.