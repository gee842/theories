#!/usr/bin/env python3
"""R35 step 0 (20 October 2026): the two goal-scope proposals of R25 (study section 218), approved by Ren on
20 October 2026 (sources/15-codex-theory-conversations/2026-10-20-fix-all-twentieth-review.md), applied to the
goal record and the record theory-of-becoming-foundation. The board and RESEARCH-DIRECTIVES are edited by hand
in the same commit; GOALS is rendered.

usage (from the checkout root): python3 -B goal_scope.py
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
SRC = 'sources/15-codex-theory-conversations/2026-10-20-fix-all-twentieth-review.md'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'

FORMAL_EN = ('every central law of the spine (the coverage of the completion criterion, K1) stated over every law, '
             'or relation, of exchange (`ExchangeLaw`, `ExchangeRelation`), with each `World` premise shown to be a '
             'reading of the exchange or a state of the law, and the process and world families joined by '
             'definition (a world is a run by its type)')
FORMAL_ZH = ('脊柱的每条中心规律（完成标准的覆盖，K1）都对每个交换之律或交换关系（`ExchangeLaw`、`ExchangeRelation`）陈述，'
             '每个 `World` 前提都示为交换的读法或律的状态，过程族与世界族由定义相连（世界按其类型就是一段运行）')
PHIL_EN = 'that the whole\'s determinations are internally related moments of one unfolding'
PHIL_ZH = '整体的诸规定是同一展开中内在相关的环节'


def load(p):
    return json.loads((ROOT / p).read_text())


def dump(p, d):
    (ROOT / p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')


def sha(p):
    return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()


# ---- the goal record
G = '_process/goals/theory-of-becoming.json'
g = load(G)
g['objective'] = {
    'en': 'Establish the deductive necessity of the Theory of Becoming as a whole without added substantive axioms, '
          f'in two parts: its formal part, {FORMAL_EN}; and its philosophical part, {PHIL_EN}. Explain generative '
          'forms within its manifold. Articulate how relations form, persist, transform and dissolve, including life '
          'and evolution, without requiring every becoming to be generative or favorably directed.',
    'zh': f'无需附加实质公理，建立Theory of Becoming整体的演绎必然性，分两部分：形式部分，{FORMAL_ZH}；哲学部分，{PHIL_ZH}。'
          '说明其manifold中的生成形态。阐明关系怎样形成、维持、转化与消失，包含生命与演化，不要求每种变化均有生成性或有利方向。'}
g['completion'] = {
    'en': g['completion']['en'] + ' Completeness is checked by the completion criterion K1–K7 (coverage, unity, '
          'premises, representation, enclosure, the ethics chain, the open register; study section 218), adopted '
          '20 October 2026 with Ren\'s approval; until it runs, the chapter claims completeness only in the qualified '
          'sense it states.',
    'zh': g['completion']['zh'] + ' 完整性由完成标准 K1–K7 检查（覆盖、统一、前提、表示、封闭、伦理之链、开放登记；研究第 218 节），'
          '2026年10月20日经 Ren 批准采用；在它运行之前，正文只在其所述的限定意义上声称完整。'}
g['overview']['next_step'] = {
    'en': f'The formal part of the necessity of the whole: {FORMAL_EN}. Five of the eight `World` premises are '
          'readings of one exchange and three are states of the law (`Becoming.ExchangePremises`); the families are '
          'joined by definition (`Becoming.Runs`, R28); what remains is the spine\'s central laws stated over every '
          'law of exchange rather than over separately chosen premises. The philosophical part: '
          f'{PHIL_EN}, not a collection of laws each holding of every represented world. Settle whether every '
          'becoming can be represented with discrete steps and natural-number amounts, on which rest, novelty needing '
          'gain and the setting of runaway by frequency depend, and state the laws with real amounts and continuous '
          'time. Completeness is checked by K1–K7.',
    'zh': f'整体必然性的形式部分：{FORMAL_ZH}。八个 `World` 前提中五个是同一交换的读法、三个是律的状态（`Becoming.ExchangePremises`）；'
          '两族由定义相连（`Becoming.Runs`，R28）；尚待的是把脊柱的中心规律对每个交换之律陈述，而非对分别选定的前提陈述。哲学部分：'
          f'{PHIL_ZH}，而非各自对每个被表示世界成立的一组规律。判明每个生成／变化能否以离散步与自然数量表示（停息、新颖需要增益、'
          '由频率决定失控都依赖于此），并陈述实数量与连续时间下的规律。完整性由 K1–K7 检查。'}
if SRC not in g['sources']:
    g['sources'].append(SRC)
dump(G, g)

# ---- the record
R = 'theories/becoming/results/records/theory-of-becoming-foundation.json'
r = load(R)
r['statement'] = {
    'en': 'Target: the deductive necessity of Becoming as a whole, with no added substantive axiom: formally, every '
          'central law over every law of exchange; philosophically, its determinations as moments of one unfolding; '
          'generation, persistence, degeneration, dissolution, life, evolution, evaluation within it.',
    'zh': '目标：无需附加实质公理，建立Becoming整体的演绎必然性（形式上，每条中心规律都对每个交换之律陈述；哲学上，其诸规定是同一展开中'
          '内在相关的环节），生成、维持、转化、退化、消解、生命、演化与评价皆在其中。'}
r['next_delta'] = {
    'en': 'Formal part: every central law of the spine (K1) stated over every law of exchange, as '
          'premises-read-off-the-exchange and premises-that-are-states-of-the-law do for the World premises, the '
          'families joined by definition (worlds-are-runs). Philosophical part: the whole relationally constituted, '
          'not only consistently stated.',
    'zh': '形式部分：把脊柱的每条中心规律（K1）对每个交换之律陈述，如 premises-read-off-the-exchange 与 '
          'premises-that-are-states-of-the-law 对 World 前提所做，两族由定义相连（worlds-are-runs）。哲学部分：整体确由关系构成，'
          '而不只是被一致陈述。'}
prog = {'en': 'Formal part restated with approval: every central law of the spine stated over every law, or relation, '
              'of exchange, each World premise a reading of the exchange or a state of the law, the families joined '
              'by definition.',
        'zh': '形式部分经批准重述：脊柱的每条中心规律都对每个交换之律或交换关系陈述，每个 World 前提是交换的读法或律的状态，两族由定义相连。',
        'source': STUDY + '#218-r25-the-twentieth-reviews-step-1-docs-now'}
if not any(x.get('source') == prog['source'] for x in r.get('progress', [])):
    r.setdefault('progress', []).append(prog)
item = {'en': 'The formal part, complete, would not settle the philosophical part, and it reaches a becoming only '
              'where that becoming has a law of exchange with finite courses (the scope of representation).',
        'zh': '形式部分即使完成，也不解决哲学部分；它只及有有限进程之交换律的生成（表示的范围）。',
        'kind': 'scope'}
if item not in r['does_not_show']:
    r['does_not_show'].append(item)
for k, (a, b) in {'statement': (300, 150), 'next_delta': (400, 180)}.items():
    assert len(r[k]['en']) <= a and len(r[k]['zh']) <= b, (k, len(r[k]['en']), len(r[k]['zh']))
assert len(prog['en']) <= 240 and len(prog['zh']) <= 110 and len(item['en']) <= 240 and len(item['zh']) <= 110
paths = {x['path'] for x in r['references']}
if SRC not in paths:
    r['references'].append({'path': SRC, 'role': 'provenance', 'sha256': sha(SRC), 'declarations': []})
r['history'].append({
    'en': '20 October 2026, R35: target 1\'s formal part restated, as proposed in R25 (study section 218) and approved '
          'by Ren on 20 October 2026 (2026-10-20-fix-all-twentieth-review): the statement now names the formal part '
          '(every central law over every law of exchange) and the philosophical part (the whole\'s determinations as '
          'moments of one unfolding); a progress item states the formal part in full (each World premise a reading '
          'of the exchange or a state of the law, the families joined by definition); next_delta restated '
          'accordingly; one does_not_show item added (the formal part does not settle the philosophical part, and '
          'reaches becoming only as far as it has a law of exchange). The target, its status and the deductive '
          'necessity it asks for are unchanged; completeness is checked by K1-K7, adopted the same day.',
    'zh': '2026年10月20日，R35：目标一的形式部分按 R25 的提议（研究第 218 节）重述，2026年10月20日经 Ren 批准'
          '（2026-10-20-fix-all-twentieth-review）：陈述现写明形式部分（脊柱的每条中心规律都对每个交换之律或交换关系陈述，每个 World '
          '前提是交换的读法或律的状态，两族由定义相连）与哲学部分（整体的诸规定是同一展开中内在相关的环节）；next_delta 随之重述；新增一条 '
          'does_not_show（形式部分不解决哲学部分，且只及有交换之律的生成）。目标、其状态及其所要求的演绎必然性不变；完整性由同日采用的 K1–K7 检查。'})
dump(R, r)
print('goal and record updated')
