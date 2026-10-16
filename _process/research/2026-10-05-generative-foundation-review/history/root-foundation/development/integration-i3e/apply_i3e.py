#!/usr/bin/env python3
"""Integration I3e landing kit: python3 -B apply_i3e.py SECTION

Run from the repository root after the core receipt holding the I3e edits of Becoming.Decidedness and
Becoming.Bridge exists and the periphery checker check_organization_correspondence.py has passed against it. It
* checks that the retained core receipt and the retained copy of the periphery receipt passed for the current bytes
  of every module the records bind;
* edits the two records in an inherited module: organizational-formation-from-generative-comparison and
  practical-judgment-g0-j (core, bridge and instance references with their declarations, bindings of each to its
  retained receipt, aliases and history; claims, statements, Ren's words, dependencies and validation scope are
  left as they are, the evidence going in the history entry as in I3a to I3d). A reference the record already holds
  keeps its entry, its declarations merged; where the landed source differs from the hash the record holds, the
  reference takes the hash the core receipt passed for and the history entry says so;
* measures with SPINE-INTEGRATION.py and inserts study section SECTION (s135_zh.md before the English
  summary, s135_en.md at the end), filling receipts and measure.
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
GC = LEAN + 'universal-ethics/generative-capacity/'


def instance(folder, target, stem):
    return (folder + target + '.lean', folder + stem + '-verification.json', folder + 'check_' + stem.replace('-', '_') + '.py',
            target, folder + stem + '-checks/')


INSTANCES = {
    'organization': instance(GC, 'OrganizationCorrespondence', 'organization-correspondence'),
}
# The core and bridge modules the records bind to the retained core receipt.
CORE_MODULES = {'Decidedness', 'Bridge'}
I3 = '2026-10-15，整合 I3e（Ren：“a lot proofs are probably not integrated”）：'
I3_EN = '15 October 2026, integration I3e (Ren: “a lot proofs are probably not integrated”): '
RUN = {}
# What changed in a core or bridge source the record already referenced, for the history entry.
EDITS = {
    'Bridge': ('Bridge.lean（整合 I3e：判断的框架一节加 frontier_iff_undominated、frontier_exists、required_of_bettered；原有陈述不变）',
               'Bridge.lean (integration I3e: frontier_iff_undominated, frontier_exists and required_of_bettered added to '
               'the section on judged frames; earlier statements unchanged)'),
    'Decidedness': ('Decidedness.lean（整合 I3e：加列出之选项中不被胜过者一节；原有陈述不变）',
                    'Decidedness.lean (integration I3e: a section on undominated members of a listed menu added; earlier '
                    'statements unchanged)'),
}


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
    """The retained copy of the landed core receipt and of the periphery receipt, each passed for the current bytes
    of what the records bind."""
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


O = 'Becoming.OrganizationCorrespondence.'
JB = 'Becoming.Judgment.'
UNDOMINATED = ['Becoming.WeaklyDecided', 'Becoming.Decided.weakly', 'Becoming.Undominated', 'Becoming.exists_undominated',
               'Becoming.Undominated.not_not_has', 'Becoming.undominated_has', 'Becoming.bettered_of_undominated_has',
               'Becoming.undominated_has_iff', 'Becoming.exists_undominated_iff_weakly', 'Becoming.undominated_has_iff_em']


def changes(utc):
    return {
        'organizational-formation-from-generative-comparison': {
            'parts': joined(
                core_refs([('Decidedness', UNDOMINATED),
                           ('Bridge', [JB + 'frontier_iff_undominated', JB + 'frontier_exists', JB + 'required_of_bettered'])]),
                instance_refs('organization', [O + n for n in ['frontier_iff_undominated', 'formation_required_by_core',
                                                               'coordination_is_required_by_core']])),
            'aliases': ['Becoming.undominated_has_iff', JB + 'required_of_bettered'],
            'evidence': (f'外围实例模块由其检查器以 Lean 4.30.0-rc2 与 Mathlib 实查（回执 {utc["organization"]}），只用标准公理：'
                         'frontier_iff_undominated 的公理报告为空，formation_required_by_core 与 coordination_is_required_by_core '
                         '以 Lean 的经典判定供给核心所要求者、并用外围的 simp 引理（propext、Classical.choice、Quot.sound）；'
                         f'所实例化的核心律与桥接定理由核心运行审计（回执 {utc["core"]}，公理报告为空）。',
                         f'The periphery instance module is checked by its own checker with Lean 4.30.0-rc2 and Mathlib (receipt '
                         f'{utc["organization"]}), standard axioms only: frontier_iff_undominated has an empty report, and '
                         'formation_required_by_core and coordination_is_required_by_core supply what the core asks by Lean’s '
                         'classical decidedness and use the periphery’s simp lemmas (propext, Classical.choice, Quot.sound); the '
                         f'core laws and bridge theorems it instantiates are audited by the core run (receipt {utc["core"]}, '
                         'empty axiom reports).'),
            'zh': I3 + '在脊柱上陈述（Becoming.Decidedness 的列出之选项中不被胜过者，新增，不加前提；桥接 Judgment.required_of_bettered）。'
                  '一个列出的非空选项表上，比较非自反、传递且在表上弱判定（¬p ∨ ¬¬p，WeaklyDecided；判定者都弱判定，Decided.weakly）时，'
                  '有不被胜过的选项（exists_undominated）；不被胜过者不能缺少每个缺之者都被胜过的性质（Undominated.not_not_has），'
                  '该性质判定时不被胜过者都有它（undominated_has）；比较与性质都判定时，不被胜过者都有它，恰当缺之的每个选项都被表上某选项胜过'
                  '（undominated_has_iff）。在全部关系上，存在之律所需恰是弱排中律（exists_undominated_iff_weakly），'
                  '去掉性质的判定恰是排中律（undominated_has_iff_em）。桥接：在确切列出的选项表上，PracticalJudgment 的前沿即不被胜过者'
                  '（Judgment.frontier_iff_undominated），故比较弱判定、任务判定时，前沿非空且每个成员都完成任务（Judgment.required_of_bettered），'
                  '即 formation_required_of_improvable_absence，不用经典推理。外围实例 OrganizationCorrespondence：以 Lean 的经典判定供给核心所要求者，'
                  'formation_required_of_improvable_absence 由 exists_undominated 与 undominated_has 给出（formation_required_by_core），'
                  '所构造的协调情形亦然（coordination_is_required_by_core）。比较、合格性与所构造的历史保持原范围；规范解释继承公开的 J 承诺。',
            'en': I3_EN + 'stated on the spine (the new laws of Becoming.Decidedness for undominated members of a listed menu, no '
                  'premise; the bridge’s Judgment.required_of_bettered). On a nonempty listed menu where the comparison is '
                  'irreflexive, transitive and weakly decided (¬p ∨ ¬¬p, WeaklyDecided; whatever is decided is weakly decided, '
                  'Decided.weakly), some member is undominated (exists_undominated); an undominated member cannot lack a property '
                  'every member lacking it is bettered in (Undominated.not_not_has), and has it where the property is decided '
                  '(undominated_has); where comparison and property are both decided, every undominated member has the property '
                  'exactly where every member lacking it is bettered by some member (undominated_has_iff). Over all relations, the '
                  'existence law needs exactly weak excluded middle (exists_undominated_iff_weakly), and dropping the decidedness '
                  'of the property is exactly excluded middle (undominated_has_iff_em). Bridge: on an exact listed menu the frontier '
                  'of PracticalJudgment is the undominated members (Judgment.frontier_iff_undominated), so where the comparison is '
                  'weakly decided and the task decided, the frontier is not empty and every member of it performs the task '
                  '(Judgment.required_of_bettered): formation_required_of_improvable_absence with no classical reasoning. '
                  'Periphery instance OrganizationCorrespondence: with Lean’s classical decidedness supplying what the core asks, '
                  'formation_required_of_improvable_absence follows from exists_undominated and undominated_has '
                  '(formation_required_by_core), and so does the constructed coordination case (coordination_is_required_by_core). '
                  'The comparison, eligibility and the constructed history keep their scope; the normative interpretation '
                  'inherits the explicit J commitments.',
        },
        'practical-judgment-g0-j': {
            'parts': core_refs([('Bridge', [JB + n for n in ['frame', 'protecting', 'gaining', 'better_iff_betterAt', 'frontier_iff',
                                                             'frontier_iff_undominated', 'frontier_exists']]),
                                ('Decidedness', ['Becoming.WeaklyDecided', 'Becoming.Undominated', 'Becoming.exists_undominated',
                                                 'Becoming.exists_undominated_iff_weakly'])]),
            'aliases': [JB + 'better_iff_betterAt', JB + 'frontier_exists', 'Becoming.exists_undominated'],
            'evidence': (f'桥接与 Becoming.Decidedness 由核心运行编译与审计（回执 {utc["core"]}），新增声明的公理报告为空；'
                         'PracticalJudgment 作为继承模块随运行编译，其既有回执不变。',
                         f'The bridge and Becoming.Decidedness are compiled and audited by the core run (receipt {utc["core"]}), the '
                         'new declarations with empty axiom reports; PracticalJudgment compiles in the run as an inherited module, '
                         'its earlier receipt unchanged.'),
            'zh': I3 + '在脊柱上陈述（桥接中的确切实例；只改引用、别名与历史）。每个保护优先的比较 PracticalJudgment.Better 都是其选项框架上的 '
                  'BetterAt，前沿亦同（Judgment.better_iff_betterAt、Judgment.frontier_iff，I3d）。在确切列出的选项表上，前沿即核心的不被胜过者'
                  '（Judgment.frontier_iff_undominated）；比较非自反、传递且弱判定时前沿非空（Judgment.frontier_exists，由 '
                  'Becoming.exists_undominated），即 PracticalJudgment.finite_frontier 不用经典推理；在全部关系上，这恰需弱排中律'
                  '（exists_undominated_iff_weakly）。论断、Ren 的话与 G0 的折叠不变：BetterAt 陈述 J1/J2，即核心之外的公开承诺，这里不用也不断言 G0；'
                  'Robust 即核心的 CommonResponse（既有）；以需求为指标的覆盖（Covered）在脊柱上没有确切的对应，留在外围（同 I3d）。',
            'en': I3_EN + 'stated on the spine (exact instances in the bridge; only references, aliases and history change). Every '
                  'protection-first comparison PracticalJudgment.Better is BetterAt on the frame of its options, with the same '
                  'frontier (Judgment.better_iff_betterAt, Judgment.frontier_iff, I3d). On an exact listed menu the frontier is the '
                  'core’s undominated members (Judgment.frontier_iff_undominated), and it is not empty where the comparison is '
                  'irreflexive, transitive and weakly decided (Judgment.frontier_exists, by Becoming.exists_undominated): '
                  'PracticalJudgment.finite_frontier with no classical reasoning; over all relations this needs exactly weak '
                  'excluded middle (exists_undominated_iff_weakly). The claims, Ren’s words and the fold of G0 are unchanged: '
                  'BetterAt states J1/J2, disclosed commitments outside the core, and G0 is neither used nor asserted here; Robust '
                  'is the core’s CommonResponse (as before); demand-indexed coverage (Covered) has no exact counterpart on the '
                  'spine and stays in the periphery (as in I3d).',
        },
    }


def apply_records(utc):
    """Records keep their validation scope (schema-1 records may not grow it); the evidence of this integration goes
    in the history entry, as in I3a to I3d."""
    for rid, change in changes(utc).items():
        path = RECORDS / (rid + '.json')
        d = json.loads(path.read_text())
        have = {r['path'] for r in d['references']}
        refs, bindings = change['parts']
        rehashed = []
        for r in refs:
            if r['path'] in have:  # one reference per path, its declarations merged
                old = next(x for x in d['references'] if x['path'] == r['path'])
                if old['sha256'] != r['sha256']:
                    # Only a core or bridge source the core receipt passed for (receipts()) is rehashed, its change
                    # being this integration's, read and stated in the history entry.
                    module = Path(r['path']).stem
                    assert r['path'] == B + module + '.lean' and module in EDITS, (rid, r['path'])
                    old['sha256'] = r['sha256']
                    rehashed.append(module)
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
        zh, en = change['evidence']
        if rehashed:
            zh += '已引用的源随本次整合改哈希：' + '；'.join(EDITS[m][0] for m in rehashed) + '。'
            en += ' Sources already referenced take the hash of this integration: ' + '; '.join(EDITS[m][1] for m in rehashed) + '.'
        d['history'].append({'zh': change['zh'] + zh, 'en': change['en'] + ' ' + en})
        path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
        print(rid, len(refs), 'references,', len(change['aliases']), 'aliases', ('rehashed ' + ', '.join(rehashed)) if rehashed else '')


def measure():
    out = subprocess.run([sys.executable, '-B', str(STUDY_DIR / 'SPINE-INTEGRATION.py')], capture_output=True,
                         text=True, check=True).stdout
    return json.loads(out)


def insert_study(section, utc, before, m):
    records, was = m['records'], before['records']
    stated, inherited = records.get('stated on the spine', 0), records.get('in an inherited module', 0)
    stated0, inherited0 = was.get('stated on the spine', 0), was.get('in an inherited module', 0)
    fill = {'{CORE}': utc['core'], '{ORG}': utc['organization'], '{STATED}': f'{stated0} → {stated}',
            '{INHERITED}': f'{inherited0} → {inherited}', '{OUTSIDE}': str(records.get('outside the spine run', 0)),
            '{NOLEAN}': str(records.get('no Lean proof', 0)),
            '{CITING}': f'{before["records_citing_a_spine_proof"]} → {m["records_citing_a_spine_proof"]}',
            '{STATED_SHORT}': f'from {stated0} to {stated}', '{INHERITED_SHORT}': f'from {inherited0} to {inherited}'}
    zh, en = (KIT / 's135_zh.md').read_text(), (KIT / 's135_en.md').read_text()
    for key, value in fill.items():
        zh, en = zh.replace(key, value), en.replace(key, value)
    zh = zh.replace('## 135.', f'## {section}.', 1)
    en = en.replace('section 135', f'section {section}', 1)
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
    before = measure()
    apply_records(utc)
    m = measure()
    print(json.dumps({k: m[k] for k in ('records', 'records_citing_a_spine_proof', 'records_in_an_inherited_module')},
                     ensure_ascii=False))
    insert_study(section, utc, before, m)


if __name__ == '__main__':
    main()
