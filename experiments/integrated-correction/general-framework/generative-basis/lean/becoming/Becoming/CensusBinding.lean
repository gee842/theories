import Becoming.CensusCounts
import Becoming.Standing

/-!
# Census binding: the laws of counting where the premises bind, where the counts exist

`Becoming.CensusCounts` states the laws of counting under the premises, each selection,
enclosure and finite worlds over counted censuses: the counts of a census taken as relations
(`World.CountsOf`), with no decision procedure for activity and for every property of the counts
(`World.CountsHold`). This module does the same for the laws where the selected premises bind
(`World.binding_counting` and its family in `Becoming.Counting`), which quantify over worlds
`[∀ t x, Decidable (w.web.active t x)]` and hold for pointwise properties only.

* **What binding leaves in the counts.** Where something is active at a step, a counted census
  counts something there (`World.CountsOf.active_pos`); where something arises across a step, it
  counts something arising there (`World.CountsOf.arising_pos`). So where embodiment binds,
  something arises in every counted census (`World.binds_arising_counted`), and under the eight
  premises that is no law (`World.binds_adds_counted`). A selection binding activity needing
  support, only active relata giving or only active relata taking leaves something active
  (`World.CountsOf.acts_of_binding`); binding bounded transmission with only active relata giving
  and embodiment leaves something arising across a step at which something is active
  (`World.CountsOf.joint_of_binding`).
* **The laws where every premise binds**: the tally, nothing arising across a step at which
  nothing is active, and something arising (`World.binding_counting_counted`); in finite worlds
  and in worlds enclosed from some step on, with a change bound from the first step
  (`World.finite_binding_counting_counted`, `World.enclosed_binding_counting_counted`).
* **The laws where the premises of each selection bind**, with the three that binding adds:
  something active, something arising, and something arising across a step at which something is
  active, each where the selection gives it (`World.binding_counting_under_counted`), in finite
  worlds (`World.finite_binding_counting_under_counted`; with the census selected, every property
  is a law vacuously, `World.finite_binding_census_counted`) and under enclosure
  (`World.enclosed_binding_counting_under_counted`); and the equivalences saying where each of the
  three is a law (`…_activity_iff_counted`, `…_arising_iff_counted`, `…_joint_iff_counted`).
* **The rest of the family.** The premises leave counting free, already under every premise but
  embodiment or but balance (`World.counting_free_parts_counted`); balance and embodiment bind
  the counts together, and neither does alone (`World.counting_binds_jointly_counted`); worlds
  enclosed from some step on and finite worlds have the same laws under the eight
  (`World.enclosed_iff_finite_counting_counted`), and under a selection exactly where it bounds
  change and binds counting (`World.enclosed_iff_finite_counting_under_counted`); read on what
  stands, the laws under each selection are those of counted censuses
  (`World.standing_iff_counting_counted`).

Each law is for every property of the counts and with no decidedness. The forward directions
take the binding instances to the relata the counts list; the backward directions use the
witness worlds of `Becoming.Counting`, whose decided marks are counts of their censuses
(`World.countsOf_eq`). Where a procedure decides activity, these laws give the decided ones
(`World.CountsHold.obey`). The decided statements stay, with their scope.
-/

namespace Becoming

namespace World

variable {w : World}

/-- A procedure's marks, equal at each step to given numbers, make those numbers counts of the
census. -/
theorem countsOf_eq [∀ t x, Decidable (w.web.active t x)] {alive : Nat → List w.Relatum}
    {n c a : Nat → Nat}
    (same : ∀ t, (alive t).length = n t ∧
      ceasings (alive t) (fun x s => w.web.active s x) t = c t ∧
      comings (alive (t + 1)) (fun x s => w.web.active s x) t = a t) :
    w.CountsOf alive n c a :=
  FamilyCounts.of_eq (countsOf_decided alive) same

/-- Under the eight premises something arising is no law of counting, where the counts exist:
the empty tally is counted. -/
theorem binds_adds_counted :
    ¬ ∀ w : World, w.Premised → w.CountsHold fun _ _ a => ∃ t, 0 < a t :=
  fun law => match (premised_counting_counted (Q := fun _ _ a => ∃ t, 0 < a t)).mpr law
      (fun _ => 0) (fun _ => 0) (fun _ => 0) (fun _ => ⟨0, rfl, rfl⟩) (fun _ no => no) with
    | ⟨_, no⟩ => Nat.lt_irrefl 0 no

/-- **Where every premise binds, where the counts exist**, the laws of counting under the eight
are the tally, that nothing arises across a step at which nothing is active, and that something
arises: for every property, with no decidedness. -/
theorem binding_counting_counted {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} :
    (∀ n c a, Tally n c a → (∀ t, 0 < a t → 0 < n t) → (∃ t, 0 < a t) → Q n c a) ↔
      ∀ w : World, w.Premised → w.Binds → w.CountsHold Q :=
  census_table_holds₂ binding_counting_sound binding_counting_witnessed

/-- **The laws of counting where the premises of each selection bind, where the counts exist**:
those of `World.counting_under_counted` and three more, something active where activity needing
support, only active relata giving or only active relata taking is selected; something arising
where embodiment is; and something arising across a step at which something is active where
embodiment, only active relata giving and bounded transmission are. For every property, with no
decidedness. -/
theorem binding_counting_under_counted (S : Premise → Bool)
    {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} :
    (∀ n c a, Tally n c a → (BindsCounting S → ∀ t, 0 < a t → 0 < n t) →
      (S .dependent = true ∨ S .acting = true ∨ S .taking = true → ∃ t, 0 < n t) →
      (S .embodied = true → ∃ t, 0 < a t) →
      (S .embodied = true → S .acting = true → S .transmitting = true →
        ∃ t, 0 < n t ∧ 0 < a t) → Q n c a) ↔
      ∀ w : World, w.Meets S → (∀ p, S p = true → p.Binds w) → w.CountsHold Q :=
  have table := census_table_holds (Q := Q) (binding_counting_under_sound S)
    (binding_counting_under_witnessed S)
  ⟨fun law w meets binds => table.mp (fun n c a tally ⟨quiet, acts, arises, joint⟩ =>
      law n c a tally quiet acts arises joint) w ⟨meets, binds⟩,
   fun law n c a tally quiet acts arises joint => table.mpr (fun w ⟨meets, binds⟩ =>
      law w meets binds) n c a tally ⟨quiet, acts, arises, joint⟩⟩

/-- So, where the counts exist, binding adds that something is active exactly where activity
needing support, only active relata giving, only active relata taking or embodiment is
selected. -/
theorem binding_activity_iff_counted (S : Premise → Bool) :
    (∀ w : World, w.Meets S → (∀ p, S p = true → p.Binds w) →
      w.CountsHold fun n _ _ => ∃ t, 0 < n t) ↔
      S .dependent = true ∨ S .acting = true ∨ S .taking = true ∨ S .embodied = true :=
  ⟨fun law => match hp : S .dependent, ha : S .acting, ht : S .taking, he : S .embodied with
    | true, _, _, _ => .inl rfl
    | false, true, _, _ => .inr (.inl rfl)
    | false, false, true, _ => .inr (.inr (.inl rfl))
    | false, false, false, true => .inr (.inr (.inr rfl))
    | false, false, false, false => match (binding_counting_under_counted S
          (Q := fun n _ _ => ∃ t, 0 < n t)).mpr law
        (fun _ => 0) (fun _ => 0) (fun _ => 0) (fun _ => ⟨0, rfl, rfl⟩)
        (fun ⟨_, embodied, _⟩ => nomatch he.symm.trans embodied)
        (fun
          | .inl selected => nomatch hp.symm.trans selected
          | .inr (.inl selected) => nomatch ha.symm.trans selected
          | .inr (.inr selected) => nomatch ht.symm.trans selected)
        (fun selected => nomatch he.symm.trans selected)
        (fun selected => nomatch he.symm.trans selected) with
      | ⟨_, no⟩ => absurd no (Nat.lt_irrefl 0),
   fun selected => (binding_counting_under_counted S (Q := fun n _ _ => ∃ t, 0 < n t)).mp
    fun _ _ _ tally _ acts arises _ => match selected with
    | .inl dependent => acts (.inl dependent)
    | .inr (.inl acting) => acts (.inr (.inl acting))
    | .inr (.inr (.inl taking)) => acts (.inr (.inr taking))
    | .inr (.inr (.inr embodied)) => match arises embodied with
      | ⟨t, joins⟩ => ⟨t + 1, tally.after_pos joins⟩⟩

/-- Where the counts exist, binding adds that something arises exactly where embodiment is
selected. -/
theorem binding_arising_iff_counted (S : Premise → Bool) :
    (∀ w : World, w.Meets S → (∀ p, S p = true → p.Binds w) →
      w.CountsHold fun _ _ a => ∃ t, 0 < a t) ↔ S .embodied = true :=
  ⟨fun law => match he : S .embodied with
    | true => rfl
    | false => match (binding_counting_under_counted S (Q := fun _ _ a => ∃ t, 0 < a t)).mpr law
        (fun _ => 1) (fun _ => 0) (fun _ => 0) (fun _ => ⟨1, rfl, rfl⟩)
        (fun ⟨_, embodied, _⟩ => nomatch he.symm.trans embodied) (fun _ => ⟨0, Nat.zero_lt_one⟩)
        (fun selected => nomatch he.symm.trans selected)
        (fun selected => nomatch he.symm.trans selected) with
      | ⟨_, no⟩ => absurd no (Nat.lt_irrefl 0),
   fun embodied => (binding_counting_under_counted S (Q := fun _ _ a => ∃ t, 0 < a t)).mp
     fun _ _ _ _ _ _ arises _ => arises embodied⟩

/-- And, where the counts exist, that something arises across a step at which something is
active exactly where embodiment is selected and either the selection binds counting or only
active relata giving and bounded transmission are selected. -/
theorem binding_joint_iff_counted (S : Premise → Bool) :
    (∀ w : World, w.Meets S → (∀ p, S p = true → p.Binds w) →
      w.CountsHold fun n _ a => ∃ t, 0 < n t ∧ 0 < a t) ↔
      S .embodied = true ∧ (BindsCounting S ∨ S .acting = true ∧ S .transmitting = true) :=
  ⟨fun law => match he : S .embodied with
    | false => match (binding_counting_under_counted S
          (Q := fun n _ a => ∃ t, 0 < n t ∧ 0 < a t)).mpr law (fun _ => 1) (fun _ => 0)
        (fun _ => 0) (fun _ => ⟨1, rfl, rfl⟩)
        (fun ⟨_, embodied, _⟩ => nomatch he.symm.trans embodied) (fun _ => ⟨0, Nat.zero_lt_one⟩)
        (fun selected => nomatch he.symm.trans selected)
        (fun selected => nomatch he.symm.trans selected) with
      | ⟨_, _, no⟩ => absurd no (Nat.lt_irrefl 0)
    | true => if both : BindsCounting S ∨ S .acting = true ∧ S .transmitting = true then
        ⟨rfl, both⟩
      else match (binding_counting_under_counted S
            (Q := fun n _ a => ∃ t, 0 < n t ∧ 0 < a t)).mpr law Queue.lone (fun _ => 0)
          Queue.joins Queue.lone_tally (fun binds => absurd (.inl binds) both)
          (fun _ => ⟨1, Nat.zero_lt_one⟩) (fun _ => ⟨0, Nat.zero_lt_one⟩)
          (fun _ acting transmitting => absurd (.inr ⟨acting, transmitting⟩) both) with
        | ⟨0, empty, _⟩ => absurd empty (Nat.lt_irrefl 0)
        | ⟨_ + 1, _, no⟩ => absurd no (Nat.lt_irrefl 0),
   fun ⟨embodied, both⟩ => (binding_counting_under_counted S
      (Q := fun n _ a => ∃ t, 0 < n t ∧ 0 < a t)).mp
    fun _ _ _ _ quiet _ arises joint => match both with
    | .inl binds => match arises embodied with
      | ⟨t, joins⟩ => ⟨t, quiet binds t joins, joins⟩
    | .inr ⟨acting, transmitting⟩ => joint embodied acting transmitting⟩

/-- **In finite worlds in which every premise but the census binds, where the counts exist**,
the laws of counting under the eight are those of finite worlds and that something arises: for
every property, with no decidedness. -/
theorem finite_binding_counting_counted {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} :
    (∀ n c a, Tally n c a → (∀ t, 0 < a t → 0 < n t) → (∃ B, ChangeBound 0 B n c a) →
      (∃ t, 0 < a t) → Q n c a) ↔
      ∀ w : World, w.Premised → w.Finite → (∀ p : Premise, p ≠ .counted → p.Binds w) →
        w.CountsHold Q :=
  ⟨fun law _ premised finite binds alive n c a census counted =>
    law n c a (counted.tally census)
      (fun _ => company_of counted fun _ _ comes => active_of_coming_jointly
        (premised _ (.tail _ (.head _))) (premised _ (.tail _ (.tail _ (.head _))))
        (Embodied.arising (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _
          (.head _))))))))
        census comes)
      ⟨_, (enclosure_bounds_change_counted census counted
        (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _)))))))
        (premised _ (.tail _ (.head _)))
        (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _))))))
        (T := 0) fun t _ => finite.enclosed t).from_zero⟩
      (binds_arising_counted (binds .embodied fun same => nomatch same) alive n c a census
        counted),
   fun law n c a tally company ⟨B, bound⟩ ⟨_, joins⟩ =>
    law (finiteQueue n c a B).saturated
      ((finiteQueue_premised tally company bound).saturated
        fun t i => EnclosedQueue.level_le (n := n) (c := c) (a := a) (B := B) t i.val)
      (finiteQueue_finite n c a B) (finiteQueue_saturated_binds tally company bound joins) _ n c a
      (finiteQueue_census n c a B) (countsOf_eq (finiteQueue_counts tally bound))⟩

/-- **Under enclosure from some step on, where every premise binds, where the counts exist**,
the laws of counting are those under enclosure and that something arises: for every property,
with no decidedness. -/
theorem enclosed_binding_counting_counted {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} :
    (∀ n c a, Tally n c a → (∀ t, 0 < a t → 0 < n t) → (∃ B, ChangeBound 0 B n c a) →
      (∃ t, 0 < a t) → Q n c a) ↔
      ∀ w : World, w.Premised → (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) → w.Binds →
        w.CountsHold Q :=
  ⟨fun law _ premised ⟨_, enclosed⟩ binds alive n c a census counted =>
    law n c a (counted.tally census)
      (fun _ => company_of counted fun _ _ comes => active_of_coming_jointly
        (premised _ (.tail _ (.head _))) (premised _ (.tail _ (.tail _ (.head _))))
        (Embodied.arising (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _
          (.head _))))))))
        census comes)
      ⟨_, (enclosure_bounds_change_counted census counted
        (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _)))))))
        (premised _ (.tail _ (.head _)))
        (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _)))))) enclosed).from_zero⟩
      (binds_arising_counted (binds .embodied) alive n c a census counted),
   fun law n c a tally company ⟨B, bound⟩ ⟨_, joins⟩ =>
    law (enclosedQueue n c a B).saturated
      ((enclosedQueue_premised tally company bound).saturated
        fun t k => EnclosedQueue.level_le (n := n) (c := c) (a := a) (B := B) t k)
      ⟨0, fun t _ => enclosedQueue_enclosed tally t⟩
      (enclosedQueue_saturated_binds tally company bound joins) _ n c a
      (enclosedQueue_census n c a B) (countsOf_eq (Queue.counts tally))⟩

/-- No finite world binds the census, so under each selection with the census every property
of the counts is a law in finite worlds where the selected premises bind. -/
theorem finite_binding_census_counted {S : Premise → Bool} (counted : S .counted = true)
    {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} :
    ∀ w : World, w.Meets S → w.Finite → (∀ p, S p = true → p.Binds w) → w.CountsHold Q :=
  fun _ _ finite binds => absurd finite (binds _ counted)

/-- **The laws of counting in finite worlds where the premises of each selection without the
census bind, where the counts exist**: those of `World.finite_counting_under_counted` and the
three that binding adds, the last where embodiment and bounded transmission are selected with
only active relata giving or with both only active relata taking and dissipation. For every
property, with no decidedness. -/
theorem finite_binding_counting_under_counted (S : Premise → Bool) (uncounted : S .counted = false)
    {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} :
    (∀ n c a, Tally n c a → (∃ M, ∀ t, n t ≤ M) →
      (BindsCounting S ∨ BoundsChange S → ∀ t, 0 < a t → 0 < n t) →
      (BoundsChange S → ∃ B, ChangeBound 0 B n c a) →
      (S .dependent = true ∨ S .acting = true ∨ S .taking = true → ∃ t, 0 < n t) →
      (S .embodied = true → ∃ t, 0 < a t) →
      (S .embodied = true → S .acting = true ∨ S .taking = true ∧ S .dissipative = true →
        S .transmitting = true → ∃ t, 0 < n t ∧ 0 < a t) → Q n c a) ↔
      ∀ w : World, w.Meets S → w.Finite → (∀ p, S p = true → p.Binds w) → w.CountsHold Q :=
  ⟨fun law w meets finite binds alive n c a census counted => law n c a (counted.tally census)
    (match finite.census_bounded with
      | ⟨M, bounded⟩ => ⟨M, fun t => Nat.le_trans (Nat.le_of_eq (counted t).1)
          (bounded alive census t)⟩)
    (fun selected _ => company_of counted fun _ _ comes => match selected with
      | .inl ⟨balanced, embodied, .inl acting⟩ => active_of_coming_jointly (meets _ balanced)
          (meets _ acting) (Embodied.arising (meets _ embodied)) census comes
      | .inl ⟨balanced, embodied, .inr ⟨_, dissipative⟩⟩ | .inr ⟨balanced, embodied, dissipative⟩ =>
          active_of_coming_enclosed (meets _ balanced) (meets _ dissipative) (meets _ embodied)
            census (finite.enclosed _) comes)
    (fun ⟨balanced, embodied, dissipative⟩ => ⟨_, enclosure_bounds_change_counted census counted
      (meets _ embodied) (meets _ balanced) (meets _ dissipative) fun t _ => finite.enclosed t⟩)
    (counted.acts_of_binding meets binds census)
    (fun embodied => binds_arising_counted (binds _ embodied) alive n c a census counted)
    (fun embodied giving transmitting =>
      have acting : w.Acting := match giving with
        | .inl acting => meets _ acting
        | .inr ⟨taking, dissipative⟩ => finite.acting (meets _ taking) (meets _ dissipative)
      counted.joint_of_binding (meets _ embodied) acting (binds _ transmitting) census),
   fun law n c a tally ⟨M, bounded⟩ quiet bounds acts arises joint =>
    have holds : ∀ w : World, w.Finite → (∀ p, S p = true → p.Holds w ∧ p.Binds w) →
        w.CountsHold Q := fun w finite binding =>
      law w (fun p selected => (binding p selected).1) finite fun p selected =>
        (binding p selected).2
    have wider : ∀ t, n t ≤ M + 1 := fun t => Nat.le_succ_of_le (bounded t)
    have relayed : S .embodied = false → ∀ U g, (S .dependent = true ∨ S .acting = true ∨
        S .taking = true → (relayRing n c M U g).web.active U g) → Q n c a :=
      fun disembodied U g active =>
        holds (relayRing n c M U g) (places_listed _)
          (relayRing_binding disembodied uncounted active) _ n c a
          (Ring.census wider fun t i => RelayRing.level U t i.val)
          (countsOf_eq (Ring.counts tally wider))
    match he : S .embodied with
    | false => match hp : S .dependent, ha : S .acting, ht : S .taking with
      | false, false, false => relayed he 0 (RelayRing.sink M) fun
          | .inl selected => nomatch hp.symm.trans selected
          | .inr (.inl selected) => nomatch ha.symm.trans selected
          | .inr (.inr selected) => nomatch ht.symm.trans selected
      | true, _, _ => match acts (.inl hp) with
        | ⟨U, occupied⟩ => relayed he U (Ring.seat (M + 1) (Queue.gone c U)) fun _ =>
            Ring.front_holds occupied
      | false, true, _ => match acts (.inr (.inl ha)) with
        | ⟨U, occupied⟩ => relayed he U (Ring.seat (M + 1) (Queue.gone c U)) fun _ =>
            Ring.front_holds occupied
      | false, false, true => match acts (.inr (.inr ht)) with
        | ⟨U, occupied⟩ => relayed he U (Ring.seat (M + 1) (Queue.gone c U)) fun _ =>
            Ring.front_holds occupied
    | true => match arises he with
      | ⟨T, joins⟩ =>
        have exchanging : S .dissipative = false → (S .acting = true → ∀ t, 0 < a t → 0 < n t) →
            Q n c a := fun dissipating giving =>
          holds (exchangingRing n c M (T + 1)) (places_listed _)
            (exchangingRing_binding tally bounded joins dissipating uncounted giving) _ n c a
            (Ring.census bounded (Ring.stands n c M)) (countsOf_eq (Ring.counts tally bounded))
        have lossy : ∀ J U, 0 < a J → S .balanced = false →
            (S .acting = true ∨ S .taking = true → 0 < n U) → (S .transmitting = true → J = U) →
            Q n c a := fun _ U joins unbalanced occupied descends =>
          holds (lossyRing n c M U) (places_listed _)
            (lossyRing_binding tally bounded joins unbalanced uncounted occupied descends) _ n c a
            (Ring.census bounded (Ring.stands n c M)) (countsOf_eq (Ring.counts tally bounded))
        match hb : S .balanced, hd : S .dissipative, ha : S .acting, ht : S .taking,
            hr : S .transmitting with
        | true, true, _, _, _ => match bounds ⟨hb, he, hd⟩ with
          | ⟨B, bound⟩ =>
            have company := quiet (.inr ⟨hb, he, hd⟩)
            law (finiteQueue n c a B).saturated
              (((finiteQueue_premised tally company bound).saturated
                fun t i => EnclosedQueue.level_le (n := n) (c := c) (a := a) (B := B) t i.val).meets S)
              (finiteQueue_finite n c a B)
              (fun p selected => finiteQueue_saturated_binds tally company bound joins p
                fun same => absurd (uncounted.symm.trans (same ▸ selected)) Bool.noConfusion)
              _ n c a (finiteQueue_census n c a B) (countsOf_eq (finiteQueue_counts tally bound))
        | true, false, _, _, _ => exchanging hd fun acting => quiet (.inl ⟨hb, he, .inl acting⟩)
        | false, false, false, _, _ => exchanging hd fun selected => nomatch ha.symm.trans selected
        | false, _, true, _, true => match joint he (.inl ha) hr with
          | ⟨U, occupied, here⟩ => lossy U U here hb (fun _ => occupied) fun _ => rfl
        | false, true, false, true, true => match joint he (.inr ⟨ht, hd⟩) hr with
          | ⟨U, occupied, here⟩ => lossy U U here hb (fun _ => occupied) fun _ => rfl
        | false, _, true, _, false => lossy T (T + 1) joins hb (fun _ => tally.after_pos joins)
            fun selected => nomatch hr.symm.trans selected
        | false, true, false, true, false => lossy T (T + 1) joins hb
            (fun _ => tally.after_pos joins) fun selected => nomatch hr.symm.trans selected
        | false, true, false, false, _ => lossy T T joins hb (fun
            | .inl selected => nomatch ha.symm.trans selected
            | .inr selected => nomatch ht.symm.trans selected) fun _ => rfl⟩

/-- So, where the counts exist, in finite worlds where the premises of a selection without the
census bind, something is active exactly where activity needing support, only active relata
giving, only active relata taking or embodiment is selected. -/
theorem finite_binding_activity_iff_counted (S : Premise → Bool) (uncounted : S .counted = false) :
    (∀ w : World, w.Meets S → w.Finite → (∀ p, S p = true → p.Binds w) →
      w.CountsHold fun n _ _ => ∃ t, 0 < n t) ↔
      S .dependent = true ∨ S .acting = true ∨ S .taking = true ∨ S .embodied = true :=
  ⟨fun law => match hp : S .dependent, ha : S .acting, ht : S .taking, he : S .embodied with
    | true, _, _, _ => .inl rfl
    | false, true, _, _ => .inr (.inl rfl)
    | false, false, true, _ => .inr (.inr (.inl rfl))
    | false, false, false, true => .inr (.inr (.inr rfl))
    | false, false, false, false => match (finite_binding_counting_under_counted S uncounted
          (Q := fun n _ _ => ∃ t, 0 < n t)).mpr law (fun _ => 0) (fun _ => 0) (fun _ => 0)
        (fun _ => ⟨0, rfl, rfl⟩)
        ⟨0, fun _ => Nat.le_refl 0⟩ (fun _ _ no => absurd no (Nat.lt_irrefl 0))
        (fun ⟨_, embodied, _⟩ => nomatch he.symm.trans embodied)
        (fun
          | .inl selected => nomatch hp.symm.trans selected
          | .inr (.inl selected) => nomatch ha.symm.trans selected
          | .inr (.inr selected) => nomatch ht.symm.trans selected)
        (fun selected => nomatch he.symm.trans selected)
        (fun selected => nomatch he.symm.trans selected) with
      | ⟨_, no⟩ => absurd no (Nat.lt_irrefl 0),
   fun selected => (finite_binding_counting_under_counted S uncounted
      (Q := fun n _ _ => ∃ t, 0 < n t)).mp
    fun _ _ _ tally _ _ _ acts arises _ => match selected with
    | .inl dependent => acts (.inl dependent)
    | .inr (.inl acting) => acts (.inr (.inl acting))
    | .inr (.inr (.inl taking)) => acts (.inr (.inr taking))
    | .inr (.inr (.inr embodied)) => match arises embodied with
      | ⟨t, joins⟩ => ⟨t + 1, tally.after_pos joins⟩⟩

/-- Where the counts exist, in such finite worlds something arises exactly where embodiment is
selected. -/
theorem finite_binding_arising_iff_counted (S : Premise → Bool) (uncounted : S .counted = false) :
    (∀ w : World, w.Meets S → w.Finite → (∀ p, S p = true → p.Binds w) →
      w.CountsHold fun _ _ a => ∃ t, 0 < a t) ↔ S .embodied = true :=
  ⟨fun law => match he : S .embodied with
    | true => rfl
    | false => match (finite_binding_counting_under_counted S uncounted
          (Q := fun _ _ a => ∃ t, 0 < a t)).mpr law (fun _ => 1)
        (fun _ => 0) (fun _ => 0) (fun _ => ⟨1, rfl, rfl⟩) ⟨1, fun _ => Nat.le_refl 1⟩
        (fun _ _ _ => Nat.zero_lt_one)
        (fun ⟨_, embodied, _⟩ => nomatch he.symm.trans embodied) (fun _ => ⟨0, Nat.zero_lt_one⟩)
        (fun selected => nomatch he.symm.trans selected)
        (fun selected => nomatch he.symm.trans selected) with
      | ⟨_, no⟩ => absurd no (Nat.lt_irrefl 0),
   fun embodied => (finite_binding_counting_under_counted S uncounted
      (Q := fun _ _ a => ∃ t, 0 < a t)).mp
     fun _ _ _ _ _ _ _ _ arises _ => arises embodied⟩

/-- And, where the counts exist, that something arises across a step at which something is
active exactly where embodiment is selected and either the selection binds counting or bounds
change, or bounded transmission is selected with only active relata giving or with both only
active relata taking and dissipation. -/
theorem finite_binding_joint_iff_counted (S : Premise → Bool) (uncounted : S .counted = false) :
    (∀ w : World, w.Meets S → w.Finite → (∀ p, S p = true → p.Binds w) →
      w.CountsHold fun n _ a => ∃ t, 0 < n t ∧ 0 < a t) ↔
      S .embodied = true ∧ (BindsCounting S ∨ BoundsChange S ∨
        (S .acting = true ∨ S .taking = true ∧ S .dissipative = true) ∧
          S .transmitting = true) :=
  ⟨fun law => match he : S .embodied with
    | false => match (finite_binding_counting_under_counted S uncounted
          (Q := fun n _ a => ∃ t, 0 < n t ∧ 0 < a t)).mpr law (fun _ => 1)
        (fun _ => 0) (fun _ => 0) (fun _ => ⟨1, rfl, rfl⟩) ⟨1, fun _ => Nat.le_refl 1⟩
        (fun _ _ _ => Nat.zero_lt_one)
        (fun ⟨_, embodied, _⟩ => nomatch he.symm.trans embodied) (fun _ => ⟨0, Nat.zero_lt_one⟩)
        (fun selected => nomatch he.symm.trans selected)
        (fun selected => nomatch he.symm.trans selected) with
      | ⟨_, _, no⟩ => absurd no (Nat.lt_irrefl 0)
    | true => if both : BindsCounting S ∨ BoundsChange S ∨
          (S .acting = true ∨ S .taking = true ∧ S .dissipative = true) ∧
            S .transmitting = true then ⟨rfl, both⟩
      else match (finite_binding_counting_under_counted S uncounted
            (Q := fun n _ a => ∃ t, 0 < n t ∧ 0 < a t)).mpr law Queue.lone
          (fun _ => 0) Queue.joins Queue.lone_tally
          ⟨1, fun | 0 => Nat.zero_le 1 | _ + 1 => Nat.le_refl 1⟩
          (fun bound => absurd (match bound with
            | .inl binds => .inl binds
            | .inr bounds => .inr (.inl bounds)) both)
          (fun bounds => absurd (.inr (.inl bounds)) both) (fun _ => ⟨1, Nat.zero_lt_one⟩)
          (fun _ => ⟨0, Nat.zero_lt_one⟩)
          (fun _ giving transmitting => absurd (.inr (.inr ⟨giving, transmitting⟩)) both) with
        | ⟨0, empty, _⟩ => absurd empty (Nat.lt_irrefl 0)
        | ⟨_ + 1, _, no⟩ => absurd no (Nat.lt_irrefl 0),
   fun ⟨embodied, both⟩ => (finite_binding_counting_under_counted S uncounted
      (Q := fun n _ a => ∃ t, 0 < n t ∧ 0 < a t)).mp
    fun _ _ _ _ _ quiet _ _ arises joint => match both with
    | .inl binds => match arises embodied with
      | ⟨t, joins⟩ => ⟨t, quiet (.inl binds) t joins, joins⟩
    | .inr (.inl bounds) => match arises embodied with
      | ⟨t, joins⟩ => ⟨t, quiet (.inr bounds) t joins, joins⟩
    | .inr (.inr ⟨giving, transmitting⟩) => joint embodied giving transmitting⟩

/-- **The laws of counting under enclosure from some step on, where the premises of each
selection bind, where the counts exist**: those of `World.enclosed_counting_under_counted` and
the three of `World.binding_counting_under_counted`, each on its own. For every property, with
no decidedness. -/
theorem enclosed_binding_counting_under_counted (S : Premise → Bool)
    {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} :
    (∀ n c a, Tally n c a → (BindsCounting S → ∀ t, 0 < a t → 0 < n t) →
      (BoundsChange S → ∃ T B, ChangeBound T B n c a ∧ ∀ t, T ≤ t → 0 < a t → 0 < n t) →
      (S .dependent = true ∨ S .acting = true ∨ S .taking = true → ∃ t, 0 < n t) →
      (S .embodied = true → ∃ t, 0 < a t) →
      (S .embodied = true → S .acting = true → S .transmitting = true →
        ∃ t, 0 < n t ∧ 0 < a t) → Q n c a) ↔
      ∀ w : World, w.Meets S → (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) →
        (∀ p, S p = true → p.Binds w) → w.CountsHold Q :=
  ⟨fun law _ meets ⟨T, enclosed⟩ binds alive n c a census counted =>
    law n c a (counted.tally census)
    (fun bindsCounting => counted.company_binding meets bindsCounting census)
    (fun ⟨balanced, embodied, dissipative⟩ => ⟨T, _, enclosure_bounds_change_counted census
      counted (meets _ embodied) (meets _ balanced) (meets _ dissipative) enclosed,
      fun t later => company_of counted fun _ _ comes => active_of_coming_enclosed
        (meets _ balanced) (meets _ dissipative) (meets _ embodied) census (enclosed t later)
        comes⟩)
    (counted.acts_of_binding meets binds census)
    (fun embodied => binds_arising_counted (binds _ embodied) alive n c a census counted)
    (fun embodied acting transmitting => counted.joint_of_binding (meets _ embodied)
      (meets _ acting) (binds _ transmitting) census),
   fun law n c a tally quiet bounded acts arises joint =>
    have holds : ∀ w : World, (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) →
        (∀ p, S p = true → p.Holds w ∧ p.Binds w) → w.CountsHold Q := fun w enclosed binding =>
      law w (fun p selected => (binding p selected).1) enclosed
        fun p selected => (binding p selected).2
    have relayed : S .embodied = false → ∀ U g, (S .dependent = true ∨ S .acting = true ∨
        S .taking = true → (relayQueue n c U g).web.active U g) → Q n c a :=
      fun disembodied _ _ active =>
        holds _ ⟨0, fun t _ => relayQueue_enclosed n c _ _ t⟩
          (relayQueue_binding disembodied active) _ n c a (openQueue_census n c)
          (countsOf_eq (openQueue_counts tally))
    have lossy : ∀ (T U E : Nat) (gift : Nat → Nat), 0 < a T → 0 < n U → gift U = 0 →
        (∀ t, E ≤ t → gift t = 0) → S .balanced = false →
        (S .acting = true → ∀ t, gift t = 0) →
        (S .transmitting = true → T = U ∨ 0 < gift T) → Q n c a :=
      fun _ _ _ _ joins occupied shut still unbalanced giving descends =>
        holds _ ⟨_, fun _ later => lossyQueue_enclosed tally occupied (still _ later)⟩
          (lossyQueue_binding tally occupied joins shut unbalanced giving descends) _ n c a
          (openQueue_census n c) (countsOf_eq (openQueue_counts tally))
    match he : S .embodied with
    | false => match hp : S .dependent, ha : S .acting, ht : S .taking with
      | false, false, false => relayed he 0 (.ground 1) fun
          | .inl selected => nomatch hp.symm.trans selected
          | .inr (.inl selected) => nomatch ha.symm.trans selected
          | .inr (.inr selected) => nomatch ht.symm.trans selected
      | true, _, _ => match acts (.inl hp) with
        | ⟨U, occupied⟩ => relayed he U (.member (Queue.gone c U)) fun _ =>
            OpenQueue.front.mpr occupied
      | false, true, _ => match acts (.inr (.inl ha)) with
        | ⟨U, occupied⟩ => relayed he U (.member (Queue.gone c U)) fun _ =>
            OpenQueue.front.mpr occupied
      | false, false, true => match acts (.inr (.inr ht)) with
        | ⟨U, occupied⟩ => relayed he U (.member (Queue.gone c U)) fun _ =>
            OpenQueue.front.mpr occupied
    | true => match arises he with
      | ⟨T, joins⟩ =>
        have saturated : S .balanced = true → S .dissipative = true →
            (∀ t, 0 < a t → 0 < n t) → Q n c a := fun hb hd company =>
          match changeBound_iff_zero.mp (match bounded ⟨hb, he, hd⟩ with
            | ⟨T, B, bound, _⟩ => ⟨T, B, bound⟩) with
          | ⟨B, bound⟩ =>
              holds (enclosedQueue n c a B).saturated
                ⟨0, fun t _ => enclosedQueue_enclosed tally t⟩
                (fun p selected => ⟨((enclosedQueue_premised tally company bound).saturated
                    fun t k => EnclosedQueue.level_le (n := n) (c := c) (a := a) t k).meets S p
                      selected,
                  enclosedQueue_saturated_binds tally company bound joins p⟩)
                _ n c a (enclosedQueue_census n c a B) (countsOf_eq (Queue.counts tally))
        match hb : S .balanced, hd : S .dissipative, ha : S .acting, ht : S .taking,
            hr : S .transmitting with
        | true, false, _, _, _ =>
            holds _ ⟨0, fun t _ => exchangingQueue_enclosed tally (tally.after_pos joins) t⟩
              (exchangingQueue_binding (B := 0) tally joins hd fun selected =>
                quiet ⟨hb, he, .inl selected⟩) _ n c a Queue.listed
              (countsOf_eq (Queue.counts tally))
        | true, true, true, _, _ => saturated hb hd (quiet ⟨hb, he, .inl ha⟩)
        | true, true, false, true, _ => saturated hb hd (quiet ⟨hb, he, .inr ⟨ht, hd⟩⟩)
        | true, true, false, false, _ => match bounded ⟨hb, he, hd⟩ with
          | ⟨_, _, bound, company⟩ => match tally.occupied_from company joins with
            | ⟨_, occupied, company⟩ =>
                holds _ ⟨_, fun _ later => sheddingQueue_enclosed tally occupied later⟩
                  (sheddingQueue_binding tally bound.from_zero company occupied joins ha ht) _ n c a
                  Queue.listed (countsOf_eq (Queue.counts tally))
        | false, _, true, _, true => match joint he ha hr with
          | ⟨U, occupied, here⟩ => lossy U U 0 (fun _ => 0) here occupied rfl (fun _ _ => rfl)
              hb (fun _ _ => rfl) fun _ => .inl rfl
        | false, _, true, _, false => lossy T (T + 1) 0 (fun _ => 0) joins (tally.after_pos joins)
            rfl (fun _ _ => rfl) hb (fun _ _ => rfl)
            fun selected => nomatch hr.symm.trans selected
        | false, _, false, _, _ => lossy T (T + 1) (T + 1) (fun t => mark (t = T)) joins
            (tally.after_pos joins) (mark_zero (Nat.succ_ne_self T))
            (fun _ later => mark_zero fun same =>
              Nat.not_succ_le_self T (Nat.le_trans later (Nat.le_of_eq same)))
            hb (fun selected => nomatch ha.symm.trans selected)
            fun _ => .inr (mark_pos.mpr rfl)⟩

/-- So, where the counts exist, in worlds enclosed from some step on where the premises of a
selection bind, something is active exactly where activity needing support, only active relata
giving, only active relata taking or embodiment is selected. -/
theorem enclosed_binding_activity_iff_counted (S : Premise → Bool) :
    (∀ w : World, w.Meets S → (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) →
      (∀ p, S p = true → p.Binds w) → w.CountsHold fun n _ _ => ∃ t, 0 < n t) ↔
      S .dependent = true ∨ S .acting = true ∨ S .taking = true ∨ S .embodied = true :=
  ⟨fun law => match hp : S .dependent, ha : S .acting, ht : S .taking, he : S .embodied with
    | true, _, _, _ => .inl rfl
    | false, true, _, _ => .inr (.inl rfl)
    | false, false, true, _ => .inr (.inr (.inl rfl))
    | false, false, false, true => .inr (.inr (.inr rfl))
    | false, false, false, false => match (enclosed_binding_counting_under_counted S
          (Q := fun n _ _ => ∃ t, 0 < n t)).mpr law
        (fun _ => 0) (fun _ => 0) (fun _ => 0) (fun _ => ⟨0, rfl, rfl⟩)
        (fun ⟨_, embodied, _⟩ => nomatch he.symm.trans embodied)
        (fun ⟨_, embodied, _⟩ => nomatch he.symm.trans embodied)
        (fun
          | .inl selected => nomatch hp.symm.trans selected
          | .inr (.inl selected) => nomatch ha.symm.trans selected
          | .inr (.inr selected) => nomatch ht.symm.trans selected)
        (fun selected => nomatch he.symm.trans selected)
        (fun selected => nomatch he.symm.trans selected) with
      | ⟨_, no⟩ => absurd no (Nat.lt_irrefl 0),
   fun selected => (enclosed_binding_counting_under_counted S
      (Q := fun n _ _ => ∃ t, 0 < n t)).mp
    fun _ _ _ tally _ _ acts arises _ => match selected with
    | .inl dependent => acts (.inl dependent)
    | .inr (.inl acting) => acts (.inr (.inl acting))
    | .inr (.inr (.inl taking)) => acts (.inr (.inr taking))
    | .inr (.inr (.inr embodied)) => match arises embodied with
      | ⟨t, joins⟩ => ⟨t + 1, tally.after_pos joins⟩⟩

/-- Where the counts exist, in such worlds something arises exactly where embodiment is
selected. -/
theorem enclosed_binding_arising_iff_counted (S : Premise → Bool) :
    (∀ w : World, w.Meets S → (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) →
      (∀ p, S p = true → p.Binds w) → w.CountsHold fun _ _ a => ∃ t, 0 < a t) ↔
      S .embodied = true :=
  ⟨fun law => match he : S .embodied with
    | true => rfl
    | false => match (enclosed_binding_counting_under_counted S
          (Q := fun _ _ a => ∃ t, 0 < a t)).mpr law (fun _ => 1)
        (fun _ => 0) (fun _ => 0) (fun _ => ⟨1, rfl, rfl⟩)
        (fun ⟨_, embodied, _⟩ => nomatch he.symm.trans embodied)
        (fun ⟨_, embodied, _⟩ => nomatch he.symm.trans embodied) (fun _ => ⟨0, Nat.zero_lt_one⟩)
        (fun selected => nomatch he.symm.trans selected)
        (fun selected => nomatch he.symm.trans selected) with
      | ⟨_, no⟩ => absurd no (Nat.lt_irrefl 0),
   fun embodied => (enclosed_binding_counting_under_counted S
      (Q := fun _ _ a => ∃ t, 0 < a t)).mp
     fun _ _ _ _ _ _ _ arises _ => arises embodied⟩

/-- And, where the counts exist, that something arises across a step at which something is
active exactly where embodiment is selected and either the selection binds counting or selects
only active relata giving and bounded transmission, as where nothing is enclosed. -/
theorem enclosed_binding_joint_iff_counted (S : Premise → Bool) :
    (∀ w : World, w.Meets S → (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) →
      (∀ p, S p = true → p.Binds w) → w.CountsHold fun n _ a => ∃ t, 0 < n t ∧ 0 < a t) ↔
      S .embodied = true ∧ (BindsCounting S ∨ S .acting = true ∧ S .transmitting = true) :=
  ⟨fun law => match he : S .embodied with
    | false => match (enclosed_binding_counting_under_counted S
          (Q := fun n _ a => ∃ t, 0 < n t ∧ 0 < a t)).mpr law (fun _ => 1)
        (fun _ => 0) (fun _ => 0) (fun _ => ⟨1, rfl, rfl⟩)
        (fun ⟨_, embodied, _⟩ => nomatch he.symm.trans embodied)
        (fun ⟨_, embodied, _⟩ => nomatch he.symm.trans embodied) (fun _ => ⟨0, Nat.zero_lt_one⟩)
        (fun selected => nomatch he.symm.trans selected)
        (fun selected => nomatch he.symm.trans selected) with
      | ⟨_, _, no⟩ => absurd no (Nat.lt_irrefl 0)
    | true => if both : BindsCounting S ∨ S .acting = true ∧ S .transmitting = true then
        ⟨rfl, both⟩
      else match (enclosed_binding_counting_under_counted S
            (Q := fun n _ a => ∃ t, 0 < n t ∧ 0 < a t)).mpr law Queue.lone (fun _ => 0)
          Queue.joins Queue.lone_tally (fun binds => absurd (.inl binds) both)
          (fun _ => ⟨1, 1, Queue.lone_settles, fun
            | 0, early, _ => absurd early (Nat.not_succ_le_zero 0)
            | _ + 1, _, _ => Nat.zero_lt_one⟩) (fun _ => ⟨1, Nat.zero_lt_one⟩)
          (fun _ => ⟨0, Nat.zero_lt_one⟩)
          (fun _ acting transmitting => absurd (.inr ⟨acting, transmitting⟩) both) with
        | ⟨0, empty, _⟩ => absurd empty (Nat.lt_irrefl 0)
        | ⟨_ + 1, _, no⟩ => absurd no (Nat.lt_irrefl 0),
   fun ⟨embodied, both⟩ => (enclosed_binding_counting_under_counted S
      (Q := fun n _ a => ∃ t, 0 < n t ∧ 0 < a t)).mp
    fun _ _ _ _ quiet _ _ arises joint => match both with
    | .inl binds => match arises embodied with
      | ⟨t, joins⟩ => ⟨t, quiet binds t joins, joins⟩
    | .inr ⟨acting, transmitting⟩ => joint embodied acting transmitting⟩

/-- **The premises leave counting free, where the counts exist**: a property of the counts holds
of every tally exactly when it holds of every counted census of every world meeting every
premise but embodiment, and of every world meeting every premise but balance. For every
property, with no decidedness. -/
theorem counting_free_parts_counted {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} :
    ((∀ n c a, Tally n c a → Q n c a) ↔
      ∀ w : World, w.Dependent → w.Balanced → w.Acting → w.Taking → w.Dissipative →
        w.Transmitting → w.CountsHold Q) ∧
    ((∀ n c a, Tally n c a → Q n c a) ↔
      ∀ w : World, w.Dependent → w.Acting → w.Taking → w.Dissipative → w.Embodied →
        w.Transmitting → w.CountsHold Q) :=
  ⟨⟨fun law w _ _ _ _ _ _ => counting_free_counted.mp law w, fun law n c a tally =>
      match queue_premised n c with
      | ⟨dependent, balanced, acting, taking, dissipative, _, transmitting⟩ =>
        law (queue n c) dependent balanced acting taking dissipative transmitting _ n c a
          Queue.listed (queue_countsOf tally)⟩,
   ⟨fun law w _ _ _ _ _ _ => counting_free_counted.mp law w, fun law n c a tally =>
      match embodiedQueue_premised n c with
      | ⟨dependent, acting, taking, dissipative, embodied, _, transmitting⟩ =>
        law (embodiedQueue n c) dependent acting taking dissipative embodied transmitting _ n c a
          Queue.listed (embodiedQueue_countsOf tally)⟩⟩

/-- **Together, balance and embodiment bind the counts, where the counts exist.** Where the flow
balances, only active relata give and whatever arises is embodied, nothing arises across a step
at which nothing is active, in every counted census. One relatum arising from none is counted by a
queue meeting every premise but embodiment, and by one meeting every premise but balance. -/
theorem counting_binds_jointly_counted :
    (∀ w : World, w.Balanced → w.Acting → w.ArisingEmbodied →
      w.CountsHold fun n _ a => ∀ t, 0 < a t → 0 < n t) ∧
    ¬ (queue Queue.lone fun _ => 0).CountsHold (fun n _ a => ∀ t, 0 < a t → 0 < n t) ∧
    ¬ (embodiedQueue Queue.lone fun _ => 0).CountsHold
      (fun n _ a => ∀ t, 0 < a t → 0 < n t) :=
  ⟨fun _ balanced acting embodied _ _ _ _ census counted _ =>
    company_of counted fun _ _ comes => active_of_coming_jointly balanced acting embodied census comes,
   fun obeys => Nat.lt_irrefl 0
    (obeys _ _ _ _ Queue.listed (queue_countsOf Queue.lone_tally) 0 Nat.zero_lt_one),
   fun obeys => Nat.lt_irrefl 0
    (obeys _ _ _ _ Queue.listed (embodiedQueue_countsOf Queue.lone_tally) 0 Nat.zero_lt_one)⟩

/-- So, where the counts exist, under the eight premises worlds enclosed from some step on and
finite worlds have the same laws of counting. -/
theorem enclosed_iff_finite_counting_counted
    {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} :
    (∀ w : World, w.Premised → (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) → w.CountsHold Q) ↔
      ∀ w : World, w.Premised → w.Finite → w.CountsHold Q :=
  enclosed_counting_counted.symm.trans finite_counting_counted

/-- Where the counts exist, finite worlds and worlds enclosed from some step on have the same laws
of counting under a selection exactly when it bounds change and binds counting. -/
theorem enclosed_iff_finite_counting_under_counted (S : Premise → Bool) :
    (∀ Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop,
      ((∀ w : World, w.Meets S → (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) → w.CountsHold Q) ↔
        ∀ w : World, w.Meets S → w.Finite → w.CountsHold Q)) ↔
      BoundsChange S ∧ BindsCounting S :=
  have growing : ¬ BoundsChange S → ¬ ∀ Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop,
      ((∀ w : World, w.Meets S → (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) → w.CountsHold Q) ↔
        ∀ w : World, w.Meets S → w.Finite → w.CountsHold Q) := fun free law =>
    match (enclosed_counting_under_counted S (Q := fun n _ _ => ∃ M, ∀ t, n t ≤ M)).mpr
        ((law _).mpr fun _ _ finite alive _ _ _ census counted =>
          match finite.census_bounded with
          | ⟨M, bounded⟩ => ⟨M, fun t => Nat.le_trans (Nat.le_of_eq (counted t).1)
              (bounded alive census t)⟩)
        (fun t => t + 1) (fun _ => 0) (fun _ => 1) (fun t => ⟨t + 1, rfl, rfl⟩)
        (fun _ _ _ => Nat.succ_pos _) (fun bounds => absurd bounds free) with
    | ⟨M, bounded⟩ => Nat.lt_irrefl M (bounded M)
  have arising : BoundsChange S → ¬ BindsCounting S → ¬ ∀ Q : (Nat → Nat) → (Nat → Nat) →
      (Nat → Nat) → Prop,
      ((∀ w : World, w.Meets S → (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) → w.CountsHold Q) ↔
        ∀ w : World, w.Meets S → w.Finite → w.CountsHold Q) := fun bounds free law =>
    Nat.lt_irrefl 0 ((enclosed_counting_under_counted S
        (Q := fun n _ a => ∀ t, 0 < a t → 0 < n t)).mpr ((law _).mpr
        ((finite_counting_binds_iff_counted S).mpr (.inr bounds))) _ _ _ Queue.lone_tally
      (fun binds => absurd binds free)
      (fun _ => ⟨1, 1, Queue.lone_settles, fun t later pos => match t, later, pos with
        | 0, later, _ => absurd later (Nat.not_succ_le_zero 0)
        | _ + 1, _, pos => absurd pos (Nat.lt_irrefl 0)⟩)
      0 Nat.zero_lt_one)
  ⟨fun law => match hb : S .balanced, he : S .embodied, hd : S .dissipative, ha : S .acting,
      ht : S .taking with
    | true, true, true, true, _ => ⟨⟨hb, he, hd⟩, ⟨hb, he, .inl ha⟩⟩
    | true, true, true, false, true => ⟨⟨hb, he, hd⟩, ⟨hb, he, .inr ⟨ht, hd⟩⟩⟩
    | true, true, true, false, false => absurd law (arising ⟨hb, he, hd⟩ fun
        | ⟨_, _, .inl acting⟩ => nomatch ha.symm.trans acting
        | ⟨_, _, .inr ⟨taking, _⟩⟩ => nomatch ht.symm.trans taking)
    | false, _, _, _, _ => absurd law (growing fun bounds => nomatch hb.symm.trans bounds.1)
    | true, false, _, _, _ => absurd law (growing fun bounds => nomatch he.symm.trans bounds.2.1)
    | true, true, false, _, _ =>
      absurd law (growing fun bounds => nomatch hd.symm.trans bounds.2.2),
   fun ⟨bounds, binds⟩ _ => (enclosed_counting_under_counted S).symm.trans
    (Iff.trans ⟨fun law n c a tally _ quiet bounded => law n c a tally (fun _ => quiet (.inl binds))
        fun _ => match bounded bounds with
          | ⟨_, bound⟩ => ⟨0, _, bound, fun t _ => quiet (.inl binds) t⟩,
      fun law n c a tally quiet bounded => match bounded bounds with
        | ⟨_, _, bound, _⟩ => law n c a tally ⟨_, fun t => Nat.le_trans (Nat.le_add_right _ _)
            (bound.from_zero t (Nat.zero_le t))⟩ (fun _ => quiet binds)
            (fun _ => ⟨_, bound.from_zero⟩)⟩
      (finite_counting_under_counted S))⟩

/-- **Read on what stands, where the counts exist**: under each selection, a pointwise property
holds of what stands in every world meeting it exactly when it holds of every counted census of
every world meeting it. The pointwise condition belongs to the reading on what stands; the
counted side needs none. -/
theorem standing_iff_counting_counted (S : Premise → Bool)
    {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} (pointwise : Pointwise Q) :
    (∀ w : World, w.Meets S → w.StandsObey Q) ↔ ∀ w : World, w.Meets S → w.CountsHold Q :=
  (standing_counting_under S pointwise).symm.trans (counting_under_counted S)

end World

end Becoming
