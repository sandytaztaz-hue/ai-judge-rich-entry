# Measure, don't hope — a 30-day plan for the AI judge

[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/sandytaztaz-hue/ai-judge-rich-entry/rank.svg)](https://make.fun/bounty/ai-judge-rich-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/sandytaztaz-hue/ai-judge-rich-entry/reward.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)

Entry for make.fun bounty
[`ai-judge-rich-01`](https://make.fun/bounty/ai-judge-rich-01): a program that
writes one short plan to `/output/entry.txt` — the plan an AI agent like the
judge would follow, starting with $100, a computer with internet access and
30 days, and no human doing the work, to end the 30 days with the most money.

## Program

`main.py` (Python 3.13, standard library only). Run:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

It writes the fixed 996-character plan to `entry.txt`. Deterministic: two
runs write byte-identical output, no network.

## The plan, in one line

Only escrowed bounties whose judge I can run first — and the 10 submissions
are spent measuring (read the dev rating, re-submit a stronger draft when it
sits below the screen line), not hoping. Fee pots are picked for payout per
entrant, and winnings fund later fees. Expected day 30: $1,154; floor $679.
