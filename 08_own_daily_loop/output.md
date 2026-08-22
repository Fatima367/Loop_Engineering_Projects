# 08 — Your Own Daily Loop · Output

> ## 📋 TEMPLATE — how to fill this in
> After you run Project 8 by hand 3–4 times, paste the real output of each
> "day" over the `{{PLACEHOLDER}}` markers below. Keep the section titles and
> check off what applied.

## Run 1 (Day 1)

```
{{PASTE_RUN_1}}
```

- New stale candidates found: **{{COUNT_1}}**
- Logged to progress.md: **{{YES_NO_1}}**

## Run 2 (Day 2)

```
{{PASTE_RUN_2}}
```

- New stale candidates found: **{{COUNT_2}}**
- Logged to progress.md: **{{YES_NO_2}}**

How is this run building on the last one (spine proof)?:

{{YOUR_MEMORY_PROOF_2}}

## Run 3 (Day 3)

```
{{PASTE_RUN_3}}
```

- New stale candidates found: **{{COUNT_3}}**
- Logged to progress.md: **{{YES_NO_3}}**

## Run 4 (optional, Day 4)

```
{{PASTE_RUN_4_IF_RUN}}
```

## Reviewer grade each run

| Run | Reviewer reply | PR opened? |
|-----|----------------|-----------|
| 1 | {{GRADE_1}} | {{PR_1}} |
| 2 | {{GRADE_2}} | {{PR_2}} |
| 3 | {{GRADE_3}} | {{PR_3}} |

## Final spine state

{{PASTE_FINAL_PROGRESS_MD}}

**Do you trust what the loop shipped because you read it?** {{YOUR_TRUST_ANSWER}}

---

## ✅ Done check (note which apply after you run)

- [ ] Ran the checker (`python todo_sweep.py`) and a command decided there was work
- [ ] Ran the full loop (skill → maker → checker → PR only on PASS → spine)
- [ ] Ran it again — the second run built on the first (no repeated entries)
- [ ] Reviewer never let a bad diff through (maker-checker worked)
- [ ] I read what it shipped and understood every change