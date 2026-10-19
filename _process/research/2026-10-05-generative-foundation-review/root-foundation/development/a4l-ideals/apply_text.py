#!/usr/bin/env python3
"""A4-L landing text: python3 -B apply_text.py RECEIPT BASE AFTER CONN_LOG CORR_RECEIPT

RECEIPT is the core checker run, BASE the main commit it ran on, AFTER what BASE adds to the last landing (for the
receipt sentence), CONN_LOG the connectivity check's output, CORR_RECEIPT the correspondence checker's run. Writes the
study section; the chapter (sections 2, the theory stated whole, 8.1, 8.2, 8.4, 8.6 and 9, English); the module and
instance rows of the reference; the record what-a-finite-history-refutes (next delta, correspondence, related,
history); the directive register's note on Ren's "(a)" of 16 October; and the landed note under D45 (4), en and zh.
The counts are read from the receipts and the log. Every edit must match exactly once. Prints the study section number
last. The package README rows, the CORE list, the root and the scope text are integrate.py's; the apart register's
entries register_apart.py's; the new record make_record.py's."""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
RID, BASE, AFTER, CONN_LOG, CORR = sys.argv[1:6]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
FORMAL = 'experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/completion/formal'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
STUDY = RF + 'BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
REFERENCE = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING-REFERENCE.md'
DIRECTIVES = '_process/RESEARCH-DIRECTIVES.md'
CHOICES, CHOICES_ZH = RF + 'DELEGATED-CHOICES.md', RF + 'DELEGATED-CHOICES.zh.md'
HORIZON_RECORD = 'theories/becoming/results/records/what-a-finite-history-refutes.json'
REN = 'integrate all, the theory is a whole, not stitched pieces, go ahead'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-19-integrate-all.md'
RECID = 'a-history-read-off-its-finite-stretches'

# Links from the chapter and the reference (theories/becoming/chapters/).
C_REC = f'../results/records/{RECID}.md'
C_HREC = '../results/records/what-a-finite-history-refutes.md'
C_IDEALS = f'../../../{PKG}/Becoming/Ideals.lean'
C_HISTORY = f'../../../{PKG}/Becoming/HistoryIdeals.lean'
C_CORR = f'../../../{FORMAL}/IdealsCorrespondence.lean'
C_STUDY = '../../../' + STUDY
# Links from the study and the choices (the root-foundation folder).
S_SOURCE = '../../../../' + SOURCE
S_REC = f'../../../../theories/becoming/results/records/{RECID}.md'


OUT = {}


def read(path):
    return OUT[path] if path in OUT else (ROOT / path).read_text(encoding='utf-8')


def write(path, text):
    """Stage an edit; nothing is written until every edit has matched."""
    OUT[path] = text


def once(text, old, new, what):
    k = text.count(old)
    if k != 1:
        sys.exit(f'{what}: expected one match, found {k}: {old[:100]!r}')
    return text.replace(old, new)


def subn1(pattern, repl, text, what):
    text, k = re.subn(pattern, repl, text)
    if k != 1:
        sys.exit(f'{what}: expected one match, found {k}')
    return text


def insert_after_line(text, start, new_lines, what):
    lines = text.split('\n')
    idx = [i for i, line in enumerate(lines) if line.startswith(start)]
    if len(idx) != 1:
        sys.exit(f'{what}: expected one line, found {len(idx)}')
    lines[idx[0] + 1:idx[0] + 1] = new_lines
    return '\n'.join(lines)


def replace_line(text, start, new, what):
    lines = text.split('\n')
    idx = [i for i, line in enumerate(lines) if line.startswith(start)]
    if len(idx) != 1:
        sys.exit(f'{what}: expected one line, found {len(idx)}')
    lines[idx[0]] = new
    return '\n'.join(lines)


def n(x):
    return f'{x:,}'


# ------------------------------------------------------------------ counts
receipt = json.loads(read(f'{PKG}/becoming-checks/{RID}/verification.json'))
assert receipt['status'] == 'passed', receipt['status']
mods = {m['module']: m for m in receipt['modules']}
th = lambda names: sum(int(mods[x]['theorems']) for x in names)
c = {
    'core': (len(receipt['core_modules']), th(receipt['core_modules'])),
    'foundation': (len(receipt['foundation_modules']), th(receipt['foundation_modules'])),
    'closure': (len(receipt['core_closure']), th(receipt['core_closure'])),
    'bridge': (len(receipt['bridge_modules']), th(receipt['bridge_modules'])),
    'spine': th(receipt['spine_modules']),
    'audited': sum(len(mods[x]['declarations']) for x in receipt['spine_modules']),
    'pj': len(receipt['periphery_join_modules']),
    'inherited': len(receipt['inherited_receipts']),
    'compile': len(receipt['compile_order']),
    'injeq': (len(receipt['generated_axiom_dependencies']), len(receipt['bridge_generated_axiom_dependencies'])),
    'ran': len(receipt['lean_steps']['ran']),
    'reused': len(receipt['lean_steps']['reused']),
}
ideals_t, history_t = int(mods['Becoming.Ideals']['theorems']), int(mods['Becoming.HistoryIdeals']['theorems'])
ideals_d, history_d = len(mods['Becoming.Ideals']['declarations']), len(mods['Becoming.HistoryIdeals']['declarations'])
assert c['bridge'] == (0, 0) and c['pj'] == 0 and c['injeq'][1] == 0, (c['bridge'], c['pj'], c['injeq'])
assert c['spine'] == c['core'][1], (c['spine'], c['core'])
log = Path(CONN_LOG).read_text()
conn = json.loads(log[log.index('{'):log.rindex('}') + 1])
assert not conn['apart_roots_unclassified'] and not conn['register_entries_not_apart_roots']
apart = sum(v for k, v in conn['classes'].items() if k.startswith('apart'))
assert sum(conn['classes'].values()) == c['spine'], (sum(conn['classes'].values()), c['spine'])
ia, ib = conn['apart_by_module'].get('Becoming.Ideals', [0, ideals_t])[0], \
    conn['apart_by_module'].get('Becoming.HistoryIdeals', [0, history_t])[0]
register = json.loads(read(RF + 'THEOREM-CONNECTIVITY-APART.json'))
roots = sum(1 for v in register['roots'].values() if v['module'] in ('Becoming.Ideals', 'Becoming.HistoryIdeals'))
corr = json.loads(read(f'{FORMAL}/ideals-correspondence-checks/{CORR}/verification.json'))
assert corr['status'] == 'passed', corr['status']
target = next(m for m in corr['modules'] if m['module'] == 'IdealsCorrespondence')
corr_t, corr_d = int(target['theorems']), len(target['declarations'])
corr_e = sum(1 for x in target['declarations'] if not target['axiom_dependencies'].get(x['name']))

# ------------------------------------------------------------------ study
s = read(STUDY)
sec = max(int(m) for m in re.findall(r'^## (\d+)\. ', s, re.M)) + 1
anchor = f'{sec}-a-history-read-off-its-finite-stretches-a4-l'
SECTION = f'''## {sec}. A history read off its finite stretches (A4-L)

```text
Result(s): a-history-read-off-its-finite-stretches (new); depends on what-a-finite-history-refutes; related
           becoming-finite-horizon
Delta: section 145 (Becoming.Horizon) stated what a finite history refutes for the runs of every process and left
       IdealWarrant's order form, and the converse of refutable_passes, unstated. IdealWarrant, CompletionRole and
       HistoryIdeals of the completion package proved the order form, the completion and the ideals of histories with
       Std and classical reasoning, outside the run. Here they are one family in the core: a history is the ideal of
       its finite stretches; Horizon's laws are the case of runs of the laws of points; a closed class is the class
       within a lower set, its content; refutable and closed classes pass into each other up to a step that, asked of
       every process, is exactly double-negation elimination; adhering is the least closed class; the completion is
       read at runs; the classification of histories holds for every process, and telling which is LPO
Supplied premises / correspondence: none, no axiom; the classification takes the decision of settling and the picked
       stretches as data; the calibrations take double-negation elimination or LPO as one direction's hypothesis
Evidence: Becoming.Ideals ({ideals_t} theorems) and Becoming.HistoryIdeals ({history_t}), every axiom report empty; core
          receipt `{RID}`; IdealsCorrespondence, {corr_t} theorems, checked by check_ideals_correspondence.py (receipt
          `{CORR}`), {corr_e} of its {corr_d} declarations with empty reports; connectivity check passes, {apart} apart of
          {n(c['spine'])}, {ia + ib} of them in the two modules, their {roots} roots registered
Boundary: what a finite stretch verifies (the open classes) on this order; Boolean tests from the propositional tests a
          closed reading is made of; which readings of an actual unfolding are refutable
```

Ren, 19 October 2026: "{REN}" ([source]({S_SOURCE})). Decision D45 (4) joined `IdealWarrant` with `CompletionRole` and `HistoryIdeals` as one core family under structural names ([choices](DELEGATED-CHOICES.md#d45-一个说明中的读法--the-readings-in-one-account)), board item A4-L. Ren's "(a)" of 16 October had kept `IdealWarrant` outside the spine (section 153). His words are provenance, not warrant.

**The question.** What a finite history refutes was stated twice: on the runs of every process (`Becoming.Horizon`, section 145) and, classically, on the ideals of any poset (`IdealWarrant`), with the completion (`CompletionRole`) and the ideals of words (`HistoryIdeals`) beside it, outside the run. Are they one law of the unfolding, and what does each classical step say about it?

**The move.** A history is read off its finite stretches. For a process, a stretch is a run with a horizon. One stretch extends another where its horizon is later and the two runs agree up to the earlier one (`stretchOrder`). An ideal of this order is a history: nonempty, closed downward, any two of its stretches extended by a third. A finite history is a principal ideal, and a run is the ideal of the stretches it passes through (`Run.stretches`). `Becoming.Ideals` states the laws for any order. It uses no antisymmetry, so "the same history" is two-way inclusion, not equality. `Becoming.HistoryIdeals` reads them on runs and on words.

**What is proved** (`Becoming.Ideals`, {ideals_t} theorems; `Becoming.HistoryIdeals`, {history_t}; no premise).
- *Points and runs.* A reading of points is refutable where every point outside it shows a stretch that no point of the reading passes through. A point adheres to it where each of its stretches is a stretch of a point of the reading. A refutable reading holds, up to double negation, at every adhering point (`Ideals.RefutableBy.not_not`). For runs, refutability and adhering are these at the runs' ideals (`refutable_iff_refutableBy`, `adheres_iff_adheresBy`). So Horizon's `Refutable.not_not`, `Refutable.adheres_least`, `Refutable.adheres_iff`, `not_refutable_of_adheres` and `refutable_adheres_iff` follow from the laws of points (`Stretches.not_not` and the four after it).
- *Closed classes.* A class of ideals is closed (closed downward and under directed unions) exactly where it is the class of the ideals within a lower set of stretches (`Ideals.closed_iff_lower`). That set is unique (`Ideals.lower_unique`) and is the class's content (`Ideals.lower_iff_content`). Read on runs, a reading that holds every run adhering to it is the reading of the runs whose stretches lie in the content of its runs (`closed_iff_within_lower`). It is made of tests, one for each stretch, read as propositions. This is the converse section 145 left: `refutable_passes` reads Boolean tests fixed by prefixes, the converse gives propositional ones, and Boolean ones would need each test decided.
- *Adhering is the least closed class.* A run adheres to a reading exactly where every closed class of histories holding the reading's runs holds it (`Stretches.adheres_iff_closed`). With closure in place of refutability, no double negation is left. The closure is unique (`Stretches.adherence_unique`) and adds no stretch (`Stretches.adheres_content`). It extends any two stretches of an adhering run by one stretch of one run of the reading (`Stretches.adheres_joint`).
- *Refutable and closed.* A refutable class is closed up to double negation (`Ideals.Refutable.closed`). A closed class is refutable where a history known not to lie within it shows a stretch outside (`Ideals.Closed.refutable_iff`). Asked of every order and class, each step is exactly double-negation elimination (`Ideals.refutable_closed_iff`, `Ideals.closed_refutable_iff`). Asked of every process it is too, with witnesses on the process of `()`s (`Stretches.refutable_closed_iff`, `Stretches.closed_refutable_iff`). And a refutable reading holds at every run adhering to it exactly under double-negation elimination (`refutable_holds_iff`, witnessed on the process of Boolean sequences).
- *Avoidance.* The histories avoiding a set of stretches form a closed class (`Ideals.avoids_closed`), the only closed class holding exactly the finite histories that avoid the set (`Ideals.avoids_unique`). It is refutable where every history failing to avoid the set holds a stretch of it (`Ideals.avoids_refutable_of_found`). On runs these are `Stretches.avoids_adheres`, `Stretches.avoids_runs` and `Stretches.avoids_refutable`. These are the safety classes.
- *A lower set's own histories.* The order a lower set inherits has, as its histories, the process's histories within the set (`Ideals.lift_restrict`, `Ideals.restrict_lift`, `Stretches.inherited_histories`). They are ordered as the runs are (`Stretches.within_order_iff`).
- *The completion.* The ideals are directed-complete (`Ideals.idealComplete`) and compact exactly at the finite histories (`Ideals.compact_iff_principal`), so no run is compact (`Stretches.run_not_compact`). A monotone reading of stretches extends to a continuous reading of histories, unique up to the target's equivalence (`Ideals.unique_continuous_extension`). So a continuous reading is fixed at every run by its values on finite histories (`Stretches.run_reading_unique`). The readings "lies above this stretch" tell histories, and runs, apart (`Ideals.above_readings_separate`, `Stretches.runs_told_apart`). The finite histories are a compact basis (`Stretches.finite_basis`). Any directed-complete order with a compact basis copying the stretches is the order of the histories, by an equivalence the stretches fix (`Ideals.unique_basis_representation`, `Stretches.histories_representation`).
- *Which histories are runs.* A history that settles, having a latest stretch, is finite (`Stretches.settles_principal`). One that goes on, with a stretch beyond each horizon picked, is the history of the run read off the picks (`Stretches.pickedRun`, `Stretches.goesOn_run`). So a history that settles, or goes on with picks, is a finite history or a run (`Stretches.classification`: the completion package's A4, for every process). Telling which, on the histories of `()`s cut at a Boolean sequence's first `true`, is exactly the limited principle of omniscience (`Stretches.cut_decided_iff_lpo`, through the word version `HistoryIdeals.cut_decided_iff_lpo`).
- *Words.* Words are ordered by prefix, and a sequence is the ideal of its initial words (`HistoryIdeals.traceIdeal`). A history's ideal lies below another's exactly where it is a prefix of it (`HistoryIdeals.history_le_iff`), and the same words make the same history (`HistoryIdeals.historyIdeal_same_iff`). For the process of all sequences, the runs' histories are these (`Stretches.sequences_le_iff`, `Stretches.sequences_same_iff`, `Stretches.sequences_within_iff`). A prefix-closed language is a lower set of words, so its histories form a closed class (`HistoryIdeals.history_within_iff`). The finite histories with the infinite ones of a property are not refutable where some sequence lies outside the property (`HistoryIdeals.finiteOr_not_refutable`).

**The instance.** `IdealsCorrespondence` (periphery, Lean 4.30.0-rc2, its own checker) reads the three originals as instances. A poset's order is an order of stretches, its antisymmetry unused, and its ideals and classes are the core's. W1, W2, W2a, A2, A2a, A3 and A4 then follow from the core's laws. {corr_e} of its {corr_d} declarations have empty reports. The rest name the classical or extensionality step each needs: the stability, the element outside, the decision of settling and the picks; equalities of predicates, ideals and words. The originals keep their paths and bytes.

**What this changes.** The order form section 145 left unstated is stated, and Horizon's laws are its case of runs: the theory has one law of what a finite stretch refutes, not two. The classical equivalence of finite refutability and Scott closure (W1) is located: it is two steps, and each, asked of every process, is double-negation elimination. Ren's "(a)" of 16 October is superseded by D45 (4), and the directive register notes it.

*Readings* [AI reading]. Not being refuted by any finite stretch is not belonging: a history that no stretch shows outside a class may still not lie in it, and saying it does is the step double negation would take. A history known not to lie within a closed class does not thereby show the stretch at which it leaves. Telling whether a history ends is deciding whether it changes again. What a finite stretch can show is that a history lies outside a closed class; that a run lies in one is only not refuted.

**Not done.** What a finite stretch verifies, the open classes, read on the same order; Boolean tests from the propositional tests a closed reading is made of, which needs each test decided; a world's courses read as histories of this order (through `worlds-are-runs` they are runs).

**Self-review.** The statements were read against the Lean.
- The first build stood apart from the base: 115 of its 139 theorems (`Becoming.Ideals` 94 of 98, `Becoming.HistoryIdeals` 21 of 41), with 50 roots unregistered. Against "the theory is a whole, not stitched pieces", each law of ideals is now read on the histories of a process (`Stretches`). {ia + ib} of {ideals_t + history_t} stand apart: equivalence and empty-class lemmas, unpacked definitions, two laws of directed suprema, the hull's idempotence (its case of runs is Horizon's `Adheres.adheres`) and the classification of the ideals of words (whose process form is `Stretches.classification`). Their {roots} roots are in the apart register.
- `Stretches.not_not` and the four laws after it restate Horizon's statements on purpose: they derive them from the laws of points, which is the connection. Horizon's own proofs stand.
- `closed_iff_within_lower` was re-proved through the content of the reading's runs (`Ideals.content_lower`), so its lower set is that content.
- The first scratch build of `Stretches` reported two unused variables, which the checker counts as warnings. Renamed `_`, the next build was clean, every axiom report empty.
- The A4-L board row counted 41 correspondence declarations with empty reports; the checker's list and the audit have {corr_e}.

'''
s = once(s, '## Ren’s words quoted in passages that exist only in the Chinese edition',
         SECTION + '## Ren’s words quoted in passages that exist only in the Chinese edition', 'study')
write(STUDY, s)
STUDY_LINK = f'{C_STUDY}#{anchor}'

# ------------------------------------------------------------------ chapter
ch = read(CHAPTER)
S2 = (f'**What a finite stretch refutes, in every process** ([{RECID}]({C_REC}), '
      f'[what-a-finite-history-refutes]({C_HREC})). A history is read off its finite stretches. A stretch is a run up to '
      'a horizon, and one stretch extends another where its horizon is later and the two runs agree up to the earlier '
      'one. The histories are the ideals of this order: a finite history is the stretches below one stretch, and a run '
      f'is the stretches it passes through ([Becoming.Ideals]({C_IDEALS}), [Becoming.HistoryIdeals]({C_HISTORY})). A '
      'reading of runs is refutable where every run outside it passes through a stretch that no run of the reading '
      'passes through; a run adheres to a reading where each of its stretches is a stretch of a run of the reading. '
      'Adhering is the least closed class of histories that holds the reading\'s runs (`Stretches.adheres_iff_closed`). '
      'A closed class is the class of the histories within a lower set of stretches, so a reading that holds every run '
      'adhering to it is made of tests, one for each stretch, read as propositions (`closed_iff_within_lower`). A '
      'refutable reading holds, up to double negation, at every run adhering to it (`Stretches.not_not`, which derives '
      '`Becoming.Horizon`\'s law from the law of any order). Asked of every process, removing that double negation is '
      'exactly double-negation elimination (`refutable_holds_iff`), and so is each direction between refutable and '
      'closed classes (`Stretches.refutable_closed_iff`, `Stretches.closed_refutable_iff`): not being refuted by any '
      'finite stretch is not belonging, and a history known not to lie within a closed class does not thereby show the '
      'stretch at which it leaves. A history that settles is finite, and one that goes on, with a stretch beyond each '
      'horizon picked, is a run (`Stretches.classification`). Telling which, asked of the histories cut at a sequence\'s '
      'first `true`, is exactly the limited principle of omniscience (`Stretches.cut_decided_iff_lpo`): telling whether '
      'a history ends is deciding whether it changes again. The finite histories are a compact basis of the histories, '
      'which are their completion, and a continuous reading of the histories is fixed at every run by its values on the '
      'finite ones (`Stretches.histories_representation`, `Stretches.run_reading_unique`).')
ch = insert_after_line(ch, '**No finite history decides the classification, in the process `Renewable`.**', ['', S2],
                       'section 2 paragraph')
ch = once(ch, 'the origin law with a proposition as the gate is double-negation elimination '
              '(`Gated.origin_of_propositions_iff`), and runs from every member',
          'the origin law with a proposition as the gate is double-negation elimination '
          '(`Gated.origin_of_propositions_iff`), and so is passing, either way, between the refutable classes of '
          'histories and the closed ones (`Stretches.refutable_closed_iff`, '
          '`Stretches.closed_refutable_iff`); telling whether a history ends or goes on is the limited principle of '
          'omniscience (`Stretches.cut_decided_iff_lpo`); and runs from every member', 'the deepest part')
ch = once(ch, ' The apart roots of the superseded modules and of the bridge left the register with them',
          f' Rerun with A4-L (receipt {RID}), it counts {apart} of {n(c["spine"])}: {ia} of the {ideals_t} theorems of '
          f'`Becoming.Ideals` and {ib} of the {history_t} of `Becoming.HistoryIdeals` stand apart: support lemmas of the '
          'order (equivalences, the empty class, unpacked definitions, two laws of directed suprema), the hull\'s '
          'idempotence, whose case of runs is `Becoming.Horizon`\'s `Adheres.adheres`, and the classification of the '
          f'ideals of words with its lemmas, which `Stretches.classification` states for every process; their {roots} '
          'roots are in the '
          'apart register. The first build of the two modules had 115 of 139 apart; reading each law of ideals on the '
          'histories of a process (`Stretches`) joined the rest.'
          ' The apart roots of the superseded modules and of the bridge left the register with them', 'section 8.1 rerun')
ch = replace_line(ch, '| Origins, refutation and the remaining joins |',
                  '| Origins and refutation | The first origin step where the gated determination is decided; what a '
                  'finite stretch verifies, the open classes of histories, on the order whose closed classes '
                  '`Becoming.Ideals` states. | [every-origin-passes-the-gate](../results/records/every-origin-passes-the-gate.md), '
                  f'[{RECID}]({C_REC}) |', 'section 8.2 row')
ch = once(ch, '- `IdealWarrant` is joined with `CompletionRole` and `HistoryIdeals` as one core family of ideals under '
              'structural names; this is new Lean, open in §8.2 until it lands (board item A4-L).',
          '- `IdealWarrant` is joined with `CompletionRole` and `HistoryIdeals` as one core family of ideals under '
          'structural names: `Becoming.Ideals` and `Becoming.HistoryIdeals`, landed on 19 October 2026 (board item '
          f'A4-L, [{RECID}]({C_REC})). The three originals keep their paths and bytes and are read as instances '
          f'([IdealsCorrespondence]({C_CORR})).', 'section 8.4 bullet')
ch = once(ch, '**Double-negation elimination (DNE).** Asked of every process, the origin law with the gate a proposition '
              'is exactly ¬¬Q → Q for every Q (`origin_of_propositions_iff`).',
          '**Double-negation elimination (DNE).** Asked of every process, the origin law with the gate a proposition '
          'is exactly ¬¬Q → Q for every Q (`origin_of_propositions_iff`). So is each of these, asked of every process: '
          'that a refutable reading holds at every run adhering to it (`refutable_holds_iff`); that a refutable class of '
          'histories is closed, since not being refuted by any finite stretch is not belonging '
          '(`Stretches.refutable_closed_iff`); and that a closed class is refutable, since a history known not to lie '
          'within it does not thereby show the stretch at which it leaves (`Stretches.closed_refutable_iff`). Asked of '
          'every order and class, the last two are `Ideals.refutable_closed_iff` and `Ideals.closed_refutable_iff`.',
          'section 8.6 DNE')
ch = insert_after_line(ch, '- Naming the step from which a finite world rests (`lpo_of_finite_ends`).',
                       ['- Telling, of every history of `()`s cut at a Boolean sequence\'s first `true`, whether it '
                        'settles or goes on; the converse holds, so this is exactly LPO (`Stretches.cut_decided_iff_lpo`, '
                        '`HistoryIdeals.cut_decided_iff_lpo`): telling whether a history ends is deciding whether it '
                        'changes again.'], 'section 8.6 LPO')
spine = n(c['spine'])
ch = subn1(r'finds \d+ of the [\d,]+ spine theorems apart from both base families at the last rerun',
           f'finds {apart} of the {spine} spine theorems apart from both base families at the last rerun', ch,
           'section 9 connectivity')
ch = subn1(r'\d+ modules counting the root `Becoming`, and \d+ in the core closure with the foundation',
           f'{c["core"][0]} modules counting the root `Becoming`, and {c["closure"][0]} in the core closure with the '
           'foundation', ch, 'section 9 module counts')
ch = once(ch, 'together with assurance, segmentation, gating, viability, keeping, countdown, lasting and copying.',
          'together with assurance, segmentation, gating, viability, keeping, countdown, lasting and copying, and the '
          'ideals by which a history is read off its finite stretches.', 'section 9 L2')
start = ch.index('**The current receipt.**')
end = ch.index('Further facts about the receipt:', start)
para = ch[start:end]
old_rid = re.search(r'is run `([0-9TZ.]+)`', para).group(1)
para = para.replace(old_rid, RID)
para = subn1(r'It was checked with Lean 4\.29\.1 on main \S+ (?:\(.*?\) )?with .*? in the working tree\. It passed\.',
             f'It was checked with Lean 4.29.1 on main {BASE} ({AFTER}) with A4-L (`Becoming.Ideals` and '
             f'`Becoming.HistoryIdeals`, [study §{sec}]({STUDY_LINK})) in the working tree. It passed.', para,
             'receipt sentence')
rows = {
    '| Core modules (with the root `Becoming`, 0 theorems) |': f' {c["core"][0]} modules, {n(c["core"][1])} theorems |',
    '| Foundation modules |': f' {c["foundation"][0]} modules, {n(c["foundation"][1])} theorems |',
    '| Core closure |': f' {c["closure"][0]} modules, {n(c["closure"][1])} theorems |',
    '| Spine (the core; no bridge since the F3 sweep) |': f' {spine} theorems |',
    '| Audited spine declarations |': f' {n(c["audited"])} |',
    '| Modules in the compile order |': f' {c["compile"]} |',
    '| Generated `injEq` lemmas on `propext` |': f' {c["injeq"][0]} in the core closure |',
}
lines = para.split('\n')
for i, line in enumerate(lines):
    for head, tail in rows.items():
        if line.startswith(head):
            lines[i] = head + tail
    if line.startswith('| Inherited modules bound'):
        assert f'| {c["inherited"]} (' in line, line
for head in rows:
    assert sum(line.startswith(head) for line in lines) == 1, head
para = '\n'.join(lines)
ch = ch[:start] + para + ch[end:]
ch = subn1(r'That run reused [\d,]+ cached Lean steps from `~/\.cache/becoming-lean` and ran [\d,]+\.',
           f'That run reused {n(c["reused"])} cached Lean steps from `~/.cache/becoming-lean` and ran {n(c["ran"])}.',
           ch, 'section 9 steps')
ch = once(ch, '- Seventeen further instance modules connect in the same way,',
          '- Eighteen further instance modules connect in the same way,', 'section 9 instance count')
ch = once(ch, 'finite-branching lifting, and selection through a model of the options.',
          'finite-branching lifting, selection through a model of the options, and the ideals, completion and histories '
          'of the completion package.', 'section 9 instance list')
write(CHAPTER, ch)

# ------------------------------------------------------------------ reference
ref = read(REFERENCE)
IDEALS_ROW = (
    f'| L2 | [Becoming.Ideals]({C_IDEALS}) | A history read off its finite stretches (no premise; it imports nothing): '
    'the ideals of an order of stretches, no antisymmetry used, so the same history is two-way inclusion. A refutable '
    'reading of points holds, up to double negation, where a point adheres (`RefutableBy.not_not`); a class of ideals '
    'is closed exactly where it is the class within a lower set, its content (`closed_iff_lower`, `lower_iff_content`); '
    'a refutable class is closed, and a closed class refutable, each up to a step that, asked of every order and class, '
    'is exactly double-negation elimination (`Refutable.closed`, `Closed.refutable_iff`, `refutable_closed_iff`, '
    '`closed_refutable_iff`); the least closed hull (`hull_least`, `hull_unique`), avoidance (`avoids_unique`) and a '
    'lower set\'s own order (`lift_restrict`, `restrict_lift`); the completion: directed-complete (`idealComplete`), '
    'compact exactly at finite histories (`compact_iff_principal`), the unique continuous extension '
    '(`unique_continuous_extension`) and the completion of a compact basis (`unique_basis_representation`). '
    f'| {ideals_t} |')
HISTORY_ROW = (
    f'| L3 | [Becoming.HistoryIdeals]({C_HISTORY}) | Histories as ideals of their finite stretches (no premise). A run '
    'is the ideal of the stretches it passes through (`Run.stretches`, `Run.stretches_le_iff`), and the laws of '
    '`Becoming.Ideals` are read on the histories of every process (`Stretches`): Horizon\'s laws of what a finite '
    'history refutes as their case of runs (`Stretches.not_not`, `Stretches.refutable_adheres_iff`); adhering as the '
    'least closed class, with no double negation (`Stretches.adheres_iff_closed`); a reading holding every adhering run '
    'made of tests on stretches (`closed_iff_within_lower`); asked of every process, refutable and closed classes '
    'passing into each other exactly under double-negation elimination (`Stretches.refutable_closed_iff`, '
    '`Stretches.closed_refutable_iff`, `refutable_holds_iff`); avoidance, a lower set\'s own histories and the '
    'completion at runs (`Stretches.avoids_runs`, `Stretches.inherited_histories`, `Stretches.run_not_compact`, '
    '`Stretches.run_reading_unique`); a history that settles, or goes on with its stretches picked, is a finite history '
    'or a run (`Stretches.classification`), and telling which on cut histories is LPO '
    '(`Stretches.cut_decided_iff_lpo`). Words under prefix, histories and their order (`HistoryIdeals.history_le_iff`), '
    'and for the process of all sequences the runs\' histories (`Stretches.sequences_le_iff`); prefix-closed languages '
    'give closed classes (`HistoryIdeals.history_within_iff`), and the finite histories with the infinite ones of a '
    'property are not refutable where a sequence lies outside it (`HistoryIdeals.finiteOr_not_refutable`). '
    f'| {history_t} |')
CORR_ROW = (
    f'| [IdealsCorrespondence]({C_CORR}) | The instance in the completion package\'s ideals, completion and histories, '
    'with Lean 4.30.0-rc2, checked by `check_ideals_correspondence.py` with standard axioms only; `IdealWarrant`, '
    '`CompletionRole`, `PrefixSafety` and `HistoryIdeals` must match the package receipt. A poset\'s order is the core\'s '
    'order of stretches, its antisymmetry unused, and its ideals, classes, content and hull are the core\'s (`toCore`, '
    '`finiteRefutable_iff_refutable`, `scottClosed_iff_closed`, `scottHull_iff_hull`); W1\'s lower bases, W2\'s least '
    'hull and W2a\'s prohibitions follow with empty reports. W1\'s equivalence of finite refutability and Scott closure '
    '(`finiteRefutable_iff_scottClosed_by_core`) takes classical reasoning for the two steps the core shows are each '
    'exactly double-negation elimination; A2, A2a, A3 and the compact elements follow from the core\'s completion, the '
    'supplied antisymmetry turning its equivalences into equalities; A4\'s classification is the core\'s, with the '
    'decision of settling and the picks taken classically (`ideal_classification_by_core`). '
    f'{corr_e} of its {corr_d} declarations have empty reports; the rest name their classical and extensionality steps. '
    f'| {corr_t} |')
ref = insert_after_line(ref, '| L2 | [Becoming.Naturals](', [IDEALS_ROW], 'reference Ideals row')
ref = insert_after_line(ref, '| L3 | [Becoming.HistoryLanguages](', [HISTORY_ROW], 'reference HistoryIdeals row')
ref = insert_after_line(ref, '| [SelectionRelabelCorrespondence](', [CORR_ROW], 'reference instance row')
write(REFERENCE, ref)

# ------------------------------------------------------------------ Horizon's record
d = json.loads(read(HORIZON_RECORD))
assert d['next_delta']['en'].startswith('An independent review; IdealWarrant\'s order form on posets'), d['next_delta']
old_next = d['next_delta']['en']
d['next_delta'] = {
    'en': f'An independent review; what a finite history verifies, read on the order of stretches ({RECID}).',
    'zh': f'独立审查；有限历史所证实者，在片段之序上读出（{RECID}）。'}
OLD_EN = ('IdealWarrant generalizes it to posets and belongs to the general mathematical line Ren left outside the spine '
          'for now.')
OLD_ZH = 'IdealWarrant 在偏序上推广它，属 Ren 暂留脊柱外的一般数学线。'
d['correspondence']['en'] = once(d['correspondence']['en'], OLD_EN,
                                 'IdealWarrant generalizes it to posets; on 19 October 2026 its content was stated in '
                                 'the core (Becoming.Ideals, Becoming.HistoryIdeals), and this result is the case of '
                                 f'runs there ({RECID}).', 'record correspondence en')
d['correspondence']['zh'] = once(d['correspondence']['zh'], OLD_ZH,
                                 'IdealWarrant 在偏序上推广它；2026年10月19日其内容在核心中陈述（Becoming.Ideals、Becoming.HistoryIdeals），'
                                 f'本结果是那里的运行情形（{RECID}）。', 'record correspondence zh')
d['related'].append({'id': RECID, 'detail': {
    'en': 'There the laws of ideals of any order, read on the histories of every process: this record\'s laws are '
          'derived there as the case of runs, adhering is the least closed class, and each step between refutable and '
          'closed classes is, asked of every process, exactly double-negation elimination.',
    'zh': '那里是任意序的理想之律，读在每个过程的历史上：本记录的律在那里作为运行情形推出，附着是最小的闭类，可否证类与闭类之间的每一步，对每个过程要求时恰是双重否定消去。'}})
d['history'].append({
    'en': f'19 October 2026, A4-L (Becoming.Ideals, Becoming.HistoryIdeals; study section {sec}): IdealWarrant\'s order '
          'form is stated in the core, so next_delta drops it (former: "' + old_next + '") and the correspondence '
          'sentence on IdealWarrant now says where it is stated (former: "' + OLD_EN + '"). ' + RECID + ' is added as '
          'related. This record\'s claims are unchanged.',
    'zh': f'2026年10月19日，A4-L（Becoming.Ideals、Becoming.HistoryIdeals；研究第 {sec} 节）：IdealWarrant 的序形式已在核心中陈述，'
          '所以 next_delta 删去它，correspondence 中关于 IdealWarrant 的一句改为说明它在何处陈述（原文：“' + OLD_ZH + '”）。'
          f'加入 {RECID} 为相关。本记录的论断不变。'})
write(HORIZON_RECORD, json.dumps(d, ensure_ascii=False, indent=2) + '\n')

# ------------------------------------------------------------------ directive register and D45 (4)
t = read(DIRECTIVES)
t = once(t, 'IdealWarrant stays with the general mathematical line outside the spine.',
         'IdealWarrant stays with the general mathematical line outside the spine. Superseded on 19 October 2026 by '
         'D45 (4), on Ren\'s “integrate all, the theory is a whole, not stitched pieces, go ahead”: IdealWarrant\'s '
         'content is stated in the core with CompletionRole\'s and HistoryIdeals\' (`Becoming.Ideals`, '
         f'`Becoming.HistoryIdeals`, [record](../theories/becoming/results/records/{RECID}.md)); the three files keep '
         'their paths and bytes and are read as instances.', 'directive register')
write(DIRECTIVES, t)
t = read(CHOICES)
t = once(t, 'This is new Lean, board sub-item A4-L.',
         f'This is new Lean, board sub-item A4-L. Landed on 19 October 2026 ([record]({S_REC})): constructively, each '
         'direction of the equivalence holds up to a step that, asked of every order and class, is exactly '
         'double-negation elimination, and the core states it so; the original\'s classical statement is the instance '
         'with that step supplied. `Becoming.Refutable`\'s laws are derived as the case of runs.', 'choices D45 (4)')
write(CHOICES, t)
t = read(CHOICES_ZH)
t = once(t, '这是新的 Lean，即工作板子项 A4-L。',
         f'这是新的 Lean，即工作板子项 A4-L。2026年10月19日落地（[记录]({S_REC})）：构造地，等价的每个方向差一步，'
         '对每个序与类要求时这一步恰是双重否定消去，核心如此陈述；原文的经典陈述是补上这一步的实例。`Becoming.Refutable` 的律作为运行情形推出。',
         'choices D45 (4) zh')
write(CHOICES_ZH, t)
for path, text in OUT.items():
    (ROOT / path).write_text(text, encoding='utf-8')
    print('edited', path, file=sys.stderr)
print(sec)
