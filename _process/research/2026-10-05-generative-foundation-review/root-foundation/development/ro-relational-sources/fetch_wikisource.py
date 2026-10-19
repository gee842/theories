#!/usr/bin/env python3
"""Retrieve Chinese Wikisource pages through the MediaWiki API, as Y1 did, into
sources/chinese-classical-texts/wikisource/. usage: python3 -B fetch_wikisource.py TITLE [TITLE ...]
Each page is written as the API's response body, byte for byte as received, under a file name made
from the title ('/' becomes '__', ':' and ' ' become '_'). Existing files are never overwritten (the bytes of a source never
change); a title already retrieved is skipped."""
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
OUT = ROOT / 'sources/chinese-classical-texts/wikisource'
API = 'https://zh.wikisource.org/w/api.php'
AGENT = 'theories-research-retrieval/1.0 (https://github.com/yongxu/theories; preservation of cited passages)'


def name(title):
    return title.replace('/', '__').replace(' ', '_').replace(':', '_') + '.json'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for title in sys.argv[1:]:
        path = OUT / name(title)
        if path.exists():
            print('kept', path.name)
            continue
        query = urllib.parse.urlencode({'action': 'query', 'prop': 'revisions', 'titles': title,
                                        'rvprop': 'ids|timestamp|content', 'rvslots': 'main',
                                        'format': 'json', 'formatversion': '2', 'redirects': '1'})
        req = urllib.request.Request(f'{API}?{query}', headers={'User-Agent': AGENT})
        with urllib.request.urlopen(req, timeout=60) as r:
            body = r.read()
        page = json.loads(body)['query']['pages'][0]
        if 'missing' in page or 'revisions' not in page:
            print('MISSING', title)
            continue
        path.write_bytes(body)
        rev = page['revisions'][0]
        print('wrote', path.name, rev['revid'], rev['timestamp'], len(body))
        time.sleep(1)


if __name__ == '__main__':
    main()
