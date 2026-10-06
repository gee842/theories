import EvaluativeSuccession
namespace DependencyReview
-- Exhaustive nested cases avoid generated sparse-case proof helpers.
def exhaustiveRoute (m : ReasonReplay.Mask) : Option Bool :=
  match m.p with
  | false => match m.q with
    | false => none
    | true => some true
  | true => match m.q with
    | false => some false
    | true => none
#print axioms exhaustiveRoute
-- Equality comparison necessarily still names the original route.
theorem route_equal (m : ReasonReplay.Mask) : exhaustiveRoute m = RecipientAction.route m := by
  cases m with
  | mk p q => cases p <;> cases q <;> rfl
#print axioms route_equal
end DependencyReview
set_option pp.proofs true in
#print RecipientArchive.producer
#print RecipientAction.route._sparseCasesOn_1
#print RecipientAction.route._sparseCasesOn_2
