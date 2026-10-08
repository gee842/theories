#!/usr/bin/env python3
"""Extract published summaries; do not manufacture replicate observations."""
import csv
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[6]
HERE = Path(__file__).resolve().parent
SOURCE = ROOT / 'sources/evolutionary-selection/koza-2011/article.html'


class TableReader(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rows, self.row, self.cell = [], [], None
    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            self.row = []
        if tag in ('td', 'th'):
            self.cell = []
    def handle_data(self, data):
        if self.cell is not None:
            self.cell.append(data)
    def handle_endtag(self, tag):
        if tag in ('td', 'th') and self.cell is not None:
            self.row.append(' '.join(''.join(self.cell).split()))
            self.cell = None
        if tag == 'tr':
            self.rows.append(self.row)


def extract():
    html = SOURCE.read_text()
    block = html.split('id="tbl1"', 1)[1].split('</table>', 1)[0]
    reader = TableReader()
    reader.feed(block)
    assert len(reader.rows) == 4, reader.rows
    assert 'static' in reader.rows[0][1] and 'shaken' in reader.rows[0][2]
    assert ['High' in x for x in reader.rows[1][1:]] == [True, False, True, False]
    conditions = [('static', 'high'), ('static', 'low'), ('shaken', 'high'), ('shaken', 'low')]
    rows = []
    for source_row in reader.rows[2:]:
        for (mixing, oxygen), value in zip(conditions, source_row[1:], strict=True):
            match = re.fullmatch(r'([0-9.]+)±([0-9.]+)([a-z])', value)
            assert match, value
            mean, se, group = match.groups()
            rows.append(dict(strain=source_row[0], mixing=mixing, oxygen=oxygen,
                             mean=mean, se=se, group=group, unit='delta_OD600_per_hour',
                             locator='tbl1', source_value=value))
    with (HERE / 'growth-summary.csv').open('w', newline='') as out:
        writer = csv.DictWriter(out, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    section = html.split('id="sec16"', 1)[1].split('</section>', 1)[0]
    means = re.findall(r'<em>W</em>=([0-9.]+)±([0-9.]+)', section)
    assert len(means) == 2, means
    methods = html.split('id="sec9"', 1)[1].split('</section>', 1)[0]
    assert '<em>n</em>=8' in methods
    result = dict(source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                  growth_summary_rows=len(rows), growth_rows_are_replicates=False,
                  growth_sampling='Five destructively sampled microcosms per incubation period; reported maximum growth rates.',
                  competition=[dict(oxygen=oxygen, mean=mean, se=se,
                                    focal='WS', comparator='SM-13', n=8,
                                    hours=48, mixing='static', locator='sec16')
                               for oxygen, (mean, se) in zip(('high', 'low'), means)],
                  competition_target='ratio of log fold changes in cell counts; not a survival probability',
                  raw_replicates_retrieved=False,
                  fitted_mat_viability_model=False,
                  inference='Reported mean competitive advantage changes sign around W=1 between oxygen conditions; no new significance test.')
    (HERE / 'oxygen-summary.json').write_text(json.dumps(result, indent=2)+'\n')
    return result


if __name__ == '__main__':
    print(json.dumps(extract(), indent=2))
