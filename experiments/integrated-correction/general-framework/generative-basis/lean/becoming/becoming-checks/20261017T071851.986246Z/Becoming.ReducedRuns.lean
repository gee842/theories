import Becoming.Courses

/-!
# Reduced runs: what a reduction keeps of the courses and runs of a law

`Becoming.Readout` states, for every reduction `π : S → K`, when an observable can be decoded from
what `π` keeps (`decodes_iff_of_section`, where `π` has a section) and that a reduced law commuting
with every move commutes with every course of moves (`foldl_semiconj`). `Becoming.Courses` reads
what a reduction keeps of a run as a run of the law read through it (`Courses.reducedRun`), and
every course of configurations as a run of the process in which every change is admitted
(`Courses.anyChange`, `Courses.anyRun`). A law of change with moves is a process
(`Assurance.ofMap`). This module states those laws of runs and courses.

* **Decoding every run's reduced run.** Where the reduction has a section, one decoder reads an
  observable from the reduced run at every date of every course of configurations exactly where
  the observable goes alike across what the reduction merges (`runs_decoder_iff_of_section`).
* **The reduced law carries every course.** A course of a law of change ends where its moves take
  the start (`trace_foldl`). Where a reduced law commutes with every move, what the reduction
  keeps at the end of every course is the reduced law's fold of the course's moves from the
  reduced start (`course_reduced`), and the reduced run of every run of the law is so at every date
  (`run_reduced`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative Assurance Readout

universe u v w x

namespace ReducedRuns

variable {S : Type u} {K : Type v} {V : Type w} {A : Type x}

/-- **Decoding every run's reduced run.** Where the reduction has a section, some decoder reads the
observable from the reduced run at every date of every course of configurations exactly where the
observable goes alike across what the reduction merges. -/
theorem runs_decoder_iff_of_section {π : S → K} {f : S → V} (sec : K → S)
    (back : ∀ k, π (sec k) = k) :
    (∃ g : K → V, ∀ (r : Run (Courses.anyChange S)) (n : Nat),
        f (r.state n) = g ((Courses.reducedRun π r).state n)) ↔ Learning.Lumped π f :=
  ⟨fun ⟨g, decodes⟩ =>
    (decodes_iff_of_section sec back).mp ⟨g, fun s => decodes (Courses.anyRun fun _ => s) 0⟩,
   fun lumped => match (decodes_iff_of_section sec back).mpr lumped with
    | ⟨g, decodes⟩ => ⟨g, fun r n => decodes (r.state n)⟩⟩

/-- A course of a law of change ends where its moves, taken in turn, take the start. -/
theorem trace_foldl {f : S → A → S} :
    ∀ {s t : S} {plan : List A}, Trace (ofMap f) s plan t → t = plan.foldl f s
  | _, _, [], .nil _ => rfl
  | _, _, _ :: rest, .cons moved tail =>
    (trace_foldl tail).trans (congrArg (fun y => rest.foldl f y) moved)

/-- **The reduced law carries every course.** Where a reduced law commutes with every move, what
the reduction keeps at the end of a course of the law is the reduced law's fold of the course's
moves from what it keeps of the start. -/
theorem course_reduced (next : S → A → S) (π : S → K) (reduced : K → A → K)
    (commutes : ∀ s a, π (next s a) = reduced (π s) a) {s t : S} {plan : List A}
    (path : Trace (ofMap next) s plan t) : π t = plan.foldl reduced (π s) :=
  (congrArg π (trace_foldl path)).trans (foldl_semiconj next π reduced commutes plan s)

/-- **The reduced run of every run of the law is the reduced law's fold of its moves**, where the
reduced law commutes with every move. -/
theorem run_reduced (next : S → A → S) (π : S → K) (reduced : K → A → K)
    (commutes : ∀ s a, π (next s a) = reduced (π s) a) (r : Run (ofMap next)) (n : Nat) :
    (Courses.reducedRun π r).state n = (r.window 0 n).foldl reduced (π (r.state 0)) :=
  Eq.subst (motive := fun k => π (r.state k) = (r.window 0 n).foldl reduced (π (r.state 0)))
    (Nat.zero_add n) (course_reduced next π reduced commutes (r.window_trace n 0))

end ReducedRuns

end Becoming
