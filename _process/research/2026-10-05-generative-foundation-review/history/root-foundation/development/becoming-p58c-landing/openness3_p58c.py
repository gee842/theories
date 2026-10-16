#!/usr/bin/env python3
"""P58c: Openness's flow form is `Flow.exchange_not_recurring_around`, since Resolution already has
`Flow.exchange_not_recurring` (taking at least 1/p of the unit). Usage: openness3_p58c.py TREE"""
import sys
from pathlib import Path
p = Path(sys.argv[1]) / 'Becoming/Openness.lean'; t = p.read_text()
for old, new in [('(`Flow.exchange_not_recurring`, `World.exchange_not_recurring`)', '(`Flow.exchange_not_recurring_around`, `World.exchange_not_recurring`)'),
                 ('theorem exchange_not_recurring (balances : L.Balances W)', 'theorem exchange_not_recurring_around (balances : L.Balances W)'),
                 ('arbitrarily late steps (`Flow.exchange_not_recurring`). This', 'arbitrarily late steps (`Flow.exchange_not_recurring_around`). This'),
                 ('  Flow.exchange_not_recurring balanced dissipative standing around', '  Flow.exchange_not_recurring_around balanced dissipative standing around')]:
    assert t.count(old) == 1, old
    t = t.replace(old, new)
p.write_text(t); print('ok')
