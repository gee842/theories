#!/usr/bin/env python3
"""IV1: the reading-catalogue entry for the chapter THE-STEP-OF-INVARIANCE (arguments-m-z.json, in id order),
read against the chapter's current bytes. usage: python3 -B catalogue.py (from the checkout root)"""
import hashlib
import json
from pathlib import Path

P = Path('theories/becoming/results/data/arguments-m-z.json')
SRC = 'theories/becoming/chapters/THE-STEP-OF-INVARIANCE.md'
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
entry = {
    'id': 'the-step-of-invariance',
    'title_zh': '不变之步：论证及其反驳',
    'title_en': 'The step of invariance: the argument and its objections',
    'category': 'ethical-argument',
    'status': '形式结果已检查；不变之步本身开放 / Formal results checked; the step itself open',
    'argument_zh': '延续条件的内容超出自我之预设的部分是不变之步。它是两个论证：跨立场（Gewirth）由各立场自身的预设只迫使诸中心有意义；'
                   '跨画法（Parfit、Siderits）不经其他立场。批评者与普遍主义者恰在“无论自我如何画出”取窄辖域还是宽辖域上分开，'
                   '这归结为自我的预设是否本质上是从己的（de se）。定序方面，C 恰是每个计入一切的正加权共有的序：偏倚恰决定混合的比较，零权是否认范围，同权即计数。',
    'argument_en': 'The continuation condition\'s content beyond the self\'s presupposition is the step of invariance. It is '
                   'two arguments: across standpoints (Gewirth) each standpoint\'s own presupposition forces significance '
                   'for exactly the centers; across drawings (Parfit, Siderits) no other standpoint enters. The critic and '
                   'the universalist part exactly on whether "however the self is drawn" takes narrow or wide scope, which '
                   'reduces to whether the self\'s presupposition is essentially de se. On order, C is exactly what every '
                   'positive weighting that counts everything shares: partiality decides exactly the mixed comparisons, '
                   'a zero weight denies scope, and equal weights count numbers.',
    'significance_zh': '把伦理的范围前提定位到一个可检查的问题上，并给 §8.9 的每条反驳一个裁定：回答、锐化为确切的开放问题，或表明其推翻此步（没有一条做到）。',
    'significance_en': 'It locates the ethics\' premise of scope at one checkable question and gives each §8.9 objection a '
                       'verdict: answered, sharpened into an exact open question, or shown to defeat the step (none does).',
    'scope_zh': 'Becoming.Weightings 35 条定理、公理报告为空；文献核查见显著性审查。论证不是证明：不变之步既未证明也未被推翻，从己问题、特许关系、诸中心的范围与覆盖、量级、立场处的单调性都开放。',
    'scope_en': 'Becoming.Weightings, 35 theorems with empty axiom reports; the literature check is in the significance '
                'review. An argument, not a proof: the step is neither shown nor defeated, and the de se question, a '
                'privileged relation, the range of the centers and covering, magnitude and monotonicity at the '
                'standpoint stay open.',
    'next_zh': '从己问题；基底上哪些构成是中心；跨立场的分级意义；独立的哲学审查。',
    'next_en': 'The de se question; which formations are centers on the base; graded significance across standpoints; '
               'an independent philosophical review.',
    'source': SRC,
    'source_sha256': hashlib.sha256(Path(SRC).read_bytes()).hexdigest(),
    'lean': [f'{PKG}/Becoming/Weightings.lean', f'{PKG}/Becoming/Boundaries.lean'],
    'evidence': ['_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-SIGNIFICANCE-REVIEW.md',
                 'theories/becoming/results/records/what-the-step-across-standpoints-reaches.json',
                 'theories/becoming/results/records/widening-as-what-every-weighting-ranks.json'],
    'status_code': 'mixed-verified-open',
}
d = json.loads(P.read_text())
assert all(x['id'] != entry['id'] for x in d)
i = next(i for i, x in enumerate(d) if x['id'] > entry['id'])
d.insert(i, entry)
raw = P.read_text()
P.write_text(json.dumps(d, ensure_ascii=False, indent=1 if raw.startswith('[\n {') else 2) + '\n')
print('inserted at', i)
