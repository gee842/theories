import Becoming.Counting
import Becoming.Decidedness

/-!
# Census counts: the laws of counting where the counts exist

`Becoming.Counting` states its laws for worlds whose activity a procedure decides at every
relatum and step (`[∀ t x, Decidable (w.web.active t x)]`), and for properties of the counts
that respect their values at each step (`Pointwise`). This module states the same laws with
neither. The counts of a census are relations (`Counts` of `Becoming.Decidedness`): `n` counts
what is active at each step, `c` what of it ceases across the step, `a` what is active after the
step and came to be across it (`World.CountsOf`). A property of the counts holds in a world where
it holds of every census and every counts of it (`World.CountsHold`). A count across a step
exists exactly where activity is decided at the relata it counts there
(`counts_iff_decided`, `World.comings_exist_iff`), and, the census listing what is active,
exactly where it is decided whether each of them is listed at the other end of the step
(`World.ceasings_exist_iff_listed`, `World.comings_exist_iff_listed`). So the yes or no a law of
counting needs is asked only of the relata it counts, at the step it counts them, and only for the
count to exist.

* **The counts of a census are a tally**, with no decidedness (`World.CountsOf.tally`), from the
  census across a step of `Becoming.Decidedness` (`Counts.listed_across`).
* **The laws of counting, where the counts exist.** For every property of the counts, not only
  pointwise ones: it holds of the counts of every listed family exactly when it holds of every
  tally (`counted_laws`), and so of every counted census of every world
  (`World.counting_free_counted`); it holds in every world meeting a selection of the premises exactly when
  it holds of every tally, and, where the selection binds counting, of every tally in which
  nothing arises across a step at which nothing is active (`World.counting_under_counted`); under
  all eight premises, exactly when it holds of every tally in which nothing arises across a step
  at which nothing is active (`World.premised_counting_counted`). Nothing arising across a step
  at which nothing is active is a law exactly where the selection binds counting
  (`World.counting_binds_iff_counted`).
* **Enclosure bounds change**, for every counted census of embodied relata under a balanced,
  dissipative flow enclosed from `T` on (`World.enclosure_bounds_change_counted`). So, where the
  counts exist and for every property: under the eight premises, in worlds enclosed from some step
  on and in finite worlds, the laws are the tally, nothing arising across a step at which nothing
  is active, and a change bound from the first step (`World.enclosed_counting_counted`,
  `World.finite_counting_counted`); under each selection, in worlds enclosed from some step on
  and in finite worlds, the laws are those of `Becoming.Counting`
  (`World.enclosed_counting_under_counted`, `World.finite_counting_under_counted`), with the
  selections binding counting and bounding change exactly as there
  (`World.enclosed_change_bound_iff_counted`, `World.finite_counting_binds_iff_counted`,
  `World.finite_change_bound_iff_counted`). The grounds are the counted forms of the binding
  steps: something coming to be across a step needs something active at it under balance with
  only active relata giving and embodiment of what arises, under balance with only active relata
  taking, dissipation and embodiment, and at an enclosed step under balance, dissipation and
  embodiment (`World.active_of_coming_jointly`, `World.active_of_coming_taking`,
  `World.active_of_coming_enclosed`).
* **Agreement.** Where a procedure decides activity, its marks are counts of every census
  (`World.countsOf_decided`): what holds of every counted census holds of the census counts of
  `Becoming.Counting` (`World.CountsHold.obey`), and for pointwise properties conversely
  (`World.countsHold_of_obey`).

Not restated here: the laws where the premises bind (`World.binding_counting` and its family in
`Becoming.Counting`), which still take a decision procedure for activity.

No premise beyond what each theorem names. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

variable {α : Type}

/-- **The tally is the whole law of counting, where the counts exist.** A property of the counts
holds of the counts of every listed family exactly when it holds of every tally: for every
property, with no decidedness. -/
theorem counted_laws {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} :
    (∀ (β : Type) (p : β → Nat → Prop) (l : Nat → List β) (n c a : Nat → Nat), Listed p l →
      FamilyCounts p l n c a → Q n c a) ↔ ∀ n c a, Tally n c a → Q n c a :=
  ⟨fun law n c a tally => law Nat (Queue.holds n c) (Queue.line n c) n c a Queue.listed
      ((familyCounts_decided (Queue.line n c)).of_eq fun t => Queue.counts tally t),
   fun law _ _ _ _ _ _ listed counted => law _ _ _ (counted.tally listed)⟩

namespace World

variable {w : World}

/-- **A coming count across a step exists exactly where activity before the step is decided at
each relatum active after it.** -/
theorem comings_exist_iff (alive : Nat → List w.Relatum) (t : Nat) :
    (∃ d, Counts (alive (t + 1)) (fun x => ComesToBe (fun s => w.web.active s x) t) d) ↔
      ∀ x, x ∈ alive (t + 1) → Decided (ComesToBe (fun s => w.web.active s x) t) :=
  counts_iff_decided

/-- **Under a census, a ceasing count across a step exists exactly where, for each relatum listed
before the step, whether it is missing from the list after the step is weakly decided**: it is
missing, or its missing is refuted. -/
theorem ceasings_exist_iff_listed {alive : Nat → List w.Relatum} (census : w.web.Census alive)
    (t : Nat) :
    (∃ d, Counts (alive t) (fun x => CeasesToBe (fun s => w.web.active s x) t) d) ↔
      ∀ x, x ∈ alive t → WeaklyDecided (x ∈ alive (t + 1)) :=
  counts_iff_decided.trans
    ⟨fun decided x mem => match decided x mem with
      | .inl ceases => .inl fun listed => ceases.2 (((census (t + 1)).2 x).mpr listed)
      | .inr stays => .inr fun missing => stays
          ⟨((census t).2 x).mpr mem, fun active => missing (((census (t + 1)).2 x).mp active)⟩,
     fun weakly x mem => match weakly x mem with
      | .inl missing => .inl
          ⟨((census t).2 x).mpr mem, fun active => missing (((census (t + 1)).2 x).mp active)⟩
      | .inr kept => .inr fun ceases => kept fun listed =>
          ceases.2 (((census (t + 1)).2 x).mpr listed)⟩

/-- **Under a census, a coming count across a step exists exactly where, for each relatum listed
after the step, whether it is missing from the list before the step is weakly decided.** -/
theorem comings_exist_iff_listed {alive : Nat → List w.Relatum} (census : w.web.Census alive)
    (t : Nat) :
    (∃ d, Counts (alive (t + 1)) (fun x => ComesToBe (fun s => w.web.active s x) t) d) ↔
      ∀ x, x ∈ alive (t + 1) → WeaklyDecided (x ∈ alive t) :=
  (comings_exist_iff alive t).trans
    ⟨fun decided x mem => match decided x mem with
      | .inl comes => .inl fun listed => comes.1 (((census t).2 x).mpr listed)
      | .inr stays => .inr fun missing => stays
          ⟨fun active => missing (((census t).2 x).mp active), ((census (t + 1)).2 x).mpr mem⟩,
     fun weakly x mem => match weakly x mem with
      | .inl missing => .inl
          ⟨fun active => missing (((census t).2 x).mp active), ((census (t + 1)).2 x).mpr mem⟩
      | .inr kept => .inr fun comes => kept fun listed =>
          comes.1 (((census t).2 x).mpr listed)⟩

/-! ## Agreement with the counts a procedure gives -/

/-! ## Counting under the premises, where the counts exist -/

/-- The queue's counts are counts of its census. -/
theorem queue_countsOf {n c a : Nat → Nat} (tally : Tally n c a) :
    (queue n c).CountsOf (Queue.line n c) n c a :=
  FamilyCounts.of_eq (countsOf_decided (w := queue n c) (Queue.line n c)) fun t =>
    Queue.counts tally t

theorem embodiedQueue_countsOf {n c a : Nat → Nat} (tally : Tally n c a) :
    (embodiedQueue n c).CountsOf (Queue.line n c) n c a :=
  FamilyCounts.of_eq (countsOf_decided (w := embodiedQueue n c) (Queue.line n c)) fun t =>
    Queue.counts tally t

theorem openQueue_countsOf {n c a : Nat → Nat} (tally : Tally n c a) :
    (openQueue n c).CountsOf (fun t => (Queue.line n c t).map .member) n c a :=
  FamilyCounts.of_eq (countsOf_decided (w := openQueue n c) _) (openQueue_counts tally)

theorem drivenQueue_countsOf {n c a : Nat → Nat} (tally : Tally n c a) :
    (drivenQueue n c).CountsOf (fun t => (Queue.line n c t).map .member) n c a :=
  FamilyCounts.of_eq (countsOf_decided (w := drivenQueue n c) _) (openQueue_counts tally)

/-- **The tally is the whole law of counting of every world, where the counts exist.** A property
of the counts holds of every counted census of every world exactly when it holds of every tally:
for every property, with no decidedness (the counted form of the first part of
`World.counting_free`). -/
theorem counting_free_counted {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} :
    (∀ n c a, Tally n c a → Q n c a) ↔ ∀ w : World, w.CountsHold Q :=
  (census_table_holds_free counting_free_witnessed.1).trans
    ⟨fun law w => law w trivial, fun law w _ => law w⟩

/-- **The laws of counting under each selection of the premises, where the counts exist.** A
property of the counts holds of every counted census of every world meeting the selection
exactly when it holds of every tally, and, where the selection binds counting, of every tally in
which nothing arises across a step at which nothing is active. For every property, with no
decidedness. -/
theorem counting_under_counted (S : Premise → Bool)
    {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} :
    (∀ n c a, Tally n c a → (BindsCounting S → ∀ t, 0 < a t → 0 < n t) → Q n c a) ↔
      ∀ w : World, w.Meets S → w.CountsHold Q :=
  census_table_holds (counting_under_sound S) (counting_under_witnessed S)

/-- **Under all eight premises, where the counts exist**, the laws of counting are the tally and
that nothing arises across a step at which nothing is active: for every property, with no
decidedness. -/
theorem premised_counting_counted {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} :
    (∀ n c a, Tally n c a → (∀ t, 0 < a t → 0 < n t) → Q n c a) ↔
      ∀ w : World, w.Premised → w.CountsHold Q :=
  census_table_holds premised_counting_sound premised_counting_witnessed

/-- Nothing arising across a step at which nothing is active is a law of counting under a
selection, where the counts exist, exactly when the selection binds counting. -/
theorem counting_binds_iff_counted (S : Premise → Bool) :
    (∀ w : World, w.Meets S → w.CountsHold fun n _ a => ∀ t, 0 < a t → 0 < n t) ↔
      BindsCounting S :=
  have unbound : ¬ BindsCounting S → ¬ ∀ w : World, w.Meets S →
      w.CountsHold fun n _ a => ∀ t, 0 < a t → 0 < n t := fun free law =>
    Nat.lt_irrefl 0 ((counting_under_counted S).mpr law _ _ _ Queue.lone_tally
      (fun binds => absurd binds free) 0 Nat.zero_lt_one)
  ⟨fun law => match hb : S .balanced, he : S .embodied, ha : S .acting, ht : S .taking,
      hd : S .dissipative with
    | true, true, true, _, _ => ⟨hb, he, .inl ha⟩
    | true, true, false, true, true => ⟨hb, he, .inr ⟨ht, hd⟩⟩
    | false, _, _, _, _ => absurd law (unbound fun binds => nomatch hb.symm.trans binds.1)
    | true, false, _, _, _ => absurd law (unbound fun binds => nomatch he.symm.trans binds.2.1)
    | true, true, false, false, _ => absurd law (unbound fun binds => match binds.2.2 with
        | .inl acting => nomatch ha.symm.trans acting
        | .inr ⟨taking, _⟩ => nomatch ht.symm.trans taking)
    | true, true, false, true, false => absurd law (unbound fun binds => match binds.2.2 with
        | .inl acting => nomatch ha.symm.trans acting
        | .inr ⟨_, dissipative⟩ => nomatch hd.symm.trans dissipative),
   fun binds => (counting_under_counted S).mp fun _ _ _ _ quiet => quiet binds⟩

theorem enclosedQueue_countsOf {n c a : Nat → Nat} (B : Nat) (tally : Tally n c a) :
    (enclosedQueue n c a B).CountsOf (Queue.line n c) n c a :=
  FamilyCounts.of_eq (countsOf_decided (w := enclosedQueue n c a B) (Queue.line n c)) fun t =>
    Queue.counts tally t

theorem closingQueue_countsOf {n c a : Nat → Nat} (B T : Nat) (tally : Tally n c a) :
    (closingQueue n c a B T).CountsOf (Queue.line n c) n c a :=
  FamilyCounts.of_eq (countsOf_decided (w := closingQueue n c a B T) (Queue.line n c)) fun t =>
    Queue.counts tally t

theorem finiteQueue_countsOf {n c a : Nat → Nat} {B : Nat} (tally : Tally n c a)
    (bound : ChangeBound 0 B n c a) :
    (finiteQueue n c a B).CountsOf (FiniteQueue.alive n c B) n c a :=
  FamilyCounts.of_eq (countsOf_decided (w := finiteQueue n c a B) _) (finiteQueue_counts tally bound)

theorem ring_countsOf {n c a : Nat → Nat} {M : Nat} (tally : Tally n c a)
    (bounded : ∀ t, n t ≤ M) : (ring n c M).CountsOf (Ring.seated n c M) n c a :=
  FamilyCounts.of_eq (countsOf_decided (w := ring n c M) _) (Ring.counts tally bounded)

theorem embodiedRing_countsOf {n c a : Nat → Nat} {M : Nat} (tally : Tally n c a)
    (bounded : ∀ t, n t ≤ M) : (embodiedRing n c M).CountsOf (Ring.seated n c M) n c a :=
  FamilyCounts.of_eq (countsOf_decided (w := embodiedRing n c M) _) (Ring.counts tally bounded)

theorem balancedRing_countsOf {n c a : Nat → Nat} {M : Nat} (tally : Tally n c a)
    (bounded : ∀ t, n t ≤ M) : (balancedRing n c M).CountsOf (Ring.seated n c M) n c a :=
  FamilyCounts.of_eq (countsOf_decided (w := balancedRing n c M) _) (Ring.counts tally bounded)

/-- **Under all eight premises, with every step from some step on enclosed, where the counts
exist**, the laws of counting are the tally, that nothing arises across a step at which nothing
is active, and a change bound from the first step: for every property, with no decidedness. -/
theorem enclosed_counting_counted {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} :
    (∀ n c a, Tally n c a → (∀ t, 0 < a t → 0 < n t) → (∃ B, ChangeBound 0 B n c a) →
      Q n c a) ↔
      ∀ w : World, w.Premised → (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) → w.CountsHold Q :=
  census_table_holds₂ enclosed_counting_sound enclosed_counting_witnessed

/-- **Under all eight premises, in finite worlds, where the counts exist**: the same laws. -/
theorem finite_counting_counted {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} :
    (∀ n c a, Tally n c a → (∀ t, 0 < a t → 0 < n t) → (∃ B, ChangeBound 0 B n c a) →
      Q n c a) ↔ ∀ w : World, w.Premised → w.Finite → w.CountsHold Q :=
  census_table_holds₂ finite_counting_sound finite_counting_witnessed

/-- **The laws of counting under each selection, in worlds enclosed from some step on, where
the counts exist**: the tally, and, where the selection binds counting, nothing arising across a
step at which nothing is active, and, where it bounds change, from some step on change within a
bound and nothing arising across a step at which nothing is active. For every property, with no
decidedness. -/
theorem enclosed_counting_under_counted (S : Premise → Bool)
    {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} :
    (∀ n c a, Tally n c a → (BindsCounting S → ∀ t, 0 < a t → 0 < n t) →
      (BoundsChange S → ∃ T B, ChangeBound T B n c a ∧ ∀ t, T ≤ t → 0 < a t → 0 < n t) →
        Q n c a) ↔
      ∀ w : World, w.Meets S → (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) → w.CountsHold Q :=
  census_table_holds₂ (enclosed_counting_under_sound S) (enclosed_counting_under_witnessed S)

/-- In worlds enclosed from some step on, where the counts exist, a change bound from some step
is a law of counting under a selection exactly when the selection bounds change. -/
theorem enclosed_change_bound_iff_counted (S : Premise → Bool) :
    (∀ w : World, w.Meets S → (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) →
        w.CountsHold fun n c a => ∃ T B, ChangeBound T B n c a) ↔ BoundsChange S :=
  have growing : Tally (fun t => t + 1) (fun _ => 0) (fun _ => 1) := fun t => ⟨t + 1, rfl, rfl⟩
  ⟨fun law => if bounds : S .balanced = true ∧ S .embodied = true ∧ S .dissipative = true
      then bounds else
      match (enclosed_counting_under_counted S
          (Q := fun n (_ _ : Nat → Nat) => ∃ T B, ∀ t, T ≤ t → n t ≤ B)).mpr
          (fun w meets enclosed alive n c a census counted =>
            match law w meets enclosed alive n c a census counted with
            | ⟨T, B, bound⟩ => ⟨T, B, fun t later =>
                Nat.le_trans (Nat.le_add_right _ _) (bound t later)⟩)
          _ _ _ growing (fun _ t _ => Nat.zero_lt_succ t) (fun bound => absurd bound bounds) with
      | ⟨T, B, bounded⟩ => (Nat.not_succ_le_self B (Nat.le_trans
          (Nat.succ_le_succ (Nat.le_add_right B T)) (bounded (B + T) (Nat.le_add_left T B)))).elim,
   fun ⟨balanced, embodied, dissipative⟩ _ meets ⟨T, enclosed⟩ _ _ _ _ census counted =>
     ⟨T, _, enclosure_bounds_change_counted census counted (meets _ embodied) (meets _ balanced)
       (meets _ dissipative) enclosed⟩⟩

/-- **The laws of counting under each selection, in finite worlds, where the counts exist**: the
tally with at most some number active at each step; where the selection binds counting or bounds
change, nothing arising across a step at which nothing is active; where it bounds change, a
change bound from the first step. For every property, with no decidedness. -/
theorem finite_counting_under_counted (S : Premise → Bool)
    {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} :
    (∀ n c a, Tally n c a → (∃ M, ∀ t, n t ≤ M) →
      (BindsCounting S ∨ BoundsChange S → ∀ t, 0 < a t → 0 < n t) →
      (BoundsChange S → ∃ B, ChangeBound 0 B n c a) → Q n c a) ↔
      ∀ w : World, w.Meets S → w.Finite → w.CountsHold Q :=
  census_table_holds₃ (finite_counting_under_sound S) (finite_counting_under_witnessed S)

/-- In finite worlds, where the counts exist, nothing arising across a step at which nothing is
active is a law under a selection exactly when the selection binds counting or bounds change. -/
theorem finite_counting_binds_iff_counted (S : Premise → Bool) :
    (∀ w : World, w.Meets S → w.Finite →
      w.CountsHold fun n _ a => ∀ t, 0 < a t → 0 < n t) ↔ BindsCounting S ∨ BoundsChange S :=
  have unbound : ¬ (BindsCounting S ∨ BoundsChange S) → ¬ ∀ w : World, w.Meets S → w.Finite →
      w.CountsHold fun n _ a => ∀ t, 0 < a t → 0 < n t := fun free law =>
    Nat.lt_irrefl 0 ((finite_counting_under_counted S).mpr law _ _ _ Queue.lone_tally
      ⟨1, fun | 0 => Nat.zero_le 1 | _ + 1 => Nat.le_refl 1⟩
      (fun binds => absurd binds free) (fun bounds => absurd (.inr bounds) free)
      0 Nat.zero_lt_one)
  ⟨fun law => match hb : S .balanced, he : S .embodied, ha : S .acting,
      hd : S .dissipative with
    | true, true, true, _ => .inl ⟨hb, he, .inl ha⟩
    | true, true, false, true => .inr ⟨hb, he, hd⟩
    | false, _, _, _ => absurd law (unbound fun
        | .inl binds => nomatch hb.symm.trans binds.1
        | .inr bounds => nomatch hb.symm.trans bounds.1)
    | true, false, _, _ => absurd law (unbound fun
        | .inl binds => nomatch he.symm.trans binds.2.1
        | .inr bounds => nomatch he.symm.trans bounds.2.1)
    | true, true, false, false => absurd law (unbound fun
        | .inl ⟨_, _, .inl acting⟩ => nomatch ha.symm.trans acting
        | .inl ⟨_, _, .inr ⟨_, dissipative⟩⟩ => nomatch hd.symm.trans dissipative
        | .inr ⟨_, _, dissipative⟩ => nomatch hd.symm.trans dissipative),
   fun binds => (finite_counting_under_counted S).mp fun _ _ _ _ _ quiet _ => quiet binds⟩

/-- In finite worlds, where the counts exist, a change bound from the first step is a law under a
selection exactly when the selection bounds change. -/
theorem finite_change_bound_iff_counted (S : Premise → Bool) :
    (∀ w : World, w.Meets S → w.Finite →
      w.CountsHold fun n c a => ∃ B, ChangeBound 0 B n c a) ↔ BoundsChange S :=
  have replaced : Tally (fun _ => 1) (fun _ => 1) (fun _ => 1) := fun _ => ⟨0, rfl, rfl⟩
  have bounded : ∀ t, (fun _ => 1 : Nat → Nat) t ≤ 1 := fun _ => Nat.le_refl 1
  have recurring : ¬ ∃ B, ChangeBound 0 B (fun _ => 1) (fun _ => 1) (fun _ => 1) :=
    fun ⟨_, bound⟩ => bound.not_recurring fun N => ⟨N, Nat.le_refl N,
      Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_add_right 1 1)⟩
  ⟨fun law => match hb : S .balanced, he : S .embodied, hd : S .dissipative with
    | true, true, true => ⟨hb, he, hd⟩
    | false, _, _ => absurd (law (embodiedRing _ _ 1) (embodiedRing_meets bounded hb)
        (places_listed _) _ _ _ _ (Ring.census bounded _) (embodiedRing_countsOf replaced bounded))
        recurring
    | true, false, _ => absurd (law (ring _ _ 1) (ring_meets bounded he)
        (places_listed _) _ _ _ _ (Ring.census bounded _) (ring_countsOf replaced bounded))
        recurring
    | true, true, false => absurd (law (balancedRing _ _ 1)
        (balancedRing_meets replaced bounded (fun _ _ _ => Nat.zero_lt_one) hd)
        (places_listed _) _ _ _ _ (Ring.census bounded _)
        (balancedRing_countsOf replaced bounded)) recurring,
   fun ⟨balanced, embodied, dissipative⟩ _ meets finite _ _ _ _ census counted =>
    ⟨_, enclosure_bounds_change_counted census counted (meets _ embodied) (meets _ balanced)
      (meets _ dissipative) fun t _ => finite.enclosed t⟩⟩

end World

end Becoming
