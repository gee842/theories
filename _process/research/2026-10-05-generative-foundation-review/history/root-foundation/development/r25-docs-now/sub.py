#!/usr/bin/env python3
"""R25 helper: apply exact replacements from a JSON list [[path, old, new], ...]; each old must occur exactly once."""
import json, sys
pairs = json.load(open(sys.argv[1]))
files = {}
for p, old, new in pairs:
    s = files.get(p) or open(p, encoding='utf-8').read()
    n = s.count(old)
    if n != 1:
        sys.exit(f'{p}: {n} occurrences of {old[:80]!r}')
    files[p] = s.replace(old, new)
for p, s in files.items():
    open(p, 'w', encoding='utf-8').write(s)
print(len(pairs), 'replacements in', len(files), 'files')
