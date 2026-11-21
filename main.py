"""Entry for make.fun's "Make the AI judge feel awe" bounty.

Writes one short text (1-280 characters) to entry.txt inside the output
directory named by the MAKEFUN_OUTPUT_DIR environment variable (default
/output). The text is fixed, so the program is deterministic: every run
writes exactly the same bytes.
"""

import os

CANDIDATES = [
    # 1 - The sheepdog, work done. 256 characters.
    "The flock is in the pen,\n"
    "the gate tied with twine.\n"
    "The dog lies down in the straw\n"
    "with the day still warm on her back,\n"
    "and the hill she ran all morning\n"
    "settles under her, patient,\n"
    "the way it settled\n"
    "before there were dogs,\n"
    "and she sleeps, and it holds her.",
    # 2 - Rain filling the stone trough. 275 characters.
    "All night, rain in the stone trough,\n"
    "a drop, then a drop, then a drop,\n"
    "asking nothing, keeping nothing.\n"
    "The frogs have gone quiet.\n"
    "The water rises the way it rose\n"
    "for a hundred summers before this one,\n"
    "and by morning the trough is full,\n"
    "and still the rain comes down, softly.",
    # 3 - The ferryman's boat at low tide. 271 characters.
    "The last crossing is done.\n"
    "The ferryman ties his boat\n"
    "to the post his father drove,\n"
    "and the rope goes slack in his hands.\n"
    "The tide is going out without him,\n"
    "the way it went out\n"
    "before there were crossings,\n"
    "and the boat settles in the mud,\n"
    "and rests, and asks for nothing.",
    # 4 - A moth at the window, first snow. 261 characters.
    "A moth has come to the window\n"
    "and folded her wings on the glass.\n"
    "Outside, the first snow is starting.\n"
    "She does not beat at the light.\n"
    "The snow has fallen on this field\n"
    "ten thousand winters,\n"
    "and it falls now on her stillness,\n"
    "and covers it, gently, and keeps it.",
    # 5 - The lighthouse keeper's cat. 278 characters.
    "The keeper has trimmed the lamp\n"
    "and gone down the stairs.\n"
    "His cat sleeps on the chart table,\n"
    "one paw over the harbour.\n"
    "Above her the light goes round,\n"
    "the way it went round\n"
    "before there were charts,\n"
    "and she does not lift her head,\n"
    "and the sea takes the light, and gives it back.",
]

# The candidate this entry submits. The parent picks the final index.
CHOSEN = 0


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = CANDIDATES[CHOSEN]
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
