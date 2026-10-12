#!/usr/bin/env python3
"""The reading-catalogue entries of the two chapters this landing edits: python3 -B reading_entries.py ROOT
(after apply_docs.py, which writes the Becoming chapter's sentence and Lean list).

Each entry must be current with its chapter at HEAD, so that the only drift is this landing's edit (reread: the
cognition chapter gains the §2 subsection on the laws of learning on the Becoming spine, two disposition rows and
the P74 note in §4; the Becoming chapter the learning paragraph, Ren's reading of 理, the status rows, the spine row
and the glossary). The cognition entry gains one sentence on the new subsection; then both hashes are refreshed."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
DATA = 'theories/becoming/results/data'
COG_ZH = ('脊柱上的学习规律（P73、P74）：无记录固定下一个；按否证学习从不越过成立的假设，在被列表所持的世界中否证有界；迁移是经归并的推广，'
          '数据恰在类把未试之例与已观察者归并之处决定它；本章的习得与连接主义构造是这些规律的实例。')
COG_EN = ('On the Becoming spine (P73, P74), learning has general laws: no record fixes the next value; learning by refutation '
          'never passes a hypothesis that holds and, where a list holds the world, is refuted a bounded number of times; '
          'transfer is generalization through a lumping, the data determining an untried case exactly where the class '
          "lumps it with an observed one; this chapter's acquisition and connectionist constructions are their instances.")
ENTRIES = {'cognition-learning-and-evolution': f'{DATA}/arguments-a-l.json', 'the-theory-of-becoming': f'{DATA}/arguments-m-z.json'}

for ident, path in ENTRIES.items():
    p = ROOT / path
    data = json.loads(p.read_text())
    entry = next(e for e in data['entries'] if e['id'] == ident) if isinstance(data, dict) else \
        next(e for e in data if e['id'] == ident)
    head = subprocess.run(['git', 'show', f'HEAD:{entry["source"]}'], cwd=ROOT, capture_output=True, check=True).stdout
    assert entry['source_sha256'] == hashlib.sha256(head).hexdigest(), \
        (ident, 'the entry was not current with the chapter at HEAD; reread it before refreshing the hash')
    if ident == 'cognition-learning-and-evolution':
        assert COG_ZH not in entry['argument_zh'] and COG_EN not in entry['argument_en']
        entry['argument_zh'] = entry['argument_zh'] + COG_ZH
        entry['argument_en'] = entry['argument_en'] + ' ' + COG_EN
    entry['source_sha256'] = hashlib.sha256((ROOT / entry['source']).read_bytes()).hexdigest()
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print('reading entry', ident, entry['source_sha256'][:12])
