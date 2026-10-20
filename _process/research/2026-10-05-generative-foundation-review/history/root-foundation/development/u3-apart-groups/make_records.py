#!/usr/bin/env python3
"""U3/U4 (19 October 2026): attach the base readings to the records whose laws they read, and re-point the records
citing Hexagrams.lean and Listing.lean: python3 -B make_records.py CORE_RECEIPT SECTION   (from the checkout root)

The receipt is checked against the current bytes of every module cited, and every declaration cited against the
receipt's audited list, before anything is written. SECTION is the study section number U3 lands as."""
import datetime
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path.cwd()
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
RECORDS = ROOT / 'theories/becoming/results/records'
core_id, section = sys.argv[1], sys.argv[2]
core_receipt = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
core = json.loads((ROOT / core_receipt).read_text())
assert core['status'] == 'passed'
MODS = {m['module']: m for m in core['modules']}


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def src(module):
    path = f'{PKG}/Becoming/{module}.lean'
    assert core['source_sha256'][f'Becoming.{module}'] == sha(path), f'receipt does not bind {module}'
    assert not any(MODS[f'Becoming.{module}']['axiom_dependencies'].values()), module
    return path


def decls(module, *names):
    have = {d['name'] for d in MODS[f'Becoming.{module}']['declarations']}
    out = ['Becoming.' + n for n in names]
    missing = [n for n in out if n not in have]
    assert not missing, missing
    return out


def count(module):
    ds = MODS[f'Becoming.{module}']['declarations']
    return len(ds), sum(1 for d in ds if d.get('kind') == 'theorem')


def binding(path, module):
    return {'source': path, 'receipt': core_receipt, 'sha256_pointer': f'/source_sha256/Becoming.{module}',
            'success_pointer': '/status', 'success_value': 'passed'}


def add_proof(r, module, names):
    """Add a proof reference for a new module, with the receipt and its binding."""
    path = src(module)
    assert not any(ref['path'] == path for ref in r['references'])
    r['references'].append({'path': path, 'role': 'proof', 'sha256': sha(path), 'declarations': names})
    if not any(ref['path'] == core_receipt for ref in r['references']):
        r['references'].append({'path': core_receipt, 'role': 'receipt', 'sha256': sha(core_receipt),
                                'declarations': []})
    r['proof_bindings'].append(binding(path, module))


def repoint(r, module, extra=()):
    """Re-point an existing proof reference to the module's current bytes and receipt."""
    path = src(module)
    refs = [ref for ref in r['references'] if ref['path'] == path]
    assert len(refs) == 1, (r['id'], module, len(refs))
    refs[0]['sha256'] = sha(path)
    for name in extra:
        if name not in refs[0]['declarations']:
            refs[0]['declarations'].append(name)
    bound = [b for b in r['proof_bindings'] if b['source'] == path]
    assert bound, (r['id'], module)
    for b in bound:
        b['receipt'] = core_receipt
    if not any(ref['path'] == core_receipt for ref in r['references']):
        r['references'].append({'path': core_receipt, 'role': 'receipt', 'sha256': sha(core_receipt),
                                'declarations': []})


def alias(r, *names):
    for a in names:
        if a not in r['aliases']:
            r['aliases'].append(a)


def load(i):
    return json.loads((RECORDS / f'{i}.json').read_text())


def save(r):
    (RECORDS / f"{r['id']}.json").write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print(r['id'])


ff_n, ff_t = count('FrontierFrames')
fw_n, fw_t = count('FrontierWorlds')

# The practical commitments: J1–J4 in the core, read on frames and worlds (U4).
r = load('practical-judgment-g0-j')
r['reviewed_at_utc'] = NOW
add_proof(r, 'FrontierFrames', decls(
    'FrontierFrames', 'FrontierFrames.Priority', 'FrontierFrames.Options', 'FrontierFrames.basicPriority_iff_priority',
    'FrontierFrames.Priority.anchor', 'FrontierFrames.Priority.no_trade', 'FrontierFrames.Priority.comparison',
    'FrontierFrames.excluded', 'FrontierFrames.Priority.choice_exists', 'FrontierFrames.choice_exists_iff_weakly',
    'FrontierFrames.performed', 'FrontierFrames.means', 'FrontierFrames.nothing_required',
    'FrontierFrames.Priority.kept_unrefuted', 'FrontierFrames.Priority.kept_required'))
add_proof(r, 'FrontierWorlds', decls(
    'FrontierWorlds', 'FrontierWorlds.Served', 'FrontierWorlds.Served.successor', 'FrontierWorlds.served_of_handover',
    'FrontierWorlds.Served.not_of_gap'))
alias(r, 'J1–J4 in the core', '实践承诺在核心中', 'Becoming.FrontierFrames.Priority',
      'Becoming.FrontierFrames.choice_exists_iff_weakly', 'Becoming.FrontierFrames.Priority.kept_required')
r['progress'].append({
    'en': 'J1–J4 in the pure core: Becoming.Lexical states J1/J2 as the condition BasicPriority and Becoming.Frontier '
          'states J3/J4, every PracticalJudgment declaration with a core counterpart and an empty axiom report; '
          'FrontierFrames reads them on a frame, the options of a configuration being what one move reaches, and '
          'FrontierWorlds reads service across a handover in a world. The one classical step of PracticalJudgment '
          '(finite_frontier) is weak excluded middle, now a hypothesis calibrated on frames (choice_exists_iff_weakly).',
    'zh': 'J1–J4 在纯核心中：Becoming.Lexical 把 J1/J2 陈述为条件 BasicPriority，Becoming.Frontier 陈述 J3/J4，'
          'PracticalJudgment 的每项声明在核心中都有对应，公理报告为空；FrontierFrames 在框架上读它们（一个构形的选项是一步移动所达），'
          'FrontierWorlds 在世界中读跨交接的服务。PracticalJudgment 唯一的经典步骤（finite_frontier）是弱排中律，'
          '现为假设，并在框架上校准（choice_exists_iff_weakly）。',
    'source': f'_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#{section}-theorems-apart-from-the-base-largest-groups-first-the-practical-commitments-in-the-core-u3-u4'})
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
if not any(ref['path'] == STUDY for ref in r['references']):
    r['references'].append({'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY), 'declarations': []})
r['validation_scope'] = {
    'en': 'Independent completion review accepted the explicit-commitment scope; the 30 theorems of the original '
          f'package concern its form, not normative warrant. Since 19 October 2026 (receipt {core_id}) J1–J4 are '
          f'stated in the pure core (Lexical, Frontier) and read on frames and worlds (FrontierFrames, {ff_t} '
          f'theorems; FrontierWorlds, {fw_t}), all with empty axiom reports; choice_exists_iff_weakly calibrates the '
          'choice at every step as weak excluded middle. Timely continuation is interpretive application. The '
          'commitments stay argued, not proved.',
    'zh': '既有独立完成审查接受明确承诺的一般原则范围；原形式包的 30 项定理关乎形式，不是规范根据。'
          f'2026年10月19日起（回执 {core_id}），J1–J4 在纯核心中陈述（Lexical、Frontier），并在框架与世界上读出'
          f'（FrontierFrames {ff_t} 项定理，FrontierWorlds {fw_t} 项），公理报告皆空；choice_exists_iff_weakly '
          '把每一步有被选者校准为弱排中律。及时接续部分是解释性应用。承诺仍是论证的，不是证明的。'}
assert len(r['validation_scope']['en']) <= 600 and len(r['validation_scope']['zh']) <= 260, (
    len(r['validation_scope']['en']), len(r['validation_scope']['zh']))
r['history'].append({
    'en': f'19 October 2026, U4 (study section {section}): J1–J4 recorded as stated in the pure core (Lexical, Frontier, '
          'since F3J) and read on frames and worlds (FrontierFrames, FrontierWorlds); the choice at a step calibrated '
          'as weak excluded middle; the validation scope restated to say so. The statement and the warrant of the '
          'commitments are unchanged.',
    'zh': f'2026年10月19日，U4（研究第 {section} 节）：记明 J1–J4 已在纯核心中陈述（Lexical、Frontier，自 F3J 起），'
          '并在框架与世界上读出（FrontierFrames、FrontierWorlds）；一步中的选择校准为弱排中律；验证范围据此重述。陈述与承诺的根据不变。'})
save(r)

# Fresh contents under every classification, on a frame of two kinds.
r = load('classification-robust-generative-comparison')
add_proof(r, 'FrontierFrames', decls(
    'FrontierFrames', 'FrontierFrames.classifiedOn', 'FrontierFrames.classifiedOn_none_iff',
    'FrontierFrames.classifiedOn_robust_iff_of_decided', 'FrontierFrames.classifiedOn_robust_iff_of_em',
    'FrontierFrames.classifiedOn_extremes_iff_of_decided', 'FrontierFrames.classifiedOn_required'))
r['history'].append({
    'en': f'19 October 2026, U3 (study section {section}): the core laws of comparison under every classification read '
          'on a frame of two kinds, old contents compared by tier and fresh contents classified '
          '(Becoming.FrontierFrames.classifiedOn_*). The claim is unchanged.',
    'zh': f'2026年10月19日，U3（研究第 {section} 节）：每种分类下比较的核心规律在两类内容的框架上读出（旧内容按层比较，新内容被分类；'
          'Becoming.FrontierFrames.classifiedOn_*）。论断不变。'})
save(r)

# Codes of a frame's branching tests and its joint relation.
r = load('multivalued-joining-common-structure')
add_proof(r, 'PresentationFrames', decls(
    'PresentationFrames', 'PresentationFrames.correspondence', 'PresentationFrames.canonical_kernel',
    'PresentationFrames.canonical_factor', 'PresentationFrames.joint_descends_iff', 'PresentationFrames.joint_image_iff',
    'PresentationFrames.joint_reading_unique', 'PresentationFrames.joint_blocked'))
r['history'].append({
    'en': f'19 October 2026, U3 (study section {section}): the presentation laws this record cites read on a frame '
          '(Becoming.PresentationFrames): exact reduced codes of a frame\'s branching tests correspond one to one, factor '
          'through the canonical one, and the joint relation of a joint frame descends to them exactly where saturated. '
          'The claim is unchanged.',
    'zh': f'2026年10月19日，U3（研究第 {section} 节）：本记录所引的呈现规律在框架上读出（Becoming.PresentationFrames）：'
          '框架分支检验的精确约简代码一一对应、经典范代码分解，联合框架的联合关系恰在饱和时下降到代码。论断不变。'})
save(r)

# The received pairing through the law of waxing and waning.
r = load('hexagrams-on-the-spine')
hx_n, hx_t = count('Hexagrams')
law = r['laws'][1]
assert law['declarations'][-1] == 'Becoming.Hexagram.order_paired'
law['declarations'] += decls('Hexagrams', 'Hexagram.order_paired_by_law')
assert law['en'].endswith('the first changed in every line.')
law['en'] = law['en'][:-1] + ', which is six steps along the law of waxing and waning.'
law['zh'] = law['zh'][:-1] + '；六爻皆变即消息之律走六步。'
repoint(r, 'Hexagrams', decls('Hexagrams', 'Hexagram.order_paired_by_law'))
for ref in r['references']:
    if ref['path'].endswith('Hexagrams.lean'):
        ref['declarations'].sort()
old = r['validation_scope']['en']
assert 'the 97 declarations of Becoming.Hexagrams, 71 of them theorems' in old
r['validation_scope']['en'] = old.replace('receipt 20261019T060745.666273Z', f'receipt {core_id}').replace(
    'the 97 declarations of Becoming.Hexagrams, 71 of them theorems', f'the {hx_n} declarations of Becoming.Hexagrams, '
    f'{hx_t} of them theorems')
r['validation_scope']['zh'] = r['validation_scope']['zh'].replace('20261019T060745.666273Z', core_id).replace(
    '97 项声明（71 项定理）', f'{hx_n} 项声明（{hx_t} 项定理）')
alias(r, 'Becoming.Hexagram.order_paired_by_law')
r['history'].append({
    'en': f'19 October 2026, U3 (study section {section}): law 2 gains order_paired_by_law, the received pairing read '
          'through the law (changing every line is six steps of waxing and waning, 非覆即變 with 變 as six steps of 消息); '
          'revisits_within_order now goes through order_length, its statement unchanged. The other laws are unchanged.',
    'zh': f'2026年10月19日，U3（研究第 {section} 节）：规律 2 新增 order_paired_by_law，所传之对经律读出（六爻皆变即消息六步，'
          '非覆即變之變读作消息六步）；revisits_within_order 改经 order_length 证明，陈述不变。其他规律不变。'})
save(r)

# What takes part in a step, counted.
present = decls('Listing', 'Flow.present_listsOnce_iff', 'Flow.present_numbers_iff', 'Flow.present_number_unique',
                'Flow.present_number_le', 'Flow.present_listsOnce_length', 'Flow.present_of_listsOnce',
                'Flow.present_numbers_iff_by_eq', 'Flow.present_repeated', 'Flow.present_listsOnce_all_iff')
li_n, li_t = count('Listing')
r = load('listing-once-is-decided-identity')
r['reviewed_at_utc'] = NOW
repoint(r, 'Listing', present)
r['claim']['en'] += (' Read on a flow\'s steps, what takes part in a step can be listed once, and has a number, exactly '
                     'where identity among it is decided (Flow.present_listsOnce_iff, Flow.present_numbers_iff); a step '
                     'listing one relatum twice numbers one relatum in two places (Flow.present_repeated); and every '
                     'flow on a type lists each step once exactly where identity on the type is decided '
                     '(Flow.present_listsOnce_all_iff).')
r['claim']['zh'] += ('读在流的步上：参与一步者恰在其间同一已定时能列出一次并有数目（Flow.present_listsOnce_iff、'
                     'Flow.present_numbers_iff）；一步把同一关系项列两次，则在两处只数得一个关系项（Flow.present_repeated）；'
                     '一个类型上的每个流都把每一步列出一次，恰当该类型上的同一已定（Flow.present_listsOnce_all_iff）。')
r['validation_scope']['en'] += (f' Current receipt {core_id}: Becoming.Listing has {li_n} declarations, {li_t} '
                                'theorems, all with empty axiom reports, the Flow.present_* section among them.')
r['validation_scope']['zh'] += (f'当前回执 {core_id}：Becoming.Listing 有 {li_n} 项声明、{li_t} 项定理，公理报告全为空，'
                                '含 Flow.present_* 一节。')
alias(r, *present[:2], 'what takes part in a step, counted', '参与一步者计数')
r['history'].append({
    'en': f'19 October 2026, U3 (study section {section}): Listing.lean gained the section "what takes part in a step, '
          'counted", its laws read on a flow\'s steps (Flow.present_*); one sentence added to the claim. The earlier '
          'claim is unchanged.',
    'zh': f'2026年10月19日，U3（研究第 {section} 节）：Listing.lean 新增“参与一步者计数”一节，其规律在流的步上读出'
          '（Flow.present_*）；论断添一句。原论断不变。'})
save(r)

r = load('relata-counted-up-to-indiscernibility')
repoint(r, 'Listing')
r['history'].append({
    'en': f'19 October 2026, U3 (study section {section}): Listing.lean re-pointed after reading the change (a new '
          'section reads its laws on a flow\'s steps, Flow.present_*; listsOnce_all_iff is read on flows by '
          'Flow.present_listsOnce_all_iff); the declarations this record cites are unchanged, and its binding moves to '
          f'core receipt {core_id}. The claim is unchanged.',
    'zh': f'2026年10月19日，U3（研究第 {section} 节）：读过改动后，Listing.lean 重新指向（新一节在流的步上读其规律，Flow.present_*；'
          f'listsOnce_all_iff 由 Flow.present_listsOnce_all_iff 在流上读出）；本记录所引声明不变，绑定移到核心回执 {core_id}。论断不变。'})
save(r)
print('written')
