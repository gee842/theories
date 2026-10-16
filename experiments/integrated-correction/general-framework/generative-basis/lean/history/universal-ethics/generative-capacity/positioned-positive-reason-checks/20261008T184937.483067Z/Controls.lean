import PositionedPositiveReason
open PositionedPositiveReason GenerativeComparison

-- Any position with access, of either substrate and either endorsement value, has the reason.
example (s : Substrate) (e : Bool) :
    RouteReason access admittedAfter priorIn g0Relevant ⟨s, e, true⟩ .respond :=
  every_situated_position_has_reason access admittedAfter priorIn wholeInventory g0Relevant
    (RouteReason access admittedAfter priorIn g0Relevant) g0_holds
    (route_reason_is_least access admittedAfter priorIn g0Relevant).1
    .respond respond_formation ⟨s, e, true⟩ rfl

-- Changing only endorsement and substrate leaves the route reason unchanged.
example :
    RouteReason access admittedAfter priorIn g0Relevant ⟨.human, true, true⟩ .respond ↔
      RouteReason access admittedAfter priorIn g0Relevant ⟨.artificial, false, true⟩ .respond :=
  route_reason_depends_only_on_access access admittedAfter priorIn g0Relevant _ _
    (fun a => by cases a <;> exact Iff.rfl) .respond
