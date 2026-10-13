#!/usr/bin/env python3
"""Reconcile the catalogue after reviewing P70–P72's chapter additions, then bind its final bytes."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

root = Path(sys.argv[1]).resolve()
path = root / 'theories/becoming/results/data/arguments-m-z.json'
data = json.loads(path.read_text())
entry = next(e for e in data if e['id'] == 'the-theory-of-becoming')
old = subprocess.run(['git', 'show', f'HEAD:{entry["source"]}'], cwd=root,
                     capture_output=True, check=True).stdout
assert entry['source_sha256'] == hashlib.sha256(old).hexdigest()
entry['argument_zh'] += 'P70–P72 在同一展开内说明描述的损失：分离恰在整体为矩形处保留关系；确定的律下有意义的描述按所识的未来等同配置，有限多状态恰是套索；识在所识之中的对角缺口与补全的展开，以及诸语境的识何时粘合。Mermin–Peres 方阵的整数矩阵实现给出无不依语境的值的实例（P72q）。'
entry['argument_en'] += ' P70–P72 state what a description loses within one unfolding: separation preserves the whole exactly where it is rectangular; under a determined law a description makes sense by identifying configurations with the same registered future, and finitely many states is a lasso; diagonal gaps concern registration within what it registers, and contextual gluing states when context-free claims fit. An integer-matrix realization of the Mermin–Peres square supplies the quantum instance (P72q).'
for module in ('Description', 'Diagonal', 'Context', 'Quantum'):
    lean = f'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/{module}.lean'
    assert lean not in entry['lean']
    entry['lean'].append(lean)
entry['source_sha256'] = hashlib.sha256((root / entry['source']).read_bytes()).hexdigest()
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
print('P70–P72 chapter reading reconciled')
