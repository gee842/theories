#!/usr/bin/env python3
"""Register Y1's apart roots in THEOREM-CONNECTIVITY-APART.json (the received order's length and pairing, facts of the
text's own list). usage: python3 -B register_apart.py [CHECKOUT_ROOT]"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE.parents[5]
REG = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY-APART.json'
ENTRIES = {
    'Becoming.Hexagram.order_length': {
        'module': 'Becoming.Hexagrams', 'category': 'support',
        'reason': 'The received order lists sixty-four hexagrams: a one-line unpacking of the module\'s own list.'},
    'Becoming.Hexagram.order_paired': {
        'module': 'Becoming.Hexagrams', 'category': 'model-witness',
        'reason': 'Each pair of the received order (序卦) is turned over or changed in every line: a fact about the '
                  'text\'s one constructed list, checked line by line, not a law of the unfolding; the order serves '
                  'the base as the list holding every configuration (mem_order).'},
}
data = json.loads(REG.read_text())
for name, entry in ENTRIES.items():
    assert name not in data['roots'], name
    data['roots'][name] = entry
REG.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n')
print('registered', len(ENTRIES))
