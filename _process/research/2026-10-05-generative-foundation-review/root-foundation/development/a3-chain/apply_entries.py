#!/usr/bin/env python3
"""A3: apply the entry revisions of revisions.json to the chain's data.

Each text edit replaces one exact fragment of one field of one entry; the fragment must occur exactly once, or the
script stops before writing. Each link edit replaces the path and labels of the one link of the entry whose path is
`old_path`. The newly linked pages of reading.json (`newly_linked`) enter `reviewed_sources` with the hash read, only
where the file is still that version; otherwise the script stops, since the page must be read again. The data's
`updated` field becomes the landing date. Nothing else in the data changes.

usage (from the repository root): python3 -B apply_entries.py DATE [--dry]
"""
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, '.')
from tools.research import generative_chain as chain  # noqa: E402

HERE = Path(__file__).resolve().parent


def entries(data):
    return {e['id']: e for s in data['sections'] for e in s['entries']}


def main():
    date, dry = sys.argv[1], '--dry' in sys.argv
    revisions = json.loads((HERE / 'revisions.json').read_text())
    reading = json.loads((HERE / 'reading.json').read_text())
    data = chain.read_data()
    by_id = entries(data)
    for edit in revisions['text']:
        entry = by_id[edit['entry']]
        text = entry[edit['field']]
        count = text.count(edit['old'])
        if count != 1:
            raise SystemExit(f"{edit['entry']} {edit['field']}: fragment occurs {count} times: {edit['old'][:80]}")
        entry[edit['field']] = text.replace(edit['old'], edit['new'])
    for edit in revisions['links']:
        links = [link for link in by_id[edit['entry']]['links'] if link['path'] == edit['old_path']]
        if len(links) != 1:
            raise SystemExit(f"{edit['entry']}: {len(links)} links to {edit['old_path']}")
        links[0].update(path=edit['new_path'], label_zh=edit['label_zh'], label_en=edit['label_en'])
    for name, item in reading['newly_linked'].items():
        current = hashlib.sha256((chain.ROOT / name).read_bytes()).hexdigest()
        if current != item['sha256']:
            raise SystemExit(f'{name} changed since it was read; read it again and update reading.json')
        data['reviewed_sources'][name] = current
    data['updated'] = date
    errors = chain.validate(data)
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f"{len(revisions['text'])} text edits, {len(revisions['links'])} link edits, "
          f"{len(reading['newly_linked'])} newly linked pages; validate passes")
    if not dry:
        chain.write_data(data)


if __name__ == '__main__':
    main()
