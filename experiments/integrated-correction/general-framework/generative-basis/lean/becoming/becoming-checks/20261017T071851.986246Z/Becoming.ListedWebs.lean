import Becoming.Identity
import Becoming.Locality
import Becoming.Space

/-!
# Listed webs: the laws of listing what is active, read of a web's activity

`Becoming.Population` states the census law for any determination listed at each step, each
member once (`Listed`); `Becoming.Change` states what holds of every finite family of
determinations; `Becoming.Locality` states the laws of one stretch for a list holding what holds
at one step; and `Becoming.Identity` states when more forces arising under a continuation. A web
carries the determination these laws are about: a formation's activity, `W.active t f`, of which
arising (`Web.Arises`) and ceasing (`Web.Ceases`) are the coming and ceasing to be
(`Web.change_readings`), and a census of a web is a listing of it (`Web.Census`). This module
states those laws of a web's activity and proves them through the general laws.

* **The census balance across a step and over a stretch.** Under a census, the formations active
  after a step with those that ceased across it are those active before with those that arose
  (`across`); over any stretch the ceasings are at most the arisings with those active at the
  start, and the arisings at most the ceasings with those active at the end (`ceasings_within`,
  `arisings_within`). Where at most `B t` are active at each step and the arisings over some
  stretch from every step outnumber the bound at its end, ceasing recurs (`ceasing_of_outpacing`).
* **A finite family of formations, with no census.** Over any stretch, the arisings and ceasings of
  the members of a finite list differ by at most its length (`keep_pace`); a formation active at a
  step that ceases at no later step stays active (`persists`).
* **One stretch, from one listing.** With a list holding exactly the formations active at `N`, each
  once, and nothing arising across the stretch of `n` steps from `N`, every formation active at a
  step of the stretch is on the list, every one ceasing there is on it, and those active at the end
  with those that ceased number the list (`ceasing_needs_arising`). With a list covering the
  formations active at `N` and nothing arising from `N` on, ceasing does not recur
  (`ceasing_not_recurring`); no decidability is needed. Where something ceases at arbitrarily late
  steps, any number of distinct steps from `N` see a ceasing, all before some step
  (`ceasing_steps_found`).
* **Arising forced across a step.** Under a census at a step and the next, under every
  continuation in which no formation continues as two, not every formation active after the step
  continues one active before, exactly when more are active after than before
  (`forced_iff_more`); and across every web, more active after a step forces this exactly under a
  continuation in which no formation continues as two (`forces_iff_noSplit`).
* **Rest, unrefuted.** That a world rests from some step on cannot be refuted exactly when it is
  not the case that after every step a later arising or ceasing stays unrefuted
  (`rests_unrefuted_iff`); no decidedness is needed.

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

namespace ListedWebs

variable {F C : Type}

/-! ## The census balance -/

section Census

variable {W : Web F C} [∀ t f, Decidable (W.active t f)] {alive : Nat → List F}

/-- **The census balance across a step.** Under a census of a web, the formations active after a
step with those that ceased across it are those active before it with those that arose. -/
theorem across (census : W.Census alive) (t : Nat) :
    (alive (t + 1)).length + total (alive t) (fun f => mark (W.Ceases t f)) =
      (alive t).length + total (alive (t + 1)) (fun f => mark (W.Arises t f)) :=
  Listed.across census t

/-- **Ceasings are at most arisings with those active at the start.** Under a census, over any
stretch. -/
theorem ceasings_within (census : W.Census alive) (S n : Nat) :
    total (steps S n) (fun t => total (alive t) fun f => mark (W.Ceases t f)) ≤
      (alive S).length + total (steps S n) (fun t => total (alive (t + 1)) fun f =>
        mark (W.Arises t f)) :=
  Listed.ceasings_within census S n

/-- **Arisings are at most ceasings with those active at the end.** Under a census, over any
stretch: where at most `B` are active, at most `B` more arise than cease. -/
theorem arisings_within (census : W.Census alive) (S n : Nat) :
    total (steps S n) (fun t => total (alive (t + 1)) fun f => mark (W.Arises t f)) ≤
      (alive (S + n)).length + total (steps S n) (fun t => total (alive t) fun f =>
        mark (W.Ceases t f)) :=
  Listed.comings_within census S n

/-- **The rate law of a web.** Under a census with at most `B t` formations active at each step
`t`, where from each step the arisings over some stretch outnumber the bound at its end, some
formation ceases at arbitrarily late steps. -/
theorem ceasing_of_outpacing (census : W.Census alive) {B : Nat → Nat}
    (bounded : ∀ t, (alive t).length ≤ B t)
    (outpacing : ∀ N, ∃ n, B (N + n) <
      total (steps N n) fun t => total (alive (t + 1)) fun f => mark (W.Arises t f)) :
    ∀ N, ∃ t f, N ≤ t ∧ W.Ceases t f :=
  Listed.ceasing_of_outpacing census bounded outpacing

end Census

/-! ## A finite family of formations -/

section Family

variable (W : Web F C) [∀ t f, Decidable (W.active t f)]

/-- **Arising and ceasing keep pace in a finite family.** Over any stretch, the arisings and the
ceasings of the members of a finite list of formations differ by at most its length. -/
theorem keep_pace (fs : List F) (S n : Nat) :
    total (steps S n) (fun t => total fs fun f => mark (W.Arises t f)) ≤
        fs.length + total (steps S n) (fun t => total fs fun f => mark (W.Ceases t f)) ∧
      total (steps S n) (fun t => total fs fun f => mark (W.Ceases t f)) ≤
        fs.length + total (steps S n) (fun t => total fs fun f => mark (W.Arises t f)) :=
  Becoming.keep_pace (as := fs) (p := fun f t => W.active t f) S n

/-- **What ceases at no later step stays active.** A formation active at step `S` that ceases
across no step from `S` on is active at every later step. -/
theorem persists {f : F} {S : Nat} (active : W.active S f)
    (unceasing : ∀ t, S ≤ t → ¬ W.Ceases t f) : ∀ n, W.active (S + n) f :=
  Becoming.persists (p := fun t => W.active t f) active unceasing

end Family

/-! ## One stretch, from one listing -/

section Stretch

variable {W : Web F C}

/-- **Ceasing needs arising, on a web.** With a list holding exactly the formations active at `N`,
each once, and no formation arising across the stretch of `n` steps from `N`: every formation
active at a step of the stretch is on the list, every formation ceasing there is on it, and those
active at the end with those that ceased since `N` number the list. -/
theorem ceasing_needs_arising [∀ t f, Decidable (W.active t f)] {l : List F} {N n : Nat}
    (lists : Distinct l ∧ ∀ f, W.active N f ↔ f ∈ l)
    (none : ∀ s f, N ≤ s → s < N + n → ¬ W.Arises s f) :
    (∀ k, k ≤ n → ∀ f, W.active (N + k) f → f ∈ l) ∧
      (∀ s f, N ≤ s → s < N + n → W.Ceases s f → f ∈ l) ∧
      total l (fun f => mark (W.active (N + n) f)) +
          total (steps N n) (fun t => total l fun f => mark (W.Ceases t f)) = l.length :=
  Becoming.ceasing_needs_arising (p := fun f t => W.active t f) lists none

/-- **With nothing arising from a step on, ceasing does not recur.** Where a list covers the
formations active at `N` and no formation arises at any step from `N` on, it is not the case that
some formation ceases at arbitrarily late steps. No decidability is needed. -/
theorem ceasing_not_recurring {l : List F} {N : Nat} (covers : ∀ f, W.active N f → f ∈ l)
    (none : ∀ s f, N ≤ s → ¬ W.Arises s f) : ¬ ∀ M, ∃ t f, M ≤ t ∧ W.Ceases t f :=
  Covers.ceasing_not_recurring (p := fun f t => W.active t f) covers
    fun _ s f from_ _ => none s f from_

/-- **Recurring ceasing, found step by step.** Where some formation ceases at arbitrarily late
steps, for every `k` there are `k` distinct steps from `N`, all before some step, at each of which
some formation ceases. -/
theorem ceasing_steps_found (ceasing : ∀ M, ∃ t f, M ≤ t ∧ W.Ceases t f) (N : Nat) :
    ∀ k, ∃ E U, Distinct E ∧ E.length = k ∧ N ≤ U ∧
      ∀ t, t ∈ E → N ≤ t ∧ t < U ∧ ∃ f, W.Ceases t f :=
  Becoming.ceasing_steps_found (p := fun f t => W.active t f) ceasing N

end Stretch

/-! ## Arising forced across a step -/

section Forced

variable {W : Web F C}

/-- **Arising is forced across a step exactly where more are active after it.** Under a listing
of the active formations at a step and the next, each once: under every continuation in which no
formation continues as two, not every formation active after the step continues one active before
it, exactly when more formations are active after the step than before. -/
theorem forced_iff_more {alive : Nat → List F} {t : Nat}
    (now : Distinct (alive t) ∧ ∀ f, W.active t f ↔ f ∈ alive t)
    (next : Distinct (alive (t + 1)) ∧ ∀ f, W.active (t + 1) f ↔ f ∈ alive (t + 1)) :
    (∀ S : F → F → Prop, (∀ g f f', S g f → S g f' → f = f') →
      ¬ ∀ f, W.active (t + 1) f → W.Continues (fun _ => S) t f) ↔
      (alive t).length < (alive (t + 1)).length :=
  ⟨fun forced => (Becoming.forced_iff_more now.1 next.1).mp fun S noSplit covered =>
     forced S noSplit fun f active => match covered f ((next.2 f).mp active) with
       | ⟨g, mem, continues⟩ => ⟨g, (now.2 g).mpr mem, continues⟩,
   fun more S noSplit covered => (Becoming.forced_iff_more now.1 next.1).mpr more S noSplit
     fun f mem => match covered f ((next.2 f).mpr mem) with
       | ⟨g, active, continues⟩ => ⟨g, (now.2 g).mp active, continues⟩⟩

/-- **More forces arising across every web exactly where nothing continues as two.** Across every
step of every web, where more formations active after the step are listed, each once, than a list
covering those active before it holds, not every formation active after the step continues under
`S` one active before it, exactly when under `S` no formation continues as two. -/
theorem forces_iff_noSplit [DecidableEq F] {S : F → F → Prop} :
    (∀ (W : Web F C) (t : Nat) (before after : List F), (∀ f, W.active t f → f ∈ before) →
      Distinct after → (∀ f, f ∈ after → W.active (t + 1) f) → before.length < after.length →
        ¬ ∀ f, W.active (t + 1) f → W.Continues (fun _ => S) t f) ↔
      ∀ g f f', S g f → S g f' → f = f' :=
  ⟨fun forces => Becoming.forces_iff_noSplit.mp fun before after distinct more covered =>
     forces ⟨fun _ _ => 0, fun t f => (t = 0 ∧ f ∈ before) ∨ (t ≠ 0 ∧ f ∈ after),
         fun _ _ _ => False, fun _ _ _ => 0, fun _ _ _ => False⟩ 0 before after
       (fun _ held => held.elim And.right fun other => absurd rfl other.1)
       distinct (fun _ mem => .inr ⟨fun zero => Nat.noConfusion zero, mem⟩) more
       fun f held => match covered f (held.elim (fun zero => Nat.noConfusion zero.1)
           And.right) with
         | ⟨g, mem, continues⟩ => ⟨g, .inl ⟨rfl, mem⟩, continues⟩,
   fun noSplit _ _ before after listed distinct now more covered =>
     Becoming.forces_iff_noSplit.mpr noSplit before after distinct more fun f mem =>
       match covered f (now f mem) with
       | ⟨g, active, continues⟩ => ⟨g, listed g active, continues⟩⟩

end Forced

/-! ## Rest, unrefuted -/

/-- **A world's rest, unrefuted.** That a world rests from some step from `T` on cannot be refuted
exactly when it is not the case that after every step from `T` on a later arising or ceasing of
some relatum stays unrefuted. No decidedness is needed. -/
theorem rests_unrefuted_iff (w : World) {T : Nat} :
    (¬ ∀ M, T ≤ M → ¬ ¬ ∃ t, M ≤ t ∧ ∃ x, w.web.Arises t x ∨ w.web.Ceases t x) ↔
      ¬ ¬ ∃ M, T ≤ M ∧ w.RestsFrom M :=
  (stop_unrefuted_iff (P := fun t => ∃ x, w.web.Arises t x ∨ w.web.Ceases t x)).trans
    ⟨fun unrefuted never => unrefuted fun ⟨M, from_, quiet⟩ => never ⟨M, from_, fun t later x =>
       ⟨fun arises => quiet t later ⟨x, .inl arises⟩,
        fun ceases => quiet t later ⟨x, .inr ceases⟩⟩⟩,
     fun unrefuted never => unrefuted fun ⟨M, from_, rests⟩ =>
       never ⟨M, from_, fun t later ⟨x, moves⟩ => moves.elim (rests t later x).1 (rests t later x).2⟩⟩

end ListedWebs

end Becoming
