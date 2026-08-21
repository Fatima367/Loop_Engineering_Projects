# Project 7 · Monthly Cost Estimate

How much one beat of your loop costs, extrapolated to a month (Concept 13).

## The formula

```
monthly_cost = tokens_per_beat × beats_per_month
```

## Measure one beat

Run the loop once and read how many tokens it consumed:

```bash
claude -p "Read progress.md. List all TODO comments in the repo not already logged there Append a new time stamped dated entry to loop.log and progress.md summarizing what you found. Do not repeat prior entries." --output-format json
```

Look for the token count line in the `--verbose` output (e.g. `input tokens … output tokens …`).

- Tokens per beat (measured): **188,867**
- Roughly how many are read vs written: **187,661** read (93,069 fresh + 94,592 cached) / **1,206** written

## Extrapolate to a month

| Beat cadence | Beats / month | Monthly tokens |
|--------------|---------------|----------------|
| Daily | 30 | 188,867 × 30 = **5,666,010** |
| Hourly | 720 | 188,867 × 720 = **135,984,240** |

## Rough USD at current cadence

> Measured rate from this run: **$0.416 ÷ 188,867 tokens ≈ $2.20 / 1M tokens**
> The point is **relative magnitude**, not pennies. Compute:
> `monthly_cost ≈ 5,666,010 tokens × $2.20 / 1,000,000 = $12.47 USD/month` (daily cadence)
> `monthly_cost ≈ 135,984,240 tokens × $2.20 / 1,000,000 = $299.17 USD/month` (hourly cadence)

## Real version (paid tier)

If Project 3 runs as a live cloud Routine, the **run transcript** on the Routine's
detail page shows the exact token usage per run — copy it here instead of guessing:

- Real Routine tokens per run: **188,867** (93k input + 94k cached + 1.2k output)
- Actual cost per run: **$0.416**
- Monthly estimate at daily cadence: **$12.47**
- Monthly estimate at hourly cadence: **$299.17**

## Why this matters

If one beat is cheap but the cadence is aggressive (hourly → 720 beats/month),
even a modest beat adds up. Knowing the number lets you choose: slow the cadence,
shorten the prompt, or scope the loop smaller — before it runs overnight.

## Reference: Claude API Pricing (per 1M tokens)

| Model | Input | Output | Context Window |
|-------|-------|--------|----------------|
| Claude Fable 5 | $10.00 | $50.00 | 1M |
| Claude Opus 5 | $5.00 | $25.00 | 1M |
| Claude Sonnet 5 | $2.00 | $10.00 | 1M |
| Claude Haiku 4.5 | $1.00 | $5.00 | 200k |

*Source: [platform.claude.com/docs/en/about-claude/models](https://platform.claude.com/docs/en/about-claude/models) — verify current rates before budgeting.*

Using these rates, a beat with **93k input + 94k cached + 1.2k output** costs approximately:

- **Claude Fable 5:** $1.55 (input $0.93 + cache ~$0.09 + output $0.06) ≈ **$46.50/mo** daily
- **Claude Opus 5:** $0.78 (input $0.47 + cache ~$0.05 + output $0.03) ≈ **$23.25/mo** daily
- **Claude Sonnet 5:** $0.31 (input $0.19 + cache ~$0.02 + output $0.01) ≈ **$9.30/mo** daily
- **Claude Haiku 4.5:** $0.16 (input $0.09 + cache ~$0.01 + output $0.01) ≈ **$4.70/mo** daily