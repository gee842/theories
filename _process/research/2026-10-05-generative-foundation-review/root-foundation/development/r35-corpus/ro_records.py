#!/usr/bin/env python3
"""R35 step 2(d), E4, in the RO passage map: record ids follow the renamed records. passages.json changes only through
build_passages.py, so the builder gains a rename step for record ids (from the rename receipts under
_process/architecture/renames/), applied like the declaration renames, after FIXES. Run once from the checkout root:
python3 -B ro_records.py"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
p = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation/development/ro-relational-sources/build_passages.py'
s = p.read_text()
pairs = [
    ("RENAMES = renamed()\nR30_WINDOWS, R30_WORDS = r30_rules()\n",
     "RENAMES = renamed()\nR30_WINDOWS, R30_WORDS = r30_rules()\n\n"
     "# Renamed records (R35, E4): a passage's records, and record ids named in its readings, follow the record renames\n"
     "# (receipts in _process/architecture/renames/), claims unchanged. Applied after FIXES, so a FIXES entry may still\n"
     "# name a former id.\n"
     "RECORDS_RENAMED_WHY = 'record ids follow the renamed records (R35; receipts in _process/architecture/renames), claims unchanged'\n\n\n"
     "def renamed_records():\n"
     "    out = {}\n"
     "    for f in sorted((V.ROOT / '_process/architecture/renames').glob('*.json')):\n"
     "        for x in json.loads(f.read_text())['renames']:\n"
     "            out[x['old']] = x['new']\n"
     "    return out\n\n\n"
     "def rename_records_text(s, table):\n"
     "    import re\n"
     "    for old, new in table.items():\n"
     "        s = re.sub(r'(?<![A-Za-z0-9_-])' + re.escape(old) + r'(?![A-Za-z0-9_-])', new, s)\n"
     "    return s\n\n\n"
     "RECORD_RENAMES = renamed_records()\n"),
    ("            if (p['declarations'], p['reading'], p['reading_en']) != before:\n"
     "                p['corrected'] = (p['corrected'] + '; ' if p.get('corrected') else '') + RENAMED_WHY\n",
     "            if (p['declarations'], p['reading'], p['reading_en']) != before:\n"
     "                p['corrected'] = (p['corrected'] + '; ' if p.get('corrected') else '') + RENAMED_WHY\n"
     "            before = (p['records'], p['reading'], p['reading_en'])\n"
     "            p['records'] = [RECORD_RENAMES.get(r, r) for r in p['records']]\n"
     "            p['reading'] = rename_records_text(p['reading'], RECORD_RENAMES)\n"
     "            p['reading_en'] = rename_records_text(p['reading_en'], RECORD_RENAMES)\n"
     "            if (p['records'], p['reading'], p['reading_en']) != before:\n"
     "                p['corrected'] = (p['corrected'] + '; ' if p.get('corrected') else '') + RECORDS_RENAMED_WHY\n"),
]
for a, b in pairs:
    assert s.count(a) == 1, a[:60]
    s = s.replace(a, b)
p.write_text(s)
print('patched')
