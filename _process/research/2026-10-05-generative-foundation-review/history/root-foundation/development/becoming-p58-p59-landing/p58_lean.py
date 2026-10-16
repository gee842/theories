#!/usr/bin/env python3
"""P58 Lean: decidedness made local. python3 -B p58_lean.py ROOT

Adds the core module `Becoming.Decidedness`, and in place (names kept, only the unused decision
procedure on activity dropped, agreed with the integrator 10-12) frees the rest theorems:
`World.rests_covering`, `World.rests` (Space), `World.comes_to_rest`, `World.Finite.comes_to_rest`,
`World.rest_few` (Openness), `World.premised_rests` (Premises) and, where present,
`World.sample_rests` (Sampling). The settling lemmas go in the lowest module that uses them:
Space (`still_le`, `unrefuted_falls_exceed`, `falls_settle`, `amount_settles`,
`Web.generation_settles`, `World.arising_unrefuted_covering`) and Openness (`Flow.change_settles`,
`comes_after_unrefuted`, `Listed.few_of_settled`, `World.arising_settles_from`,
`World.comes_to_rest_from`). Registers the module in the root and the checker. Every edit is an
exact replacement that must match once."""
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(sys.argv[1])
HERE = Path(__file__).resolve().parent
LB = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
B = LB / 'Becoming'


def ws(old):
    """A pattern matching `old` with any run of whitespace where it has one."""
    return re.compile(r'\s+'.join(re.escape(w) for w in old.split()))


def sub_once(s, old, new, where):
    pat = ws(old)
    found = pat.findall(s)
    assert len(found) == 1, (where, len(found), old[:90])
    return pat.sub(lambda _: new, s, count=1)


def insert_after(s, anchor, text, where):
    pat = ws(anchor)
    m = list(pat.finditer(s))
    assert len(m) == 1, (where, len(m), anchor[:90])
    return s[:m[0].end()] + text + s[m[0].end():]


def insert_before(s, anchor, text, where):
    pat = ws(anchor)
    m = list(pat.finditer(s))
    assert len(m) == 1, (where, len(m), anchor[:90])
    return s[:m[0].start()] + text + s[m[0].start():]


# ---------------------------------------------------------------- the new module
shutil.copyfile(HERE / 'Becoming/Decidedness.lean', B / 'Decidedness.lean')

# ---------------------------------------------------------------- Space
p = B / 'Space.lean'
s = p.read_text()
s = sub_once(s, '''Read of worlds: in a finite world
  whose activity is decided, arising recurs exactly when ceasing does
  (`World.arising_iff_ceasing`). Decidability is part of the representation: asked of
  every finite world without it, this law is equivalent to excluded middle
  (`World.law_iff_em`, from `World.law_decides` and `World.law_of_em`); classically every
  activity is decided.''', '''Read of worlds: in a finite world
  whose activity is decided, arising recurs exactly when ceasing does
  (`World.arising_iff_ceasing`). Decidedness is this law's own condition, not a commitment of
  the representation: asked of every finite world without it, the law is equivalent to
  excluded middle (`World.law_iff_em`, from `World.law_decides` and `World.law_of_em`);
  classically every activity is decided.''', 'Space doc law')
s = sub_once(s, '''* **Dissipation brings a finite world to rest.** In a finite, balanced, dissipative world
  whose activity is decided and in which whatever arises is embodied, neither arising nor
  ceasing recurs (`World.rests`). Each premise is needed (`World.rests_needs`): a world''', '''* **Dissipation brings a finite world to rest.** In a finite, balanced, dissipative world
  in which whatever arises is embodied, neither arising nor ceasing recurs, with no decision
  procedure (`World.rests`): the stock does not rise, so generation settles
  (`falls_settle`, `Web.generation_settles`), which refutes the arising that ceasing leaves
  unrefuted under a covering list (`World.arising_unrefuted_covering`). Each premise is
  needed (`World.rests_needs`): a world''', 'Space doc rest')
s = sub_once(s, '''/-- In a finite world whose activity is decided, arising recurs exactly when ceasing does.
Decidability is part of the representation: without it the law implies excluded middle
(`law_decides`). -/''', '''/-- In a finite world whose activity is decided, arising recurs exactly when ceasing does.
Decidedness is this law's own condition, not part of the representation: without it the law
implies excluded middle (`law_decides`). -/''', 'Space arising_iff_ceasing doc')
s = insert_before(s, '/-! ## The space and its parts -/', '''/-! ## Settling, with no decision procedure -/

/-- An amount that does not rise from step `T` on is, at any later step, at most what it was. -/
theorem still_le {q : Nat → Nat} {T M : Nat} (still : ∀ n, T ≤ n → q (n + 1) ≤ q n)
    (from_ : T ≤ M) : ∀ k, q (M + k) ≤ q M
  | 0 => Nat.le_refl _
  | k + 1 => Nat.le_trans (still (M + k) (Nat.le_trans from_ (Nat.le_add_right M k)))
      (still_le still from_ k)

/-- Where an amount does not rise from step `T` on and, after every step from `T` on, a later
fall is not refuted, the amount exceeds every bound at every step from `T` on. -/
theorem unrefuted_falls_exceed {q : Nat → Nat} {T : Nat} (still : ∀ n, T ≤ n → q (n + 1) ≤ q n)
    (falls : ∀ M, T ≤ M → ¬ ¬ ∃ t, M ≤ t ∧ q (t + 1) < q t) :
    ∀ v M, T ≤ M → q M ≤ v → False
  | 0, M, from_, le => falls M from_ fun ⟨_, later, down⟩ => match le_dest later with
    | ⟨k, same⟩ => Nat.not_lt_zero _ (Nat.lt_of_lt_of_le down (Nat.le_trans
        (Eq.subst (motive := fun x => q x ≤ q M) same.symm (still_le still from_ k)) le))
  | v + 1, M, from_, le => falls M from_ fun ⟨t, later, down⟩ => match le_dest later with
    | ⟨k, same⟩ => unrefuted_falls_exceed still falls v (t + 1)
        (Nat.le_succ_of_le (Nat.le_trans from_ later))
        (Nat.le_of_lt_succ (Nat.lt_of_lt_of_le down (Nat.le_trans
          (Eq.subst (motive := fun x => q x ≤ q M) same.symm (still_le still from_ k)) le)))

/-- An amount that does not rise from step `T` on settles: it is not the case that after every
step from `T` on a later fall stays unrefuted. No decidedness is needed;
`falls_finitely_from_floor` is the weaker form, that its falls do not recur. -/
theorem falls_settle {q : Nat → Nat} {T : Nat} (still : ∀ n, T ≤ n → q (n + 1) ≤ q n) :
    ¬ ∀ M, T ≤ M → ¬ ¬ ∃ t, M ≤ t ∧ q (t + 1) < q t :=
  fun falls => unrefuted_falls_exceed still falls (q T) T (Nat.le_refl T) (Nat.le_refl _)

/-- So the amount stays the same from some step on, which cannot be refuted. -/
theorem amount_settles {q : Nat → Nat} {T : Nat} (still : ∀ n, T ≤ n → q (n + 1) ≤ q n) :
    ¬ ¬ ∃ M, T ≤ M ∧ ∀ t, M ≤ t → q (t + 1) = q t :=
  fun never => falls_settle still fun M from_ none_ => never ⟨M, from_, fun t later =>
    Nat.le_antisymm (still t (Nat.le_trans from_ later))
      (Nat.ge_of_not_lt fun down => none_ ⟨t, later, down⟩)⟩

/-- Embodied members of a family balanced and dissipated on from step `T` on settle: it is not
the case that after every step from `T` on a later arising of one of them stays unrefuted. No
decidedness is needed; `Web.generation_ceases_from` is the weaker form, that their arising does
not recur. -/
theorem Web.generation_settles {X : Type} {W : Web X X} {L : Flow X X} {ds : List X} {T : Nat}
    (balances : ∀ t, T ≤ t → L.BalancesOn W ds t) (dissipates : ∀ t, T ≤ t → L.DissipatesOn ds t) :
    ¬ ∀ M, T ≤ M → ¬ ¬ ∃ t x, M ≤ t ∧ x ∈ ds ∧ W.Embodied x ∧ W.Arises t x :=
  fun arising => falls_settle (q := W.stock ds) (T := T)
    (fun t later => Nat.le_trans (Nat.le_add_right _ _)
      ((balances t later).runs_down (dissipates t later)))
    fun M from_ falls => arising M from_ fun ⟨t, _, later, mem, embodied, arises⟩ =>
      falls ⟨t, later, (balances t (Nat.le_trans from_ later)).rise_lowers
        (dissipates t (Nat.le_trans from_ later)) mem (embodied.comesToStand arises).rises⟩

''', 'Space settling')
s = sub_once(s, '''/-- Rest, from a step on: in any world whose activity is decided and whatever arises is
embodied, where from some step on the active relata lie in one family, balanced and
dissipated on at each of those steps, neither arising nor ceasing recurs. No finiteness of
the world, no closure and no premise on other families or steps. -/
theorem rests_covering [∀ t x, Decidable (w.web.active t x)] {ds : List w.Relatum} {T : Nat}
    (covers : ∀ t, T ≤ t → ∀ x, w.web.active t x → x ∈ ds)
    (balances : ∀ t, T ≤ t → w.flow.BalancesOn w.web ds t)
    (dissipates : ∀ t, T ≤ t → w.flow.DissipatesOn ds t) (embodied : w.ArisingEmbodied) :
    ¬ w.ArisingRecurs ∧ ¬ w.CeasingRecurs :=
  have quiet : ¬ w.ArisingRecurs := fun arising =>
    Web.generation_ceases_from balances dissipates fun N => match arising (N + T) with
      | ⟨t, x, later, arises⟩ => ⟨t, x, Nat.le_trans (Nat.le_add_right N T) later,
          covers (t + 1) (Nat.le_succ_of_le (Nat.le_trans (Nat.le_add_left T N) later)) x arises.2,
          embodied t x arises, arises⟩
  ⟨quiet, fun ceasing => quiet ((arising_iff_ceasing_covering covers).mpr ceasing)⟩

/-- Dissipation brings a finite world to rest: where activity is decided, the flow balances
and dissipates and whatever arises is embodied, neither arising nor ceasing recurs. -/
theorem rests [∀ t x, Decidable (w.web.active t x)] (finite : w.Finite)
    (balanced : w.Balanced) (dissipative : w.Dissipative) (embodied : w.ArisingEmbodied) :
    ¬ w.ArisingRecurs ∧ ¬ w.CeasingRecurs :=''', '''/-- With a list covering what is active from step `T` on, where ceasing recurs, after every
step from `T` on a later arising of a member is not refuted. No decidedness is needed
(`Covers.not_not_coming_from`). -/
theorem arising_unrefuted_covering {ds : List w.Relatum} {T : Nat}
    (covers : ∀ t, T ≤ t → ∀ x, w.web.active t x → x ∈ ds) (ceasing : w.CeasingRecurs) :
    ∀ M, T ≤ M → ¬ ¬ ∃ t x, M ≤ t ∧ x ∈ ds ∧ w.web.Arises t x :=
  fun M from_ none_ => Covers.not_not_coming_from (p := fun x t => w.web.active t x)
    (L := ds) (N := M) (fun x active => covers M from_ x active) ceasing
    fun ⟨t, x, later, arises⟩ => none_ ⟨t, x, later,
      covers (t + 1) (Nat.le_succ_of_le (Nat.le_trans from_ later)) x arises.2, arises⟩

/-- Rest, from a step on: in any world whose arising is embodied, where from some step on the
active relata lie in one family, balanced and dissipated on at each of those steps, neither
arising nor ceasing recurs. No decision procedure, no finiteness of the world, no closure and
no premise on other families or steps: generation settles (`Web.generation_settles`), which
refutes the arising that ceasing leaves unrefuted (`arising_unrefuted_covering`). -/
theorem rests_covering {ds : List w.Relatum} {T : Nat}
    (covers : ∀ t, T ≤ t → ∀ x, w.web.active t x → x ∈ ds)
    (balances : ∀ t, T ≤ t → w.flow.BalancesOn w.web ds t)
    (dissipates : ∀ t, T ≤ t → w.flow.DissipatesOn ds t) (embodied : w.ArisingEmbodied) :
    ¬ w.ArisingRecurs ∧ ¬ w.CeasingRecurs :=
  have settles := Web.generation_settles balances dissipates
  ⟨fun arising => settles fun M from_ none_ => match arising M with
      | ⟨t, x, later, arises⟩ => none_ ⟨t, x, later,
          covers (t + 1) (Nat.le_succ_of_le (Nat.le_trans from_ later)) x arises.2,
          embodied t x arises, arises⟩,
   fun ceasing => settles fun M from_ none_ =>
      arising_unrefuted_covering covers ceasing M from_ fun ⟨t, x, later, mem, arises⟩ =>
        none_ ⟨t, x, later, mem, embodied t x arises, arises⟩⟩

/-- Dissipation brings a finite world to rest: where the flow balances and dissipates and
whatever arises is embodied, neither arising nor ceasing recurs. No decision procedure. -/
theorem rests (finite : w.Finite)
    (balanced : w.Balanced) (dissipative : w.Dissipative) (embodied : w.ArisingEmbodied) :
    ¬ w.ArisingRecurs ∧ ¬ w.CeasingRecurs :=''', 'Space rests')
p.write_text(s)

# ---------------------------------------------------------------- Openness
p = B / 'Openness.lean'
s = p.read_text()
s = sub_once(s, '''* **The rest theorem.** Where what stands is listed, whatever arises is embodied, the
  flow balances and dissipates, and every step from some step on is enclosed around what
  stands, arising stops, since standing stops changing (`World.arising_stops`). With a
  census of what is active as well, ceasing stops too, by the census law: the world comes
  to rest (`World.comes_to_rest`).''', '''* **The rest theorem.** Where what stands is listed, whatever arises is embodied, the
  flow balances and dissipates, and every step from some step on is enclosed around what
  stands, arising stops, since standing stops changing (`World.arising_stops`); more, it
  settles: it is not the case that after every step from then on a later arising stays
  unrefuted (`World.arising_settles_from`, from `Flow.change_settles`). With a census of what is active
  as well, ceasing stops too: the world comes to rest (`World.comes_to_rest`). No decision
  procedure is used, and of the census only that it covers what is active: under a covering
  list, ceasing recurring leaves a later arising unrefuted after every step
  (`Covers.not_not_coming_from`), which settling refutes (`World.comes_to_rest_from`).''',
             'Openness doc rest')
s = sub_once(s, '''so the finite rest of `Becoming.Space` is a case
  (`World.Finite.comes_to_rest`). Where every relatum is embodied''', '''so the finite rest of `Becoming.Space` is a case
  (`World.Finite.comes_to_rest`), its relata covering whatever is active. Where every relatum
  is embodied''', 'Openness doc cases')
s = sub_once(s, '''* **What comes to rest is few.** Where what holds is listed at each step and coming to be
  does not recur, not unboundedly many members ever hold (`Listed.few_of_quiet`). So in
  every world that comes to rest under the rest theorem, not unboundedly many relata are
  ever active and not unboundedly many ever stand (`World.rest_few`);''', '''* **What comes to rest is few.** Where what holds is listed at each step and coming to be
  does not recur, not unboundedly many members ever hold (`Listed.few_of_quiet`), and with no
  decision procedure where coming to be settles (`Listed.few_of_settled`). So in every world
  that comes to rest under the rest theorem, not unboundedly many relata are ever active and
  not unboundedly many ever stand, with no decision procedure (`World.rest_few`);''',
             'Openness doc few')
s = sub_once(s, '''The standing laws need
no embodiment; the rest theorem uses it only for what arises, turning arising into
rising, and reaches ceasing through the census law. Activity is supposed decidable where
a theorem needs it, a logical commitment of the representation.''', '''The standing laws need
no embodiment; the rest theorem uses it only for what arises, turning arising into
rising, and reaches ceasing through a list covering what is active. Decidedness of activity
is not a commitment of the representation: it is the condition of the laws that find a step
where without it a step is only not refuted, the census law, the bounded laws and
`World.few_active`.''',
             'Openness doc close')
s = insert_after(s, '''theorem stills_from (census : W.StandingCensus stand) {T : Nat}
    (runs : ∀ t, T ≤ t → ¬¬ L.RunsDown W t) :
    ¬ ∀ N, ∃ t c, N ≤ t ∧ (W.Rises t c ∨ W.Falls t c) :=
  fun changing => match (change_recurs_iff census).mp (fun N => match changing N with
      | ⟨t, c, later, changes⟩ => ⟨t, later, c, changes⟩) T with
  | ⟨t, later, unmet, _⟩ => runs t later unmet''', '''

/-- Change settles: under a census of what stands, where across every step from `T` on it is
not refuted that what stands runs down, it is not the case that after every step from `T` on a
later change of some standing stays unrefuted. No premise; `stills_from` is the weaker form,
that change does not recur. -/
theorem change_settles (census : W.StandingCensus stand) {T : Nat}
    (runs : ∀ t, T ≤ t → ¬¬ L.RunsDown W t) :
    ¬ ∀ M, T ≤ M → ¬ ¬ ∃ t c, M ≤ t ∧ (W.Rises t c ∨ W.Falls t c) :=
  fun changing => falls_settle (q := fun t => W.stock (stand t) t) (T := T)
    (fun t later => Decidable.of_not_not fun above => runs t later fun down =>
      above (down.standing_le census))
    fun M from_ falls => changing M from_ fun ⟨t, c, later, changes⟩ =>
      falls ⟨t, later, Decidable.of_not_not fun level =>
        runs t (Nat.le_trans from_ later) fun down =>
          level ((down.changes_iff census).mp ⟨c, changes⟩)⟩''', 'Openness change_settles')
s = insert_after(s, '''theorem comes_after {p : Nat → Prop} [∀ t, Decidable (p t)] {N : Nat} (fails : ¬ p N) :
    ∀ {T}, N ≤ T → p T → ∃ t, N ≤ t ∧ ComesToBe p t
  | _, .refl, holds => absurd holds fails
  | m + 1, .step within, holds =>
    if h : p m then comes_after fails within h else ⟨m, within, h, holds⟩''', '''

/-- The same, unrefuted, with no decision procedure. -/
theorem comes_after_unrefuted {p : Nat → Prop} {N : Nat} (fails : ¬ p N) :
    ∀ {T}, N ≤ T → p T → ¬ ¬ ∃ t, N ≤ t ∧ ComesToBe p t
  | _, .refl, holds => absurd holds fails
  | _ + 1, .step within, holds => fun none_ =>
      none_ ⟨_, within, fun h => comes_after_unrefuted fails within h none_, holds⟩''',
                 'Openness comes_after_unrefuted')
s = insert_after(s, '''      | isFalse early => absurd (mem_gather (((listed t).2 a).mp holds)
          (Nat.le_of_lt (Nat.gt_of_not_le early))) out''', '''

/-- Where what holds is listed at each step and coming to be settles, not unboundedly many
members ever hold, with no decision procedure: `Listed.few_of_quiet` from the settling form
of quiet. -/
theorem Listed.few_of_settled {p : α → Nat → Prop} {l : Nat → List α} (listed : Listed p l)
    (settled : ¬ ∀ N, ¬ ¬ ∃ t a, N ≤ t ∧ ComesToBe (p a) t) :
    ¬ ∀ L : List α, ∃ t a, p a t ∧ ¬ a ∈ L :=
  fun many => settled fun N none_ => match many (gather l N) with
    | ⟨t, a, holds, out⟩ =>
      have fails : ¬ p a N := fun h => out (mem_gather (((listed N).2 a).mp h) (Nat.le_refl N))
      match Nat.decLe N t with
      | isTrue later => comes_after_unrefuted fails later holds fun ⟨s, after, comes⟩ =>
          none_ ⟨s, a, after, comes⟩
      | isFalse early => out (mem_gather (((listed t).2 a).mp holds)
          (Nat.le_of_lt (Nat.gt_of_not_le early)))''', 'Openness few_of_settled')
s = insert_after(s, '''theorem arising_stops_from {stand : Nat → List w.Relatum} (standing : w.web.StandingCensus stand)
    (embodied : w.ArisingEmbodied) {T : Nat} (runs : ∀ t, T ≤ t → ¬¬ w.flow.RunsDown w.web t) :
    ¬ w.ArisingRecurs :=
  fun arising => Flow.stills_from standing runs fun N => match arising N with
    | ⟨t, x, later, arises⟩ =>
      ⟨t, x, later, .inl ((embodied t x arises).comesToStand arises).rises⟩''', '''

/-- Arising settles there: it is not the case that after every step from `T` on a later arising
stays unrefuted. No premise on the flow and no decision procedure (`Flow.change_settles`). -/
theorem arising_settles_from {stand : Nat → List w.Relatum} (standing : w.web.StandingCensus stand)
    (embodied : w.ArisingEmbodied) {T : Nat} (runs : ∀ t, T ≤ t → ¬¬ w.flow.RunsDown w.web t) :
    ¬ ∀ M, T ≤ M → ¬ ¬ ∃ t x, M ≤ t ∧ w.web.Arises t x :=
  fun arising => Flow.change_settles standing runs fun M from_ none_ =>
    arising M from_ fun ⟨t, x, later, arises⟩ =>
      none_ ⟨t, x, later, .inl ((embodied t x arises).comesToStand arises).rises⟩''',
                 'Openness arising_settles_from')
s = sub_once(s, '''/-- The rest theorem. A world with a census of activity and of what stands, whose arising
is embodied, with a balanced, dissipative flow, in which every step from some step on is
enclosed around what stands, comes to rest. Arising stops (`arising_stops`), and by the
census law ceasing stops too. -/
theorem comes_to_rest [decided : ∀ t x, Decidable (w.web.active t x)] (counted : w.Counted)
    {stand : Nat → List w.Relatum} (standing : w.web.StandingCensus stand)
    (embodied : w.ArisingEmbodied) (balanced : w.Balanced) (dissipative : w.Dissipative)
    {T : Nat} (around : ∀ t, T ≤ t → w.flow.AroundStanding stand t) :
    ¬ w.ArisingRecurs ∧ ¬ w.CeasingRecurs :=
  have quiet := arising_stops standing embodied balanced dissipative around
  ⟨quiet, fun ceasing => quiet (arising_of_ceasing counted ceasing)⟩''', '''/-- Rest wherever what stands runs down from some step on: a world whose arising is
embodied, with a census of what stands and a list covering what is active at each step from
`T` on, across every step from `T` on of which it is not refuted that what stands runs down,
comes to rest. No premise on the flow, no census of activity and no decision procedure:
arising settles (`arising_settles_from`), and ceasing recurring would leave a later arising
unrefuted after every step (`Covers.not_not_coming_from`). -/
theorem comes_to_rest_from {stand : Nat → List w.Relatum} {T : Nat}
    (covered : ∀ t, T ≤ t → ∃ L : List w.Relatum, Covers (fun x s => w.web.active s x) L t)
    (standing : w.web.StandingCensus stand) (embodied : w.ArisingEmbodied)
    (runs : ∀ t, T ≤ t → ¬¬ w.flow.RunsDown w.web t) :
    ¬ w.ArisingRecurs ∧ ¬ w.CeasingRecurs :=
  have settles := arising_settles_from standing embodied runs
  ⟨fun arising => settles fun M _ none_ => match arising M with
      | ⟨t, x, later, arises⟩ => none_ ⟨t, x, later, arises⟩,
   fun ceasing => settles fun M from_ none_ => match covered M from_ with
     | ⟨_, covers⟩ => Covers.not_not_coming_from (p := fun x s => w.web.active s x) covers ceasing
         fun ⟨t, x, later, arises⟩ => none_ ⟨t, x, later, arises⟩⟩

/-- The rest theorem. A world with a census of activity and of what stands, whose arising
is embodied, with a balanced, dissipative flow, in which every step from some step on is
enclosed around what stands, comes to rest. Arising stops (`arising_stops`), and ceasing
stops too, with no decision procedure: the census covers what is active
(`comes_to_rest_from`). -/
theorem comes_to_rest (counted : w.Counted)
    {stand : Nat → List w.Relatum} (standing : w.web.StandingCensus stand)
    (embodied : w.ArisingEmbodied) (balanced : w.Balanced) (dissipative : w.Dissipative)
    {T : Nat} (around : ∀ t, T ≤ t → w.flow.AroundStanding stand t) :
    ¬ w.ArisingRecurs ∧ ¬ w.CeasingRecurs :=
  match counted with
  | ⟨alive, census⟩ => comes_to_rest_from (T := T)
      (fun t _ => ⟨alive t, fun x active => ((census t).2 x).mp active⟩) standing embodied
      fun t later unmet =>
        unmet ((around t later).runsDownClosed balanced dissipative standing).runsDown''',
             'Openness comes_to_rest')
s = sub_once(s, '''/-- The finite case: `World.rests` follows from the rest theorem. -/
theorem Finite.comes_to_rest [∀ t x, Decidable (w.web.active t x)] (finite : w.Finite)
    (balanced : w.Balanced) (dissipative : w.Dissipative) (embodied : w.ArisingEmbodied) :
    ¬ w.ArisingRecurs ∧ ¬ w.CeasingRecurs :=
  match finite.standing with
  | ⟨_, standing, around⟩ => World.comes_to_rest finite.counted standing embodied balanced
      dissipative (T := 0) fun t _ => around t''', '''/-- The finite case: `World.rests` follows from the rest theorem, with no decision procedure.
A finite world lists what stands, every step is enclosed around it (`Finite.standing`), and
its relata cover what is active (`comes_to_rest_from`); its census of activity, which needs a
decision procedure (`Finite.counted`), is not used. -/
theorem Finite.comes_to_rest (finite : w.Finite)
    (balanced : w.Balanced) (dissipative : w.Dissipative) (embodied : w.ArisingEmbodied) :
    ¬ w.ArisingRecurs ∧ ¬ w.CeasingRecurs :=
  match finite.standing with
  | ⟨_, standing, around⟩ => match finite with
    | ⟨all, _, every⟩ => comes_to_rest_from (T := 0) (fun _ _ => ⟨all, fun x _ => every x⟩)
        standing embodied fun t _ unmet =>
          unmet ((around t).runsDownClosed balanced dissipative standing).runsDown''',
             'Openness Finite.comes_to_rest')
s = sub_once(s, '''  comes_to_rest (decided := fun t x => decidable_of_iff _ (embodied x t).symm) ⟨alive, census⟩''',
             '''  comes_to_rest ⟨alive, census⟩''', 'Openness rests_around call')
s = sub_once(s, '''/-- In every world to which the rest theorem applies, with enclosure from some step on not
refuted, not unboundedly many relata are ever active and not unboundedly many ever stand
(the eleventh review's probe). So the worlds it covers beyond finite ones add only relata
that never stand or act. -/
theorem rest_few [∀ t x, Decidable (w.web.active t x)] (counted : w.Counted)
    {stand : Nat → List w.Relatum} (standing : w.web.StandingCensus stand)
    (embodied : w.ArisingEmbodied) (balanced : w.Balanced) (dissipative : w.Dissipative)
    {T : Nat} (around : ∀ t, T ≤ t → ¬¬ w.flow.AroundStanding stand t) :
    (¬ ∀ L : List w.Relatum, ∃ t x, w.web.active t x ∧ ¬ x ∈ L) ∧
    (¬ ∀ L : List w.Relatum, ∃ t x, 0 < w.web.level t x ∧ ¬ x ∈ L) :=
  have still := Flow.stills balanced dissipative standing around
  match counted with
  | ⟨_, census⟩ =>
    ⟨few_active census fun arising => still fun N => match arising N with
      | ⟨t, x, later, arises⟩ =>
        ⟨t, x, later, .inl ((embodied t x arises).comesToStand arises).rises⟩,
     Listed.few_of_quiet (p := fun x t => 0 < w.web.level t x) standing fun coming =>
       still fun N => match coming N with
       | ⟨t, x, later, comes⟩ => ⟨t, x, later, .inl (Web.ComesToStand.rises (W := w.web) comes)⟩⟩''',
             '''/-- In every world to which the rest theorem applies, with enclosure from some step on not
refuted, not unboundedly many relata are ever active and not unboundedly many ever stand
(the eleventh review's probe), with no decision procedure: change settles
(`Flow.change_settles`), and with it coming to be (`Listed.few_of_settled`). So the worlds it
covers beyond finite ones add only relata that never stand or act. -/
theorem rest_few (counted : w.Counted)
    {stand : Nat → List w.Relatum} (standing : w.web.StandingCensus stand)
    (embodied : w.ArisingEmbodied) (balanced : w.Balanced) (dissipative : w.Dissipative)
    {T : Nat} (around : ∀ t, T ≤ t → ¬¬ w.flow.AroundStanding stand t) :
    (¬ ∀ L : List w.Relatum, ∃ t x, w.web.active t x ∧ ¬ x ∈ L) ∧
    (¬ ∀ L : List w.Relatum, ∃ t x, 0 < w.web.level t x ∧ ¬ x ∈ L) :=
  have settles := Flow.change_settles standing (T := T) fun t later unmet =>
    around t later fun enclosed => unmet (enclosed.runsDownClosed balanced dissipative standing).runsDown
  match counted with
  | ⟨_, census⟩ =>
    ⟨Listed.few_of_settled (p := fun x t => w.web.active t x) census fun all =>
        settles fun M _ none_ => all M fun ⟨t, x, later, arises⟩ =>
          none_ ⟨t, x, later, .inl ((embodied t x arises).comesToStand arises).rises⟩,
     Listed.few_of_settled (p := fun x t => 0 < w.web.level t x) standing fun all =>
        settles fun M _ none_ => all M fun ⟨t, x, later, comes⟩ =>
          none_ ⟨t, x, later, .inl (Web.ComesToStand.rises (W := w.web) comes)⟩⟩''', 'Openness rest_few')
p.write_text(s)

# ---------------------------------------------------------------- Premises
p = B / 'Premises.lean'
s = p.read_text()
s = sub_once(s, '''A finite world whose activity is decided and which meets the eight comes to rest:''',
             '''A finite world which meets the eight comes to rest, with no decision procedure:''',
             'Premises doc')
s = sub_once(s, '''/-- A finite world whose activity is decided and which meets the premises comes to rest:
neither arising nor ceasing recurs. The proof uses balance, dissipation and embodiment. -/
theorem premised_rests [∀ t x, Decidable (w.web.active t x)] (finite : w.Finite)''',
             '''/-- A finite world which meets the premises comes to rest: neither arising nor ceasing
recurs. The proof uses balance, dissipation and embodiment, and no decision procedure. -/
theorem premised_rests (finite : w.Finite)''', 'Premises premised_rests')
p.write_text(s)

# ---------------------------------------------------------------- Sampling, once it has landed
p = B / 'Sampling.lean'
if p.exists() and 'theorem sample_rests [decided' in p.read_text():
    s = p.read_text()
    s = sub_once(s, '''/-- The laws of a world hold at every step size: a finite world read at coarser steps, where
activity is decided, whose flow balances and dissipates and whose arisings are embodied, has
neither arising nor ceasing recurring (`World.rests`). -/''', '''/-- The laws of a world hold at every step size: a finite world read at coarser steps, whose
flow balances and dissipates and whose arisings are embodied, has neither arising nor ceasing
recurring, with no decision procedure (`World.rests`). -/''', 'Sampling doc')
    s = sub_once(s, '''finite world read at a coarser step rests (`World.sample_rests`).''',
                 '''finite world read at a coarser step rests, with no decision procedure
  (`World.sample_rests`).''', 'Sampling module doc')
    s = sub_once(s, 'theorem sample_rests [decided : ∀ t x, Decidable (w.web.active t x)] (strict : Strict σ)',
                 'theorem sample_rests (strict : Strict σ)', 'Sampling binder')
    s = sub_once(s, '@rests (w.sample σ) (fun t x => decided (σ t) x) (sample_finite finite)',
                 'rests (sample_finite finite)', 'Sampling call')
    p.write_text(s)
    print('Sampling patched')

# ---------------------------------------------------------------- root module and checker
p = LB / 'Becoming.lean'
s = p.read_text()
s = sub_once(s, 'import Becoming.Openness', 'import Becoming.Openness\nimport Becoming.Decidedness', 'root import')
s = insert_before(s, '* `Becoming.Counting` (L3):', '''* `Becoming.Decidedness` (L3): decidedness made local (Ren, 11 October 2026: decidability
  is "too dualist", then "please"). A proposition is decided where it holds or fails; a count
  is a relation, existing exactly where what it counts is decided, and where a procedure
  decides, its marks are the count. Between counts the census holds with no decidedness; in a
  finite family, coming to be recurring makes ceasing never stop for good, and conversely, with
  none; decided from some step on, the recurrence law holds. The rest theorems of
  `Becoming.Space` and `Becoming.Openness` use no decision procedure. The readings are the
  AI's, pending Ren.
''', 'root bullet')
p.write_text(s)

p = LB / 'check_becoming.py'
s = p.read_text()
s = sub_once(s, '"Becoming.Openness", "Becoming.Counting",',
             '"Becoming.Openness", "Becoming.Decidedness", "Becoming.Counting",', 'checker CORE')
s = sub_once(s, '''in a finite, balanced, dissipative world whose "
    "activity is decided and in which whatever arises is embodied, neither arising nor ceasing "
    "recurs, and''', '''in a finite, balanced, dissipative world in "
    "which whatever arises is embodied, neither arising nor ceasing recurs, with no decision "
    "procedure, and''', 'scope rests')
s = sub_once(s, '''and a finite "
    "world whose activity is decided and which meets them comes to rest, by balance, "''', '''and a finite "
    "world which meets them comes to rest, with no decision procedure, by balance, "''',
             'scope premised_rests')
s = sub_once(s, '''arising stops; the rest theorem: with a census "
    "of what is active as well, the world comes to rest, finite worlds being a case,''',
             '''arising stops and settles; the rest theorem: with "
    "a census of what is active as well, the world comes to rest with no decision procedure, "
    "the census used only as a list covering what is active, under which ceasing recurring "
    "leaves a later arising unrefuted after every step, which settling refutes, finite worlds "
    "being a case,''', 'scope rest theorem')
s = insert_before(s, '''"Counting: what the premises add to the laws of counting''', '''"Decidedness: a proposition is decided where it holds or fails, which a decision procedure "
    "gives as data; a number counts the members of a list of which a determination holds where "
    "it sums their indicators, a count exists exactly where each member counted is decided, is "
    "unique, and where a procedure decides is its marks; over a stretch, wherever the counts "
    "exist, those holding at the end with those that ceased are those holding at the start with "
    "those that came to be, with no decidedness even inside the stretch, and likewise where what "
    "holds is listed at each step; in a finite family, while nothing ceases each member comes to "
    "be at most once, so where coming to be recurs ceasing never stops for good, and conversely, "
    "with no decidedness, the step being found where the stretch is decided; decided from some "
    "step on, coming to be recurs exactly when ceasing does, in finite families, in webs with "
    "finitely many formations and in finite worlds, a covering list asking decidedness only of "
    "its members; an amount that does not rise settles, so the rest theorems need no decision "
    "procedure. "
    ''', 'scope Decidedness')
p.write_text(s)
print('P58 Lean patch applied to', ROOT)
