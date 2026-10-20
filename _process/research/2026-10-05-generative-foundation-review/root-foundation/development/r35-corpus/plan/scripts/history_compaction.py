#!/usr/bin/env python3
"""Read-only measure of the proposed E3 record-history compaction (R35).

Run from the repository root:  python3 -B history_compaction.py OUT_DIR
Reads theories/becoming/results/records/*.json, classifies every history note, and writes
OUT_DIR/history-compaction.tsv (per record: before, kept, condensed, bytes before/after) and
OUT_DIR/history-classes.json (counts and samples per class). Writes nothing in the repository.

Classes (first match wins, in this order):
  first        the record's first note (creation)                        -> keep
  substantive  claim, statement, title, premise, law, boundary, scope of claim, counterexample,
               name, status, migration, supersession, correction, reading -> keep
  bookkeeping  rebind / re-point / rehash / receipt / source maintenance /
               reconciliation with "unchanged" and nothing substantive      -> condense
  other        anything else                                               -> keep (conservative)
A substantive cue inside a bookkeeping note keeps it ("validation scope", "claim is unchanged"
and "names and statements unchanged" are removed before the substantive test).
"""
import glob, json, os, re, sys
from collections import Counter, defaultdict

OUT = sys.argv[1]
RECS = sorted(glob.glob('theories/becoming/results/records/*.json'))

STRONG = re.compile(
    r"\b(corrected|correction of|renam\w*|retitl\w*|the title|title becomes|now titled|migrat\w* to schema|schema 2|readability migration|"
    r"supersed\w*|withdrawn|counterexamples?\b|hypothes[ie]s|premises? (added|removed|changed|weakened|dropped)|"
    r"laws? (added|removed)|added as|^[^:]{0,60}: added|new laws?|restat\w*|strengthen\w*|generali[sz]\w*|"
    r"weaker premise|stronger (claim|theorem)|readings? (taken|decided|revised|replaced)|status (changed|becomes)|"
    r"does[_ ]not[_ ]show|statement (becomes|changed|revised)|claim (becomes|changed|revised|narrowed|widened)|"
    r"wording of the public fields|outdated labels|retired labels? replaced|vocabulary)", re.I)
BOOK = re.compile(
    r"re-?pointed|re-?point|rebound|re-?bind|rehash\w*|receipts?\b|source maintenance|source reconciliation|"
    r"reconciled after reading|reconciliation|drift|moved verbatim|move receipt|documentary correspondence|"
    r"reviewed only|pinned to (their )?existing|checker was rerun|declarations moved with their full", re.I)


def outer(t):
    """The note without parenthetical descriptions of other files' changes."""
    prev = None
    while prev != t:
        prev, t = t, re.sub(r'\([^()]*\)', ' ', t)
    return t


def text(h):
    if isinstance(h, dict):
        return h.get('en') or h.get('zh') or json.dumps(h, ensure_ascii=False)
    return str(h)


def classify(i, h):
    t = text(h)
    if i == 0:
        return 'first'
    if STRONG.search(outer(t)):
        return 'substantive'
    if BOOK.search(t):
        return 'bookkeeping'
    return 'other'


rows, classes, samples = [], Counter(), defaultdict(list)
tot_before = tot_after = 0
for p in RECS:
    raw = open(p, encoding='utf-8').read()
    r = json.loads(raw)
    hist = r.get('history', [])
    cls = [classify(i, h) for i, h in enumerate(hist)]
    for c, h in zip(cls, hist):
        classes[c] += 1
        if len(samples[c]) < 12 and (hash(text(h)) % 37 == 0):
            samples[c].append(r['id'] + ' | ' + text(h)[:260])
    kept = [h for c, h in zip(cls, hist) if c != 'bookkeeping']
    dropped = [h for c, h in zip(cls, hist) if c == 'bookkeeping']
    after = dict(r)
    if dropped:
        first = re.search(r'(\d{1,2} \w+ 2026|2026-\d\d-\d\d)', text(dropped[0]))
        last = re.search(r'(\d{1,2} \w+ 2026|2026-\d\d-\d\d)', text(dropped[-1]))
        kept = kept + [{'en': f'{len(dropped)} bookkeeping notes (rebinds, re-points, receipts) '
                              f'from {first.group(1) if first else "?"} to {last.group(1) if last else "?"} '
                              f'condensed; their text is kept in the snapshot named in text_versions and in git.'}]
    after['history'] = kept
    b0 = len(raw.encode())
    b1 = len((json.dumps(after, ensure_ascii=False, indent=2) + '\n').encode())
    tot_before += b0
    tot_after += b1
    rows.append((r['id'], len(hist), len(kept), len(dropped), cls.count('substantive'), cls.count('other'), b0, b1))

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, 'history-compaction.tsv'), 'w') as f:
    f.write('id\tnotes_before\tnotes_after\tcondensed\tsubstantive\tother_kept\tbytes_before\tbytes_after\n')
    for row in sorted(rows, key=lambda x: -x[1]):
        f.write('\t'.join(map(str, row)) + '\n')
summary = {
    'records': len(rows),
    'notes_before': sum(r[1] for r in rows),
    'notes_after': sum(r[2] for r in rows),
    'condensed': sum(r[3] for r in rows),
    'classes': dict(classes),
    'bytes_before': tot_before, 'bytes_after_estimate': tot_after,
    'records_with_no_bookkeeping': sum(1 for r in rows if r[3] == 0),
    'median_before': sorted(r[1] for r in rows)[len(rows) // 2],
    'median_after': sorted(r[2] for r in rows)[len(rows) // 2],
    'samples': samples,
}
json.dump(summary, open(os.path.join(OUT, 'history-classes.json'), 'w'), indent=1, ensure_ascii=False)
print(json.dumps({k: v for k, v in summary.items() if k != 'samples'}, indent=1))
