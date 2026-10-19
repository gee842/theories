import Becoming.Courses

/-!
# Retrodiction runs: reading an earlier configuration of a run from later dated records

`Becoming.Retrodiction` states, for every type of histories, when dated records read an earlier
relation right: the actual history is always a candidate, a history fits the records another
gave exactly when it gives the same records, an agreed reading is the actual one where the actual
history is in the family, and a change seen only at both ends is not located. `Becoming.Courses`
reads the histories as the runs of a process, the relation at a date as the configuration then,
and every course of configurations as a run of the process in which every change is admitted
(`Courses.anyChange`, `Courses.anyRun`). This module states those laws of runs.

* **A run fits the records another run gave exactly when it gives the same records**
  (`runs_fits_iff_same`).
* **An agreed reading of a run is the actual one.** Where the actual run is in the family and its
  source admitted, a content on which every explanation of the packet by a fitting run of the
  family agrees is the actual content (`runs_agreed_reading_actual`).
* **Controls at both ends do not locate a change.** Where two configurations differ, there are two
  runs of the process in which every change is admitted, each changing once over the span, that
  agree at both ends and differ at a date strictly between (`runs_change_unlocated`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v x y z p q

namespace RetrodictionRuns

variable {S : Type u} {A : Type v} {P : Process S A} {Q : Type x} {O : Type y}

/-- **A run fits the dated records another run gave exactly when it gives the same records.** -/
theorem runs_fits_iff_same (emit : S → Q → O) (g r : Run P) (ps : List (Nat × Q)) :
    Retrodiction.Fits (fun g : Run P => g.state) emit g
        (Retrodiction.acquire (fun g : Run P => g.state) emit r ps) ↔
      Retrodiction.acquire (fun g : Run P => g.state) emit g ps =
        Retrodiction.acquire (fun g : Run P => g.state) emit r ps :=
  Retrodiction.fits_iff_same (fun g : Run P => g.state) emit g r ps

/-- **An agreed reading of a run is the actual one.** The packet at date `d` was produced by the
actual run's configuration and the hidden source `s`. Where the actual run is in the family and
`s` admitted, a content on which every explanation of the packet by a run of the family fitting
the dated records and an admitted source agrees is the content of `s`. -/
theorem runs_agreed_reading_actual {X : Type z} {Pk : Type p} {V : Type q} (emit : S → Q → O)
    (packet : S → X → Pk) (content : X → V) (F : Run P → Prop) (Admitted : X → Prop) (d : Nat)
    (r : Run P) (s : X) (ps : List (Nat × Q)) (v : V) (inF : F r) (admitted : Admitted s)
    (agree : ∀ g t, F g → Retrodiction.Fits (fun g : Run P => g.state) emit g
        (Retrodiction.acquire (fun g : Run P => g.state) emit r ps) → Admitted t →
      packet (g.state d) t = packet (r.state d) s → content t = v) :
    content s = v :=
  Retrodiction.agreed_reading_actual (fun g : Run P => g.state) emit packet content F Admitted d r
    s ps v inF admitted agree

/-- **Controls at both ends do not locate a change.** Where `s` and `s'` differ, two runs of the
process in which every change is admitted each change once over the span from `a`, are at `s` at
`a` and at `s'` at the end, and are at `s'` and at `s` at the date `a + j + 1` strictly between. -/
theorem runs_change_unlocated [DecidableEq S] {s s' : S} (two : s ≠ s') (a j m : Nat) :
    ∃ g g' : Run (Courses.anyChange S),
      Retrodiction.changes g.state a (j + 1 + (m + 1)) = 1 ∧
      Retrodiction.changes g'.state a (j + 1 + (m + 1)) = 1 ∧
      g.state a = s ∧ g'.state a = s ∧
      g.state (a + (j + 1 + (m + 1))) = s' ∧ g'.state (a + (j + 1 + (m + 1))) = s' ∧
      g.state (a + j + 1) = s' ∧ g'.state (a + j + 1) = s :=
  match Retrodiction.change_unlocated two a j m with
  | ⟨c, c', e, e', b, b', at_g, at_g'⟩ =>
    have span : j + 1 + 1 + m = j + 1 + (m + 1) := Nat.add_right_comm (j + 1) 1 m
    ⟨Courses.anyRun (Retrodiction.stepAt s s' (a + j + 1)),
     Courses.anyRun (Retrodiction.stepAt s s' (a + (j + 1) + 1)),
     c,
     Eq.subst (motive := fun k =>
       Retrodiction.changes (Retrodiction.stepAt s s' (a + (j + 1) + 1)) a k = 1) span c',
     e, e', b,
     Eq.subst (motive := fun k => Retrodiction.stepAt s s' (a + (j + 1) + 1) (a + k) = s') span b',
     at_g, at_g'⟩

end RetrodictionRuns

end Becoming
