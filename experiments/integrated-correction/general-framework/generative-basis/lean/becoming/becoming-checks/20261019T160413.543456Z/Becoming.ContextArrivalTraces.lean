import Becoming.Context
import Becoming.Frame

/-!
# Arrival in a context along traces of the evolving law

`Becoming.Context` keeps a context beside the configuration and lets both change by one joint
relation (`evolvingLaw R`, a process on context and configuration). Which contexts support an
endpoint is derived from the common history: `Arrives R initial s word t j` holds where a trace of
`evolvingLaw R` from an initial context and `s` reaches context `j` at `t`, and one step of it is
`Advance` (`arrives_singleton`). This module states its step laws of those traces.

* **A step from a supported context arrives**: a step of the evolving law from a context in the
  support is a one-step trace arriving at its target context (`step_arrives`).
* **No support, no arrival**: from an empty support no one-step trace arrives
  (`empty_support_no_arrival`).
* **A context changes with the step**: in `ChangingContext.relation`, the one-step trace from
  context `false` at 0 arrives at 1 in the different context `true` (`changed_context_arrives`).

`BecomingCompatibility` states these of its `evolving`, `Arrives`, `Advance` and
`changingRelation`, which are the core's by definition (`Becoming.Bridge`, `…_by_core`); its
`empty_support_cannot_advance`, `actual_step_supplies_advance` and `changed_context_is_formed`
are these laws' one-step forms. This module imports nothing outside the core. No ethical
predicate, ranking or axiom occurs.

Declarations moved here unchanged, with their names, from `Becoming.Context` (board item W): see the
sections so headed.
-/

/-! ## Contexts as laws on configurations: indexed, pooled, retained, evolving and erased (moved from `Becoming.Context`) -/

namespace Becoming

open Generative

universe u v w u' u''

namespace Contextual

variable {S : Type u} {K : Type v} {C : Type w} {V : Type u'} (X : Contextual S K C V)

/-- Read with its context, everything shown is a claim: a context, a claim and a value. -/
def indexed {A : Type u''} (P : Process S A) : Frame S A (K × C × V) :=
  ⟨P, fun s q => X.within q.1 q.2.1 ∧ X.shows s q.1 q.2.1 = q.2.2⟩

/-- The indexed frame fits everything shown. -/
theorem indexed_fits {A : Type u''} (P : Process S A) (s : S) (k : K) (c : C) (b : V) :
    (X.indexed P).realized s (k, c, b) ↔ X.within k c ∧ X.shows s k c = b :=
  Iff.rfl

/-- A frame of context-free claims, a claim with a value, fits when it agrees with every context
on every claim within the context. -/
def FitsFree {A : Type u''} (F : Frame S A (C × V)) : Prop :=
  ∀ s k c b, X.within k c → (X.shows s k c = b ↔ F.realized s (c, b))

/-- **A frame of context-free claims fits exactly where what the contexts show glues at every
configuration.** -/
theorem fitsFree_iff {A : Type u''} (P : Process S A) (home : C → K)
    (covers : ∀ c, X.within (home c) c) :
    (∃ F : Frame S A (C × V), F.P = P ∧ X.FitsFree F) ↔ ∀ s, X.Glues s :=
  ⟨fun ⟨_, _, fits⟩ s =>
    ⟨fun c => X.shows s (home c) c, fun k c w =>
      ((fits s (home c) c (X.shows s k c) (covers c)).mpr
        ((fits s k c (X.shows s k c) w).mp rfl)).symm⟩,
   fun glues =>
    ⟨⟨P, fun s q => X.shows s (home q.1) q.1 = q.2⟩, rfl, fun s k c _ w =>
      match glues s with
      | ⟨_, hv⟩ =>
        have same : X.shows s k c = X.shows s (home c) c := (hv k c w).trans (hv (home c) c (covers c)).symm
        ⟨fun e => same.symm.trans e, fun e => same.trans e⟩⟩⟩

/-- So no frame of context-free claims fits a world one of whose configurations respects them,
since such a frame glues at every configuration; the indexed frame fits it (`indexed_fits`). -/
theorem no_free_frame {A : Type u''} {support : K → (C → V) → Prop} (loc : Local X.within support)
    (none : NoGlobal support) {s₀ : S} (respects : X.Respects support s₀) (P : Process S A)
    (home : C → K) (covers : ∀ c, X.within (home c) c) :
    ¬ ∃ F : Frame S A (C × V), F.P = P ∧ X.FitsFree F :=
  fun fits => X.not_glues loc none respects ((X.fitsFree_iff P home covers).mp fits s₀)

end Contextual

section Laws

variable {I : Type u} {S : Type v} {A : Type w}

/-- The pooled law of a family of laws, one for each context: a step some context's law takes,
with the context forgotten. -/
def pooledLaw (family : I → Process S A) : Process S A :=
  ⟨fun s a t => ∃ i, (family i).step s a t⟩

/-- A course some single context's law runs. -/
def InOne (family : I → Process S A) (s : S) (word : List A) (t : S) : Prop :=
  ∃ i, Trace (family i) s word t

/-- Courses of single contexts compose: a course run in one context followed by a course run in
one context is a course run in one context. -/
def JoinClosed (family : I → Process S A) : Prop :=
  ∀ s m t xs ys, InOne family s xs m → InOne family m ys t → InOne family s (xs ++ ys) t

/-- A course of one context is a course of the pooled law. -/
theorem InOne.pooled {family : I → Process S A} {s t : S} {word : List A} :
    InOne family s word t → Trace (pooledLaw family) s word t
  | ⟨i, path⟩ => trace_map (P := family i) (Q := pooledLaw family) (f := fun x => x)
      (fun _ _ _ step => ⟨i, step⟩) path

/-- Where courses of single contexts compose, every pooled course is run in one context. -/
theorem JoinClosed.inOne {family : I → Process S A} (joins : JoinClosed family) (seed : I) :
    ∀ {s t : S} {word : List A}, Trace (pooledLaw family) s word t → InOne family s word t
  | _, _, _, .nil s => ⟨seed, .nil s⟩
  | _, _, _, .cons ⟨i, step⟩ path =>
    joins _ _ _ [_] _ ⟨i, .cons step (.nil _)⟩ (JoinClosed.inOne joins seed path)

/-- **Pooling keeps exactly the courses of single contexts where they compose.** For an
inhabited family, the pooled law runs exactly the courses some single context runs, exactly
where such courses are closed under joining. -/
theorem pooledLaw_exact_iff_joinClosed {family : I → Process S A} (seed : I) :
    (∀ s word t, Trace (pooledLaw family) s word t ↔ InOne family s word t) ↔
      JoinClosed family :=
  ⟨fun exact s _ t xs ys first second =>
     (exact s (xs ++ ys) t).mp (trace_append_iff.mpr ⟨_, first.pooled, second.pooled⟩),
   fun joins _ _ _ => ⟨joins.inOne seed, InOne.pooled⟩⟩

/-- The law that retains the context: a configuration carries its context, and a step keeps the
context and takes a step of that context's law. -/
def retainedLaw (family : I → Process S A) : Process (I × S) A :=
  ⟨fun p a q => p.1 = q.1 ∧ (family p.1).step p.2 a q.2⟩

theorem retainedLaw_trace {family : I → Process S A} :
    ∀ {p q : I × S} {word : List A}, Trace (retainedLaw family) p word q →
      p.1 = q.1 ∧ Trace (family p.1) p.2 word q.2
  | _, _, _, .nil p => ⟨rfl, .nil p.2⟩
  | _, _, _, .cons ⟨same, step⟩ path =>
    match retainedLaw_trace path with
    | ⟨same', rest⟩ =>
      ⟨same.trans same', .cons step
        (Eq.subst (motive := fun i => Trace (family i) _ _ _) same.symm rest)⟩

/-- **Retaining the context runs exactly the courses of that context.** -/
theorem retainedLaw_trace_iff {family : I → Process S A} {i j : I} {s t : S} {word : List A} :
    Trace (retainedLaw family) (i, s) word (j, t) ↔ i = j ∧ Trace (family i) s word t :=
  ⟨retainedLaw_trace, fun ⟨same, path⟩ =>
    Eq.subst (motive := fun k => Trace (retainedLaw family) (i, s) word (k, t)) same
      (trace_map (P := family i) (Q := retainedLaw family) (f := fun x => (i, x))
        (fun _ _ _ step => ⟨rfl, step⟩) path)⟩

/-- **The retained law realizes exactly the courses of single contexts.** -/
theorem retainedLaw_realizes_inOne {family : I → Process S A} {s t : S} {word : List A} :
    (∃ i j, Trace (retainedLaw family) (i, s) word (j, t)) ↔ InOne family s word t :=
  ⟨fun ⟨i, _, path⟩ => ⟨i, (retainedLaw_trace_iff.mp path).2⟩,
   fun ⟨i, path⟩ => ⟨i, i, retainedLaw_trace_iff.mpr ⟨rfl, path⟩⟩⟩

/-- Contexts and configurations changing together: `R i s a j t` says that from configuration `s`
in context `i` the move `a` leads to `t` in context `j`. -/
def evolvingLaw (R : I → S → A → I → S → Prop) : Process (I × S) A :=
  ⟨fun p a q => R p.1 p.2 a q.1 q.2⟩

/-- The same law with the context forgotten. -/
def erasedLaw (R : I → S → A → I → S → Prop) : Process S A :=
  ⟨fun s a t => ∃ i j, R i s a j t⟩

/-- **Forgetting the context is exact from every context exactly where every context can follow
each forgotten step.** This is the foundation's `projection_exact_iff`, read along `Prod.snd`. -/
theorem erasedLaw_exact_iff_lifts (R : I → S → A → I → S → Prop) :
    (∀ i s a t, (∃ j k, R j s a k t) → ∃ k, R i s a k t) ↔
      ∀ i s word t, Trace (erasedLaw R) s word t ↔ ∃ j, Trace (evolvingLaw R) (i, s) word (j, t) :=
  Iff.trans
    ⟨fun lifts => ⟨fun p _ q step => ⟨p.1, q.1, step⟩,
       fun p a t ⟨_, _, step⟩ => match lifts p.1 p.2 a t ⟨_, _, step⟩ with
         | ⟨k, next⟩ => ⟨(k, t), next, rfl⟩⟩,
     fun ⟨_, lift⟩ i s a t forgotten => match lift (i, s) a t forgotten with
       | ⟨q, next, same⟩ =>
         ⟨q.1, Eq.subst (motive := fun x => R i s a q.1 x) same next⟩⟩
    (Iff.trans (projection_exact_iff (P := evolvingLaw R) (Q := erasedLaw R) (q := fun p => p.2))
      ⟨fun exact i s word t => (exact (i, s) word t).trans
          ⟨fun ⟨q, path, same⟩ =>
             ⟨q.1, Eq.subst (motive := fun x => Trace (evolvingLaw R) (i, s) word (q.1, x))
               same path⟩,
           fun ⟨j, path⟩ => ⟨(j, t), path, rfl⟩⟩,
       fun exact p word t => (exact p.1 p.2 word t).trans
          ⟨fun ⟨j, path⟩ => ⟨(j, t), path, rfl⟩,
           fun ⟨q, path, same⟩ =>
             ⟨q.1, Eq.subst (motive := fun x => Trace (evolvingLaw R) p word (q.1, x)) same path⟩⟩⟩)

/-- The contexts a course can arrive in: from a context in `initial`, the evolving law runs the
course from `s` to `t`, arriving in context `j`. -/
def Arrives (R : I → S → A → I → S → Prop) (initial : I → Prop) (s : S) (word : List A) (t : S)
    (j : I) : Prop :=
  ∃ i, initial i ∧ Trace (evolvingLaw R) (i, s) word (j, t)

/-- **Arrival along a joined course is arrival along its second part from where the first
arrives.** -/
theorem arrives_append {R : I → S → A → I → S → Prop} {initial : I → Prop} {s t : S}
    {xs ys : List A} {k : I} :
    Arrives R initial s (xs ++ ys) t k ↔ ∃ m, Arrives R (Arrives R initial s xs m) m ys t k :=
  ⟨fun ⟨i, start, path⟩ => match trace_append_iff.mp path with
    | ⟨mid, first, second⟩ => ⟨mid.2, mid.1, ⟨i, start, first⟩, second⟩,
   fun ⟨_, j, ⟨i, start, first⟩, second⟩ =>
    ⟨i, start, trace_append_iff.mpr ⟨(j, _), first, second⟩⟩⟩

theorem arrives_singleton {R : I → S → A → I → S → Prop} {possible : I → Prop} {s t : S} {a : A}
    {j : I} : Arrives R possible s [a] t j ↔ Advance R possible s a t j :=
  ⟨fun ⟨i, start, path⟩ => ⟨i, start, trace_singleton_iff.mp path⟩,
   fun ⟨i, start, step⟩ => ⟨i, start, trace_singleton_iff.mpr step⟩⟩

/-- **The contexts a course arrives in are those its last step advances to from the contexts its
earlier part arrives in.** Support is carried by the one course, not chosen afresh per step. -/
theorem arrives_snoc {R : I → S → A → I → S → Prop} {initial : I → Prop} {s t : S}
    {word : List A} {a : A} {j : I} :
    Arrives R initial s (word ++ [a]) t j ↔ ∃ m, Advance R (Arrives R initial s word m) m a t j :=
  arrives_append.trans
    ⟨fun ⟨m, arrives⟩ => ⟨m, arrives_singleton.mp arrives⟩,
     fun ⟨m, advance⟩ => ⟨m, arrives_singleton.mpr advance⟩⟩

end Laws

namespace CrossingContexts

/-- Context `false` steps from `0` to `1`; context `true` steps from `1` to `2`. -/
def family (b : Bool) : Process Nat Unit :=
  ⟨fun s _ t => (b = false ∧ s = 0 ∧ t = 1) ∨ (b = true ∧ s = 1 ∧ t = 2)⟩

theorem pooled_crosses : Trace (pooledLaw family) 0 [(), ()] 2 :=
  .cons ⟨false, Or.inl ⟨rfl, rfl, rfl⟩⟩ (.cons ⟨true, Or.inr ⟨rfl, rfl, rfl⟩⟩ (.nil 2))

/-- **No single context runs the crossing.** -/
theorem not_inOne : ¬ InOne family 0 [(), ()] 2 :=
  fun ⟨_, path⟩ => match trace_cons_iff.mp path with
    | ⟨_, first, rest⟩ => match trace_cons_iff.mp rest with
      | ⟨_, second, _⟩ => match first, second with
        | .inl ⟨_, _, one⟩, .inl ⟨_, zero, _⟩ => Nat.noConfusion (one.symm.trans zero)
        | .inl ⟨off, _, _⟩, .inr ⟨on, _, _⟩ => Bool.noConfusion (off.symm.trans on)
        | .inr ⟨_, start, _⟩, _ => Nat.noConfusion start

theorem not_joinClosed : ¬ JoinClosed family :=
  fun joins => not_inOne (((pooledLaw_exact_iff_joinClosed false).mpr joins 0 [(), ()] 2).mp
    pooled_crosses)

theorem retained_excludes : ¬ ∃ i j, Trace (retainedLaw family) (i, 0) [(), ()] (j, 2) :=
  fun crossing => not_inOne (retainedLaw_realizes_inOne.mp crossing)

end CrossingContexts

namespace ChangingContext

theorem joins : Trace (evolvingLaw relation) (false, 0) [(), ()] (true, 2) :=
  .cons (m := (true, 1)) (Or.inl ⟨rfl, rfl, rfl, rfl⟩)
    (.cons (Or.inr ⟨rfl, rfl, rfl, rfl⟩) (.nil (true, 2)))

theorem arrives : Arrives relation (fun i => i = false) 0 [(), ()] 2 true :=
  ⟨false, rfl, joins⟩

/-- **The forgotten law can take a step the given context cannot follow.** -/
theorem erased_not_lifted :
    Trace (erasedLaw relation) 0 [()] 1 ∧
      ¬ ∃ j, Trace (evolvingLaw relation) (true, 0) [()] (j, 1) :=
  ⟨trace_singleton_iff.mpr ⟨false, true, Or.inl ⟨rfl, rfl, rfl, rfl⟩⟩,
   fun ⟨_, path⟩ => match trace_singleton_iff.mp path with
     | .inl ⟨on, _, _, _⟩ => Bool.noConfusion on
     | .inr ⟨_, start, _, _⟩ => Nat.noConfusion start⟩

end ChangingContext

end Becoming


namespace Becoming

namespace ContextArrivalTraces

open Generative

universe u v w

variable {I : Type u} {S : Type v} {A : Type w}

/-- **A step of the evolving law from a supported context arrives at its target context.** -/
theorem step_arrives (R : I → S → A → I → S → Prop) {possible : I → Prop} {i j : I} {s t : S}
    {a : A} (supported : possible i) (step : (evolvingLaw R).step (i, s) a (j, t)) :
    Arrives R possible s [a] t j :=
  arrives_singleton.mpr ⟨i, supported, step⟩

/-- **From an empty support no one-step trace of the evolving law arrives.** -/
theorem empty_support_no_arrival (R : I → S → A → I → S → Prop) (s : S) (a : A) (t : S) (j : I) :
    ¬ Arrives R (fun _ => False) s [a] t j :=
  fun ⟨_, unsupported, _⟩ => unsupported

/-- **The context changes with the step**: the one-step trace of `ChangingContext.relation` from
context `false` at 0 arrives at 1 in context `true`, which differs from `false`. -/
theorem changed_context_arrives :
    Arrives ChangingContext.relation (fun i => i = false) 0 [()] 1 true ∧ (true : Bool) ≠ false :=
  ⟨step_arrives ChangingContext.relation rfl (Or.inl ⟨rfl, rfl, rfl, rfl⟩),
   fun same => Bool.noConfusion same⟩

end ContextArrivalTraces

end Becoming
