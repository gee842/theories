#!/usr/bin/env python3
"""Integration I4b: mark the readings of the three landed I4b records as taken by Ren (run from the repository root):
python3 -B mark_readings_taken.py

Ren, 16 October 2026, “agree with other readings”
(sources/15-codex-theory-conversations/2026-10-16-loops-readings-and-delegated-choices.md). The AI read this as
Ren taking I4b's three readings, and Ren did not correct it. Selection's reading (selection-by-the-record-alone) is not
among them: Ren questioned its framing the same day. Each record changes the reading's label only (the reading text
is unchanged), drops from next_delta the closest gaps that have since landed, cites the source and gains one paired,
dated history note. The study sections keep their “pending Ren” as evidence, as section 147 reads earlier sections.
Every replacement is asserted to apply once.
"""
import hashlib
import json
from pathlib import Path

RECORDS = Path('theories/becoming/results/records')
SOURCE = 'sources/15-codex-theory-conversations/2026-10-16-loops-readings-and-delegated-choices.md'
LABEL = (('Readings (the AI\'s, pending Ren):', 'Readings (the AI\'s, which Ren took on 16 October 2026):'),
         ('读法（AI 的，待 Ren）：', '读法（AI 的，Ren 2026-10-16 已取）：'))
ITEMS = {
    'every-origin-passes-the-gate': (143, {
        'en': ('; the other closest gaps (Horizon, Lasting, Selection, I4b).', '.'),
        'zh': ('；其余最近的缺口（Horizon、Lasting、Selection，I4b）。', '。')}),
    'what-a-finite-history-refutes': (145, {
        'en': ('; the other closest gaps (Lasting, Selection).', '.'),
        'zh': ('；其余最近的缺口（Lasting、Selection）。', '。')}),
    'lifting-where-branching-is-finite': (146, {
        'en': ('; the other closest gap (Selection).', '.'),
        'zh': ('；其余最近的缺口（Selection）。', '。')}),
}


def once(text, old, new):
    assert text.count(old) == 1, old
    return text.replace(old, new)


sha = hashlib.sha256(Path(SOURCE).read_bytes()).hexdigest()
for name, (section, delta) in ITEMS.items():
    path = RECORDS / f'{name}.json'
    raw = path.read_text()
    record = json.loads(raw)
    corr = record['correspondence']
    corr['en'] = once(corr['en'], *LABEL[0])
    corr['zh'] = once(corr['zh'], *LABEL[1])
    for lang in ('en', 'zh'):
        record['next_delta'][lang] = once(record['next_delta'][lang], *delta[lang])
    assert all(r['path'] != SOURCE for r in record['references'])
    record['references'].append({'path': SOURCE, 'role': 'provenance', 'sha256': sha})
    record['history'].append({
        'zh': f'2026年10月16日：Ren 同意交托之后提出的读法（“agree with other readings”）；AI 读作包括 I4b 的三项读法'
              f'（含本记录的），Ren 未更正。correspondence 把读法标为 AI 的、Ren 已取，读法文字不变；next_delta 删去此后已'
              f'落地的最近缺口。研究第{section}节的“待 Ren”作为证据保留。原措辞：“读法（AI 的，待 Ren）”。',
        'en': f'16 October 2026: Ren agreed with the readings posed after the delegation (“agree with other readings”); '
              f'the AI read this as taking I4b\'s three readings, this record\'s among them, and Ren did not correct it. '
              f'Correspondence marks the readings as the AI\'s which Ren took, the reading text unchanged; next_delta '
              f'drops the closest gaps that have since landed. Study section {section}\'s “pending Ren” stays as '
              f'evidence. Former wording: “Readings (the AI\'s, pending Ren)”.'})
    out = json.dumps(record, ensure_ascii=False, indent=2) + '\n'
    assert json.dumps(json.loads(raw), ensure_ascii=False, indent=2) + '\n' == raw, f'{name}: format round-trip'
    path.write_text(out)
    print(path)
