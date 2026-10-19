#!/usr/bin/env python3
"""R29 (20 October 2026), compression under board rule 9: rebind and re-point the records.

Usage (from the checkout root): python3 -B rebind.py BASE RECEIPT_ID [RENDER_LOG]

BASE is the main commit R29 was rebased on; RECEIPT_ID the passing core receipt of R29's checker run.

* The moves and removals are read off the two receipts (R28's, the base, and R29's): a declaration
  whose module changed moved with its full name; one in the base and not in R29's was removed, and
  must be a key of REMAP, which names the kept declaration stating the same (or, for `Readout.image`,
  the definition it was a copy of).
* In every declaration list (laws, references) a removed name is replaced by its kept name; a removed
  alias is dropped, since the kept name is another record's alias or none.
  In references a declaration is filed under the file of its module in R29's receipt: a moved or
  replaced name goes to the record's reference to that file, which is added (with a proof binding
  where the record has bindings) where the record had none. Every name is checked against the
  receipt's elaborated declarations.
* TEXT replaces the sentences that said a removed name proved something (each must occur once in the
  record); the claim is otherwise unchanged.
* Proof bindings to the Lean files R29 changed are rebound to the receipt; references to the files R29
  changed are re-pointed where they matched BASE (the record was current), or where the render log
  reports drift in sections the record cites, after reading the change (WHAT says what changed).
* A history note says what moved, what was replaced and what was re-pointed.
"""
import glob
import hashlib
import json
import subprocess
import sys

BASE, RID = sys.argv[1], sys.argv[2]
DRIFT = {}
if len(sys.argv) > 3:
    _log = open(sys.argv[3]).read()
    _dec = json.JSONDecoder()
    for _k in range(len(_log)):
        if _log[_k] == '{':
            try:
                _o, _ = _dec.raw_decode(_log[_k:])
            except ValueError:
                continue
            if isinstance(_o, dict) and 'source_drift' in _o:
                for _x in _o['source_drift']:
                    DRIFT.setdefault(_x['path'], set()).add(_x['id'])
                break
LEANDIR = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
PKG = LEANDIR + 'becoming/'
B = PKG + 'Becoming/'
BASE_RID = '20261019T181519.226999Z'
RECEIPT = PKG + 'becoming-checks/' + RID + '/verification.json'
receipt = json.load(open(RECEIPT))
assert receipt['status'] == 'passed'
assert not any(v for m in receipt['modules'] if m.get('layer') == 'core' for v in m['axiom_dependencies'].values()), 'core axiom report not empty'
base_receipt = json.load(open(PKG + 'becoming-checks/' + BASE_RID + '/verification.json'))


def homes(r):
    out = {}
    for m in r['modules']:
        if m.get('layer') != 'core':
            continue
        for x in m.get('declarations', []):
            out[x['name'] if isinstance(x, dict) else x] = m['module']
    return out


home, home_base = homes(receipt), homes(base_receipt)
path_of = {m: LEANDIR + p for m, p in receipt['source_paths'].items()}
module_of = {p: m for m, p in path_of.items()}

P = 'Becoming.'
REMAP = {P + k: P + v for k, v in {
    # Item 1: the laws of every process, at Law.process (Becoming.Recurrence)
    'Law.Merges.not_lossless': 'Branching.Merges.not_lossless',
    'Law.Reachable.earlier': 'Branching.Reachable.earlier',
    'Law.Returns.reachable': 'Branching.Returns.reachable',
    # Item 2: the rest family proved as the whole-number instance of Becoming.Amounts
    'whole_falls_not_recurring': 'falls_not_recurring',
    'whole_falls_stop_unrefuted': 'falls_stop_unrefuted',
    'Flow.taking_not_recurring_whole': 'Flow.taking_not_recurring_from',
    'Flow.takers_within_on_whole': 'Flow.takers_within_on',
    'Flow.change_stops_unrefuted_whole': 'Flow.change_stops_unrefuted',
    'World.rests_unrefuted_enclosed_whole': 'World.rests_unrefuted_enclosed',
    # Item 4: the law of one formation, proved at the singleton pool
    'Flow.unselected_beyond_coupling_all_of_pool': 'Flow.unselected_beyond_coupling_all',
    # Item 5: one name per statement (the twentieth review's B9 pairs)
    'Dependence.dichotomy_of_determined': 'Dependence.determined_dichotomy',
    'World.Finite.arising_iff_ceasing': 'World.arising_iff_ceasing',
    'World.arising_iff_ceasing_of_decidable': 'World.arising_iff_ceasing',
    'World.Finite.comes_to_rest_unrefuted': 'World.rests_unrefuted',
    'Switching.no_state_law_of_criterion': 'Switching.no_state_law',
    'Loop.responds_by_law': 'Loop.responds',
    'Hexagram.pairs_goAlike_of_commutes': 'Hexagram.pairs_goAlike',
    'Remainder.carriedWithin_exact': 'carriedWithin_exact',
    'Remainder.carriedWithin_exact_of_no_loop': 'carriedWithin_exact_of_no_loop',
    'ExchangeLaw.Nonanticipating.through_sensitive_of_every': 'ExchangeLaw.Nonanticipating.through_sensitive',
    'ReferencePlan.added_keeps_of_law': 'ReferencePlan.added_keeps',
    'ReferencePlan.new_contact_choice_of_law': 'ReferencePlan.new_contact_choice',
    'ReferencePlan.trace_conserves_of_law': 'ReferencePlan.trace_conserves',
    'Hexagram.complement_line': 'Hexagram.line_complement',
    'Hexagram.flip_line': 'Hexagram.line_flip_self',
    'Hexagram.or_false_split': 'Hexagram.neither',
    # Item 6: one image of a process through a projection
    'Readout.image': 'Image',
}.items()}
removed = set(home_base) - set(home)
assert removed == set(REMAP), (sorted(removed - set(REMAP)), sorted(set(REMAP) - removed))
for x, y in REMAP.items():
    assert y in home, y
MOVED = {x for x in home_base if x in home and home[x] != home_base[x]}

# Sentences that said a removed name proved something; each occurs once in the record (en, then zh).
TEXT = {
    'least-loss-rest': [
        ("From the law, the spine's two descents falls_not_recurring and falls_stop_unrefuted, Flow.taking_not_recurring_from, Flow.takers_within_on, Flow.change_stops_unrefuted and the rest theorem World.rests_unrefuted_enclosed are proved again with their statements unchanged.",
         "The rest family is proved as this instance, below the modules that state it: the spine's two descents falls_not_recurring (Becoming.Renewal) and falls_stop_unrefuted (Becoming.Space), Flow.taking_not_recurring_from and Flow.takers_within_on (Becoming.Dissipation) and Flow.change_stops_unrefuted (Becoming.Openness), through which the rest theorem World.rests_unrefuted_enclosed follows."),
        ("由此律重新证明脊柱的两个下降 falls_not_recurring 与 falls_stop_unrefuted、Flow.taking_not_recurring_from、Flow.takers_within_on、Flow.change_stops_unrefuted 以及停息定理 World.rests_unrefuted_enclosed，陈述不变。",
         "停息诸律作为这一实例证明，在陈述它们的模块之下：脊柱的两个下降 falls_not_recurring（Becoming.Renewal）与 falls_stop_unrefuted（Becoming.Space）、Flow.taking_not_recurring_from 与 Flow.takers_within_on（Becoming.Dissipation）以及 Flow.change_stops_unrefuted（Becoming.Openness），停息定理 World.rests_unrefuted_enclosed 经最后一条推出。"),
        ("to prove Flow.change_stops_unrefuted and World.rests_unrefuted_enclosed again from the least-loss law, statements unchanged.",
         "to prove Flow.change_stops_unrefuted from the least-loss law, which Becoming.Openness does, World.rests_unrefuted_enclosed following through it."),
        ("由最小损失律重新证明 Flow.change_stops_unrefuted 与 World.rests_unrefuted_enclosed，陈述不变。",
         "由最小损失律证明 Flow.change_stops_unrefuted（Becoming.Openness 如此证明），World.rests_unrefuted_enclosed 经它推出。"),
    ],
    'what-pooled-coupling-reaches': [
        ("Flow.unselected_beyond_coupling_all is the case of one formation's closure.",
         "Flow.unselected_beyond_coupling_all, the law of one formation's closure, is proved as the case of the pool of that formation."),
        ("Flow.unselected_beyond_coupling_all 是一个形成之闭包的情形。",
         "一个形成之闭包的律 Flow.unselected_beyond_coupling_all 作为该形成之池的情形证明。"),
    ],
    'what-a-cut-loses': [
        ("The results of Becoming.Loops on exactness are instances: order j is exact up to step j; no loop upstream suffices; the equivalence",
         "Of the results of Becoming.Loops on exactness, order j being exact up to step j and no loop upstream sufficing are stated once, in Becoming.Loops; the equivalence"),
        ("Becoming.Loops 关于精确的结果是实例：j 阶到第 j 步精确；上游没有回路即足够；耦合每步成立时",
         "Becoming.Loops 关于精确的结果中，j 阶到第 j 步精确与上游没有回路即足够只在 Becoming.Loops 中陈述一次；耦合每步成立时"),
    ],
    'a-law-through-a-projection-along-one-run': [
        ("Switching's missing state law follows from the criterion along its run.",
         "Switching's run is inconsistent through the projection; its missing state law is Switching.no_state_law of Becoming.Mechanism."),
        ("Switching 缺少状态规律，可沿其运行由判据推出。",
         "Switching 的运行经投影不一致；它缺少状态规律，即 Becoming.Mechanism 的 Switching.no_state_law。"),
    ],
    'continued-change-needs-openness': [
        ("so World.rests_unrefuted is the finite case, its relata covering what is active, with no decision procedure.",
         "and the finite rest, World.rests_unrefuted of Becoming.Space, states the same conclusion of finite worlds, its relata covering what is active, with no decision procedure."),
        ("所以 World.rests_unrefuted 是有限情形，其关系项覆盖活跃者，不用判定程序。",
         "有限世界的停息 World.rests_unrefuted（Becoming.Space）陈述同一结论，其关系项覆盖活跃者，不用判定程序。"),
        ("rests_unrefuted is its finite case (World.Finite.comes_to_rest_unrefuted, P26).",
         "rests_unrefuted states its conclusion of finite worlds (P26)."),
        ("rests_unrefuted 是它的有限情形（World.Finite.comes_to_rest_unrefuted，P26）。",
         "rests_unrefuted 陈述它对有限世界的结论（P26）。"),
    ],
    'bounded-census-keeps-pace': [
        ("so the law of finite worlds, World.arising_iff_ceasing, is a case.",
         "the premise of the bounded law; the law of finite worlds is World.arising_iff_ceasing of Becoming.Space."),
        ("所以有限世界的规律 World.arising_iff_ceasing 是其情形。",
         "这是有界之律的前提；有限世界的规律是 Becoming.Space 的 World.arising_iff_ceasing。"),
    ],
    'recurrence-without-decidedness': [
        ("World.arising_iff_ceasing being the case decided by a procedure from the first step (World.arising_iff_ceasing_of_decidable);",
         "World.arising_iff_ceasing (Becoming.Space) stating the case decided by a procedure from the first step;"),
        ("World.arising_iff_ceasing 是由判定程序从第一步起已定的情形（World.arising_iff_ceasing_of_decidable）；",
         "World.arising_iff_ceasing（Becoming.Space）陈述由判定程序从第一步起已定的情形；"),
    ],
    'determinacy-up-to-likeness': [
        ("and determinacy is a case (Dependence.dichotomy_of_determined).",
         "and the dichotomy under determinacy is Joint's Dependence.determined_dichotomy."),
        ("确定是其情形（Dependence.dichotomy_of_determined）。",
         "确定之下的二分即 Joint 的 Dependence.determined_dichotomy。"),
        (", and determinacy, are cases.", " is a case, and the dichotomy under determinacy is Joint's determined_dichotomy, stated once."),
        ("，以及确定，都是其情形。", "是其情形；确定之下的二分即 Joint 的 determined_dichotomy，只陈述一次。"),
    ],
    'what-a-commuting-law-keeps-apart': [
        ("the going alike across pairs is the general law's instance,",
         "the pairs go alike, as the general law says (Hexagram.pairs_goAlike, stated once in Becoming.Hexagrams),"),
        ("在对之间同行是一般律的实例，", "在对之间同行，如一般律所说（Hexagram.pairs_goAlike，只在 Becoming.Hexagrams 中陈述），"),
    ],
    'counterfactual-is-the-course': [
        ("so the response follows from the law,",
         "so the response follows from the law (ExchangeLaw.Through.responds at Loop.replyLaw_through; the response is Loop.responds),"),
        ("所以回应由律推出；", "所以回应由律推出（ExchangeLaw.Through.responds 用于 Loop.replyLaw_through；回应即 Loop.responds）；"),
    ],
    'comparison-where-the-rest-responds': [
        ("Loop.responds follows from the law (Loop.responds_by_law).",
         "Loop.responds follows from the law (ExchangeLaw.Through.responds at Loop.replyLaw_through)."),
        ("Loop.responds 由律推出（Loop.responds_by_law）。",
         "Loop.responds 由律推出（ExchangeLaw.Through.responds 用于 Loop.replyLaw_through）。"),
    ],
    'attraction-is-not-returning': [
        ("a returning configuration can be had at every step (Law.Returns.reachable)",
         "a returning configuration can be had at every step (Branching.Returns.reachable at Law.process)"),
        ("返回者每步可得（Law.Returns.reachable）", "返回者每步可得（Branching.Returns.reachable，在 Law.process 上）"),
    ],
    'recurrence-without-premise': [
        ("a configuration that returns can be had at every step (Law.Returns.reachable);",
         "a configuration that returns can be had at every step (Branching.Returns.reachable at Law.process);"),
        ("回返的构型每一步都可得（Law.Returns.reachable）；", "回返的构型每一步都可得（Branching.Returns.reachable，在 Law.process 上）；"),
    ],
    'entropy-history-and-record': [
        ("Law.Merges, Law.Merges.not_lossless, Law.Returns,", "Law.Merges, Branching.Merges.not_lossless, Law.Returns,"),
        ("Law.Merges、Law.Merges.not_lossless、Law.Returns", "Law.Merges、Branching.Merges.not_lossless、Law.Returns"),
    ],
}
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CH = 'theories/becoming/chapters/'
DOCS = {
    CH + 'THE-THEORY-OF-BECOMING.md': ('the sentences citing the removed names cite the kept ones; §9 (layers, import tree, receipt, counts) follows R29',
                                       '引用删去名称的句子改引保留者；§9（层、导入树、回执、计数）随 R29'),
    CH + 'THE-THEORY-OF-BECOMING.zh.md': ('the matching sentences, the module counts and §9 follow R29', '对应句子、模块计数与 §9 随 R29'),
    CH + 'THE-THEORY-OF-BECOMING-REFERENCE.md': ('the Recurrence and Selection rows state what moved in, the rest theorem rows cite the kept names, module counts follow R29',
                                                 'Recurrence 与 Selection 两行陈述移入者，停息定理各行改引保留的名称，模块计数随 R29'),
    'theories/becoming/OPENING.md': ('footnote [^conditions] cites Becoming.Amounts and the rest theorem itself, proved from the law; the body is unchanged',
                                     '脚注 [^conditions] 引 Becoming.Amounts 与由此律证明的停息定理本身；正文不变'),
    STUDY: ('section 220 added', '新增第 220 节'),
    PKG + 'Becoming.lean': ('imports Becoming.Amounts; the notes of Amounts, LeastLoss and SelectionPool', '导入 Becoming.Amounts；Amounts、LeastLoss 与 SelectionPool 的说明'),
    PKG + 'README.md': ('the Amounts and LeastLoss rows, the SelectionPool row, the rows citing removed names and the import order follow R29',
                        'Amounts 与 LeastLoss 两行、SelectionPool 一行、引用删去名称的各行与导入次序随 R29'),
    PKG + 'README.zh.md': ('the rows citing removed names and the import order follow R29', '引用删去名称的各行与导入次序随 R29'),
    PKG + 'check_becoming.py': ('Becoming.Amounts added to CORE; the SCOPE text of Amounts, LeastLoss and SelectionPool; no logic changed',
                                'CORE 加入 Becoming.Amounts；Amounts、LeastLoss 与 SelectionPool 的 SCOPE 文本；逻辑不变'),
    PKG + 'becoming-verification.json': ("the current receipt is R29's run", '当前回执为 R29 之运行'),
}
LEAN_WHAT = {
    'Recurrence.lean': ("the laws of every process (Branching's Merges.not_lossless, Reachable.earlier, lost_stays, Returns.reachable, Lossless.returns and others), Law.run, Law.run_state and Run.onward moved in; Law.lost_stays, Law.Lossless.returns, Law.Lossless.unlisted and Law.rise_not_lossless are their one-line cases at the law's run; Law.Merges.not_lossless, Law.Reachable.earlier and Law.Returns.reachable removed; statements kept unchanged",
                        "每个过程之律（Branching 的 Merges.not_lossless、Reachable.earlier、lost_stays、Returns.reachable、Lossless.returns 等）、Law.run、Law.run_state 与 Run.onward 移入；Law.lost_stays、Law.Lossless.returns、Law.Lossless.unlisted、Law.rise_not_lossless 是它们在律之运行上的一行情形；删去 Law.Merges.not_lossless、Law.Reachable.earlier、Law.Returns.reachable；保留的陈述不变"),
    'Branching.lean': ('the laws of every process moved to Recurrence.lean', '每个过程之律移到 Recurrence.lean'),
    'Labelled.lean': ('Law.run and Law.run_state moved to Recurrence.lean', 'Law.run 与 Law.run_state 移到 Recurrence.lean'),
    'Amounts.lean': ('new module: the amounts that may be dense and their laws of rest and approach, moved from LeastLoss.lean, with the whole-number instance; imports only Naturals',
                     '新模块：可稠密的量及其停息与趋近之律，自 LeastLoss.lean 移入，并有整数实例；只导入 Naturals'),
    'LeastLoss.lean': ('the amounts and their laws moved to Amounts.lean, Amounts.whole_sum to Dissipation.lean; the six whole-number re-proofs removed; the countermodels and the laws of merging kept',
                       '量及其律移到 Amounts.lean，Amounts.whole_sum 移到 Dissipation.lean；六个整数重证删去；反模型与合并之律保留'),
    'Renewal.lean': ('imports Becoming.Amounts; falls_not_recurring proved as the whole-number instance of Amounts.rests, statement unchanged',
                     '导入 Becoming.Amounts；falls_not_recurring 作为 Amounts.rests 的整数实例证明，陈述不变'),
    'Space.lean': ('falls_stop_unrefuted proved as the whole-number instance of Amounts.rests_unrefuted, statement unchanged',
                   'falls_stop_unrefuted 作为 Amounts.rests_unrefuted 的整数实例证明，陈述不变'),
    'Dissipation.lean': ('Amounts.whole_sum moved in; Flow.takers_within_on and Flow.taking_not_recurring_from proved through Becoming.Amounts, statements unchanged',
                         'Amounts.whole_sum 移入；Flow.takers_within_on 与 Flow.taking_not_recurring_from 经 Becoming.Amounts 证明，陈述不变'),
    'Openness.lean': ('Flow.change_stops_unrefuted proved by Amounts.rests_unrefuted with no decision, statement unchanged; World.Finite.arising_iff_ceasing and World.Finite.comes_to_rest_unrefuted removed (one name per statement)',
                      'Flow.change_stops_unrefuted 由 Amounts.rests_unrefuted 不经判定证明，陈述不变；删去 World.Finite.arising_iff_ceasing 与 World.Finite.comes_to_rest_unrefuted（每个陈述一个名称）'),
    'Selection.lean': ('the pool closure (WithinClosureOf, withinClosureOf_iff, withinClosureOf_single, Flow.WithinPoolCoupling, Flow.beyond_pool_coupling, Flow.uncoupled_beyond_pool, Flow.unselected_beyond_pool) moved in; Flow.unselected_beyond_coupling_all proved at the singleton pool, statement unchanged',
                       '池的闭包（WithinClosureOf、withinClosureOf_iff、withinClosureOf_single、Flow.WithinPoolCoupling、Flow.beyond_pool_coupling、Flow.uncoupled_beyond_pool、Flow.unselected_beyond_pool）移入；Flow.unselected_beyond_coupling_all 在单元素池上证明，陈述不变'),
    'SelectionPool.lean': ('the pool closure moved to Selection.lean; Flow.unselected_beyond_coupling_all_of_pool removed', '池的闭包移到 Selection.lean；删去 Flow.unselected_beyond_coupling_all_of_pool'),
    'Readout.lean': ('Readout.image removed for Image of Becoming.Mechanism', '删去 Readout.image，改用 Becoming.Mechanism 的 Image'),
    'HexagramPlaces.lean': ('Hexagram.neither moved in from HexagramLaws.lean', 'Hexagram.neither 自 HexagramLaws.lean 移入'),
    'HexagramLaws.lean': ('Hexagram.neither moved to HexagramPlaces.lean', 'Hexagram.neither 移到 HexagramPlaces.lean'),
    'ReferencePlan.lean': ('added_keeps, new_contact_choice and trace_conserves carry the proofs through the laws; their _of_law twins removed, statements unchanged',
                           'added_keeps、new_contact_choice 与 trace_conserves 承载经律的证明；其 _of_law 孪生删去，陈述不变'),
}
DEFAULT_LEAN = ('a restatement of a statement proved under another name removed (one name per statement), or a use or docstring re-pointed to the kept name; kept statements unchanged',
                '删去以另一名称证明之陈述的重述（每个陈述一个名称），或用法与说明改指保留的名称；保留的陈述不变')


def h(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


changed = subprocess.run(['git', 'diff', '--name-only', BASE, '--'], capture_output=True, text=True, check=True).stdout.split()
LEAN = {p for p in changed if p.startswith(B) and p.endswith('.lean')}
WHAT = dict(DOCS)
for p in LEAN:
    WHAT[p] = LEAN_WHAT.get(p.rsplit('/', 1)[-1], DEFAULT_LEAN)
base = {}
for p in WHAT:
    out = subprocess.run(['git', 'show', f'{BASE}:{p}'], capture_output=True)
    base[p] = hashlib.sha256(out.stdout).hexdigest() if out.returncode == 0 else None


def binding(src):
    return {'source': src, 'receipt': RECEIPT, 'sha256_pointer': '/source_sha256/' + module_of[src],
            'success_pointer': '/status', 'success_value': 'passed'}


def short(p):
    return p.rsplit('/', 1)[-1]


def bare(x):
    return x.split(P, 1)[1] if x.startswith(P) else x


def remap(names, replaced):
    out = []
    for x in names:
        y = REMAP.get(x, x)
        if y != x:
            replaced.append((x, y))
        if y not in out:
            out.append(y)
    return out


def strings(x):
    if isinstance(x, dict):
        for k, v in x.items():
            if k == 'history':
                continue
            if isinstance(v, str):
                yield x, k
            else:
                yield from strings(v)
    elif isinstance(x, list):
        for i, v in enumerate(x):
            if isinstance(v, str):
                yield x, i
            else:
                yield from strings(v)


n = 0
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    d = json.load(open(f))
    rid = d['id']
    before = json.dumps(d, ensure_ascii=False)
    refs = d.get('references', [])
    by = {r['path']: r for r in refs}
    moved, replaced, texts = [], [], 0
    for old, new in TEXT.get(rid, []):
        hits = [(c, k) for c, k in strings(d) if old in c[k]]
        assert len(hits) == 1 and hits[0][0][hits[0][1]].count(old) == 1, (rid, old[:60], len(hits))
        c, k = hits[0]
        c[k] = c[k].replace(old, new)
        texts += 1
    for law in d.get('laws', []) or []:
        if isinstance(law, dict) and law.get('declarations'):
            law['declarations'] = remap(law['declarations'], replaced)
    # An alias is a name the record owns; a removed name's alias is dropped (its kept name has its own owner).
    if isinstance(d.get('aliases'), list):
        replaced += [(x, REMAP[x]) for x in d['aliases'] if x in REMAP]
        d['aliases'] = [x for x in d['aliases'] if x not in REMAP]

    added, filed = [], set()

    def ref_for(path, after):
        if path not in by:
            by[path] = {'path': path, 'role': 'proof', 'sha256': h(path), 'declarations': []}
            added.append(path)
            refs.insert(refs.index(after) + 1 if after in refs else len(refs), by[path])
        return by[path]

    for r in list(refs):
        if not r.get('declarations'):
            continue
        keep = []
        for x in r['declarations']:
            y = REMAP.get(x, x)
            if y != x:
                replaced.append((x, y))
            target = path_of[home[y]] if y in home else r['path']
            if target != r['path'] and (y != x or x in MOVED):
                t = ref_for(target, r)
                t.setdefault('declarations', [])
                if y not in t['declarations']:
                    t['declarations'].append(y)
                filed.add(target)
                if y == x:
                    moved.append((x, r['path'], target))
            elif y not in keep:
                keep.append(y)
        r['declarations'] = keep
    bound = {b['source'] for b in d.get('proof_bindings', [])}
    if d.get('proof_bindings'):
        for path in sorted(filed):
            if path not in bound and by[path].get('declarations'):
                d['proof_bindings'].append(binding(path))
                bound.add(path)
    rebound, touched = [], set()
    for b in d.get('proof_bindings', []):
        if b['source'] in LEAN and b['receipt'] != RECEIPT:
            assert receipt['source_sha256'][module_of[b['source']]] == h(b['source'])
            b['receipt'] = RECEIPT
            rebound.append(short(b['source']))
    for r in refs:
        p = r['path']
        if p in LEAN and any(b['source'] == p and b['receipt'] == RECEIPT for b in d.get('proof_bindings', [])):
            if r.get('sha256') != h(p):
                r['sha256'] = h(p)
                touched.add(p)
        elif p in WHAT and (r.get('sha256') == base[p] or rid in DRIFT.get(p, ())) and r.get('sha256') != h(p):
            r['sha256'] = h(p)
            touched.add(p)
    # Empty references left by a move are dropped only where nothing else cites the file.
    for r in list(refs):
        if r['role'] == 'proof' and not r.get('declarations') and any(m[1] == r['path'] for m in moved) \
                and r['path'] != d.get('canonical_source') \
                and not any(b['source'] == r['path'] for b in d.get('proof_bindings', [])):
            refs.remove(r)
    if any(b['receipt'] == RECEIPT for b in d.get('proof_bindings', [])) and not any(r['path'] == RECEIPT for r in refs):
        refs.append({'path': RECEIPT, 'role': 'receipt', 'sha256': h(RECEIPT), 'declarations': []})
    if json.dumps(d, ensure_ascii=False) == before:
        continue
    en = '20 October 2026, R29 (compression under board rule 9: generalize below, not beside; one name per statement):'
    zh = '2026年10月20日，R29（按看板规则 9 压缩：在下面推广而非并列；每个陈述一个名称）：'
    mv = sorted({(bare(x), short(a), short(c)) for x, a, c in moved})
    if mv:
        groups = {}
        for x, a, c in mv:
            groups.setdefault((a, c), []).append(x)
        en += ' Moved with their full names: ' + '; '.join(f'from {a} to {c}, ' + ', '.join(xs) for (a, c), xs in sorted(groups.items())) + '.'
        zh += '连同完整名称移动：' + '；'.join(f'从 {a} 到 {c}：' + '、'.join(xs) for (a, c), xs in sorted(groups.items())) + '。'
    rp = sorted({(bare(x), bare(y)) for x, y in replaced})
    if rp:
        en += ' Removed, with the statement kept under one name: ' + '; '.join(f'{x} (now {y})' for x, y in rp) + '.'
        zh += '删去，陈述以一个名称保留：' + '；'.join(f'{x}（现为 {y}）' for x, y in rp) + '。'
    if texts:
        en += ' The sentences that said a removed name proved something cite the kept statement.'
        zh += '说删去之名证明了什么的句子改引保留的陈述。'
    if rebound:
        en += f' Proof bindings ({", ".join(sorted(set(rebound)))}) rebound to core receipt {RID}.'
        zh += f'证明绑定（{"、".join(sorted(set(rebound)))}）改到核心回执 {RID}。'
    ps = sorted(touched)
    if ps:
        en += ' Re-pointed after reading the change: ' + '; '.join(short(p) + ', ' + WHAT[p][0] for p in ps) + '.'
        zh += '读过改动后重新指向：' + '；'.join(short(p) + '，' + WHAT[p][1] for p in ps) + '。'
    en += ' The claim is unchanged.'
    zh += '论断不变。'
    last = d['history'][-1] if d.get('history') else {}
    if last.get('en', '').startswith('20 October 2026, R29'):
        if ps:
            last['en'] = last['en'].replace(' The claim is unchanged.', ' Also re-pointed after reading the change: '
                                            + '; '.join(short(p) + ', ' + WHAT[p][0] for p in ps) + '. The claim is unchanged.')
            last['zh'] = last['zh'].replace('论断不变。', '另读过改动后重新指向：'
                                            + '；'.join(short(p) + '，' + WHAT[p][1] for p in ps) + '。论断不变。')
    else:
        d.setdefault('history', []).append({'en': en, 'zh': zh})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    n += 1
    print(rid, len(mv), len(rp), texts, sorted(set(rebound)), len(ps))
print(n, 'records changed')
