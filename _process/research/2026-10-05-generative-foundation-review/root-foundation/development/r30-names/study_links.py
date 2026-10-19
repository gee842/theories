"""R30: earlier sections of the study (en, zh) link to the files of renamed modules. The text of those sections is
history and keeps its words and names; only a link's target follows the table's `paths`, so the link resolves.
Run from the checkout root."""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
PATHS = json.loads((HERE / 'RENAME-TABLE.json').read_text())['paths']
TAIL = {o.split('lean/becoming/', 1)[1]: n.split('lean/becoming/', 1)[1] for o, n in PATHS.items()}
for name in ('BECOMING-RENEWAL-READING.md', 'BECOMING-RENEWAL-READING.zh.md'):
    f = HERE.parents[1] / name
    s = f.read_text(encoding='utf-8')
    n = 0

    def fix(m):
        global n
        t = m.group(1)
        for o, new in TAIL.items():
            if t.endswith('lean/becoming/' + o) or ('lean/becoming/' + o + '#') in t:
                n += 1
                return '](' + t.replace('lean/becoming/' + o, 'lean/becoming/' + new) + ')'
        return m.group(0)
    s = re.sub(r'\]\(([^)\s]+)\)', fix, s)
    f.write_text(s, encoding='utf-8')
    print(name, n)
