#!/usr/bin/env python3
"""U2c (18 October 2026): re-point the record references that `research.py check` reports as source drift, after
reading the change, with a history note naming each file and what U2c changed there. Only files U2c changed, and only
drift that the check reports, are re-pointed: references that do not drift are left as they are, and a reported path
without an entry in WHAT stops the script.

usage (from the repository root): python3 -B rehash_refs.py CHECK_OUTPUT
CHECK_OUTPUT is the saved output of `python3 -B tools/research/research.py check --changed-since BASE`."""
import hashlib, json, sys
from pathlib import Path

WHAT = {
    '_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md':
        'U2c recorded in D43 ("The joins") that the two trace laws flagged as possibly vacuous were checked: both '
        'traces exist, and each law now states its trace',
    'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md':
        'U2c updated the current receipt in section 9 (run, main commit, steps reused and run); the counts are '
        'unchanged',
}
WHAT_ZH = {
    '_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md':
        'U2c 在 D43（“接合”）中记下被标为可能空洞的两条迹之律已检查：两条迹都存在，各律现在陈述它的迹',
    'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md':
        'U2c 更新了第 9 节的当前回执（运行、main 提交、复用与运行的步数）；计数不变',
}

text = Path(sys.argv[1]).read_text()
check = json.loads(text[text.index('{'):])
drift = {}
for item in check['source_drift']:
    assert item['path'] in WHAT, item
    drift.setdefault(item['id'], set()).add(item['path'])
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
for rid, paths in sorted(drift.items()):
    f = Path(f'theories/becoming/results/records/{rid}.json')
    d = json.loads(f.read_text())
    done = []
    for r in d.get('references', []):
        if r.get('path') in paths and r.get('sha256') != sha(r['path']):
            r['sha256'] = sha(r['path'])
            done.append(r['path'])
    assert sorted(set(done)) == sorted(paths), (rid, done, paths)
    names = sorted({p.rsplit('/', 1)[-1] for p in paths})
    why = '; '.join(f'{p.rsplit("/", 1)[-1]}: {WHAT[p]}' for p in sorted(paths))
    why_zh = '；'.join(f'{p.rsplit("/", 1)[-1]}：{WHAT_ZH[p]}' for p in sorted(paths))
    d['history'].append({
        'en': f'18 October 2026, U2c (the two trace laws of Becoming.ProbeRunsInherited): {", ".join(names)} '
              f're-pointed after reading the change ({why}). The claim is unchanged.',
        'zh': f'2026年10月18日，U2c（Becoming.ProbeRunsInherited 的两条迹之律）：读过改动后，{"、".join(names)} '
              f'重新指向（{why_zh}）。论断不变。'})
    f.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(rid, names)
print(len(drift), 'records re-pointed')
