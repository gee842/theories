#!/usr/bin/env python3
"""U5 follow-up (19 October 2026): after order_paired_by_law and six_steps join the passage 非覆即變 (feifu) of Y1's
passage map and study section 208 says so, re-point the record references to those two files, after reading the
change, with a history note. Only references that matched the file at BASE are re-pointed.
usage (from the checkout root): python3 -B repoint_passage.py BASE"""
import glob, hashlib, json, subprocess, sys

BASE = sys.argv[1]
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', BASE + ':' + p], capture_output=True).stdout).hexdigest()
ROOT = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
WHAT = {
    ROOT + 'development/y1-changes/passages.json': (
        'passages.json: the passage 非覆即變 (feifu) names order_paired_by_law and six_steps beside order_paired, and its '
        'reading adds that 變 is six steps along the law of waxing and waning; no other passage changed',
        'passages.json：非覆即變一段（feifu）在 order_paired 旁加列 order_paired_by_law 与 six_steps，读法补一句：變即沿消息之律六步；其他段未变'),
    ROOT + 'BECOMING-RENEWAL-READING.md': (
        'BECOMING-RENEWAL-READING.md: the paragraph on Y1\'s passage map in study section 208 says the addition is made',
        'BECOMING-RENEWAL-READING.md：研究第 208 节关于 Y1 段落图的一段改为已加入'),
}
SHA = {p: (at_base(p), h(p)) for p in WHAT}
n = 0
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    d = json.load(open(f))
    hit = []
    for r in d.get('references', []):
        p = r.get('path')
        if p in SHA and r.get('sha256') == SHA[p][0] != SHA[p][1]:
            r['sha256'] = SHA[p][1]
            hit.append(p)
    if not hit:
        continue
    hit = sorted(set(hit))
    d['history'].append({
        'en': '19 October 2026, U5 follow-up (the passage map): re-pointed after reading the change ('
              + '; '.join(WHAT[p][0] for p in hit) + '). The claim is unchanged.',
        'zh': '2026年10月19日，U5 后续（段落图）：读过改动后重新指向（' + '；'.join(WHAT[p][1] for p in hit) + '）。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    n += 1
    print(f.rsplit('/', 1)[-1], [p.rsplit('/', 1)[-1] for p in hit])
print(n, 'records re-pointed')
