#!/usr/bin/env python3
"""P58c: pure renames (statements unchanged) across the core, on word boundaries. Copies every core module
that mentions one into TREE first unless it is already there. Usage: tokens_p58c.py CHECKOUT TREE"""
import re
import shutil
import sys
from pathlib import Path

SRC = Path(sys.argv[1]) / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
TREE = Path(sys.argv[2]) / 'Becoming'
RENAMES = [
    ('falls_finitely_from_floor', 'falls_not_recurring_from_floor'),
    ('falls_finitely', 'falls_not_recurring'),
    ('rising_ceases_from', 'rising_not_recurring_from'),
    ('standing_ceases_from', 'standing_not_recurring_from'),
    ('taking_ceases_from', 'taking_not_recurring_from'),
    ('generation_ceases_from', 'generation_not_recurring_from'),
    ('active_finitely_from', 'active_not_recurring_from'),
    ('active_finitely', 'active_not_recurring'),
    ('arising_finitely_from', 'arising_not_recurring_from'),
    ('arising_finitely', 'arising_not_recurring'),
    ('change_stops', 'change_not_recurring'),
    ('unfed_consumption_stops', 'unfed_consumption_not_continuing'),
    ('taking_stops', 'taking_not_recurring'),
    ('exchange_stops', 'exchange_not_recurring'),
    ('rests_at_resolution', 'not_recurring_at_resolution'),
    # statement changes, done by hand in the modules that state them; callers follow the name
    ('premised_rests', 'premised_rests_unrefuted'),
    ('sample_rests', 'sample_rests_unrefuted'),
    ('hatch_rests', 'hatch_rests_unrefuted'),
    ('rests_of_after', 'rests_unrefuted_of_after'),
    ('rests_unrefined', 'rests_unrefuted_without_refinement'),
    ('rests_refinement_counted', 'rests_unrefuted_refinement_counted'),
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
