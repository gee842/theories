import Becoming.Readings
import Becoming.Gluing
import Becoming.Quantum
import Becoming.ContextArrivalTraces

/-!
# Parity readings: where the readings of one unfolding glue, for parity and for quantum states

`Becoming.Readings` reads every contextual system along a run as one world: each claim read with
its context is a relatum, active exactly where its context shows it with that value
(`Contextual.world`). `Becoming.Context` showed that a frame of context-free claims fits exactly
where what the contexts show glues at every configuration (`Contextual.fitsFree_iff`). `Becoming.Gluing`
gives the exact law for parity constraints (`ParitySystem.global_or_contradicts`), and
`Becoming.Quantum` the quantum contextual systems of the Mermin–Peres square
(`Square.no_context_free_values`). This module states those laws about the world of readings along
a run of any process and about the frames of that process, and proves them through them.

* **Gluing is the world being context-free at a step.** At a step of a run, what the contexts show
  glues exactly where the active relata of the world of readings are read off one context-free
  assignment (`Contextual.glues_iff_freeAt`): every active claim `(k, c, b)` has the value `b`
  the assignment gives `c`.
* **The parity law on the world.** For a parity system with its claims listed without repetition
  and its contexts listed, some world of readings respecting the contexts' possibilities at a
  step is context-free there exactly where no selection of contexts contradicts
  (`ParitySystem.world_free_iff`). Where a selection of `m` contexts contradicts, a world of
  readings context-free at a step meets at most `m − 1` of them within their possibilities
  there (`ParitySystem.world_met_le`); readings in context meet all `m`
  (`ParitySystem.indexed_met`, cited).
* **The parity law on frames.** For every process, some contextual system respecting the
  possibilities at a configuration is fitted by a frame of context-free claims of that process
  exactly where no selection contradicts (`ParitySystem.freeFrame_iff`).
* **Quantum readings never glue.** A contextual system of the square is quantum at a
  configuration where what each line shows on its three cells is shown jointly by a
  nonzero state vector (`Square.QuantumAt`). Quantum contextual systems exist at every configuration
  (`Square.quantum_at`); where a contextual system is quantum it does not glue
  (`Square.QuantumAt.not_glues`), so the world of readings along every run is context-free at no
  step where it is quantum (`Square.QuantumAt.not_freeAt`), and no frame of context-free claims of
  any process fits it (`Square.QuantumAt.no_free_frame`), while the indexed frame fits everything
  shown (`Contextual.indexed_fits`, cited). So along every run of every process, the
  quantum readings are one world (`Contextual.world`) that no context-free description fits
  (`Square.quantum_readings`).

What is not derived: which contextual systems of an actual unfolding are parity-constrained or quantum;
the quantum values beyond the square (Tsirelson's bound is not stated); the cycle law of
`Becoming.Gluing` on a base object, since no relation of the base is a cycle of equal-or-different
relations between claims without supplying one. Readings of this as the context carrying what no
context-free description of the unfolding can, belong to the study, not to this module. No ethical
predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

namespace Contextual

variable {S K C V A : Type} (X : Contextual S K C V)

/-- At step `t` of a run, the active relata of the world of readings are read off one
context-free assignment. -/
def FreeAt (P : Process S A) (r : Run P) (t : Nat) : Prop :=
  ∃ v : C → V, ∀ k c b, (X.world P r).web.active t (k, c, b) → v c = b

/-- **What the contexts show glues at a step of a run exactly where the world of readings is
context-free there.** -/
theorem glues_iff_freeAt (P : Process S A) (r : Run P) (t : Nat) :
    X.Glues (r.state t) ↔ X.FreeAt P r t :=
  ⟨fun ⟨v, hv⟩ => ⟨v, fun k c _ active =>
      (hv k c (X.world_active.mp active).1).symm.trans (X.world_active.mp active).2⟩,
   fun ⟨v, hv⟩ => ⟨v, fun k c w => (hv k c _ (X.world_active.mpr ⟨w, rfl⟩)).symm⟩⟩

end Contextual

namespace ParitySystem

variable {K C σ A : Type}

/-- Whether an assignment meets a context depends only on the claims within the context. -/
theorem met_congr {S : ParitySystem K C} {k : K} {u u' : C → Bool}
    (same : ∀ c, S.within k c → u c = u' c) : S.met k u = S.met k u' :=
  have values : S.value k u = S.value k u' :=
    oddOver_congr fun c _ => and_congr_of (S.counts k c) (u c) (u' c) (same c)
  congrArg (fun b => !(addParity b (S.odd k))) values

/-- **The parity law on the world of readings.** With the claims listed without repetition and
the contexts listed, some world of readings along a run, respecting the contexts' possibilities at
a step, is context-free there exactly where no selection of contexts contradicts. -/
theorem world_free_iff [DecidableEq C] (S : ParitySystem K C) (distinct : Distinct S.claims)
    {all : List K} (every : ∀ k, k ∈ all) (P : Process σ A) (r : Run P) (t : Nat) :
    (∃ X : Contextual σ K C Bool, X.within = S.within ∧ X.Respects S.support (r.state t) ∧
        X.FreeAt P r t) ↔
      ¬ ∃ ks, S.Contradicts ks :=
  ⟨fun ⟨X, same, respects, free⟩ ⟨_, contra⟩ =>
     X.not_glues (Eq.subst (motive := fun w => Local w S.support) same.symm S.local_)
       (contradicts_noGlobal contra) respects ((X.glues_iff_freeAt P r t).mpr free),
   fun none => match S.global_or_contradicts distinct all with
    | .inl ⟨v, met⟩ =>
      ⟨⟨S.within, fun _ _ => v⟩, rfl, fun k => met k (every k), ⟨v, fun _ _ _ active => active.2⟩⟩
    | .inr ⟨ks, _, contra⟩ => absurd ⟨ks, contra⟩ none⟩

/-- **A Bell-type bound on the world of readings.** Where a selection of `m` contexts contradicts,
a world of readings that is context-free at a step meets at most `m − 1` of them within their
possibilities there. -/
theorem world_met_le {S : ParitySystem K C} {ks : List K} (contra : S.Contradicts ks)
    {X : Contextual σ K C Bool} (same : X.within = S.within) {P : Process σ A} {r : Run P}
    {t : Nat} (free : X.FreeAt P r t) :
    total ks (fun k => cond (S.met k (X.shows (r.state t) k)) 1 0) + 1 ≤ ks.length :=
  match (X.glues_iff_freeAt P r t).mpr free with
  | ⟨v, hv⟩ =>
    have agree : ∀ k, S.met k (X.shows (r.state t) k) = S.met k v := fun k =>
      met_congr fun c w => hv k c (Eq.subst (motive := fun W => W k c) same.symm w)
    Eq.subst (motive := fun n => n + 1 ≤ ks.length)
      (total_congr (fun k => congrArg (fun b => cond b 1 0) (agree k)) ks).symm
      (met_le contra v)

/-- **The parity law on frames.** For every process, with the claims listed without repetition,
the contexts listed and every claim within some context, some contextual system respecting
the possibilities at a configuration is fitted by a frame of context-free claims of that process
exactly where no selection of contexts contradicts. -/
theorem freeFrame_iff [DecidableEq C] (S : ParitySystem K C) (distinct : Distinct S.claims)
    {all : List K} (every : ∀ k, k ∈ all) (home : C → K) (covers : ∀ c, S.within (home c) c)
    (P : Process σ A) (s₀ : σ) :
    (∃ X : Contextual σ K C Bool, X.within = S.within ∧ X.Respects S.support s₀ ∧
        ∃ F : Frame σ A (C × Bool), F.P = P ∧ X.FitsFree F) ↔
      ¬ ∃ ks, S.Contradicts ks :=
  ⟨fun ⟨X, same, respects, fits⟩ ⟨_, contra⟩ =>
     X.not_glues (Eq.subst (motive := fun w => Local w S.support) same.symm S.local_)
       (contradicts_noGlobal contra) respects
       ((X.fitsFree_iff P home
          (fun c => Eq.subst (motive := fun W => W (home c) c) same.symm (covers c))).mp fits s₀),
   fun none => match S.global_or_contradicts distinct all with
    | .inl ⟨v, met⟩ =>
      ⟨⟨S.within, fun _ _ => v⟩, rfl, fun k => met k (every k),
        (Contextual.fitsFree_iff ⟨S.within, fun _ _ => v⟩ P home covers).mpr
          fun _ => ⟨v, fun _ _ _ => rfl⟩⟩
    | .inr ⟨ks, _, contra⟩ => absurd ⟨ks, contra⟩ none⟩

end ParitySystem

namespace Square

variable {σ A : Type}

/-- A contextual system of the square is quantum at a configuration where what each line shows on
its three cells is shown jointly by a nonzero state vector. -/
def QuantumAt (X : Contextual σ Line Cell Bool) (s : σ) : Prop :=
  (∀ l q, X.within l (at_ l q)) ∧
    ∀ l, ∃ v : Fin 4 → Int, (¬ ∀ k, v k = 0) ∧ ∀ q, Shows v (at_ l q) (X.shows s l (at_ l q))

/-- **Quantum contextual systems do not glue.** -/
theorem QuantumAt.not_glues {X : Contextual σ Line Cell Bool} {s : σ} (quantum : QuantumAt X s) :
    ¬ X.Glues s :=
  fun ⟨f, hf⟩ => no_context_free_values ⟨f, fun l => match quantum.2 l with
    | ⟨v, nonzero, shows⟩ => ⟨v, nonzero, fun q =>
        Eq.subst (motive := fun b => Shows v (at_ l q) b) (hf l (at_ l q) (quantum.1 l q))
          (shows q)⟩⟩

/-- **Along every run, the world of readings is context-free at no step where the contextual
system is quantum.** -/
theorem QuantumAt.not_freeAt {X : Contextual σ Line Cell Bool} {P : Process σ A} {r : Run P}
    {t : Nat} (quantum : QuantumAt X (r.state t)) : ¬ X.FreeAt P r t :=
  fun free => quantum.not_glues ((X.glues_iff_freeAt P r t).mpr free)

/-- **No frame of context-free claims of any process fits a contextual system quantum at some
configuration.** -/
theorem QuantumAt.no_free_frame {X : Contextual σ Line Cell Bool} {s₀ : σ}
    (quantum : QuantumAt X s₀) (P : Process σ A) :
    ¬ ∃ F : Frame σ A (Cell × Bool), F.P = P ∧ X.FitsFree F :=
  fun fits => quantum.not_glues
    ((X.fitsFree_iff P (fun c => Line.row c.1) (fun c => quantum.1 (Line.row c.1) c.2)).mp
      fits s₀)

/-- The quantum contextual systems of the square: each line shows its own support (`inLine`). -/
def quantum : Contextual σ Line Cell Bool := ⟨within, fun _ l => inLine l⟩

/-- **Quantum contextual systems exist at every configuration.** -/
theorem quantum_at (s : σ) : QuantumAt (quantum (σ := σ)) s :=
  ⟨within_at, fun l => support_shown (inLine_support l)⟩

/-- **Along every run of every process, the quantum readings are one world that no context-free
description fits.** No frame of context-free claims of the process fits them, and the world of
readings is context-free at no step. -/
theorem quantum_readings (P : Process σ A) (s₀ : σ) :
    (¬ ∃ F : Frame σ A (Cell × Bool), F.P = P ∧ (quantum (σ := σ)).FitsFree F) ∧
      ∀ (r : Run P) t, ¬ (quantum (σ := σ)).FreeAt P r t :=
  ⟨(quantum_at s₀).no_free_frame P, fun r t => (quantum_at (r.state t)).not_freeAt⟩

end Square

end Becoming
