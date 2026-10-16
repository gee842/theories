import Becoming.Testing
import Becoming.Capture

/-!
# Selection: a selection through registration reaches exactly what registers

On 12 October 2026, after the AI compared the theory with a general cause–effect system
(`x_{t+1} = F(x_t, u_t, ε_t)`, with feedback, adaptive parameters and attractors), Ren gave the
go: "Great, let's finish all of them". This module states, with no premise beyond what each law
names, what a selection decided by a formation's registration can tell apart. A selection is any
claim about level histories, read as which histories are kept, rewarded or leave more
descendants. It is through a selector's registration up to a step when the histories the
selector registers alike up to that step are selected alike (`Web.SelectsThrough`); a score is
through it when they score alike (`Web.ScoresThrough`). That a selection is through
registration is supplied, never derived.

* **A selection reaches exactly what registers.** Two histories are selected alike by every
  selection through `f`'s registration up to `t` exactly when `f` registers them alike up to `t`
  (`Web.selects_alike_iff`). The belief of `Becoming.Testing` is such a selection
  (`Web.belief_selects`), so where `f` registers two histories apart, a selection through its
  registration holds at one and fails at the other (`Web.separates`); registering alike is an
  equivalence (`Web.RegistersAlikeUpTo.trans`). A selection through registration is a claim its
  selector tests completely, refuted exactly where it fails (`Web.SelectsThrough.refutes_iff`).
  Admission and the levels of observed conditions are selected and scored through registration
  (`Web.admits_through`, `Web.observed_scores`); a selection through registration stays so at
  later steps, under more observation, under negation and under conjunction
  (`Web.SelectsThrough.later`, `Web.SelectsThrough.widen`, `Web.SelectsThrough.not`,
  `Web.SelectsThrough.and`), and a score's thresholds are selections
  (`Web.ScoresThrough.atLeast`). For scores the same law holds where registering alike with the
  first history is decidable, a hypothesis named at that point (`Web.scores_alike_iff`).
* **Groups.** A selection through a group's pooled registration is one that selects alike the
  histories every member registers alike (`Web.SelectsThroughAll`); the same law holds of it
  (`Web.selects_alike_all_iff`, `Web.separates_all`). A member's selection is a group selection
  (`Web.SelectsThrough.all`), and group selections are closed under conjunction
  (`Web.SelectsThroughAll.and`).
* **Blind beyond the registration closure.** With the rest of the exchange fixed, every
  selection and every score through the registration of a formation within `f`'s registration
  closure selects the levels with and without a part beyond the closure alike
  (`Flow.unselected_beyond_registration`, `Flow.unscored_beyond_registration`); so does every
  selection through the pooled registration of a group within the closure
  (`Flow.unselected_beyond_registration_all`). Where the members respond, under the hypotheses of
  `Flow.alike_within_registration`, it selects the two flows alike
  (`Flow.unselected_beyond_registration_responsive`).
* **The gap.** In `Clearing` the dweller lies within the clearer's reach closure and beyond its
  registration closure, and the clearer does not register the habitat
  (`Clearing.dweller_within_reach`). Every selection through the clearer's registration selects
  the cleared and the spared world alike at every step, while the dweller ends in the one and
  not the other; that the dweller ends is selected through the clearer's registration at no step
  (`Clearing.unselected`). The dweller's admission at the third step is a selection through the
  dweller's registration and separates the two worlds (`Clearing.selected_by_dweller`); the
  admission of both at the third step is a selection through the pooled registration of the
  clearer and the dweller that separates them and is through neither alone
  (`Clearing.selected_pooled`).
* **Selection favours reaching beyond.** In `Diversion` a taker gauges a store. In the diverting
  flow it takes one unit from a source a dweller depends on and gives it to the store; in the
  undiverted flow nothing is exchanged. The selection that the store stands at least one at the
  second step is through the taker's registration, holds in the diverting flow and fails in the
  undiverted one, while the diverting flow reaches the dweller, beyond the taker's registration
  closure, and ends it (`Diversion.favours`). Every selection through the taker's registration
  selects the diverting flow alike with a supplying flow, which raises the store without drawing
  on the source and reaches nothing beyond the taker (`Diversion.blind_to_source`).
* **Share among descendants.** Where a selection gives each parent whose history it holds for at
  least `a` offspring and each other parent at most `b < a`, the share of the parents it holds for
  rises among the offspring (`share_rises_through`): `share_rises` of `Becoming.Capture`, the
  selection supplying which parents are carriers.
* **By the record alone.** Options are told apart only by what a record holds of each. A
  selection reads the record alone when exchanging two options' entries exchanges what it
  selects (`Relabel.Equivariant`). Two options are selected alike by every such selection exactly
  when the record ties them (`Relabel.selected_alike_iff`), as a selection through registration
  reaches exactly what registers. One selecting at most one option singles out exactly the
  options whose entry no other option shares (`Relabel.singled_iff_untied`, the selection
  `Relabel.Alone`), and at a full tie of two or more options it selects none
  (`Relabel.Equivariant.none_of_full_tie`). A valuation reading the record alone, such as a
  weight on each option, gives tied options equal values (`Relabel.EquivariantValue.tied`,
  `Relabel.valued_alike_iff`), and a choice of one option chooses no tied option and withholds at
  a full tie (`Relabel.EquivariantChoice.untied`, `Relabel.EquivariantChoice.withholds_of_full_tie`).
  Exchanging two options tells them apart: their equality is decided, a condition each statement
  names. Reading (the AI's, pending Ren): which option is which is not part of the record's
  relations; to part what the record ties takes a further recorded relation, such as an order of
  arrival or an agreement.

**Readings (the AI's, adopted on Ren's delegation of 15 October 2026, DELEGATED-CHOICES D25).**
- Any selection decided by what a selector registers (keeping, rewarding, reproducing,
  training) reaches exactly what that selector registers. It is blind to whatever a candidate's
  part does beyond the selector's registration closure, however far the candidate's reach
  closure extends. The gap is the reach closure less the registration closure.
- The gap closes only through relations: dependence, observation, or another's registration
  pooled, as the dweller's is in `Clearing`. Pooling with formations within the closure does not
  close it (`Flow.unselected_beyond_registration_all`).
- Where reaching beyond raises what registers, selection favours it (`Diversion`), and cannot
  tell it from raising what registers without reaching beyond. With `share_rises` the share of
  what reaches beyond rises among descendants while the world is open; enclosed, the selection
  stops with the descent (`Flow.descent_exhausted` of `Becoming.Capture`).
- Read for AI training, a reward process is a selector: training reaches only what the reward
  registers. The AI connects this with Ren's phrase from an earlier paper, "capability outruns
  correction": what is selected through a registration can reach beyond it, and correction by
  that registration does not reach there.

What is not derived: who selects, what the selector registers, that a selection is through
registration at all (supplied as `Web.SelectsThrough`), that offspring follow the selection,
that reaching beyond is chosen, that a selection reads the record alone, and how an option it
singles out is found (a search over listed options). The law for scores in the converse direction takes the
decidability of registering alike as a hypothesis. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

variable {F C : Type}

/-! ## Selection through registration -/

namespace Web

/-- A selection is through `f`'s registration up to `t`: histories `f` registers alike up to `t`
are selected alike. A selection is any claim about level histories: which are kept, rewarded or
leave more descendants. -/
def SelectsThrough (W : Web F C) (obs : F → C → Prop) (f : F) (t : Nat)
    (select : (Nat → C → Nat) → Prop) : Prop :=
  ∀ l l', W.RegistersAlikeUpTo obs f l l' t → (select l ↔ select l')

/-- A score is through `f`'s registration up to `t`: histories `f` registers alike up to `t`
score alike. -/
def ScoresThrough (W : Web F C) (obs : F → C → Prop) (f : F) (t : Nat)
    (score : (Nat → C → Nat) → Nat) : Prop :=
  ∀ l l', W.RegistersAlikeUpTo obs f l l' t → score l = score l'

/-- A selection is through a group's pooled registration up to `t`: histories every member
registers alike up to `t` are selected alike. -/
def SelectsThroughAll (W : Web F C) (obs : F → C → Prop) (group : F → Prop) (t : Nat)
    (select : (Nat → C → Nat) → Prop) : Prop :=
  ∀ l l', W.RegistersAlikeAll obs group l l' t → (select l ↔ select l')

variable {W : Web F C} {obs obs' : F → C → Prop} {g : F} {group : F → Prop}
  {l l' l'' : Nat → C → Nat} {t : Nat} {select select' : (Nat → C → Nat) → Prop}
  {score : (Nat → C → Nat) → Nat}

/-- Registering alike at a step is transitive. -/
theorem RegistersAlike.trans (first : W.RegistersAlike obs g l l' t)
    (second : W.RegistersAlike obs g l' l'' t) : W.RegistersAlike obs g l l'' t :=
  ⟨first.1.trans second.1, fun c observed => (first.2 c observed).trans (second.2 c observed)⟩

/-- Registering alike up to a step is transitive: with `RegistersAlike.refl` and
`RegistersAlikeUpTo.symm`, an equivalence. -/
theorem RegistersAlikeUpTo.trans (first : W.RegistersAlikeUpTo obs g l l' t)
    (second : W.RegistersAlikeUpTo obs g l' l'' t) : W.RegistersAlikeUpTo obs g l l'' t :=
  fun s le => (first s le).trans (second s le)

/-- Every member registers a history alike with itself. -/
theorem RegistersAlikeAll.refl (t : Nat) : W.RegistersAlikeAll obs group l l t :=
  fun _ _ s _ => RegistersAlike.refl s

/-- Registering alike in every member is symmetric. -/
theorem RegistersAlikeAll.symm (alike : W.RegistersAlikeAll obs group l l' t) :
    W.RegistersAlikeAll obs group l' l t :=
  fun g member => (alike g member).symm

/-- Registering alike in every member is transitive. -/
theorem RegistersAlikeAll.trans (first : W.RegistersAlikeAll obs group l l' t)
    (second : W.RegistersAlikeAll obs group l' l'' t) : W.RegistersAlikeAll obs group l l'' t :=
  fun g member => (first g member).trans (second g member)

/-- A formation's belief, the histories it registers alike with `l`, is a selection through its
registration. -/
theorem belief_selects : W.SelectsThrough obs g t (W.Belief obs g l t) :=
  fun _ _ alike => ⟨fun first => first.trans alike, fun second => second.trans alike.symm⟩

/-- **A selection reaches exactly what registers.** Two histories are selected alike by every
selection through `g`'s registration up to `t` exactly when `g` registers them alike up to `t`. -/
theorem selects_alike_iff :
    (∀ select, W.SelectsThrough obs g t select → (select l ↔ select l')) ↔
      W.RegistersAlikeUpTo obs g l l' t :=
  ⟨fun all => (all (W.Belief obs g l t) belief_selects).mp fun s _ => RegistersAlike.refl s,
   fun alike _ through => through l l' alike⟩

/-- **What registers apart is separated.** Where `g` does not register two histories alike up to
`t`, a selection through its registration, its belief, holds at the first and fails at the
second. -/
theorem separates (differ : ¬ W.RegistersAlikeUpTo obs g l l' t) :
    ∃ select, W.SelectsThrough obs g t select ∧ select l ∧ ¬ select l' :=
  ⟨W.Belief obs g l t, belief_selects, fun s _ => RegistersAlike.refl s, differ⟩

/-- **A selection through registration is tested completely.** Its selector refutes it exactly
where it fails. -/
theorem SelectsThrough.refutes_iff (through : W.SelectsThrough obs g t select) :
    W.Refutes obs select g l t ↔ ¬ select l :=
  ⟨Refutes.not_meets, fun fails l' meets alike => fails ((through l l' alike).mpr meets)⟩

/-- Admission at a step up to `t` is selected through registration up to `t`. -/
theorem admits_through {s : Nat} (le : s ≤ t) :
    W.SelectsThrough obs g t (fun l => W.Admits (l s) s g) :=
  fun _ _ alike => (alike s le).1

/-- The level of an observed condition at a step up to `t` is scored through registration up to
`t`. -/
theorem observed_scores {c : C} {s : Nat} (observed : obs g c) (le : s ≤ t) :
    W.ScoresThrough obs g t (fun l => l s c) :=
  fun _ _ alike => (alike s le).2 c observed

/-- A score's threshold is a selection through the same registration. -/
theorem ScoresThrough.atLeast (through : W.ScoresThrough obs g t score) (k : Nat) :
    W.SelectsThrough obs g t (fun l => k ≤ score l) :=
  fun l l' alike =>
    ⟨fun le => Nat.le_trans le (Nat.le_of_eq (through l l' alike)),
     fun le => Nat.le_trans le (Nat.le_of_eq (through l l' alike).symm)⟩

/-- A selection through registration up to a step is through registration up to every later
step. -/
theorem SelectsThrough.later {s : Nat} (through : W.SelectsThrough obs g s select) (le : s ≤ t) :
    W.SelectsThrough obs g t select :=
  fun l l' alike => through l l' (alike.earlier le)

/-- A selection through registration stays so under more observation. -/
theorem SelectsThrough.widen (larger : ∀ g c, obs g c → obs' g c)
    (through : W.SelectsThrough obs g t select) : W.SelectsThrough obs' g t select :=
  fun l l' alike => through l l' (alike.of_obs larger)

/-- What a selection through registration does not select is selected through it. -/
theorem SelectsThrough.not (through : W.SelectsThrough obs g t select) :
    W.SelectsThrough obs g t (fun l => ¬ select l) :=
  fun l l' alike =>
    ⟨fun fails holds => fails ((through l l' alike).mpr holds),
     fun fails holds => fails ((through l l' alike).mp holds)⟩

/-- Two selections through one registration select jointly through it. -/
theorem SelectsThrough.and (first : W.SelectsThrough obs g t select)
    (second : W.SelectsThrough obs g t select') :
    W.SelectsThrough obs g t (fun l => select l ∧ select' l) :=
  fun l l' alike =>
    ⟨fun ⟨one, two⟩ => ⟨(first l l' alike).mp one, (second l l' alike).mp two⟩,
     fun ⟨one, two⟩ => ⟨(first l l' alike).mpr one, (second l l' alike).mpr two⟩⟩

/-- **Scores reach exactly what registers, where registering alike is decidable.** Given, for
each history, whether `g` registers it alike with `l` up to `t`, two histories are scored alike
by every score through `g`'s registration exactly when `g` registers them alike: the mark of
the belief is such a score. -/
theorem scores_alike_iff (decided : ∀ m, Decidable (W.RegistersAlikeUpTo obs g l m t)) :
    (∀ score, W.ScoresThrough obs g t score → score l = score l') ↔
      W.RegistersAlikeUpTo obs g l l' t :=
  have through : W.ScoresThrough obs g t
      (fun m => @mark (W.RegistersAlikeUpTo obs g l m t) (decided m)) := fun m m' alike =>
    @mark_cases _ (decided m) (fun x => x = @mark _ (decided m'))
      (fun holds => @mark_cases _ (decided m') (fun y => 1 = y) (fun _ => rfl)
        fun fails => absurd (holds.trans alike) fails)
      (fun fails => @mark_cases _ (decided m') (fun y => 0 = y)
        (fun holds => absurd (holds.trans alike.symm) fails) fun _ => rfl)
  ⟨fun all =>
    have one : @mark _ (decided l) = 1 :=
      @mark_cases _ (decided l) (fun x => x = 1) (fun _ => rfl)
        fun fails => absurd (fun s _ => RegistersAlike.refl s) fails
    @mark_cases _ (decided l') (fun y => 1 = y → W.RegistersAlikeUpTo obs g l l' t)
      (fun holds _ => holds) (fun _ zero => Nat.noConfusion zero)
      (one.symm.trans (all _ through)),
   fun alike _ through => through l l' alike⟩

/-- **A member's selection is a group selection.** -/
theorem SelectsThrough.all (member : group g) (through : W.SelectsThrough obs g t select) :
    W.SelectsThroughAll obs group t select :=
  fun l l' alike => through l l' (alike g member)

/-- Two group selections select jointly through the pooled registration. -/
theorem SelectsThroughAll.and (first : W.SelectsThroughAll obs group t select)
    (second : W.SelectsThroughAll obs group t select') :
    W.SelectsThroughAll obs group t (fun l => select l ∧ select' l) :=
  fun l l' alike =>
    ⟨fun ⟨one, two⟩ => ⟨(first l l' alike).mp one, (second l l' alike).mp two⟩,
     fun ⟨one, two⟩ => ⟨(first l l' alike).mpr one, (second l l' alike).mpr two⟩⟩

/-- **A pooled selection reaches exactly what the pool registers.** Two histories are selected
alike by every selection through a group's pooled registration up to `t` exactly when every
member registers them alike up to `t`. -/
theorem selects_alike_all_iff :
    (∀ select, W.SelectsThroughAll obs group t select → (select l ↔ select l')) ↔
      W.RegistersAlikeAll obs group l l' t :=
  ⟨fun all => (all (fun m => W.RegistersAlikeAll obs group l m t)
      (fun _ _ alike => ⟨fun first => first.trans alike, fun second => second.trans alike.symm⟩)).mp
      (RegistersAlikeAll.refl t),
   fun alike _ through => through l l' alike⟩

/-- Where the members do not all register two histories alike up to `t`, a selection through the
pooled registration holds at the first and fails at the second. -/
theorem separates_all (differ : ¬ W.RegistersAlikeAll obs group l l' t) :
    ∃ select, W.SelectsThroughAll obs group t select ∧ select l ∧ ¬ select l' :=
  ⟨fun m => W.RegistersAlikeAll obs group l m t,
   fun _ _ alike => ⟨fun first => first.trans alike, fun second => second.trans alike.symm⟩,
   RegistersAlikeAll.refl t, differ⟩

end Web

/-! ## Blind beyond the registration closure -/

namespace Flow

variable {L L' : Flow F C} {W W' : Web F C} {obs : F → C → Prop} {part : F → Bool}
  {select : (Nat → C → Nat) → Prop} {score : (Nat → C → Nat) → Nat}

/-- **Selection is blind beyond the registration closure.** With the rest of the exchange fixed,
where every member of a part lies beyond `f`'s registration closure, every selection through the
registration of a formation within the closure, `f` among them, selects the levels with and
without the part alike: an instance of `unregistered_beyond_registration`. -/
theorem unselected_beyond_registration {l : Nat → C → Nat}
    (without : L.WithheldLevels part W l) {f : F}
    (balanced : ∀ t g c, L.WithinRegistration W obs f g → W.Registers obs g c →
      L.BalancesOn W [c] t)
    (beyond : ∀ h, part h = true → ¬ L.WithinRegistration W obs f h) {g : F}
    (within : L.WithinRegistration W obs f g) {t : Nat}
    (through : W.SelectsThrough obs g t select) : select W.level ↔ select l :=
  through _ _ fun s _ => unregistered_beyond_registration without balanced beyond s g within

/-- Every score through the registration of a formation within the closure scores the levels
with and without a part beyond it alike. -/
theorem unscored_beyond_registration {l : Nat → C → Nat}
    (without : L.WithheldLevels part W l) {f : F}
    (balanced : ∀ t g c, L.WithinRegistration W obs f g → W.Registers obs g c →
      L.BalancesOn W [c] t)
    (beyond : ∀ h, part h = true → ¬ L.WithinRegistration W obs f h) {g : F}
    (within : L.WithinRegistration W obs f g) {t : Nat}
    (through : W.ScoresThrough obs g t score) : score W.level = score l :=
  through _ _ fun s _ => unregistered_beyond_registration without balanced beyond s g within

/-- **Pooling within the closure stays blind.** Every selection through the pooled registration
of a group whose members lie within `f`'s registration closure selects the levels with and
without a part beyond the closure alike. -/
theorem unselected_beyond_registration_all {l : Nat → C → Nat}
    (without : L.WithheldLevels part W l) {f : F}
    (balanced : ∀ t g c, L.WithinRegistration W obs f g → W.Registers obs g c →
      L.BalancesOn W [c] t)
    (beyond : ∀ h, part h = true → ¬ L.WithinRegistration W obs f h) {group : F → Prop}
    (members : ∀ g, group g → L.WithinRegistration W obs f g) {t : Nat}
    (through : W.SelectsThroughAll obs group t select) : select W.level ↔ select l :=
  through _ _ fun g member s _ =>
    unregistered_beyond_registration without balanced beyond s g (members g member)

/-- **Blind beyond the closure where the members respond.** Under the hypotheses of
`alike_within_registration`, every selection through the registration of a formation within
`f`'s registration closure, drawn through both flows, selects the two flows' levels alike. -/
theorem unselected_beyond_registration_responsive {f : F}
    (balanced : ∀ t g c, WithinClosure (L.RegisteredFromEither W L' obs) f g →
      W.Registers obs g c → L.BalancesOn W [c] t)
    (balanced' : ∀ t g c, WithinClosure (L.RegisteredFromEither W L' obs) f g →
      W.Registers obs g c → L'.BalancesOn W' [c] t)
    (present : ∀ t, L.present t = L'.present t)
    (start : ∀ g, WithinClosure (L.RegisteredFromEither W L' obs) f g →
      ∀ c, W.Registers obs g c → W.level 0 c = W'.level 0 c)
    (responds : ∀ h, WithinClosure (L.RegisteredFromEither W L' obs) f h →
      ∀ t, W.RegistersAlikeUpTo obs h W.level W'.level t →
      ∀ g c, WithinClosure (L.RegisteredFromEither W L' obs) f g → W.Registers obs g c →
        L.take t h c = L'.take t h c ∧ L.give t h c = L'.give t h c)
    {g : F} (within : WithinClosure (L.RegisteredFromEither W L' obs) f g) {t : Nat}
    (through : W.SelectsThrough obs g t select) : select W.level ↔ select W'.level :=
  through _ _ fun s _ =>
    alike_within_registration balanced balanced' present start responds s g within

end Flow

/-! ## Share among descendants -/

section Share

variable {α : Type}

/-- **A selection's carriers gain share.** Let a selection give each parent whose history it holds
for at least `a` offspring and each other parent at most `b < a`. Where it holds for every parent
of `ms` and for none of `es`, both present, the parents of `ms` stand to those of `es` strictly
less than their offspring do: `share_rises`, the selection supplying the carriers. Where the
selection is through a selector's registration, parents whose histories it registers alike are
carriers together (`Web.SelectsThrough`), whatever their parts do beyond its registration
closure. -/
theorem share_rises_through {history : α → Nat → C → Nat} {kids : α → List α}
    {select : (Nat → C → Nat) → Prop} {ms es : List α} {a b : Nat}
    (carriers : ∀ p, p ∈ ms → select (history p)) (others : ∀ p, p ∈ es → ¬ select (history p))
    (rewarded : ∀ p, select (history p) → a ≤ (kids p).length)
    (unrewarded : ∀ p, ¬ select (history p) → (kids p).length ≤ b)
    (lt : b < a) (some : 0 < ms.length) (some' : 0 < es.length) :
    ms.length * offspringCount es kids < offspringCount ms kids * es.length :=
  share_rises (fun p mem => rewarded p (carriers p mem))
    (fun p mem => unrewarded p (others p mem)) lt some some'

end Share

/-! ## Selection by the record alone

Options are told apart only by what a record holds of each: an entry per option, of any kind. A
selection among them reads the record alone when exchanging two options' entries exchanges what it
selects (`Relabel.Equivariant`); a valuation of the options, such as a weight on each, reads the
record alone when it exchanges their values (`Relabel.EquivariantValue`); a choice of at most one
option does when it exchanges the choice (`Relabel.EquivariantChoice`). As a selection through
registration reaches exactly what registers (`Web.selects_alike_iff`), a selection by the record
alone reaches exactly what the record parts. -/

namespace Relabel

universe u v w

variable {K : Type u} {V : Type v} [DecidableEq K]

/-- Exchange the options `a` and `b`. -/
def swap (a b k : K) : K := if k = a then b else if k = b then a else k

theorem swap_left (a b : K) : swap a b a = b := if_pos rfl

theorem swap_right (a b : K) : swap a b b = a :=
  match decEq b a with
  | isTrue same => (show (if b = a then b else if b = b then a else b) = a from
      (if_pos same).trans same)
  | isFalse differ => (show (if b = a then b else if b = b then a else b) = a from
      (if_neg differ).trans (if_pos rfl))

theorem swap_other (a b : K) {k : K} (not_a : k ≠ a) (not_b : k ≠ b) : swap a b k = k :=
  (if_neg not_a).trans (if_neg not_b)

/-- Exchanging twice returns every option. -/
theorem swap_swap (a b k : K) : swap a b (swap a b k) = k :=
  match decEq k a with
  | isTrue at_a =>
    ((congrArg (swap a b) ((congrArg (swap a b) at_a).trans (swap_left a b))).trans
      (swap_right a b)).trans at_a.symm
  | isFalse not_a => match decEq k b with
    | isTrue at_b =>
      ((congrArg (swap a b) ((congrArg (swap a b) at_b).trans (swap_right a b))).trans
        (swap_left a b)).trans at_b.symm
    | isFalse not_b =>
      (congrArg (swap a b) (swap_other a b not_a not_b)).trans (swap_other a b not_a not_b)

theorem swap_inj (a b : K) {x y : K} (same : swap a b x = swap a b y) : x = y :=
  (swap_swap a b x).symm.trans ((congrArg (swap a b) same).trans (swap_swap a b y))

/-- A selection reads the record alone: where `r'` is `r` with the entries of `a` and `b`
exchanged, it selects at `r'` what it selects at `r`, exchanged. -/
def Equivariant (select : (K → V) → K → Prop) : Prop :=
  ∀ r r' a b, (∀ k, r' k = r (swap a b k)) → ∀ i, select r' i ↔ select r (swap a b i)

/-- A valuation of the options reads the record alone: exchanging two options' entries exchanges
their values. -/
def EquivariantValue {W : Type w} (value : (K → V) → K → W) : Prop :=
  ∀ r r' a b, (∀ k, r' k = r (swap a b k)) → ∀ i, value r' i = value r (swap a b i)

/-- A choice of at most one option reads the record alone: exchanging two options' entries
exchanges the choice. -/
def EquivariantChoice (rule : (K → V) → Option K) : Prop :=
  ∀ r r' a b, (∀ k, r' k = r (swap a b k)) → rule r' = (rule r).map (swap a b)

variable {r : K → V} {j k : K}

/-- Exchanging two tied options leaves the record as it was. -/
theorem fixed_of_tied (tie : r j = r k) : ∀ i, r i = r (swap j k i) := fun i =>
  match decEq i j with
  | isTrue at_j =>
    (congrArg r at_j).trans (tie.trans ((congrArg r (swap_left j k)).symm.trans
      (congrArg (fun x => r (swap j k x)) at_j.symm)))
  | isFalse not_j => match decEq i k with
    | isTrue at_k =>
      (congrArg r at_k).trans (tie.symm.trans ((congrArg r (swap_right j k)).symm.trans
        (congrArg (fun x => r (swap j k x)) at_k.symm)))
    | isFalse not_k => congrArg r (swap_other j k not_j not_k).symm

/-- **Tied options are selected alike.** -/
theorem Equivariant.tied {select : (K → V) → K → Prop} (equivariant : Equivariant select)
    (tie : r j = r k) : select r j ↔ select r k :=
  (equivariant r r j k (fixed_of_tied tie) j).trans (iff_of_eq (congrArg (select r) (swap_left j k)))

/-- **A selection by the record alone reaches exactly what the record parts.** Two options are
selected alike by every selection reading the record alone exactly when the record ties them. -/
theorem selected_alike_iff :
    (∀ select : (K → V) → K → Prop, Equivariant select → (select r j ↔ select r k)) ↔ r j = r k :=
  ⟨fun all => ((all (fun r' i => r' i = r j) (fun _ _ _ _ relabel i =>
      ⟨fun holds => (relabel i).symm.trans holds, fun holds => (relabel i).trans holds⟩)).mp
      rfl).symm,
   fun tie _ equivariant => equivariant.tied tie⟩

/-- **What is singled out is untied.** A selection reading the record alone that selects at most
one option at `r` selects none that another option's entry ties. -/
theorem Equivariant.untied {select : (K → V) → K → Prop} (equivariant : Equivariant select)
    (single : ∀ i i', select r i → select r i' → i = i') (selected : select r k) :
    ∀ j, j ≠ k → r j ≠ r k :=
  fun j differ tie => differ (single j k ((equivariant.tied tie).mpr selected) selected)

/-- At a full tie of two or more options, a selection reading the record alone that selects at
most one option selects none. -/
theorem Equivariant.none_of_full_tie {select : (K → V) → K → Prop}
    (equivariant : Equivariant select) (single : ∀ i i', select r i → select r i' → i = i')
    {a b : K} (two : a ≠ b) (tied : ∀ i i', r i = r i') : ∀ k, ¬ select r k :=
  fun k selected => match decEq k a with
  | isTrue at_a => equivariant.untied single selected b (fun same => two (at_a.symm.trans
      same.symm)) (tied b k)
  | isFalse not_a => equivariant.untied single selected a (fun same => not_a same.symm) (tied a k)

/-- The option holding `v` alone in the record. -/
def Alone (v : V) (r : K → V) (i : K) : Prop := r i = v ∧ ∀ j, j ≠ i → r j ≠ v

/-- Holding an entry alone is read off the record alone. -/
theorem alone_equivariant (v : V) : Equivariant (Alone (K := K) v) :=
  fun r _ a b relabel i =>
    ⟨fun ⟨holds, only⟩ => ⟨(relabel i).symm.trans holds, fun j differ same =>
        only (swap a b j)
          (fun at_i => differ ((swap_swap a b j).symm.trans (congrArg (swap a b) at_i)))
          ((relabel (swap a b j)).trans ((congrArg r (swap_swap a b j)).trans same))⟩,
     fun ⟨holds, only⟩ => ⟨(relabel i).trans holds, fun j differ same =>
        only (swap a b j) (fun at_i => differ (swap_inj a b at_i)) ((relabel j).symm.trans same)⟩⟩

/-- At most one option holds an entry alone. -/
theorem alone_single {v : V} {i i' : K} (first : Alone v r i) (second : Alone v r i') : i = i' :=
  match decEq i i' with
  | isTrue same => same
  | isFalse differ => absurd first.1 (second.2 i differ)

/-- **An option is singled out exactly where the record parts it.** Some selection reading the
record alone, selecting at most one option at each record, selects `k` at `r` exactly when no
other option's entry ties `k`'s. -/
theorem singled_iff_untied :
    (∃ select : (K → V) → K → Prop, Equivariant select ∧
      (∀ r' i i', select r' i → select r' i' → i = i') ∧ select r k) ↔
      ∀ j, j ≠ k → r j ≠ r k :=
  ⟨fun ⟨_, equivariant, single, selected⟩ => equivariant.untied (single r) selected,
   fun untied => ⟨Alone (r k), alone_equivariant (r k), fun _ _ _ => alone_single,
     ⟨rfl, untied⟩⟩⟩

/-! ### Values -/

section Values

variable {W : Type w} {value : (K → V) → K → W}

/-- **Tied options are valued alike**, a weight on each among them. -/
theorem EquivariantValue.tied (equivariant : EquivariantValue value) (tie : r j = r k) :
    value r j = value r k :=
  (equivariant r r j k (fixed_of_tied tie) j).trans (congrArg (value r) (swap_left j k))

/-- At a full tie every option is valued alike. -/
theorem EquivariantValue.full_tie (equivariant : EquivariantValue value)
    (tied : ∀ i i', r i = r i') (i i' : K) : value r i = value r i' :=
  equivariant.tied (tied i i')

/-- The options taking a given value form a selection reading the record alone. -/
theorem EquivariantValue.level (equivariant : EquivariantValue value) (c : W) :
    Equivariant (fun r i => value r i = c) :=
  fun r r' a b relabel i => ⟨fun holds => (equivariant r r' a b relabel i).symm.trans holds,
    fun holds => (equivariant r r' a b relabel i).trans holds⟩

/-- A constant valuation, the same weight on every option, reads the record alone. -/
theorem EquivariantValue.const (c : W) : EquivariantValue (fun (_ : K → V) (_ : K) => c) :=
  fun _ _ _ _ _ _ => rfl

end Values

/-- The entry itself is a valuation reading the record alone. -/
theorem entry_equivariant : EquivariantValue (fun (r : K → V) (i : K) => r i) :=
  fun _ _ _ _ relabel i => relabel i

/-- Two options are valued alike by every valuation reading the record alone exactly when the
record ties them. -/
theorem valued_alike_iff :
    (∀ value : (K → V) → K → V, EquivariantValue value → value r j = value r k) ↔ r j = r k :=
  ⟨fun all => all _ entry_equivariant, fun tie _ equivariant => equivariant.tied tie⟩

/-! ### Choices -/

section Choices

variable {rule : (K → V) → Option K}

theorem map_swap_eq_some (a b : K) {i : K} :
    ∀ {o : Option K}, o.map (swap a b) = some i ↔ o = some (swap a b i)
  | none => ⟨fun e => (nomatch e), fun e => (nomatch e)⟩
  | some c => ⟨fun e => congrArg some ((swap_swap a b c).symm.trans
        (congrArg (swap a b) (Option.some.inj e))),
      fun e => congrArg some ((congrArg (swap a b) (Option.some.inj e)).trans (swap_swap a b i))⟩

/-- A choice reading the record alone selects, reading the record alone, the option it chooses. -/
theorem EquivariantChoice.selects (equivariant : EquivariantChoice rule) :
    Equivariant (fun r i => rule r = some i) :=
  fun r r' a b relabel _ =>
    (iff_of_eq (congrArg (fun o => o = some _) (equivariant r r' a b relabel))).trans
      (map_swap_eq_some a b)

omit [DecidableEq K] in
/-- A choice chooses at most one option. -/
theorem EquivariantChoice.single (r : K → V) {i i' : K} (first : rule r = some i)
    (second : rule r = some i') : i = i' :=
  Option.some.inj (first.symm.trans second)

/-- **A choice reading the record alone chooses no tied option.** -/
theorem EquivariantChoice.untied (equivariant : EquivariantChoice rule) (chosen : rule r = some k) :
    ∀ j, j ≠ k → r j ≠ r k :=
  equivariant.selects.untied (fun _ _ => EquivariantChoice.single r) chosen

/-- **At a full tie of two or more options a choice reading the record alone withholds.** -/
theorem EquivariantChoice.withholds_of_full_tie (equivariant : EquivariantChoice rule) {a b : K}
    (two : a ≠ b) (tied : ∀ i i', r i = r i') : rule r = none :=
  match chosen : rule r with
  | none => rfl
  | some k => absurd chosen (equivariant.selects.none_of_full_tie
      (fun _ _ => EquivariantChoice.single r) two tied k)

end Choices

end Relabel

/-! ## Witnesses -/

/-! ### The gap in `Clearing` -/

namespace Clearing

/-- **What the clearer's selection cannot reach.** Every selection through the clearer's
registration (support only, the observation of `alike_for_clearer`) selects the cleared and the
spared world alike at every step, while the dweller is ended in the cleared world and not in the
spared one: that the dweller is ended is selected through the clearer's registration at no
step. -/
theorem unselected :
    (∀ t select, web.SelectsThrough supportOnly .clearer t select →
      (select web.level ↔ select sparedWeb.level)) ∧
      DwellerEnded web.level ∧ ¬ DwellerEnded sparedWeb.level ∧
      ∀ t, ¬ web.SelectsThrough supportOnly .clearer t DwellerEnded :=
  have spared : ¬ DwellerEnded sparedWeb.level := Web.Refutes.not_meets tested_by_dweller.2.2
  ⟨fun t _ through => through _ _ (alike_for_clearer t), tested_by_dweller.1, spared,
   fun t through => spared ((through _ _ (alike_for_clearer t)).mp tested_by_dweller.1)⟩

/-- **The gap.** The dweller lies within the clearer's reach closure and beyond its registration
closure; the clearer does not register the habitat its clearing takes from. -/
theorem dweller_within_reach :
    flow.WithinReach web .clearer .dweller ∧
      ¬ flow.WithinRegistration web supportOnly .clearer .dweller ∧
      ¬ web.Registers supportOnly .clearer .habitat :=
  ⟨reach_middle.1,
   fun within => reach_middle.2.2.2.1 (Flow.withinRegistration_supportOnly.mp within),
   fun registers => match registers with
    | .inl depends => Place.noConfusion (resource_of_clearer depends)
    | .inr no => no⟩

/-- In the spared world the dweller is admitted at the third step. -/
theorem dweller_spared : web.Admits (sparedWeb.level 2) 2 .dweller :=
  fun c requires => match c, requires with
  | .habitat, _ => Nat.le_succ 1
  | .resource, no => nomatch no
  | .fuel _, no => nomatch no

/-- In the spared world the clearer is admitted at the third step. -/
theorem clearer_spared : web.Admits (sparedWeb.level 2) 2 .clearer :=
  fun c requires => match c, requires with
  | .resource, _ => Nat.le_refl 1
  | .habitat, no => nomatch no
  | .fuel _, no => nomatch no

/-- **The dweller's registration selects.** The dweller's admission at the third step is a
selection through the dweller's registration; it holds in the spared world and fails in the
cleared one, which the dweller registers apart up to the third step. -/
theorem selected_by_dweller :
    web.SelectsThrough supportOnly .dweller 2 (fun l => web.Admits (l 2) 2 .dweller) ∧
      web.Admits (sparedWeb.level 2) 2 .dweller ∧ ¬ web.Admits (web.level 2) 2 .dweller ∧
      ¬ web.RegistersAlikeUpTo supportOnly .dweller web.level sparedWeb.level 2 :=
  ⟨Web.admits_through (Nat.le_refl 2), dweller_spared, unsupported_with 0,
   fun alike => unsupported_with 0 ((Web.admits_through (Nat.le_refl 2) _ _ alike).mpr
     dweller_spared)⟩

/-- The dweller registers the spared world alike with the world whose resource is gone at the
third step, at every step. -/
theorem dweller_alike_gone (t : Nat) :
    web.RegistersAlikeUpTo supportOnly .dweller sparedWeb.level resourceGone t :=
  fun _ _ => ⟨⟨fun admits c requires => (match c, requires with
      | .habitat, _ => admits .habitat trivial
      | .resource, no => nomatch no
      | .fuel _, no => nomatch no),
    fun admits c requires => (match c, requires with
      | .habitat, _ => admits .habitat trivial
      | .resource, no => nomatch no
      | .fuel _, no => nomatch no)⟩, fun _ no => False.elim no⟩

/-- At the third step the dweller and the clearer are both admitted. -/
def BothAdmitted (l : Nat → Place → Nat) : Prop :=
  web.Admits (l 2) 2 .dweller ∧ web.Admits (l 2) 2 .clearer

/-- **Pooled selection.** That both the dweller and the clearer are admitted at the third step is
a selection through the pooled registration of the clearer and the dweller. It holds in the
spared world and fails in the cleared one, and it is through neither registration alone: the
clearer registers the cleared world alike with the spared one, the dweller the world whose
resource is gone. -/
theorem selected_pooled :
    web.SelectsThroughAll supportOnly clearerAndDweller 2 BothAdmitted ∧
      BothAdmitted sparedWeb.level ∧ ¬ BothAdmitted web.level ∧
      ¬ web.SelectsThrough supportOnly .clearer 2 BothAdmitted ∧
      ¬ web.SelectsThrough supportOnly .dweller 2 BothAdmitted :=
  have dweller : web.SelectsThroughAll supportOnly clearerAndDweller 2
      (fun l => web.Admits (l 2) 2 .dweller) :=
    Web.SelectsThrough.all (g := Formation.dweller) trivial (Web.admits_through (Nat.le_refl 2))
  have clearer : web.SelectsThroughAll supportOnly clearerAndDweller 2
      (fun l => web.Admits (l 2) 2 .clearer) :=
    Web.SelectsThrough.all (g := Formation.clearer) trivial (Web.admits_through (Nat.le_refl 2))
  have spared : BothAdmitted sparedWeb.level := ⟨dweller_spared, clearer_spared⟩
  have cleared : ¬ BothAdmitted web.level := fun both => unsupported_with 0 both.1
  have gone : ¬ BothAdmitted resourceGone := fun both =>
    Nat.not_succ_le_zero 0 (both.2 .resource trivial)
  ⟨dweller.and clearer, spared, cleared,
   fun through => cleared ((through _ _ (alike_for_clearer 2)).mpr spared),
   fun through => gone ((through _ _ (dweller_alike_gone 2)).mp spared)⟩

end Clearing

/-! ### Diversion: selection favours reaching beyond

A taker gauges a store and depends on nothing; a dweller depends on a source, needing two units.
In the diverting flow the taker takes one unit of the source across the first step and gives it to
the store; in the undiverted flow nothing is exchanged; in the supplying flow the taker gives the
store one unit across the first step and takes nothing. -/

namespace Diversion

/-- A taker and a dweller. -/
inductive Formation where
  | taker
  | dweller

/-- The source the dweller depends on and the store the taker gauges. -/
inductive Place where
  | source
  | store

/-- One unit across the first step, nothing after. -/
def first : Nat → Nat
  | 0 => 1
  | _ + 1 => 0

/-- The source drawn: two at the start, one after. -/
def drawn : Nat → Nat
  | 0 => 2
  | _ + 1 => 1

/-- The store raised: nothing at the start, one after. -/
def raised : Nat → Nat
  | 0 => 0
  | _ + 1 => 1

/-- Across the first step the taker takes one unit of the source and gives one to the store. -/
def diverting : Flow Formation Place where
  present _ := [.taker, .dweller]
  take t f c := match f, c with
    | .taker, .source => first t
    | .taker, .store => 0
    | .dweller, _ => 0
  give t f c := match f, c with
    | .taker, .store => first t
    | .taker, .source => 0
    | .dweller, _ => 0

/-- Nothing is taken or given. -/
def undiverted : Flow Formation Place where
  present _ := [.taker, .dweller]
  take _ _ _ := 0
  give _ _ _ := 0

/-- Across the first step the taker gives the store one unit and takes nothing. -/
def supplying : Flow Formation Place where
  present _ := [.taker, .dweller]
  take _ _ _ := 0
  give := diverting.give

/-- The levels of the diverting flow: the source drawn, the store raised. -/
def divertedLevel (t : Nat) : Place → Nat
  | .source => drawn t
  | .store => raised t

/-- The levels of the undiverted flow: the source at two, the store at nothing. -/
def undivertedLevel (_ : Nat) : Place → Nat
  | .source => 2
  | .store => 0

/-- The levels of the supplying flow: the source at two, the store raised. -/
def suppliedLevel (t : Nat) : Place → Nat
  | .source => 2
  | .store => raised t

/-- The dweller requires the source at need two and is active exactly while it stands so; the
taker requires nothing, is active throughout and draws on the source. -/
def web (level : Nat → Place → Nat) : Web Formation Place where
  level := level
  active t f := match f with
    | .taker => True
    | .dweller => 2 ≤ level t .source
  requires _ f c := match f, c with
    | .dweller, .source => True
    | .dweller, .store => False
    | .taker, _ => False
  need _ _ _ := 2
  draws _ f c := match f, c with
    | .taker, .source => True
    | .taker, .store => False
    | .dweller, _ => False

/-- The taker observes the store. -/
def gauge : Formation → Place → Prop
  | .taker, .store => True
  | .taker, .source => False
  | .dweller, _ => False

/-- The store stands at least `k` at step `t`. -/
def StoreAtLeast (k t : Nat) (l : Nat → Place → Nat) : Prop :=
  k ≤ l t .store

/-- The taker alone. -/
def takerAlone : Formation → Prop
  | .taker => True
  | .dweller => False

theorem diverting_balances : diverting.Balances (web divertedLevel)
  | 0, .source => rfl
  | _ + 1, .source => rfl
  | 0, .store => rfl
  | _ + 1, .store => rfl

theorem undiverted_balances : undiverted.Balances (web undivertedLevel)
  | _, .source => rfl
  | _, .store => rfl

theorem supplying_balances : supplying.Balances (web suppliedLevel)
  | _, .source => rfl
  | 0, .store => rfl
  | _ + 1, .store => rfl

/-- In every web of the witness activity needs support. -/
theorem dependent (level : Nat → Place → Nat) : (web level).Dependent
  | _, .taker, _, _, no => nomatch no
  | _, .dweller, active, .source, _ => active
  | _, .dweller, _, .store, no => nomatch no

/-- In the diverting flow only active formations give. -/
theorem diverting_acting : diverting.Acting (web divertedLevel)
  | _, .taker, _, _, _ => trivial
  | _, .dweller, _, _, gives => absurd gives (Nat.lt_irrefl 0)

/-- In the diverting flow only active formations take, and only from what they draw on. -/
theorem diverting_taking : diverting.Taking (web divertedLevel)
  | _, .taker, .source, _, _ => ⟨trivial, trivial⟩
  | _, .taker, .store, _, takes => absurd takes (Nat.lt_irrefl 0)
  | _, .dweller, _, _, takes => absurd takes (Nat.lt_irrefl 0)

/-- In the diverting flow the taker alone is closed under being affected through what is
registered: only the taker exchanges with the store, and it depends on nothing. -/
theorem takerAlone_closed :
    ClosedUnder (diverting.RegisteredFrom (web divertedLevel) gauge) takerAlone
  | .taker, .taker, _, _ => trivial
  | .taker, .dweller, _, ⟨_, _, _, _, .inl takes⟩ => absurd takes (Nat.lt_irrefl 0)
  | .taker, .dweller, _, ⟨_, _, _, _, .inr gives⟩ => absurd gives (Nat.lt_irrefl 0)
  | .dweller, _, no, _ => nomatch no

/-- In the supplying flow the taker alone is closed under affecting: it exchanges with the store
only, which the dweller does not depend on. -/
theorem supplied_closed : ClosedUnder (supplying.Affects (web suppliedLevel)) takerAlone
  | _, .taker, _, _ => trivial
  | .taker, .dweller, _, ⟨.source, _, _, _, .inl takes⟩ => absurd takes (Nat.lt_irrefl 0)
  | .taker, .dweller, _, ⟨.source, _, _, _, .inr gives⟩ => absurd gives (Nat.lt_irrefl 0)
  | .taker, .dweller, _, ⟨.store, ⟨_, no⟩, _⟩ => nomatch no
  | .dweller, _, no, _ => nomatch no

/-- **Selection favours reaching beyond.** Both flows balance and in both activity needs support;
in the diverting flow only active formations give and take, and take only from what they draw on.
The diverting flow reaches the dweller, which lies within the taker's reach closure and beyond its
registration closure; the undiverted flow does not reach it. The selection that the store stands
at least one at the second step is through the taker's registration, holds in the diverting flow
and fails in the undiverted one. The dweller is unsupported from the second step on in the
diverting flow and supported at every step in the undiverted one. -/
theorem favours :
    diverting.Balances (web divertedLevel) ∧ undiverted.Balances (web undivertedLevel) ∧
      (web divertedLevel).Dependent ∧ (web undivertedLevel).Dependent ∧
      diverting.Acting (web divertedLevel) ∧ diverting.Taking (web divertedLevel) ∧
      diverting.WithinReach (web divertedLevel) .taker .dweller ∧
      ¬ diverting.WithinRegistration (web divertedLevel) gauge .taker .dweller ∧
      ¬ undiverted.WithinReach (web undivertedLevel) .taker .dweller ∧
      (web divertedLevel).SelectsThrough gauge .taker 1 (StoreAtLeast 1 1) ∧
      StoreAtLeast 1 1 divertedLevel ∧ ¬ StoreAtLeast 1 1 undivertedLevel ∧
      (∀ n, ¬ (web divertedLevel).Supported (n + 1) .dweller) ∧
      ∀ t, (web undivertedLevel).Supported t .dweller :=
  ⟨diverting_balances, undiverted_balances, dependent _, dependent _, diverting_acting,
   diverting_taking,
   WithinClosure.of_rel ⟨.source, ⟨0, trivial⟩, 0, .head _, .inl Nat.zero_lt_one⟩,
   fun within => within takerAlone takerAlone_closed trivial,
   fun within => within takerAlone (fun _ _ _ ⟨_, _, _, _, exchanges⟩ => match exchanges with
     | .inl takes => absurd takes (Nat.lt_irrefl 0)
     | .inr gives => absurd gives (Nat.lt_irrefl 0)) trivial,
   (Web.observed_scores (W := web divertedLevel) (g := Formation.taker) (c := Place.store)
     trivial (Nat.le_refl 1)).atLeast 1,
   Nat.le_refl 1, Nat.not_succ_le_zero 0,
   fun _ supported => Nat.lt_irrefl 1 (supported .source trivial),
   fun _ c requires => match c, requires with
    | .source, _ => Nat.le_refl 2
    | .store, no => nomatch no⟩

/-- **Selection cannot tell reaching beyond from not.** The supplying flow balances, raises the
store as the diverting flow does, and reaches nothing beyond the taker. The taker registers the
diverting and the supplying levels alike at every step, so every selection through its
registration selects them alike, while the dweller is supported at every step in the supplying
flow and unsupported from the second step on in the diverting one. -/
theorem blind_to_source :
    supplying.Balances (web suppliedLevel) ∧ (web suppliedLevel).Dependent ∧
      ¬ supplying.WithinReach (web suppliedLevel) .taker .dweller ∧
      (∀ t, (web divertedLevel).RegistersAlikeUpTo gauge .taker divertedLevel suppliedLevel t) ∧
      (∀ t select, (web divertedLevel).SelectsThrough gauge .taker t select →
        (select divertedLevel ↔ select suppliedLevel)) ∧
      (∀ t, (web suppliedLevel).Supported t .dweller) ∧
      ∀ n, ¬ (web divertedLevel).Supported (n + 1) .dweller :=
  have alike : ∀ t,
      (web divertedLevel).RegistersAlikeUpTo gauge .taker divertedLevel suppliedLevel t :=
    fun _ _ _ => ⟨⟨fun _ _ no => (nomatch no), fun _ _ no => (nomatch no)⟩,
      fun c observed => match c, observed with
      | .store, _ => rfl
      | .source, no => nomatch no⟩
  ⟨supplying_balances, dependent _,
   fun within => within takerAlone supplied_closed trivial,
   alike, fun t _ through => through _ _ (alike t),
   fun _ c requires => match c, requires with
    | .source, _ => Nat.le_refl 2
    | .store, no => (nomatch no),
   fun _ supported => Nat.lt_irrefl 1 (supported .source trivial)⟩

end Diversion

end Becoming
