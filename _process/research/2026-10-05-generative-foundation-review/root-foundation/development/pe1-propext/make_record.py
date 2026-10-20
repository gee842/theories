#!/usr/bin/env python3
"""Write PE1's record and add it to the related records of generalization-through-lumping:
python3 -B make_record.py CORE_RECEIPT STUDY_SECTION   (from the checkout root, after apply_text.py)

Every declaration cited is resolved against the receipt's audited declarations of Becoming.PropositionIdentity (a short
name must match exactly one declaration by suffix), and the receipt must bind the module's current bytes."""
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path.cwd()
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
KIT = '_process/research/2026-10-05-generative-foundation-review/root-foundation/development/pe1-propext'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
RECORDS = ROOT / 'theories/becoming/results/records'
MOD = 'PropositionIdentity'
core_id, N = sys.argv[1], int(sys.argv[2])
RECEIPT = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
core = json.loads((ROOT / RECEIPT).read_text())
assert core['status'] == 'passed'
HEAD = f'## {N}. What identifying interderivable propositions keeps and loses (PE1)'
assert re.search('^' + re.escape(HEAD) + '$', (ROOT / STUDY).read_text(), re.M)


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def src(mod):
    return f'{PKG}/Becoming/{mod}.lean'


def decls(mod):
    m = next(m for m in core['modules'] if m['module'] == f'Becoming.{mod}')
    assert core['source_sha256'][f'Becoming.{mod}'] == sha(src(mod)), ('receipt does not bind', mod)
    return m


def resolve(mod, names):
    full = [d['name'] for d in decls(mod)['declarations']]
    out = []
    for n in names:
        hits = [f for f in full if f == 'Becoming.' + n or f.endswith('.' + n)]
        assert len(hits) == 1, (mod, n, hits)
        out.append(hits[0])
    return out


m = decls(MOD)
assert not any(m['axiom_dependencies'].values())
n_decl, n_thm = len(m['declarations']), sum(1 for d in m['declarations'] if d.get('kind') == 'theorem')

BOUNDS = ['no-ethical-premise', 'no-evaluation', 'formal-not-empirical', 'names-provisional', 'omission-not-refutation']


def dep(rid, relation, en, zh, out_en, out_zh, in_en, in_zh, cond_en, cond_zh, evidence):
    return {'id': rid, 'relation': relation, 'detail': {'en': en, 'zh': zh},
            'interface': {'output': {'en': out_en, 'zh': out_zh}, 'input': {'en': in_en, 'zh': in_zh},
                          'conditions': {'en': cond_en, 'zh': cond_zh}, 'evidence': evidence}}


RID = 'proposition-identity'
P = 'PropositionIdentity.'
laws = [
    ('propext is a lumping of every reading: a reading of propositions is lumped (Learning.Lumped) by interderivability, '
     'read through the two ends of an interderivation, exactly where it takes one value at both ends of every one; '
     'propext, as a proposition (Extensional), holds exactly where every reading into propositions is so lumped, and '
     'then every reading into any type is.',
     'propext 是对每个读法的归并：命题的一个读法经一个互推的两端按可互推归并（Learning.Lumped），恰当它在每个互推的两端取同一值；'
     '作为命题的 propext（Extensional）恰在每个到命题的读法都如此归并之处成立，此时到任何类型的读法都如此。',
     [P + 'Extensional', P + 'Interderivation', P + 'endOf', P + 'relation', P + 'lumped_iff',
      P + 'extensional_iff_lumped', P + 'lumped_of_extensional']),
    ('Readings built from relations need no axiom: a formula built from atoms, the two constants, conjunction, '
     'disjunction, implication and quantifiers over any type takes interderivable atoms to interderivable '
     'propositions, so a reading of one proposition through a formula, the other atoms fixed, respects '
     'interderivability, with iff, not equality.',
     '由关系构成的读法不需公理：由原子、两个常值、合取、析取、蕴涵与对任何类型的量词构成的公式把可互推的原子变为可互推的命题，'
     '所以经公式读一个命题（其余原子固定）尊重可互推，给出 ↔，不是 =。',
     [P + 'Formula', P + 'Formula.eval', P + 'Formula.eval_congr', P + 'Formula.atoms', P + 'Formula.read',
      P + 'Formula.read_congr']),
    ('The reading that needs propext reads by name: the identity reading is lumped by interderivability exactly where '
     'propext holds, and where it is, every reading is.',
     '需要 propext 的读法是按名读：恒等读法恰在 propext 成立处按可互推归并；它如此之处，每个读法都如此。',
     [P + 'byName', P + 'byName_lumped_iff', P + 'lumped_of_byName']),
    ('What a derivation carries: any two witnesses of a ↔ b are equal, as are any two derivations of b from a, so the '
     'identification forgets no witness; between types it would, since Bool has two different self-inverse maps, the '
     'identity and negation.',
     '推导所载：a ↔ b 的任两个见证相等，由 a 推出 b 的任两个推导亦然，所以这一等同不丢失见证；在类型之间会丢失，因为 Bool 有两个不同的自逆映射，恒等与否定。',
     [P + 'iff_witness_unique', P + 'derivation_unique', P + 'flip', P + 'two_equivalences']),
    ('What is lost is the course: transport along any equation of propositions with a constant motive keeps the value, '
     'and along rfl it is the identity by computation. That along propext it does not reduce is a kernel observation '
     '(Lean 4.29.1), not a theorem.',
     '失去的是进程：沿命题之间任一等式、以常值动机的输运保值，沿 rfl 由计算即为恒等。沿 propext 它不归约，是内核的观察（Lean 4.29.1），不是定理。',
     [P + 'transport_const', P + 'transport_refl']),
]
for en, zh, _ in laws:
    assert len(en) <= 420 and len(zh) <= 190, (en[:40], len(en), len(zh))
all_named = {n for _, _, names in laws for n in resolve(MOD, names)}
missing = sorted(d['name'] for d in m['declarations'] if d['name'] not in all_named)
assert not missing, ('declarations no law names', missing)

LUMP_DEP = dep('generalization-through-lumping', 'formal-reuse',
               'States propext through Becoming.Learning\'s Lumped: the lumping is the interderivation, forgetting which '
               'end is read.',
               '经 Becoming.Learning 的 Lumped 陈述 propext：归并即互推，忘掉读的是哪一端。',
               'What a reading goes alike across: Lumped.', '读法在其上相同的：Lumped。',
               'A reading of propositions through the two ends of an interderivation.', '经一个互推两端的命题读法。',
               'None.', '无。', src('Learning'))
STUCK = f'{KIT}/stuck/StuckTransport.lean'
STUCK_LOG = f'{KIT}/stuck/stuck.log'

rec = {
    'schema_version': 2, 'id': RID,
    'title': {'en': 'What identifying interderivable propositions keeps and loses (propext)',
              'zh': '等同可互推的命题保留什么、失去什么（propext）'},
    'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F11', 'reviewed_at_utc': NOW,
    'statement': {
        'en': 'propext holds exactly where every reading of propositions is lumped by interderivability, and exactly '
              'where the reading by name is; readings built from relations need no axiom. The identification forgets '
              'no witness and keeps every outcome; what it stops is the course.',
        'zh': 'propext 恰在命题的每个读法都按可互推归并之处成立，也恰在按名的读法如此之处；由关系构成的读法不需公理。这一等同不丢失见证、保留每个结果；它停下的是进程。'},
    'laws': [{'en': en, 'zh': zh, 'declarations': resolve(MOD, names)} for en, zh, names in laws],
    'hypotheses': [{
        'en': 'No axiom. propext appears only as a proposition (Extensional), a hypothesis or the other side of an iff, '
              'never as a conclusion or as the axiom. The kernel observation uses the axiom propext on purpose and is '
              'not part of the core.',
        'zh': '不用公理。propext 只作为命题（Extensional）出现，是假设或等价的另一边，从不是结论或公理本身。内核观察有意用到公理 propext，不属于核心。'}],
    'does_not_show': [
        {'en': 'That every reading of a proposition is relational: that is propext itself, stated here as Extensional '
               'and never proved. That Lean without the axiom cannot prove it is known metatheory, not checked here.',
         'zh': '命题的每个读法都是关系的：这就是 propext 本身，在此陈述为 Extensional，从未被证明。没有该公理的 Lean 证不出它，是已知的元理论，此处未检查。',
         'kind': 'non-implication'},
        {'en': 'That transport along propext never reduces: the record checks one closed value with Lean 4.29.1 '
               '(#reduce stops, rfl and decide fail); it is a kernel observation, not a theorem about every term.',
         'zh': '沿 propext 的输运从不归约：本记录以 Lean 4.29.1 检查一个闭值（#reduce 停下，rfl 与 decide 失败）；这是内核观察，不是关于每个项的定理。',
         'kind': 'scope'},
        {'en': 'Formulas are one presentation of readings built from relations; that every relational reading of '
               'interest is a formula of this syntax is a correspondence, not a result.',
         'zh': '公式是由关系构成的读法的一种呈现；每个所关心的关系读法都是这一语法的公式，是对应，不是结果。',
         'kind': 'correspondence'},
        {'en': 'Nothing about function extensionality or quotient soundness, which the core also excludes.',
         'zh': '不涉及函数外延性或商的可靠性，核心同样不用它们。', 'kind': 'scope'}],
    'counterexamples': [{'path': src(MOD), 'detail': {
        'en': 'Between types an equivalence carries content: Bool has two different self-inverse maps '
              '(two_equivalences), so the analogous identification of equivalent types would forget which one, as '
              'propext does not for propositions (iff_witness_unique).',
        'zh': '在类型之间，等价载有内容：Bool 有两个不同的自逆映射（two_equivalences），所以对等价类型作类似的等同会忘掉是哪一个，而 propext 对命题不会（iff_witness_unique）。'}}],
    'standard_boundaries': BOUNDS,
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {n_decl} declarations of '
              f'Becoming.{MOD}, {n_thm} of them theorems, have empty axiom reports; the checker verifies core purity. '
              f'The kernel observation is checked with Lean 4.29.1 (the kit\'s stuck/StuckTransport.lean and stuck.log). '
              f'Built and reviewed in one session; author review in study section {N}; not independently reviewed by a person.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.{MOD} 的 {n_decl} 项声明（{n_thm} 项定理）公理报告为空；'
              f'内核观察以 Lean 4.29.1 检查（工具包 stuck/StuckTransport.lean 与 stuck.log）。在一个会话中构建并审查；作者审查见研究第 {N} 节；未经人的独立审查。'},
    'next_delta': {
        'en': 'Whether the periphery\'s uses of propext are all of this kind (an identification of interderivable '
              'propositions in a proof, with no value computed through it), checked use by use; the same account for '
              'function extensionality and quotient soundness; an independent review.',
        'zh': '外围对 propext 的使用是否都属此类（证明中对可互推命题的等同，不经它计算任何值），逐一检查；对函数外延性与商的可靠性作同样的说明；独立审查。'},
    'correspondence': {
        'en': 'Lean\'s propext and proof irrelevance; the extensionality of propositions in Martin-Löf type theory '
              'with univalence restricted to propositions (homotopy type theory\'s propositional univalence), where an '
              'equivalence of mere propositions is a pair of maps and, for types in general, univalence keeps which '
              'equivalence; the loss of canonicity under axioms (a closed term built with an axiom need not reduce to a '
              'canonical form), which cubical type theory recovers by giving the identification a computation. The '
              'delta is the reading in the theory\'s terms: propext as the lumping of every reading by '
              'interderivability, and the core\'s exclusion as keeping courses that compute.',
        'zh': 'Lean 的 propext 与证明无关性；Martin-Löf 类型论中命题的外延性，即只对命题的单值公理（同伦类型论的命题单值性），在那里纯命题之间的等价是一对映射，'
              '而一般类型的单值性保留是哪一个等价；公理下规范性的丧失（含公理的闭项不必归约为规范形式），立方类型论给这一等同以计算而恢复它。'
              '增量是以本理论的语言所作的读法：propext 是按可互推对每个读法的归并，核心之不用它是保留可计算的进程。'},
    'canonical_source': src(MOD),
    'aliases': ['propext', 'propositional extensionality', '命题外延性', 'proposition identity', '命题的等同',
                'why the core excludes propext', 'interderivability', '可互推',
                'Becoming.PropositionIdentity.extensional_iff_lumped', 'Becoming.PropositionIdentity.byName_lumped_iff',
                'Becoming.PropositionIdentity.Formula.eval_congr', 'Becoming.PropositionIdentity.transport_const'],
    'dependencies': [LUMP_DEP],
    'related': [
        {'id': 'generalization-through-lumping', 'detail': {
            'en': 'The lumping propext is: every reading of propositions goes alike across interderivability.',
            'zh': 'propext 所是的归并：命题的每个读法在可互推上相同。'}},
        {'id': 'identity-across-steps', 'detail': {
            'en': 'The parallel, as a reading, not an instance: a renaming keeps every reading defined from the '
                  'relations, so labels carry nothing, but cannot show that the pattern of names carries nothing; here '
                  'readings built from relations respect interderivability, and that the name carries nothing beyond '
                  'them is propext, a hypothesis.',
            'zh': '平行，作为读法而非实例：改名保留由关系定义的每个读法，所以标签不载任何东西，却不能表明名字的模式不载任何东西；'
                  '在此由关系构成的读法尊重可互推，而名字在它们之外不载任何东西就是 propext，是假设。'}}],
    'references': [{'path': src(MOD), 'role': 'proof', 'declarations': sorted(d['name'] for d in m['declarations']),
                    'sha256': sha(src(MOD))},
                   {'path': src('Learning'), 'role': 'proof', 'sha256': sha(src('Learning'))},
                   {'path': RECEIPT, 'role': 'receipt', 'sha256': sha(RECEIPT)},
                   {'path': STUCK, 'role': 'review', 'sha256': sha(STUCK)},
                   {'path': STUCK_LOG, 'role': 'review', 'sha256': sha(STUCK_LOG)},
                   {'path': f'{KIT}/Propext.lean', 'role': 'provenance', 'sha256': sha(f'{KIT}/Propext.lean')},
                   {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
                   {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)}],
    'proof_bindings': [{'source': src(MOD), 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/Becoming.{MOD}',
                        'success_pointer': '/status', 'success_value': 'passed'}],
    'history': [{
        'en': f'20 October 2026: added (PE1), on the question whether propext can be approved as a practical approach or '
              f'explained within the theory; first checked in scratch ({KIT}/Propext.lean, Stuck.lean); study section {N}.',
        'zh': f'2026年10月20日：新增（PE1），针对 propext 能否作为实用做法被认可、或在理论之内被说明的问题；先在草稿中检查（{KIT}/Propext.lean、Stuck.lean）；研究第 {N} 节。'}],
}
assert len(rec['statement']['en']) <= 300, len(rec['statement']['en'])
assert len(rec['validation_scope']['en']) <= 600 and len(rec['validation_scope']['zh']) <= 260, (len(rec['validation_scope']['en']), len(rec['validation_scope']['zh']))
path = RECORDS / f'{RID}.json'
assert not path.exists(), ('record exists', RID)
path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + '\n')
print('written', RID, n_thm, n_decl)

p = RECORDS / 'generalization-through-lumping.json'
d = json.loads(p.read_text())
d.setdefault('related', []).append({'id': RID, 'detail': {
    'en': 'propext stated as this lumping: every reading of propositions lumped by interderivability.',
    'zh': '以这一归并陈述的 propext：命题的每个读法按可互推归并。'}})
d['history'].append({
    'en': f'20 October 2026, PE1: propext is stated through Lumped in Becoming.PropositionIdentity (record {RID}, '
          f'study section {N}). The claim is unchanged.',
    'zh': f'2026年10月20日，PE1：propext 经 Lumped 陈述于 Becoming.PropositionIdentity（记录 {RID}，研究第 {N} 节）。论断不变。'})
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('updated', p.name)
