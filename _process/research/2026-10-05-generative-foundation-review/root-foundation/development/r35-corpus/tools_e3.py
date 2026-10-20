#!/usr/bin/env python3
"""R35 step 2(a), E3: adds `research.py compact-history` (classifier and compaction in tools/research/history_notes.py).
Run once from the checkout root: python3 -B tools_e3.py"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
p = ROOT / 'tools/research/research.py'
s = p.read_text()
pairs = [
    ("from tools.research import registry, navigation, lean_catalogue, reading_catalogue, style, paths, moves, indexes, session_map\n",
     "from tools.research import registry, navigation, lean_catalogue, reading_catalogue, style, paths, moves, indexes, session_map, history_notes\n"),
    ("    p = sub.add_parser('move', help=",
     "    p = sub.add_parser('compact-history', help='Condense bookkeeping history notes of records (dry run unless --apply); snapshot each record first')\n"
     "    p.add_argument('--apply', action='store_true')\n"
     "    p.add_argument('--ids', nargs='+')\n"
     "    p = sub.add_parser('move', help="),
    ("    elif args.command == 'snapshot':\n",
     "    elif args.command == 'compact-history':\n"
     "        result, code = compact_history(args.ids, args.apply), 0\n"
     "    elif args.command == 'snapshot':\n"),
    ("def main():\n",
     "def compact_history(ids=None, apply=False):\n"
     "    \"\"\"E3 (R35): condense the bookkeeping notes of record histories; see tools/research/history_notes.py.\"\"\"\n"
     "    from datetime import date\n"
     "    settings = json.loads((ROOT / '_process/research-config.json').read_text())\n"
     "    records = sorted(p for d in settings['record_directories'] for p in (ROOT / d).glob('*.json'))\n"
     "    if ids:\n"
     "        wanted = set(ids)\n"
     "        records = [p for p in records if p.stem in wanted]\n"
     "        missing = wanted - {p.stem for p in records}\n"
     "        if missing:\n"
     "            raise ValueError('no record with id ' + ', '.join(sorted(missing)))\n"
     "    if apply:\n"
     "        dirty = subprocess.run(['git', '-C', str(ROOT), 'status', '--porcelain', '--', *settings['record_directories']],\n"
     "                               capture_output=True, text=True, check=True).stdout\n"
     "        if dirty.strip():\n"
     "            raise ValueError('Refusing to compact with uncommitted record changes; commit them first')\n"
     "    receipt = ROOT / '_process/architecture/compactions' / f'{date.today().isoformat()}.json'\n"
     "    result = history_notes.compact(ROOT, records, registry.snapshot_record, apply=apply, receipt=receipt)\n"
     "    if apply:\n"
     "        result['receipt'] = str(receipt.relative_to(ROOT))\n"
     "    else:\n"
     "        result['records'] = [{k: r[k] for k in ('id', 'notes_before', 'condensed', 'kept')} for r in result['records']]\n"
     "    return result\n\n\n"
     "def main():\n"),
]
for a, b in pairs:
    assert s.count(a) == 1, a
    s = s.replace(a, b)
p.write_text(s)
print('patched')
