#!/usr/bin/env python3
"""R32: inside each folded section, the folded module's own `##` headings become `###`, under the section's
`##` heading (its former module doc), so no section heading stands empty over a heading of its own level.
usage: python3 -B headings.py"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fold  # noqa: E402

n = 0
for x, s in fold.FOLDS:
    path = fold.B / f'{s}.lean'
    text = path.read_text()
    a = text.index(f'\nsection {x}\n')
    b = text.index(f'\nend {x}\n', a)
    part = text[a:b]
    head = part.index('/-!\n## ')  # the section's heading
    rest = part[head + 7:]
    rest, k = re.subn(r'/-! ## ', '/-! ### ', rest)
    n += k
    path.write_text(text[:a] + part[:head + 7] + rest + text[b:])
print(n, 'headings')
