#!/usr/bin/env python3
"""P58c, Openness: the rest theorems stated as rest from some step on, unrefuted; stills and
arising_stops strengthened in place; weaker twins renamed `…_not_recurring`. Usage: openness_p58c.py FILE"""
import sys
from pathlib import Path
p = Path(sys.argv[1]); t = p.read_text()


def once(old, new):
    global t
    assert t.count(old) == 1, (t.count(old), old[:80])
    t = t.replace(old, new)


once('''/-- Standing comes to rest wherever what stands runs down from some step on: under a census
of what stands, where across every step from `T` on it is not refuted that what stands runs
down, no condition's standing changes at arbitrarily late steps. No premise is asked: the
corollary of `Flow.change_recurs_iff`. -/
theorem stills_from (census : W.StandingCensus stand) {T : Nat}''',
'''/-- Change does not recur wherever what stands runs down from some step on: under a census
of what stands, where across every step from `T` on it is not refuted that what stands runs
down, no condition's standing changes at arbitrarily late steps. No premise is asked: the
corollary of `Flow.change_recurs_iff`; `Flow.change_stops_unrefuted` is the stronger form. -/
theorem change_not_recurring_from (census : W.StandingCensus stand) {T : Nat}''')
once('''(`stop_unrefuted_iff`). No premise; `stills_from` is the weaker form,
that change does not recur. -/''', '''(`stop_unrefuted_iff`). No premise; `change_not_recurring_from` is the weaker form,
that change does not recur. -/''')
once('''/-- Standing comes to rest: where every step from some step on is enclosed around what
stands, no condition's standing changes at arbitrarily late steps. It is enough that each
of those enclosures is not refuted. The corollary of `Flow.change_recurs_iff`: change
recurring would recur across steps at which what stands does not run down, and under the
premises an enclosure around what stands is such a step. -/
theorem stills (balances : L.Balances W) (dissipative : L.Dissipative)
    (census : W.StandingCensus stand) {T : Nat}
    (around : ∀ t, T ≤ t → ¬¬ L.AroundStanding stand t) :
    ¬ ∀ N, ∃ t c, N ≤ t ∧ (W.Rises t c ∨ W.Falls t c) :=
  stills_from census fun t later unmet => around t later fun enclosed =>
    unmet (enclosed.runsDownClosed balances dissipative census).runsDown''',
'''/-- That standing stops changing from some step on cannot be refuted where every step from
some step on is enclosed around what stands: it is not the case that after every step from
`T` on a later change of some standing stays unrefuted. It is enough that each of those
enclosures is not refuted: under the premises an enclosure around what stands is a step at
which what stands runs down (`Flow.change_stops_unrefuted`). -/
theorem change_stops_unrefuted_around (balances : L.Balances W) (dissipative : L.Dissipative)
    (census : W.StandingCensus stand) {T : Nat}
    (around : ∀ t, T ≤ t → ¬¬ L.AroundStanding stand t) :
    ¬ ∀ M, T ≤ M → ¬ ¬ ∃ t c, M ≤ t ∧ (W.Rises t c ∨ W.Falls t c) :=
  change_stops_unrefuted census fun t later unmet => around t later fun enclosed =>
    unmet (enclosed.runsDownClosed balances dissipative census).runsDown''')
once('''/-- The exchange comes to rest wherever what stands runs down closed from some step on:
under a census of what stands, where across every step from `T` on it is not refuted that
what stands runs down closed, no formation takes or gives at arbitrarily late steps. The
corollary of `Flow.exchange_recurs_iff`, with no premise. -/
theorem exchanges_finitely_from''', '''/-- The exchange does not recur wherever what stands runs down closed from some step on:
under a census of what stands, where across every step from `T` on it is not refuted that
what stands runs down closed, no formation takes or gives at arbitrarily late steps. The
corollary of `Flow.exchange_recurs_iff`, with no premise. -/
theorem exchange_not_recurring_from''')
once('''/-- The exchange comes to rest: where every step from some step on is not refuted to be
enclosed around what stands, no formation takes or gives at arbitrarily late steps. The
corollary of `Flow.exchange_recurs_iff`. -/
theorem exchanges_finitely (balances''', '''/-- The exchange does not recur: where every step from some step on is not refuted to be
enclosed around what stands, no formation takes or gives at arbitrarily late steps. The
corollary of `Flow.exchange_recurs_iff`. -/
theorem exchange_not_recurring (balances''')
once('''  exchanges_finitely_from census fun t later unmet''', '''  exchange_not_recurring_from census fun t later unmet''')

start = t.index('/-- Arising stops wherever what stands runs down from some step on:')
end = t.index('/-- A finite world lists what stands at each step, and every step is enclosed around it,')
t = t[:start] + '''/-- Arising does not recur wherever what stands runs down from some step on: where what stands
is listed and whatever arises is embodied, and across every step from `T` on it is not refuted
that what stands runs down, arising does not recur. No premise on the flow is asked;
`arising_stops_unrefuted_from` is the stronger form. -/
theorem arising_not_recurring_from {stand : Nat → List w.Relatum}
    (standing : w.web.StandingCensus stand) (embodied : w.ArisingEmbodied) {T : Nat}
    (runs : ∀ t, T ≤ t → ¬¬ w.flow.RunsDown w.web t) : ¬ w.ArisingRecurs :=
  fun arising => Flow.change_not_recurring_from standing runs fun N => match arising N with
    | ⟨t, x, later, arises⟩ =>
      ⟨t, x, later, .inl ((embodied t x arises).comesToStand arises).rises⟩

/-- That arising stops there from some step on cannot be refuted: it is not the case that after
every step from `T` on a later arising stays unrefuted (`stop_unrefuted_iff`). No premise on the
flow and no decision procedure (`Flow.change_stops_unrefuted`). -/
theorem arising_stops_unrefuted_from {stand : Nat → List w.Relatum}
    (standing : w.web.StandingCensus stand) (embodied : w.ArisingEmbodied) {T : Nat}
    (runs : ∀ t, T ≤ t → ¬¬ w.flow.RunsDown w.web t) :
    ¬ ∀ M, T ≤ M → ¬ ¬ ∃ t x, M ≤ t ∧ w.web.Arises t x :=
  fun arising => Flow.change_stops_unrefuted standing runs fun M from_ none_ =>
    arising M from_ fun ⟨t, x, later, arises⟩ =>
      none_ ⟨t, x, later, .inl ((embodied t x arises).comesToStand arises).rises⟩

/-- That arising stops from some step on cannot be refuted where what stands is listed,
whatever arises is embodied, the flow balances and dissipates, and every step from some step on
is enclosed around what stands: an enclosure around what stands is a step at which what stands
runs down (`arising_stops_unrefuted_from`). Ceasing need not stop (`rest_needs_census`). -/
theorem arising_stops_unrefuted {stand : Nat → List w.Relatum}
    (standing : w.web.StandingCensus stand) (embodied : w.ArisingEmbodied)
    (balanced : w.Balanced) (dissipative : w.Dissipative)
    {T : Nat} (around : ∀ t, T ≤ t → w.flow.AroundStanding stand t) :
    ¬ ∀ M, T ≤ M → ¬ ¬ ∃ t x, M ≤ t ∧ w.web.Arises t x :=
  arising_stops_unrefuted_from standing embodied fun t later unmet =>
    unmet ((around t later).runsDownClosed balanced dissipative standing).runsDown

/-- Rest wherever what stands runs down from some step on, unrefuted: in a world whose arising
is embodied, with a census of what stands and a list covering what is active at each step from
`T` on, across every step from `T` on of which it is not refuted that what stands runs down,
that the world rests from some step on cannot be refuted. No premise on the flow, no census of
activity and no decision procedure: that arising stops cannot be refuted
(`arising_stops_unrefuted_from`), and ceasing left unrefuted after every step would leave a
later arising unrefuted after every step (`Covers.not_not_coming_from`). -/
theorem comes_to_rest_unrefuted_from {stand : Nat → List w.Relatum} {T : Nat}
    (covered : ∀ t, T ≤ t → ∃ L : List w.Relatum, Covers (fun x s => w.web.active s x) L t)
    (standing : w.web.StandingCensus stand) (embodied : w.ArisingEmbodied)
    (runs : ∀ t, T ≤ t → ¬¬ w.flow.RunsDown w.web t) :
    ¬ ¬ ∃ N, w.RestsFrom N :=
  have unrefuted := arising_stops_unrefuted_from standing embodied runs
  rests_unrefuted_iff.mpr
  ⟨fun arising => unrefuted fun M _ none_ => arising M none_,
   fun ceasing => unrefuted fun M from_ none_ => match covered M from_ with
     | ⟨_, covers⟩ => Covers.not_not_coming_from (p := fun x s => w.web.active s x) covers ceasing
         fun ⟨t, x, later, arises⟩ => none_ ⟨t, x, later, arises⟩⟩

/-- The rest theorem. In a world with a census of activity and of what stands, whose arising is
embodied, with a balanced, dissipative flow, in which every step from some step on is enclosed
around what stands, that the world rests from some step on cannot be refuted, with no decision
procedure: the census covers what is active (`comes_to_rest_unrefuted_from`). Neither arising
nor ceasing recurs, the weaker form (`not_recurring_of_rests_unrefuted`); naming the step is a
principle of omniscience (`World.lpo_of_finite_ends`). -/
theorem comes_to_rest_unrefuted (counted : w.Counted)
    {stand : Nat → List w.Relatum} (standing : w.web.StandingCensus stand)
    (embodied : w.ArisingEmbodied) (balanced : w.Balanced) (dissipative : w.Dissipative)
    {T : Nat} (around : ∀ t, T ≤ t → w.flow.AroundStanding stand t) :
    ¬ ¬ ∃ N, w.RestsFrom N :=
  match counted with
  | ⟨alive, census⟩ => comes_to_rest_unrefuted_from (T := T)
      (fun t _ => ⟨alive t, fun x active => ((census t).2 x).mp active⟩) standing embodied
      fun t later unmet =>
        unmet ((around t later).runsDownClosed balanced dissipative standing).runsDown

''' + t[end:]
once('''so `World.rests` is the finite case of the rest theorem (`Finite.comes_to_rest`). -/''',
     '''so `World.rests_unrefuted` is the finite case of the rest theorem
(`Finite.comes_to_rest_unrefuted`). -/''')
once('''/-- The finite case: `World.rests` follows from the rest theorem, with no decision procedure.
A finite world lists what stands, every step is enclosed around it (`Finite.standing`), and
its relata cover what is active (`comes_to_rest_from`); its census of activity, which needs a
decision procedure (`Finite.counted`), is not used. -/
theorem Finite.comes_to_rest (finite : w.Finite)
    (balanced : w.Balanced) (dissipative : w.Dissipative) (embodied : w.ArisingEmbodied) :
    ¬ w.ArisingRecurs ∧ ¬ w.CeasingRecurs :=
  match finite.standing with
  | ⟨_, standing, around⟩ => match finite with
    | ⟨all, _, every⟩ => comes_to_rest_from (T := 0)''',
'''/-- The finite case: `World.rests_unrefuted` follows from the rest theorem, with no decision
procedure. A finite world lists what stands, every step is enclosed around it
(`Finite.standing`), and its relata cover what is active (`comes_to_rest_unrefuted_from`); its
census of activity, which needs a decision procedure (`Finite.counted`), is not used. -/
theorem Finite.comes_to_rest_unrefuted (finite : w.Finite)
    (balanced : w.Balanced) (dissipative : w.Dissipative) (embodied : w.ArisingEmbodied) :
    ¬ ¬ ∃ N, w.RestsFrom N :=
  match finite.standing with
  | ⟨_, standing, around⟩ => match finite with
    | ⟨all, _, every⟩ => comes_to_rest_unrefuted_from (T := 0)''')
once('''/-- A world with a census whose relata are embodied, with a balanced, dissipative flow, in
which every step from some step on is enclosed around what stands, comes to rest: neither
arising nor ceasing recurs. -/
theorem rests_around {alive : Nat → List w.Relatum} (census : w.web.Census alive)
    (embodied : w.Embodied) (balanced : w.Balanced) (dissipative : w.Dissipative) {T : Nat}
    (around : ∀ t, T ≤ t → w.flow.AroundStanding alive t) :
    ¬ w.ArisingRecurs ∧ ¬ w.CeasingRecurs :=
    comes_to_rest ⟨alive, census⟩''',
'''/-- A world with a census whose relata are embodied, with a balanced, dissipative flow, in
which every step from some step on is enclosed around what stands: that it rests from some step
on cannot be refuted. -/
theorem rests_unrefuted_around {alive : Nat → List w.Relatum} (census : w.web.Census alive)
    (embodied : w.Embodied) (balanced : w.Balanced) (dissipative : w.Dissipative) {T : Nat}
    (around : ∀ t, T ≤ t → w.flow.AroundStanding alive t) :
    ¬ ¬ ∃ N, w.RestsFrom N :=
    comes_to_rest_unrefuted ⟨alive, census⟩''')
once('''/-- Enclosure from some step on suffices, with no decision of equality: each enclosed step
is not not enclosed around what stands, which is enough for standing to come to rest; an
embodied relatum arising rises, and one ceasing falls. -/
theorem rests_enclosed (counted : w.Counted) (embodied : w.Embodied)
    (balanced : w.Balanced) (dissipative : w.Dissipative) {T : Nat}
    (enclosed : ∀ t, T ≤ t → w.flow.Enclosed t) : ¬ w.ArisingRecurs ∧ ¬ w.CeasingRecurs :=
  match counted with
  | ⟨alive, census⟩ =>
    have still := Flow.stills balanced dissipative (standingCensus census embodied)
      fun t later => (enclosed t later).aroundStanding_not_not alive
    ⟨fun arising => still fun N => match arising N with
      | ⟨t, x, later, arises⟩ => ⟨t, x, later, .inl (rises_of_arises embodied arises)⟩,
     fun ceasing => still fun N => match ceasing N with
      | ⟨t, x, later, ceases⟩ => ⟨t, x, later, .inr (falls_of_ceases embodied ceases)⟩⟩''',
'''/-- Enclosure from some step on suffices, with no decision of equality: each enclosed step
is not not enclosed around what stands, which is enough for that standing stops changing to be
unrefuted (`Flow.change_stops_unrefuted_around`); an embodied relatum arising rises, and one
ceasing falls. So that the world rests from some step on cannot be refuted. -/
theorem rests_unrefuted_enclosed (counted : w.Counted) (embodied : w.Embodied)
    (balanced : w.Balanced) (dissipative : w.Dissipative) {T : Nat}
    (enclosed : ∀ t, T ≤ t → w.flow.Enclosed t) : ¬ ¬ ∃ N, w.RestsFrom N :=
  match counted with
  | ⟨alive, census⟩ =>
    have still := Flow.change_stops_unrefuted_around balanced dissipative
      (standingCensus census embodied) fun t later => (enclosed t later).aroundStanding_not_not alive
    rests_unrefuted_iff.mpr
    ⟨fun arising => still fun M _ none_ => arising M fun ⟨t, x, later, arises⟩ =>
        none_ ⟨t, x, later, .inl (rises_of_arises embodied arises)⟩,
     fun ceasing => still fun M _ none_ => ceasing M fun ⟨t, x, later, ceases⟩ =>
        none_ ⟨t, x, later, .inr (falls_of_ceases embodied ceases)⟩⟩''')
once('''  fun enclosed => (rests_enclosed counted embodied balanced dissipative enclosed).1 arising''',
     '''  fun enclosed => (not_recurring_of_rests_unrefuted
    (rests_unrefuted_enclosed counted embodied balanced dissipative enclosed)).1 arising''')
p.write_text(t)
print('ok')
