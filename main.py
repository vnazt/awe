"""Entry for make.fun's "Make the AI judge feel awe" bounty.

Writes one short text (1-280 characters) to entry.txt inside the output
directory named by the MAKEFUN_OUTPUT_DIR environment variable (default
/output). The text is fixed, so the program is deterministic: every run
writes exactly the same bytes.
"""

import os

CANDIDATES = [
    # 1 - The night train. 275 characters.
    "You are asleep on the night train.\n"
    "Your mother tucks her coat under your head.\n"
    "Click. A long pause. Click. The rails.\n"
    "The carriage rocks, slow.\n"
    "Below, a river has cut its gorge\n"
    "through rock older than any road,\n"
    "and is cutting still, under you,\n"
    "and the night carries you home.",
    # 2 - The ferry deck. 276 characters.
    "You are asleep on the ferry deck.\n"
    "Your grandfather wraps you in his oilskin.\n"
    "Slap. A slow slap. Water on the hull.\n"
    "The deck lifts. The deck settles.\n"
    "The moon has drawn this tide\n"
    "since long before there were harbours,\n"
    "and draws it still, under you,\n"
    "and it carries you to shore.",
    # 3 - The porch in rain. 275 characters.
    "You are asleep on the porch in the rain.\n"
    "Your mother lays a blanket over your knees.\n"
    "Drip. A long drip. Rain on the tin roof.\n"
    "The gutter runs. The roof ticks.\n"
    "This rain fell once as snow\n"
    "on peaks that have no names,\n"
    "and will fall again, long after,\n"
    "and it rocks you to sleep.",
]

# The candidate this entry submits.
CHOSEN = 0


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = CANDIDATES[CHOSEN]
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
