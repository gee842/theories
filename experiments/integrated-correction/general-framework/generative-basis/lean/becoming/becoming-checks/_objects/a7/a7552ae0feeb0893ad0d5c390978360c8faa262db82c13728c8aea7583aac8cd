import Becoming.Unfolding
import Becoming.Diagonal
import Becoming.Context
import Becoming.Learning

/-!
# What a description keeps and loses

A description of an unfolding cuts it: into parts described one at a time, or into classes a
reading lumps together. This module states what a cut keeps and what it loses, with no premise.

* **Separation loses exactly the relation.** Describing each part by what it can be, with
  nothing of what it goes with, keeps every combination that occurs (`separated_of_whole`) and
  gives back the whole exactly where the whole is rectangular, whatever goes with one part going
  with every other (`separation_faithful_iff`). The lost relation reappears as surplus: two
  parts that always go alike, described separately, could go apart (`separation_surplus`).
* **A relation held by no part.** Three parts can be related as a whole while every two of them
  are free (`whole_not_in_pairs`), so describing every pair still loses it. Read on Specker's
  three boxes and their pairs (`Becoming.Context`), parity is a whole its pairs do not give back
  (`evenBoxes_glued`, `evenBoxes_not_determined`), while Specker's possibilities on the same pairs
  are the parts of no whole (`Specker.no_whole`): the two ways the parts fail a whole.
* **A relation forms, lasts and ends in the joint law.** A law that moves each part by itself
  never relates unrelated parts (`Rectangular.image_of_separate`); a law that copies one part into
  the other does (`copy_relates`). Once formed, a relation lasts under every law that moves each
  part by itself and loses nothing of what occurs (`relation_persists`), so it ends only by loss
  within what occurs, as where a part is forgotten (`forgetting_unrelates`), or by what acts on
  the parts together: for example, a coupling that relates two parts unrelates them when it acts
  a second time, losing nothing either way (`coupling_relates_and_unrelates`).
* **The split that makes sense, under a determined law.** `Becoming.Unfolding` (P69) states
  when a description makes sense (`MakesSense`: it identifies exactly the alike configurations)
  and, for a determined law read through a registration (`Law.registered`), that alike is the
  same registered future (`Law.alike_iff_sameFuture`). In those terms: a split that keeps what
  is registered and carries a law in `Becoming.Mechanism`'s sense (`GoAlike`) relates
  configurations by a bisimulation (`Law.kernel_bisimulation`), so it loses nothing registered
  (`Law.sameFuture_of_law`), and the coarsest such split makes sense (`Law.makesSense_of_law`).
  Carrying a law is not enough: the split that lumps everything always carries one
  (`goAlike_const`) and makes sense only where nothing registered ever differs
  (`Law.const_makesSense_iff`). Registering everything, the configuration itself makes sense
  (`Law.whole_makesSense`). What is registered now makes sense by itself exactly where it
  carries a law, a condition on one step (`Law.now_makesSense_iff_goAlike`), equivalently where it
  fixes its own registered future (`Law.now_makesSense_iff`). So a registered part alone makes
  sense exactly where the rest makes no difference to its next value
  (`Law.part_makesSense_iff_step`, `Law.part_makesSense_iff`), and otherwise the split that makes
  sense includes the rest. For a part whose next value is set by a rule that changes with it, as
  in `Becoming.Mechanism`'s `adaptive`, that is the rule making no difference to it
  (`Law.adaptive_makesSense_iff`).
* **The pair.** Where a standing changes by a passing and only the standing is registered
  (`Motion.move`), the split that makes sense is the pair (`Motion.makes_sense`); the standing
  alone carries no law, as `Becoming.Mechanism`'s `adaptive_state_law_iff` gives with the
  passing as the rule (`Motion.standing_alone`), and the passing alone loses the standing
  (`Motion.passing_alone`), so neither alone makes sense (`Motion.neither_alone`). Where nothing
  passes, the standing alone makes sense (`Motion.still_makes_sense`).
* **States from one registered history.** Two moments of one registered unfolding are one state
  when everything registered after them is alike (`SameAhead`); this is an equivalence that goes
  on as itself (`SameAhead.next`), `Becoming.Unfolding`'s same registered future read along
  an orbit (`sameAhead_orbit_iff`), so states and their law are read off the history with no
  configuration given. Where every moment is registered differently, each moment is its own
  state (`SameAhead.new_each`). This needs no law given beforehand beyond the succession of
  steps, the representation's shared step index: every registered history is a determined law,
  the law of moments, read through what is registered, and its alike moments
  are the moments that are one state (`alike_moments_iff`, through `Becoming.Unfolding`). A
  registered history has finitely many states exactly where two of its moments are one state,
  that is, where its registration repeats from some moment on (`finitely_many_states_iff`, by a
  pigeonhole up to a relation with no decision, `shared_below`); a configuration that returns
  has finitely many states under every registration (`Law.Returns.states`). The two-valued
  denial, `Becoming.Diagonal`'s rhythm of a revision that never rests, has exactly two states
  (`Denial.two_states`), each defined through the other (`Denial.each_through_other`).
  `Becoming.Learning`'s lasso course is two moments being one state (`lasso_iff_sameAhead`), so
  finitely many states is a lasso (`finitely_many_states_iff_lasso`).

So a cut keeps everything exactly where what it cuts is unrelated, and a relation is made and
unmade only by what acts on the parts together or by loss; relative to what is registered, one
split loses no difference that will make a difference and adds none that never will, and the law
comes out of it. That an unfolding has a law is not a premise beyond the succession of its steps:
its states and their law are read off what it registers, and they are finitely many exactly
where the registration repeats from some moment on. The readings of this as what a projection
deducts, as 阴阳, as what makes two a pair, or as the tests a decomposition owes the nondual
method belong to the study, not to this module.

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v w

/-! ## Separation -/

section Separation

variable {A : Type u} {B : Type v}

/-- Whatever goes with one part goes with every other: the parts are unrelated. -/
def Rectangular (whole : A × B → Prop) : Prop :=
  ∀ a a' b b', whole (a, b) → whole (a', b') → whole (a, b')

/-- Each part described by itself: what it can be, with nothing of what it goes with. -/
def Separated (whole : A × B → Prop) (p : A × B) : Prop :=
  (∃ b, whole (p.1, b)) ∧ (∃ a, whole (a, p.2))

/-- Separation keeps every combination that occurs. -/
theorem separated_of_whole {whole : A × B → Prop} {p : A × B} (h : whole p) :
    Separated whole p :=
  ⟨⟨p.2, h⟩, ⟨p.1, h⟩⟩

/-- **Separation adds nothing exactly when the parts are unrelated.** -/
theorem separation_faithful_iff {whole : A × B → Prop} :
    (∀ p, Separated whole p → whole p) ↔ Rectangular whole :=
  ⟨fun faithful a a' b b' hab ha'b' => faithful (a, b') ⟨⟨b, hab⟩, ⟨a', ha'b'⟩⟩,
   fun rect p ⟨⟨b, hb⟩, ⟨a, ha⟩⟩ => rect p.1 a b p.2 hb ha⟩

/-- Two parts that always go alike, described separately, could go apart: the lost relation
reappears as surplus. -/
theorem separation_surplus :
    Separated (fun p : Bool × Bool => p.1 = p.2) (true, false) ∧
      ¬ (fun p : Bool × Bool => p.1 = p.2) (true, false) :=
  ⟨⟨⟨true, rfl⟩, ⟨false, rfl⟩⟩, fun h => nomatch h⟩

/-- `flipIf x b` turns `b` over exactly when `x` holds. -/
def flipIf : Bool → Bool → Bool
  | true, b => !b
  | false, b => b

/-- Three parts related as a whole: their parity is even. -/
def EvenThree (p : Bool × Bool × Bool) : Prop := flipIf p.1 (flipIf p.2.1 p.2.2) = false

/-- **A relation held by the whole and by no part.** Every two of the three may be anything,
and the three may not. -/
theorem whole_not_in_pairs :
    (∀ x y : Bool, ∃ z, EvenThree (x, y, z)) ∧ (∀ y z : Bool, ∃ x, EvenThree (x, y, z)) ∧
      (∀ x z : Bool, ∃ y, EvenThree (x, y, z)) ∧ ¬ EvenThree (true, false, false) :=
  ⟨fun x y => match x, y with
    | true, true => ⟨false, rfl⟩
    | true, false => ⟨true, rfl⟩
    | false, true => ⟨true, rfl⟩
    | false, false => ⟨false, rfl⟩,
   fun y z => match y, z with
    | true, true => ⟨false, rfl⟩
    | true, false => ⟨true, rfl⟩
    | false, true => ⟨true, rfl⟩
    | false, false => ⟨false, rfl⟩,
   fun x z => match x, z with
    | true, true => ⟨false, rfl⟩
    | true, false => ⟨true, rfl⟩
    | false, true => ⟨true, rfl⟩
    | false, false => ⟨false, rfl⟩,
   fun h => nomatch h⟩

/-- The same relation on Specker's three boxes (`Becoming.Context`): their values have even
parity. -/
def evenBoxes (v : Specker.Box → Bool) : Prop := flipIf (v .a) (flipIf (v .b) (v .c)) = false

theorem flipIf_self : ∀ x : Bool, flipIf x x = false
  | true => rfl
  | false => rfl

theorem even_first : ∀ x y : Bool, flipIf x (flipIf y (flipIf x y)) = false
  | true, true => rfl
  | true, false => rfl
  | false, true => rfl
  | false, false => rfl

theorem even_third : ∀ x z : Bool, flipIf x (flipIf (flipIf z x) z) = false
  | true, true => rfl
  | true, false => rfl
  | false, true => rfl
  | false, false => rfl

/-- Every reading is allowed by every pair: any two values extend to an even three. -/
theorem evenBoxes_glued (v : Specker.Box → Bool) : Glued (restrict Specker.within evenBoxes) v
  | .ab => ⟨fun x => match x with
      | .a => v .a
      | .b => v .b
      | .c => flipIf (v .a) (v .b),
      even_first (v .a) (v .b),
      fun _ w => match w with
        | .inl e => by subst e; rfl
        | .inr e => by subst e; rfl⟩
  | .bc => ⟨fun x => match x with
      | .a => flipIf (v .b) (v .c)
      | .b => v .b
      | .c => v .c,
      flipIf_self (flipIf (v .b) (v .c)),
      fun _ w => match w with
        | .inl e => by subst e; rfl
        | .inr e => by subst e; rfl⟩
  | .ca => ⟨fun x => match x with
      | .a => v .a
      | .b => flipIf (v .c) (v .a)
      | .c => v .c,
      even_third (v .a) (v .c),
      fun _ w => match w with
        | .inl e => by subst e; rfl
        | .inr e => by subst e; rfl⟩

/-- **Parity is a whole its pairs do not give back**: on the same three boxes and pairs where
Specker's possibilities are the parts of no whole (`Specker.no_whole`). -/
theorem evenBoxes_not_determined : ¬ PartsDetermine Specker.within evenBoxes :=
  fun det => absurd (det (fun x => match x with
      | .a => true
      | .b => false
      | .c => false) (evenBoxes_glued _)) (fun h => nomatch h)

/-- What a law makes of a whole: the configurations it leads to from the whole. -/
def imageOf (next : A × B → A × B) (whole : A × B → Prop) (p : A × B) : Prop :=
  ∃ q, whole q ∧ next q = p

/-- A law that moves each part by itself keeps a rectangular whole rectangular. -/
theorem Rectangular.image_of_separate {whole : A × B → Prop} (rect : Rectangular whole)
    (f : A → A) (g : B → B) : Rectangular (imageOf (fun p => (f p.1, g p.2)) whole) := by
  intro a a' b b' ⟨⟨x, y⟩, hxy, exy⟩ ⟨⟨x', y'⟩, hxy', exy'⟩
  have e1 : f x = a := congrArg Prod.fst exy
  have e2 : g y' = b' := congrArg Prod.snd exy'
  subst e1
  subst e2
  exact ⟨(x, y'), rect x x' y y' hxy hxy', rfl⟩

/-- **Relation forms by coupling.** Copying one part into the other turns the full whole into
the parts going alike, which is not rectangular. -/
theorem copy_relates :
    Rectangular (fun _ : Bool × Bool => True) ∧
      (∀ p, imageOf (fun p : Bool × Bool => (p.1, p.1)) (fun _ => True) p ↔ p.1 = p.2) ∧
      ¬ Rectangular (imageOf (fun p : Bool × Bool => (p.1, p.1)) (fun _ => True)) :=
  have image : ∀ p, imageOf (fun p : Bool × Bool => (p.1, p.1)) (fun _ => True) p ↔ p.1 = p.2 :=
    fun ⟨x, y⟩ => ⟨fun ⟨q, _, e⟩ => (congrArg Prod.fst e).symm.trans (congrArg Prod.snd e),
      fun same => ⟨(x, y), trivial, by
        show (x, x) = (x, y)
        exact congrArg (fun z => (x, z)) same⟩⟩
  ⟨fun _ _ _ _ _ _ => trivial, image,
   fun rect =>
    absurd ((image (true, false)).mp
      (rect true false true false ((image (true, true)).mpr rfl) ((image (false, false)).mpr rfl)))
      (fun h => nomatch h)⟩

/-- A law that moves each part by itself and loses nothing of what occurs leads to a rectangular
whole only from a rectangular one: `f` merges no two first parts that occur, and `g` no two
second parts. -/
theorem Rectangular.of_image_injective {whole : A × B → Prop} {f : A → A} {g : B → B}
    (inj_f : ∀ a a' b b', whole (a, b) → whole (a', b') → f a = f a' → a = a')
    (inj_g : ∀ a a' b b', whole (a, b) → whole (a', b') → g b = g b' → b = b')
    (rect : Rectangular (imageOf (fun p => (f p.1, g p.2)) whole)) : Rectangular whole := by
  intro a a' b b' hab ha'b'
  match rect (f a) (f a') (g b) (g b') ⟨(a, b), hab, rfl⟩ ⟨(a', b'), ha'b', rfl⟩ with
  | ⟨⟨x, y⟩, hxy, e⟩ =>
    have ex : x = a := inj_f x a y b hxy hab (congrArg Prod.fst e)
    have ey : y = b' := inj_g x a' y b' hxy ha'b' (congrArg Prod.snd e)
    subst ex
    subst ey
    exact hxy

/-- **A relation persists under laws that move each part by itself and lose nothing of what
occurs.** -/
theorem relation_persists {whole : A × B → Prop} {f : A → A} {g : B → B}
    (inj_f : ∀ a a' b b', whole (a, b) → whole (a', b') → f a = f a' → a = a')
    (inj_g : ∀ a a' b b', whole (a, b) → whole (a', b') → g b = g b' → b = b')
    (related : ¬ Rectangular whole) : ¬ Rectangular (imageOf (fun p => (f p.1, g p.2)) whole) :=
  fun rect => related (Rectangular.of_image_injective inj_f inj_g rect)

/-- **Forgetting a part unrelates it**: a law that sends one part to one value, however it moves
the other, leads to a rectangular whole. -/
theorem forgetting_unrelates (whole : A × B → Prop) (a₀ : A) (g : B → B) :
    Rectangular (imageOf (fun p => (a₀, g p.2)) whole) := by
  intro a a' b b' ⟨_, _, e⟩ ⟨q', hq', e'⟩
  have ea : a₀ = a := congrArg Prod.fst e
  have eb : g q'.2 = b' := congrArg Prod.snd e'
  subst ea
  subst eb
  exact ⟨q', hq', rfl⟩

/-- `couple p` turns the second part over where the first holds. -/
def couple (p : Bool × Bool) : Bool × Bool := (p.1, flipIf p.1 p.2)

theorem couple_couple : ∀ p, couple (couple p) = p
  | (true, true) => rfl
  | (true, false) => rfl
  | (false, true) => rfl
  | (false, false) => rfl

/-- **A coupling that relates two parts can unrelate them when it acts again**, losing nothing
either way: from the second part settled, `couple` leads to the parts going alike, and from there
back to the second part settled. `couple` loses nothing; what ends the relation is that it acts
on the parts together. -/
theorem coupling_relates_and_unrelates :
    Rectangular (fun p : Bool × Bool => p.2 = false) ∧
      ¬ Rectangular (imageOf couple (fun p : Bool × Bool => p.2 = false)) ∧
      (∀ p, imageOf couple (imageOf couple (fun p : Bool × Bool => p.2 = false)) p ↔ p.2 = false) :=
  have settled : Rectangular (fun p : Bool × Bool => p.2 = false) := fun _ _ _ _ _ h => h
  have related : ¬ Rectangular (imageOf couple (fun p : Bool × Bool => p.2 = false)) :=
    fun rect =>
      match rect false true false true ⟨(false, false), rfl, rfl⟩ ⟨(true, false), rfl, rfl⟩ with
      | ⟨⟨x, y⟩, hy, e⟩ => by
        have h1 := congrArg Prod.fst e
        have h2 := congrArg Prod.snd e
        cases x <;> cases y
        · exact nomatch (h2 : false = true)
        · exact nomatch (hy : true = false)
        · exact nomatch (h1 : true = false)
        · exact nomatch (hy : true = false)
  have back : ∀ p, imageOf couple (imageOf couple (fun p : Bool × Bool => p.2 = false)) p ↔
      p.2 = false := fun p =>
    ⟨fun ⟨_, ⟨r, hr, e1⟩, e2⟩ => by
       subst e1
       have same : r = p := (couple_couple r).symm.trans e2
       subst same
       exact hr,
     fun h => ⟨couple p, ⟨p, h, rfl⟩, couple_couple p⟩⟩
  ⟨settled, related, back⟩

end Separation

/-! ## The split that makes sense, under a determined law -/

namespace Law

variable {S : Type u} {R : Type v} {K : Type w}

/-- Under a determined law, going alike is carrying what is lumped into what is lumped. This is
`Becoming.Learning`'s `goAlike_iff_lumped`, written independently with the same proof, and is
stated here as its instance. -/
theorem goAlike_process_iff {next : S → S} {π : S → K} :
    GoAlike (process next) π ↔ ∀ s s', π s = π s' → π (next s) = π (next s') :=
  Learning.goAlike_iff_lumped

/-- A split that keeps what is registered and carries a law relates configurations by a
bisimulation of the registered law. -/
theorem kernel_bisimulation {next : S → S} {o : S → R} {π : S → K}
    (keeps : ∀ s s', π s = π s' → o s = o s') (alike : GoAlike (process next) π) :
    Bisimulation (registered next o) (registered next o) (fun s s' => π s = π s') :=
  fun s s' same =>
    have ahead : π (next s) = π (next s') := goAlike_process_iff.mp alike s s' same
    ⟨fun _ => ⟨fun h => (keeps s s' same).symm.trans h, fun h => (keeps s s' same).trans h⟩,
     fun _ _ to => ⟨next s', rfl, by cases to; exact ahead⟩,
     fun _ _ to => ⟨next s, rfl, by cases to; exact ahead⟩⟩

/-- Such a split loses nothing registered. -/
theorem sameFuture_of_law {next : S → S} {o : S → R} {π : S → K}
    (keeps : ∀ s s', π s = π s' → o s = o s') (alike : GoAlike (process next) π) {s s' : S}
    (same : π s = π s') : SameFuture next o s s' :=
  alike_iff_sameFuture.mp ⟨_, kernel_bisimulation keeps alike, same⟩

/-- **The coarsest split that keeps what is registered and carries a law makes sense.** -/
theorem makesSense_of_law {next : S → S} {o : S → R} {π : S → K}
    (keeps : ∀ s s', π s = π s' → o s = o s') (alike : GoAlike (process next) π)
    (coarsest : ∀ s s', SameFuture next o s s' → π s = π s') : MakesSense (registered next o) π :=
  makesSense_iff.mpr ⟨kernel_bisimulation keeps alike,
    fun s s' same => coarsest s s' (alike_iff_sameFuture.mp same)⟩

/-- The split that lumps everything always carries a law (`goAlike_const`), and makes sense only
where nothing registered ever differs. -/
theorem const_makesSense_iff {next : S → S} {o : S → R} (k : K) :
    MakesSense (registered next o) (fun _ => k) ↔ ∀ s s', SameFuture next o s s' :=
  ⟨fun sense s s' => alike_iff_sameFuture.mp ((sense s s').mp rfl),
   fun all s s' => ⟨fun _ => alike_iff_sameFuture.mpr (all s s'), fun _ => rfl⟩⟩

/-- **What is registered now makes sense by itself exactly where it fixes its own registered
future.** -/
theorem now_makesSense_iff {next : S → S} {o : S → R} :
    MakesSense (registered next o) o ↔ ∀ s s', o s = o s' → SameFuture next o s s' :=
  ⟨fun sense s s' e => alike_iff_sameFuture.mp ((sense s s').mp e),
   fun fixes s s' => ⟨fun e => alike_iff_sameFuture.mpr (fixes s s' e),
     fun same => (alike_iff_sameFuture.mp same) 0⟩⟩

/-- **Registering everything, the configuration itself is the split that makes sense**: nothing
alike is two. -/
theorem whole_makesSense (next : S → S) : MakesSense (registered next id) id :=
  makesSense_id_iff.mpr fun _ _ alike => alike_iff_sameFuture.mp alike 0

/-- **The registered part alone makes sense exactly where the rest never makes a registered
difference**; elsewhere the split that makes sense includes the rest. -/
theorem part_makesSense_iff {X : Type u} {C : Type v} {next : X × C → X × C} :
    MakesSense (registered next Prod.fst) Prod.fst ↔
      ∀ x c c', SameFuture next Prod.fst (x, c) (x, c') :=
  now_makesSense_iff.trans
    ⟨fun fixes x c c' => fixes (x, c) (x, c') rfl,
     fun rest s s' e => by
       cases s with
       | mk x c =>
         cases s' with
         | mk x' c' =>
           have e : x = x' := e
           subst e
           exact rest x c c'⟩

/-- Where what is registered carries a law, it fixes its own registered future. -/
theorem sameFuture_of_goAlike {next : S → S} {o : S → R} (alike : GoAlike (process next) o) :
    ∀ s s', o s = o s' → SameFuture next o s s' := by
  intro s s' e n
  induction n with
  | zero => exact e
  | succ n ih => exact goAlike_process_iff.mp alike _ _ ih

/-- **What is registered now makes sense by itself exactly where it carries a law**: a condition on
one step. -/
theorem now_makesSense_iff_goAlike {next : S → S} {o : S → R} :
    MakesSense (registered next o) o ↔ GoAlike (process next) o :=
  now_makesSense_iff.trans
    ⟨fun fixes => goAlike_process_iff.mpr fun s s' e => fixes s s' e 1, sameFuture_of_goAlike⟩

/-- **The registered part alone makes sense exactly where the rest makes no difference to its next
value.** -/
theorem part_makesSense_iff_step {X : Type u} {C : Type v} {next : X × C → X × C} :
    MakesSense (registered next Prod.fst) Prod.fst ↔ ∀ x c c', (next (x, c)).1 = (next (x, c')).1 := by
  refine now_makesSense_iff_goAlike.trans ⟨fun alike x c c' => goAlike_process_iff.mp alike _ _ rfl, ?_⟩
  intro every
  apply goAlike_process_iff.mpr
  intro s s' e
  cases s with
  | mk x c =>
    cases s' with
    | mk x' c' =>
      have e : x = x' := e
      subst e
      exact every x c c'

/-- A part whose next value is set by a rule that changes with it: the part alone makes sense
exactly where the rule makes no difference to it, the condition of `adaptive_state_law_iff`. -/
theorem adaptive_makesSense_iff {X : Type u} {C : Type v} (F : C → X → X) (G : C → X → C) :
    MakesSense (registered (fun s : X × C => (F s.2 s.1, G s.2 s.1)) Prod.fst) Prod.fst ↔
      ∀ x c c', F c x = F c' x :=
  part_makesSense_iff_step

end Law

/-! ## The pair: a standing that changes by a passing, as a position by a velocity -/

namespace Motion

theorem cancel : ∀ k {a b : Nat}, a + k = b + k → a = b
  | 0, _, _, h => h
  | k + 1, _, _, h => cancel k (Nat.succ.inj h)

/-- A standing that changes by a passing: a state going on under a rule that holds. -/
def move : Nat × Nat → Nat × Nat := fun s => (s.1 + s.2, s.2)

/-- The same law read as `Becoming.Mechanism`'s adaptive process, the passing as the rule. -/
theorem move_adaptive :
    Law.process move = adaptive (fun g x (_ : Unit) => x + g) (fun g (_ : Nat) => g) :=
  rfl

/-- **Registering only the standing, the split that makes sense is the pair.** -/
theorem makes_sense : MakesSense (Law.registered move Prod.fst) (fun s : Nat × Nat => s) :=
  fun ⟨x, v⟩ ⟨x', v'⟩ =>
    ⟨fun e => match e with | rfl => Alike.refl _ (x, v),
     fun alike =>
      have h := Law.alike_iff_sameFuture.mp alike
      have hx : x = x' := h 0
      have h1 : x + v = x' + v' := h 1
      match hx with
      | rfl => match cancel x ((Nat.add_comm v x).trans (h1.trans (Nat.add_comm x v'))) with
        | rfl => rfl⟩

/-- The standing alone carries no law: the passing makes a difference to it. -/
theorem standing_alone : ¬ GoAlike (Law.process move) Prod.fst :=
  fun alike => absurd ((adaptive_state_law_iff.mp (move_adaptive ▸ alike)) 0 1 0 ()) (by decide)

/-- The passing alone loses the standing. -/
theorem passing_alone : ¬ Law.SameFuture move Prod.fst (0, 0) (1, 0) :=
  fun h => absurd (h 0) (by decide)

/-- Neither alone makes sense. -/
theorem neither_alone :
    ¬ MakesSense (Law.registered move Prod.fst) Prod.fst ∧
      ¬ MakesSense (Law.registered move Prod.fst) Prod.snd :=
  ⟨fun sense => standing_alone (carries_law_iff.mp (Law.MakesSense.carries sense)),
   fun sense => passing_alone (Law.alike_iff_sameFuture.mp ((sense (0, 0) (1, 0)).mp rfl))⟩

/-- Nothing passes. -/
def still : Nat × Nat → Nat × Nat := fun s => s

theorem orbit_still : ∀ (s : Nat × Nat) n, Law.orbit still s n = s
  | _, 0 => rfl
  | s, n + 1 => orbit_still s n

/-- **Where nothing passes, the standing alone makes sense**: the pair is one. -/
theorem still_makes_sense : MakesSense (Law.registered still Prod.fst) Prod.fst :=
  Law.now_makesSense_iff.mpr fun s s' h n =>
    (congrArg Prod.fst (orbit_still s n)).trans (h.trans (congrArg Prod.fst (orbit_still s' n)).symm)

end Motion

/-! ## States from one registered history -/

section Moments

variable {O : Type v}

/-- Two moments of one registered unfolding are one state when everything registered after them
is alike. -/
def SameAhead (o : Nat → O) (t t' : Nat) : Prop := ∀ n, o (t + n) = o (t' + n)

theorem SameAhead.refl (o : Nat → O) (t : Nat) : SameAhead o t t := fun _ => rfl

theorem SameAhead.symm {o : Nat → O} {t t' : Nat} (h : SameAhead o t t') : SameAhead o t' t :=
  fun n => (h n).symm

theorem SameAhead.trans {o : Nat → O} {t t' t'' : Nat} (h : SameAhead o t t')
    (h' : SameAhead o t' t'') : SameAhead o t t'' :=
  fun n => (h n).trans (h' n)

/-- The states read off the history go on as themselves: their law is read off too. -/
theorem SameAhead.next {o : Nat → O} {t t' : Nat} (h : SameAhead o t t') :
    SameAhead o (t + 1) (t' + 1) :=
  fun n => (congrArg o (Nat.succ_add t n)).trans
    ((h (n + 1)).trans (congrArg o (Nat.succ_add t' n)).symm)

/-- Read along an orbit, one state is the same registered future. -/
theorem sameAhead_orbit_iff {S : Type u} {next : S → S} {o : S → O} {s : S} {t t' : Nat} :
    SameAhead (fun n => o (Law.orbit next s n)) t t' ↔
      Law.SameFuture next o (Law.orbit next s t) (Law.orbit next s t') :=
  ⟨fun h n => (congrArg o (Law.orbit_add next s t n)).symm.trans
      ((h n).trans (congrArg o (Law.orbit_add next s t' n))),
   fun h n => (congrArg o (Law.orbit_add next s t n)).trans
      ((h n).trans (congrArg o (Law.orbit_add next s t' n)).symm)⟩

/-- Where every moment is registered differently, each moment is its own state. -/
theorem SameAhead.new_each {o : Nat → O} (new : ∀ t t', o t = o t' → t = t') {t t' : Nat}
    (h : SameAhead o t t') : t = t' :=
  new t t' (h 0)

/-- **Every registered history is a determined law read through a registration**: the law of
moments, each going on to the next, which is the succession of the step index and nothing more.
Its alike moments are the moments that are one state. -/
theorem alike_moments_iff {o : Nat → O} {t t' : Nat} :
    Alike (Law.registered Nat.succ o) (Law.registered Nat.succ o) t t' ↔ SameAhead o t t' :=
  Law.alike_iff_sameFuture.trans
    ⟨fun h n => (congrArg o (Law.succ_orbit t n)).symm.trans
        ((h n).trans (congrArg o (Law.succ_orbit t' n))),
     fun h n => (congrArg o (Law.succ_orbit t n)).trans
        ((h n).trans (congrArg o (Law.succ_orbit t' n)).symm)⟩

/-- Sorting the first `K + 1` moments by a relation to values up to `L`: two are related to `L`,
or all to values below `L`, or exactly one to `L` and the rest below. Nothing is decided about
the relation. -/
theorem split_top {P : Nat → Nat → Prop} {L : Nat} :
    ∀ K, (∀ n, n ≤ K → P n L ∨ ∃ i, i < L ∧ P n i) →
      (∃ t t', t < t' ∧ t' ≤ K ∧ P t L ∧ P t' L) ∨ (∀ n, n ≤ K → ∃ i, i < L ∧ P n i) ∨
        (∃ m, m ≤ K ∧ P m L ∧ ∀ n, n ≤ K → n ≠ m → ∃ i, i < L ∧ P n i)
  | 0, held =>
    match held 0 (Nat.le_refl 0) with
    | .inl top => Or.inr (Or.inr ⟨0, Nat.le_refl 0, top,
        fun n le other => absurd (Nat.le_antisymm le (Nat.zero_le n)) other⟩)
    | .inr below => Or.inr (Or.inl fun n le => by
        have same : n = 0 := Nat.le_antisymm le (Nat.zero_le n)
        subst same
        exact below)
  | K + 1, held =>
    match split_top K (fun n le => held n (Nat.le_succ_of_le le)) with
    | .inl ⟨t, t', lt, le, h, h'⟩ => Or.inl ⟨t, t', lt, Nat.le_succ_of_le le, h, h'⟩
    | .inr (.inl all) =>
      match held (K + 1) (Nat.le_refl _) with
      | .inl top => Or.inr (Or.inr ⟨K + 1, Nat.le_refl _, top, fun n le other =>
          match le_succ_cases le with
          | .inl le => all n le
          | .inr same => absurd same other⟩)
      | .inr below => Or.inr (Or.inl fun n le =>
          match le_succ_cases le with
          | .inl le => all n le
          | .inr same => by subst same; exact below)
    | .inr (.inr ⟨m, le_m, top_m, rest⟩) =>
      match held (K + 1) (Nat.le_refl _) with
      | .inl top => Or.inl ⟨m, K + 1, Nat.lt_succ_of_le le_m, Nat.le_refl _, top_m, top⟩
      | .inr below => Or.inr (Or.inr ⟨m, Nat.le_succ_of_le le_m, top_m, fun n le other =>
          match le_succ_cases le with
          | .inl le => rest n le other
          | .inr same => by subst same; exact below⟩)

/-- **Pigeonhole up to a relation, with no decision.** If each of the first `L + 1` moments is
related to some value below `L`, two of them are related to one value. `Becoming.Recurrence`'s
`revisits_within` is the form with a list and equality. -/
theorem shared_below : ∀ (L : Nat) (P : Nat → Nat → Prop), (∀ n, n ≤ L → ∃ i, i < L ∧ P n i) →
    ∃ t t' i, t < t' ∧ t' ≤ L ∧ P t i ∧ P t' i
  | 0, _, held => match held 0 (Nat.le_refl 0) with
    | ⟨_, lt, _⟩ => absurd lt (Nat.not_lt_zero _)
  | L + 1, P, held =>
    match split_top (L := L) (L + 1) (fun n le => match held n le with
        | ⟨i, lt, h⟩ => match Nat.lt_or_eq_of_le (Nat.le_of_lt_succ lt) with
          | .inl lt' => .inr ⟨i, lt', h⟩
          | .inr e => .inl (by subst e; exact h)) with
    | .inl ⟨t, t', lt, le, h, h'⟩ => ⟨t, t', L, lt, le, h, h'⟩
    | .inr (.inl all) =>
      match shared_below L P (fun n le => all n (Nat.le_succ_of_le le)) with
      | ⟨t, t', i, lt, le, h, h'⟩ => ⟨t, t', i, lt, Nat.le_succ_of_le le, h, h'⟩
    | .inr (.inr ⟨m, _, _, rest⟩) =>
      match shared_below L (fun n i => P (skipAt m n) i) (fun n le =>
          rest (skipAt m n) (Nat.le_trans (skipAt_le m n) (Nat.succ_le_succ le)) (skipAt_ne m n)) with
      | ⟨t, t', i, lt, le, h, h'⟩ => ⟨skipAt m t, skipAt m t', i, skipAt_lt m lt,
          Nat.le_trans (skipAt_le m t') (Nat.succ_le_succ le), h, h'⟩

/-- Every moment is one of the states of the moments before `L`. -/
def StatesBelow (o : Nat → O) (L : Nat) : Prop := ∀ t, ∃ i, i < L ∧ SameAhead o t i

/-- **Where two moments are one state, every moment is one of the states before the later.** -/
theorem statesBelow_of_same {o : Nat → O} {i j : Nat} (lt : i < j) (same : SameAhead o i j) :
    StatesBelow o j := by
  intro t
  induction t with
  | zero => exact ⟨0, Nat.lt_of_le_of_lt (Nat.zero_le i) lt, SameAhead.refl o 0⟩
  | succ t ih =>
    match ih with
    | ⟨k, lt_k, h⟩ =>
      match Nat.lt_or_eq_of_le (Nat.succ_le_of_lt lt_k) with
      | .inl lt' => exact ⟨k + 1, lt', h.next⟩
      | .inr e =>
        have back : SameAhead o (k + 1) i := by
          subst e
          exact same.symm
        exact ⟨i, lt, h.next.trans back⟩

/-- **A registered history has finitely many states exactly where two of its moments are one
state**, that is, where its registration repeats from some moment on. -/
theorem finitely_many_states_iff {o : Nat → O} :
    (∃ L, StatesBelow o L) ↔ ∃ i j, i < j ∧ SameAhead o i j :=
  ⟨fun ⟨L, below⟩ => match shared_below L (fun t i => SameAhead o t i) (fun n _ => below n) with
    | ⟨t, t', _, lt, _, h, h'⟩ => ⟨t, t', lt, h.trans h'.symm⟩,
   fun ⟨_, _, lt, same⟩ => ⟨_, statesBelow_of_same lt same⟩⟩

/-- **A configuration that returns has finitely many states under every registration.** -/
theorem Law.Returns.states {S : Type u} {next : S → S} {s : S} (returns : Law.Returns next s)
    (o : S → O) : ∃ i j, i < j ∧ SameAhead (fun n => o (Law.orbit next s n)) i j :=
  match returns with
  | ⟨p, pos, back⟩ => ⟨0, p, pos, fun n =>
      (congrArg (fun m => o (Law.orbit next s m)) (Nat.zero_add n)).trans
        (congrArg o ((congrArg (fun x => Law.orbit next x n) back).symm.trans
          (Law.orbit_add next s p n).symm))⟩

end Moments

namespace Denial

/-- The two-valued denial, registered at each moment. -/
def register (n : Nat) : Bool := Law.orbit (fun b : Bool => !b) true n

theorem zero_two : SameAhead register 0 2 :=
  fun n => (congrArg (Law.orbit (fun b : Bool => !b) true) (Nat.zero_add n)).trans
    (Law.orbit_add (fun b : Bool => !b) true 2 n).symm

/-- **Exactly two states**: the first two moments differ, the third is the first again, and every
moment is one of the two. -/
theorem two_states :
    (¬ SameAhead register 0 1) ∧ SameAhead register 0 2 ∧
      ∀ t, SameAhead register t 0 ∨ SameAhead register t 1 :=
  ⟨fun h => Diagonal.revision_never_rests Diagonal.flip_moves true 0 (h 0).symm, zero_two,
   fun t => match statesBelow_of_same (Nat.zero_lt_succ 1) zero_two t with
     | ⟨0, _, h⟩ => .inl h
     | ⟨1, _, h⟩ => .inr h
     | ⟨_ + 2, lt, _⟩ => absurd (Nat.le_of_lt_succ (Nat.lt_of_succ_lt_succ lt)) (Nat.not_succ_le_zero _)⟩

/-- **Each is defined through the other**: one registers `true` and goes into the other, which
registers `false` and goes into the first. -/
theorem each_through_other (t : Nat) :
    (SameAhead register t 0 → register t = true ∧ SameAhead register (t + 1) 1) ∧
      (SameAhead register t 1 → register t = false ∧ SameAhead register (t + 1) 0) :=
  ⟨fun h => ⟨h 0, h.next⟩, fun h => ⟨h 0, h.next.trans zero_two.symm⟩⟩

end Denial

/-! ## Lassos are finitely many states -/

section Lassos

variable {O : Type u}

/-- **A lasso is two moments that are one state.** `Becoming.Learning`'s course repeating from
step `i` with period `q + 1` (`Learning.Lasso`) is moments `i` and `i + (q + 1)` being one
state. -/
theorem lasso_iff_sameAhead {o : Nat → O} {i q : Nat} :
    Learning.Lasso o i q ↔ SameAhead o i (i + (q + 1)) :=
  ⟨fun lasso n => (lasso (i + n) (Nat.le_add_right i n)).symm.trans
      (congrArg o (Nat.add_right_comm i n (q + 1))),
   fun same u later => match gap_of_le later with
    | ⟨d, at_u⟩ => by
      subst at_u
      exact (congrArg o (Nat.add_right_comm i d (q + 1))).trans (same d).symm⟩

/-- **Finitely many states is a lasso**: a registered history has finitely many states exactly
where it repeats from some step on with some period, `Becoming.Learning`'s lasso course. -/
theorem finitely_many_states_iff_lasso {o : Nat → O} :
    (∃ L, StatesBelow o L) ↔ ∃ i q, Learning.Lasso o i q :=
  finitely_many_states_iff.trans
    ⟨fun ⟨i, _, lt, same⟩ => match gap_of_lt lt with
      | ⟨q, at_j⟩ => ⟨i, q, lasso_iff_sameAhead.mpr (at_j ▸ same)⟩,
     fun ⟨i, q, lasso⟩ =>
      ⟨i, i + (q + 1), Nat.lt_succ_of_le (Nat.le_add_right i q), lasso_iff_sameAhead.mp lasso⟩⟩

end Lassos

end Becoming
