#!/usr/bin/env python3
"""Apply G2's text: study section, chapter bullet, section 8.2 row, section 9 receipt and connectivity, package
README row, and the selection record's open item: python3 -B apply_text.py NEW_RECEIPT APART MAIN_COMMIT

The old receipt id, the counts and the last connectivity sentence are read from the chapter; the new counts from the
new receipt and its checker log. Each edit must match exactly once. Prints the study section number used."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
NEW_R, APART, MAIN = sys.argv[1], sys.argv[2], sys.argv[3]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
STUDY = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
C = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
README = ROOT / PKG / 'README.md'
SEL = ROOT / 'theories/becoming/results/records/selection-through-registration.json'
LOG = Path(__file__).resolve().parent / 'checker-g2.log'
LEAN = f'../../../{PKG}/Becoming/SelectionReach.lean'
REC = '../results/records/raising-what-couples-in-draws-from-beyond.md'
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
st = json.loads(log[log.index('{'):log.rindex('}') + 1])['spine_theorems']
log_d = json.loads(log[log.index('{'):log.rindex('}') + 1])
core_n, core_t = len(r['core_modules']), sum(st.get(m, 0) for m in r['core_modules'])
clos_n = len(r['core_closure'])
found_t = 74
spine = sum(st.values())
audits = log_d['spine_declaration_audits']
order = len(r['compile_order'])
fmt = lambda n: f'{n:,}'

# Study.
s = STUDY.read_text()
n = max(int(m) for m in re.findall(r'^## (\d+)\. ', s, re.M)) + 1
ANCHOR = f'{n}-raising-what-couples-in-draws-from-beyond-g2'
SEC = f'''## {n}. Raising what couples in draws from beyond (G2)

```text
Result(s): raising-what-couples-in-draws-from-beyond (new); depends on selection-through-registration and
           entropy-history-and-record
Delta: section 86 (Becoming.Selection) showed favouring what reaches beyond in one world (Diversion); Dissipation
       showed that rising recurring at arbitrarily late steps, under dissipation, draws in (negative form). Here, for
       any balanced flow and one step: where a family containing what couples in gains nothing, a rise of what
       couples in has a formation that gives it more than it takes from it and takes from beyond it, with equality
       decided from a named condition, and the rise is paid from beyond in full; so every selection holding only where what couples in rises holds only on
       flows reaching beyond the coupling; Diversion is an instance and its supplying flow shows the premise binds
Supplied premises / correspondence: no axiom; balance, the containing family gaining nothing across the step
       (Flow.GainlessOn, nothing from nothing), equality of conditions decided for the named condition, and the family
       listing what the group couples into, each written into the theorem that uses it
Evidence: Becoming.SelectionReach, 13 theorems, empty axiom reports; core receipt `{NEW_R}`; connectivity check
          passes, {APART} apart of {fmt(spine)}, none in Becoming.SelectionReach
Boundary: how much more than the rise is drawn beyond (dissipation would add to it); whether what is drawn is
          depended on; the rising share of what reaches beyond with transmission, descent and openness
```

Ren, 18 October 2026: "{REN}" ([source]({SRC_LINK})). The item is the next of the chapter's open programme in the same row as G1 (§8.2, "Selection, causes and experiment": "the general form of favouring what reaches beyond").

**The question.** In `Diversion` a selection through the taker's coupling favours a flow that takes from a source a dweller depends on, to raise a store the taker observes. When must a part raising what couples in reach beyond the coupling closure, for any flow?

**The move.** A rise of a family's stock across a step, in a balanced flow, is replenishment above uptake, so some formation gives the family more than it takes from it (totals over the formations and over the family taken in either order). Where a family containing it gains nothing across the step, that formation takes from the containing family at least what it gives to it, so it takes from the containing family more than from the risen one. With equality decided, a list search names the condition.

**What is proved** (`Becoming.SelectionReach`).
- **A rise is given more than it is taken** (`Flow.Balances.gives_more_of_rise`).
- **From nothing new, it is drawn from beyond** (`Flow.Balances.rise_draws_beyond`): the formation takes from the containing family more than from the risen one. With equality decided, it takes from a named condition of the containing family outside the risen one (`Flow.Balances.rise_takes_beyond`, through `exists_outside_of_total_lt`). Under `Flow.Gainless` with the step enclosed around the family, wherever its stock rises (`Flow.Gainless.rise_takes_beyond`).
- **Paid from beyond in full** (`Flow.Balances.rise_paid_from_beyond`): the family's stock after the step is at most its stock before plus what the formations take from the containing family beyond what they take from the family itself. So how much is drawn beyond is at least the whole rise.
- **Selection favours reaching beyond** (`Flow.favours_reaching_beyond`): where the family lists every condition a member of a group couples into, every selection that holds of the flow only where the family's stock rises holds only where, across the step, a formation raising the family takes from a condition no member of the group couples into. Raising an observed family's stock is a selection through the observer's coupling (`Web.raises_selectsThrough`).
- **The instance and the bound** (`Diversion.draws_beyond`, `Diversion.supplying_raises_untaken`): the diverting flow gains nothing on the source and the store, and the general law, applied, gives the taker taking from a place it does not couple into. The supplying flow raises the store with nothing taken, so without the premise a rise need not reach beyond.

**What this changes.** The favour of `Diversion` is a law: wherever nothing comes from nothing on a family containing what couples in, raising what couples in is paid from beyond it, and a selection that rewards the rise rewards the draw, which, with G1 (§176's predecessor, `Becoming.SelectionGap`), it does not see. Dissipation's `rising_draws_in` needed rising at arbitrarily late steps and dissipation and gave a negative form; here one step, the weaker premise of gaining nothing, and a named formation and condition.

*Reading* [AI reading]. Where a selector rewards what it couples into, and nothing comes from nothing, the selected are those that draw on what the selector does not couple into. The favour is structural, not intended. The reading does not say that drawing from beyond is wrong or harmful: what is drawn may be replenished, and whether anything depends on it is not stated.

**Not done.** How much more than the rise is drawn beyond (under dissipation, at least one more unit for each formation taking); whether what is drawn is depended on (with `Becoming.SelectionGap`, whether a dependent beyond is ended); the rising share of what reaches beyond, with transmission, descent and openness.

**Self-review.** The statements were read against the Lean.
- `GainlessOn` is per formation over a family: each formation taking part gives the family no more than it takes from it. It is weaker than dissipation (`Flow.DissipatesOn.gainlessOn`) and holds of lossless exchange, so `Diversion`'s diverting flow, which moves one unit, falls under it.
- `Flow.favours_reaching_beyond` uses the selection only through `rewards` and `holds`; that a rise of an observed family is a selection through coupling is the separate `Web.raises_selectsThrough`, so the law covers every selection, through coupling or not, that holds only where the family rises.
- The helper lemmas are the core's own (`exists_lt_of_total_lt`, `search`, `total_congr_on`, `total_le_of_support`, `decideMem`); a first draft redeclared three of them and was changed to reuse them.
- `nomatch` takes several discriminants, so inside anonymous constructors it is parenthesized.
- A first draft of `Flow.Balances.rise_paid_from_beyond` used Lean's `Nat.add_sub_of_le` and `Nat.le_of_add_le_add_right`, which depend on `propext`; the scratch audit caught it, and the proof uses the core's own `add_sub_of_le` and `le_of_add_le_add_right`.
- Scratch build: 13 theorems, `unclean` empty, `with_axioms` empty; core receipt `{NEW_R}` passed ({core_n} core modules).

'''
s = once(s, '## Ren’s words quoted in passages that exist only in the Chinese edition',
         SEC + '## Ren’s words quoted in passages that exist only in the Chinese edition')
STUDY.write_text(s.replace("which, with G1 (§176's predecessor, `Becoming.SelectionGap`), it does not see",
                           "which, by G1 (`Becoming.SelectionGap`), it does not see"))

# Chapter.
c = C.read_text()
c = once(c, "`Becoming.SelectionGap`.) The general form of favouring what reaches beyond; ",
         "`Becoming.SelectionGap`; the general form of favouring what reaches beyond: `Becoming.SelectionReach`.) ")
c = once(c, "(The gap for one's own act is stated as a general theorem: ",
         "(Stated: the gap for one's own act as a general theorem, ")
c = once(c, "with transmission, descent and openness, the rising share of what reaches beyond;",
         "Whether what is drawn beyond is depended on; with transmission, descent and openness, the rising share of what reaches beyond;")
c = once(c, '[the-gap-for-ones-own-act](../results/records/the-gap-for-ones-own-act.md), [projection-carrying-a-law]',
         f'[the-gap-for-ones-own-act](../results/records/the-gap-for-ones-own-act.md), [raising-what-couples-in-draws-from-beyond]({REC}), [projection-carrying-a-law]')
BULLET_AFTER = '- In `Diversion`, a flow that reaches beyond the registration closure'
lines = c.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith(BULLET_AFTER)]
assert len(idx) == 1, idx
BULLET = (f"- *Raising what couples in draws from beyond* ([Becoming.SelectionReach]({LEAN}), "
          f"[raising-what-couples-in-draws-from-beyond]({REC})). The favour in `Diversion` is a law of any balanced flow. "
          "Where a family containing what couples in gains nothing across a step (nothing from nothing, `Flow.GainlessOn`), a "
          "rise of what couples in has a formation that gives it more than it takes from it and takes from beyond it "
          "(`Flow.Balances.rise_draws_beyond`); with equality decided, from a named condition outside it "
          "(`Flow.Balances.rise_takes_beyond`); and it is paid from beyond in full, the rise at most what is taken beyond "
          "it (`Flow.Balances.rise_paid_from_beyond`). So, where the family lists what a group couples into, every selection "
          "holding only where it rises holds only on flows in which a formation takes from a condition no member of the "
          "group couples into (`Flow.favours_reaching_beyond`). `Diversion` is an instance (`Diversion.draws_beyond`), and "
          "its supplying flow, which gains, raises the store with nothing taken: the premise binds "
          f"(`Diversion.supplying_raises_untaken`). Study: [section {n}]({STUDY_LINK}#{ANCHOR}).")
lines[idx[0] + 1:idx[0] + 1] = [BULLET]
c = '\n'.join(lines)
start = c.index('**The current receipt.**')
end = c.index('| Generated `injEq` lemmas', start)
para = c[start:end]
OLD_R = re.search(r'is run `([0-9TZ.]+)`', para).group(1)
para = para.replace(OLD_R, NEW_R)
m = re.search(r'It was checked with Lean 4\.29\.1 on main \w+ \(.*?\) with .*? in the working tree', para, re.S)
para = para[:m.start()] + (f'It was checked with Lean 4.29.1 on main {MAIN} with G2 (`Becoming.SelectionReach`, '
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
c = c[:last.end()] + (f' Rerun with G2 (receipt {NEW_R}), it counts {APART} of {fmt(spine)}, none in '
                      '`Becoming.SelectionReach`.') + c[last.end():]
C.write_text(c)

# Package README.
rd = README.read_text()
lines = rd.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| L4 | [`Becoming.SelectionGap`](Becoming/SelectionGap.lean) |')]
assert len(idx) == 1, idx
lines[idx[0] + 1:idx[0] + 1] = [
    '| L4 | [`Becoming.SelectionReach`](Becoming/SelectionReach.lean) | favouring what reaches beyond, in general (no axiom; '
    'balance and the containing family gaining nothing are hypotheses of the theorems): a rise of what couples in, where a '
    'family containing it gains nothing across the step, has a formation giving it more than it takes from it and taking '
    'from beyond it (`Flow.Balances.rise_draws_beyond`, `Flow.Balances.rise_takes_beyond`), so a selection holding only '
    'where what couples in rises holds only on flows reaching beyond the coupling (`Flow.favours_reaching_beyond`); '
    '`Diversion` is an instance (`Diversion.draws_beyond`) and its supplying flow shows the premise binds |']
README.write_text('\n'.join(lines))

# The selection record's open items.
d = json.loads(SEL.read_text())
items = [x for x in d['does_not_show'] if x['en'].startswith('Favouring reaching beyond is stated only in the minimal witness')]
assert len(items) == 1
d['does_not_show'].remove(items[0])
d['next_delta'] = {
    'en': "With transmission, descent and openness (Capture's descent_needs_unrun), the rising share of what reaches beyond.",
    'zh': '与传递、后代和开放（Capture 的 descent_needs_unrun）组合，陈述伸出者份额的上升。'}
d['related'].append({'id': 'raising-what-couples-in-draws-from-beyond', 'detail': {
    'en': 'There favouring reaching beyond is a general law: where a family containing what couples in gains nothing, a '
          'rise of what couples in is drawn from beyond it, so a selection rewarding the rise rewards the draw; Diversion '
          'is its instance.',
    'zh': '那里偏向伸出是一般规律：包含所耦合者的族不增益时，所耦合者的上升取自其外，所以奖励上升的选择奖励这一汲取；Diversion 是其实例。'}})
d['history'].append({
    'en': '18 October 2026, G2 (Becoming.SelectionReach): the open item "favouring reaching beyond is stated only in the '
          'minimal witness Diversion" is removed from does_not_show and next_delta, since '
          'raising-what-couples-in-draws-from-beyond states it in general; that record is added as related. This '
          "record's claims are unchanged.",
    'zh': '2026年10月18日，G2（Becoming.SelectionReach）：因 raising-what-couples-in-draws-from-beyond 一般地陈述了它，从 does_not_show 与 '
          'next_delta 删去开放项“偏向伸出只在最小的见证 Diversion 中陈述”；加入该记录为相关。本记录的论断不变。'})
SEL.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(n)
