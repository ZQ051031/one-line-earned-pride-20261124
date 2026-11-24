# One Line of Earned Pride

A make.fun micro bounty entry: one line of text (1–240 characters) that gives
the judge a quiet, earned moment of pride for someone in a scene.

## The line

> Six ruined loaves later, the bread finally rose, and she cut the first slice herself, still in her apron, before anyone else was awake.

A home baker, six ruined loaves behind her, watches the seventh rise — and
claims the first slice herself, alone in the kitchen before anyone else is awake.

## How it works

`main.py` (Python standard library only) writes the line exactly as above —
one line, 135 characters, no trailing newline — to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

## Run it

```sh
python3 main.py
```

## Why this line

It is built against the judge's brief, in order:

- **Earned pride:** six ruined loaves are the effort the reader can feel;
  the seventh loaf rising is the long effort finally landing.
- **Concrete scene:** a real person at her own kitchen counter, apron on,
  cutting the first slice — seen happening, not summarised.
- **No assertion:** nobody says she is proud. The pride is in the doing:
  she takes the first slice herself, before anyone else is awake.
- **One read:** the quiet lands on the last word — the kitchen is still
  empty, and the moment is hers alone.
- **Fresh:** a dawn kitchen, not a trophy, a podium or a graduation.

## Testing

Run `main.py` twice with a private output directory and compare the bytes:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/earned-pride-out python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/earned-pride-out2 python3 main.py
cmp /tmp/earned-pride-out/entry.txt /tmp/earned-pride-out2/entry.txt
wc -c /tmp/earned-pride-out/entry.txt
```

Both runs must produce byte-identical output: one line, 135 bytes,
no trailing newline.

## License

MIT — see LICENSE.
