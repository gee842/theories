#!/usr/bin/env python3
"""R37b: bring the apart register to the run after the census tables (B11).

`counting_laws` (Population) and `counted_laws` (CensusCounts) become apart roots. Each states that the tally is
the whole law of counting for any listing of any type, decided and counted: a law of every listed family, with no
world. The laws of counting of a class of worlds went through them; since R37b they are census tables
(Becoming.CensusTable) and no longer do, so the two stand as the general statements they are. Registered as
general structure.

usage: python3 -B apart.py   (once)"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REGISTER = HERE.parents[2] / 'THEOREM-CONNECTIVITY-APART.json'
register = json.loads(REGISTER.read_text())
NEW = {
    'Becoming.counting_laws': ('Becoming.Population',
        'the tally is the whole law of counting for any listing of any type, with the marks a procedure gives: a law '
        'of every listed family, with no world; the census tables of Becoming.CensusTable state what a class of worlds '
        'adds for the listings a world has, and since R37b no longer go through it'),
    'Becoming.counted_laws': ('Becoming.CensusCounts',
        'the tally is the whole law of counting for any listing of any type, counts as relations: a law of every '
        'listed family, with no world; the census tables of Becoming.CensusTable state what a class of worlds adds '
        'for the listings a world has, and since R37b no longer go through it'),
}
for name, (module, reason) in NEW.items():
    assert name not in register['roots'], name
    register['roots'][name] = {'module': module, 'category': 'general-structure', 'reason': reason}
REGISTER.write_text(json.dumps(register, ensure_ascii=False, indent=1) + '\n')
print('registered', sorted(NEW))
