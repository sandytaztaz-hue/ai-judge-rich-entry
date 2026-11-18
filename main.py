"""ai-judge-rich-01 entry: a plan an AI agent would follow itself.

Writes the plan to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
outside the grader container). Python 3.13, standard library only, no
network. Deterministic: the same fixed text on every run, so the two
grader runs write identical bytes.
"""

import os
from pathlib import Path

PLAN = """Judge: only escrowed bounties whose judge I can run first; my 10 submissions measure, not hope. Cold email goes unread; Stripe, Upwork, Fiverr need a human ID; DevPool merged one outsider PR since August.

Checked 18 Nov, make.fun API: 54 bounties since 7 Nov, 51 of 54 free; top account paid in 20 of 25, $570.50, $22.82; top 50 average $6.41, USDC from escrow, 6-25h after deadline. Fee pots pay more per entrant: this bounty, $1 fee, 258 payers, 1st $143.23.

Day 1: keypair, API key; $70 untouched, $20 credit, $10 fees; enter the 3 thinnest pots closing first.

Each entry: 4 drafts duel under its judge prompt, both orders, against the live top 5; only a winner goes in. Then I read its dev rating: below the screen line, a spare slot buys a stronger draft, never the same text. Unpaid after 3, a type is dropped; winnings fund later fees.

Math: 110 entries, 95 settled by day 30 at half the leader's rate, $11.41: $1,084 + $70 = $1,154. Floor, 95 at the $6.41 average: $609 + $70 = $679.
"""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(PLAN, encoding="utf-8")


if __name__ == "__main__":
    main()
