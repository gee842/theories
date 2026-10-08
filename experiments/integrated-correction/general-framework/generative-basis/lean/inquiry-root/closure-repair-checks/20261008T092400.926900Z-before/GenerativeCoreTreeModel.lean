import GenerativeNondualModel
import GenerativeReceiptModel
import CoreTreeRearticulation
import GenerativeEpisode

/-!
# Continuing the existing model under the nondual core/tree method

One actual episode jointly transforms evidence, retained response and support.
Separately, within the existing inquiry calculus, a generated branch can become
a reusable articulation without acquiring independent justificatory authority.
Both results preserve their original configurations and local premises.

These are two scoped contributions to the shared investigation, not a claim
that an embodied process executes this proof calculus, that deduction exhausts
generativity, or that an import graph proves nondual ontology. All inherited
physical and logical definitions remain unchanged.
-/

namespace Generative.Model.CoreTree

universe u v

/-- The generated theory can be reused as a basis without changing any local
derivation. The apparent root/branch position is relative to a presentation. -/
theorem generated_tree_preserves_derivations
    {World : Type u} {Index : Type v}
    (basis : Index → InquiryRoot.Formula World)
    (context : List (InquiryRoot.Formula World)) (p : InquiryRoot.Formula World) :
    InquiryRoot.Derives (InquiryRoot.CoreTree.branchBasis basis) context p ↔
      InquiryRoot.Derives basis context p :=
  InquiryRoot.CoreTree.whole_tree_rearticulation basis context p

/-- This actual common-core history already carries the joint receipt,
revision and support transformation; its aspects are not separate inputs. -/
theorem actual_episode_preserves_joint_transformation
    {p : PredictionAction.Parameters} {start finish : PredictionAction.State}
    (h : Generative.Trace (PredictionAction.process p) start
      PredictionAction.cycleEvents finish) :
    ∃ rented observed written,
      PredictionAction.Step p start .rent rented ∧
      PredictionAction.Step p rented .work observed ∧
      PredictionAction.Step p observed .write written ∧
      PredictionAction.Step p written .finish finish ∧
      GenerativeEpisode.EpisodeRelations p start observed finish :=
  GenerativeEpisode.actual_episode_has_joint_relations h

end Generative.Model.CoreTree

#print axioms Generative.Model.CoreTree.generated_tree_preserves_derivations
#print axioms Generative.Model.CoreTree.actual_episode_preserves_joint_transformation
