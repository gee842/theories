#!/usr/bin/env python3
"""P58b: exact names for P58's settling lemmas. Renames and docstrings only, plus the prelude-only
lemma stop_unrefuted_iff that makes each name's meaning its statement. Usage: python3 -B lean_p58b.py WT"""
import sys
from pathlib import Path

W = Path(sys.argv[1])
B = W / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
RENAMES = [('falls_settle', 'falls_stop_unrefuted'), ('amount_settles', 'amount_still_unrefuted'),
           ('generation_settles', 'generation_stops_unrefuted'), ('change_settles', 'change_stops_unrefuted'),
           ('arising_settles_from', 'arising_stops_unrefuted_from'), ('few_of_settled', 'few_of_stop_unrefuted')]


def once(text, old, new, where):
    n = text.count(old)
    assert n == 1, (where, n, old[:80])
    return text.replace(old, new)


def edit(name, pairs):
    p = B / name
    t = p.read_text()
    for i, (old, new) in enumerate(pairs):
        t = once(t, old, new, f'{name}#{i}')
    for old, new in RENAMES:
        t = t.replace(old, new)
    p.write_text(t)


edit('Space.lean', [
    ('''  procedure (`World.rests`): the stock does not rise, so generation settles
  (`falls_settle`, `Web.generation_settles`), which refutes the arising that ceasing leaves''',
     '''  procedure (`World.rests`): the stock does not rise, so that generation stops from some step
  on cannot be refuted (`falls_settle`, `Web.generation_settles`; read through
  `stop_unrefuted_iff`), which refutes the arising that ceasing leaves'''),
    ('''/-- An amount that does not rise from step `T` on settles: it is not the case that after every
step from `T` on a later fall stays unrefuted. No decidedness is needed;
`falls_finitely_from_floor` is the weaker form, that its falls do not recur. -/''',
     '''/-- Stopping from some step on cannot be refuted exactly where it is not the case that after
every step from `T` on a later occurrence stays unrefuted. Each `…_unrefuted` stopping lemma below
states the left side; this reads it as the right. No decidedness: actually finding the step
would need it. -/
theorem stop_unrefuted_iff {P : Nat → Prop} {T : Nat} :
    (¬ ∀ M, T ≤ M → ¬ ¬ ∃ t, M ≤ t ∧ P t) ↔ ¬ ¬ ∃ M, T ≤ M ∧ ∀ t, M ≤ t → ¬ P t :=
  ⟨fun h no => h fun M from_ none_ => no ⟨M, from_, fun t later holds => none_ ⟨t, later, holds⟩⟩,
   fun nn all => nn fun ⟨M, from_, none_⟩ => all M from_ fun ⟨t, later, holds⟩ =>
     none_ t later holds⟩

/-- That the falls of an amount not rising from step `T` on stop from some step on cannot be
refuted: it is not the case that after every step from `T` on a later fall stays unrefuted
(`stop_unrefuted_iff`). No decidedness is needed; `falls_finitely_from_floor` is the weaker
form, that its falls do not recur. -/'''),
    ('''/-- So the amount stays the same from some step on, which cannot be refuted. -/''',
     '''/-- So that the amount stays the same from some step on cannot be refuted. -/'''),
    ('''/-- Embodied members of a family balanced and dissipated on from step `T` on settle: it is not
the case that after every step from `T` on a later arising of one of them stays unrefuted. No''',
     '''/-- That the arising of embodied members of a family balanced and dissipated on from step `T`
on stops from some step on cannot be refuted: it is not the case that after every step from `T`
on a later arising of one of them stays unrefuted (`stop_unrefuted_iff`). No'''),
    ('''no premise on other families or steps: generation settles (`Web.generation_settles`), which''',
     '''no premise on other families or steps: that generation stops cannot be refuted
(`Web.generation_settles`), which'''),
    ('''  have settles := Web.generation_settles balances dissipates
  ⟨fun arising => settles fun M from_ none_ => match arising M with''',
     '''  have unrefuted := Web.generation_settles balances dissipates
  ⟨fun arising => unrefuted fun M from_ none_ => match arising M with'''),
    ('''   fun ceasing => settles fun M from_ none_ =>
      arising_unrefuted_covering''',
     '''   fun ceasing => unrefuted fun M from_ none_ =>
      arising_unrefuted_covering'''),
])

edit('Openness.lean', [
    ('''  stands, arising stops, since standing stops changing (`World.arising_stops`); more, it
  settles: it is not the case that after every step from then on a later arising stays
  unrefuted (`World.arising_settles_from`, from `Flow.change_settles`).''',
     '''  stands, arising stops, since standing stops changing (`World.arising_stops`); more, that
  it stops from some step on cannot be refuted even where the flow is only not refuted to run
  down: it is not the case that after every step from then on a later arising stays
  unrefuted (`World.arising_settles_from`, from `Flow.change_settles`).'''),
    ('''  (`Covers.not_not_coming_from`), which settling refutes (`World.comes_to_rest_from`).''',
     '''  (`Covers.not_not_coming_from`), which the unrefuted stopping refutes (`World.comes_to_rest_from`).'''),
    ('''  decision procedure where coming to be settles (`Listed.few_of_settled`).''',
     '''  decision procedure where that coming to be stops cannot be refuted (`Listed.few_of_settled`).'''),
    ('''/-- Change settles: under a census of what stands, where across every step from `T` on it is
not refuted that what stands runs down, it is not the case that after every step from `T` on a
later change of some standing stays unrefuted. No premise;''',
     '''/-- That change stops from some step on cannot be refuted: under a census of what stands, where
across every step from `T` on it is not refuted that what stands runs down, it is not the case
that after every step from `T` on a later change of some standing stays unrefuted
(`stop_unrefuted_iff`). No premise;'''),
    ('''/-- Arising settles there: it is not the case that after every step from `T` on a later arising
stays unrefuted.''',
     '''/-- That arising stops there from some step on cannot be refuted: it is not the case that after
every step from `T` on a later arising stays unrefuted (`stop_unrefuted_iff`).'''),
    ('''arising settles (`arising_settles_from`), and ceasing recurring''',
     '''that arising stops cannot be refuted (`arising_settles_from`), and ceasing recurring'''),
    ('''  have settles := arising_settles_from standing embodied runs
  ⟨fun arising => settles fun M _ none_ => match arising M with
      | ⟨t, x, later, arises⟩ => none_ ⟨t, x, later, arises⟩,
   fun ceasing => settles fun M from_ none_ => match covered M from_ with''',
     '''  have unrefuted := arising_settles_from standing embodied runs
  ⟨fun arising => unrefuted fun M _ none_ => match arising M with
      | ⟨t, x, later, arises⟩ => none_ ⟨t, x, later, arises⟩,
   fun ceasing => unrefuted fun M from_ none_ => match covered M from_ with'''),
    ('''/-- Where what holds is listed at each step and coming to be settles, not unboundedly many
members ever hold, with no decision procedure: `Listed.few_of_quiet` from the settling form
of quiet. -/''',
     '''/-- Where what holds is listed at each step and that coming to be stops from some step on
cannot be refuted (`stop_unrefuted_iff` from step `0`), not unboundedly many members ever hold,
with no decision procedure: `Listed.few_of_quiet` from the unrefuted-stopping form of quiet. -/'''),
    ('''    (settled : ¬ ∀ N, ¬ ¬ ∃ t a, N ≤ t ∧ ComesToBe (p a) t) :
    ¬ ∀ L : List α, ∃ t a, p a t ∧ ¬ a ∈ L :=
  fun many => settled fun N none_''',
     '''    (stopping : ¬ ∀ N, ¬ ¬ ∃ t a, N ≤ t ∧ ComesToBe (p a) t) :
    ¬ ∀ L : List α, ∃ t a, p a t ∧ ¬ a ∈ L :=
  fun many => stopping fun N none_'''),
    ('''(the eleventh review's probe), with no decision procedure: change settles
(`Flow.change_settles`), and with it coming to be (`Listed.few_of_settled`).''',
     '''(the eleventh review's probe), with no decision procedure: that change stops cannot be
refuted (`Flow.change_settles`), nor with it that coming to be stops (`Listed.few_of_settled`).'''),
    ('''  have settles := Flow.change_settles standing (T := T)''',
     '''  have unrefuted := Flow.change_settles standing (T := T)'''),
    ('''        settles fun M _ none_ => all M fun ⟨t, x, later, arises⟩ =>''',
     '''        unrefuted fun M _ none_ => all M fun ⟨t, x, later, arises⟩ =>'''),
    ('''        settles fun M _ none_ => all M fun ⟨t, x, later, comes⟩ =>''',
     '''        unrefuted fun M _ none_ => all M fun ⟨t, x, later, comes⟩ =>'''),
])

edit('Decidedness.lean', [
    ('''  `World.rest_few`) use no decision procedure: an amount that does not rise settles, it not
  being the case that after every step from then on a later fall stays unrefuted
  (`falls_settle`),''',
     '''  `World.rest_few`) use no decision procedure: that the falls of an amount that does not rise
  stop from some step on cannot be refuted, it not being the case that after every step from
  then on a later fall stays unrefuted (`falls_settle`, `stop_unrefuted_iff`),'''),
])
for f in ('Space.lean', 'Openness.lean', 'Decidedness.lean'):
    t = (B / f).read_text()
    assert 'settle' not in t, (f, [l for l in t.splitlines() if 'settle' in l])
print('ok')
