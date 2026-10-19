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
(`World.ceasings_exist_iff`, `World.comings_exist_iff`), and, the census listing what is active,
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

/-- Adding the same on the right cancels. -/
theorem cancel_add_right {a b : Nat} : ∀ c : Nat, a + c = b + c → a = b
  | 0, same => same
  | c + 1, same => cancel_add_right c (Nat.succ.inj same)

/-- Two numbers balancing across a step, the ceased among those before it, are a tally there. -/
theorem tally_step {n n' c a : Nat} (le : c ≤ n) (across : n' + c = n + a) :
    ∃ k, n = k + c ∧ n' = k + a :=
  match exists_add_of_le le with
  | ⟨k, before⟩ =>
    ⟨k, before, cancel_add_right c (across.trans
      ((congrArg (· + a) before).trans (Nat.add_right_comm k c a)))⟩

/-- What a listed family counts across each step, as relations: `n` counts what holds at each
step, `c` what of it ceases across the step, `a` what holds after the step and came to be across
it. -/
def FamilyCounts (p : α → Nat → Prop) (l : Nat → List α) (n c a : Nat → Nat) : Prop :=
  ∀ t, n t = (l t).length ∧ Counts (l t) (fun x => CeasesToBe (p x) t) (c t) ∧
    Counts (l (t + 1)) (fun x => ComesToBe (p x) t) (a t)

/-- **The counts of a listed family are a tally**, with no decidedness. -/
theorem FamilyCounts.tally {p : α → Nat → Prop} {l : Nat → List α} {n c a : Nat → Nat}
    (listed : Listed p l) (counted : FamilyCounts p l n c a) : Tally n c a := fun t =>
  match counted t, counted (t + 1) with
  | ⟨length, ceased, came⟩, ⟨length', _, _⟩ =>
    have across : (l (t + 1)).length + c t = (l t).length + a t :=
      Counts.listed_across (p := p) (listed t) (listed (t + 1)) ceased came
    match tally_step (Nat.le_trans ceased.le_length (Nat.le_of_eq length.symm))
      ((congrArg (· + c t) length').trans (across.trans (congrArg (· + a t) length.symm))) with
    | ⟨k, before, after⟩ => ⟨k, before, after⟩

/-- Where a procedure decides, its marks are the counts of a listed family. -/
theorem familyCounts_decided {p : α → Nat → Prop} [∀ x t, Decidable (p x t)] (l : Nat → List α) :
    FamilyCounts p l (fun t => (l t).length) (fun t => ceasings (l t) p t)
      (fun t => comings (l (t + 1)) p t) :=
  fun t => ⟨rfl, ceasings_counts t, comings_counts t⟩

/-- Counts given by values agreeing with them at each step are counts. -/
theorem FamilyCounts.of_eq {p : α → Nat → Prop} {l : Nat → List α} {n c a n' c' a' : Nat → Nat}
    (counted : FamilyCounts p l n c a) (same : ∀ t, n t = n' t ∧ c t = c' t ∧ a t = a' t) :
    FamilyCounts p l n' c' a' := fun t =>
  match counted t, same t with
  | ⟨length, ceased, came⟩, ⟨sameN, sameC, sameA⟩ =>
    ⟨sameN.symm.trans length, sameC ▸ ceased, sameA ▸ came⟩

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

/-- `n`, `c` and `a` count the census `alive`: how many are active at each step, how many of
them cease across it, and how many active after it came to be across it; counts as relations,
with no decision procedure. -/
abbrev CountsOf (w : World) (alive : Nat → List w.Relatum) (n c a : Nat → Nat) : Prop :=
  Becoming.FamilyCounts (fun x s => w.web.active s x) alive n c a

/-- `Q` holds of every census of the world and every counts of it. -/
def CountsHold (w : World) (Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop) : Prop :=
  ∀ alive n c a, w.web.Census alive → w.CountsOf alive n c a → Q n c a

/-- **The counts of a census are a tally**, with no decidedness. -/
theorem CountsOf.tally {alive : Nat → List w.Relatum} {n c a : Nat → Nat}
    (census : w.web.Census alive) (counted : w.CountsOf alive n c a) : Tally n c a :=
  Becoming.FamilyCounts.tally census counted

/-- **A ceasing count across a step exists exactly where activity after the step is decided at
each relatum active before it.** -/
theorem ceasings_exist_iff (alive : Nat → List w.Relatum) (t : Nat) :
    (∃ d, Counts (alive t) (fun x => CeasesToBe (fun s => w.web.active s x) t) d) ↔
      ∀ x, x ∈ alive t → Decided (CeasesToBe (fun s => w.web.active s x) t) :=
  counts_iff_decided

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
  (ceasings_exist_iff alive t).trans
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

/-- Where a procedure decides activity, its marks count every census. -/
theorem countsOf_decided [∀ t x, Decidable (w.web.active t x)] (alive : Nat → List w.Relatum) :
    w.CountsOf alive (fun t => (alive t).length)
      (fun t => ceasings (alive t) (fun x s => w.web.active s x) t)
      (fun t => comings (alive (t + 1)) (fun x s => w.web.active s x) t) :=
  familyCounts_decided alive

/-- What holds of every counted census holds of the census counts a procedure gives. -/
theorem CountsHold.obey [∀ t x, Decidable (w.web.active t x)]
    {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} (holds : w.CountsHold Q) :
    w.CountsObey Q :=
  fun alive census => holds alive _ _ _ census (countsOf_decided alive)

/-- For a pointwise property, what holds of the census counts a procedure gives holds of every
counted census. -/
theorem countsHold_of_obey [∀ t x, Decidable (w.web.active t x)]
    {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} (pointwise : Pointwise Q)
    (obeys : w.CountsObey Q) : w.CountsHold Q :=
  fun alive _ _ _ census counted => pointwise (fun t =>
    match counted t, countsOf_decided (w := w) alive t with
    | ⟨length, ceased, came⟩, ⟨_, ceased', came'⟩ =>
      ⟨length.symm, ceased'.unique ceased, came'.unique came⟩) (obeys alive census)

/-! ## Counting under the premises, where the counts exist -/

/-- Where the flow balances, only active relata give and whatever arises is embodied, under a
census something coming to be across a step needs something active at it. -/
theorem active_of_coming_jointly (balanced : w.Balanced) (acting : w.Acting)
    (embodied : w.ArisingEmbodied) {alive : Nat → List w.Relatum} (census : w.web.Census alive)
    {t : Nat} {x : w.Relatum} (comes : ComesToBe (fun s => w.web.active s x) t) :
    0 < (alive t).length :=
  match Web.Embodied.arises_given balanced acting (embodied t x comes) comes with
  | ⟨f, active, _⟩ => Nat.lt_of_lt_of_le (total_pos_of_mem (((census t).2 f).mp active)
      Nat.zero_lt_one) (Nat.le_of_eq (total_ones (alive t)))

/-- Where the flow balances, only active relata take and only from what they draw on, the flow
dissipates and every relatum is embodied, under a census something coming to be across a step
needs something active at it, whoever gives. -/
theorem active_of_coming_taking (balanced : w.Balanced) (taking : w.Taking)
    (dissipative : w.Dissipative) (embodied : w.Embodied) {alive : Nat → List w.Relatum}
    (census : w.web.Census alive) {t : Nat} {x : w.Relatum} (listed : x ∈ alive (t + 1))
    (comes : ComesToBe (fun s => w.web.active s x) t) : 0 < (alive t).length :=
  match Nat.eq_zero_or_pos (alive t).length with
  | .inr pos => pos
  | .inl empty =>
    have idle : ∀ f, ¬ w.web.active t f := fun f active =>
      Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le (Nat.lt_of_lt_of_le
        (total_pos_of_mem (((census t).2 f).mp active) Nat.zero_lt_one)
        (Nat.le_of_eq (total_ones (alive t)))) (Nat.le_of_eq empty))
    have untaken : ∀ f c, f ∈ w.flow.present t → w.flow.take t f c = 0 :=
      fun f c present => eq_zero_of_not_pos fun takes => idle f (taking t f c present takes).1
    have flows : ∀ c, w.web.level (t + 1) c = w.flow.given t c := fun c =>
      (congrArg (w.web.level (t + 1) c + ·)
          ((total_congr_on (g := fun _ => 0) fun f present => untaken f c present).trans
            (total_zero _)).symm).trans
        ((balanced t c).trans ((congrArg (· + w.flow.given t c)
          (eq_zero_of_not_pos fun stands => idle c ((embodied c t).mpr stands))).trans
          (Nat.zero_add _)))
    have closed : w.flow.ClosedAt (alive (t + 1)) t := fun f present c outside =>
      ⟨untaken f c present, eq_zero_of_not_pos fun gives => outside
        (((census (t + 1)).2 c).mp ((embodied c (t + 1)).mpr (Nat.lt_of_lt_of_le
          (Nat.lt_of_lt_of_le gives (le_total_of_mem (q := fun g => w.flow.give t g c)
            present)) (Nat.le_of_eq (flows c).symm))))⟩
    False.elim ((dissipative _ t (census (t + 1)).1 closed).still_untaken (balanced.on _ t)
      (fun c _ => (total_congr_on (g := fun _ => 0) fun f present =>
        untaken f c present).trans (total_zero _))
      ⟨x, listed, Nat.lt_of_le_of_lt (Nat.le_of_eq (eq_zero_of_not_pos fun stands =>
        idle x ((embodied x t).mpr stands))) ((embodied x (t + 1)).mp comes.2)⟩)

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
  ⟨fun law w alive n c a census counted =>
      counted_laws.mpr law w.Relatum _ alive n c a census counted,
   fun law n c a tally => law (queue n c) _ n c a Queue.listed (queue_countsOf tally)⟩

/-- **The laws of counting under each selection of the premises, where the counts exist.** A
property of the counts holds of every counted census of every world meeting the selection
exactly when it holds of every tally, and, where the selection binds counting, of every tally in
which nothing arises across a step at which nothing is active. For every property, with no
decidedness. -/
theorem counting_under_counted (S : Premise → Bool)
    {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} :
    (∀ n c a, Tally n c a → (BindsCounting S → ∀ t, 0 < a t → 0 < n t) → Q n c a) ↔
      ∀ w : World, w.Meets S → w.CountsHold Q :=
  ⟨fun law _ meets _ n c a census counted => law n c a (counted.tally census)
    fun ⟨balanced, embodied, giving⟩ t arising => match counted t with
    | ⟨length, _, came⟩ => match came.exists_of_pos arising with
      | ⟨_, listed, comes⟩ => Nat.lt_of_lt_of_le (match giving with
        | .inl acting => active_of_coming_jointly (meets _ balanced) (meets _ acting)
            (Embodied.arising (meets _ embodied)) census comes
        | .inr ⟨taking, dissipative⟩ => active_of_coming_taking (meets _ balanced)
            (meets _ taking) (meets _ dissipative) (meets _ embodied) census listed comes)
        (Nat.le_of_eq length.symm),
   fun law n c a tally quiet =>
    match hb : S .balanced, he : S .embodied with
    | false, _ => law (embodiedQueue n c) (embodiedQueue_meets n c hb) _ n c a Queue.listed
        (embodiedQueue_countsOf tally)
    | true, false => law (queue n c) (queue_meets n c he) _ n c a Queue.listed
        (queue_countsOf tally)
    | true, true => match ha : S .acting, ht : S .taking, hd : S .dissipative with
      | true, _, _ => law (openQueue n c)
          ((openQueue_premised tally (quiet ⟨hb, he, .inl ha⟩)).meets S) _ n c a
          (openQueue_census n c) (openQueue_countsOf tally)
      | false, true, true => law (openQueue n c)
          ((openQueue_premised tally (quiet ⟨hb, he, .inr ⟨ht, hd⟩⟩)).meets S) _ n c a
          (openQueue_census n c) (openQueue_countsOf tally)
      | false, false, _ => law (drivenQueue n c) (drivenQueue_meets n c ha ht) _ n c a
          (openQueue_census n c) (drivenQueue_countsOf tally)
      | false, true, false => law (openQueue n c) (openQueue_meets n c ha hd) _ n c a
          (openQueue_census n c) (openQueue_countsOf tally)⟩

/-- **Under all eight premises, where the counts exist**, the laws of counting are the tally and
that nothing arises across a step at which nothing is active: for every property, with no
decidedness. -/
theorem premised_counting_counted {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} :
    (∀ n c a, Tally n c a → (∀ t, 0 < a t → 0 < n t) → Q n c a) ↔
      ∀ w : World, w.Premised → w.CountsHold Q :=
  ⟨fun law _ premised _ n c a census counted => law n c a (counted.tally census)
    fun t arising => match counted t with
    | ⟨length, _, came⟩ => match came.exists_of_pos arising with
      | ⟨_, _, comes⟩ => Nat.lt_of_lt_of_le (active_of_coming_jointly
          (premised _ (.tail _ (.head _))) (premised _ (.tail _ (.tail _ (.head _))))
          (Embodied.arising (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _
            (.head _))))))))
          census comes) (Nat.le_of_eq length.symm),
   fun law n c a tally company => law (openQueue n c) (openQueue_premised tally company) _ n c a
      (openQueue_census n c) (openQueue_countsOf tally)⟩

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

/-! ## Enclosure bounds change, where the counts exist -/

/-- **Enclosure bounds change for every counted census.** In a world whose relata are embodied,
with a balanced, dissipative flow and every step from `T` on enclosed, the total standing at `T`
bounds the change of every counted census from `T`. No decidedness. -/
theorem enclosure_bounds_change_counted {alive : Nat → List w.Relatum}
    (census : w.web.Census alive) {n c a : Nat → Nat} (counted : w.CountsOf alive n c a)
    (embodied : w.Embodied) (balanced : w.Balanced) (dissipative : w.Dissipative) {T : Nat}
    (enclosed : ∀ t, T ≤ t → w.flow.Enclosed t) :
    ChangeBound T (w.web.stock (alive T) T) n c a :=
  have standing := standingCensus census embodied
  Flow.runsDown_change_bound standing
    (fun t later down => (enclosed t later).aroundStanding_not_not alive fun around =>
      down (around.runsDownClosed balanced dissipative standing).runsDown)
    (fun t _ => Nat.le_trans (Nat.le_of_eq (counted t).1) (length_le_stock census embodied t))
    fun t _ changes => match counted t with
    | ⟨_, ceased, came⟩ => match Nat.eq_zero_or_pos (c t) with
      | .inr ceasing => match ceased.exists_of_pos ceasing with
        | ⟨x, _, ceases⟩ => ⟨x, .inr (falls_of_ceases embodied ceases)⟩
      | .inl still => match came.exists_of_pos (Nat.lt_of_lt_of_le changes (Nat.le_of_eq
          ((congrArg (· + a t) still).trans (Nat.zero_add _)))) with
        | ⟨x, _, comes⟩ => ⟨x, .inl (rises_of_arises embodied comes)⟩

/-- At an enclosed step, where the flow balances and dissipates and every relatum is embodied,
under a census something coming to be across the step needs something active at it, whoever
gives and whoever takes. -/
theorem active_of_coming_enclosed (balanced : w.Balanced) (dissipative : w.Dissipative)
    (embodied : w.Embodied) {alive : Nat → List w.Relatum} (census : w.web.Census alive)
    {t : Nat} (enclosed : w.flow.Enclosed t) {x : w.Relatum}
    (comes : ComesToBe (fun s => w.web.active s x) t) : 0 < (alive t).length :=
  match Nat.eq_zero_or_pos (alive t).length, enclosed with
  | .inr pos, _ => pos
  | .inl empty, ⟨cs, distinct, closed⟩ =>
    have idle : ∀ f, ¬ w.web.active t f := fun f active =>
      Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le (Nat.lt_of_lt_of_le
        (total_pos_of_mem (((census t).2 f).mp active) Nat.zero_lt_one)
        (Nat.le_of_eq (total_ones (alive t)))) (Nat.le_of_eq empty))
    have nothing : w.web.stock cs t = 0 :=
      total_eq_zero fun c _ => eq_zero_of_not_pos fun stands => idle c ((embodied c t).mpr stands)
    have stands : w.web.ComesToStand t x :=
      ⟨fun standing => idle x ((embodied x t).mpr standing), (embodied x (t + 1)).mp comes.2⟩
    match total_pos _ (Flow.Balances.rise_given balanced stands.rises) with
    | ⟨f, present, gives⟩ =>
      absurd (fun mem => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le
          ((balanced.on cs t).comes_from_standing (dissipative cs t distinct closed) mem stands)
          (Nat.le_of_eq nothing)))
        fun out => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le gives
          (Nat.le_of_eq (closed f present x out).2))

/-- Something coming to be across a step needs something active at it, given a ground. -/
theorem company_of {alive : Nat → List w.Relatum} {n c a : Nat → Nat}
    (counted : w.CountsOf alive n c a) {t : Nat}
    (ground : ∀ x, x ∈ alive (t + 1) → ComesToBe (fun s => w.web.active s x) t →
      0 < (alive t).length) : 0 < a t → 0 < n t := fun arising =>
  match counted t with
  | ⟨length, _, came⟩ => match came.exists_of_pos arising with
    | ⟨x, listed, comes⟩ => Nat.lt_of_lt_of_le (ground x listed comes) (Nat.le_of_eq length.symm)

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
  ⟨fun law _ premised ⟨_, enclosed⟩ _ n c a census counted =>
    law n c a (counted.tally census)
      (fun _ => company_of counted fun _ _ comes => active_of_coming_jointly
        (premised _ (.tail _ (.head _))) (premised _ (.tail _ (.tail _ (.head _))))
        (Embodied.arising (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _
          (.head _))))))))
        census comes)
      ⟨_, (enclosure_bounds_change_counted census counted
        (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _)))))))
        (premised _ (.tail _ (.head _)))
        (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _)))))) enclosed).from_zero⟩,
   fun law n c a tally company ⟨_, bound⟩ =>
    law (enclosedQueue _ _ _ _) (enclosedQueue_premised tally company bound)
      ⟨0, fun t _ => enclosedQueue_enclosed tally t⟩ _ n c a (enclosedQueue_census _ _ _ _)
      (enclosedQueue_countsOf _ tally)⟩

/-- **Under all eight premises, in finite worlds, where the counts exist**: the same laws. -/
theorem finite_counting_counted {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} :
    (∀ n c a, Tally n c a → (∀ t, 0 < a t → 0 < n t) → (∃ B, ChangeBound 0 B n c a) →
      Q n c a) ↔ ∀ w : World, w.Premised → w.Finite → w.CountsHold Q :=
  ⟨fun law w premised finite => enclosed_counting_counted.mp law w premised
      ⟨0, fun t _ => finite.enclosed t⟩,
   fun law n c a tally company ⟨_, bound⟩ =>
    law (finiteQueue _ _ _ _) (finiteQueue_premised tally company bound)
      (finiteQueue_finite _ _ _ _) _ n c a (finiteQueue_census _ _ _ _)
      (finiteQueue_countsOf tally bound)⟩

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
  ⟨fun law _ meets ⟨T, enclosed⟩ _ n c a census counted => law n c a (counted.tally census)
    (fun ⟨balanced, embodied, giving⟩ _ => company_of counted fun _ listed comes =>
      match giving with
      | .inl acting => active_of_coming_jointly (meets _ balanced) (meets _ acting)
          (Embodied.arising (meets _ embodied)) census comes
      | .inr ⟨taking, dissipative⟩ => active_of_coming_taking (meets _ balanced)
          (meets _ taking) (meets _ dissipative) (meets _ embodied) census listed comes)
    (fun ⟨balanced, embodied, dissipative⟩ => ⟨T, _, enclosure_bounds_change_counted census
      counted (meets _ embodied) (meets _ balanced) (meets _ dissipative) enclosed,
      fun t later => company_of counted fun _ _ comes => active_of_coming_enclosed
        (meets _ balanced) (meets _ dissipative) (meets _ embodied) census (enclosed t later)
        comes⟩),
   fun law n c a tally quiet bounded =>
    match hb : S .balanced, he : S .embodied with
    | false, _ => law (embodiedQueue n c) (embodiedQueue_meets n c hb)
        ⟨0, fun t _ => still_enclosed _ (fun _ => rfl) t⟩ _ n c a Queue.listed
        (embodiedQueue_countsOf tally)
    | true, false => law (queue n c) (queue_meets n c he)
        ⟨0, fun t _ => still_enclosed _ (fun _ => rfl) t⟩ _ n c a Queue.listed
        (queue_countsOf tally)
    | true, true => match hd : S .dissipative, ha : S .acting, ht : S .taking with
      | false, _, _ => law (enclosedQueue n c a 0)
          (fun
            | .dependent, _ => fun _ _ _ _ no => (nomatch no)
            | .balanced, _ => enclosedQueue_balanced n c a 0
            | .acting, selected => enclosedQueue_acting tally (quiet ⟨hb, he, .inl selected⟩)
            | .taking, _ => enclosedQueue_taking n c a 0
            | .dissipative, selected => nomatch hd.symm.trans selected
            | .embodied, _ => enclosedQueue_embodied n c a 0
            | .counted, _ => ⟨_, enclosedQueue_census n c a 0⟩
            | .transmitting, _ => ⟨0, fun _ _ _ _ _ no => (nomatch no)⟩)
          ⟨0, fun t _ => enclosedQueue_enclosed tally t⟩ _ n c a (enclosedQueue_census n c a 0)
          (enclosedQueue_countsOf 0 tally)
      | true, true, _ => match bounded ⟨hb, he, hd⟩ with
        | ⟨_, _, bound, _⟩ => law (enclosedQueue n c a _)
            ((enclosedQueue_premised tally (quiet ⟨hb, he, .inl ha⟩) bound.from_zero).meets S)
            ⟨0, fun t _ => enclosedQueue_enclosed tally t⟩ _ n c a (enclosedQueue_census n c a _)
            (enclosedQueue_countsOf _ tally)
      | true, false, true => match bounded ⟨hb, he, hd⟩ with
        | ⟨_, _, bound, _⟩ => law (enclosedQueue n c a _)
            ((enclosedQueue_premised tally (quiet ⟨hb, he, .inr ⟨ht, hd⟩⟩)
              bound.from_zero).meets S)
            ⟨0, fun t _ => enclosedQueue_enclosed tally t⟩ _ n c a (enclosedQueue_census n c a _)
            (enclosedQueue_countsOf _ tally)
      | true, false, false => match bounded ⟨hb, he, hd⟩ with
        | ⟨T, K, bound, company⟩ =>
            law (closingQueue n c a (K + T) T)
              (fun
                | .dependent, _ => fun _ _ _ _ no => (nomatch no)
                | .balanced, _ => closingQueue_balanced n c a (K + T) T
                | .acting, selected => nomatch ha.symm.trans selected
                | .taking, selected => nomatch ht.symm.trans selected
                | .dissipative, _ => closingQueue_dissipative tally bound company
                | .embodied, _ => enclosedQueue_embodied n c a (K + T)
                | .counted, _ => ⟨_, enclosedQueue_census n c a (K + T)⟩
                | .transmitting, _ => ⟨0, fun _ _ _ _ _ no => (nomatch no)⟩)
              ⟨T, fun _ later => closingQueue_enclosed tally later⟩ _ n c a
              (enclosedQueue_census n c a (K + T)) (closingQueue_countsOf (K + T) T tally)⟩

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
  ⟨fun law _ meets finite alive n c a census counted => law n c a (counted.tally census)
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
      (meets _ embodied) (meets _ balanced) (meets _ dissipative) fun t _ => finite.enclosed t⟩),
   fun law n c a tally ⟨M, bounded⟩ quiet bounds =>
    match hb : S .balanced, he : S .embodied with
    | false, _ => law (embodiedRing n c M) (embodiedRing_meets bounded hb) (places_listed _) _
        n c a (Ring.census bounded _) (embodiedRing_countsOf tally bounded)
    | true, false => law (ring n c M) (ring_meets bounded he) (places_listed _) _ n c a
        (Ring.census bounded _) (ring_countsOf tally bounded)
    | true, true => match hd : S .dissipative with
      | false => law (balancedRing n c M)
          (balancedRing_meets tally bounded (fun ha => quiet (.inl ⟨hb, he, .inl ha⟩)) hd)
          (places_listed _) _ n c a (Ring.census bounded _) (balancedRing_countsOf tally bounded)
      | true => match bounds ⟨hb, he, hd⟩ with
        | ⟨_, bound⟩ => law (finiteQueue _ _ _ _)
            ((finiteQueue_premised tally (quiet (.inr ⟨hb, he, hd⟩)) bound).meets S)
            (finiteQueue_finite _ _ _ _) _ n c a (finiteQueue_census _ _ _ _)
            (finiteQueue_countsOf tally bound)⟩

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
