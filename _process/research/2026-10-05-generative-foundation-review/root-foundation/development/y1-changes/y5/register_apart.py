#!/usr/bin/env python3
"""Register Y5's apart roots in THEOREM-CONNECTIVITY-APART.json: the 雜卦's sequence and the received order's pairing
as facts about the texts' lists, the census of the twenty with three unbroken lines, the opposite stations of 說卦
ch. 5 against the pairs of ch. 3, the partner as a restatement of the pairing, and the parity of the count in phase.
Each is a fact about the texts' arrangements or a restatement, checked on them; the laws they instance are read on
the base along runs.
usage: python3 -B register_apart.py [CHECKOUT_ROOT]"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE.parents[6]
REG = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY-APART.json'
MOD = 'Becoming.HexagramSequences'
ZAGUA = ('{what}: a fact about the 雜卦\'s list, checked on it, its sequence matched to the preserved text by '
         'verify_mapping.py; a law running the list is read on the base by zagua_not_commutes, and the pairing as a '
         'law by partner_run')
ENTRIES = {
    'zagua_every': ('model-witness', ZAGUA.format(what='the 雜卦 lists each of the sixty-four configurations once')),
    'zagua_partners': ('model-witness', ZAGUA.format(what='the 雜卦\'s first fifty-six are twenty-eight pairs side '
                                                     'by side, each a configuration and its partner')),
    'zagua_last_eight': ('model-witness', ZAGUA.format(what='the 雜卦\'s last eight hold the remaining four pairs, '
                                                       'no partner beside partner')),
    'order_partners': ('model-witness', 'the received order sets every configuration beside its partner: a fact '
                       'about the order\'s list, checked pair by pair (order_paired read through the partner); a law '
                       'running the order is read on the base by runsOrder_agrees and runsOrder_not_commutes, and '
                       'the pairing as a law by partner_run'),
    'three_census': ('model-witness', 'the census of the configurations with three unbroken lines (twenty) and of '
                     '泰, 否 and the eighteen one exchange across from them (no two alike), counted over the received '
                     'order; the law it counts is read on the base by exchanges_from_tai_pi'),
    'Trigram.opposite_stations': ('model-witness', 'of the four pairs of opposite stations of 說卦 ch. 5 only 離 and 坎 '
                                  'are complements, while each of the four pairs of ch. 3 is: a fact about two '
                                  'arrangements of the text, checked on the eight trigrams; a law running the '
                                  'stations is read on the base by Trigram.stations_not_commutes'),
    'paired_iff_partner': ('restates', 'Paired (Becoming.Hexagrams, 非覆即變) restated as a configuration\'s partner, '
                           'a map; the pairing is read on the base as a law by partner_run'),
    'phaseCount_yangOdd': ('restates', 'phaseCount_parity (Becoming.HexagramPlaces) restated in the count of unbroken '
                           'lines: the count in phase has the other parity; the parity is read on the base by '
                           'run_yangOdd and changes_run_yangOdd'),
}
data = json.loads(REG.read_text())
for name, (category, reason) in ENTRIES.items():
    full = f'Becoming.Hexagram.{name}'
    assert full not in data['roots'], full
    data['roots'][full] = {'module': MOD, 'category': category, 'reason': reason[0].upper() + reason[1:] + '.'}
REG.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n')
print('registered', len(ENTRIES))
