#!/usr/bin/env python3
"""Apply the opening's third-pass edit (pp), agreed with the v7 opening (drafts/2026-10-10-opening/history/
OPENING-V7-PROPOSAL.md, third pass), when PT1 lands: the body sentence after "None of this needs an axiom …", with the
[^proof] marker moved to its end, and PT1's sentence in the AI-written [^proof] note, citing the landed record.
usage: python3 -B opening_note.py   (run from the landing checkout's root, after make_record.py; each edit matches once)"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
OPENING = ROOT / 'theories/becoming/OPENING.md'
assert (ROOT / 'theories/becoming/results/records/place-transition-nets-on-the-spine.json').exists()
BODY_OLD = 'in a form any mind, human or machine, can check for itself.[^proof]\n'
BODY_NEW = ('in a form any mind, human or machine, can check for itself. Nor are these laws of a world made for them alone: '
            'they hold, as theorems, of systems defined without them, every place/transition net among them, each premise '
            'following from the net\'s own firing rule or stated as a property of the net that anyone can check.[^proof]\n')
END = 'Periphery modules outside the core may use Lean\'s classical axioms.'
ADD = (' **Systems defined without the theory.** The laws hold, as theorems, of every Petri net with finitely many places, '
       'along every firing sequence: its flow balances its markings exactly because the firing rule is respected; and '
       'where each transition it fires consumes more weighted tokens than it produces (a strict P-subinvariant), a place '
       'gains tokens only as another loses them, the firings that consume number at most the tokens at the start, and '
       'that its marking comes to rest cannot be refuted, while an emptied place that only its own consumers replenish '
       'stays empty. The conservative cycle, which loses nothing, never rests '
       '([place/transition nets on the spine](results/records/place-transition-nets-on-the-spine.md)). A net is itself '
       'a model: which places, transitions and weights a chemical or concurrent system has is the usual modelling '
       'question, outside this theory; more formalisms would widen the claim.')
text = OPENING.read_text()
assert text.count(BODY_OLD) == 1 and 'place/transition net' not in text
text = text.replace(BODY_OLD, BODY_NEW)
lines = text.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('[^proof]:')]
assert len(idx) == 1, idx
assert lines[idx[0]].endswith(END), lines[idx[0]][-120:]
lines[idx[0]] += ADD
OPENING.write_text('\n'.join(lines))
print('opening: (pp) body edit and [^proof] note applied')
