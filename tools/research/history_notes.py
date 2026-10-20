#!/usr/bin/env python3
"""Classify and compact the history notes of result records (R35, E3).

A record's `history` grew by one note per landing that re-pointed a hash or rebound a receipt, so most
notes said only that bookkeeping changed. Compaction keeps every note that says what the record says or
why it changed, replaces the bookkeeping notes by one counting note, and stores the record's exact bytes
before compaction as a snapshot under `record_snapshots` (named in the condensing note, and listed in
`text_versions` for schema-2 records), so no note is lost: the snapshot and git keep each one.

Classes, first match wins:
  first        the record's first note (its creation)                                   kept
  substantive  a cue that the record's claim, statement, title, premises, laws, scope,
               status, readings or vocabulary changed, or that it was corrected,
               superseded or migrated (parenthetical descriptions of other files'
               changes are removed before this test)                                    kept
  bookkeeping  a rebind, re-point, rehash, receipt, drift, reconciliation or source-
               maintenance cue and no substantive cue                                   condensed
  other        anything else                                                            kept

Since R35, bookkeeping re-points write no note at all (tools/research/repoint.py logs them in
_process/architecture/rebinds.jsonl), so compaction is needed once, not after every landing.

usage (from the checkout root): python3 -B tools/research/research.py compact-history [--apply] [--ids ID ...]
"""
import hashlib
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path

STRONG = re.compile(
    r"\b(corrected|correction of|renam\w*|retitl\w*|the title|title becomes|now titled|migrat\w* to schema|schema 2|"
    r"readability migration|supersed\w*|withdrawn|counterexamples?\b|hypothes[ie]s|"
    r"premises? (added|removed|changed|weakened|dropped)|laws? (added|removed)|added as|^[^:]{0,60}: added|new laws?|"
    r"new theorems?|restat\w*|strengthen\w*|generali[sz]\w*|weaker premise|stronger (claim|theorem)|"
    r"readings? (taken|decided|revised|replaced|adopted)|status (changed|becomes)|does[_ ]not[_ ]show|"
    r"statement (becomes|changed|revised)|claim (becomes|changed|revised|narrowed|widened)|"
    r"wording of the public fields|outdated labels|retired labels? replaced|vocabulary)", re.I)
BOOK = re.compile(
    r"re-?pointed|re-?point|rebound|re-?bind|rehash\w*|receipts?\b|source maintenance|source reconciliation|"
    r"reconciled after reading|reconciliation|drift|moved verbatim|move receipt|documentary correspondence|"
    r"reviewed only|pinned to (their )?existing|checker was rerun|declarations moved with their full", re.I)
DATE = re.compile(r'(\d{1,2} (?:January|February|March|April|May|June|July|August|September|October|November|December) 20\d\d'
                  r'|20\d\d-\d\d-\d\d)')
MARK = re.compile(r'bookkeeping notes? condensed')


def outer(text):
    """The note without parenthetical descriptions of other files' changes."""
    previous = None
    while previous != text:
        previous, text = text, re.sub(r'\([^()]*\)', ' ', text)
    return text


def note_text(note):
    if isinstance(note, dict):
        return note.get('en') or note.get('zh') or ''
    return str(note)


def classify(index, note):
    text = note_text(note)
    if index == 0:
        return 'first'
    if MARK.search(text):
        return 'other'
    if STRONG.search(outer(text)):
        return 'substantive'
    if BOOK.search(text):
        return 'bookkeeping'
    return 'other'


def dates(notes):
    found = [m.group(1) for m in (DATE.search(note_text(n)) for n in notes) if m]
    return (found[0], found[-1]) if found else (None, None)


def condensing_note(count, first, last, snapshot):
    span = f' from {first} to {last}' if first and last and first != last else f' of {first}' if first else ''
    span_zh = f'（{first} 至 {last}）' if first and last and first != last else f'（{first}）' if first else ''
    return {'en': f'{date.today().isoformat()}: {count} bookkeeping {"note" if count == 1 else "notes"} condensed{span}: receipts rebound, sources re-pointed or rehashed '
                  f'after reading their changes, with the claim unchanged. Each note is kept verbatim in the snapshot '
                  f'{snapshot} and in git.',
            'zh': f'{date.today().isoformat()}：{count} 条记账性说明合并{span_zh}：收据重绑、来源重指或重算哈希，主张不变。'
                  f'每条原文保存在快照 {snapshot} 和 git 中。'}


def plan(record):
    """(kept notes in order with the condensing note appended, condensed notes, class counts)."""
    history = record.get('history', [])
    classes = [classify(i, n) for i, n in enumerate(history)]
    kept = [n for c, n in zip(classes, history) if c != 'bookkeeping']
    dropped = [n for c, n in zip(classes, history) if c == 'bookkeeping']
    return kept, dropped, Counter(classes)


def dump(record):
    return json.dumps(record, ensure_ascii=False, indent=2) + '\n'


def compact(root, record_paths, snapshot, apply=False, receipt=None):
    """Compact each record with at least one bookkeeping note. `snapshot(id)` stores the exact bytes and
    returns its text_versions entry. Returns the receipt data."""
    rows, totals = [], Counter()
    for path in record_paths:
        raw = path.read_bytes()
        record = json.loads(raw)
        kept, dropped, classes = plan(record)
        totals.update(classes)
        if not dropped:
            continue
        first, last = dates(dropped)
        row = {'id': record['id'], 'notes_before': len(record['history']), 'condensed': len(dropped),
               'kept': len(kept), 'classes': dict(classes), 'sha256_before': hashlib.sha256(raw).hexdigest()}
        if apply:
            entry = snapshot(record['id'])
            entry['note'] = {'en': 'Exact record bytes before its history was compacted (R35, E3); every condensed '
                                   'note is kept here.',
                             'zh': '历史说明压缩前的记录原始字节（R35，E3）；每条被合并的说明都保存在这里。'}
            if record.get('schema_version') == 2:
                # Schema-1 records carry no text_versions; their condensing note names the snapshot.
                record['text_versions'] = record.get('text_versions', []) + [entry]
            record['history'] = kept + [condensing_note(len(dropped), first, last, entry['path'])]
            data = dump(record)
            path.write_text(data)
            row['snapshot'] = entry['path']
            row['sha256_after'] = hashlib.sha256(data.encode()).hexdigest()
        rows.append(row)
    result = {'date': date.today().isoformat(), 'applied': apply, 'records_read': len(record_paths),
              'records_compacted': len(rows), 'notes_before': sum(totals.values()),
              'notes_condensed': sum(r['condensed'] for r in rows),
              'notes_after': sum(totals.values()) - sum(r['condensed'] for r in rows) + len(rows),
              'classes': dict(totals), 'records': rows}
    if apply and receipt is not None:
        receipt.parent.mkdir(parents=True, exist_ok=True)
        if receipt.exists():
            raise ValueError('Refusing to overwrite compaction receipt: ' + str(receipt))
        receipt.write_text(json.dumps(result, ensure_ascii=False, indent=1) + '\n')
    return result
