#!/usr/bin/env python3
"""P58c, second pass: pure renames (statements unchanged) across the core, on word boundaries. Copies every core module
that mentions one into TREE first unless it is already there. Usage: tokens_p58c.py CHECKOUT TREE"""
import re
import shutil
import sys
from pathlib import Path

SRC = Path(sys.argv[1]) / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
TREE = Path(sys.argv[2]) / 'Becoming'
RENAMES = [
    ('Dissipative.finite_ceases', 'Dissipative.finite_taking_not_recurring'),
    ('finite_ceases', 'finite_taking_not_recurring'),
    ('Dissipative.one_ceases', 'Dissipative.one_taking_not_recurring'),
    ('one_ceases', 'one_taking_not_recurring'),
    ('taking_ceases_within', 'taking_not_recurring_within'),
    ('taking_ceases', 'taking_not_recurring'),
    ('rising_ceases_on', 'rising_not_recurring_on'),
    ('standing_ceases_on', 'standing_not_recurring_on'),
    ('rising_ceases', 'rising_not_recurring'),
    ('standing_ceases', 'standing_not_recurring'),
    ('dissipation_ceases', 'dissipation_generation_not_recurring'),
    ('depletes_finitely', 'depletion_not_recurring'),
    ('generation_ceases_on', 'generation_not_recurring_on'),
    ('generation_ceases', 'generation_not_recurring'),
    ('Conditions.drawdown_finite', 'Conditions.drawdown_not_recurring'),
]
PAT = re.compile(r'\b(' + '|'.join(re.escape(o) for o, _ in RENAMES) + r')\b')
MAP = dict(RENAMES)
for src in sorted(SRC.glob('*.lean')):
    target = TREE / src.name
    text = (target if target.exists() else src).read_text()
    new = PAT.sub(lambda m: MAP[m.group(1)], text)
    if new != text:
        target.write_text(new)
        print('renamed in', src.name, len(PAT.findall(text)))
