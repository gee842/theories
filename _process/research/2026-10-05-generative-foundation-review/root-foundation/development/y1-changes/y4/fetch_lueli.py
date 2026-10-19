#!/usr/bin/env python3
"""Preserve 王弼《周易略例》 from Chinese Wikisource (Y4), as Y1 preserved the 周易 and the 易传.

usage: python3 -I -B fetch_lueli.py            # fetch, write sources/zhouyi-yizhuan/lueli/, add to PROVENANCE.json

Each page is the MediaWiki API's response body, byte for byte as received (form "api-response"), with
the revision id, its timestamp, the SHA-256 of the bytes and of the wikitext. A page already bound by
the provenance is not fetched again."""
import datetime
import hashlib
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[7]
SRC = ROOT / 'sources/zhouyi-yizhuan'
API = 'https://zh.wikisource.org/w/api.php'
AGENT = 'theories-repository/1.0 (research archive; contact ren@datong.to)'
PAGES = [
    ('lueli/index.json', '周易略例'),
    ('lueli/mingtuan.json', '周易略例/明彖'),
    ('lueli/mingyao-tongbian.json', '周易略例/明爻通變'),
    ('lueli/minggua-shibian-tongyao.json', '周易略例/明卦適變通爻'),
    ('lueli/mingxiang.json', '周易略例/明象'),
    ('lueli/bianwei.json', '周易略例/辯位'),
    ('lueli/lueli-xia.json', '周易略例/略例下'),
    ('lueli/guale.json', '周易略例/卦略'),
]


def fetch(title):
    query = urllib.parse.urlencode({
        'action': 'query', 'prop': 'revisions', 'rvprop': 'ids|timestamp|content', 'rvslots': 'main',
        'format': 'json', 'formatversion': '2', 'redirects': '1', 'titles': title})
    request = urllib.request.Request(f'{API}?{query}', headers={'User-Agent': AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def main():
    prov_path = SRC / 'PROVENANCE.json'
    prov = json.loads(prov_path.read_text())
    bound = {f['file'] for f in prov['files']}
    start = datetime.datetime.now(datetime.timezone.utc)
    added = []
    for rel, title in PAGES:
        if rel in bound:
            continue
        raw = fetch(title)
        page = json.loads(raw)['query']['pages'][0]
        if page.get('missing') or page['title'] != title:
            sys.exit(f'{title}: missing or redirected to {page.get("title")}')
        rev = page['revisions'][0]
        text = rev['slots']['main']['content']
        out = SRC / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(raw)
        added.append({
            'file': rel, 'title': page['title'], 'pageid': page['pageid'], 'revid': rev['revid'],
            'revision_timestamp': rev['timestamp'],
            'revision_url': 'https://zh.wikisource.org/w/index.php?title='
                            + urllib.parse.quote(page['title'], safe='') + f"&oldid={rev['revid']}",
            'form': 'api-response', 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
            'wikitext_sha256': hashlib.sha256(text.encode()).hexdigest()})
        time.sleep(1)
    end = datetime.datetime.now(datetime.timezone.utc)
    prov['files'].extend(added)
    prov_path.write_text(json.dumps(prov, ensure_ascii=False, indent=1) + '\n')
    print(f'{len(added)} pages added, {start:%Y-%m-%d %H:%M}–{end:%H:%M} UTC')
    for a in added:
        print(a['file'], a['revid'], a['revision_timestamp'], a['bytes'])


if __name__ == '__main__':
    main()
