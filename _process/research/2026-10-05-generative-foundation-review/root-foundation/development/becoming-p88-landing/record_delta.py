#!/usr/bin/env python3
"""P88: add census to the existing commutation record and narrow P78's open boundaries.
Called only after successful actual checks by make_records.py, with W S.
No new census record; existing claims and counterexamples remain preserved.
"""
import json
from pathlib import Path
import sys

W = Path(sys.argv[1]).resolve()
S = sys.argv[2]
KIT = Path(__file__).resolve().parent.parent / 'becoming-landing-kit'
sys.path.insert(0, str(KIT))
import kit
R = kit.Receipts(W)
MODULE = 'Becoming.OrderNormal'
SOURCE = kit.lean('OrderNormal')
assert MODULE in R.modules
assert kit.sha(W, SOURCE) == R.receipt['source_sha256'][MODULE], 'OrderNormal source differs from checked bytes'
RECORDS = W / kit.RECORDS
Y = lambda zh, en: {'zh': zh, 'en': en}
NORMAL = 'normal-forms-need-decided-apartness'
LEAST = 'least-footprint-where-idleness-decided'


def load(rid):
    return json.loads((RECORDS / (rid + '.json')).read_text())


def save(r):
    (RECORDS / (r['id'] + '.json')).write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print(r['id'] + ': P88 delta applied')


def relate(r, rid, zh, en):
    assert not any(d['id'] == rid for d in r['related']), (r['id'], rid, 'already applied')
    r['related'].append({'id': rid, 'detail': Y(zh, en)})


def swap(r, field, lang, old, new):
    assert r[field][lang].count(old) == 1, (r['id'], field, lang, 'reread changed record')
    r[field][lang] = r[field][lang].replace(old, new)


r = load('exchanges-commute-unless-joined')
assert 'Becoming.Reorders.census' not in r['aliases'], 'census delta already applied'
r['claim']['zh'] += (' P88 接续：listed_splice 以交换前后普查的两侧构造中间一步的列表，任意交换都正向保存活动与所立者的普查'
                     '（Web.commute_census、Web.commute_standingCensus），返回方向要求两侧分开（World.commute_counted_iff）。'
                     '因此任意 Reorders，包括相连交换，都双向保持两种普查的存在（Reorders.census）；任意 Footprinted.reorder '
                     '正向保存，包含足迹下的不相连交换重排双向保存（Footprinted.reorder_census）。这是存在普查的保存，不是中间每步人数不变，'
                     '也不推出相连交换下其他前提保持。')
r['claim']['en'] += (' P88 continuation: listed_splice constructs the intermediate list from sides of the censuses before '
                     'and after a commutation. Every commutation preserves activity and standing censuses forward '
                     '(Web.commute_census, Web.commute_standingCensus); the reverse direction requires split sides '
                     '(World.commute_counted_iff). Thus every Reorders, joined pairs included, preserves existence of both '
                     'censuses in both directions (Reorders.census). Arbitrary Footprinted.reorder preserves them forward; '
                     'independent reorderings with a containing footprint preserve them both ways '
                     '(Footprinted.reorder_census). This preserves census existence, not population at every intermediate '
                     'step, and does not preserve the other premises under joined commutations.')
# P78b already supplied the converse inside this record's claim. Its old hypothesis
# accidentally retained P78's earlier boundary; repair the documentary contradiction.
old = Y('逆方向——同样交换、同样依存次序的任意两个序列由 Reorders 相关（Foata 范式）——没有证明，偏序本身没有形式化。',
        'The converse, that any two sequences of the same exchanges with the same order of dependence are related by Reorders (Foata normal form), is not proved, and the partial order itself is not formalized.')
new = Y('P78b 已在包含足迹与有限段的给定重新编号下刻画逆方向（order-of-exchanges-is-the-invariant）；这不等于 Foata 同时层正规形。普查返回方向要求两侧分开，Reorders 已包含此条件。',
        'P78b already characterizes the converse for a containing footprint and supplied finite-stretch reindexing (order-of-exchanges-is-the-invariant); this is not a Foata simultaneous-layer normal form. The census reverse direction requires split sides, already part of Reorders.')
if old in r['hypotheses']:
    r['hypotheses'][r['hypotheses'].index(old)] = new
else:
    # A concurrent P78 reconciliation may already have repaired it. Do not erase it.
    assert not any('partial order itself is not formalized' in h.get('en', '') for h in r['hypotheses']), 'reread partial hypothesis change'
    r['hypotheses'].append(new)
swap(r, 'limitations', 'zh', '足迹是给定的，不由世界推出（最小的足迹需要“被变动”可判定）；存量耗减只在两步上；沿重排的普查没有证明；',
     '足迹的原记录读法是给定的；P88 在闲置可判定时构造最小足迹（逆刻画另需关系项相等可判定），见 least-footprint-where-idleness-decided；存量耗减只在两步上；普查沿两侧分开的重排双向保持，任意交换只保证正向；')
swap(r, 'limitations', 'en', 'The footprint is given, not derived from the world (the least footprint would need being moved decided); running down is shown only at the two steps; the census along reorderings is not shown;',
     'The original footprint reading is supplied; P88 constructs the least footprint with decided idleness (the converse additionally needs decidable equality of relata), see least-footprint-where-idleness-decided. Running down is shown only at the two steps; census existence carries both ways along split-sided reorderings and only forward under arbitrary commutation;')
r['next_delta'] = Y('沿重排的普查已在 P88 接入本记录，最小足迹见 least-footprint-where-idleness-decided；无界重排与连续时间对应仍开放。',
                     'The census along reorderings is incorporated here by P88; the least footprint is in least-footprint-where-idleness-decided. Unbounded reorderings and continuous-time correspondence remain open.')
r['aliases'] += ['Becoming.' + n for n in ['listed_splice', 'Web.commute_census', 'Web.commute_standingCensus',
    'Web.commute_census_back', 'Web.commute_standingCensus_back', 'World.commute_counted', 'World.commute_counted_iff',
    'Reorders.census', 'Footprinted.counted_reorder', 'Footprinted.standing_reorder', 'Footprinted.reorder_census']]
assert all(n in R.owner for n in r['aliases'] if n.startswith('Becoming.'))
declarations = kit.declared(W / SOURCE)
own = [n for n in R.names(MODULE) if declarations[n] == 'The census along reordering']
assert 'Becoming.Reorders.census' in own
assert not any(x['path'] == SOURCE for x in r['references'])
r['references'].append({'path': SOURCE, 'role': 'proof', 'sha256': kit.sha(W, SOURCE), 'declarations': own})
r['proof_bindings'].append({'source': SOURCE, 'receipt': kit.RECEIPT,
    'sha256_pointer': '/source_sha256/' + MODULE, 'success_pointer': '/status', 'success_value': 'passed'})
r['validation_scope']['zh'] += f' P88 普查增量实际检查：合并回执 {R.run} 中 OrderNormal 的 {R.theorems("OrderNormal")} 项定理均为空公理报告；其中 Reorders.census 及普查构造按当前源码绑定。范围审读见 §{S}，尚无独立全证明审查。'
r['validation_scope']['en'] += f' P88 census delta actually checked: all {R.theorems("OrderNormal")} OrderNormal theorems have empty axiom reports in consolidated receipt {R.run}; Reorders.census and its census constructions are bound to current source. Scope review is in §{S}; no independent full proof review.'
relate(r, LEAST, 'P88 在闲置可判定时给出最小足迹，逆刻画另需关系项相等可判定。',
       'P88 supplies the least footprint with decided idleness; its converse additionally needs decidable equality of relata.')
r['history'].append(Y(f'2026-10-13 P88：把普查构造与双向保存接入既有交换记录；修正 P78b 已证明逆方向却仍写未证明的旧边界；保留原反例；见 §{S}。',
                       f'2026-10-13 P88: incorporated census construction and two-way preservation in the existing commutation record; corrected the stale boundary that called the already-proved P78b converse unproved; original counterexamples retained; see §{S}.'))
save(r)

r = load('order-of-exchanges-is-the-invariant')
relate(r, NORMAL, 'P88 在有限有名段中以不相连判定选字典序正规形；完整有限 Nat 值不变量恰需该判定。',
       'P88 selects a lexicographic form on a named finite stretch with decided apartness; a complete finite Nat-valued invariant needs exactly that decision.')
relate(r, LEAST, 'P88 在闲置可判定时把足迹读到最小，相连与偏序均被所有包含足迹包含。',
       'P88 reads off the least footprint with decided idleness; its joining and order lie within every containing footprint’s.')
swap(r, 'limitations', 'zh', '足迹是给定的，最小足迹需要“被变动”可判定；没有构造 Foata 范式（规范代表）；',
     '本记录的足迹是给定的；P88 在闲置可判定时给最小足迹，并在有限有名段内以不相连判定给字典序规范代表；Foata 同时层正规形未给；')
swap(r, 'limitations', 'en', 'The footprint is given, and the least footprint would need being moved decided; no Foata normal form (a canonical representative) is built;',
     'The footprint in this record is supplied; P88 gives the least footprint with decided idleness and a lexicographic representative on a finite named stretch with decided apartness. No Foata simultaneous-layer normal form is built;')
r['next_delta'] = Y('字典序正规形与可判定闲置下的最小足迹已由 P88 给出；Foata 同时层正规形、无名或无界正规形及连续时间对应仍开放。',
                     'P88 supplies the lexicographic normal form and the least footprint under decided idleness. Foata simultaneous layers, unnamed or unbounded forms, and continuous-time correspondence remain open.')
r['history'].append(Y(f'2026-10-13 P88：保留已有逆定理，连接新正规形与最小足迹记录，缩小未完成边界；见 §{S}。',
                       f'2026-10-13 P88: retained the existing converse, connected the new normal-form and least-footprint records, and narrowed the remaining boundary; see §{S}.'))
save(r)
