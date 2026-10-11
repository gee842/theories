/-! ## Relational identity: the earlier bisimulations are the core's -/

section Likeness

variable {S : Type u} {T : Type w} {A : Type v}

/-- A process read with no claims. -/
def Frame.unclaimed (P : Process S A) : Frame S A Empty :=
  ⟨P, fun _ c => nomatch c⟩

/-- **`Deeper.Bisimulation` is the core's bisimulation of frames with no claims.** -/
theorem deeper_bisimulation_iff {P : Process S A} {Q : Process T A} {B : S → T → Prop} :
    Deeper.Bisimulation P Q B ↔ Bisimulation (Frame.unclaimed P) (Frame.unclaimed Q) B :=
  ⟨fun ⟨forth, back⟩ s t related =>
    ⟨(fun c => nomatch c), fun a s' step => forth s t a s' related step,
     fun a t' step => back s t a t' related step⟩,
   fun bisim =>
    ⟨fun s t a s' related step => (bisim s t related).2.1 a s' step,
     fun s t a t' related step => (bisim s t related).2.2 a t' step⟩⟩

/-- **The relational reading of 6 October 2026 is an instance.** In `static` and `toggle`
every configuration of one is alike to every configuration of the other. -/
theorem static_toggle_alike (s t : Bool) :
    Alike (Frame.unclaimed Deeper.static) (Frame.unclaimed Deeper.toggle) s t :=
  ⟨_, deeper_bisimulation_iff.mp Deeper.static_toggle_one_dynamics, trivial⟩

variable {O : Type v}

/-- A model of `ExplanatoryBranching` is a frame whose claims are its conditions. -/
def Frame.ofModel (m : ExplanatoryBranching.Model S A O) : Frame S A O :=
  ⟨m.process, m.condition⟩

/-- **`ExplanatoryBranching.Bisimulation` is the core's bisimulation of frames.** -/
theorem branching_bisimulation_iff {m : ExplanatoryBranching.Model S A O}
    {n : ExplanatoryBranching.Model T A O} {R : S → T → Prop} :
    ExplanatoryBranching.Bisimulation m n R ↔
      Bisimulation (Frame.ofModel m) (Frame.ofModel n) R :=
  ⟨fun ⟨⟨forth, back⟩, conditions⟩ s t related =>
    ⟨conditions s t related, fun a s' step => forth s t a s' related step,
     fun a t' step => back s t a t' related step⟩,
   fun bisim =>
    ⟨⟨fun s t a s' related step => (bisim s t related).2.1 a s' step,
      fun s t a t' related step => (bisim s t related).2.2 a t' step⟩,
     fun s t related => (bisim s t related).1⟩⟩

/-- **Alike configurations pass every branching test** of `ExplanatoryBranching`, negation and
conjunction included (`bisimulation_implies_same`). -/
theorem Alike.same {m : ExplanatoryBranching.Model S A O} {n : ExplanatoryBranching.Model T A O}
    {s : S} {t : T} (alike : Alike (Frame.ofModel m) (Frame.ofModel n) s t) :
    ExplanatoryBranching.Same m n s t :=
  match alike with
  | ⟨_, bisim, related⟩ =>
    ExplanatoryBranching.bisimulation_implies_same (branching_bisimulation_iff.mpr bisim) related

end Likeness
