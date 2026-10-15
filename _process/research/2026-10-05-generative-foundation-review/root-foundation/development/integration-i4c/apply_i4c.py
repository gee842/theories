#!/usr/bin/env python3
"""Integration I4c, header notes on the earlier versions: python3 -B apply_i4c.py notes | records

Ren, 16 October 2026, selected "Add the notes" for the 31 modules the I4a table reads as earlier versions
(sources/15-codex-theory-conversations/2026-10-16-i4-decisions.md). Run from the repository root.

* `notes` appends one bilingual comment to the first line of each earlier-version module, naming the spine
  declarations its row names and the relation. The note goes on the existing first line (after the import, or
  inside the opening comment), so no line number moves: the documents hold about 800 line-anchored links into
  these files. Statements and proofs are unchanged. Running it again changes nothing.
* `records` then rebinds the three records whose hashes read two of these files, each with a history entry:
  trace-law-equivalence (GenerativeModel, an integration reference), guarded-program-question-recovery
  (ExplanatoryResumptionCases, a counterexample reference) and residual-continuation-correspondence
  (ExplanatoryResumptionCases, a proof reference bound to the explanatory-resumption receipt). Run
  `python3 -B experiments/.../lean/deeper/check_explanatory_resumption.py` first: the proof binding moves to
  the receipt that checker writes for the new bytes, which must have passed. Nothing else in a record changes.
Then run `make research-render` and `make research-check`.
"""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path.cwd()
KIT = Path(__file__).resolve().parent
ROWS = KIT.parent / 'integration-i4a' / 'rows'
RECORDS = ROOT / 'theories/becoming/results/records'
DEEPER = 'experiments/integrated-correction/general-framework/generative-basis/lean/deeper/'
CASES = DEEPER + 'ExplanatoryResumptionCases.lean'
MODEL = 'experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeModel.lean'
VERIFICATION = DEEPER + 'explanatory-resumption-verification.json'
MARK = '脊柱上 / On the spine (I4'
RELATION = {
    'same': ('同一陈述', 'the same statement'),
    'spine-generalizes': ('脊柱的律更一般', 'the spine law is more general'),
    'instance': ('是其实例', 'an instance of it'),
}
HISTORY = ('2026-10-16，整合 I4c（Ren 选择“Add the notes”）：{file} 的第一行加一条注释，指向脊柱上陈述其主定理的声明；'
           '陈述与证明不变，行号不变。{what}',
           '16 October 2026, integration I4c (Ren selected “Add the notes”): the first line of {file} gains a comment '
           'naming the spine declarations that state its main theorem; statements, proofs and line numbers are '
           'unchanged. {what_en}')


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def earlier_versions():
    rows = [json.loads(line) for f in sorted(ROWS.glob('*.jsonl')) for line in f.read_text().splitlines() if line.strip()]
    return sorted((r for r in rows if r['category'] == 'earlier-version'), key=lambda r: r['path'])


def note(row):
    zh, en = RELATION[row['relation']]
    names = ', '.join(f'`{x}`' for x in row['spine'][:3])
    return f'{MARK}, 2026-10-16): {names} — {zh} / {en}; MODULE-CLASSIFICATION.md'


def notes():
    changed = 0
    for row in earlier_versions():
        path = ROOT / row['path']
        text = path.read_text()
        first, rest = text.split('\n', 1)
        if MARK in first:
            continue
        assert '-/' not in note(row) and '/-' not in note(row)
        if first.startswith('import '):
            first = f'{first} -- {note(row)}'
        else:
            assert first in ('/-', '/-!'), (row['path'], first)
            first = f'{first} {note(row)}'
        path.write_text(first + '\n' + rest)
        changed += 1
    print(json.dumps({'earlier_versions': len(earlier_versions()), 'annotated_now': changed}))


def load(name):
    return json.loads((RECORDS / f'{name}.json').read_text())


def save(name, record):
    (RECORDS / f'{name}.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')


def rehash(record, path):
    hits = [r for r in record['references'] if r['path'] == path]
    assert hits, path
    for r in hits:
        r['sha256'] = sha(path)


def history(record, file, what, what_en):
    zh, en = HISTORY
    record['history'].append({'zh': zh.format(file=file, what=what), 'en': en.format(file=file, what_en=what_en)})


def records():
    pointer = json.loads((ROOT / VERIFICATION).read_text())
    receipt_path = pointer['receipt']
    receipt = json.loads((ROOT / receipt_path).read_text())
    assert pointer['passed'] and receipt['passed'], receipt_path
    index = next(i for i, m in enumerate(receipt['modules']) if m['source'] == CASES)
    assert receipt['modules'][index]['sha256'] == sha(CASES), ('receipt predates the annotated source', receipt_path)
    stamp = receipt_path.split('/')[-2]

    r = load('trace-law-equivalence')
    rehash(r, MODEL)
    history(r, 'GenerativeModel.lean', '其集成引用改用新的哈希。', 'Its integration reference takes the new hash.')
    save('trace-law-equivalence', r)

    r = load('guarded-program-question-recovery')
    rehash(r, CASES)
    history(r, 'ExplanatoryResumptionCases.lean', '其反例引用改用新的哈希；ExplanatoryGuardedPrograms 的证明绑定不变。',
            'Its counterexample reference takes the new hash; the proof binding of ExplanatoryGuardedPrograms is '
            'unchanged.')
    save('guarded-program-question-recovery', r)

    r = load('residual-continuation-correspondence')
    rehash(r, CASES)
    binding = next(b for b in r['proof_bindings'] if b['source'] == CASES)
    binding['receipt'] = receipt_path
    binding['sha256_pointer'] = f'/modules/{index}/sha256'
    if not any(x['path'] == receipt_path for x in r['references']):
        r['references'].append({'path': receipt_path, 'role': 'receipt', 'sha256': sha(receipt_path), 'declarations': []})
    history(r, 'ExplanatoryResumptionCases.lean',
            f'其证明引用改用新的哈希，证明绑定移到 explanatory-resumption 检查器对新字节的回执（{stamp}，通过）；'
            'ExplanatoryResiduals 仍绑定原回执。',
            f'Its proof reference takes the new hash, and its proof binding moves to the explanatory-resumption '
            f'checker\'s receipt for the new bytes ({stamp}, passed); ExplanatoryResiduals stays bound to the '
            f'earlier receipt.')
    save('residual-continuation-correspondence', r)
    print(json.dumps({'receipt': receipt_path, 'module_index': index, 'records': 3}))


if __name__ == '__main__':
    {'notes': notes, 'records': records}[sys.argv[1]]()
