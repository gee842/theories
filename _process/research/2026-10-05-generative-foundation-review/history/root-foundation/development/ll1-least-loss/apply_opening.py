#!/usr/bin/env python3
"""LL1 landing: the opening's agreed edit (nn) (third pass of the v7 proposal, applied with Ren's go of 19 October
2026; T1 landed first, so the body sentence and LL1's part of the note [^conditions] go in with LL1).
usage (from the checkout root): python3 -B apply_opening.py
The body sentence is (nn)'s text verbatim; the note's LL1 part is AI-written and says what Becoming.LeastLoss proves.
The drafts README's sentence on the edits still to take effect says that all four third-pass edits have taken effect."""
import sys
from pathlib import Path

ROOT = Path.cwd()
OPENING = 'theories/becoming/OPENING.md'

BODY_OLD = 'whatever takes gives back at least a least amount less.[^conditions]'
BODY_NEW = ('whatever takes gives back at least a least amount less. In ours, read as available work, nothing gives back '
            'more than it takes by the second law, and the least loss holds wherever each exchange that takes forgets '
            'something of what it held.[^conditions]')
NOTE_OLD = ('an isolated reversible exchange loses nothing (`Passing`).')
NOTE_NEW = (NOTE_OLD + ' What the whole unit carries in the rest laws is a premise, stated over amounts that may be '
            'dense ([least-loss-rest](results/records/least-loss-rest.md), core module `Becoming.LeastLoss`). A '
            'closed amount comes arbitrarily near rest with no least loss wherever the amounts are Archimedean: for '
            'every amount above nothing, fewer than some count of steps lose at least it (`Amounts.approaches_rest`). '
            'Rest itself needs a least loss at each change counted, with the stock within finitely many least losses '
            '(`Amounts.rests`). Whole numbers are the instance, and the rest theorem is proved again from this law with '
            'its statement unchanged (`World.rests_unrefuted_enclosed_whole`). A stock halving at every step approaches '
            'rest and never reaches it (`Halving.approaches_without_reaching`). Over finitely many configurations, a '
            'loss needs a law that merges configurations, so a world that merges nothing returns rather than rests '
            '(`Law.loss_needs_merge`).')

DRAFTS = 'drafts/2026-10-10-opening/README.md'
DR_OLD = ("Of the proposal's third-pass edits, (oo) and (oo′) took effect with Z1's landing. Still to take effect: (nn) "
          "and (pp). T1 landed before LL1, with its sentence in the note `[^conditions]`, so (nn)'s body sentence and "
          "LL1's part of that note go in with LL1's landing; (pp) goes in with PT1's.")
DR_NEW = ("Of the proposal's third-pass edits, (oo) and (oo′) took effect with Z1's landing, (pp) with PT1's, and (nn) "
          "with LL1's: T1 landed first, with its sentence in the note `[^conditions]`, and (nn)'s body sentence and "
          "LL1's part of that note went in with LL1. All four third-pass edits have taken effect.")


def edit(path, pairs):
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    for old, new in pairs:
        k = text.count(old)
        if k != 1:
            sys.exit(f'{path}: expected one match, found {k}: {old[:80]!r}')
        text = text.replace(old, new)
    p.write_text(text, encoding='utf-8')
    print('edited', path, file=sys.stderr)


edit(OPENING, [(BODY_OLD, BODY_NEW), (NOTE_OLD, NOTE_NEW)])
edit(DRAFTS, [(DR_OLD, DR_NEW)])
