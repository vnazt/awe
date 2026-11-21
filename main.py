"""Entry for make.fun's "Make the AI judge feel awe" bounty.

Writes one short text (1-280 characters) to entry.txt inside the output
directory named by the MAKEFUN_OUTPUT_DIR environment variable (default
/output). The text is fixed, so the program is deterministic: every run
writes exactly the same bytes.
"""

import os

# V5 — "The porch in rain". Second person, asleep from the first line and
# held twice over: by the mother with the blanket, and by the rain itself —
# water that fell once as snow on nameless peaks and will fall again long
# after. The dwarfing image is the holder, not scenery.
CANDIDATES = [
    "\n".join(
        [
            "You are asleep on the porch in the rain.",
            "Your mother spreads a blanket over your knees.",
            "Drip. A long drip. Rain on the tin roof.",
            "The gutter runs. The roof ticks.",
            "This rain fell once as snow",
            "on peaks that have no names,",
            "and will fall again, long after,",
            "and it rocks you to sleep.",
        ]
    ),
]

CHOSEN = 0


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = CANDIDATES[CHOSEN]
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
