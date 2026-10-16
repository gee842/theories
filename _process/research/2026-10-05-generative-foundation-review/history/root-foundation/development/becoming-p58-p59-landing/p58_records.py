#!/usr/bin/env python3
"""P58 + P59 records: python3 -B p58_records.py ROOT SEC58 SEC59

P58 (decidedness made local):
- space-and-its-parts: World.rests and World.rests_covering lose the decision procedure on activity (unused), names
  unchanged; the settling lemmas; decidedness is the law's own condition, not a commitment of the representation;
- continued-change-needs-openness: World.comes_to_rest and World.rest_few lose it (unused); World.Finite.comes_to_rest
  loses it, its proof now using the world's relata as a covering list instead of the census it built; the settling
  forms and the covering form of the rest theorem;
- map-of-premises: World.premised_rests loses it (unused);
- laws-at-coarser-steps: World.sample_rests loses it (unused), as agreed with the integrator;
- new counts-exist-where-decided and recurrence-without-decidedness;
- related links from coming-and-ceasing-keep-pace, census-balance and whole-law-of-counting.
P59: new imbalance-as-relatum.
Claims grow by the delta; nothing earlier is removed except the words saying the rest theorems need decided activity.
New records' validation scopes follow the shape repoint.py rewrites, built from comparison-by-widening's (already
re-pointed to this run). Run after the checkers and the repoint step, so that every referenced file is final."""
import copy
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT, SEC58, SEC59 = Path(sys.argv[1]).resolve(), int(sys.argv[2]), int(sys.argv[3])
REC = ROOT / 'theories/becoming/results/records'
LB = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
B = LB + 'Becoming/'
RECEIPT = LB + 'becoming-verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
N, F, Wb, Wo = 'Becoming.', 'Becoming.Flow.', 'Becoming.Web.', 'Becoming.World.'
receipt = json.loads((ROOT / RECEIPT).read_text())
COUNT = {m['module']: m['theorems'] for m in receipt['modules']}
RUN = receipt['utc']
AXIOMS, MODULE = {}, {}
for m in receipt['modules']:
    AXIOMS.update(m['axiom_dependencies'])
    MODULE.update({d['name']: m['module'] for d in m['declarations']})


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def load(i):
    return json.loads((REC / (i + '.json')).read_text())


def save(r):
    (REC / (r['id'] + '.json')).write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')


def proof(name, decls):
    return {'path': B + name + '.lean', 'role': 'proof', 'sha256': sha(B + name + '.lean'), 'declarations': decls}


def binding(name):
    return {'source': B + name + '.lean', 'receipt': RECEIPT, 'sha256_pointer': '/source_sha256/Becoming.' + name,
            'success_pointer': '/status', 'success_value': 'passed'}


def audited(decls):
    for d in decls:
        assert AXIOMS.get(d) == [], (d, AXIOMS.get(d, 'not audited'))


def add_decls(r, mod, decls):
    audited(decls)
    path = B + mod + '.lean'
    refs = r['references']
    own = [x for x in refs if x['role'] == 'proof' and x['path'] == path]
    if own:
        assert not set(decls) & set(own[0]['declarations']), (r['id'], mod)
        own[0]['declarations'] += decls
    else:
        k = max(i for i, x in enumerate(refs) if x['role'] == 'proof')
        refs.insert(k + 1, proof(mod, list(decls)))
    if not any(b['source'] == path for b in r['proof_bindings']):
        r['proof_bindings'].append(binding(mod))
    assert not set(decls) & set(r['aliases']), r['id']
    r['aliases'] += decls


def cite(r, mod, decls):
    """Cite another record's declarations that a re-proof now uses: in the module's proof reference, bound to the
    receipt, with no alias (they are not this record's results)."""
    audited(decls)
    assert all(MODULE[d] == 'Becoming.' + mod for d in decls), (r['id'], mod)
    path = B + mod + '.lean'
    refs = r['references']
    own = [x for x in refs if x['role'] == 'proof' and x['path'] == path]
    if own:
        assert own[0]['sha256'] == sha(path), (r['id'], path, 'reconcile first')
        own[0]['declarations'] += [d for d in decls if d not in own[0]['declarations']]
    else:
        k = max(i for i, x in enumerate(refs) if x['role'] == 'proof')
        refs.insert(k + 1, proof(mod, list(decls)))
    if not any(b['source'] == path for b in r['proof_bindings']):
        r['proof_bindings'].append(binding(mod))


def extend(r, field, zh, en):
    r[field]['zh'] += zh
    r[field]['en'] += ' ' + en


def history(r, tag, zh, en):
    r['history'].append({'zh': f'2026-10-12 {tag}：' + zh, 'en': f'2026-10-12 {tag}: ' + en})
    r['reviewed_at_utc'] = NOW


def replace(r, path, old, new):
    *keys, last = path
    x = r
    for k in keys:
        x = x[k]
    assert x[last].count(old) == 1, (r['id'], path, x[last].count(old), old[:60])
    x[last] = x[last].replace(old, new)


def related(r, rid, zh, en):
    assert not any(x['id'] == rid for x in r['related']), (r['id'], rid)
    r['related'].append({'id': rid, 'detail': {'zh': zh, 'en': en}})


SEE58 = (f'见整合文档 §{SEC58} 与清点页 DECIDABILITY-INVENTORY。',
         f'See §{SEC58} of the integration note and the inventory page DECIDABILITY-INVENTORY.')
STRONGER = ('陈述更强：去掉活动的判定程序（未用到），名称不变', 'statement strengthened: the decision procedure on activity '
            'dropped (unused); name unchanged')

# ---------------------------------------------------------------- space-and-its-parts
r = load('space-and-its-parts')
SETTLE_SPACE = [N + 'still_le', N + 'unrefuted_falls_exceed', N + 'falls_settle', N + 'amount_settles',
                Wb + 'generation_settles', Wo + 'arising_unrefuted_covering']
add_decls(r, 'Space', SETTLE_SPACE)
cite(r, 'Locality', [N + 'Covers', N + 'Covers.not_not_coming_from'])
replace(r, ('claim', 'zh'), '可判定性是表示的承诺：', '可判定性是这一规律自己的条件，不是表示的承诺：')
replace(r, ('claim', 'en'), 'Decidability is a commitment of the representation:',
        "Decidedness is this law's own condition, not a commitment of the representation:")
replace(r, ('claim', 'zh'), '在有限、活动可判定、平衡、耗散且生起者体现的世界中，生起与止息都不复现（World.rests）',
        '在有限、平衡、耗散且生起者体现的世界中，生起与止息都不复现，不用判定程序（World.rests）')
replace(r, ('claim', 'en'), 'In a finite, balanced, dissipative world whose activity is decided and in which whatever '
        'arises is embodied, neither arising nor ceasing recurs (World.rests)',
        'In a finite, balanced, dissipative world in which whatever arises is embodied, neither arising nor ceasing '
        'recurs, with no decision procedure (World.rests)')
extend(r, 'claim',
       'P58：静止不用判定程序。从某步起不上升的量趋于平息：并非此后每一步之后再有下降都不能被否证（falls_settle，由 still_le、'
       'unrefuted_falls_exceed；它此后不变不能被否证，amount_settles）。从某步起被平衡与耗散的家族中，体现的成员趋于平息：并非此后每一步'
       '之后其中再有生起都不能被否证（Web.generation_settles）。有一个列表从某步起覆盖活跃者时，止息复现使此后每一步之后的生起都'
       '不能被否证（World.arising_unrefuted_covering，由 laws-of-one-step 的 Covers.not_not_coming_from），平息否证它；所以 '
       'World.rests_covering 与 World.rests 不要求活动可判定，名称不变，陈述更强。',
       'P58: rest needs no decision procedure. An amount that does not rise from some step on settles: it is not the '
       'case that after every step from then on a later fall stays unrefuted (falls_settle, from still_le and '
       'unrefuted_falls_exceed; that it stays the same from some step on cannot be refuted, amount_settles). In a family '
       'balanced and dissipated on from some step on, the embodied members settle: it is not the case that after every '
       'step from then on a later arising of one of them stays unrefuted (Web.generation_settles). With a list covering '
       'what is active from some step on, ceasing recurring '
       'leaves a later arising unrefuted after every step (World.arising_unrefuted_covering, from '
       'Covers.not_not_coming_from of laws-of-one-step), which settling refutes; so World.rests_covering and World.rests '
       'need no decided activity, their names unchanged and their statements stronger.')
replace(r, ('hypotheses', 0, 'zh'), '可判定性是表示的逻辑承诺，经典地总是成立；', '可判定性是这一规律自己的条件，不是表示的承诺，经典地总是成立；')
replace(r, ('hypotheses', 0, 'en'), 'Decidability is a logical commitment of the representation, classically always met;',
        "Decidedness is this law's own condition, not a commitment of the representation, classically always met;")
replace(r, ('hypotheses', 1, 'zh'), '与生起者体现（ArisingEmbodied），同样要求活动可判定。',
        '与生起者体现（ArisingEmbodied）；不要求活动可判定（P58）。')
replace(r, ('hypotheses', 1, 'en'), 'and whatever arises being embodied (ArisingEmbodied), with activity decided as well.',
        'and whatever arises being embodied (ArisingEmbodied); activity need not be decided (P58).')
related(r, 'recurrence-without-decidedness',
        '有限世界的规律在不要求可判定时的形式：止息永不终止、生起永不终止，以及从某步起已定时的规律。',
        'The forms of the law for finite worlds without decidedness: ceasing never stopping for good, arising never '
        'stopping for good, and the law where decided from some step on.')
history(r, 'P58', STRONGER[0].replace('去掉', 'World.rests 与 World.rests_covering 去掉') + '；平息引理（still_le、'
        'unrefuted_falls_exceed、falls_settle、amount_settles、Web.generation_settles、World.arising_unrefuted_covering）；'
        '可判定性是规律 arising_iff_ceasing 自己的条件，不是表示的承诺（Ren：“i intuitively feel decidability is too '
        'dualist”，以“please”接受把它局部化）。' + SEE58[0],
        STRONGER[1].replace('the decision procedure', 'World.rests and World.rests_covering have the decision procedure')
        .replace('dropped (unused); name unchanged', 'dropped (unused); names unchanged') + '; the settling lemmas '
        '(still_le, unrefuted_falls_exceed, falls_settle, amount_settles, Web.generation_settles, '
        'World.arising_unrefuted_covering); decidedness is the own condition of the law arising_iff_ceasing, not a '
        'commitment of the representation (Ren: “i intuitively feel decidability is too dualist”, and “please” to making '
        'it local). ' + SEE58[1])
save(r)

# ---------------------------------------------------------------- continued-change-needs-openness
r = load('continued-change-needs-openness')
SETTLE_OPEN = [F + 'change_settles', N + 'comes_after_unrefuted', N + 'Listed.few_of_settled',
               Wo + 'arising_settles_from', Wo + 'comes_to_rest_from']
add_decls(r, 'Openness', SETTLE_OPEN)
cite(r, 'Locality', [N + 'Covers', N + 'Covers.not_not_coming_from'])
replace(r, ('claim', 'zh'), '静止定理：有活动的普查（活动可判定）与所立者的普查', '静止定理：有活动的普查与所立者的普查')
replace(r, ('claim', 'en'), 'The rest theorem: a world with a census of what is active (its activity decided) and of '
        'what stands', 'The rest theorem: a world with a census of what is active and of what stands')
replace(r, ('claim', 'zh'), '水平不再变化，所以体现的生起停止；在普查之下止息复现需要生起复现（ceasing-needs-arising），所以止息也停止。',
        '水平不再变化，所以体现的生起停止，并且趋于平息：并非此后每一步之后再有生起都不能被否证（World.arising_settles_from，由 '
        'Flow.change_settles）；普查是覆盖活跃者的列表，在其下止息复现使此后每一步之后的生起都不能被否证（Covers.not_not_coming_from），'
        '平息否证它，所以止息也停止，不用判定程序（P58；World.comes_to_rest_from 只要求一个列表在此后每一步覆盖活跃者）。')
replace(r, ('claim', 'en'), 'Standing stops changing, so embodied arising stops; under a census recurring ceasing needs '
        'recurring arising (ceasing-needs-arising), so ceasing stops too.',
        'Standing stops changing, so embodied arising stops, and it settles: it is not the case that after every step '
        'from then on a later arising stays unrefuted (World.arising_settles_from, from Flow.change_settles); the census is a list covering '
        'what is active, under which ceasing recurring leaves a later arising unrefuted after every step '
        '(Covers.not_not_coming_from), which settling refutes, so ceasing stops too, with no decision procedure (P58; '
        'World.comes_to_rest_from asks only for a list covering what is active at each step from then on).')
replace(r, ('claim', 'zh'), '（World.rest_few，由 Listed.few_of_quiet）', '（World.rest_few，由 Listed.few_of_settled，不用判定程序）')
replace(r, ('claim', 'en'), '(World.rest_few, from Listed.few_of_quiet)',
        '(World.rest_few, from Listed.few_of_settled, with no decision procedure)')
replace(r, ('claim', 'zh'), '所以 World.rests 是有限情形（World.Finite.comes_to_rest）',
        '所以 World.rests 是有限情形，其关系项覆盖活跃者（World.Finite.comes_to_rest，不用判定程序）')
replace(r, ('claim', 'en'), 'so World.rests is the finite case (World.Finite.comes_to_rest)',
        'so World.rests is the finite case, its relata covering what is active (World.Finite.comes_to_rest, with no '
        'decision procedure)')
replace(r, ('claim', 'zh'), '活动的普查就是所立者的普查，活动由水平判定（World.rests_around）',
        '活动的普查就是所立者的普查（World.rests_around）')
replace(r, ('claim', 'en'), 'the census of what is active lists what stands and activity is decided by standing '
        '(World.rests_around)', 'the census of what is active lists what stands (World.rests_around)')
replace(r, ('hypotheses', 1, 'zh'), '静止定理（comes_to_rest）：另加活动的普查与活动可判定。',
        '静止定理（comes_to_rest）：另加活动的普查；不要求活动可判定（P58），普查只作覆盖活跃者的列表用（comes_to_rest_from）。')
replace(r, ('hypotheses', 1, 'zh'), '二者给出所立者的普查与活动的判定；', '二者给出所立者的普查；')
replace(r, ('hypotheses', 1, 'en'), 'The rest theorem (comes_to_rest): also a census of what is active, with activity '
        'decided.', 'The rest theorem (comes_to_rest): also a census of what is active; activity need not be decided '
        '(P58), the census serving only as a list covering what is active (comes_to_rest_from).')
replace(r, ('hypotheses', 1, 'en'), 'which together give the census of what stands and decide activity;',
        'which together give the census of what stands;')
replace(r, ('limitations', 'zh'), '但要求活动的普查、所立者的普查与活动可判定（逻辑承诺）；',
        '但要求活动的普查（只作覆盖列表用）与所立者的普查，不要求活动可判定（P58）；')
replace(r, ('limitations', 'en'), 'but needs a census of what is active, a census of what stands and decided activity (a '
        'logical commitment);', 'but needs a census of what is active (used only as a covering list) and a census of '
        'what stands, and no decided activity (P58);')
history(r, 'P58', 'World.comes_to_rest 与 World.rest_few 陈述更强：去掉活动的判定程序（未用到），名称不变；World.Finite.comes_to_rest '
        '去掉活动的判定程序，证明改以世界的关系项为覆盖列表、不再用它所造的普查（Finite.counted 需要判定程序），名称不变；平息的形式'
        '（Flow.change_settles、World.arising_settles_from、Listed.few_of_settled、comes_after_unrefuted）与覆盖形式的静止定理'
        '（World.comes_to_rest_from）。' + SEE58[0],
        'World.comes_to_rest and World.rest_few, statements strengthened: the decision procedure on activity dropped '
        '(unused); names unchanged; World.Finite.comes_to_rest, the decision procedure on activity dropped, its proof now '
        'using the world\'s relata as a covering list instead of the census it built (Finite.counted needs a decision '
        'procedure); name unchanged; the settling forms (Flow.change_settles, World.arising_settles_from, '
        'Listed.few_of_settled, comes_after_unrefuted) and the covering form of the rest theorem '
        '(World.comes_to_rest_from). ' + SEE58[1])
save(r)

# ---------------------------------------------------------------- map-of-premises
r = load('map-of-premises')
replace(r, ('claim', 'zh'), '有限、活动可判定且满足八个的世界中，生起与止息都不再复现',
        '有限且满足八个的世界中，生起与止息都不再复现，不用判定程序')
replace(r, ('claim', 'en'), 'in a finite world whose activity is decided and which meets the eight, neither arising '
        'nor ceasing recurs', 'in a finite world which meets the eight, neither arising nor ceasing recurs, with no '
        'decision procedure')
replace(r, ('hypotheses', 0, 'zh'), 'Finite.counted 与 premised_rests 要求每步每个关系项是否活跃可判定',
        'Finite.counted 要求每步每个关系项是否活跃可判定（premised_rests 不要求，P58）')
replace(r, ('hypotheses', 0, 'en'), 'Finite.counted and premised_rests need whether each relatum is active at each step '
        'to be decidable', 'Finite.counted needs whether each relatum is active at each step to be decidable '
        '(premised_rests does not, P58)')
replace(r, ('correspondence', 'zh'), '有限、被围住与可判定性不在这八个之中，而静止定理正是以它们为转折；',
        '有限与被围住不在这八个之中，而静止定理正是以它们为转折（可判定性不再需要，P58）；')
replace(r, ('correspondence', 'en'), 'Finiteness, enclosure and decidability are not among the eight, though the rest '
        'theorems turn on them;', 'Finiteness and enclosure are not among the eight, though the rest theorems turn on '
        'them (decidability is no longer needed, P58);')
replace(r, ('dependencies', 0, 'interface', 'conditions', 'zh'), '有限与活动可判定（只对 premised_rests）。',
        '有限（只对 premised_rests）。')
replace(r, ('dependencies', 0, 'interface', 'conditions', 'en'), 'Finite and decidable activity (premised_rests only).',
        'Finite (premised_rests only).')
history(r, 'P58', 'World.premised_rests ' + STRONGER[0] + '。' + SEE58[0],
        'World.premised_rests, ' + STRONGER[1] + '. ' + SEE58[1])
save(r)

# ---------------------------------------------------------------- laws-at-coarser-steps
r = load('laws-at-coarser-steps')
replace(r, ('claim', 'zh'), 'World.sample_survives、World.sample_rests）', 'World.sample_survives、World.sample_rests，后者不用判定程序）')
replace(r, ('claim', 'en'), 'World.sample_survives, World.sample_rests)',
        'World.sample_survives, and World.sample_rests, with no decision procedure)')
history(r, 'P58', 'World.sample_rests ' + STRONGER[0] + '（整合者同意在 P58 中一并修改）。' + SEE58[0],
        'World.sample_rests, ' + STRONGER[1] + ' (changed in P58, as agreed with the integrator). ' + SEE58[1])
save(r)

# ---------------------------------------------------------------- related links to the new records
for rid, zh, en in (
        ('coming-and-ceasing-keep-pace', '那里的规律在不要求判定程序时：开始成立复现时不再成立永不终止，反之亦然；从某步起已定时二者同时复现。',
         'This law without a decision procedure: where coming to be recurs, ceasing never stops for good, and conversely; '
         'decided from some step on, the two recur together.'),
        ('census-balance', '计数作为关系时，计数之间的普查不用可判定性，段内各步也不用。',
         'With counting as a relation, the census between counts needs no decidedness, not even at the steps inside the '
         'stretch.'),
        ('whole-law-of-counting', '以标记计数恰是已定之处的计数：计数存在恰当所计数者已定，判定程序的标记之和就是计数。',
         'Counting by marks is counting where decided: a count exists exactly where what it counts is decided, and a '
         'decision procedure\'s marks sum to the count.')):
    r = load(rid)
    target = 'recurrence-without-decidedness' if rid == 'coming-and-ceasing-keep-pace' else 'counts-exist-where-decided'
    related(r, target, zh, en)
    history(r, 'P58', f'新增关联 {target}（不用判定程序的形式）；断言不变。' + SEE58[0],
            f'related record {target} added (the forms with no decision procedure); the claim is unchanged. ' + SEE58[1])
    save(r)

# ---------------------------------------------------------------- new records
template = load('comparison-by-widening')
assert RUN in template['validation_scope']['zh'], 'run after the repoint step'


def scope(modules, sec):
    s = copy.deepcopy(template['validation_scope'])
    zh_mods = '、'.join(f'Becoming.{m} 的 {COUNT["Becoming." + m]} 项定理' for m in modules)
    en_mods = ', '.join(f'the {COUNT["Becoming." + m]} theorems of Becoming.{m}' for m in modules)
    for lang, pattern, new in (
            ('zh', r'Becoming\.Significance 的 \d+ 项定理、Becoming\.Regions 的 \d+ 项定理与 Becoming\.Metaethics 的 \d+ 项定理',
             zh_mods),
            ('en', r'the \d+ theorems of Becoming\.Significance, the \d+ of Becoming\.Regions and the \d+ of '
                   r'Becoming\.Metaethics', en_mods),
            ('zh', re.escape('作者反审见整合文档 §78；'), f'作者反审见整合文档 §{sec}；'),
            ('en', re.escape("The author's counterreview is in §78 of the integration note;"),
             f"The author's counterreview is in §{sec} of the integration note;")):
        assert len(re.findall(pattern, s[lang])) == 1, (lang, pattern)
        s[lang] = re.sub(pattern, lambda _: new, s[lang])
    return s


STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-11-decidability-local-imbalance-relatum.md'
INVENTORY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/DECIDABILITY-INVENTORY.md'
WORDS_ZH = ('Ren 2026-10-11：“give me more context, but i intuitively feel decidability is too dualist, also proved '
            'solutions and their pro/cons”，并以“please”接受 AI 的建议：可判定性局部化，不再是表示的承诺')
WORDS_EN = ('Ren, 11 October 2026: “give me more context, but i intuitively feel decidability is too dualist, also '
            'proved solutions and their pro/cons”, and “please” to the AI\'s suggestion that decidability be made local, '
            'no longer a commitment of the representation')


def new_record(rid, title, claim, hyps, corr, mod, decls, deps, rel, cex, lim, nxt, hist, sec, evidence,
               extra_refs=()):
    """`evidence` maps each other module a dependency or a boundary cites to the declarations cited there; each
    becomes a proof reference bound to the receipt, so that every evidence and boundary path is a reviewed source."""
    assert not (REC / (rid + '.json')).exists(), rid
    audited(decls)
    for m, ds in evidence.items():
        audited(ds)
        assert all(MODULE[d] == 'Becoming.' + m for d in ds), (rid, m, [d for d in ds if MODULE[d] != 'Becoming.' + m])
    refs = [proof(mod, decls)] + [proof(m, list(ds)) for m, ds in evidence.items()] + [
        doc(RECEIPT, 'receipt'), doc(STUDY, 'integration'), doc(CHAPTER, 'statement'), doc(SOURCE, 'provenance')] + \
        list(extra_refs)
    paths = {x['path'] for x in refs}
    assert cex and all(c['path'] in paths and c['detail']['zh'] and c['detail']['en'] for c in cex), rid
    assert all(d['interface']['evidence'] in paths for d in deps), rid
    return {
        'schema_version': 1, 'id': rid, 'title': title, 'kind': 'theorem', 'status': 'recorded-checked',
        'family': 'F01', 'reviewed_at_utc': NOW, 'claim': claim, 'hypotheses': hyps, 'correspondence': corr,
        'canonical_source': B + mod + '.lean', 'aliases': list(decls), 'dependencies': deps, 'related': rel,
        'counterexamples': cex, 'limitations': lim, 'validation_scope': scope([mod], sec), 'references': refs,
        'proof_bindings': [binding(mod)] + [binding(m) for m in evidence], 'next_delta': nxt, 'history': [hist]}


def dep(rid, relation, zh, en, out_zh, out_en, in_zh, in_en, cond_zh, cond_en, evidence):
    return {'id': rid, 'relation': relation, 'detail': {'zh': zh, 'en': en},
            'interface': {'output': {'zh': out_zh, 'en': out_en}, 'input': {'zh': in_zh, 'en': in_en},
                          'conditions': {'zh': cond_zh, 'en': cond_en}, 'evidence': evidence}}


def doc(path, role):
    return {'path': path, 'role': role, 'sha256': sha(path)}


COUNTS = [N + x for x in [
    'Decided', 'not_not_decided', 'Decided.of_not_not', 'Decided.and', 'Decided.not', 'Decided.exists_mem',
    'Decided.exists_below', 'Indicates', 'indicates_iff_decided', 'Indicates.eq_one', 'Indicates.eq_zero',
    'Indicates.unique', 'Indicates.le_one', 'Indicates.holds_of_pos', 'Indicates.decided', 'indicates_mark', 'Counts',
    'counts_iff_decided', 'Counts.unique', 'Counts.le_length', 'Counts.exists_of_pos', 'Counts.pos_of_mem',
    'Counts.eq_zero', 'counts_total', 'comings_counts', 'ceasings_counts', 'CountsAcross', 'Counts.across_step',
    'shift_succ', 'Counts.over_stretch_decided', 'Counts.over_stretch', 'CountsAcross.keep_pace', 'Counts.of_all',
    'Counts.of_none', 'Counts.listing', 'length_eq_of_same', 'Counts.listed_across', 'Counts.listed_over_stretch']]
RECURS = [N + x for x in [
    'holds_on', 'comes_once', 'ceases_once_of', 'coming_steps_within', 'ceasing_steps_within', 'Recurs.steps_found',
    'Recurs.ceasing_within', 'Recurs.coming_within', 'Recurs.ceasing_not_stopping', 'Recurs.coming_not_stopping',
    'Recurs.ceasing_found', 'Recurs.coming_found', 'coming_recurs_iff_decided', 'Web.unceasing_iff_decided',
    'World.ceasing_not_stopping', 'World.arising_not_stopping', 'World.arising_iff_ceasing_decided',
    'World.arising_iff_ceasing_of_decidable', 'World.ceasing_not_stopping_covered', 'World.arising_not_stopping_covered',
    'World.arising_iff_ceasing_covered']]
module_decls = set(m for mm in receipt['modules'] if mm['module'] == 'Becoming.Decidedness'
                   for m in mm['axiom_dependencies'])
assert set(COUNTS) | set(RECURS) <= module_decls, sorted((set(COUNTS) | set(RECURS)) - module_decls)
assert not (module_decls - set(COUNTS) - set(RECURS)), sorted(module_decls - set(COUNTS) - set(RECURS))

r = new_record(
    'counts-exist-where-decided',
    {'zh': '计数是关系：计数存在恰当所计数者已定，判定程序的标记就是计数；计数之间的普查不用可判定性',
     'en': 'Counting is a relation: a count exists exactly where what it counts is decided, and a decision procedure\'s '
           'marks are the count; the census between counts needs no decidedness'},
    {'zh': '一个命题已定（Decided），是指它成立或不成立；判定程序（Decidable）把这一点作为数据给出，核心的逻辑不对每个命题假定它，'
           '已定不能被否证（not_not_decided）。一个数指示一个命题（Indicates），是指它为一而命题成立，或为零而命题不成立；一个数计列表中'
           '某规定成立的成员（Counts），是指它是这些指示之和；跨一列步，各步的计数相加（CountsAcross）。某数指示一个命题恰当该命题已定'
           '（indicates_iff_decided），列表的计数存在恰当每个成员已定（counts_iff_decided）；计数唯一（Counts.unique），不超过成员数'
           '（Counts.le_length）；判定程序给出的标记之和就是计数（counts_total、comings_counts、ceasings_counts）。计数之间的普查不用可判定'
           '性：一段步上，只要计数存在，终点成立的加其间不再成立的，等于起点成立的加其间开始成立的（Counts.over_stretch），段内各步也不'
           '要求已定：段内各步已定时它成立（Counts.over_stretch_decided），有限多个状态都已定不能被否证，而数的等式在其否定被否证处成立。'
           '跨一步亦然（Counts.across_step）；开始与不再成立的计数相差不超过成员数（CountsAcross.keep_pace）。成立者在各步被列出、每个一次'
           '时，列表本身给出普查，也不用可判定性（Counts.listed_across、Counts.listed_over_stretch）：计数是被计成员列表的长度'
           '（Counts.listing），成员相同、不重复的两个列表一样长（length_eq_of_same）。不用伦理前提，也不用 Lean 公理。',
     'en': 'A proposition is decided (Decided) where it holds or fails; a decision procedure (Decidable) gives this as '
           'data, the core\'s logic does not assume it of every proposition, and that a proposition is decided cannot be '
           'refuted (not_not_decided). A number indicates a proposition (Indicates) where it is one and the proposition '
           'holds, or zero and it fails; a number counts the members of a list of which a determination holds (Counts) '
           'where it sums their indicators; across a list of steps, the counts at each step sum (CountsAcross). Something '
           'indicates a proposition exactly where the proposition is decided (indicates_iff_decided), and a count of a '
           'list exists exactly where each member is decided (counts_iff_decided); a count is one number (Counts.unique), '
           'at most the members (Counts.le_length), and where a procedure decides, its marks are the count '
           '(counts_total, comings_counts, ceasings_counts). The census between counts needs no decidedness: over a '
           'stretch, wherever the counts exist, those holding at the end with those that ceased are those holding at the '
           'start with those that came to be (Counts.over_stretch), with no decidedness even at the steps inside the '
           'stretch: decided there, the census holds (Counts.over_stretch_decided), that finitely many states are all '
           'decided cannot be refuted, and an equation of numbers holds wherever its failure is refuted. Likewise across '
           'one step (Counts.across_step), and comings and ceasings differ by at most the members '
           '(CountsAcross.keep_pace). Where what holds is listed at each step, each member once, the lists give the census '
           'with no decidedness either (Counts.listed_across, Counts.listed_over_stretch): a count is the length of a list '
           'of the members counted (Counts.listing), and two lists without repetition with the same members are equally '
           'long (length_eq_of_same). No ethical premise and no Lean axiom is used.'},
    [{'zh': '计数的规律：计数存在（Counts）；段内各步不要求已定。', 'en': 'The laws of counting: the counts exist (Counts); the steps '
      'inside the stretch need not be decided.'},
     {'zh': '列出的形式：成立者在各步被列出、每个一次（Listed）。', 'en': 'The listed forms: what holds is listed at each step, each '
      'member once (Listed).'},
     {'zh': '离散的步；有限的列表。', 'en': 'Discrete steps; finite lists.'}],
    {'zh': WORDS_ZH + '（零前提计划 §1.4 (b2)）。AI 的读法：“too dualist”读作强加给生成的是或否之分；“局部”读作只在所计数之处、作为该规律'
           '自己的条件。计数之间的规律对任何存在的计数成立，不要求它们存在；需要计数的陈述把已定写作条件，范围是所计数之处。读法待 Ren。',
     'en': WORDS_EN + ' (zero-premise plan, section 1.4 (b2)). The AI\'s reading: “too dualist” is the yes/no split '
           'imposed on becoming; “local” is at the states counted only, as that law\'s own condition. The laws between '
           'counts hold of whatever counts exist, without asking that they exist; a statement that needs a count states '
           'decidedness as its condition, at what it counts. The reading awaits Ren.'},
    'Decidedness', COUNTS,
    [dep('coming-and-ceasing-keep-pace', 'formal-reuse',
         '复用开始成立与不再成立（ComesToBe、CeasesToBe）及以判定程序的标记对它们的计数（mark、comings、ceasings）。',
         'Reuses coming to be and ceasing (ComesToBe, CeasesToBe) and their counts by a decision procedure\'s marks '
         '(mark, comings, ceasings).',
         '跨一步的开始成立与不再成立，以及以标记对它们的计数。', 'Coming to be and ceasing across a step, and their counts by marks.',
         '判定程序的标记之和就是计数（counts_total、comings_counts、ceasings_counts）；计数作为关系，存在恰当所计数者已定。',
         'Where a procedure decides, its marks sum to the count (counts_total, comings_counts, ceasings_counts); a count '
         'as a relation, existing exactly where what it counts is decided.',
         '判定程序（只对 counts_total、comings_counts、ceasings_counts）。',
         'A decision procedure (counts_total, comings_counts and ceasings_counts only).', B + 'Change.lean')],
    [{'id': 'recurrence-without-decidedness', 'detail': {
        'zh': '同一模块：复现的规律在不要求可判定时的形式。', 'en': 'The same module: the laws of recurrence without decidedness.'}},
     {'id': 'census-balance', 'detail': {
         'zh': '那里成立者在各步被列出时，普查平衡以标记计数（Listed.across、Listed.over_stretch）；这里同一普查在计数之间成立，不用可'
               '判定性（Counts.listed_across、Counts.listed_over_stretch、Counts.over_stretch）。',
         'en': 'There, with what holds listed at each step, the census balance is counted by marks (Listed.across, '
               'Listed.over_stretch); here the same census holds between counts, with no decidedness (Counts.listed_across, '
               'Counts.listed_over_stretch, Counts.over_stretch).'}},
     {'id': 'whole-law-of-counting', 'detail': {
         'zh': '那里的规律以标记计数；这里计数是关系，存在恰当所计数者已定，所以以标记计数就是已定之处的计数。',
         'en': 'There the laws count by marks; here a count is a relation, existing exactly where what it counts is '
               'decided, so counting by marks is counting where decided.'}}],
    [{'path': B + 'Space.lean', 'detail': {
        'zh': 'undecided 世界（World.undecided）有限，生起复现（World.undecided_world）；要求每个有限世界中生起复现给出止息复现的规律，'
              '在 undecided Q 上判定任一命题 Q（World.law_decides），所以对每个有限世界要求复现的规律而不给已定，就是排中律'
              '（World.law_iff_em）：计数之间的规律不用可判定性，复现的确切形式要用。',
        'en': 'The undecided world (World.undecided) is finite, with arising recurring (World.undecided_world); a law '
              'giving ceasing recurring from arising recurring in every finite world decides any proposition Q at '
              'undecided Q (World.law_decides), so asking the recurrence law of every finite world without decidedness '
              'is excluded middle (World.law_iff_em): the laws between counts need no decidedness, the exact form of '
              'recurrence does.'}}],
    {'zh': '计数存在要求所计数者已定，这是定理（counts_iff_decided），不是对世界的前提；陈述以 mark 计数的定理仍以判定程序为自己的条件，'
           '清点页逐条列出；只对离散步与有限列表陈述；读法是 AI 的，待 Ren。',
     'en': 'A count existing needs what it counts to be decided, a theorem (counts_iff_decided), not a premise on worlds; '
           'theorems whose statements count by mark keep a decision procedure as their own condition, listed on the '
           'inventory page; stated for discrete steps and finite lists; the readings are the AI\'s, pending Ren.'},
    {'zh': '以 Counts 重述以 mark 计数的定理（清点页的“陈述依赖它”一类）；Ren 对读法的确认。',
     'en': 'Restating the theorems counted by mark with Counts (the inventory page\'s class of statements depending on '
           'it); Ren\'s confirmation of the reading.'},
    {'zh': f'2026-10-12 P58：新增，按{WORDS_ZH}；新核心模块 Becoming.Decidedness，按工作板认领；见整合文档 §{SEC58}。',
     'en': f'2026-10-12 P58: added, following {WORDS_EN}; new core module Becoming.Decidedness, claimed on the work '
           f'board; see §{SEC58} of the integration note.'},
    SEC58,
    {'Change': [N + 'ComesToBe', N + 'CeasesToBe', N + 'mark', N + 'comings', N + 'ceasings'],
     'Space': [Wo + 'undecided', Wo + 'undecided_world', Wo + 'law_decides', Wo + 'law_iff_em']},
    [doc(INVENTORY, 'integration')])
save(r)

r = new_record(
    'recurrence-without-decidedness',
    {'zh': '复现不用可判定性：有限家族中开始成立复现时不再成立永不终止，反之亦然；在所寻之处已定时找到那一步，从某步起已定时二者同时复现',
     'en': 'Recurrence with no decidedness: in a finite family, where coming to be recurs ceasing never stops for good, '
           'and conversely; decided where it is sought the step is found, and decided from some step on the two recur '
           'together'},
    {'zh': '有限家族中，没有东西不再成立时，每个成员至多开始成立一次（comes_once）；没有东西开始成立时，每个成员至多不再成立一次'
           '（ceases_once_of）。所以一段中看到成员开始成立、或不再成立的不同步数不多于成员数（coming_steps_within、ceasing_steps_within）。'
           '由此，开始成立复现时，从每一步起都有一段，其中有东西不再成立不能被否证（Recurs.ceasing_within），不再成立永不终止：从某步起'
           '再没有不再成立被否证（Recurs.ceasing_not_stopping）；反之亦然（Recurs.coming_within、Recurs.coming_not_stopping）。不用可判定性。'
           '那一段的状态已定时，那一步被找到（Recurs.ceasing_found、Recurs.coming_found）；从某步起已定时，开始成立复现恰当不再成立复现'
           '（coming_recurs_iff_decided），不要判定程序，而 coming_recurs_iff 在每一步都要求判定程序。依存网中形成有限多时亦然'
           '（Web.unceasing_iff_decided）。有限世界中，生起复现时止息永不终止，反之亦然，不用可判定性（World.ceasing_not_stopping、'
           'World.arising_not_stopping）；从某步起已定时生起复现恰当止息复现（World.arising_iff_ceasing_decided），World.arising_iff_ceasing '
           '是由判定程序从第一步起已定的情形（World.arising_iff_ceasing_of_decidable）；有一个列表从某步起覆盖活跃者时亦然，已定只问列表的'
           '成员（World.ceasing_not_stopping_covered、World.arising_not_stopping_covered、World.arising_iff_ceasing_covered）。不用伦理前提，也不用 '
           'Lean 公理。',
     'en': 'In a finite family, while nothing of it ceases each member comes to be at most once (comes_once), and while '
           'nothing comes to be each ceases at most once (ceases_once_of); so no more steps of a stretch see a member come '
           'to be, or cease, than the family has members (coming_steps_within, ceasing_steps_within). Hence, where coming '
           'to be recurs, from any step there is a stretch in which something ceasing cannot be refuted '
           '(Recurs.ceasing_within), and ceasing never stops for good: that from some step on nothing ceases is refuted '
           '(Recurs.ceasing_not_stopping); and conversely (Recurs.coming_within, Recurs.coming_not_stopping). No '
           'decidedness is used. With the states of that stretch decided, the step is found (Recurs.ceasing_found, '
           'Recurs.coming_found); decided from some step on, coming to be recurs exactly where ceasing does '
           '(coming_recurs_iff_decided), with no decision procedure, where coming_recurs_iff asks one at every step. '
           'The same holds of a web with finitely many formations '
           '(Web.unceasing_iff_decided). In a finite world, where arising recurs ceasing never stops for good, and '
           'conversely, with no decidedness (World.ceasing_not_stopping, World.arising_not_stopping); decided from some '
           'step on, arising recurs exactly when ceasing does (World.arising_iff_ceasing_decided), World.arising_iff_ceasing '
           'being the case decided by a procedure from the first step (World.arising_iff_ceasing_of_decidable); with a list '
           'covering what is active from some step on the same holds, decidedness asked only of the list\'s members '
           '(World.ceasing_not_stopping_covered, World.arising_not_stopping_covered, World.arising_iff_ceasing_covered). No '
           'ethical premise and no Lean axiom is used.'},
    [{'zh': '不终止的形式：家族有限（一个列表覆盖它），不要求可判定。', 'en': 'The forms that never stop: the family is finite (a list '
      'covers it), with no decidedness.'},
     {'zh': '找到一步的形式：所寻那一段的状态已定；同时复现的形式：从某步起已定。', 'en': 'The forms finding a step: the states of the '
      'stretch searched decided; the forms recurring together: decided from some step on.'},
     {'zh': '离散的步。', 'en': 'Discrete steps.'}],
    {'zh': WORDS_ZH + '。AI 的读法：不终止的形式是双重否定的复现，不指出在哪一步，但排除“从某步起再没有”；这正是已证的界：不给已定时，'
           '命名一步需要有限全知原则（World.lpo_of_finite_ends、Listed.lpo_of_few、Web.lpo_of_ending），对每个有限世界要求复现需要排中律'
           '（World.law_iff_em）。读法待 Ren。',
     'en': WORDS_EN + '. The AI\'s reading: the forms that never stop are recurrence doubly negated, naming no step but '
           'excluding “none from some step on”; this is the proved boundary: without decidedness, naming a step needs the '
           'limited principle of omniscience (World.lpo_of_finite_ends, Listed.lpo_of_few, Web.lpo_of_ending), and asking '
           'recurrence of every finite world needs excluded middle (World.law_iff_em). The reading awaits Ren.'},
    'Decidedness', RECURS,
    [dep('coming-and-ceasing-keep-pace', 'formal-reuse', '复用开始成立与不再成立（ComesToBe、CeasesToBe）与家族中的复现（Recurs）。',
         'Reuses coming to be and ceasing (ComesToBe, CeasesToBe) and recurrence in a family (Recurs).',
         '开始成立、不再成立与其复现；有限家族中，以判定程序，一方复现恰当另一方复现（coming_recurs_iff）。',
         'Coming to be, ceasing and their recurrence; in a finite family, with a decision procedure, each recurs exactly '
         'when the other does (coming_recurs_iff).',
         '同一规律不用判定程序：永不终止的形式，以及从某步起已定时的形式。',
         'The same law with no decision procedure: the forms that never stop, and the form decided from some step on.',
         '有限家族。', 'A finite family.', B + 'Change.lean'),
     dep('space-and-its-parts', 'formal-reuse',
         '复用世界、有限、生起复现与止息复现（World、World.Finite、World.ArisingRecurs、World.CeasingRecurs）。',
         'Reuses worlds, finiteness, and arising and ceasing recurring (World, World.Finite, World.ArisingRecurs, '
         'World.CeasingRecurs).',
         '世界与其复现；活动可判定的有限世界中生起复现恰当止息复现（World.arising_iff_ceasing）。',
         'Worlds and their recurrence; in a finite world whose activity is decided, arising recurs exactly when ceasing '
         'does (World.arising_iff_ceasing).',
         '有限世界中不要求可判定时的形式与从某步起已定时的形式。',
         'For finite worlds, the forms without decidedness and the form decided from some step on.',
         '有限世界，或从某步起覆盖活跃者的列表。', 'A finite world, or a list covering what is active from some step on.',
         B + 'Space.lean')],
    [{'id': 'counts-exist-where-decided', 'detail': {
        'zh': '同一模块：计数作为关系。', 'en': 'The same module: counting as a relation.'}},
     {'id': 'recurrence-without-premise', 'detail': {
        'zh': '那里每条变化规律不加前提，无损恰当在有限构形中返回；这里有限家族的复现不加可判定性。',
        'en': 'There every law of change, with no premise, is lossless exactly when it returns within finite '
              'configurations; here the recurrence of a finite family needs no decidedness.'}},
     {'id': 'laws-of-one-step', 'detail': {
         'zh': '那里一个列表从某步起覆盖活跃者时，止息复现使此后每一步之后的生起都不能被否证（Covers.not_not_coming_from）；这里有这样'
               '的列表时，复现的不终止形式，以及只问列表成员已定的规律。',
         'en': 'There, with a list covering what is active from some step on, ceasing recurring leaves a later arising '
               'unrefuted after every step (Covers.not_not_coming_from); here, with such a list, the forms of recurrence '
               'that never stop, and the law asking decidedness only of the list\'s members.'}}],
    [{'path': B + 'Space.lean', 'detail': {
        'zh': 'undecided 世界（World.undecided）有限，生起复现（World.undecided_world）；要求每个有限世界中生起复现给出止息复现的规律，'
              '在 undecided Q 上判定任一命题 Q（World.law_decides），所以对每个有限世界要求确切的复现规律而不给已定，就是排中律'
              '（World.law_iff_em）；不终止的形式不要求已定。',
        'en': 'The undecided world (World.undecided) is finite, with arising recurring (World.undecided_world); a law '
              'giving ceasing recurring from arising recurring in every finite world decides any proposition Q at '
              'undecided Q (World.law_decides), so asking the exact recurrence law of every finite world without '
              'decidedness is excluded middle (World.law_iff_em); the forms that never stop ask no decidedness.'}}],
    {'zh': '不终止的形式不指出在哪一步；命名一步需要所寻之处已定，对每个世界要求复现需要从某步起已定；只对离散步陈述；读法是 AI 的，待 Ren。',
     'en': 'The forms that never stop name no step; naming one needs decidedness where it is sought, and asking '
           'recurrence of every world needs decidedness from some step on; stated for discrete steps; the readings are '
           'the AI\'s, pending Ren.'},
    {'zh': '以不终止的形式重述其余只在证明中用到可判定性的复现规律（清点页逐条列出理由）；Ren 对读法的确认。',
     'en': 'Restating the other recurrence laws that use decidedness only in their proofs in the forms that never stop '
           '(the inventory page gives each one\'s reason); Ren\'s confirmation of the reading.'},
    {'zh': f'2026-10-12 P58：新增，按{WORDS_ZH}；新核心模块 Becoming.Decidedness，按工作板认领；见整合文档 §{SEC58}。',
     'en': f'2026-10-12 P58: added, following {WORDS_EN}; new core module Becoming.Decidedness, claimed on the work '
           f'board; see §{SEC58} of the integration note.'},
    SEC58,
    {'Change': [N + 'ComesToBe', N + 'CeasesToBe', N + 'Recurs', N + 'Web.Ceases', N + 'coming_recurs_iff',
                N + 'Web.unceasing_iff'],
     'Space': [N + 'World', Wo + 'Finite', Wo + 'ArisingRecurs', Wo + 'CeasingRecurs', Wo + 'arising_iff_ceasing',
               Wo + 'undecided', Wo + 'undecided_world', Wo + 'law_decides', Wo + 'law_iff_em']})
save(r)

# ---------------------------------------------------------------- P59: imbalance-as-relatum
IMB = [N + 'sub_eq_zero_of_le', N + 'le_of_sub_eq_zero', N + 'mem_of_some_mem'] + [F + x for x in [
    'withImbalance', 'withImbalance_taken', 'withImbalance_given', 'withImbalance_balances', 'withImbalance_balancesOn',
    'balancesOn_iff_idle', 'balances_iff_idle', 'withImbalance_acting_at_iff', 'withImbalance_taking_at_iff',
    'withImbalance_acting_taking_on_iff', 'withImbalance_acting_iff', 'withImbalance_taking_iff',
    'withImbalance_acting_taking_iff']]
imb_decls = set(m for mm in receipt['modules'] if mm['module'] == 'Becoming.Imbalance' for m in mm['axiom_dependencies'])
assert set(IMB) == imb_decls, (sorted(set(IMB) ^ imb_decls))
WORDS59_ZH = 'Ren 2026-10-11 以“please”接受 AI 的建议：把不平衡算作关系项，先作为与现行表示等价的表示加以证明，是否采用由 Ren 定'
WORDS59_EN = ('Ren, 11 October 2026: “please”, to the AI\'s suggestion that counting an imbalance as a relatum first be '
              'proved as a representation equivalent to the current one, adoption staying with Ren')
r = new_record(
    'imbalance-as-relatum',
    {'zh': '不平衡作为关系项：算入不平衡，每个流都平衡；平衡恰是新增关系项闲置，两种表示逐步等价',
     'en': 'Imbalance as a relatum: with the imbalance counted, every flow balances; balance is exactly the added relatum '
           'idle, and the two representations are equivalent step by step'},
    {'zh': '一步上，一个条件的水平按流所给、所取改变，恰当流在那里平衡。不平衡之处，把差额算作又一个关系项 none 的交换：它给每个条件其水平'
           '超出流的净交换而升的部分，取其超出而降的部分（Flow.withImbalance，Flow.withImbalance_given、Flow.withImbalance_taken）；依存网'
           '照 rest-with-refinement-counted 的细分读入它：从不活跃，不要求任何东西（Web.withRefinement）。于是扩展的流在每一步、每个条件上'
           '平衡（Flow.withImbalance_balances），在每个家族上亦然（Flow.withImbalance_balancesOn）。流在一个家族上跨一步平衡，恰当新增的关系'
           '项在那里对其成员不给不取（Flow.balancesOn_iff_idle），处处平衡恰当它处处闲置（Flow.balances_iff_idle）。两种表示逐步等价：在一步'
           '一个条件上，扩展的流中只有活跃者给予，恰当原流中只有活跃者给予且水平不超出净交换而升（Flow.withImbalance_acting_at_iff）；只有'
           '活跃者取、只取其所汲取的，恰当原流如此且水平不超出净交换而降（Flow.withImbalance_taking_at_iff）；所以在一个家族上跨一步，二者在'
           '扩展的流上成立，恰当二者在原流上成立且流在那里平衡（Flow.withImbalance_acting_taking_on_iff）；全步全条件的形式是推论'
           '（Flow.withImbalance_acting_iff、Flow.withImbalance_taking_iff、Flow.withImbalance_acting_taking_iff）。自然数的截断减法不丢失'
           '信息：给与取各取一边的差额，一边为零（sub_eq_zero_of_le、le_of_sub_eq_zero）。不用伦理前提，也不用 Lean 公理。',
     'en': 'Across a step, a condition\'s level changes by what the flow gives and takes exactly where the flow balances '
           'there. Wherever it does not, the difference is counted as the exchange of one more relatum, none: it gives '
           'each condition what its level rose beyond the flow\'s net exchange, and takes what its level fell beyond it '
           '(Flow.withImbalance, Flow.withImbalance_given, Flow.withImbalance_taken); the web reads it as the refinement '
           'of rest-with-refinement-counted is read, never active and requiring nothing (Web.withRefinement). Then the '
           'extended flow balances at every step and condition (Flow.withImbalance_balances), and on every family '
           '(Flow.withImbalance_balancesOn). The flow balances on a family across a step exactly where the added relatum '
           'neither gives nor takes on its members there (Flow.balancesOn_iff_idle), and everywhere exactly where it is '
           'idle everywhere (Flow.balances_iff_idle). The two representations are equivalent step by step: at a step and '
           'condition, in the extended flow only active relata give exactly where only active relata give in the flow and '
           'the level does not rise beyond the flow\'s net exchange (Flow.withImbalance_acting_at_iff), and only active '
           'relata take, and only what they draw on, exactly where they do so in the flow and the level does not fall '
           'beyond it (Flow.withImbalance_taking_at_iff); so on a family across a step both hold of the extended flow '
           'exactly where both hold of the flow and it balances there (Flow.withImbalance_acting_taking_on_iff), the forms '
           'over every step and condition being corollaries (Flow.withImbalance_acting_iff, Flow.withImbalance_taking_iff, '
           'Flow.withImbalance_acting_taking_iff). Truncated subtraction loses nothing: giving and taking each take one side '
           'of the difference, the other being zero (sub_eq_zero_of_le, le_of_sub_eq_zero). No ethical premise and no Lean '
           'axiom is used.'},
    [{'zh': '任意流与依存网；新增的关系项从不活跃、不要求任何东西。', 'en': 'Any flow and web; the added relatum is never active and '
      'requires nothing.'},
     {'zh': '离散的步；自然数的水平。', 'en': 'Discrete steps; natural-number levels.'}],
    {'zh': WORDS59_ZH + '（零前提计划 §1.4 的重新奠定）。AI 的读法：算入不平衡后，平衡是表示的性质，它对世界所说的改由一个关系项的不活跃来说；'
           '哪种读法更好由 Ren 定。核心的规律仍以 Flow.BalancesOn 为局部条件。',
     'en': WORDS59_EN + ' (the re-founding of the zero-premise plan, section 1.4). The AI\'s reading: with the imbalance '
           'counted, balance is a property of the representation, and what it said of a world is said instead by the '
           'inactivity of one relatum; which reading is better is Ren\'s. The laws of the core keep Flow.BalancesOn as a '
           'local condition.'},
    'Imbalance', IMB,
    [dep('rest-with-refinement-counted', 'formal-reuse', '复用把细分算作从不活跃、不要求任何东西的关系项的读法（Web.withRefinement）。',
         'Reuses reading the refinement as a relatum never active and requiring nothing (Web.withRefinement).',
         '细分作为惰性的关系项。', 'The refinement as an inert relatum.', '不平衡作为同样的惰性关系项。',
         'The imbalance as the same kind of inert relatum.', '无。', 'None.', B + 'Resolution.lean'),
     dep('laws-of-one-step', 'formal-reuse', '复用局部的平衡（Flow.BalancesOn）。', 'Reuses local balance (Flow.BalancesOn).',
         '一个家族上跨一步的平衡。', 'Balance on a family across a step.', '它恰是新增关系项闲置。',
         'It is exactly the added relatum idle.', '无。', 'None.', B + 'Flow.lean')],
    [{'id': 'map-of-premises', 'detail': {
        'zh': '那里一个世界满足平衡以外的每个前提（World.unbalanced_but）；这里平衡恰是新增关系项闲置（Flow.balancesOn_iff_idle）。',
        'en': 'There a world meets every premise but balance (World.unbalanced_but); here balance is exactly the added '
              'relatum idle (Flow.balancesOn_iff_idle).'}}],
    [{'path': B + 'Premises.lean', 'detail': {
        'zh': 'unbalanced 世界，即没有流的 Shuttle 两侧，满足平衡以外的每个前提（World.unbalanced_but）：平衡是世界在满足其余前提时'
              '仍可不满足的条件。算入不平衡不去掉这一条件，只移动它：流在一个家族上跨一步平衡，恰当新增的关系项在那里闲置'
              '（Flow.balancesOn_iff_idle）；扩展的流在那里满足活动前提，恰当原流满足它们且在那里平衡'
              '（Flow.withImbalance_acting_taking_on_iff）。等价不是采用；核心仍以平衡为局部条件。',
        'en': 'The unbalanced world, the sides of Shuttle with no flow, meets every premise but balance '
              '(World.unbalanced_but): balance is a condition a world can fail while meeting the others. Counting the '
              'imbalance does not remove the condition but moves it: a flow balances on a family across a step exactly '
              'where the added relatum is idle there (Flow.balancesOn_iff_idle), and the extended flow meets the '
              'activity premises there exactly where the flow meets them and balances there '
              '(Flow.withImbalance_acting_taking_on_iff). The equivalence is not an adoption; the core keeps balance as a '
              'local condition.'}}],
    {'zh': '这是表示之间的等价，不是采用：核心的规律仍以平衡为局部条件；等价不说明哪种读法更好，也不说明世界在哪里平衡；只对离散步与自然数'
           '的量陈述；读法是 AI 的，待 Ren；尚无独立审查。',
     'en': 'This is an equivalence of representations, not an adoption: the laws of the core keep balance as a local '
           'condition; the equivalence says neither which reading is better nor where a world balances; stated for '
           'discrete steps and natural-number amounts; the readings are the AI\'s, pending Ren; not yet independently '
           'reviewed.'},
    {'zh': 'Ren 决定是否采用；采用时核心的规律以新增关系项的闲置陈述平衡。',
     'en': 'Ren\'s decision whether to adopt it; adopted, the core\'s laws would state balance as the added relatum '
           'idle.'},
    {'zh': f'2026-10-12 P59：新增，按{WORDS59_ZH}；新核心模块 Becoming.Imbalance，按工作板认领；见整合文档 §{SEC59}。',
     'en': f'2026-10-12 P59: added, following {WORDS59_EN}; new core module Becoming.Imbalance, claimed on the work board; '
           f'see §{SEC59} of the integration note.'},
    SEC59,
    {'Resolution': [Wb + 'withRefinement'],
     'Flow': [F + 'BalancesOn', F + 'Balances', F + 'Acting', F + 'Taking'],
     'Premises': [Wo + 'unbalanced_but']})
save(r)
print('P58 + P59 records written:', SEC58, SEC59)
