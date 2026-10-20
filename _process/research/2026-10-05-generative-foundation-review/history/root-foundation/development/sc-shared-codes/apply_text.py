#!/usr/bin/env python3
"""Apply SC's text to the shared pages of a landing checkout, after the core checker and the connectivity check:
  python3 -B apply_text.py RECEIPT MAIN CONNECTIVITY_LOG CHECKER_LOG
RECEIPT is the core run, MAIN the main commit it ran on, the two logs the outputs of THEOREM-CONNECTIVITY.py --check
and check_becoming.py. Writes the study section and the decision at the next free numbers (the section counting those
other board items have claimed; both printed), the decision's Chinese edition, the canonical chapter's section 4
paragraph with its readings, its section 8.2 row, section 8.3 item and decision count, the integration row's counts and
section 9's receipt and counts, and the Chinese edition's section 4 paragraph and decision count. Each edit must match
exactly once; run on a checkout that has none of them."""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
R, MAIN, CONN, CHECK = sys.argv[1], sys.argv[2], Path(sys.argv[3]), Path(sys.argv[4])
RF = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation'
STUDY = RF / 'BECOMING-RENEWAL-READING.md'
DC, DCZ = RF / 'DELEGATED-CHOICES.md', RF / 'DELEGATED-CHOICES.zh.md'
BOARD = ROOT / '_process/BECOMING-WORKBOARD.md'
CH = ROOT / 'theories/becoming/chapters'
CANON, CANON_ZH = CH / 'THE-THEORY-OF-BECOMING.md', CH / 'THE-THEORY-OF-BECOMING.zh.md'
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
LEAN = f'../../../{PKG}/Becoming/SharedCodes.lean'
MODULE = 'Becoming.SharedCodes'
RID = 'a-code-formed-between-formations'
RECORD = f'[{RID}](../results/records/{RID}.md)'
SECTION_5 = '<a id="5-评价的形成--how-evaluation-forms"></a>'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:100], text.count(old))
    return text.replace(old, new)


def number(n):
    return f'{n:,}'


receipt = json.loads((ROOT / PKG / 'becoming-checks' / R / 'verification.json').read_text())
assert receipt['status'] == 'passed'
ms = {m['module']: m for m in receipt['modules']}
core, found = receipt['core_modules'], receipt['foundation_modules']
core_thms = sum(ms[m]['theorems'] for m in core)
found_thms = sum(ms[m]['theorems'] for m in found)
audited = sum(len(ms[m]['declarations']) for m in receipt['spine_modules'])
mod = ms[MODULE]
assert not any(mod['axiom_dependencies'].values())
thms, decls_n = mod['theorems'], len(mod['declarations'])
generated = len(receipt['generated_axiom_dependencies'])
log = CHECK.read_text()
run = json.loads(log[log.index('{'):log.rindex('}') + 1])
assert run['status'] == 'passed'
ran, reused = run['lean_steps_run'], run['lean_steps_reused']
conn_text = CONN.read_text()
conn = json.loads(conn_text[conn_text.index('{'):conn_text.rindex('}') + 1])
assert not conn['apart_roots_unclassified'] and not conn['register_entries_not_apart_roots']
classes = conn['classes']
apart = sum(v for k, v in classes.items() if k.startswith('apart'))
total = sum(classes.values())
assert conn['apart_by_module'].get(MODULE, [0])[0] == 0, conn['apart_by_module'].get(MODULE)
components = conn['components']['count']
outside = len(conn['components']['theorems_outside_the_main_component'])
both = sum(conn['statements_on_both_by_module'].values())

# The next free numbers: the study section counting what other board items have claimed, the decision after the last.
board = BOARD.read_text()
study = STUDY.read_text()
assert 'A code formed between formations (SC)' not in study
claimed_sections = [int(x) for x in re.findall(r'study §(\d+)', board)]
N = max([int(m.group(1)) for m in re.finditer(r'^## (\d+)\. ', study, re.M)] + claimed_sections) + 1
ANCHOR = f'#{N}-a-code-formed-between-formations-sc'
dc = DC.read_text()
D = max(int(m.group(1)) for m in re.finditer(r'^\| D(\d+) \|', dc, re.M)) + 1
D_ID = f'd{D}-在形成之间形成的编码--a-code-formed-between-formations'
STUDY_LINK = f'../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md{ANCHOR}'

section = (HERE / 'study_sc.txt').read_text().format(
    N=N, R=R, D=D, THMS=thms, DECLS=decls_n, APART=number(apart), TOTAL=number(total),
    COMPONENTS=components, OUTSIDE=outside, BOTH=both)
STUDY.write_text(study.rstrip('\n') + '\n\n' + section)

# The decision, both editions.
WHERE = (f'Where: [Becoming.SharedCodes](../../../../{PKG}/Becoming/SharedCodes.lean); the record '
         f'[{RID}](../../../../theories/becoming/results/records/{RID}.md); the chapter '
         '[CHINESE-SOURCES-AND-BECOMING](../../../../theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md) §8 '
         'and four passages of its map (同则同之, 名无固宜, the 說文\'s 止戈 gloss, 书同文); canonical chapter §4; study '
         f'section {N} ([SC](BECOMING-RENEWAL-READING.md{ANCHOR})). Decided in the one account of D45; continues D54.')
DEC = f'''

<a id="{D_ID}"></a>
### A code formed between formations

{WHERE}

**Decision.** (1) **约定俗成.** 名无固宜，约定俗成谓之宜 is read with the symmetry law (`never_agrees_of_both`): a law privileging neither form nor formation cannot settle a symmetric disagreement, and what settles one breaks a symmetry. A centre does so beforehand (荀子's 王者制名), a preferred form by a fit in the form, an order of hearing through the relation's own history (`three_agree`). 约定俗成 is read as the last: the fit of a name is formed in the course of use, and the form reached is fixed by the start and the order (`run_agrees_every_start_iff`, `run_shared_iff_in_use`). (2) **同则同之.** Renaming forms changes neither what a code tells apart nor whether it carries a law (`run_renamed_tells_apart_iff`, `renamed_carries_iff`): the fit (宜) is conventional, what is carried (实) is not. Agreement formed sense by sense can merge senses a code told apart (`TwoFormations.homonym`), so forming a convention can cost distinctions. (3) **书同文.** An imposed code is a centre's code made everyone's at once: its source loses nothing, every other formation loses what its code told apart and the imposed code merges, and no later exchange among those it was imposed on recovers it; a merged distinction comes back only from a form kept outside (`run_from_imposition`, `outside_needed`, `outside_returns`). “古文由此絕” is read as nothing outside having kept the old forms in use. (4) **止戈 in the 說文.** A reading written into the records later readers learn from rests at once and confirms itself (`written_rests`); later records do not recover what came before (`no_reading_recovers`); only records kept from before, the bone and bronze forms in which 止 is a foot, bar a different resolution (`kept_bars`), and records only added lose a resolution without replacing it (`added_never_replaced`). This is the law beneath D54 (4), which keeps the two layers of 武 apart. (5) **The proposed coupling form.** The gap's statement that codes adopted from the least-indexed coupled formation come to rest alike exactly where every coupling closure is the whole is false (`Path.never_agree`); under a pointer law agreement is the meeting of the pointer's paths (`follow_agrees_iff`). (6) **The theory's own terms.** D54 (5) reads a single-character term as a code formed among the theory's users; these laws say what such a code keeps (agreement through closed hearings, reading across where codes agree) and what it costs (merged senses, distinctions lost to an imposed term). (7) **Not read into it.** The laws do not say whether a shared, an imposed or a kept code supports or damages 生生, nor that actual conventions form by hearing in this way.
**Reasons.** Each reading is argued from the theorems it names, with their exact hypotheses: a rule of adoption reading the two codes, and orders of hearing; no centre, meaning or truth of a form is assumed. The symmetry law is what turns 名无固宜 from a remark about arbitrariness into a statement about what convention needs, and the three witnesses show each way of breaking the symmetry attained. Reading 止戈 as written back keeps the graph's history from being settled by its later uptake, as D54 does, and says which records keep it readable.
**What would change it.** A law of the spine under which a symmetric disagreement settles without breaking a symmetry (which `never_agrees_of_both` excludes for every law it covers); a reading of 约定俗成, argued from the 正名 and its commentaries, under which the fit is fixed by a centre rather than formed in use; evidence that the 說文's gloss did not enter later readings of 武; a model of actual exchange (probabilities over orders, codes with several forms) under which these laws fail.'''
DEC_ZH = f'''

<a id="{D_ID}"></a>
### D{D}. 在形成之间形成的编码

所在：[Becoming.SharedCodes](../../../../{PKG}/Becoming/SharedCodes.lean)；记录 [{RID}](../../../../theories/becoming/results/records/{RID}.md)；[《中国思想的关系本体与生成之论》](../../../../theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md) §8 及其逐句对应中的四段（同则同之、名无固宜、说文止戈之释、书同文）；正典一章 §4；研究第 {N} 节。在 D45 的一个说明中决定；接续 D54。

**决定。** 一、**约定俗成。** 名无固宜，约定俗成谓之宜，以对称之律读之（`never_agrees_of_both`）：既不特许形式、也不特许形成者的律不能解决对称的分歧，解决分歧者打破一个对称。中心事先打破它（荀子之王者制名），偏好之形以形式上的合宜打破它，听取的次序以关系自身的历史打破它（`three_agree`）。约定俗成读作最后一种：名之宜在使用的过程中形成，所成之形由起点与次序固定（`run_agrees_every_start_iff`、`run_shared_iff_in_use`）。二、**同则同之。** 改名既不改变编码所分别者，也不改变它是否承载规律（`run_renamed_tells_apart_iff`、`renamed_carries_iff`）：宜由约定，实不由约定。逐义形成的相合可以合并编码原已分别的义（`TwoFormations.homonym`），所以约定之成可以付出分别。三、**书同文。** 强加的编码是一个中心的编码一举成为众人的：其来源一无所失；其余每个形成失去其编码所分而强加编码所合并者；此后被强加者之间的交换不能恢复；被合并的分别只能从强加之外保留的形式回来（`run_from_imposition`、`outside_needed`、`outside_returns`）。“古文由此絕”读作外面再无人用旧形。四、**说文之止戈。** 写入后人所学之记录的读法即刻静止并自我确认（`written_rests`）；后来的记录读不回此前（`no_reading_recovers`）；只有保留下来的此前记录（止为足的甲骨金文字形）阻止另一种判定（`kept_bars`），只增补的记录使判定失去而不被替换（`added_never_replaced`）。这是 D54（四）把武分两层而读之下的律。五、**原拟的耦合形式。** 缺口所拟“各取其所耦合者中最小编号者之码，恰在每个耦合闭包为全体时静止为同”不成立（`Path.never_agree`）；指针律之下相合是指针之路相遇（`follow_agrees_iff`）。六、**理论自己的术语。** D54（五）把单字术语读作理论使用者之间形成的编码；这些律说明这样的编码保持什么（经封闭的听取而保持的相合，编码相合处的互读），付出什么（被合并的义，被强加术语所失的分别）。七、**不读入的。** 律不说共有的、强加的或保留的编码支持还是损害生生，也不说实际的约定以这种听取方式形成。
**理由。** 每条读法由它所列的定理论证，带着确切的前提：一条读两个编码的采纳规则，以及听取的次序；不假定中心、意义或形式的真。对称之律把名无固宜从关于任意性的一句话变成关于约定需要什么的陈述，三个见证显示打破对称的每一途都可达到。把止戈读作写回，像 D54 一样不让字形之史由其后的采用决定，并说明是哪些记录让它仍可读。
**会改变它的。** 一条脊柱定律，在它之下对称的分歧不打破对称也能解决（`never_agrees_of_both` 对它所涵盖的每条律排除了这一点）；一种由正名篇及其注疏论证的约定俗成之读，在其下宜由中心固定而不是在使用中形成；说文之释未进入后来对武之读的证据；一个实际交换的模型（次序上的概率、一义多形的编码），在其下这些律不成立。'''
ROW = (f'| D{D} | a code formed between formations (19 October) | 约定俗成 as breaking a symmetry by the order of '
       'hearing (a centre and a preferred form the other two ways); 同则同之 what renaming cannot change; 书同文 an '
       'imposed code whose merges return only from outside; the 說文\'s 止戈 a reading written back, barred only by kept '
       'records; the coupling form of the gap false |')
ROW_ZH = (f'| D{D} | 在形成之间形成的编码（10-19） | 约定俗成为以听取次序打破对称（中心与偏好之形为另两途）；同则同之为改名所不能改者；'
          '书同文为强加的编码，其合并只从外面回来；说文之止戈为写回的读法，只为保留的记录所阻；缺口的耦合形式不成立 |')
for path, row, dec in ((DC, ROW, DEC), (DCZ, ROW_ZH, DEC_ZH)):
    text = path.read_text()
    lines = text.split('\n')
    at = [i for i, line in enumerate(lines) if line.startswith(f'| D{D - 1} |')]
    assert len(at) == 1, (path, D - 1)
    lines.insert(at[0] + 1, row)
    text = '\n'.join(lines)
    assert D_ID not in text
    text = text.rstrip('\n') + dec + '\n'
    mark = '<a id="13-一个说明--one-account"></a>'
    head, tail = text.split(mark)
    if path == DC:
        item = (f'- The same request, continued by board item SC (a code formed between formations, RO\'s second gap): '
                f'D{D} ([study section {N}](BECOMING-RENEWAL-READING.md{ANCHOR})).')
    else:
        item = f'- 同一要求，由看板项 SC（在形成之间形成的编码，RO 的第二个缺口）接续：D{D}（研究第 {N} 节）。'
    head = head.rstrip('\n') + '\n' + item + '\n\n'
    path.write_text(head + mark + tail)

# The canonical chapter.
canon = CANON.read_text()
PARA = f'''**A code formed between formations** ([{MODULE}]({LEAN}); record {RECORD}). Let each formation hold a code from senses to forms, changed only by hearing: a hearer takes the form a speaker gives a sense, where a supplied rule reading the two codes says so; hearing is a process of the spine. Hearing makes no form (`run_held`). A group's agreement at a sense is kept exactly through the hearings closed for it (`kept_iff`), and agreement of all is a rest under every rule (`all_agree_rest`). The start and the order of hearing fix the form reached: an order brings every start to agreement exactly where it gives every formation one origin (`run_agrees_every_start_iff`), and any form in use can become the shared one (`run_shared_iff_in_use`). Being joined through couplings is not enough: on a path whose ends each follow the least-indexed of themselves and their couplings, the ends never agree (`Path.never_agree`). A formation reads another's form as the sense meant exactly where their codes agree there (`reads_iff`), and agreement formed sense by sense can merge senses (`TwoFormations.homonym`). No form is privileged (`run_renamed`), and a law privileging neither forms nor formations never brings a symmetric disagreement to agreement (`never_agrees_of_both`): a centre, a preferred form or an order of hearing breaks the symmetry (`TwoFormations.three_agree`). An imposed code makes all agree; each formation loses what its code told apart and the imposed code merges, and only a form kept outside brings it back (`run_from_imposition`, `outside_needed`). A reading written back into the records later generations read rests at once, merges the histories before it and is barred only by records kept from before (`written_rests`, `resolved_alike_merged`, `kept_bars`); where records are only added, a resolution is lost but never replaced (`added_never_replaced`).

*Readings* [AI reading, D{D}]. 名无固宜，约定俗成谓之宜 is read as the third way of breaking the symmetry: the fit of a name formed by the order of use, where 荀子's own 王者制名 is the first, a centre. 同则同之 says what renaming cannot change: what a code tells apart and whether it carries a law. 书同文 is an imposed code, whose merges stay unless a form is kept outside (“古文由此絕”). The 說文's 止戈为武 is a reading written back into its own evidence; only records kept from before, the bone and bronze forms in which 止 is a foot, bar it. None of this says whether a shared, imposed or kept code supports or damages 生生.

'''
canon = once(canon, SECTION_5, PARA + SECTION_5)
OLD_ROW = 'conditions kept together and keeping a part, `Becoming.JointKeeping`; §4.)'
canon = once(canon, OLD_ROW, 'conditions kept together and keeping a part, `Becoming.JointKeeping`; a code formed '
             'between formations, imposed and written back, `Becoming.SharedCodes`; §4.)')
OPEN_END = 'homeostasis and carrying capacity stated as instances. |'
canon = once(canon, OPEN_END, 'homeostasis and carrying capacity stated as instances; the orders exchange takes, with '
             'probabilities over orders, and the time agreement takes; codes holding several forms for a sense, and '
             'adoption of whole codes. |')
REC_END = '[conditions-kept-together](../results/records/conditions-kept-together.md) |'
canon = once(canon, REC_END, '[conditions-kept-together](../results/records/conditions-kept-together.md), ' + RECORD + ' |')
ITEM = (f'- A code formed between formations (D{D}). 约定俗成 is breaking a symmetry by the order of hearing, a centre '
        'and a preferred form being the other two ways; 同则同之 is what renaming cannot change; 书同文 is an imposed '
        'code whose merges return only from a form kept outside; the 說文\'s 止戈 is a reading written back, barred only '
        'by records kept from before. The coupling form proposed for 名无固宜 is false.\n')
canon = once(canon, '- One account (D45).', ITEM + '- One account (D45).')
canon, k = re.subn(r'numbered D1–D\d+', f'numbered D1–D{D}', canon)
assert k == 1, k
COUNTS = re.compile(r'There are \d+ dependency components, with \d+ spine theorems outside the main one; \d+ statements '
                    r'use both families\.')
assert len(COUNTS.findall(canon)) == 1
canon = COUNTS.sub(
    f'Rerun with SC (receipt {R}), it counts {number(apart)} of {number(total)}, none in `{MODULE}`, whose laws are '
    f'stated on runs of hearing and on the runs of its laws. There are {components} dependency components, with '
    f'{outside} spine theorems outside the main one; {both} statements use both families.', canon)
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
    f'on main {MAIN[:9]} with SC (`{MODULE}`, [study §{N}]({STUDY_LINK})) in the working tree. It passed. Its '
    'counts:') + canon[end:]
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

zh = CANON_ZH.read_text()
PARA_ZH = (f'**在形成之间形成的编码**（[{MODULE}]({LEAN})；记录 {RECORD}）。每个形成持有一个从义到形的编码，只经听取而改变：'
           '听者在一条读两个编码的给定规则允许处，取说者给一义之形；听取是脊柱的一个过程。听取不造新形（`run_held`）。一组在某义上的'
           '相合恰经对它封闭的听取而保持（`kept_iff`），全体相合在每条规则下都是静止（`all_agree_rest`）。所成之形由起点与听取的次序'
           '固定：一个次序恰在给每个形成同一来源时，从每个起点都形成相合（`run_agrees_every_start_iff`），在用的任何形都可成为共有之形'
           '（`run_shared_iff_in_use`）。经耦合相连并不够：路的两端各取其自身与所耦合者中编号最小者，两端永不相合（`Path.never_agree`）。'
           '一个形成恰在两编码于某义相合处，把对方之形读作所指之义（`reads_iff`），逐义形成的相合可以合并诸义'
           '（`TwoFormations.homonym`）。不特许任何形式（`run_renamed`）；既不特许形式也不特许形成者的律，永不使对称的分歧相合'
           '（`never_agrees_of_both`）：中心、偏好之形或听取的次序打破对称（`TwoFormations.three_agree`）。强加的编码使所有人相合；'
           '每个形成失去其编码所分而强加编码所合并者，只有强加之外保留的形式能把它带回（`run_from_imposition`、`outside_needed`）。'
           '写回后代所读记录的读法即刻静止，合并此前的历史，只为此前保留下来的记录所阻（`written_rests`、`resolved_alike_merged`、'
           '`kept_bars`）；记录只增补处，判定可失去而不被替换（`added_never_replaced`）。读法是 AI 的（D' + str(D) + '）：约定俗成是以'
           '使用的次序打破对称，荀子自己的王者制名是第一途，即中心；同则同之说的是改名所不能改者；书同文是强加的编码，外面不保留旧形则其'
           '合并不回（“古文由此絕”）；说文之止戈为武是写回其证据的读法，只有止为足的甲骨金文字形这些此前的记录阻止它。这些都不说共有的、'
           '强加的或保留的编码支持还是损害生生。\n\n')
zh = once(zh, SECTION_5, PARA_ZH + SECTION_5)
zh, k = re.subn(r'编号 D1–D\d+', f'编号 D1–D{D}', zh)
assert k == 1, k
CANON_ZH.write_text(zh)
print(N, D, thms, decls_n, apart, total)
