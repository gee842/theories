#!/usr/bin/env python3
"""MA1 landing text: the study section; the chapter (EN, ZH: sections 4.1, 4.3 and 4.5, the record table, the
glossary's meta-attractor and 元闭 rows, section 9's receipt, counts and layers); OPENING's note [^meta]; the
meta-attractor page's status; D58 in DELEGATED-CHOICES; the coverage file's collective row; the board row moved to
the history file and the queue and receipt sentences. Every edit must match exactly once.

usage (from the checkout root to edit): python3 -B apply_text.py RECEIPT CONNECTIVITY_LOG BASE
Prints the study section number."""
import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path.cwd()
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHOICES = '_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md'
CH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
ZH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
OPENING = 'theories/becoming/OPENING.md'
META = 'theories/meta-attractor/README.md'
COVERAGE = 'theories/becoming/results/completion/COVERAGE.json'
BOARD = '_process/BECOMING-WORKBOARD.md'
HISTORY = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-20-meta-attractor-note-taken-care-of.md'
MOD = 'Becoming.ClosedCapture'
RID = 'closed-capture'
receipt_id, conn_log, base = sys.argv[1], sys.argv[2], sys.argv[3]


def edit(path, pairs):
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    for old, new in pairs:
        k = text.count(old)
        if k != 1:
            sys.exit(f'{path}: expected one match, found {k}: {old[:100]!r}')
        text = text.replace(old, new)
    p.write_text(text, encoding='utf-8')
    print('edited', path, len(pairs))


R = json.loads((ROOT / PKG / 'becoming-checks' / receipt_id / 'verification.json').read_text())
assert R['status'] == 'passed' and R['core_compiles_from_prelude'] and R['source_unchanged_during_check']
core = [m for m in R['modules'] if m['layer'] == 'core']
assert not any(v for m in R['modules'] for v in m['axiom_dependencies'].values())
mod = next(m for m in core if m['module'] == MOD)
n_mod_thm, n_mod_decl = mod['theorems'], len(mod['declarations'])
mods, thms = Counter(), Counter()
for m in R['modules']:
    mods[m['layer']] += 1
    thms[m['layer']] += m['theorems']
spine_decls = sum(len(m['declarations']) for m in R['modules'] if m['spine'])
spine_thms = sum(m['theorems'] for m in R['modules'] if m['spine'])
closure = len(R['core_closure'])
closure_thms = sum(m['theorems'] for m in R['modules'] if m['module'] in R['core_closure'])
injeq = len(R.get('generated_axiom_dependencies', {}))
ran, reused = len(R['lean_steps']['ran']), len(R['lean_steps']['reused'])
fmt = lambda n: f'{n:,}'
t = Path(conn_log).read_text() if conn_log.startswith('/') else (ROOT / conn_log).read_text()
conn = json.loads(t[t.index('{'):t.rindex('}') + 1])
apart = sum(v for k, v in conn['classes'].items() if k.startswith('apart'))
assert conn['spine_theorems'] == spine_thms, (conn['spine_theorems'], spine_thms)
mod_apart = conn['apart_by_module'].get(MOD, [0])[0]

# Study section: after the last.
stext = (ROOT / STUDY).read_text(encoding='utf-8')
N = max(int(x) for x in re.findall(r'^## (\d+)\. ', stext, re.M)) + 1
core_line = (f'core {mods["core"]} modules and {fmt(thms["core"])} theorems, instances {mods["instance"]} and '
             f'{thms["instance"]}, applications {mods["application"]} and {thms["application"]}; {ran} Lean steps ran, '
             f'{fmt(reused)} reused')
apart_text = (f'{apart} of {fmt(spine_thms)} apart, {mod_apart} of the module\'s {n_mod_thm}, every root registered; '
              'register check passes')
study = (HERE / 'study_ma1.txt').read_text(encoding='utf-8')
study = (study.replace('{N}', str(N)).replace('{RECEIPT}', receipt_id).replace('{THEOREMS}', str(n_mod_thm))
         .replace('{DECLS}', str(n_mod_decl)).replace('{APART}', apart_text).replace('{CORE_LINE}', core_line))
(ROOT / STUDY).write_text(stext.rstrip('\n') + '\n\n' + study.rstrip('\n') + '\n', encoding='utf-8')
print('appended', STUDY, 'section', N)
SLUG = f'{N}-the-meta-attractors-loop-closed-on-the-spine-ma1'
SA = f'../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#{SLUG}'
REC = f'[{RID}](../results/records/{RID}.md)'

# Chapter, English.
OLD41 = ("present advantage changes future selection ([meta-attractor](../../meta-attractor/README.md)).\n")
NEW41 = ("present advantage changes future selection ([meta-attractor](../../meta-attractor/README.md)). The loop in which "
         "the rule of selection, and how it is read, are formed from the share it selects is stated in §4.5.\n")
OLD45W = ("Where a rule of selection is read from the share it selects, what holds the outcome is how the rule reads, "
          "not the rule's value, which every reading step sets again.\n")
NEW45W = (OLD45W.rstrip('\n') + " Where how the rule is read is itself formed from the share, and nothing in the loop "
          "reads what lies beyond the share, the loop is closed: a loss it does not read leaves it locked however large "
          "the loss grows, a change of the reading is absorbed as a change of the rule's value is, and what leaves is a "
          "change of the law, such as a reading that reaches what lies beyond the share.\n")
OLD45B = ("it is where “the winner shapes the rule” of `Becoming.Capture` enters, as a premise, not a conclusion.\n")
NEW45B = OLD45B + (
    "- `ClosedCapture.lock_outlives_loss`: read the fast configuration as the share and what lies beyond it. Where neither "
    "the next share nor the rule read reads what lies beyond (`Unread`), courses from starts alike in share and rule stay "
    "alike in both at every step (`unread_course`), and the share's law joined with a step beyond runs exactly as the "
    "share's law alone (`join_course`); so from a locked configuration a loss rising by at least one a step passes every "
    "bound while the course stays locked and neither share nor rule falls below the start. A reading that favours at no "
    "loss above a bound turns at the step after the first reading step past it (`turned_by_loss`); in `Beyond` the same "
    "selection from the same start stays locked read from the share and, read from the loss, favours the others from the "
    "second step with the share falling at the third (`Beyond.closed_locked`, `Beyond.open_turned`, "
    "`Beyond.open_falls`). Where how the rule is read is itself formed from the share (`mind`) and the rule read through "
    "it (`read`), rule and reading are one rule read from the share (`both_reads`): locked, none of share, rule and "
    "reading falls (`readers_not_below`), a change of the reading of any size, either way, is absorbed at the next "
    "reading step (`reading_absorbed`), and where the rule read favours at every reading every course locks from its "
    "second reading step (`readers_uniform_locks`); `Proportional` meets every premise (`Proportional.reform_absorbed`). "
    "That the reading is formed from the share is the premise `ReadsShare` on `mind`, not a conclusion.\n")
OLDREAD = '*Readings* [AI reading, D48, D56, D57]. Forming the next members'
NEWREAD = '*Readings* [AI reading, D48, D56, D57, D58]. Forming the next members'
OLDNONE = ("None of these says whether a shared, imposed or locked code or loop supports or damages 生生.\n")
NEWNONE = (
    "The corpus's meta-attractor (元吸引子) is this loop closed: the winners of one round writing the next round's "
    "scorecard is `ReadsShare`, the winners forming the minds the scorecard will later read is `ReadsShare` on `mind`, "
    "and “the metric survives its own refutation” is `lock_outlives_loss`: the refutation lies beyond the share, and "
    "nothing in the loop reads it. Goodhart's law says a measure made a target stops measuring; the loop says why it is "
    "kept: what keeps it reads the share it gives, not what it fails to measure. What leaves is a change of the law, such as 明, a "
    "reading reaching what the share does not carry (§7.3), not reform of the state, the rule's value or the readers "
    "alone, since the share forms each of them again. That actual rules and readers are so formed is the "
    "premise, and that readers are minds is a reading. " + OLDNONE)
OLDRECS = ('[capture-through-the-rule](../results/records/capture-through-the-rule.md), '
           '[joint-practice-forms-continuation]')
NEWRECS = ('[capture-through-the-rule](../results/records/capture-through-the-rule.md), ' + REC + ', '
           '[joint-practice-forms-continuation]')
OLD43 = ("where the rule reads the share it selects, only a change of how it reads leaves (`Becoming.RuleCapture`). |")
NEW43 = ("where the rule reads the share it selects, only a change of how it reads leaves (`Becoming.RuleCapture`), and a "
         "loss the loop does not read leaves it locked (`ClosedCapture.lock_outlives_loss`). |")
OLDROW = ('| [Capture through the rule: a selection whose rule reads the share it selects]'
          '(../results/records/capture-through-the-rule.md) | theorem without premise | — | §4.5 |\n')
NEWROW = (f'| [Closed capture: a loop whose every level reads only the share](../results/records/{RID}.md) | theorem '
          'without premise | — | §4.5 |\n')
OLDGM = ("The nearest formal terms here are hijacking (a goal kept by the rules the winners write), re-absorption under a "
         "rule, and runaway. | `share_rises`, `Law.perturbation_reabsorbed` |")
NEWGM = ("The nearest formal terms here are hijacking (a goal kept by the rules the winners write), re-absorption under a "
         "rule, and runaway. Its loop is stated in §4.5 under named premises: a rule read from the share it selects locks "
         "(capture through the rule), how the rule is read, formed from the share, locks with it, and a loss the loop "
         "does not read leaves it locked (closed capture). | `share_rises`, `Law.perturbation_reabsorbed`, "
         "`RuleCapture.uniform_locks`, `ClosedCapture.lock_outlives_loss`, `ClosedCapture.reading_absorbed` |")
OLDGC = ("and only a change of the reading leaves (`Becoming.RuleCapture`, §4). | `Law.rule_absorbing`, "
         "`Captured.state_perturbation_drawn`, `Law.perturbation_reabsorbed`, `Captured.rule_perturbation_drawn`, "
         "`RuleCapture.perturbation_absorbed`, `RuleCapture.uniform_locks` |")
NEWGC = ("and only a change of the reading leaves (`Becoming.RuleCapture`, §4). Where how the rule is read is itself "
         "formed from the share, a change of the reading is absorbed in the same way, and a loss the loop does not read "
         "leaves it locked; what leaves is a change of the law, such as a reading that reaches what lies beyond the "
         "share (`Becoming.ClosedCapture`, §4.5). | `Law.rule_absorbing`, `Captured.state_perturbation_drawn`, "
         "`Law.perturbation_reabsorbed`, `Captured.rule_perturbation_drawn`, `RuleCapture.perturbation_absorbed`, "
         "`RuleCapture.uniform_locks`, `ClosedCapture.reading_absorbed`, `ClosedCapture.lock_outlives_loss` |")
ch = (ROOT / CH).read_text(encoding='utf-8')
L1 = mods['core'] - 1 - 3 - 17
OLD_CORE = re.search(r'with the base and its layers: (\d+) modules counting the root `Becoming`\.', ch).group(0)
OLD_L2 = re.search(r'L2, the (\d+) modules whose source names the condition', ch).group(0)
OLD_L1 = re.search(r'L1, the other (\d+) of the core,', ch).group(0)
i = ch.index('**The current receipt** is run [`')
OLD_RECEIPT = ch[i:ch.index('\n', i)]
NEW_RECEIPT = (f"**The current receipt** is run [`{receipt_id}`](../../../{PKG}/becoming-checks/{receipt_id}/verification.json) "
               f"(the [current pointer](../../../{PKG}/becoming-verification.json)), checked with Lean 4.29.1 on main "
               f"{base[:9]} with MA1 in the working tree ([study §{N}]({SA})). It passed, the source unchanged during the "
               "check and the core with the ring compiled from the prelude.")
i = ch.index('| Core modules (with the root `Becoming`, 0 theorems) |')
j = ch.index('\n', ch.index('| Generated `injEq` lemmas on `propext` |', i))
OLD_TABLE = ch[i:j]
NEW_TABLE = f"""| Core modules (with the root `Becoming`, 0 theorems) | {mods['core']} modules, {fmt(thms['core'])} theorems |
| Instance modules | {mods['instance']} modules, {fmt(thms['instance'])} theorems |
| Application modules | {mods['application']} modules, {fmt(thms['application'])} theorems |
| Foundation modules | {mods['foundation']} modules, {thms['foundation']} theorems |
| Closure (core, ring and foundation) | {closure} modules, {fmt(closure_thms)} theorems |
| Spine (the core and the ring; no bridge since F3) | {fmt(spine_thms)} theorems |
| Audited spine declarations | {fmt(spine_decls)} |
| Inherited modules bound to passed receipts by hash | 3 (the foundation) |
| Superseded periphery modules (out of the run, bytes kept) | {len(R['superseded_modules'])} |
| Modules in the compile order | {len(R['compile_order'])} |
| Generated `injEq` lemmas on `propext` | {injeq} in the closure |"""
OLD_STEPS = re.search(r'The run reused [\d,]+ cached Lean steps from `~/.cache/becoming-lean` and ran \d+;', ch).group(0)
NEW_STEPS = f'The run reused {fmt(reused)} cached Lean steps from `~/.cache/becoming-lean` and ran {ran};'
edit(CH, [(OLD41, NEW41), (OLD45W, NEW45W), (OLD45B, NEW45B), (OLDREAD, NEWREAD), (OLDNONE, NEWNONE),
          (OLDRECS, NEWRECS), (OLD43, NEW43), (OLDROW, OLDROW + NEWROW), (OLDGM, NEWGM), (OLDGC, NEWGC),
          (OLD_CORE, f"with the base and its layers: {mods['core']} modules counting the root `Becoming`."),
          (OLD_L2, 'L2, the 17 modules whose source names the condition'), (OLD_L1, f'L1, the other {L1} of the core,'),
          (OLD_RECEIPT, NEW_RECEIPT), (OLD_TABLE, NEW_TABLE), (OLD_STEPS, NEW_STEPS)])

# Chapter, Chinese.
z = (ROOT / ZH).read_text(encoding='utf-8')
OLDZ41 = '当下的优势改变未来的选择（[元吸引子](../../meta-attractor/README.md)）。\n'
NEWZ41 = ('当下的优势改变未来的选择（[元吸引子](../../meta-attractor/README.md)）。选择的规则及其被读的方式都由它所选出的份额形成，'
          '这一回路陈述于 §4.5。\n')
OLDZ45W = '选择的规则从它所选择的份额读出之处，持住结果的是规则怎样读取，不是规则的值，每个读取步都重新设定它。\n'
NEWZ45W = (OLDZ45W.rstrip('\n') + '规则怎样被读本身由份额形成、且回路中没有什么读份额之外者之处，回路闭合：它不读的损失不论增长多大都使它保持锁定，'
           '读法的改变如规则之值的改变一样被吸收；离开的是律的改变，例如读到份额之外者的读法。\n')
OLDZ45T = '`favouring_locks`、`uniform_locks`；完整陈述见'
NEWZ45T = ('`favouring_locks`、`uniform_locks`、`ClosedCapture.lock_outlives_loss`（回路不读的损失越过每一界限，锁定仍保持）、'
           '`ClosedCapture.reading_absorbed`（由份额形成的读法的改变在下一读取步被吸收）；完整陈述见')
OLDZRECS = ('[capture-through-the-rule](../results/records/capture-through-the-rule.md)、'
            '[joint-practice-forms-continuation]')
NEWZRECS = ('[capture-through-the-rule](../results/records/capture-through-the-rule.md)、' + REC + '、'
            '[joint-practice-forms-continuation]')
OLDZROW = '| [经由规则的捕获：规则读其所选出之份额的选择](../results/records/capture-through-the-rule.md) | 不加前提的定理 | — | §4.5 |\n'
NEWZROW = f'| [闭合的捕获：每一层都只读份额的回路](../results/records/{RID}.md) | 不加前提的定理 | — | §4.5 |\n'
OLDZGC = ('只有改变读法才离开（`Becoming.RuleCapture`，§4）。 | `Law.rule_absorbing`、`Captured.state_perturbation_drawn`、'
          '`Law.perturbation_reabsorbed`、`Captured.rule_perturbation_drawn`、`RuleCapture.perturbation_absorbed`、'
          '`RuleCapture.uniform_locks` |')
NEWZGC = ('只有改变读法才离开（`Becoming.RuleCapture`，§4）。规则怎样被读本身由份额形成之处，读法的改变也同样被吸收，回路不读的损失使它保持锁定；'
          '离开的是律的改变，例如读到份额之外者的读法（`Becoming.ClosedCapture`，§4.5）。 | `Law.rule_absorbing`、'
          '`Captured.state_perturbation_drawn`、`Law.perturbation_reabsorbed`、`Captured.rule_perturbation_drawn`、'
          '`RuleCapture.perturbation_absorbed`、`RuleCapture.uniform_locks`、`ClosedCapture.reading_absorbed`、'
          '`ClosedCapture.lock_outlives_loss` |')
i = z.index('**当前回执**是运行 [`')
OLDZR = z[i:z.index('\n', i)]
NEWZR = (f"**当前回执**是运行 [`{receipt_id}`](../../../{PKG}/becoming-checks/{receipt_id}/verification.json)"
         f"（[当前指针](../../../{PKG}/becoming-verification.json)），以 Lean 4.29.1 检查（[研究第 {N} 节]({SA})）。")
i = z.index('| 核心模块（含根 `Becoming`） |')
j = z.index('\n', z.index('| 被取代的外围模块', i))
OLDZT = z[i:j]
NEWZT = f"""| 核心模块（含根 `Becoming`） | {mods['core']} 个模块，{fmt(thms['core'])} 条定理 |
| 实例模块 | {mods['instance']} 个模块，{fmt(thms['instance'])} 条定理 |
| 应用模块 | {mods['application']} 个模块，{fmt(thms['application'])} 条定理 |
| 根基模块 | {mods['foundation']} 个模块，{thms['foundation']} 条定理 |
| 闭包（核心、环与根基） | {closure} 个模块，{fmt(closure_thms)} 条定理 |
| 审计的脊柱声明 | {fmt(spine_decls)} |
| 在 `propext` 上的生成的 `injEq` 引理 | 闭包中 {injeq} 条 |
| 被取代的外围模块（不在运行中，字节保留） | {len(R['superseded_modules'])} |"""
edit(ZH, [(OLDZ41, NEWZ41), (OLDZ45W, NEWZ45W), (OLDZ45T, NEWZ45T), (OLDZRECS, NEWZRECS),
          (OLDZROW, OLDZROW + NEWZROW), (OLDZGC, NEWZGC), (OLDZR, NEWZR), (OLDZT, NEWZT)])

# OPENING's note on the meta-attractor (AI-written; the body is Ren's and is not touched).
o = (ROOT / OPENING).read_text(encoding='utf-8')
i = o.index('[^meta]: **')
OLDNOTE = o[i:o.index('\n', i)]
assert 'its loop is not on this theory\'s spine' in OLDNOTE, OLDNOTE[:120]
NEWNOTE = (
    "[^meta]: **A theory with formal results at its own scope; its loop is on this theory's spine under named premises; "
    "its present reach is a judgment.** [The Meta-Attractor](../meta-attractor/README.md) develops how a pattern of "
    "selection gains power over the rule that selects, so that the winners of one round write the next round's "
    "scorecard, and how the loop closes in the minds it selects. The spine states that loop under premises it names "
    "([§4.5](chapters/THE-THEORY-OF-BECOMING.md#45-passing-shared-codes-and-capture-through-the-rule)). Where a "
    "selection's rule is read from the share it selects, monotonically (the premise `ReadsShare`), the loop locks: "
    "neither share nor rule falls again, a change of the rule's value that keeps its direction is absorbed at the next "
    "reading, and only a change of how the rule reads leaves (`Becoming.RuleCapture`); on counts, with the margin by "
    "which the rule favours read from the share, the margin falls at no step after the first reading and the share rises "
    "strictly at every step whose margin is positive, which is winning buying more power to win (`CarrierCounts.margin_course`, "
    "`CarrierCounts.rises_strictly_along`). Where how the rule is read is itself formed from the share, a change of the "
    "reading alone is absorbed in the same way (`ClosedCapture.reading_absorbed`), so in a loop whose every level reads "
    "only the share the share forms each level again, and what leaves is a change of the law, such as a reading that "
    "reaches what lies beyond the share (明). A loss the loop does not read changes nothing in it: the locked loop outlives a loss that passes "
    "every bound (`ClosedCapture.lock_outlives_loss`), which is how a measure survives its own refutation, while a "
    "reading of the loss turns once the loss passes its bound (`ClosedCapture.turned_by_loss`) "
    f"([record](results/records/{RID}.md)). That actual rules and readings are formed from the share is the premise, "
    "not a result, and that the readers are minds is a reading. In this theory's "
    "[collective dynamics](chapters/THE-THEORY-OF-BECOMING.md#4-collective-dynamics), joint consumption has no single "
    "consumer, and \"my share makes no difference\" does not remove a drawer from consumption "
    "([record](results/records/joint-difference-making.md)). Its calibration to today's world is not established.")
edit(OPENING, [(OLDNOTE, NEWNOTE)])

# The meta-attractor page: a status paragraph at the head (its other dated paragraphs stay as they are).
OLDMETA = '# The Meta-Attractor (元吸引子 / 总体化吸引子)\n\n'
NEWMETA = OLDMETA + (
    "**主干上的回路 / The loop on the spine，2026-10-20。** 规则从它所选出的份额读出时回路锁定（`Becoming.RuleCapture`）；规则怎样被读本身由份额形成时，"
    "只改读法被吸收；回路不读的损失越过每一界限，锁定仍保持，这就是度量在自身被驳倒后仍存（`Becoming.ClosedCapture`，"
    f"[记录](../becoming/results/records/{RID}.md)）。/ The loop this page develops is now on the Becoming spine under "
    "named premises: a rule read from the share it selects locks; how the rule is read, formed from the share, locks with "
    "it; a loss the loop does not read leaves it locked however large it grows, and a reading of the loss leaves "
    f"([chapter §4.5](../becoming/chapters/THE-THEORY-OF-BECOMING.md#45-passing-shared-codes-and-capture-through-the-rule)). "
    "That actual rules and readers are so formed is the premise `ReadsShare`, not a result; the calibration to the "
    "present world is not established.\n\n")
edit(META, [(OLDMETA, NEWMETA)])

# D58.
OLDD = next(l for l in (ROOT / CHOICES).read_text(encoding='utf-8').split('\n') if l.startswith('| D57 |')) + '\n'
NEWD = OLDD + ('| D58 | the readings of the meta-attractor\'s loop on the spine (20 October) | adopted with exact scope: the winners '
               'writing the next scorecard the premise `ReadsShare`; the winners forming the minds the scorecard reads '
               '`ReadsShare` on `mind`; the metric surviving its refutation `lock_outlives_loss` (the refutation lies '
               'beyond the share, unread); leaving 明, a reading of what lies beyond the share, or a change of the law; '
               'readers as minds a reading |\n')
OLDREQ = ('- The same request, continued by board item RC (capture through the rule, the third gap RO found): D57 '
          '([study section 213](BECOMING-RENEWAL-READING.md#213-capture-through-the-rule-rc)).\n')
NEWREQ = OLDREQ + (f'- Ren\'s message of 20 October 2026 on OPENING\'s note on the meta-attractor, “this needs to be fully '
                   f'taken care of” ([words](../../../../{SOURCE})): D58 ([study section {N}](BECOMING-RENEWAL-READING.md#{SLUG})).\n')
choices = (ROOT / CHOICES).read_text(encoding='utf-8')
SECTION = f"""
### The readings of the meta-attractor's loop on the spine

Where: OPENING's note `[^meta]`; the canonical chapter, §4.5 and the glossary's meta-attractor and 元闭 rows; the record [{RID}](../../../../theories/becoming/results/records/{RID}.md); the [meta-attractor page](../../../../theories/meta-attractor/README.md); study section {N} ([MA1](BECOMING-RENEWAL-READING.md#{SLUG})). Decided in the one account of D45.

**Decision.** Adopted with exact scope. (1) **The winners write the next round's scorecard.** Read as the premise `ReadsShare`: the rule read at a reading step is a monotone function of the share the selection gave; what is derived is that such a rule holds the outcome (`RuleCapture.uniform_locks`), not that any actual rule is so read. (2) **The loop closes in the minds it selects.** Read as how the rule is read, itself formed from the share (`ReadsShare` on `mind`): the readers are formed by what they select, and a change of the reading alone is absorbed (`ClosedCapture.reading_absorbed`). That the readers are minds, rather than institutions, codes or a culture, is the reading, not the law. (3) **The metric survives its own refutation.** Read as `lock_outlives_loss`: the refutation is what lies beyond the share, and where neither the selection nor the reading reads it (`Unread`) the lock holds however large it grows. Goodhart's law is the measure ceasing to measure; this is why it is kept. (4) **Leaving.** Read as a change of the law, of which 明, a reading that reaches what the share does not carry, is one (`turned_by_loss`, §7.3); reform of the state, of the rule's value or of the readers alone is re-formed by the share. Where the reading favours at every share this is exact: no change of configuration leaves the lock for longer (`RuleCapture.uniform_locks`, `readers_uniform_locks`); where it favours only above a threshold, a change of the share across the threshold also leaves (`RuleCapture.Reversed.not_absorbed`).

**Reasons.** Each reading names the declarations it rests on and says no more than they prove. The note said the loop was not on the spine and that Capture's premise excluded the state writing the rule; RuleCapture states that writing as a premise, and ClosedCapture states the two parts the note's description still needed, so the description is no longer only a reading: the loop is a law under named premises, and what stays a reading is which actual formations meet them.

**What would change it.** A rule or reading formed from the share under which a change of the reading alone leaves the lock; a reading of the loss that leaves no lock it reads; a calibration showing that the decisive rules of a present system read more than the share they give.
"""
choices = choices.rstrip('\n') + '\n' + SECTION
(ROOT / CHOICES).write_text(choices, encoding='utf-8')
edit(CHOICES, [(OLDD, NEWD), (OLDREQ, NEWREQ)])

# Coverage: the collective row reads the new record.
cov = json.loads((ROOT / COVERAGE).read_text())
row = next(r for r in cov['rows'] if r['id'] == 'collective')
assert RID not in row['records']
row['records'].append(RID)
row['declarations'].append('Becoming.ClosedCapture.lock_outlives_loss')
(ROOT / COVERAGE).write_text(json.dumps(cov, ensure_ascii=False, indent=2) + '\n')
print('coverage row collective')

# Board: the row moves to the history file; the queue and receipt sentences name the landing.
board = (ROOT / BOARD).read_text(encoding='utf-8')
history = (ROOT / HISTORY).read_text(encoding='utf-8')
lines = board.split('\n')
rows = [i for i, line in enumerate(lines) if line.startswith("| **MA1: the meta-attractor's loop closed on the spine**")]
assert len(rows) == 1, rows
row = lines.pop(rows[0])
cells = row.split(' | ')
assert len(cells) == 5, len(cells)
cells[2] = (f'landed 2026-10-20, core receipt `{receipt_id}`; {n_mod_thm} theorems in one core module, empty axiom '
            f'reports; record {RID}; readings D58; study §{N}')
row = ' | '.join(cells).replace('](../', '](../../../').replace('](research/', '](../../research/')
hist = history.split('\n')
stop = next((i for i, line in enumerate(hist) if line.startswith('## Lapsed claims')), len(hist))
lastrow = max(i for i, line in enumerate(hist[:stop]) if line.startswith('| **'))
hist.insert(lastrow + 1, row)
board = '\n'.join(lines)
m = re.search(r"the latest core receipt is [^;]*?`(\d{8}T\d{6}\.\d+Z)` \(20 October 2026\)", board)
assert m, 'receipt sentence'
board = board.replace(m.group(0), f"the latest core receipt is MA1's `{receipt_id}` (20 October 2026)")
m = re.search(r'- \*\*Queue:\*\* ([^\n]*)', board)
assert m, 'queue sentence'
q = m.group(1)
q2 = re.sub(r'MA1 (after RB1|next|at the head)[^;]*; ', '', q)
assert q2 != q, 'MA1 not in the queue sentence'
board = board.replace(m.group(0), f'- **Queue:** MA1 landed (the meta-attractor\'s loop closed on the spine, '
                      f'`Becoming.ClosedCapture`; OPENING `[^meta]` restated; core receipt `{receipt_id}`, study §{N}, '
                      f'readings D58, row in the history file); {q2}')
(ROOT / BOARD).write_text(board, encoding='utf-8')
(ROOT / HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('board row moved; receipt', receipt_id, 'apart', apart, 'spine theorems', spine_thms)
print('STUDY_SECTION', N)
