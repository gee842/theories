#!/usr/bin/env python3
"""Apply G4's text: study section, chapter bullet, section 8.2 row, section 9 receipt and connectivity, and the open
items of a-law-through-a-projection-along-one-run, projection-carrying-a-law and testing-within-registration:
python3 -B apply_text.py NEW_RECEIPT APART MAIN_COMMIT

The old receipt id and the counts are read from the chapter; the new counts from the new receipt and its checker log
(checker-g4.log here). Each edit must match exactly once. Prints the study section number used. The package README
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
LOG = Path(__file__).resolve().parent / 'checker-g4.log'
LEAN = f'../../../{PKG}/Becoming/LawThroughCoupling.lean'
REC = '../results/records/a-law-through-coupling-along-one-run.md'
REN = ("Yes: claim G4 on the board — the criterion along one run with Becoming.Testing's registration as the "
       "projection — and prove it in scratch while the queue runs.")
SRC_LINK = ('../../../../sources/15-codex-theory-conversations/2026-10-17-registration-dualist-vocabulary.md'
            '#rens-go-for-g4-18-october-2026')
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
assert st['Becoming.LawThroughCoupling'] == 18, st['Becoming.LawThroughCoupling']

# Study.
s = STUDY.read_text()
n = max(int(m) for m in re.findall(r'^## (\d+)\. ', s, re.M)) + 1
ANCHOR = f'{n}-a-law-through-what-a-formation-couples-into-along-one-run-g4'
SEC = f'''## {n}. A law through what a formation couples into, along one run (G4)

```text
Result(s): a-law-through-coupling-along-one-run (new); depends on a-law-through-a-projection-along-one-run,
           testing-within-registration, determinacy-up-to-likeness, becoming-dependence-dynamics and
           becoming-renewal-reading
Delta: section 181 (Becoming.LawAlongRun) stated the criterion along one run through a projection. Coupling
       (Web.AlikeThrough, formerly registration) is a relation, and an equality of what is coupled would need propext.
       Here the criterion up to an equivalence (any process going alike under it, GoAlikeUnder through the identity),
       with the record read under it as the witness, failure persisting, and the projection criterion as the instance
       with equal projections; with fixed conditions a formation's coupling at a configuration is such an equivalence,
       exactly Web.AlikeThrough on the runs read through the conditions; a witness where an uncoupled level decides the
       next coupling of a determined process, and coupling into it restores the law
Supplied premises / correspondence: an equivalence for the backward direction; fixed conditions for coupling; no axiom
Evidence: Becoming.LawThroughCoupling, 18 theorems, empty axiom reports; core receipt `{NEW_R}`; connectivity check
          passes, {APART} apart of {fmt(spine)}, none in Becoming.LawThroughCoupling
Boundary: coupling that changes along the run (Dependence rather than fixed Conditions); the up-to form over histories
          (Web.AlikeThroughUpTo), which compares two histories; which formation's coupling carries a law along an
          actual unfolding; how many steps settle it
```

Ren, 18 October 2026: "{REN}" ([source]({SRC_LINK})). The item is the open programme's "the instance of the criterion along one run with `Becoming.Testing`'s registration as the projection" (§8.2, "Selection, causes and experiment"), which G3 left in its record's `does_not_show`.

**The question.** Along one course, does what a formation couples into carry a law: does what it couples into now, with the move, fix what it couples into next?

**The move.** Coupling is not a projection: `Web.AlikeThrough` relates two level histories at a step, through an equivalence of admissions and equalities of observed levels. Turning it into a description type would need equal propositions, so `propext`. So G3's criterion is stated up to an equivalence `E`: the law is any process going alike under `E` (`GoAlikeUnder Q id E` of `Becoming.Likeness`), and the witness is the record read under `E`, a move going from `x` to `y` where the run took it from a configuration related to `x` to one related to `y`.

**What is proved** (`Becoming.LawThroughCoupling`).
- **The criterion up to a relation** (`Run.law_under_iff`): where `E` is an equivalence, some process going alike under `E` admits the run's steps before `t` exactly where any two of them from configurations related by `E`, by the same move, reach configurations related by `E` (`Run.ConsistentUnder`). The record read under `E` is the witness (`Run.recordUnder_steps`, `Run.recordUnder_goAlike`); the forward direction needs no equivalence. Failure persists (`Run.ConsistentUnder.earlier`, `Run.no_law_under_later`); a process going alike under `E` makes every run consistent (`Run.consistentUnder_of_goAlikeUnder`). Through equal projections it is G3's criterion (`Run.consistentUnder_eq_iff`, by definition).
- **Coupling as the relation** (`Conditions.AlikeAt`, `Conditions.alikeAt_equivalence`): with fixed conditions, two configurations are alike in what `g` couples into when their levels admit `g` alike and the conditions it observes stand alike. It is exactly `Web.AlikeThrough` on the runs read through the conditions, between two runs at one step (`Conditions.alikeThrough_iff`) and between two steps of one run (`Conditions.alikeAt_iff_alikeThrough`), both by definition. So `Run.law_through_coupling_iff`.
- **An uncoupled level decides** (`Unseen`): the process (two levels; each step moves the second into the first and empties the second) is determined (`Unseen.determined`). A formation depending on the first level with need 1 and observing nothing couples the run's first two steps, `(1, 1)` and `(1, 0)`, alike, and by the same move they lead to `(1, 0)`, which admits it, and `(0, 0)`, which does not (`Unseen.inconsistent`, `Unseen.no_law`). Observing the second level, the same run is consistent at every step (`Unseen.consistent_observing`).

**What this changes.** `Becoming.Testing` said a difference beyond what couples in is not tested. Along one course this has a law form: what a formation couples into carries a law exactly as far as the occasions it couples alike went alike, and an uncoupled difference can break that law however determined the unfolding is. Observing more can create a law along a course; the criterion is not monotone in what is observed, since a finer relation asks more of the ends as well as less of the starts.

*Reading* [AI reading]. A formation's own course is evidence of a law at its coupling exactly as far as it agrees with itself; where the next coupling is decided by what it does not couple into, it meets no law at its coupling, only a record. The reading does not say which formations couple into enough.

**Not done.** Coupling that changes along the run (`Dependence` rather than fixed `Conditions`; the relation then is not an equivalence in general); the up-to form over histories (`Web.AlikeThroughUpTo`), which relates two histories and would need configurations that keep their history; how many steps settle whether a law at a finite coupling holds.

**Self-review.** The statements were read against the Lean.
- The bridges to `Web.AlikeThrough` are by `Iff.rfl`: `Conditions.along` of `Becoming.Renewal` gives a `RelationalRenewal.Unfolding`, so the bridge is stated on `K.dependence.along r`, a `Web` of `Becoming.World`, whose requirements at every step are the fixed ones.
- `Run.consistentUnder_eq_iff` is definitional: G3's `ConsistentThrough` is `ConsistentUnder` with equal projections; the delta is the relation form, not a new criterion through projections.
- A first draft used `.elim` on a term of `thresholdOnly`'s type and an underscore motive; both were fixed before the first build. The scratch build reported one unused binder, fixed.
- Scratch build: 18 theorems, `unclean` empty, `with_axioms` empty; core receipt `{NEW_R}` passed ({core_n} core modules).

'''
s = once(s, '## Ren’s words quoted in passages that exist only in the Chinese edition',
         SEC + '## Ren’s words quoted in passages that exist only in the Chinese edition')
STUDY.write_text(s)

# Chapter.
c = C.read_text()
c = once(c, "and the bridge to `GenerativeCore`'s exact projection: `Becoming.LawAlongRun`; ",
         "and the bridge to `GenerativeCore`'s exact projection: `Becoming.LawAlongRun`; the criterion along one run "
         "through what a formation couples into: `Becoming.LawThroughCoupling`; ")
c = once(c, "the instance of the criterion along one run with `Becoming.Testing`'s registration as the projection; ",
         "the criterion through coupling that changes along the run; ")
c = once(c, '[a-law-through-a-projection-along-one-run](../results/records/a-law-through-a-projection-along-one-run.md), ',
         '[a-law-through-a-projection-along-one-run](../results/records/a-law-through-a-projection-along-one-run.md), '
         f'[a-law-through-coupling-along-one-run]({REC}), ')
lines = c.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('- *Along one run, and exactly*')]
assert len(idx) == 1, idx
BULLET = (f"- *Through what a formation couples into* ([Becoming.LawThroughCoupling]({LEAN}), "
          f"[a-law-through-coupling-along-one-run]({REC})). Coupling (`Web.AlikeThrough`) is a relation, not a "
          "projection, so the criterion is stated up to an equivalence: some process going alike under it admits a "
          "run's steps up to a step exactly where any two of them alike under it, by the same move, end alike "
          "(`Run.law_under_iff`), the record read under it being the witness; through equal projections this is the "
          "criterion above (`Run.consistentUnder_eq_iff`). With fixed conditions, what a formation couples into at a "
          "configuration is such an equivalence, exactly `Web.AlikeThrough` on the runs read through the conditions "
          "(`Conditions.alikeThrough_iff`), so `Run.law_through_coupling_iff`. A level the formation does not couple "
          "into can decide what it next couples into, however determined the process is, and then no law holds at "
          "its coupling along the run (`Unseen.no_law`); coupling into that level restores it "
          f"(`Unseen.consistent_observing`). Study: [section {n}]({STUDY_LINK}#{ANCHOR}).")
lines[idx[0] + 1:idx[0] + 1] = [BULLET]
c = '\n'.join(lines)
start = c.index('**The current receipt.**')
end = c.index('| Generated `injEq` lemmas', start)
para = c[start:end]
OLD_R = re.search(r'is run `([0-9TZ.]+)`', para).group(1)
para = para.replace(OLD_R, NEW_R)
m = re.search(r'It was checked with Lean 4\.29\.1 on main \w+ \(.*?\) with .*? in the working tree', para, re.S)
para = para[:m.start()] + (f'It was checked with Lean 4.29.1 on main {MAIN} with G4 (`Becoming.LawThroughCoupling`, '
                           f'[study §{n}]({STUDY_LINK}#{ANCHOR})) in the working tree') + para[m.end():]
for label, value in [
        ('Core modules (with the root `Becoming`, 0 theorems)', f'{core_n} modules, {fmt(core_t)} theorems'),
        ('Core closure', f'{clos_n} modules, {fmt(core_t + found_t)} theorems'),
        ('Spine (core and bridge)', f'{fmt(spine)} theorems'),
        ('Audited spine declarations', fmt(audits)),
        ('Modules in the compile order', str(order))]:
    para, k = re.subn(r'(\| ' + re.escape(label) + r' \| )[^|]*( \|)', lambda mm: mm.group(1) + value + mm.group(2), para)
    assert k == 1, label
c = c[:start] + para + c[end:]
last = list(re.finditer(r'Rerun with \w+ \(receipt [0-9TZ.]+\), it counts \d+ of [\d,]+, none in `[^`]+`\.', c))[-1]
c = c[:last.end()] + (f' Rerun with G4 (receipt {NEW_R}), it counts {APART} of {fmt(spine)}, none in '
                      '`Becoming.LawThroughCoupling`.') + c[last.end():]
C.write_text(c)

# G3's record.
p = RECS / 'a-law-through-a-projection-along-one-run.json'
d = json.loads(p.read_text())
gone = [x for x in d['does_not_show'] if x['en'].startswith("The instance with Becoming.Testing's registration")]
assert len(gone) == 1
d['does_not_show'].remove(gone[0])
d['next_delta'] = {
    'en': 'How many steps of a run settle whether a law through a finite description holds (with Becoming.Recurrence); '
          'an independent review.',
    'zh': '一个运行要多少步才定下经有限描述的规律是否成立（与 Becoming.Recurrence 一起）；独立审查。'}
d['related'].append({'id': 'a-law-through-coupling-along-one-run', 'detail': {
    'en': 'There the criterion up to an equivalence, of which this one is the instance with equal projections, and its '
          "instance with a formation's coupling (Web.AlikeThrough) as the relation.",
    'zh': '那里是到等价关系为止的判据，本判据是其以相等投影的实例；以及以形成的耦合（Web.AlikeThrough）为关系的实例。'}})
d['history'].append({
    'en': '18 October 2026, G4 (Becoming.LawThroughCoupling): the open item "the instance with Becoming.Testing\'s '
          'registration as the projection is not stated" is removed from does_not_show and next_delta, since '
          'a-law-through-coupling-along-one-run states it, up to a relation because coupling is not a projection; that '
          "record is added as related. This record's claims are unchanged.",
    'zh': '2026年10月18日，G4（Becoming.LawThroughCoupling）：因 a-law-through-coupling-along-one-run 陈述了它（因耦合不是投影，到关系为止），'
          '从 does_not_show 与 next_delta 删去开放项“以 Becoming.Testing 的识为投影的实例没有陈述”；加入该记录为相关。本记录的论断不变。'})
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')

# The Mechanism record's next step.
p = RECS / 'projection-carrying-a-law.json'
d = json.loads(p.read_text())
assert d['next_delta']['en'].startswith("The instance with Becoming.Testing's registration as the projection; "), d['next_delta']
d['next_delta'] = {'en': "The state's law over long stretches where the rule changes slowly.",
                   'zh': '规则缓慢改变时状态在长段上的规律。'}
d['history'].append({
    'en': '18 October 2026, G4 (Becoming.LawThroughCoupling): "the instance with Becoming.Testing\'s registration as the '
          'projection" is removed from next_delta, since a-law-through-coupling-along-one-run states it along one run. '
          "This record's claims are unchanged.",
    'zh': '2026年10月18日，G4（Becoming.LawThroughCoupling）：因 a-law-through-coupling-along-one-run 沿一个运行陈述了它，从 next_delta 删去'
          '“以 Becoming.Testing 的识为投影的实例”。本记录的论断不变。'})
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')

# Testing's record: related.
p = RECS / 'testing-within-registration.json'
d = json.loads(p.read_text())
d['related'].append({'id': 'a-law-through-coupling-along-one-run', 'detail': {
    'en': 'There what a formation couples into carries a law along one run exactly where the occasions it couples alike '
          'went alike; an uncoupled level can decide its next coupling (Unseen): the boundary here, read along a course.',
    'zh': '那里形成所耦合者沿一个运行承载规律，恰在它耦合相同的场合同去之处；一个未耦合的水平可以决定它下一步耦合什么（Unseen）：这里的边界沿进程读出。'}})
d['history'].append({
    'en': '18 October 2026, G4 (Becoming.LawThroughCoupling): a-law-through-coupling-along-one-run added as related. '
          "This record's claims are unchanged.",
    'zh': '2026年10月18日，G4（Becoming.LawThroughCoupling）：加入 a-law-through-coupling-along-one-run 为相关。本记录的论断不变。'})
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(n)
