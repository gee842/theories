#!/usr/bin/env python3
"""Integration I3c landing kit: python3 -B apply_i3c.py SECTION

Run from the repository root after the core receipt holding Becoming.Keeping exists and the three
periphery checkers (check_shared_stock_instances.py, check_continuation_correspondence.py,
check_transmission_correspondence.py) have passed against it. It
* checks that the retained core receipt and the retained copies of the three periphery receipts passed for the
  current bytes of every module the records bind;
* edits the four records: draws-on-a-shared-stock, finite-continuation-plans, joint-plan-composition
  and learned-procedure-transmission (core and instance references with their declarations, bindings of each to
  its retained receipt, aliases, dependencies, the choice boundary, laws and history; validation scope is left as
  it is, the evidence going in the history entry as in I3a and I3b);
* measures with SPINE-INTEGRATION.py and inserts study section SECTION (s129_zh.md before the English
  summary, s129_en.md at the end), filling receipts and measure.
Then run `make research-render` and `make research-check`.
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path.cwd()
KIT = Path(__file__).resolve().parent
STUDY_DIR = KIT.parents[1]
STUDY = STUDY_DIR / 'BECOMING-RENEWAL-READING.md'
RECORDS = ROOT / 'theories/becoming/results/records'
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
B = LEAN + 'becoming/Becoming/'
CORE_RECEIPT = LEAN + 'becoming/becoming-verification.json'
MA = 'experiments/market-generativity/meta-attractor/'
AN = LEAN + 'systems-complexity/analysis/'
EC = LEAN + 'universal-ethics/evolution-connectionism/'
INSTANCES = {
    'shared': (MA + 'SharedStockInstances.lean', MA + 'shared-stock-instances-verification.json',
               MA + 'check_shared_stock_instances.py', 'SharedStockInstances', MA + 'shared-stock-instances-checks/'),
    'continuation': (AN + 'ContinuationCorrespondence.lean', AN + 'continuation-correspondence-verification.json',
                     AN + 'check_continuation_correspondence.py', 'ContinuationCorrespondence',
                     AN + 'continuation-correspondence-checks/'),
    'transmission': (EC + 'TransmissionCorrespondence.lean', EC + 'transmission-correspondence-verification.json',
                     EC + 'check_transmission_correspondence.py', 'TransmissionCorrespondence',
                     EC + 'transmission-correspondence-checks/'),
}
# The core modules each record binds to the retained core receipt.
CORE_MODULES = {'Weighted', 'Keeping', 'Copying', 'Stock', 'Evolution'}
I3 = '2026-10-15，整合 I3c（Ren：“a lot proofs are probably not integrated”）：'
I3_EN = '15 October 2026, integration I3c (Ren: “a lot proofs are probably not integrated”): '
RUN = {}


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def declared(path, full):
    """Every named declaration occurs in the file as a definition or theorem."""
    text = (ROOT / path).read_text()
    for name in full:
        short = name.split('.')[-1]
        assert re.search(r'^\s*(?:theorem|def|inductive|structure|abbrev)\s+(?:\S+\.)?' + re.escape(short) + r'\b',
                         text, re.M), (path, name)
    return full


def passed_for(receipt, pointer_module, source):
    r = json.loads((ROOT / receipt).read_text())
    assert r['status'] == 'passed', receipt
    assert r['source_sha256'][pointer_module] == sha(source), ('receipt predates the source', receipt, source)
    return r


def receipts():
    """The retained copies of the landed core receipt and of the three periphery receipts, each passed for the
    current bytes of what the records bind."""
    core = json.loads((ROOT / CORE_RECEIPT).read_text())
    RUN['core'] = LEAN + 'becoming/becoming-checks/' + core['utc'] + '/verification.json'
    for module in CORE_MODULES:
        passed_for(RUN['core'], 'Becoming.' + module, B + module + '.lean')
    out = {'core': core['utc']}
    for key, (source, receipt, _, target, folder) in INSTANCES.items():
        top = passed_for(receipt, target, source)
        RUN[key] = folder + top['utc'] + '/verification.json'
        assert sha(RUN[key]) == sha(receipt), ('retained copy differs from the receipt', RUN[key])
        out[key] = top['utc']
    return out


def ref(path, role, decls=()):
    return {'path': path, 'role': role, 'sha256': sha(path), 'declarations': declared(path, list(decls)) if decls else []}


def core_refs(modules):
    """Core module sources with their declarations, the retained core receipt, and a binding of each."""
    refs = [ref(B + module + '.lean', 'proof', decls) for module, decls in modules]
    bindings = [{'source': B + module + '.lean', 'receipt': RUN['core'], 'sha256_pointer': '/source_sha256/Becoming.' + module,
                 'success_pointer': '/status', 'success_value': 'passed'} for module, _ in modules]
    return refs + [ref(RUN['core'], 'receipt')], bindings


def instance_refs(key, decls):
    source, _, checker, target, _ = INSTANCES[key]
    refs = [ref(source, 'proof', decls), ref(RUN[key], 'receipt'), ref(checker, 'provenance')]
    return refs, [{'source': source, 'receipt': RUN[key], 'sha256_pointer': '/source_sha256/' + target,
                   'success_pointer': '/status', 'success_value': 'passed'}]


def joined(*parts):
    refs, bindings = [], []
    for r, b in parts:
        refs += r
        bindings += b
    return refs, bindings


V = 'Becoming.Viability.'
KEEPING_PLANS = [V + n for n in ['Seen', 'Usable', 'KeptFor', 'Plan', 'Plan.Keeps', 'Plan.Keeps.keptFor', 'ChoiceOver',
                                 'choiceOver_fin', 'KeptFor.plan_of_choice', 'keptFor_iff_plan_of_choice',
                                 'keptFor_iff_plan', 'plans_iff_choice', 'KeptFor.mono', 'KeptFor.shorter',
                                 'KeptFor.finer', 'keptFor_of_closed', 'Certificate.keptFor', 'Kernel.keptFor',
                                 'Matching.registration_matters']]
KEEPING_JOINT = [V + n for n in ['Plan', 'Plan.Keeps', 'Plan.zip', 'jointSense', 'Plan.Compatible', 'Plan.zip_keeps',
                                 'Plan.compatible_of_zip_keeps']]
C = 'Becoming.ContinuationCorrespondence.'
T = 'Becoming.TransmissionCorrespondence.'
S = 'SharedStockInstances.'


def changes(utc):
    shared_ev = (f'外围实例模块由其检查器实查（Lean 4.30.0-rc2，回执 {utc["shared"]}），五条声明的公理报告都为空；'
                 f'所实例化的核心律由核心运行审计（回执 {utc["core"]}）。',
                 f'The periphery instance module is checked by its own checker (Lean 4.30.0-rc2, receipt {utc["shared"]}), '
                 f'all five declarations with empty axiom reports; the core law it instantiates is audited by the core run '
                 f'(receipt {utc["core"]}).')
    cont_ev = (f'Becoming.Keeping 由核心运行审计（回执 {utc["core"]}，公理报告为空）；外围实例模块 ContinuationCorrespondence '
               f'由其检查器以 Lean 4.30.0-rc2 与 Mathlib 实查（回执 {utc["continuation"]}）：单一方案的对应与可列举的情形公理报告为空，'
               'Classical.choice 只在 classicalChoice 与 viable_iff_plan_by_core 中，共同方案的几条用 propext 与 Quot.sound。',
               f'Becoming.Keeping is audited by the core run (receipt {utc["core"]}, empty axiom reports); the periphery instance '
               f'module ContinuationCorrespondence is checked by its own checker with Lean 4.30.0-rc2 and Mathlib (receipt '
               f'{utc["continuation"]}): the single-plan correspondence and the listed case have empty axiom reports, '
               'Classical.choice occurs only in classicalChoice and viable_iff_plan_by_core, and the joint-plan declarations '
               'use propext and Quot.sound.')
    trans_ev = (f'外围实例模块由其检查器以 Lean 4.30.0-rc2 与 Mathlib 实查（回执 {utc["transmission"]}）：不提及构造之状态的六条声明'
                '（kitWord、attach、countOf_replicate、use_kitWord、Move、total_replicate）公理报告为空，其余只有 Mathlib 的标准公理'
                f'（propext、Classical.choice、Quot.sound）；所实例化的核心律由核心运行审计（回执 {utc["core"]}）。',
                f'The periphery instance module is checked by its own checker with Lean 4.30.0-rc2 and Mathlib (receipt '
                f'{utc["transmission"]}): the six declarations that mention no state of the construction (kitWord, attach, '
                'countOf_replicate, use_kitWord, Move, total_replicate) have empty axiom reports, the rest Mathlib’s standard '
                f'axioms only (propext, Classical.choice, Quot.sound); the core laws it instantiates are audited by the core run '
                f'(receipt {utc["core"]}).')
    return {
        'draws-on-a-shared-stock': {
            'parts': joined(
                core_refs([('Weighted', ['Becoming.mass', 'Becoming.every_event_within_iff',
                                         'Becoming.entries_within_not_together'])]),
                instance_refs('shared', [S + n for n in ['firstDraws', 'selectedTotal_eq_mass', 'total_eq_mass',
                                                         'every_selection_within_iff_total_within',
                                                         'each_within_alone_not_together']])),
            'aliases': ['Becoming.every_event_within_iff', 'Becoming.entries_within_not_together'],
            'evidence': shared_ev,
            'zh': I3 + '在脊柱上陈述（Becoming.Weighted 的列出论域上的质量律）。前 n 项汲取依后先列出是一个论域（SharedStockInstances.firstDraws），一种选取是其上的事件，汲取是其权重：选取的总和即该事件的质量，总和即全域的质量（selectedTotal_eq_mass、total_eq_mass）。于是每种选取都在存量之内恰当总和在内，即核心的 every_event_within_iff（every_selection_within_iff_total_within）；两项各为二的汲取分别在二之内而合起来不在，全域的质量为四（each_within_alone_not_together，同核心的 entries_within_not_together）。CorrectionDependence 的原证明与回执保持原范围。',
            'en': I3_EN + 'stated on the spine (Becoming.Weighted’s law of masses on a listed domain). The first n draws listed latest first are a domain (SharedStockInstances.firstDraws), a selection is an event on it and the draws are its weighting: the selected total is the selection’s mass and the total the whole domain’s (selectedTotal_eq_mass, total_eq_mass). So every selection fits within the stock exactly when the total does, which is the core’s every_event_within_iff (every_selection_within_iff_total_within), and two draws of two each fit a stock of two but not together, the whole domain’s mass being four (each_within_alone_not_together, as the core’s entries_within_not_together). CorrectionDependence’s proof and receipt keep their scope.',
        },
        'finite-continuation-plans': {
            'parts': joined(
                core_refs([('Keeping', KEEPING_PLANS)]),
                instance_refs('continuation', [C + n for n in ['processOf', 'successor', 'post_eq_seen',
                                                               'viable_iff_keptFor', 'toPlan', 'ofPlan',
                                                               'works_iff_keeps', 'keeps_iff_works',
                                                               'viable_iff_plan_by_core', 'viable_iff_plan_listed']])),
            'aliases': [V + 'keptFor_iff_plan_of_choice', V + 'keptFor_iff_plan', V + 'plans_iff_choice'],
            'counterexample': {'path': B + 'Keeping.lean', 'detail': {
                'zh': '对任意登记，每个被保持之类在每个进程中都有方案，恰是对登记的选择（plans_iff_choice）：外围 viable_iff_plan 的 choose 在一般情形不能去掉；登记可列举时不需要（keptFor_iff_plan）。',
                'en': 'For arbitrary registrations, kept classes having plans in every process is exactly choice over the registrations (plans_iff_choice): the periphery’s choose in viable_iff_plan cannot be dropped in general, and is not needed where registrations are listed (keptFor_iff_plan).'}},
            'evidence': cont_ev,
            'zh': I3 + '在脊柱上陈述（新核心模块 Becoming.Keeping）。一步可用于一个配置类，指它在每个配置处都被容许且可走（Usable）；该步所登记者使类收窄（Seen，登记可列举时即 InquirySufficiency.After）。一类保持 n 步，指守卫遍及该类，且有某个可用之步无论登记什么都留下保持少一步的类（KeptFor）。依所登记者给出后续之步的方案保持该类其长度之久，不加前提（Plan.Keeps.keptFor）；登记可列举时每个被保持之类都有这样的方案，不加前提（keptFor_iff_plan）；对任意登记，这恰是对登记的选择（plans_iff_choice，选择为具名假设 ChoiceOver）。更细的登记保持更粗的登记所保持者（KeptFor.finer）；Viability 的证书在其中有一步处处可用时使其中每类对每个时程都被保持（Certificate.keptFor、Kernel.keptFor）；登记一个隐藏的位可决定保持与否（Matching.registration_matters）。外围实例：ContinuationAdequacy 的 viable 即以到达的配置为登记的 KeptFor（ContinuationCorrespondence.viable_iff_keptFor），方案两向互译（works_iff_keeps、keeps_iff_works），故 viable_iff_plan 由核心律与 Classical.choice 给出（viable_iff_plan_by_core），观察可列举时不用公理（viable_iff_plan_listed）。外围证明及其回执保持原范围。',
            'en': I3_EN + 'stated on the spine (new core module Becoming.Keeping). A move is usable from a class of configurations where it is allowed and enabled at each of them (Usable), and what its step registers narrows the class (Seen, which is InquirySufficiency.After where registrations are listed). A class is kept for n steps where the guard holds throughout and some usable move leaves, whatever is registered, a class kept one step fewer (KeptFor). A plan whose later moves follow what was registered keeps the class for its length, with no premise (Plan.Keeps.keptFor); where registrations are listed every kept class has such a plan, with no premise (keptFor_iff_plan); for arbitrary registrations that is exactly choice over the registrations (plans_iff_choice, choice the named hypothesis ChoiceOver). A finer registration keeps what a coarser one keeps (KeptFor.finer); a certificate of Viability with a move usable throughout keeps every class within it for every horizon (Certificate.keptFor, Kernel.keptFor); registering a hidden bit can decide keeping (Matching.registration_matters). Periphery instance: ContinuationAdequacy’s viable is KeptFor with the configuration reached registered (ContinuationCorrespondence.viable_iff_keptFor), plans translate both ways (works_iff_keeps, keeps_iff_works), so viable_iff_plan follows from the core law with Classical.choice (viable_iff_plan_by_core), and with no axiom for listed observations (viable_iff_plan_listed). The periphery proofs and their receipts keep their scope.',
        },
        'joint-plan-composition': {
            'parts': joined(
                core_refs([('Keeping', KEEPING_JOINT)]),
                instance_refs('continuation', [C + n for n in ['toPlan', 'toPlan_zip', 'compatible_iff',
                                                               'joint_plan_composition_by_core',
                                                               'compatibility_necessary_by_core']])),
            'aliases': [V + 'Plan.zip_keeps', V + 'Plan.compatible_of_zip_keeps'],
            'dependencies': [{'id': 'finite-continuation-plans', 'relation': 'formal-reuse', 'detail': {
                'zh': '复用 Becoming.Keeping 的方案与保持（Plan、Plan.Keeps）及外围的方案互译（ContinuationCorrespondence.toPlan）；共同方案是两部分方案的合成。',
                'en': 'Reuses Becoming.Keeping’s plans and keeping (Plan, Plan.Keeps) and the periphery’s translation of plans (ContinuationCorrespondence.toPlan); a joint plan composes the parts’ plans.'}}],
            'evidence': cont_ev,
            'zh': I3 + '在脊柱上陈述（Becoming.Keeping 的共同方案）。两部分的方案合成一个成对之步的方案，各部分依自己的登记继续（Plan.zip、jointSense）。每个共同之步投影为各部分之步、共同之类落在两部分方案所保持之类之上、成对之步处处可用（Plan.Compatible）时，共同方案保持两个守卫，不加前提（Plan.zip_keeps）；每个保持守卫的共同方案其成对之步都处处可用（Plan.compatible_of_zip_keeps）。投影与共同可用是分开的条件，都不由两部分各自的方案推出。外围实例：JointContinuation 的配对即核心的 Plan.zip（ContinuationCorrespondence.toPlan_zip），递推的共同可施行即 Plan.Compatible（compatible_iff），故 joint_plan_composition 与 compatibility_necessary 由核心律给出（joint_plan_composition_by_core、compatibility_necessary_by_core）；二者提及以两个带指标方案的匹配定义的 zipPlan，编译后用 propext。外围证明及其回执保持原范围。',
            'en': I3_EN + 'stated on the spine (the joint plans of Becoming.Keeping). Two parts’ plans run together as one plan of pairs, each part continuing by its own registration (Plan.zip, jointSense). Where every joint step projects onto a step of each part, the joint class lies over classes the parts’ plans keep and the paired moves are usable throughout (Plan.Compatible), the joint plan keeps both guards, with no premise (Plan.zip_keeps); every joint plan that keeps a guard has its paired moves usable throughout (Plan.compatible_of_zip_keeps). Projection and joint usability are separate conditions, neither following from the parts’ plans. Periphery instance: JointContinuation’s pairing is the core’s Plan.zip (ContinuationCorrespondence.toPlan_zip) and recursive joint executability is Plan.Compatible (compatible_iff), so joint_plan_composition and compatibility_necessary follow from the core laws (joint_plan_composition_by_core, compatibility_necessary_by_core); both mention zipPlan, defined by a match on two indexed plans, which compiles through propext. The periphery proofs and their receipts keep their scope.',
        },
        'learned-procedure-transmission': {
            'parts': joined(
                core_refs([('Copying', ['Becoming.Copying.lineage_all_iff', 'Becoming.Copying.batch']),
                           ('Stock', ['Becoming.Stock.Balanced', 'Becoming.Stock.trace_balance']),
                           ('Evolution', ['Becoming.price', 'Becoming.offspring', 'Becoming.selected'])]),
                instance_refs('transmission', [T + n for n in ['kitWord', 'pool', 'attach', 'lineage_released_iff',
                                                               'reconstruction_builds_longest_lineage', 'Move',
                                                               'process', 'material_balanced', 'support_balanced',
                                                               'course_conserves', 'procedure', 'successors',
                                                               'faithful_selects', 'history_selects']])),
            # Copying.lineage_all_iff and price are aliases of the records that state them; they enter here as
            # dependencies.
            'aliases': ['Becoming.Stock.trace_balance'],
            'dependencies': [
                {'id': 'inherited-structural-copying', 'relation': 'formal-reuse', 'detail': {
                    'zh': '复用 Becoming.Copying.lineage_all_iff：容量即一个共享池与支持所释放的最长谱系（TransmissionCorrespondence.lineage_released_iff）。',
                    'en': 'Reuses Becoming.Copying.lineage_all_iff: the capacity is the longest lineage one shared pool and its support release (TransmissionCorrespondence.lineage_released_iff).'}},
                {'id': 'evolution-on-descent', 'relation': 'formal-reuse', 'detail': {
                    'zh': '复用 Becoming.price 的计数形式：忠实重构不升不降，后继中控制位的总数即各家族之位以其容量加权（TransmissionCorrespondence.faithful_selects）。',
                    'en': 'Reuses the counting form of Becoming.price: faithful reconstruction raises and lowers nothing, so the successors’ total of the procedure bit is the families’ bits weighted by their capacities (TransmissionCorrespondence.faithful_selects).'}}],
            'laws': [
                {'zh': '容量即一个共享池所释放的最长谱系：后继的十三单位前体读作同一种记号的词、所持前体为池、二十单位支持在释放时汲取，n 个后继依次释放恰当 n 在容量之内，故重构恰建成所释放的最长谱系（Copying.lineage_all_iff 的实例）。',
                 'en': 'The capacity is the longest lineage one shared pool releases: reading a successor’s thirteen precursor units as a word of one kind of token, the precursor held as the pool and its twenty support units as drawn at release, n successors are released in turn exactly when n is within the capacity, so a reconstruction builds exactly the longest lineage released (an instance of Copying.lineage_all_iff).',
                 'declarations': [T + 'lineage_released_iff', T + 'reconstruction_builds_longest_lineage']},
                {'zh': '每条由接触与重构组成的路径都保存材料与支持，不只一个循环（Stock.trace_balance 的实例，无汲取无补充）。',
                 'en': 'Every course of exposures and reconstructions conserves material and support, not one cycle only (an instance of Stock.trace_balance with nothing drawn or replenished).',
                 'declarations': [T + 'material_balanced', T + 'support_balanced', T + 'course_conserves']},
                {'zh': '忠实重构不升不降，后继中控制位的总数即各家族之位以其后继数（即容量）加权（Price 方程的计数形式）；历史中三个后继有两个带响应的更新方式，两个亲代中只有一个。',
                 'en': 'Faithful reconstruction raises and lowers nothing, so the successors’ total of the procedure bit is the families’ bits weighted by their successor counts, each its capacity (the counting form of Price’s equation); in the history two of three successors carry the responsive procedure where one of two parents did.',
                 'declarations': [T + 'faithful_selects', T + 'history_selects']},
            ],
            'evidence': trans_ev,
            'zh': I3 + '在脊柱上陈述（Becoming.Copying、Becoming.Stock 与 Becoming.Evolution 的一般律）。外围实例模块 TransmissionCorrespondence：容量即一个共享池所释放的最长谱系（lineage_released_iff、reconstruction_builds_longest_lineage，Copying.lineage_all_iff 的实例）；接触与重构是同一进程的两种步，每步之后材料与支持如前，故任意路径都保存二者（course_conserves，Stock.trace_balance 的实例）；忠实重构不升不降，后继中控制位的总数即各家族之位以其容量加权（faithful_selects，Becoming.price），历史中三个后继有两个带响应的更新方式而两个亲代中只有一个（history_selects）。Price 的形式是恒等式，不是适应度的度量；后继数由各家族实际任务成功所留的支持定出。构造的理想化前提保持不变。',
            'en': I3_EN + 'stated on the spine (the general laws of Becoming.Copying, Becoming.Stock and Becoming.Evolution). Periphery instance module TransmissionCorrespondence: the capacity is the longest lineage one shared pool releases (lineage_released_iff, reconstruction_builds_longest_lineage, instances of Copying.lineage_all_iff); exposures and reconstructions are two kinds of step of one process across which material and support stand as before, so every course conserves both (course_conserves, an instance of Stock.trace_balance); faithful reconstruction raises and lowers nothing, so the successors’ total of the procedure bit is the families’ bits weighted by their capacities (faithful_selects, Becoming.price), and in the history two of three successors carry the responsive procedure where one of two parents did (history_selects). Price’s form is an identity, not a measure of fitness; the counts are set by the support each family’s actual task success left. The construction’s idealized premises are unchanged.',
        },
    }


def apply_records(utc):
    """Records keep their validation scope (schema-1 records may not grow it); the evidence of this integration goes
    in the history entry, as in I3a and I3b."""
    for rid, change in changes(utc).items():
        path = RECORDS / (rid + '.json')
        d = json.loads(path.read_text())
        have = {r['path'] for r in d['references']}
        refs, bindings = change['parts']
        for r in refs:
            if r['path'] in have:  # one reference per path, its declarations merged
                old = next(x for x in d['references'] if x['path'] == r['path'])
                assert old['sha256'] == r['sha256'], (rid, r['path'])
                old['declarations'] = old.get('declarations', []) + [n for n in r['declarations'] if n not in old.get('declarations', [])]
                continue
            d['references'].append(r)
            have.add(r['path'])
        for b in bindings:
            if b not in d['proof_bindings']:
                d['proof_bindings'].append(b)
        for alias in change['aliases']:
            assert alias not in d['aliases'], (rid, alias)
            d['aliases'].append(alias)
        for edge in change.get('dependencies', []):
            assert edge['id'] not in {e['id'] for e in d['dependencies']}, (rid, edge['id'])
            d['dependencies'].append(edge)
        if 'counterexample' in change:
            d['counterexamples'].append(change['counterexample'])
        if 'laws' in change:
            d['laws'].extend(change['laws'])
        zh, en = change['evidence']
        d['history'].append({'zh': change['zh'] + zh, 'en': change['en'] + ' ' + en})
        path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
        print(rid, len(refs), 'references,', len(change['aliases']), 'aliases')


def measure():
    out = subprocess.run([sys.executable, '-B', str(STUDY_DIR / 'SPINE-INTEGRATION.py')], capture_output=True,
                         text=True, check=True).stdout
    return json.loads(out)


def insert_study(section, utc, m):
    records = m['records']
    stated, outside = records.get('stated on the spine', 0), records.get('outside the spine run', 0)
    fill = {'{CORE}': utc['core'], '{SHARED}': utc['shared'], '{CONT}': utc['continuation'],
            '{TRANS}': utc['transmission'], '{STATED}': f'176 → {stated}', '{OUTSIDE}': f'10 → {outside}',
            '{NOLEAN}': str(records.get('no Lean proof', 0)), '{CITING}': f'180 → {m["records_citing_a_spine_proof"]}',
            '{STATED_SHORT}': str(stated), '{OUTSIDE_SHORT}': str(outside)}
    zh, en = (KIT / 's129_zh.md').read_text(), (KIT / 's129_en.md').read_text()
    for key, value in fill.items():
        zh, en = zh.replace(key, value), en.replace(key, value)
    zh = zh.replace('## 129.', f'## {section}.', 1)
    en = en.replace('section 129', f'section {section}', 1)
    assert not re.search(r'\{[A-Z_]+\}', zh + en), 'unfilled placeholder'
    text = STUDY.read_text()
    assert f'\n## {section}. ' not in text, 'section number taken'
    anchor = '\n## English summary\n'
    assert text.count(anchor) == 1
    text = text.replace(anchor, '\n' + zh.rstrip('\n') + '\n' + anchor)
    text = text.rstrip('\n') + '\n\n' + en.rstrip('\n') + '\n'
    STUDY.write_text(text)


def main():
    section = int(sys.argv[1])
    utc = receipts()
    apply_records(utc)
    m = measure()
    print(json.dumps({k: m[k] for k in ('records', 'records_citing_a_spine_proof', 'records_outside_the_spine_run')},
                     ensure_ascii=False))
    insert_study(section, utc, m)


if __name__ == '__main__':
    main()
