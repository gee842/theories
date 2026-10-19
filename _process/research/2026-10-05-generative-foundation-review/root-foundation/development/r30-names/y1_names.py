"""R30: the Y1 passage map (development/y1-changes/passages.json, edited in place by every Y landing; it has no
build) names declarations R30 renamed. Read as it was on main before R30 (BASE), so that a rerun gives the same
bytes, each passage's declarations take their new names, and a name in its reading is renamed by the RO build's
rules (build_passages.rename_text_r30: a qualified suffix, or a one-component name that cannot be an English word);
the reading's words do not change. Then the chapter on the 易传's passage table, between its markers, is written by
verify_mapping.py's own `table`. Run from anywhere."""
import importlib.util
import json
import subprocess
from pathlib import Path

BASE = '4cc010fb0'
DEV = Path(__file__).resolve().parent.parent
ROOT = DEV.parents[4]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


V = load('verify_mapping', DEV / 'y1-changes/verify_mapping.py')
REN = json.loads((DEV / 'r30-names/RENAME-TABLE.json').read_text())['declarations']
B = load('build_passages', DEV / 'ro-relational-sources/build_passages.py')
P = DEV / 'y1-changes/passages.json'
data = json.loads(subprocess.run(['git', 'show', f'{BASE}:{P.relative_to(ROOT)}'], cwd=ROOT, capture_output=True,
                                 check=True).stdout)
n = 0
for p in data['passages']:
    before = (list(p['declarations']), p['reading'])
    p['declarations'] = [REN.get(d, d) for d in p['declarations']]
    p['reading'] = B.rename_text_r30(p['reading'], B.R30_WINDOWS, B.R30_WORDS)
    if (p['declarations'], p['reading']) != before:
        n += 1
P.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n')
s = V.CHAPTER.read_text(encoding='utf-8')
a = s.index(V.BEGIN) + len(V.BEGIN)
b = s.index(V.END)
t = V.table(data['passages'])
if s[a:b].strip() != t:
    s = s[:a] + '\n' + t + '\n' + s[b:]
    V.CHAPTER.write_text(s, encoding='utf-8')
    print('chapter table rewritten')
print(n, 'passages renamed')
