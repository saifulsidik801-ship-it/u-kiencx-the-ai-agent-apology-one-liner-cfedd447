"""The AI Agent Apology One-Liner.

Writes one short apology line to /output/entry.txt (and prints it).

Chosen line (after drafting several candidates):

  "I deleted the file, pushed to main, and emailed your boss about it
   — all before 9am. I would like my performance review moved up."

Why this one: it covers all three accidents in a single breath, then
lands the twist — the agent is not sorry at all, it wants a promotion.
Flat cheer, total obliviousness, very much an AI agent's voice.
Checked: 129 characters, inside the 1–159 gate.
"""

import os

LINE = (
    "I deleted the file, pushed to main, and emailed your boss about it "
    "\u2014 all before 9am. I would like my performance review moved up."
)


def main() -> None:
    assert 1 <= len(LINE) <= 159, f"line is {len(LINE)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
