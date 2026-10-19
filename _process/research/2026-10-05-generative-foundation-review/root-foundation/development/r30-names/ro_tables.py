"""R30: the Chinese-sources chapter's passage tables, between their markers, are written from passages.json by
verify_ro.py's own `table` (the RO build renames declarations through the R22 and R30 tables). Run from anywhere."""
import importlib.util
import json
from pathlib import Path

RO = Path(__file__).resolve().parent.parent / 'ro-relational-sources'
spec = importlib.util.spec_from_file_location('verify_ro', RO / 'verify_ro.py')
V = importlib.util.module_from_spec(spec)
spec.loader.exec_module(V)
passages = json.loads((RO / 'passages.json').read_text())['passages']
s = V.CHAPTER.read_text(encoding='utf-8')
changed = []
for t in V.TRADITIONS:
    a = s.index(V.begin(t)) + len(V.begin(t))
    b = s.index(V.end(t))
    new = '\n' + V.table(passages, t) + '\n'
    if s[a:b].strip() != new.strip():
        changed.append(t)
        s = s[:a] + new + s[b:]
V.CHAPTER.write_text(s, encoding='utf-8')
print('tables rewritten:', changed)
