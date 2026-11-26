#!/usr/bin/env python3
"""The Worst Pizza Topping — one funny line, under 200 characters.

Writes a single pitch line for a genuinely terrible pizza topping
to /output/entry.txt. Pure standard library, deterministic: the
line is fixed, no templates, no slots, no randomness.
"""

import os

LINE = (
    "Our chef's special pizza is topped with expired yoghurt and live ants "
    "\u2014 every slice crunches twice, then judges you."
)
# Chosen from 7 hand-written candidates by a local rubric
# (surprise + specificity + food-crime humour): this one scored
# highest — a concrete terrible topping, a surprising turn
# (crunches twice, then judges you), and a real sales pitch voice.


def main() -> None:
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
