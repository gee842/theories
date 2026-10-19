#!/usr/bin/env python3
"""Y3's follow-up after SG (19 October 2026): the text where Becoming.HexagramLaws now cites SG's Becoming.Commuting
(cite_commuting.py applied, checker and connectivity run). usage (from the checkout's root):
  python3 -B follow_up_text.py RECEIPT MAIN CONNECTIVITY_LOG CHECKER_LOG
Edits study section 198 (its summary block, the symmetries bullet, what is not done, and a paragraph on the
follow-up), the chapter on the 易传 (the symmetries bullet and the theorem count), the canonical chapter (the 8.2
integration row, the section 9 receipt and counts), the register entry of the chapter on the 易传, and the next delta
of SG's record what-a-commuting-law-keeps-apart with a related link and a history note. Each edit must match once.
Run before make_record.py --follow-up and rehash_refs.py --follow-up."""
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[6]
R, MAIN, CONN, CHECK = sys.argv[1], sys.argv[2], Path(sys.argv[3]), Path(sys.argv[4])
RF = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation'
STUDY = RF / 'BECOMING-RENEWAL-READING.md'
CANON = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
CHAPTER = ROOT / 'theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md'
REGISTER = ROOT / 'theories/becoming/results/data/arguments-m-z.json'
SG_RECORD = ROOT / 'theories/becoming/results/records/what-a-commuting-law-keeps-apart.json'
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SG_ANCHOR = '#199-junctures-what-a-commuting-law-keeps-apart-and-the-third-value-sg'
Y3_ANCHOR = '#198-laws-of-the-hexagram-world-beyond-waxing-and-waning-y3'


def cite(text, edits):
    for old, new in edits:
        assert text.count(old) == 1, ('edit does not match once', old[:100], text.count(old))
        text = text.replace(old, new)
    return text


def number(n):
    return f'{n:,}'


receipt = json.loads((ROOT / PKG / 'becoming-checks' / R / 'verification.json').read_text())
assert receipt['status'] == 'passed'
ms = {m['module']: m for m in receipt['modules']}
core, found = receipt['core_modules'], receipt['foundation_modules']
core_thms = sum(ms[m]['theorems'] for m in core)
found_thms = sum(ms[m]['theorems'] for m in found)
audited = sum(len(ms[m]['declarations']) for m in receipt['spine_modules'])
mod = ms['Becoming.HexagramLaws']
assert not any(mod['axiom_dependencies'].values())
own = {d['name'] for d in mod['declarations']}
assert 'Becoming.Hexagram.orbit_commutes' not in own, 'cite_commuting.py has not been applied'
thms, decls_n = mod['theorems'], len(mod['declarations'])
generated = len(receipt['generated_axiom_dependencies'])
log = CHECK.read_text()
run = json.loads(log[log.index('{'):log.rindex('}') + 1])
assert run['status'] == 'passed'
ran, reused = run['lean_steps_run'], run['lean_steps_reused']
conn_text = CONN.read_text()
conn = json.loads(conn_text[conn_text.index('{'):conn_text.rindex('}') + 1])
classes = conn['classes']
apart = sum(v for k, v in classes.items() if k.startswith('apart'))
total = sum(classes.values())
mod_apart = conn['apart_by_module'].get('Becoming.HexagramLaws', [0])[0]
components = conn['components']['count']
outside = len(conn['components']['theorems_outside_the_main_component'])
both = sum(conn['statements_on_both_by_module'].values())

# Study section 198.
study = STUDY.read_text()
start = study.index('\n## 198. ')
end = study.find('\n## ', start + 5)
end = len(study) if end < 0 else end
block = study[start:end]
block = cite(block, [
    ('           recurrence-without-premise\n', '           recurrence-without-premise, what-a-commuting-law-keeps-apart\n'),
    ('a theorem; the general law of a commuting fixed-point-free symmetry (SG, G2)\n', 'a theorem\n'),
    ('text; run_complement_apart as an instance of G2; the census', 'text; the census'),
    ('and the runs from a configuration and its complement never meet (`run_complement_apart`).',
     'and the runs from a configuration and its complement never meet (`run_complement_apart`), the instance of what a '
     'commuting law keeps apart (`Law.Commutes.apart`, the complement moving every configuration, `complement_moves`).'),
    ("; the general law of a commuting fixed-point-free symmetry, board item SG's G2, of which `run_complement_apart` "
     "is an instance; an independent review.", '; an independent review.'),
])
block = block.rstrip('\n') + f'''

**After SG (follow-up).** SG landed the general law Y3 had proved for 互 alone ([section 199]({SG_ANCHOR})): a law that commutes with a map moving every configuration never brings the runs from a configuration and from its image to one configuration (`Law.Commutes.apart`), and the run from the image is the image of the run (`Law.Commutes.iterate`). Y3's two statements of it are now its instances, statements unchanged: `nuclear_run_act` is `Law.Commutes.iterate` with `nuclear_act`, and `run_complement_apart` is `Law.Commutes.apart` with `nuclear_complement` and SG's `complement_moves`. Y3's own `orbit_commutes`, the iterate proved again for hexagrams, is dropped, and so is `complement_ne`, which said what `complement_moves` says and which nothing used once `run_complement_apart` cites `complement_moves` (the connectivity measure found it standing apart); nothing else used either. The module imports `Becoming.Commuting`: {thms} theorems, {decls_n} declarations, empty axiom reports, core receipt `{R}` on main {MAIN[:9]}; {mod_apart} of the {thms} stand apart, the same roots as before. The record gains the dependency what-a-commuting-law-keeps-apart and its next delta no longer lists the general law; SG's record names 互's instances and keeps groups of symmetries as its next step.
'''
study = study[:start] + block + study[end:]
STUDY.write_text(study)

# The chapter on the 易传.
chapter = CHAPTER.read_text()
chapter = cite(chapter, [
    ('（`nuclear_run_act`）', '（`nuclear_run_act`，经 `Law.Commutes.iterate`）'),
    ('（`run_complement_apart`）', '（`run_complement_apart`，即交换之律所保持之分离 `Law.Commutes.apart` 的一例）'),
    ('没有构形是自身之錯（`complement_ne`）', '錯移动每一构形，没有构形是自身之錯（`complement_moves`）'),
])
chapter, n = re.subn(r'(\[`Becoming\.HexagramLaws`\]\([^)]*\))（\d+ 条定理，无公理）', rf'\1（{thms} 条定理，无公理）', chapter)
assert n == 1
CHAPTER.write_text(chapter)

# The canonical chapter.
canon = CANON.read_text()
COUNTS = re.compile(r'There are \d+ dependency components, with \d+ spine theorems outside the main one; \d+ statements '
                    r'use both families\.')
assert len(COUNTS.findall(canon)) == 1
canon = COUNTS.sub(
    f'Rerun with the Y3 follow-up after SG (receipt {R}), where `Becoming.HexagramLaws` states two of its laws as '
    f'instances of `Law.Commutes.iterate` and `Law.Commutes.apart`, it counts {number(apart)} of {number(total)}, '
    f'{mod_apart} of the {thms} theorems of `Becoming.HexagramLaws` apart with the same roots. There are {components} '
    f'dependency components, with {outside} spine theorems outside the main one; {both} statements use both families.',
    canon)
modules = len(core)
closure = len(receipt['core_closure'])
canon, n = re.subn(r'four layers: \d+ modules counting the root `Becoming`, and \d+ in the core closure',
                   f'four layers: {modules} modules counting the root `Becoming`, and {closure} in the core closure', canon)
assert n == 1
start = canon.index('**The current receipt.**')
end = canon.index('\n', start)
canon = canon[:start] + (
    f'**The current receipt.** The [current receipt](../../../{PKG}/becoming-verification.json) is run `{R}`, frozen in '
    f'[`becoming-checks/{R}/`](../../../{PKG}/becoming-checks/{R}/verification.json). It was checked with Lean 4.29.1 '
    f'on main {MAIN[:9]} with the Y3 follow-up after SG (`Becoming.HexagramLaws` citing `Becoming.Commuting`, '
    f'[study §198](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/'
    f'BECOMING-RENEWAL-READING.md{Y3_ANCHOR})) in the working tree. It passed. Its counts:') + canon[end:]
for pattern, value in (
        (r'\| Core modules \(with the root `Becoming`, 0 theorems\) \| [\d,]+ modules, [\d,]+ theorems \|',
         f'| Core modules (with the root `Becoming`, 0 theorems) | {modules} modules, {number(core_thms)} theorems |'),
        (r'\| Foundation modules \| \d+ modules, [\d,]+ theorems \|',
         f'| Foundation modules | {len(found)} modules, {number(found_thms)} theorems |'),
        (r'\| Core closure \| \d+ modules, [\d,]+ theorems \|',
         f'| Core closure | {closure} modules, {number(core_thms + found_thms)} theorems |'),
        (r'\| Spine \(the core; no bridge since the F3 sweep\) \| [\d,]+ theorems \|',
         f'| Spine (the core; no bridge since the F3 sweep) | {number(core_thms)} theorems |'),
        (r'\| Audited spine declarations \| [\d,]+ \|', f'| Audited spine declarations | {number(audited)} |'),
        (r'\| Modules in the compile order \| \d+ \|', f'| Modules in the compile order | {len(receipt["compile_order"])} |'),
        (r'\| Generated `injEq` lemmas on `propext` \| \d+ in the core closure \|',
         f'| Generated `injEq` lemmas on `propext` | {generated} in the core closure |'),
        (r'That run reused [\d,]+ cached Lean steps from `~/.cache/becoming-lean` and ran \d+\.',
         f'That run reused {number(reused)} cached Lean steps from `~/.cache/becoming-lean` and ran {ran}.')):
    canon, n = re.subn(pattern, value, canon)
    assert n == 1, pattern
CANON.write_text(canon)

# The register entry of the chapter on the 易传: the theorem count and the chapter's hash.
register = json.loads(REGISTER.read_text())
entry = next(e for e in register if e['id'] == 'yi-zhuan-and-becoming')
hex_thms = ms['Becoming.Hexagrams']['theorems'] + ms['Becoming.HexagramPlaces']['theorems'] + thms
for key, pattern in (('scope_zh', r'^\d+ 条 Lean 定理'), ('scope_en', r'^\d+ Lean theorems')):
    entry[key], n = re.subn(pattern, pattern[1:].replace(r'\d+', str(hex_thms)), entry[key])
    assert n == 1, entry[key]
entry['source_sha256'] = hashlib.sha256(CHAPTER.read_bytes()).hexdigest()
REGISTER.write_text(json.dumps(register, ensure_ascii=False, indent=2) + '\n')

# SG's record: 互's instances are stated; groups of symmetries stay its next step.
sg = json.loads(SG_RECORD.read_text())
sg['next_delta'] = {
    'en': cite(sg['next_delta']['en'], [('Groups of symmetries and 互 (Y3, Becoming.HexagramLaws); ',
                                         'Groups of symmetries (the four of 錯 and 綜, which 互 commutes with, in '
                                         'hexagram-world-laws); ')]),
    'zh': cite(sg['next_delta']['zh'], [('对称群与互（Y3，Becoming.HexagramLaws）；',
                                         '对称群（互与之皆交换的錯綜四对称，见 hexagram-world-laws）；')]),
}
assert not any(r['id'] == 'hexagram-world-laws' for r in sg['related'])
sg['related'].append({'id': 'hexagram-world-laws', 'detail': {
    'en': 'The nuclear law 互 is an instance: nuclear_run_act is Law.Commutes.iterate with nuclear_act, and '
          'run_complement_apart is Law.Commutes.apart with nuclear_complement and complement_moves.',
    'zh': '互是一例：nuclear_run_act 是 Law.Commutes.iterate 配 nuclear_act，run_complement_apart 是 Law.Commutes.apart '
          '配 nuclear_complement 与 complement_moves。'}})
sg['history'].append({
    'en': '19 October 2026, Y3 follow-up: Becoming.HexagramLaws states its two laws of 互 under the symmetries as '
          'instances of Law.Commutes.iterate and Law.Commutes.apart (study section 198), so the related record '
          'hexagram-world-laws is named and 互 leaves the next delta; groups of symmetries stay. The claim is unchanged.',
    'zh': '2026年10月19日，Y3 补记：Becoming.HexagramLaws 把互在诸对称下的两条律写作 Law.Commutes.iterate 与 '
          'Law.Commutes.apart 的实例（研究第 198 节），故列出相关记录 hexagram-world-laws，互从下一步中移出；对称群仍是下一步。论断不变。'})
SG_RECORD.write_text(json.dumps(sg, ensure_ascii=False, indent=2) + '\n')
print('follow-up text written:', thms, 'theorems,', decls_n, 'declarations;', mod_apart, 'apart;', apart, 'of', total)
