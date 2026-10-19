#!/usr/bin/env python3
"""Register Y3's apart roots in THEOREM-CONNECTIVITY-APART.json: the censuses over the received order (counts of the
sixty-four configurations, checked on them), the two facts about which pairs of the received order are made by which
symmetry, the composition table of the four symmetries, and the order's listing each configuration once. Every law of a
course is stated along the runs of the spine; these are what stays apart. usage: python3 -B register_apart.py
[CHECKOUT_ROOT]"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE.parents[6]
REG = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY-APART.json'
MOD = 'Becoming.HexagramLaws'
CENSUS = ('a census over the received order: {what}, counted on the sixty-four configurations and checked there; the '
          'law it counts is stated along the runs of the spine by {law}')
ORDER = ('a fact about the text\'s received order (序卦): {what}, checked on its thirty-two pairs, not a law of the '
         'unfolding; the symmetries act on the runs of the nuclear law by nuclear_run_act')
ENTRIES = {
    'class_census': ('model-witness', CENSUS.format(
        what='twenty classes under the four symmetries (錯, 綜), eight of two and twelve of four',
        law='nuclear_run_act and classes_goAlike')),
    'changesAround_counts': ('model-witness', CENSUS.format(
        what='the changes around are one on twelve configurations, three on forty and five on twelve',
        law='changesAround_run and changesAround_values')),
    'orbit_census': ('model-witness', CENSUS.format(
        what='the six orbits of the law of waxing and waning, of twelve, twelve, twelve, twelve, four and twelve '
             'configurations, with their changes around',
        law='starts_return, orbitIndex_goAlike and reach_keeps_orbit')),
    'turn_fixed_iff': ('model-witness', ORDER.format(
        what='the configurations turning over leaves as they are are exactly those the order pairs by changing '
             'every line')),
    'both_fixed_iff': ('model-witness', ORDER.format(
        what='those that turning over and changing every line take to the same hexagram are exactly the pairs in '
             'which the two agree')),
    'Symmetry.comp_comm': ('support', 'any two of the four symmetries commute: a one-line unpacking of the module\'s '
                                      'own composition table, checked case by case'),
    'order_nodup': ('support', 'the received order lists each configuration once: a list lemma on the module\'s '
                               'imported list, read with mem_order so that a count over the order counts '
                               'configurations'),
}
data = json.loads(REG.read_text())
for name, (category, reason) in ENTRIES.items():
    full = f'Becoming.Hexagram.{name}'
    assert full not in data['roots'], full
    data['roots'][full] = {'module': MOD, 'category': category, 'reason': reason[0].upper() + reason[1:] + '.'}
REG.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n')
print('registered', len(ENTRIES))
