#!/usr/bin/env python3
"""U3 (19 October 2026): move proof bindings of the package files U3 changed (Hexagrams.lean, Listing.lean) to U3's
core receipt where the bound receipt no longer binds their bytes, with a history note.
usage (from the checkout root): python3 -B rebind.py RECEIPT"""
import glob, hashlib, json, sys

PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
receipt = f'{PKG}/becoming-checks/{sys.argv[1]}/verification.json'
core = json.load(open(receipt))
assert core['status'] == 'passed'
CHANGED = {f'{PKG}/Becoming/Hexagrams.lean': 'Becoming.Hexagrams', f'{PKG}/Becoming/Listing.lean': 'Becoming.Listing'}
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
for path, module in CHANGED.items():
    assert core['source_sha256'][module] == h(path), module
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    d = json.load(open(f))
    moved = set()
    for b in d.get('proof_bindings', []):
        if b['source'] in CHANGED and b['receipt'] != receipt:
            bound = json.load(open(b['receipt']))['source_sha256'].get(CHANGED[b['source']])
            if bound != h(b['source']):
                b['receipt'] = receipt
                moved.add(b['source'].rsplit('/', 1)[-1])
    if not moved:
        continue
    if not any(r['path'] == receipt for r in d['references']):
        d['references'].append({'path': receipt, 'role': 'receipt', 'sha256': h(receipt), 'declarations': []})
    names = ', '.join(sorted(moved))
    d['history'].append({
        'en': f'19 October 2026, U3: the proof binding of {names} moves to core receipt {sys.argv[1]}, which checked the '
              'file as U3 changed it (new theorems only; the declarations this record cites are unchanged). The claim is '
              'unchanged.',
        'zh': f'2026年10月19日，U3：{names} 的证明绑定移到核心回执 {sys.argv[1]}，该回执检查了 U3 改动后的文件（只新增定理；'
              '本记录所引声明不变）。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(f.rsplit('/', 1)[-1], names)
