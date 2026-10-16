#!/usr/bin/env python3
"""Finalize P83 totals and its reading entry after apply_docs.py and both passed receipts.

Usage: python3 -B land_docs.py ROOT [BASE]
BASE defaults to HEAD and must precede this landing. Its chapter hash guards the refresh; mismatched
prior content must be read and reconciled, not overwritten. Run before make_records.py and repoint.py.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import totals

ROOT = Path(sys.argv[1]).resolve()
BASE = sys.argv[2] if len(sys.argv) > 2 else 'HEAD'
path = ROOT / 'theories/becoming/results/data/arguments-m-z.json'
raw = path.read_text()
data = json.loads(raw)
entry = next(item for item in data if item['id'] == 'the-theory-of-becoming')
base = subprocess.run(['git', 'show', f'{BASE}:{totals.CHAPTER}'], cwd=ROOT,
                      capture_output=True, check=True).stdout
assert entry['source_sha256'] == hashlib.sha256(base).hexdigest(), \
    'reading entry differs from the pre-landing chapter; read and reconcile before refreshing it'
totals.update(ROOT)
sentences = {
    'zh': '有界的记录确定所识的历程：至多 N 与 N′ 个状态的历史在 N + N′ − 1 之前相同就处处相同，在 N = 1 与 N = N′ 时更短的不够；知道界的学习者从 2N − 1 起每步正确，不知道界的套索学习者从 N + (2N − 1)·tri N 起每步正确；有限的所识的未来给有意义的切分命名，不用商（P83；界是给出的，学习者要值可判定，读法是 AI 的，待 Ren）。',
    'en': 'A bounded record fixes the registered course: histories with at most N and N′ states agreeing before N + N′ − 1 agree everywhere, with no shorter record sufficient for N = 1 and N = N′; the learner that knows the bound is right from 2N − 1 on, and the lasso learner that does not know it from N + (2N − 1)·tri N on; finite registered futures name the split that makes sense without a quotient (P83; the bound is supplied, learners need decidable values, and the readings are the AI\'s, pending Ren). ',
}
anchors = {'zh': '新的形式结果都陈述在 Lean 包 Becoming',
           'en': 'New formal results are stated on the pure core'}
for lang in ('zh', 'en'):
    field = 'argument_' + lang
    assert entry[field].count(anchors[lang]) == 1, (lang, 'reading anchor changed')
    assert sentences[lang] not in entry[field], 'P83 already added'
    entry[field] = entry[field].replace(anchors[lang], sentences[lang] + anchors[lang])
prefix = totals.LEAN + '/becoming/Becoming/'
source = prefix + 'Identification.lean'
assert source not in entry['lean'], 'P83 Lean source already added'
entry['lean'].insert(entry['lean'].index(prefix + 'Description.lean') + 1, source)
entry['source_sha256'] = hashlib.sha256((ROOT / totals.CHAPTER).read_bytes()).hexdigest()
indent = 2 if raw.startswith('[\n  {') else 1
path.write_text(json.dumps(data, ensure_ascii=False, indent=indent) + ('\n' if raw.endswith('\n') else ''))
print('P83 reading entry updated against', BASE)
