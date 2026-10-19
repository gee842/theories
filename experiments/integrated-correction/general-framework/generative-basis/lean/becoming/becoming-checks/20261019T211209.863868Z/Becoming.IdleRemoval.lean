import Becoming.Reordering

/-!
# Idle removal: a world with its idle steps removed

The converse of `Becoming.Stuttering`: where a world is idle at the idle steps of a stuttering,
the idle steps are removed, each step of the world being shown as `Web.SameAt` (of
`Becoming.Reordering`) shows it.

* **Removing idle steps.** Given a stuttering `ρ` and its moving steps `σ` (`Stutter.Moves`; each
  exists by `Stutter.crosses` and is the only one, `Stutter.moving_unique`), a world idle at the
  idle steps of `ρ` (`World.IdleAt`) has them removed by keeping the exchanges of the moving steps
  and reading the web there (`World.withoutIdle`, `Flow.readAt`). Each step of the world shows
  every relatum as the step of the world without idle steps it is read at
  (`World.withoutIdle_sameAt`); the two meet balance, dissipation, only active relata giving and
  taking, activity needing support, embodiment and bounded transmission alike, with no condition
  on listing (`World.withoutIdle_premises`, `World.withoutIdle_transmits`), and either has a
  census exactly where the other does (`World.withoutIdle_counted`); and over any stretch
  what is taken and given, the rises and falls of a family's total standing with the steps at
  which it rises and falls, and the relata arising and ceasing, are those of the stretch of the
  world without idle steps it reads (`World.withoutIdle_totals`, `World.withoutIdle_counts`).


Reading (the AI's, adopted on Ren's delegation of 15 October 2026, DELEGATED-CHOICES D30): an
idle step makes no difference, and removing it changes nothing the laws state.

Not shown: the moving steps of a stuttering are given as a function: each exists and is unique,
but choosing all of them at once is an unbounded search, not done. No ethical predicate, ranking
or axiom occurs.
-/

namespace Becoming

/-! ## Removing idle steps -/

namespace Stutter

variable {ρ : Nat → Nat}

/-- The moving step reading a step is one: two steps at which a stuttering moves from `s` to
`s + 1` are the same step. -/
theorem moving_unique (stutter : Stutter ρ) {n n' s : Nat} (here : ρ n = s)
    (next : ρ (n + 1) = s + 1) (here' : ρ n' = s) (next' : ρ (n' + 1) = s + 1) : n = n' :=
  match Nat.lt_or_ge n n' with
  | .inl lt => absurd (Nat.le_trans (Nat.le_of_eq next.symm)
      (Nat.le_trans (mono stutter.2.1 lt) (Nat.le_of_eq here'))) (Nat.not_succ_le_self s)
  | .inr ge => match Nat.lt_or_ge n' n with
    | .inl lt => absurd (Nat.le_trans (Nat.le_of_eq next'.symm)
        (Nat.le_trans (mono stutter.2.1 lt) (Nat.le_of_eq here))) (Nat.not_succ_le_self s)
    | .inr ge' => Nat.le_antisymm ge' ge

/-- `σ` gives, for each step read, the moving step reading it. -/
def Moves (ρ σ : Nat → Nat) : Prop :=
  ∀ s, ρ (σ s) = s ∧ ρ (σ s + 1) = s + 1

variable {σ : Nat → Nat}

/-- A step comes no later than the moving step reading what it reads. -/
theorem le_moving (stutter : Stutter ρ) (moves : Moves ρ σ) (n : Nat) : n ≤ σ (ρ n) :=
  match Nat.lt_or_ge (σ (ρ n)) n with
  | .inl lt => absurd (Nat.le_trans (Nat.le_of_eq (moves (ρ n)).2.symm) (mono stutter.2.1 lt))
      (Nat.not_succ_le_self (ρ n))
  | .inr ge => ge

/-- And every step from it to that moving step is idle. -/
theorem idle_before_moving (stutter : Stutter ρ) (moves : Moves ρ σ) {n k : Nat} (from_ : n ≤ k)
    (below : k < σ (ρ n)) : ρ (k + 1) = ρ k :=
  have top : ρ (k + 1) ≤ ρ n := Nat.le_trans (mono stutter.2.1 below)
    (Nat.le_of_eq (moves (ρ n)).1)
  Nat.le_antisymm (Nat.le_trans top (mono stutter.2.1 from_))
    (le_succ stutter.2.1 k)

/-- Where a stuttering moves, its step is the moving step reading what it reads. -/
theorem moving_eq (stutter : Stutter ρ) (moves : Moves ρ σ) {n : Nat}
    (moved : ρ (n + 1) = ρ n + 1) : σ (ρ n) = n :=
  moving_unique stutter (moves (ρ n)).1 (moves (ρ n)).2 rfl moved

/-- What holds at every idle step and at each moving step holds at every step. -/
theorem every_step (stutter : Stutter ρ) (moves : Moves ρ σ) {P : Nat → Prop}
    (at_idle : ∀ n, ρ (n + 1) = ρ n → P n) (at_moving : ∀ s, P (σ s)) (n : Nat) : P n :=
  match stutter.2.1 n with
  | .inl still => at_idle n still
  | .inr moved => Eq.subst (motive := P) (moving_eq stutter moves moved) (at_moving (ρ n))

end Stutter

/-- A web unmoved at every step of a stretch shows every relatum at its end as at its start. -/
theorem Web.sameAt_of_unmoved {X : Type} {W : Web X X} :
    ∀ (d n : Nat), (∀ k, n ≤ k → k < n + d → ∀ x, W.Unmoved k x) → ∀ x, W.SameAt n W (n + d) x
  | 0, _, _, x => Web.SameAt.refl W _ x
  | d + 1, n, still, x =>
    (Web.sameAt_of_unmoved d n (fun k from_ below => still k from_ (Nat.lt_succ_of_lt below)) x).trans
      (still (n + d) (Nat.le_add_right n d) (Nat.lt_succ_self _) x)

/-- A flow read at the steps `σ`: across step `s` the exchange across step `σ s`. -/
def Flow.readAt {F C : Type} (L : Flow F C) (σ : Nat → Nat) : Flow F C :=
  ⟨fun s => L.present (σ s), fun s => L.take (σ s), fun s => L.give (σ s)⟩

namespace World

/-- The world is idle at the idle steps of a reading: nothing takes part and every relatum is
unmoved. -/
def IdleAt (v : World) (ρ : Nat → Nat) : Prop :=
  ∀ n, ρ (n + 1) = ρ n → v.flow.present n = [] ∧ ∀ x, v.web.Unmoved n x

/-- **The world with its idle steps removed.** Across step `s` the exchange across step `σ s`,
the web read at the times `σ`. Where `σ` gives the moving steps of a stuttering at whose idle
steps the world is idle, this removes them. -/
def withoutIdle (v : World) (σ : Nat → Nat) : World :=
  World.of v.Relatum (v.flow.readAt σ) (v.web.sample σ)

section Removal

variable {v : World} {ρ σ : Nat → Nat} (stutter : Stutter ρ) (moves : Stutter.Moves ρ σ)
  (idle : v.IdleAt ρ)
include stutter moves idle

/-- Each step of the world shows every relatum as the step of the world without idle steps it
is read at. -/
theorem withoutIdle_sameAt (n : Nat) (x : v.Relatum) :
    v.web.SameAt n v.web (σ (ρ n)) x :=
  match le_dest (Stutter.le_moving stutter moves n) with
  | ⟨d, same⟩ => Eq.subst (motive := fun k => v.web.SameAt n v.web k x) same.symm
      (Web.sameAt_of_unmoved d n (fun k from_ below => (idle k (Stutter.idle_before_moving
        stutter moves from_ (Nat.lt_of_lt_of_le below (Nat.le_of_eq same.symm)))).2) x)

/-- After a moving step the world shows every relatum as at the next moving step. -/
theorem withoutIdle_after (s : Nat) (x : v.Relatum) : v.web.SameAt (σ s + 1) v.web (σ (s + 1)) x :=
  Eq.subst (motive := fun k => v.web.SameAt (σ s + 1) v.web (σ k) x) (moves s).2
    (withoutIdle_sameAt stutter moves idle (σ s + 1) x)

/-- **Removing idle steps keeps every premise.** The world and the world with its idle steps
removed meet balance, dissipation, only active relata giving, only active relata taking,
activity needing support and embodiment exactly alike. Unlike a reading through a stuttering, no
condition on listing is needed: each step keeps its own exchange. -/
theorem withoutIdle_premises :
    ((v.withoutIdle σ).Balanced ↔ v.Balanced) ∧ ((v.withoutIdle σ).Dissipative ↔ v.Dissipative) ∧
    ((v.withoutIdle σ).Acting ↔ v.Acting) ∧ ((v.withoutIdle σ).Taking ↔ v.Taking) ∧
    ((v.withoutIdle σ).Dependent ↔ v.Dependent) ∧ ((v.withoutIdle σ).Embodied ↔ v.Embodied) :=
  have same := withoutIdle_sameAt stutter moves idle
  have after := withoutIdle_after stutter moves idle
  ⟨⟨fun balanced n c => Stutter.every_step stutter moves
      (P := fun n => ∀ c, v.web.level (n + 1) c + v.flow.taken n c = v.web.level n c + v.flow.given n c)
      (fun n still c => (congrArg (· + v.flow.taken n c) ((idle n still).2 c).1).trans
        (congrArg (v.web.level n c + ·) ((Flow.taken_nil (idle n still).1 c).trans
          (Flow.given_nil (idle n still).1 c).symm)))
      (fun s c => (congrArg (· + v.flow.taken (σ s) c) (after s c).1.symm).trans (balanced s c))
      n c,
    fun balanced s c => (congrArg (· + v.flow.taken (σ s) c) (after s c).1).trans (balanced (σ s) c)⟩,
   ⟨fun dissipative cs => Stutter.every_step stutter moves
      (P := fun n => Distinct cs → v.flow.ClosedAt cs n → v.flow.DissipatesOn cs n)
      (fun n still _ _ f mem => absurd (Eq.subst (motive := fun l => f ∈ l) (idle n still).1 mem)
        fun no => nomatch no)
      (fun s => dissipative cs s),
    fun dissipative cs s => dissipative cs (σ s)⟩,
   ⟨fun acting => Stutter.every_step stutter moves
      (P := fun n => ∀ f c, f ∈ v.flow.present n → 0 < v.flow.give n f c → v.web.active n f)
      (fun n still f _ mem _ => absurd (Eq.subst (motive := fun l => f ∈ l) (idle n still).1 mem)
        fun no => nomatch no)
      (fun s => acting s),
    fun acting s => acting (σ s)⟩,
   ⟨fun taking => Stutter.every_step stutter moves
      (P := fun n => ∀ f c, f ∈ v.flow.present n → 0 < v.flow.take n f c →
        v.web.active n f ∧ v.web.draws n f c)
      (fun n still f _ mem _ => absurd (Eq.subst (motive := fun l => f ∈ l) (idle n still).1 mem)
        fun no => nomatch no)
      (fun s => taking s),
    fun taking s => taking (σ s)⟩,
   ⟨fun dependent n f active c requires =>
      have sf := same n f
      Nat.le_trans (Nat.le_of_eq (sf.2.2 c).2.1.symm)
        (Nat.le_trans (dependent (ρ n) f (cast sf.2.1.symm active) c
            (cast (sf.2.2 c).1.symm requires))
          (Nat.le_of_eq (same n c).1)),
    Web.sample_dependent σ⟩,
   ⟨fun embodied x n => (Iff.of_eq (same n x).2.1).symm.trans ((embodied x (ρ n)).trans
      (Iff.of_eq (congrArg (0 < ·) (same n x).1))),
    fun embodied x => Web.sample_embodied σ (embodied x)⟩⟩

/-- And bounded transmission, with the same bound. -/
theorem withoutIdle_transmits {c : v.Relatum} {δ : Nat} :
    (v.withoutIdle σ).flow.TransmitsWithin (v.withoutIdle σ).web c δ ↔
      v.flow.TransmitsWithin v.web c δ :=
  have after := withoutIdle_after stutter moves idle
  ⟨fun transmits => Stutter.every_step stutter moves
      (P := fun n => ∀ x g, v.flow.DescendsAt v.web n x g → v.web.requires (n + 1) x c →
        v.web.requires n g c ∧ v.web.need (n + 1) x c ≤ v.web.need n g c + δ)
      (fun n still _ g ⟨mem, _, _⟩ => absurd (Eq.subst (motive := fun l => g ∈ l) (idle n still).1 mem)
        fun no => nomatch no)
      (fun s x g ⟨mem, gives, absent, stands⟩ requires =>
        have inherited := transmits s x g
          ⟨mem, gives, absent, Eq.subst (motive := (0 < ·)) (after s x).1.symm stands⟩
          (cast ((after s x).2.2 c).1.symm requires)
        ⟨inherited.1, Nat.le_trans (Nat.le_of_eq ((after s x).2.2 c).2.1.symm) inherited.2⟩),
   fun transmits s x g ⟨mem, gives, absent, stands⟩ requires =>
     have inherited := transmits (σ s) x g
       ⟨mem, gives, absent, Eq.subst (motive := (0 < ·)) (after s x).1 stands⟩
       (cast ((after s x).2.2 c).1 requires)
     ⟨inherited.1, Nat.le_trans (Nat.le_of_eq ((after s x).2.2 c).2.1) inherited.2⟩⟩

/-- And a census: the relata active at each step of the world are those active at the step it is
read at. -/
theorem withoutIdle_counted : (v.withoutIdle σ).Counted ↔ v.Counted :=
  ⟨fun ⟨alive, census⟩ => ⟨fun n => alive (ρ n), fun n => ⟨(census (ρ n)).1, fun x =>
      (Iff.of_eq (withoutIdle_sameAt stutter moves idle n x).2.1).symm.trans ((census (ρ n)).2 x)⟩⟩,
   fun ⟨alive, census⟩ => ⟨fun s => alive (σ s), fun s => census (σ s)⟩⟩

/-- **And the totals.** Over any stretch, what is taken from and given to a condition, the rises
and falls of a family's total standing and the steps at which it rises and falls are those of the
stretch of the world without idle steps it reads. -/
theorem withoutIdle_totals (cs : List v.Relatum) (c : v.Relatum) (N m d : Nat)
    (reads : ρ N + d = ρ (N + m)) :
    total (steps N m) (fun n => v.flow.taken n c) =
      total (steps (ρ N) d) (fun s => (v.withoutIdle σ).flow.taken s c) ∧
    total (steps N m) (fun n => v.flow.given n c) =
      total (steps (ρ N) d) (fun s => (v.withoutIdle σ).flow.given s c) ∧
    total (steps N m) (rise (v.web.stock cs)) =
      total (steps (ρ N) d) (rise ((v.withoutIdle σ).web.stock cs)) ∧
    total (steps N m) (fall (v.web.stock cs)) =
      total (steps (ρ N) d) (fall ((v.withoutIdle σ).web.stock cs)) ∧
    count (steps N m) (rise (v.web.stock cs)) =
      count (steps (ρ N) d) (rise ((v.withoutIdle σ).web.stock cs)) ∧
    count (steps N m) (fall (v.web.stock cs)) =
      count (steps (ρ N) d) (fall ((v.withoutIdle σ).web.stock cs)) :=
  have here : ∀ n, ρ (n + 1) = ρ n + 1 → σ (ρ n) = n := fun _ moved =>
    Stutter.moving_eq stutter moves moved
  have stock : ∀ n, v.web.stock cs n = (v.withoutIdle σ).web.stock cs (ρ n) := fun n =>
    total_congr_on fun c _ => (withoutIdle_sameAt stutter moves idle n c).1.symm
  have rises : ∀ n, rise (v.web.stock cs) n =
      rise (fun k => (v.withoutIdle σ).web.stock cs (ρ k)) n := fun n =>
    (congr (congrArg excess (stock (n + 1))) (stock n) :)
  have falls : ∀ n, fall (v.web.stock cs) n =
      fall (fun k => (v.withoutIdle σ).web.stock cs (ρ k)) n := fun n =>
    (congr (congrArg excess (stock n)) (stock (n + 1)) :)
  ⟨stutter_total stutter.2.1 (fun n still => Flow.taken_nil (idle n still).1 c)
     (fun n moved => congrArg (fun k => v.flow.taken k c) (here n moved).symm) N m d reads,
   stutter_total stutter.2.1 (fun n still => Flow.given_nil (idle n still).1 c)
     (fun n moved => congrArg (fun k => v.flow.given k c) (here n moved).symm) N m d reads,
   (total_congr rises (steps N m)).trans (stutter_risen stutter.2.1 _ N m d reads),
   (total_congr falls (steps N m)).trans (stutter_fallen stutter.2.1 _ N m d reads),
   (total_congr (fun n => congrArg sign (rises n)) (steps N m)).trans
     (stutter_rise_count stutter.2.1 _ N m d reads),
   (total_congr (fun n => congrArg sign (falls n)) (steps N m)).trans
     (stutter_fall_count stutter.2.1 _ N m d reads)⟩

/-- And the relata of a finite family arising and ceasing, with activity decided. -/
theorem withoutIdle_counts [decided : ∀ n x, Decidable (v.web.active n x)] (xs : List v.Relatum)
    (N m d : Nat) (reads : ρ N + d = ρ (N + m)) :
    haveI : ∀ s x, Decidable ((v.withoutIdle σ).web.active s x) := fun s x => decided (σ s) x
    total (steps N m) (comings xs fun x n => v.web.active n x) =
      total (steps (ρ N) d) (comings xs fun x s => (v.withoutIdle σ).web.active s x) ∧
    total (steps N m) (ceasings xs fun x n => v.web.active n x) =
      total (steps (ρ N) d) (ceasings xs fun x s => (v.withoutIdle σ).web.active s x) :=
  letI : ∀ s x, Decidable ((v.withoutIdle σ).web.active s x) := fun s x => decided (σ s) x
  have alike : ∀ x n, v.web.active n x ↔ (v.withoutIdle σ).web.active (ρ n) x := fun x n =>
    (Iff.of_eq (withoutIdle_sameAt stutter moves idle n x).2.1).symm
  ⟨(total_congr (fun n => comings_of_iff alike n) (steps N m)).trans
     (stutter_comings (as := xs) (p := fun x s => (v.withoutIdle σ).web.active s x) stutter.2.1
       N m d reads),
   (total_congr (fun n => ceasings_of_iff alike n) (steps N m)).trans
     (stutter_ceasings (as := xs) (p := fun x s => (v.withoutIdle σ).web.active s x) stutter.2.1
       N m d reads)⟩

end Removal

end World

