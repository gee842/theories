#!/usr/bin/env python3
"""Apply G5's text: study section, chapter bullet, section 8.2 row, section 9 receipt and connectivity, the open items
of a-law-through-coupling-along-one-run and a related entry in becoming-dependence-dynamics:
python3 -B apply_text.py NEW_RECEIPT APART MAIN_COMMIT

The old receipt id and the counts are read from the chapter; the new counts from the new receipt and its checker log
(checker-g5.log here). Each edit must match exactly once. Prints the study section number used. The package README
row is written by integrate.py."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
NEW_R, APART, MAIN = sys.argv[1], sys.argv[2], sys.argv[3]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
STUDY = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
C = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
RECS = ROOT / 'theories/becoming/results/records'
LOG = Path(__file__).resolve().parent / 'checker-g5.log'
LEAN = f'../../../{PKG}/Becoming/LawThroughChangingCoupling.lean'
REC = '../results/records/a-law-through-changing-coupling-along-one-run.md'
REN = "you have permission now, please see what else is there to do - keep pushing the frontier till finishing"
SRC_LINK = ('../../../../sources/15-codex-theory-conversations/2026-10-17-registration-dualist-vocabulary.md'
            '#rens-go-to-push-to-the-finish-18-october-2026')
STUDY_LINK = '../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


r = json.loads((ROOT / PKG / 'becoming-checks' / NEW_R / 'verification.json').read_text())
assert r['status'] == 'passed'
log = LOG.read_text()
log_d = json.loads(log[log.index('{'):log.rindex('}') + 1])
st = log_d['spine_theorems']
core_n, core_t = len(r['core_modules']), sum(st.get(m, 0) for m in r['core_modules'])
clos_n = len(r['core_closure'])
found_t = 74
spine = sum(st.values())
audits = log_d['spine_declaration_audits']
order = len(r['compile_order'])
fmt = lambda n: f'{n:,}'
assert st['Becoming.LawThroughChangingCoupling'] == 25, st['Becoming.LawThroughChangingCoupling']

# Source: Ren's 19 October "continue", verbatim.
SOURCE = ROOT / 'sources/15-codex-theory-conversations/2026-10-17-registration-dualist-vocabulary.md'
src = SOURCE.read_text()
if "## Ren's continue (19 October 2026)" not in src:
    src = src.rstrip('\n') + """

## Ren's continue (19 October 2026)

After G4 (`Becoming.LawThroughCoupling`) landed and the assistant reported it, Ren wrote:

> continue

The assistant's reading, which Ren may revise: the standing go of 18 October continues. The next item taken is the criterion through coupling that changes along the run (board item G5), which G4 left open.
"""
    SOURCE.write_text(src)

# Study.
s = STUDY.read_text()
n = max(int(m) for m in re.findall(r'^## (\d+)\. ', s, re.M)) + 1
g4 = re.search(r'^## (\d+)\. A law through what a formation couples into, along one run \(G4\)', s, re.M).group(1)
ANCHOR = f'{n}-a-law-through-coupling-that-changes-along-the-run-g5'
SEC = f'''## {n}. A law through coupling that changes along the run (G5)

```text
Result(s): a-law-through-changing-coupling-along-one-run (new); depends on a-law-through-coupling-along-one-run,
           testing-within-registration, becoming-dependence-dynamics and becoming-renewal-reading
Delta: section {g4} (Becoming.LawThroughCoupling) stated the criterion along one run through a formation's coupling with
       fixed conditions. Here dependences are read off the configuration (Dependence), so what a formation depends on
       can form and dissolve along the run: its coupling at each occasion, through the dependence it then has, is an
       equivalence and carries the criterion; fixed conditions are the instance; Web.AlikeThrough read at one step is
       the coupling with that step's dependence held fixed; where the dependences do not change along the run the two
       criteria agree; on one determined process a dissolving dependence carries a law the coupling fixed at the start
       lacks, and a forming one breaks a law it has
Supplied premises / correspondence: dependences read off the configuration; what a formation observes is fixed; no axiom
Evidence: Becoming.LawThroughChangingCoupling, 25 theorems, empty axiom reports; core receipt `{NEW_R}`; connectivity
          check passes, {APART} apart of {fmt(spine)}, none in Becoming.LawThroughChangingCoupling
Boundary: observation that changes along the run; which dependences an actual formation forms along an unfolding; how
          many steps settle whether a law at the coupling holds
```

Ren, 18 October 2026: "{REN}" ([source]({SRC_LINK})); on 19 October Ren wrote "continue". The AI chose the item: the open programme's "the criterion through coupling that changes along the run" (§8.2, "Selection, causes and experiment"), which G4 left.

**The question.** Along one course in which what a formation depends on forms and dissolves, does what it couples into carry a law, and is that the law at its coupling read at one moment?

**The move.** `Dependence` (of `Becoming.Dependence`) reads requirements and needs off the configuration. Each configuration is read through the dependence the formation has there: two are alike in what `g` couples into when the levels at each admit `g` through `g`'s dependence there alike, and the conditions it observes stand alike (`Dependence.AlikeAt`). Because the dependence is a function of the configuration, this is still a relation on configurations, and an equivalence.

**What is proved** (`Becoming.LawThroughChangingCoupling`).
- **The criterion** (`Run.law_through_dependence_iff`): from `Dependence.alikeAt_equivalence` and G4's `Run.law_under_iff`. Fixed conditions are the instance (`Dependence.conditions_alikeAt_iff`, by definition; along a run, `Run.consistent_conditions_iff`). Along a run it is the relation between two steps each read through its own step's dependence (`Web.AlikeAcross`, `Dependence.alikeAt_iff_alikeAcross`, by definition).
- **Testing's coupling fixes a step's dependence** (`Dependence.alikeThrough_iff_fixedAt`, by definition): `Web.AlikeThrough` at step `t`, between the levels standing at two steps of the run, is the coupling through the conditions fixed at step `t`'s configuration (`Dependence.fixedAt`). Where the dependence at the two steps compared is the one at `t`, it is the changing coupling (`Web.alikeAcross_iff_alikeThrough`).
- **Unchanged dependences give one criterion**: consistency reads a relation only on the run's configurations up to `t` (`Run.consistentUnder_congr`); so where `g`'s dependences up to `t` are those of step `k` (`Dependence.Unchanged`), the run is consistent under the changing coupling exactly where it is under the coupling fixed at step `k` (`Run.consistent_unchanged_iff`).
- **Where dependences form or dissolve, neither gives the other** (`Changing`): one level rising by one each step, a determined process. Depending on the level with need 2 only at level 0 (`Changing.dissolving`, which dissolves across the first step, `Changing.dissolves`), the run is consistent at every step under the changing coupling (`Changing.dissolving_consistent`); with the dependence of level 0 held fixed, levels 0 and 1 are coupled alike and lead to 1 and 2, coupled apart (`Changing.dissolving_fixed_inconsistent`, `Changing.dissolving_fixed_no_law`). Depending on it with need 2 from level 1 on (`Changing.forming`, formed across the first step, `Changing.forms`), the coupling fixed at the start depends on nothing and is consistent at every step (`Changing.forming_fixed_consistent`), while under the changing coupling levels 0 and 2 are coupled alike and lead to 1 and 3, coupled apart (`Changing.forming_inconsistent`, `Changing.forming_no_law`).

**What this changes.** The study of G4 (section {g4}) said that with changing coupling "the relation then is not an equivalence in general". Read through the dependence each configuration carries, it is one, and the criterion holds unchanged; that note is revised here. What changes is which relation is meant: the coupling a formation has on each occasion, or the coupling of one moment held over the course. They agree where nothing it depends on changes, and otherwise neither's law gives the other's.

*Reading* [AI reading]. A law at a formation's coupling along a course is a law at the coupling it has on each occasion. Reading the course through the dependence of one moment can find a law its own coupling does not carry, or miss one it does. The reading does not say which dependences an actual formation forms.

**Not done.** Observation that changes along the run (here what a formation observes is fixed, as in `Becoming.Testing`); a dependence that is not read off the configuration (a `Web` whose requirements change with the step alone; it is read through configurations that keep the step, as the clocked runs of other modules do); how many steps settle whether a law at the coupling holds.

**Self-review.** The statements were read against the Lean.
- The new criterion is G4's applied to a new equivalence; the delta is the relation read through changing dependence, its bridges and the comparison with the fixed coupling, not a new criterion.
- `Run.consistent_unchanged_iff` takes the reference step `k` arbitrary, not necessarily before `t`; the hypothesis is that every step up to `t` has `k`'s dependence for `g`.
- The first scratch build reported `propext` in three witness theorems, through `Nat.succ_ne_zero`; replaced by `Nat.noConfusion`, the second build had `with_axioms` empty. The first landing run's connectivity check found `Dependence.conditions_alikeAt_iff` apart (its statement is on neither base family); its use along a run is now stated, `Run.consistent_conditions_iff`, and the core checker was rerun: 25 theorems, `unclean` empty, `with_axioms` empty; core receipt `{NEW_R}` passed ({core_n} core modules).

'''
s = once(s, '## Ren’s words quoted in passages that exist only in the Chinese edition',
         SEC + '## Ren’s words quoted in passages that exist only in the Chinese edition')
STUDY.write_text(s)

# Chapter.
c = C.read_text()
c = once(c, "the criterion along one run through what a formation couples into: `Becoming.LawThroughCoupling`; ",
         "the criterion along one run through what a formation couples into: `Becoming.LawThroughCoupling`; "
         "the criterion through coupling that changes along the run: `Becoming.LawThroughChangingCoupling`; ")
c = once(c, "the criterion through coupling that changes along the run; ",
         "the criterion through observation that changes along the run; ")
c = once(c, '[a-law-through-coupling-along-one-run](../results/records/a-law-through-coupling-along-one-run.md), ',
         '[a-law-through-coupling-along-one-run](../results/records/a-law-through-coupling-along-one-run.md), '
         f'[a-law-through-changing-coupling-along-one-run]({REC}), ')
lines = c.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('- *Through what a formation couples into*')]
assert len(idx) == 1, idx
BULLET = (f"- *Through coupling that changes* ([Becoming.LawThroughChangingCoupling]({LEAN}), "
          f"[a-law-through-changing-coupling-along-one-run]({REC})). Where what a formation depends on is read off the "
          "configuration (`Dependence`), it can form and dissolve along the run. Read on each occasion through the "
          "dependence the formation then has, what it couples into is still an equivalence, so the criterion above "
          "holds through it (`Run.law_through_dependence_iff`). `Web.AlikeThrough` read at one step is the coupling "
          "with that step's dependence held fixed (`Dependence.alikeThrough_iff_fixedAt`); where the formation's "
          "dependences do not change along the run, the two criteria agree (`Run.consistent_unchanged_iff`). Where they "
          "form or dissolve, neither gives the other: on one determined process a dissolving dependence carries a law "
          "the coupling fixed at the start lacks (`Changing.dissolving_consistent`, "
          "`Changing.dissolving_fixed_inconsistent`), and a forming one breaks a law it has "
          "(`Changing.forming_fixed_consistent`, `Changing.forming_inconsistent`). "
          f"Study: [section {n}]({STUDY_LINK}#{ANCHOR}).")
lines[idx[0] + 1:idx[0] + 1] = [BULLET]
c = '\n'.join(lines)
start = c.index('**The current receipt.**')
end = c.index('| Generated `injEq` lemmas', start)
para = c[start:end]
OLD_R = re.search(r'is run `([0-9TZ.]+)`', para).group(1)
para = para.replace(OLD_R, NEW_R)
m = re.search(r'It was checked with Lean 4\.29\.1 on main \w+ \(.*?\) with .*? in the working tree', para, re.S)
para = para[:m.start()] + (f'It was checked with Lean 4.29.1 on main {MAIN} with G5 (`Becoming.LawThroughChangingCoupling`, '
                           f'[study §{n}]({STUDY_LINK}#{ANCHOR})) in the working tree') + para[m.end():]
for label, value in [
        ('Core modules (with the root `Becoming`, 0 theorems)', f'{core_n} modules, {fmt(core_t)} theorems'),
        ('Core closure', f'{clos_n} modules, {fmt(core_t + found_t)} theorems'),
        ('Spine (the core; no bridge since the F3 sweep)', f'{fmt(spine)} theorems'),
        ('Audited spine declarations', fmt(audits)),
        ('Modules in the compile order', str(order))]:
    para, k = re.subn(r'(\| ' + re.escape(label) + r' \| )[^|]*( \|)', lambda mm: mm.group(1) + value + mm.group(2), para)
    assert k == 1, label
c = c[:start] + para + c[end:]
last = list(re.finditer(r'Rerun with \w+ \(receipt [0-9TZ.]+\), it counts \d+ of [\d,]+, none in `[^`]+`\.', c))[-1]
c = c[:last.end()] + (f' Rerun with G5 (receipt {NEW_R}), it counts {APART} of {fmt(spine)}, none in '
                      '`Becoming.LawThroughChangingCoupling`.') + c[last.end():]
C.write_text(c)

# G4's record.
p = RECS / 'a-law-through-coupling-along-one-run.json'
d = json.loads(p.read_text())
gone = [x for x in d['does_not_show'] if x['en'].startswith('Coupling that changes along the run')]
assert len(gone) == 1
d['does_not_show'].remove(gone[0])
assert d['next_delta']['en'].startswith('Coupling that changes along the run; '), d['next_delta']
d['next_delta'] = {
    'en': 'How many steps settle whether a law at a finite coupling holds; observation that changes along the run; an '
          'independent review.',
    'zh': '要多少步才定下有限耦合上的规律是否成立；沿运行改变的观察；独立审查。'}
d['related'].append({'id': 'a-law-through-changing-coupling-along-one-run', 'detail': {
    'en': 'There the criterion through coupling that changes along the run, of which fixed conditions are the instance; '
          'where dependences form or dissolve, the law at the coupling fixed at the start and the law at the changing '
          'coupling neither gives the other.',
    'zh': '那里是经沿运行改变的耦合的判据，固定条件是其实例；依赖形成或消散之处，开始时固定的耦合上的规律与改变的耦合上的规律互不给出。'}})
d['history'].append({
    'en': '19 October 2026, G5 (Becoming.LawThroughChangingCoupling): the open item "coupling that changes along the run '
          '(Dependence rather than fixed Conditions), where the relation need not be an equivalence, is not treated" is '
          'removed from does_not_show and next_delta, since a-law-through-changing-coupling-along-one-run states it. Its '
          'clause "where the relation need not be an equivalence" was wrong for the coupling read through the dependence '
          "each configuration carries, which is an equivalence (Dependence.alikeAt_equivalence). That record is added as "
          "related. This record's claims are unchanged.",
    'zh': '2026年10月19日，G5（Becoming.LawThroughChangingCoupling）：因 a-law-through-changing-coupling-along-one-run 陈述了它，从 '
          'does_not_show 与 next_delta 删去开放项“沿运行改变的耦合（Dependence 而非固定的 Conditions），其关系不必是等价关系，没有处理”。'
          '其中“其关系不必是等价关系”一语，对经每个配置所带依赖读出的耦合是错的，那是等价关系（Dependence.alikeAt_equivalence）。加入该记录为相关。'
          '本记录的论断不变。'})
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')

# Dependence's record: related.
p = RECS / 'becoming-dependence-dynamics.json'
d = json.loads(p.read_text())
d['related'] = d.get('related', [])
d['related'].append({'id': 'a-law-through-changing-coupling-along-one-run', 'detail': {
    'en': 'There dependences read off the configuration give what a formation couples into on each occasion; where they '
          'form or dissolve along a run, the law at that coupling and the law at the coupling of one moment neither gives '
          'the other.',
    'zh': '那里从配置读出的依赖给出形成在每个场合所耦合者；它们沿运行形成或消散之处，该耦合上的规律与某一时刻耦合上的规律互不给出。'}})
d['history'].append({
    'en': '19 October 2026, G5 (Becoming.LawThroughChangingCoupling): a-law-through-changing-coupling-along-one-run added '
          "as related. This record's claims are unchanged.",
    'zh': '2026年10月19日，G5（Becoming.LawThroughChangingCoupling）：加入 a-law-through-changing-coupling-along-one-run 为相关。'
          '本记录的论断不变。'})
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(n)
