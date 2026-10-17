import Becoming.Likeness

/-!
# Listed-outcome frames: what fixes likeness where each move has listed outcomes

`Becoming.Likeness` states that branching tests fix likeness in frames whose moves each have
listed outcomes exactly under `EitherThroughout`, a principle of reasoning
(`alike_of_sameBranchingTests_outcomes_iff`), and that this principle is the lesser limited
principle of omniscience for decided families (`eitherThroughout_iff_llpoForDecided`), gives it
in its standard form (`LLPO.of_eitherThroughout`) and follows from `NowhereDecided`
(`EitherThroughout.of_nowhereDecided`). This module states those strengths of the frames
themselves: what it takes for configurations of a frame passing the same branching tests to be
alike.

* **Branching tests fix likeness in every listed-outcome frame exactly under the lesser limited
  principle for decided families** (`sameBranchingTests_fix_iff_llpoForDecided`), and so give
  `LLPO` in its standard form (`llpo_of_sameBranchingTests_fix`).
* **Where whether a decided family holds nowhere is decided, branching tests fix likeness** in
  every pair of frames with listed moves, listed claims and listed outcomes
  (`alike_iff_sameBranchingTests_of_nowhereDecided`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u u' v w

namespace ListedOutcomeFrames

/-- **Branching tests fix likeness in every frame with listed outcomes exactly under the lesser
limited principle of omniscience for decided families.** That configurations passing the same
branching tests are alike, for every frame with one move and no claims whose moves have listed
outcomes, holds exactly where every decided family holding at most once fails at every even place
or at every odd place. -/
theorem sameBranchingTests_fix_iff_llpoForDecided :
    (∀ (S : Type) (F G : Frame S Unit Empty) (s s' : S), OutcomesListed F → OutcomesListed G →
        SameBranchingTests F G s s' → Alike F G s s') ↔ LLPOForDecided :=
  alike_of_sameBranchingTests_outcomes_iff.trans eitherThroughout_iff_llpoForDecided

/-- **Where branching tests fix likeness in every frame with listed outcomes, `LLPO` holds** in its
standard form, for Boolean sequences with at most one `true`. -/
theorem llpo_of_sameBranchingTests_fix
    (fixes : ∀ (S : Type) (F G : Frame S Unit Empty) (s s' : S), OutcomesListed F →
      OutcomesListed G → SameBranchingTests F G s s' → Alike F G s s') : LLPO :=
  LLPO.of_eitherThroughout (alike_of_sameBranchingTests_outcomes_iff.mp fixes)

section Frames

variable {S : Type u} {S' : Type u'} {A : Type v} {C : Type w}
  {F : Frame S A C} {G : Frame S' A C}

/-- **Where whether a decided family holds nowhere is decided, branching tests fix likeness in
frames with listed outcomes.** Where the moves and claims are listed, the claims are decided and
each move of each configuration has listed outcomes, configurations are alike exactly where they
pass the same branching tests. -/
theorem alike_iff_sameBranchingTests_of_nowhereDecided (nowhere : NowhereDecided)
    (moves : ∃ l : List A, ∀ a, a ∈ l) (claims : ∃ l : List C, ∀ c, c ∈ l)
    (listed : OutcomesListed F) (listed' : OutcomesListed G) {s : S} {s' : S'} :
    Alike F G s s' ↔ SameBranchingTests F G s s' :=
  OutcomesListed.alike_iff_sameBranchingTests (EitherThroughout.of_nowhereDecided nowhere) moves
    claims listed listed'

end Frames

end ListedOutcomeFrames

end Becoming
