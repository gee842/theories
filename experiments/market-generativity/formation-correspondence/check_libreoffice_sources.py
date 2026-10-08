#!/usr/bin/env python3
"""Check retained primary-source bytes and selected historical text anchors.

These are provenance/content checks, not causal identification, proof checking,
software execution or an audit of the organizations' financial accounts.
"""
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'sources/market-generativity/libreoffice-formation'


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


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    manifest = json.loads((SOURCE / 'manifest.json').read_text())
    anchors = {
        'launch': ['September 28, 2010', 'Pending this decision', 'beta version', 'Steering Committee'],
        'first-stable': ['January 25, 2011', 'first stable release', 'independent process', '75 to 11GB'],
        'endowment': ['2011-02-25', 'eight days', 'frozen assets', 'ongoing running costs'],
        'continued-release': ['March 22, 2011', 'operating expenses', 'infrastructure costs'],
        'distribution': ['Thu Mar 31', '2011', 'LibreOffice 3.3.2', 'default office package'],
        'incorporation': ['February 17th, 2012', 'interim legal entity', 'Freies Office Deutschland'],
        'other-continuation': ['18 October 2012', 'In May 2012', 'incompatibly-licensed libraries'],
    }
    expected_dates = {
        'launch': '2010-09-28', 'first-stable': '2011-01-25',
        'endowment': '2011-02-25', 'continued-release': '2011-03-22',
        'distribution': '2011-03-31', 'incorporation': '2012-02-20',
        'other-continuation': '2012-10-18',
    }
    rows = []
    assert {r['id'] for r in manifest['sources']} == set(anchors)
    for row in manifest['sources']:
        path = SOURCE / row['file']
        assert path.stat().st_size == row['bytes']
        assert digest(path) == row['sha256']
        assert row['publication_date'] == expected_dates[row['id']]
        parser = Visible()
        parser.feed(path.read_text(encoding='utf-8'))
        visible = re.sub(r'\s+', ' ', ' '.join(parser.parts))
        for anchor in anchors[row['id']]:
            assert anchor.casefold() in visible.casefold(), (row['id'], anchor)
        rows.append({'id': row['id'], 'sha256': row['sha256'],
                     'anchors_checked': anchors[row['id']]})
    # Chronology concerns published milestones, not an invented exhaustion date.
    assert expected_dates['first-stable'] < expected_dates['endowment']
    assert expected_dates['distribution'] < '2012-02-17' < expected_dates['incorporation']
    receipt = {
        'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'manifest_sha256': digest(SOURCE / 'manifest.json'),
        'checker_sha256': digest(Path(__file__)), 'source_checks': rows,
        'scope': 'Seven retained primary statements and text anchors; publication/event dates '
                 'distinguished. No new mathematical theorem, executable software test, '
                 'causal effect size, full financial ledger, measured stock threshold or '
                 'independent-agent review.'}
    (Path(__file__).parent / 'libreoffice-source-checks.json').write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': 'passed', 'sources': len(rows),
                      'scope': 'source preservation and selected content only'}))


if __name__ == '__main__':
    main()
