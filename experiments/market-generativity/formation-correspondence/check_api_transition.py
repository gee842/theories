#!/usr/bin/env python3
"""Preserved-source checks for a scoped API transition assessment, not a proof."""
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'sources/market-generativity/api-transition'


class Visible(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.hidden = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in {'script', 'style'}:
            self.hidden += 1

    def handle_endtag(self, tag):
        if tag in {'script', 'style'}:
            self.hidden -= 1

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    manifest = json.loads((SOURCE / 'manifest.json').read_text())
    anchors = {
        'apollo-plan': ['iamthatis', '50,000 yearly subscribers', 'app review',
                        'July 1st', 'June 30th will be Apollo'],
        'narwhal-unfinished': ['det0ur', "won't be able to finish Narwhal 2", 'July 1st',
                               'still waiting to hear back'],
        'narwhal-bridge': ['det0ur', 'not going anywhere on July 1st', 'Over the next few months'],
        'narwhal-release': ['det0ur', 'Narwhal 2 is finally here', 'require subscriptions in a couple weeks'],
        'narwhal-pricing': ['det0ur', '$3.99/month', 'Can I pay annually',
                            'worried about Reddit increasing the price'],
        'reddit-facts': ['June 15, 2023', 'June 30, 2023', 'Narwhal', 'infrastructure',
                         'opportunity costs', 'July 1', '$0.24'],
        'apollo-ended': ['shut down on June 30, 2023'],
        'post-dates': ['Thursday June 08 2023', 'Tuesday June 27 2023',
                       'Wednesday September 27 2023', 'Monday October 09 2023'],
    }
    expected_dates = {'apollo-plan': '2023-06-08', 'narwhal-unfinished': '2023-06-08',
                      'narwhal-bridge': '2023-06-27', 'narwhal-release': '2023-09-27',
                      'narwhal-pricing': '2023-10-09', 'reddit-facts': '2023-06-15',
                      'apollo-ended': None, 'post-dates': None}
    checked = []
    assert {r['id'] for r in manifest['sources']} == set(anchors)
    for row in manifest['sources']:
        path = SOURCE / row['file']
        assert sha(path) == row['sha256']
        assert path.stat().st_size == row['bytes']
        assert row['publication_date'] == expected_dates[row['id']]
        raw = path.read_text()
        if path.suffix == '.html':
            assert row['representation'] == 'unaltered HTML response'
            parser = Visible()
            parser.feed(raw)
            raw = ' '.join(parser.parts)
        else:
            assert 'not original server HTML' in row['representation']
            if row['id'] != 'post-dates':
                # Only the main author post is checked, not statements in replies.
                raw = raw.split('Sort by:')[0]
        normalized = re.sub(r'\s+', ' ', raw).casefold()
        for anchor in anchors[row['id']]:
            assert anchor.casefold() in normalized, (row['id'], anchor)
        checked.append({'id': row['id'], 'sha256': row['sha256'],
                        'representation': row['representation'], 'anchors': anchors[row['id']]})
    assert expected_dates['narwhal-unfinished'] < expected_dates['narwhal-bridge'] < '2023-07-01'
    assert '2023-07-01' < expected_dates['narwhal-release'] < expected_dates['narwhal-pricing']
    result = {
        'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'manifest_sha256': sha(SOURCE / 'manifest.json'), 'checker_sha256': sha(Path(__file__)),
        'source_checks': checked, 'primary_statements': 7, 'newly_examined_posts': 5,
        'scope': 'Saved representations, main-post attribution anchors and dated milestone order. '
                 'Not contemporaneous snapshots, a prospective prediction, causal identification, '
                 'financial/contract audit, proof of nonstop operation or a new mathematical theorem.'}
    (Path(__file__).parent / 'api-transition-source-checks.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': 'passed', 'documents': len(checked), 'new_posts': 5}))


if __name__ == '__main__':
    main()
