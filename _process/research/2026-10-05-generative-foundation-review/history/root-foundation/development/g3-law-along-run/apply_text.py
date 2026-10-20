#!/usr/bin/env python3
"""Apply G3's text: study section, chapter bullet, section 8.2 row, section 9 receipt and connectivity, and the
open items of projection-carrying-a-law: python3 -B apply_text.py NEW_RECEIPT APART MAIN_COMMIT

The old receipt id and the counts are read from the chapter; the new counts from the new receipt and its checker log
(checker-g3.log here). Each edit must match exactly once. Prints the study section number used. The package README
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
MECH = ROOT / 'theories/becoming/results/records/projection-carrying-a-law.json'
LOG = Path(__file__).resolve().parent / 'checker-g3.log'
LEAN = f'../../../{PKG}/Becoming/LawAlongRun.lean'
REC = '../results/records/a-law-through-a-projection-along-one-run.md'
REN = 'please see what else is there to do - keep pushing the frontier till finishing'
SRC_LINK = ('../../../../sources/15-codex-theory-conversations/2026-10-17-registration-dualist-vocabulary.md'
            '#rens-go-to-push-to-the-finish-18-october-2026')
STUDY_LINK = '../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


# Counts from the new receipt.
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
assert st['Becoming.LawAlongRun'] == 17, st['Becoming.LawAlongRun']

# Study.
s = STUDY.read_text()
n = max(int(m) for m in re.findall(r'^## (\d+)\. ', s, re.M)) + 1
ANCHOR = f'{n}-a-law-through-a-projection-along-one-run-g3'
SEC = f'''## {n}. A law through a projection along one run (G3)

```text
Result(s): a-law-through-a-projection-along-one-run (new); depends on projection-carrying-a-law,
           experiment-needs-return, process-and-frame-as-readings and finite-trace-transport
Delta: section 88 (Becoming.Mechanism) characterized a projection carrying a law over every configuration
       (carries_law_iff), and Becoming.Unfolding the law a whole history shows through the identity (exists_law_iff).
       Here, for any projection and up to any step of one run: some determined process on the description admits the
       run's steps so read exactly where they are consistent, the record read through the projection being the least
       candidate; failure persists; the identity case at every step is Unfolding's; a run can be consistent where the
       process has no law. And the bridge to GenerativeCore: the image is an exact finite-path projection
       (projection_exact_iff) exactly where configurations alike match each other's steps, which going alike does not give
Supplied premises / correspondence: none beyond the run, the projection and the step; no axiom
Evidence: Becoming.LawAlongRun, 17 theorems, empty axiom reports; core receipt `{NEW_R}`; connectivity check
          passes, {APART} apart of {fmt(spine)}, none in Becoming.LawAlongRun
Boundary: which projection an actual unfolding carries a law through; the instance with Becoming.Testing's
          registration as the projection; how many steps settle a law through a finite description; undetermined laws
```

Ren, 18 October 2026: "{REN}" ([source]({SRC_LINK})). The items are two of the open programme's row "Selection, causes and experiment" (§8.2): "a constructive criterion along one run for a projection carrying a law" and "the bridge to `GenerativeCore`'s exact projection". The record projection-carrying-a-law listed both in `does_not_show`.

**The question.** `carries_law_iff` ranges over every configuration of the process. An inquiry has one run. When does what one run did, read through a description, admit a law at that description; and when is a law at a description a faithful model of the process's finite paths?

**The move.** Read the run's steps before `t` through `π` as a process on the description: a move goes from `k` to `κ` where the run took it from a configuration projecting to `k` to one projecting to `κ` (`Run.recordThrough`). It admits the steps, and every process admitting them contains it, so it is the only candidate to check. For exactness, `Generative.projection_exact_iff` asks for step preservation and lifting from every configuration of a fibre; the image preserves steps by construction, so exactness is lifting, which is matching.

**What is proved** (`Becoming.LawAlongRun`).
- **The criterion along one run** (`Run.law_through_iff`): some determined process on the description admits the run's steps before `t` read through `π` exactly where any two of them from configurations alike under `π`, by the same move, reach configurations alike under `π` (`Run.ConsistentThrough`). The record is the least candidate (`Run.stepsThrough_record`, `Run.record_least`) and is determined exactly then (`Run.record_determined_iff`).
- **Failure persists** (`Run.ConsistentThrough.earlier`, `Run.no_law_later`): where no law through `π` admits the steps before `t`, none admits them before any later step.
- **Unfolding's history law is the identity instance** (`Run.consistent_id_iff`): consistency through the identity at every step is `Consistent`, so `exists_law_iff` is the criterion through the identity, at every step.
- **One run shows less than the process** (`Run.consistent_of_goAlike`, `Constant`): where configurations alike go alike every run is consistent; a run staying at one configuration of a process allowing every step is consistent through the identity, and the process does not go alike. `Switching.no_state_law` follows from the criterion along its run (`Switching.inconsistent`, `Switching.no_state_law_of_criterion`).
- **Exactness** (`MatchesThrough`, `image_exact_iff`, `exact_law_iff`): the image through `π` is exact for every finite path exactly where configurations alike under `π` match each other's steps up to `π`; some determined process on the description admits every step and lifts from every configuration of the fibre exactly where configurations alike go alike and match. In `Stuck`, through the description that tells nothing apart, the process goes alike and does not match (`Stuck.goAlike_not_matches`); `Coarse` is exact through its first bit (`Coarse.matching`, `Coarse.exact_law`).

**What this changes.** The law at a description has an inquiry form: one run tests it exactly as far as its own steps agree with each other, with nothing supplied, and what it refutes stays refuted. It also has a model form that is stronger: a law at a description gives step preservation (`FactorsThrough`, `trace_map`'s hypothesis) but not exact representation, which needs matching. The relation the record projection-carrying-a-law left unstated (going alike does not imply `projection_exact_iff`) is now a theorem with its missing half named.

*Reading* [AI reading]. A run is evidence of a law at a description exactly as far as its own steps agree; what it never visits it does not test, so a run can show a law the process lacks. Going alike and matching are the two halves of a mechanism stated exactly at a description: the first makes the description's future one, the second makes every member of a class able to do what any of them did.

**Not done.** The instance with `Becoming.Testing`'s registration (`Web.AlikeThroughUpTo`) as the projection; how many steps of a run settle whether a law through a finite description holds (with `Becoming.Recurrence`); undetermined and random laws along a run.

**Self-review.** The statements were read against the Lean.
- `Run.law_through_iff` and `Run.record_determined_iff` are near-definitional; the content is the least candidate, the persistence of failure, the identity instance and the separation from the process's law (`Constant`).
- `Run.consistent_id_iff` was added after finding that `Becoming.Unfolding` already stated the identity case (`Consistent`, `exists_law_iff`); the module imports Unfolding and states its relation rather than restating it.
- `image_exact_iff` goes through `Generative.projection_exact_iff`, whose axiom report in the core receipt is empty; `exact_law_iff` uses `carries_law_iff` and `image_determined_iff` from `Becoming.Mechanism`.
- `Becoming.Readout.law_through_iff` (a reduced readout carries a law exactly where configurations alike go alike, over every configuration) is a different statement in another namespace.
- Scratch build: 17 theorems, `unclean` empty, `with_axioms` empty; core receipt `{NEW_R}` passed ({core_n} core modules).

'''
s = once(s, '## Ren’s words quoted in passages that exist only in the Chinese edition',
         SEC + '## Ren’s words quoted in passages that exist only in the Chinese edition')
STUDY.write_text(s)

# Chapter.
c = C.read_text()
c = once(c, "what a pool's selections reach, and the gap for a pool's act: `Becoming.SelectionPool`.) ",
         "what a pool's selections reach, and the gap for a pool's act: `Becoming.SelectionPool`; a constructive criterion along "
         "one run for a projection carrying a law, and the bridge to `GenerativeCore`'s exact projection: "
         "`Becoming.LawAlongRun`.) ")
c = once(c, "a constructive criterion along one run for a projection carrying a law, the instance with "
            "`Becoming.Testing`'s registration as the projection, and the bridge to `GenerativeCore`'s exact projection;",
         "the instance of the criterion along one run with `Becoming.Testing`'s registration as the projection;")
c = once(c, '[projection-carrying-a-law](../results/records/projection-carrying-a-law.md), [causal-models-as-processes]',
         f'[projection-carrying-a-law](../results/records/projection-carrying-a-law.md), '
         f'[a-law-through-a-projection-along-one-run]({REC}), [causal-models-as-processes]')
BULLET_AFTER = '- A law through a projection, even a true one, is fixed by the record only where it has been taken'
lines = c.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith(BULLET_AFTER)]
assert len(idx) == 1, idx
BULLET = (f"- *Along one run, and exactly* ([Becoming.LawAlongRun]({LEAN}), "
          f"[a-law-through-a-projection-along-one-run]({REC})). Some determined process on the description admits a "
          "run's steps up to a step, read through π, exactly where any two of them from configurations alike under π, "
          "by the same move, reach configurations alike under π (`Run.law_through_iff`). The record read through π is "
          "the least candidate (`Run.record_least`), and once the criterion fails it fails from then on "
          "(`Run.no_law_later`). Through the identity at every step it is the law a history shows "
          "(`Run.consistent_id_iff`, `exists_law_iff`). A run can be consistent where the process does not go alike "
          "(`Constant`). A law at a description is not yet an exact model of finite paths: the image is exact in the "
          "sense of `Generative.projection_exact_iff` exactly where configurations alike match each other's steps up "
          "to π (`image_exact_iff`, `exact_law_iff`), and going alike does not give it (`Stuck`). "
          f"Study: [section {n}]({STUDY_LINK}#{ANCHOR}).")
lines[idx[0] + 1:idx[0] + 1] = [BULLET]
c = '\n'.join(lines)
start = c.index('**The current receipt.**')
end = c.index('| Generated `injEq` lemmas', start)
para = c[start:end]
OLD_R = re.search(r'is run `([0-9TZ.]+)`', para).group(1)
para = para.replace(OLD_R, NEW_R)
m = re.search(r'It was checked with Lean 4\.29\.1 on main \w+ \(.*?\) with .*? in the working tree', para, re.S)
para = para[:m.start()] + (f'It was checked with Lean 4.29.1 on main {MAIN} with G3 (`Becoming.LawAlongRun`, '
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
c = c[:last.end()] + (f' Rerun with G3 (receipt {NEW_R}), it counts {APART} of {fmt(spine)}, none in '
                      '`Becoming.LawAlongRun`.') + c[last.end():]
C.write_text(c)

# The Mechanism record's open items.
d = json.loads(MECH.read_text())
gone = [x for x in d['does_not_show'] if x['en'].startswith('The relation to GenerativeCore') or
        x['en'].startswith('The state-law criterion ranges over all configurations')]
assert len(gone) == 2, gone
for x in gone:
    d['does_not_show'].remove(x)
d['next_delta'] = {
    'en': "The instance with Becoming.Testing's registration as the projection; the state's law over long stretches where "
          'the rule changes slowly.',
    'zh': '以 Becoming.Testing 的识为投影的实例；规则缓慢改变时状态在长段上的规律。'}
d['related'].append({'id': 'a-law-through-a-projection-along-one-run', 'detail': {
    'en': 'There the criterion along one run (the record read through the projection is the least candidate, a law '
          'exactly where consistent) and the bridge to GenerativeCore: the image is exact exactly where configurations '
          'alike match each other\'s steps, which going alike does not give.',
    'zh': '那里是沿一个运行的判据（经投影读出的记录是最小候选，恰在一致处是规律）与到 GenerativeCore 的桥接：像恰在相同的配置相互匹配对方的步之处是精确的，'
          '同去不给出它。'}})
d['history'].append({
    'en': '18 October 2026, G3 (Becoming.LawAlongRun): the open items "the relation to GenerativeCore\'s exact projection '
          '(projection_exact_iff) is not stated" and "the iff along one run is not stated" are removed from does_not_show '
          'and next_delta, since a-law-through-a-projection-along-one-run states both; that record is added as related. '
          "This record's claims are unchanged.",
    'zh': '2026年10月18日，G3（Becoming.LawAlongRun）：因 a-law-through-a-projection-along-one-run 陈述了两者，从 does_not_show 与 '
          'next_delta 删去开放项“与 GenerativeCore 精确投影（projection_exact_iff）的关系没有陈述”与“沿一个运行的充要条件没有陈述”；'
          '加入该记录为相关。本记录的论断不变。'})
MECH.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(n)
