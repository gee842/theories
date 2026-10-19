import Becoming.Granularity

/-!
# Grains: what remained of reading one unfolding at two grains

`Becoming.Granularity` reads one unfolding at a coarser grain, by blocks and by recipes. This
module states the laws of that reading the core did not yet state.

* **Renaming then reading finer returns the test.** Where every finer move is a block of its own,
  a finer test renamed into blocks and read back at the finer grain is the test itself
  (`BranchingTest.finer_rename`), as an equality of tests, not only of where they hold.
* **Either of two tests.** `BranchingTest.either` holds where neither fails; where both tests are
  decided at a configuration, it holds exactly where one of them does
  (`BranchingTest.holds_either`).
* **Histories of recipes are finer courses.** Every history of the frame of recipes is a course of
  the finer moves (`Frame.byRecipes_trace`).
* **Configurations with no step are alike** where they realize the same claims
  (`Alike.of_stuck`), so they pass the same branching tests.
* **The witness** `Midway` has six configurations (`Midway.exists_phase`).

Every declaration's axiom report is empty; the decision of the two tests is a named hypothesis
where it is used. Ported from `Generative.ExplanatoryGranularity`,
`Generative.ExplanatoryGuardedPrograms` and `Generative.ExplanatoryGranularityBoundary` (bridge
fold F3E, 18 October 2026); the port is a restatement in the core, not a new result. The
periphery's `liftTest`, `compile`, `either`, `programModel` and `terminal_questions` are
`BranchingTest.rename`, `BranchingTest.finer`, `BranchingTest.either`, `Frame.byRecipes` and
`Alike.of_stuck`.
-/

namespace Becoming

open Generative

universe u u' v w

variable {S : Type u} {S' : Type u'} {A B : Type v} {C : Type w}

/-- **A finer test renamed into blocks of single moves and read back at the finer grain is the
test itself.** -/
theorem BranchingTest.finer_rename (expand : B → List A) (name : A → B)
    (single : ∀ a, expand (name a) = [a]) :
    ∀ φ : BranchingTest A C, BranchingTest.finer expand (φ.rename name) = φ
  | .top => rfl
  | .claim _ => rfl
  | .not φ => by
    show BranchingTest.not (BranchingTest.finer expand (φ.rename name)) = .not φ
    rw [BranchingTest.finer_rename expand name single φ]
  | .both φ ψ => by
    show BranchingTest.both (BranchingTest.finer expand (φ.rename name))
      (BranchingTest.finer expand (ψ.rename name)) = .both φ ψ
    rw [BranchingTest.finer_rename expand name single φ, BranchingTest.finer_rename expand name single ψ]
  | .can a φ => by
    show BranchingTest.along (expand (name a)) (BranchingTest.finer expand (φ.rename name)) = .can a φ
    rw [single a, BranchingTest.finer_rename expand name single φ]
    rfl

/-- **Where two tests are decided at a configuration, either of them holds exactly where one of
them does.** -/
theorem BranchingTest.holds_either {F : Frame S A C} {s : S} {φ ψ : BranchingTest A C}
    (decided : Decided (BranchingTest.Holds F s φ)) (decided' : Decided (BranchingTest.Holds F s ψ)) :
    BranchingTest.Holds F s (BranchingTest.either φ ψ) ↔
      BranchingTest.Holds F s φ ∨ BranchingTest.Holds F s ψ :=
  ⟨fun neither => match decided, decided' with
    | .inl holds, _ => .inl holds
    | _, .inl holds => .inr holds
    | .inr fails, .inr fails' => False.elim (neither ⟨fails, fails'⟩),
   fun one ⟨fails, fails'⟩ => match one with
    | .inl holds => fails holds
    | .inr holds => fails' holds⟩

/-- **Every history of the frame of recipes is a course of the finer moves.** -/
theorem Frame.byRecipes_trace {F : Frame S A C} {recipe : B → Recipe A C} {s t : S}
    {word : List B} (path : Trace (F.byRecipes recipe).P s word t) : ∃ w, Trace F.P s w t := by
  induction path with
  | nil s => exact ⟨[], .nil s⟩
  | cons step _ rest =>
    match Recipe.Leads.trace step, rest with
    | ⟨w, first⟩, ⟨w', second⟩ => exact ⟨w ++ w', trace_append_iff.mpr ⟨_, first, second⟩⟩

/-- **Configurations with no step that realize the same claims are alike.** -/
theorem Alike.of_stuck {F : Frame S A C} {G : Frame S' A C} {s : S} {s' : S'}
    (claims : ∀ c, F.realized s c ↔ G.realized s' c) (stuck : ∀ a t, ¬ F.P.step s a t)
    (stuck' : ∀ a t, ¬ G.P.step s' a t) : Alike F G s s' :=
  ⟨fun x y => x = s ∧ y = s', fun x y related => by
    cases related.1
    cases related.2
    exact ⟨claims, fun a t step => absurd step (stuck a t), fun a t step => absurd step (stuck' a t)⟩,
   rfl, rfl⟩

/-- **Configurations with no step and no claims pass the same branching tests.** -/
theorem SameBranchingTests.of_stuck {F : Frame S A Empty} {G : Frame S' A Empty} {s : S} {s' : S'}
    (stuck : ∀ a t, ¬ F.P.step s a t) (stuck' : ∀ a t, ¬ G.P.step s' a t) :
    SameBranchingTests F G s s' :=
  (Alike.of_stuck (fun c => nomatch c) stuck stuck').sameBranchingTests

/-- **`Midway` has six configurations.** -/
theorem Midway.exists_phase (p : Midway.Phase → Prop) :
    (∃ s, p s) ↔ p .origin ∨ p .risky ∨ p .safe ∨ p .ready ∨ p .blocked ∨ p .done :=
  ⟨fun ⟨s, holds⟩ => match s, holds with
    | .origin, holds => .inl holds
    | .risky, holds => .inr (.inl holds)
    | .safe, holds => .inr (.inr (.inl holds))
    | .ready, holds => .inr (.inr (.inr (.inl holds)))
    | .blocked, holds => .inr (.inr (.inr (.inr (.inl holds))))
    | .done, holds => .inr (.inr (.inr (.inr (.inr holds)))),
   fun one => match one with
    | .inl holds => ⟨_, holds⟩
    | .inr (.inl holds) => ⟨_, holds⟩
    | .inr (.inr (.inl holds)) => ⟨_, holds⟩
    | .inr (.inr (.inr (.inl holds))) => ⟨_, holds⟩
    | .inr (.inr (.inr (.inr (.inl holds)))) => ⟨_, holds⟩
    | .inr (.inr (.inr (.inr (.inr holds)))) => ⟨_, holds⟩⟩

end Becoming
