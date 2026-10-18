#!/usr/bin/env python3
"""Apply G1's text: study section, chapter bullet, section 8.2 row, section 9 receipt, package README row, and the
selection record's open item: python3 -B apply_text.py OLD_RECEIPT NEW_RECEIPT. Each edit must match exactly once.
Prints the study section number used."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
OLD_R, NEW_R = sys.argv[1], sys.argv[2]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
STUDY = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
C = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
README = ROOT / PKG / 'README.md'
SEL = ROOT / 'theories/becoming/results/records/selection-through-registration.json'
LEAN = f'../../../{PKG}/Becoming/SelectionGap.lean'
REC = '../results/records/the-gap-for-ones-own-act.md'
REN = 'please see what else is there to do - keep pushing the frontier till finishing'
SRC_LINK = '../../../../sources/15-codex-theory-conversations/2026-10-17-registration-dualist-vocabulary.md#rens-go-to-push-to-the-finish-18-october-2026'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


# Study.
s = STUDY.read_text()
n = max(int(m) for m in re.findall(r'^## (\d+)\. ', s, re.M)) + 1
SEC = f'''## {n}. The gap for one's own act (G1)

```text
Result(s): the-gap-for-ones-own-act (new); depends on selection-through-registration and counterfactual-is-the-course
Delta: section 86 (Becoming.Selection) had the gap in one world (Clearing) and in general only with the second flow
       and the rest's response supplied (Flow.unselected_beyond_coupling_responsive); here the response is derived
       from a law of exchange reading through coupling, the act is any act whose difference stays beyond the actor's
       coupling closure, and in the course form the two flows are the law's own courses
Supplied premises / correspondence: no axiom; the law the rest follows and that it reads through coupling, balance or
       feasibility, the same formations present and the same start, each written into the theorem that uses it
Evidence: Becoming.SelectionGap, 7 theorems and 9 declarations, empty axiom reports; core receipt `{NEW_R}`;
          connectivity check passes, 177 apart of 8,221, none in Becoming.SelectionGap
Boundary: which acts are taken and how large their consequences beyond the closure are; the general form of
          favouring what reaches beyond; the rising share of what reaches beyond
```

Ren, 18 October 2026: "{REN}" ([source]({SRC_LINK})). The item is the first of the chapter's open programme that no other session held (§8.2, "Selection, causes and experiment": "The gap for one's own act as a general theorem").

**The question.** §86 showed that a selection through a formation's coupling is blind beyond its coupling closure. The proof needed the rest of the exchange to respond only through coupling, and that was supplied. For one's own act the question is whether the gap holds for any act, with the rest's response given by the dynamics: where an act changes only what no member of the actor's closure couples into, does any selection through the closure ever tell the act from its absence?

**The move.** `Becoming.Counterfactual` derives, for the rest following a law of exchange that reads through coupling, that it responds through coupling in any two flows (`ExchangeLaw.Through.responds`). That is the response premise of `Flow.unselected_beyond_coupling_responsive` for the formations outside the acting part. For the part's own members, the premise is the act's condition: within the closure, coupled alike, they exchange alike with every condition coupled into the closure. Splitting on whether a formation is in the part joins the two.

**What is proved** (`Becoming.SelectionGap`).
- **The act's difference stays beyond the closure** (`Flow.ActsAlikeWithin`, `Flow.ActsAlikeOnCoupled`, `Flow.ActsAlikeOnCoupled.within`): the act's members within the closure, coupled alike up to a step, exchange alike with every condition a member of the closure couples into; differing only on conditions no member couples into is the plain case.
- **Every selection through the closure misses the act** (`Flow.act_unselected`, `Flow.act_unselected_of_coupled`): with the rest following one law of exchange reading through coupling in two balanced flows with the same formations present and the same start, every selection through the coupling of any member of the closure, the actor among them, selects the two flows' levels alike at every step.
- **A consequence is selected through no member** (`Flow.consequence_unselected`): a selection that holds with the act and fails without it is, at no step, a selection through the coupling of any member of the closure.
- **With both acts laws, nothing is supplied** (`act_courses_unselected`, with `ExchangeLaw.withAct_take_of_part` and `ExchangeLaw.withAct_give_of_part`): where the part acts by `act` or `act'`, laws of what has stood, `act` reading through its members' coupling and the two agreeing on every condition coupled into the closure, the courses the law generates with each, feasible, are selected alike through every member of the closure. The second flow, the response and the levels are the law's own.

**What this changes.** The gap is now a law of any act, not a property of one world. What a formation can select for or against is bounded by its coupling closure, not by its reach. Exactness comes from §86: two histories are selected alike through a formation exactly when it couples them alike (`Web.selects_alike_iff`), and where they come apart a selection separates them (`Web.separates`); so an act is selected through a formation exactly where its difference reaches what couples into that formation, and the theorems above give the dynamic condition under which it never does. A difference cannot return into the closure through a formation outside it, since nothing beyond the closure exchanges with a condition coupled into it (`Flow.beyond_coupling`).

*Reading* [AI reading]. An act's consequences beyond the closure, however large, never enter any selection made through the members of the closure, the actor's own included, unless they come back through a condition some member couples into. Correcting such an act takes a coupling that reaches the consequence: widening what couples into the actor, or pooling with a formation that couples into it (`Clearing.selected_pooled`). The reading does not say which acts are taken, or that any is wrong.

**Not done.** The general form of favouring what reaches beyond: when a part raising what couples in must reach beyond the closure (stated in the witness `Diversion`). With transmission, descent and openness, the rising share of what reaches beyond. How large an act's consequences beyond the closure are.

**Self-review.** The statements were read against the Lean.
- The closure is drawn through both flows (`Flow.CoupledFromEither`), as in `Flow.unselected_beyond_coupling_responsive`; in the course form it is drawn through the two generated courses, so `agree` is about the closure the theorem quantifies over, not a smaller one.
- `act_courses_unselected` needs `act` to read through its members' coupling (`act.Through W obs (fun h => !part h)`), so that two histories coupled alike give the act's members the same exchange; `act'` need only agree with `act` on coupled conditions.
- The two courses share `present` and `start`, so those premises close by `rfl`; balance comes from feasibility (`ExchangeLaw.course_balances_iff`).
- `ExchangeLaw.withAct_take_of_part` and `withAct_give_of_part` are proved by `congrArg` on the part's Boolean, with no `simp`.
- Scratch build: 7 theorems, 9 declarations, `unclean` empty, `with_axioms` empty; core receipt `{NEW_R}` passed (181 core modules). A first run on f1e29b8fc (receipt `20261018T075728.919807Z`, kept) passed before S2 landed; this run is on main after S2.

'''
s = once(s, '## Ren’s words quoted in passages that exist only in the Chinese edition', SEC + '## Ren’s words quoted in passages that exist only in the Chinese edition')
STUDY.write_text(s)
ANCHOR = f'{n}-the-gap-for-ones-own-act-g1'
STUDY_LINK = '../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'

# Chapter.
c = C.read_text()
c = once(c, "The gap for one's own act as a general theorem (where an act differs only on conditions no member of the "
            "registration closure registers, every selection through it misses the act); ",
         '')
c = once(c, "| Selection, causes and experiment | the general form",
         "| Selection, causes and experiment | (The gap for one's own act is stated as a general theorem: "
         "`Becoming.SelectionGap`.) The general form")
c = once(c, '[selection-through-registration](../results/records/selection-through-registration.md), [projection-carrying-a-law]',
         f'[selection-through-registration](../results/records/selection-through-registration.md), [the-gap-for-ones-own-act]({REC}), [projection-carrying-a-law]')
BULLET_AFTER = '- The gap is the reach closure less the registration closure. In `Clearing`'
lines = c.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith(BULLET_AFTER)]
assert len(idx) == 1, idx
BULLET = (f"- *The gap for one's own act* ([Becoming.SelectionGap]({LEAN}), [the-gap-for-ones-own-act]({REC})). "
          "Where the rest follows one law of exchange reading through coupling, an act whose difference stays beyond the "
          "actor's coupling closure is selected alike, with and without it, by every selection through any member of the "
          "closure, the actor among them, at every step (`Flow.act_unselected`, `Flow.act_unselected_of_coupled`). So a "
          "consequence of the act, holding with it and failing without it, is a selection through no member of the "
          "closure (`Flow.consequence_unselected`). The rest's response is derived from the law "
          "(`ExchangeLaw.Through.responds`), not supplied; where both acts are laws, the courses the law generates with "
          "each are compared and nothing is supplied (`act_courses_unselected`). `Clearing` is a world in which such an "
          f"act ends a formation within the actor's reach. Study: [section {n}]({STUDY_LINK}#{ANCHOR}).")
lines[idx[0] + 1:idx[0] + 1] = [BULLET]
c = '\n'.join(lines)
start = c.index('**The current receipt.**')
end = c.index('| Generated `injEq` lemmas', start)
para = c[start:end]
for old, new in [
    (f'is run `{OLD_R}`, frozen in [`becoming-checks/{OLD_R}/`](../../../{PKG}/becoming-checks/{OLD_R}/verification.json)',
     f'is run `{NEW_R}`, frozen in [`becoming-checks/{NEW_R}/`](../../../{PKG}/becoming-checks/{NEW_R}/verification.json)'),
    ('on main f1e29b8fc (after S1, `Becoming.Enough`, and the S2 and G1 claims) with S2 (`Becoming.Settling`, '
     f'[study §175]({STUDY_LINK}#175-when-the-runs-of-a-process-settle-s2)) in the working tree',
     'on main 23a6621a1 (after S2, `Becoming.Settling`) with G1 (`Becoming.SelectionGap`, '
     f'[study §{n}]({STUDY_LINK}#{ANCHOR})) in the working tree'),
    ('| 180 modules, 7,613 theorems |', '| 181 modules, 7,620 theorems |'),
    ('| 183 modules, 7,687 theorems |', '| 184 modules, 7,694 theorems |'),
    ('| Spine (core and bridge) | 8,214 theorems |', '| Spine (core and bridge) | 8,221 theorems |'),
    ('| Audited spine declarations | 11,067 |', '| Audited spine declarations | 11,076 |'),
    ('| Modules in the compile order | 323 |', '| Modules in the compile order | 324 |'),
]:
    para = once(para, old, new)
c = c[:start] + para + c[end:]
old = 'it counts 177 of 8,214, none in `Becoming.Settling`.'
c = once(c, old, old + f' Rerun with G1 (receipt {NEW_R}), it counts 177 of 8,221, none in `Becoming.SelectionGap`.')
C.write_text(c)

# Package README.
r = README.read_text()
lines = r.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| L4 | [`Becoming.Selection`](Becoming/Selection.lean) |')]
assert len(idx) == 1, idx
lines[idx[0] + 1:idx[0] + 1] = [
    '| L4 | [`Becoming.SelectionGap`](Becoming/SelectionGap.lean) | the gap for one\'s own act (no axiom; the law the rest '
    'follows, that it reads through coupling, balance or feasibility are hypotheses of the theorems): where the rest '
    'follows a law of exchange reading through coupling and an act\'s difference stays beyond the actor\'s coupling '
    'closure, every selection through a member of the closure selects the flows with and without the act alike '
    '(`Flow.act_unselected`), so a consequence of the act is selected through no member (`Flow.consequence_unselected`); '
    'with both acts laws, the two generated courses are selected alike (`act_courses_unselected`) |']
README.write_text('\n'.join(lines))

# The selection record's open item.
d = json.loads(SEL.read_text())
items = [x for x in d['does_not_show'] if x['en'].startswith("The gap for one's own act")]
assert len(items) == 1
d['does_not_show'].remove(items[0])
d['next_delta'] = {
    'en': 'The general form of favouring reaching beyond: when a part raising what registers must reach beyond the '
          'closure; with transmission, descent and openness (Capture\'s descent_needs_unrun), the rising share of what '
          'reaches beyond.',
    'zh': '偏向伸出的一般形式：抬高所识者的部分何时必伸出识闭包之外；与传递、后代和开放（Capture 的 descent_needs_unrun）组合，陈述伸出者份额的上升。'}
d['related'].append({'id': 'the-gap-for-ones-own-act', 'detail': {
    'en': "There the gap for one's own act is a general theorem: the response premise of "
          'Flow.unselected_beyond_coupling_responsive derived from a law of exchange, for any act whose difference '
          'stays beyond the closure.',
    'zh': '那里自身动作的缺口是一般定理：Flow.unselected_beyond_coupling_responsive 的回应前提由交换律推出，对差别留在闭包之外的任何动作。'}})
d['history'].append({
    'en': "18 October 2026, G1 (Becoming.SelectionGap): the open item \"the gap for one's own act has no separate general "
          "theorem\" is removed from does_not_show and next_delta, since the-gap-for-ones-own-act states it; that record "
          'is added as related. This record\'s claims are unchanged.',
    'zh': '2026年10月18日，G1（Becoming.SelectionGap）：因 the-gap-for-ones-own-act 陈述了它，从 does_not_show 与 next_delta 删去开放项“自身动作的缺口没有单独的一般定理”；'
          '加入该记录为相关。本记录的论断不变。'})
SEL.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(n)
