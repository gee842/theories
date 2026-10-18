"""F3J sub-chain 2: periphery and bridge declarations -> their core counterparts (port-j.md, section 5)."""
B, G = 'Becoming.', 'Becoming.PositiveGround.'
MAP = {
 # PositiveGroundUncertainty
 'PositiveGroundUncertainty.finiteIntegral': [G+'finiteIntegral'],
 'PositiveGroundUncertainty.positive_integral_has_positive_occurrence': [G+'positive_integral_has_positive_occurrence'],
 'PositiveGroundUncertainty.contingent_generation_has_positive_ground': [G+'contingent_generation'],
 'PositiveGroundUncertainty.certified_integral_supplies_contributory_reason': [G+'certified_integral_reason'],
 'PositiveGroundUncertainty.same_response_secures_generation_without_fixed_form': [G+'same_response_without_fixed_form'],
 'PositiveGroundUncertainty.positive_occurrence_has_actual_generative_correspondence': [G+'positive_occurrence_correspondence'],
 'PositiveGroundUncertainty.positive_integral_and_adverse_full_change': [G+'positive_integral_and_adverse_full_change'],
 'PositiveGroundUncertainty.response_preserves_joint_openness_and_query_access': [G+'response_preserves_joint_openness'],
 'PositiveGroundUncertainty.acquired_evidence_secures_good_and_leaves_both_opennesses': [G+'acquired_evidence_secures_good_and_leaves_both_opennesses'],
 'PositiveGroundUncertainty.wider_scope_can_require_certificate_retraction': [G+'wider_scope_can_require_certificate_retraction'],
 # PositionedPositiveReason
 'PositionedPositiveReason.SecuresPositiveGround': [B+'SecuresPositiveGround'],
 'PositionedPositiveReason.PositionedArticulation': [B+'PositionedArticulation'],
 'PositionedPositiveReason.RouteReason': [G+'RouteReason'],
 'PositionedPositiveReason.every_situated_position_has_reason': [G+'every_situated_position_has_reason'],
 'PositionedPositiveReason.route_reason_is_least': [G+'route_reason_is_least'],
 'PositionedPositiveReason.route_reason_depends_only_on_access': [G+'route_reason_depends_only_on_access'],
 'PositionedPositiveReason.g0_holds': [G+'g0_holds'],
 'PositionedPositiveReason.barren_not_live': [G+'barren_not_live'],
 'PositionedPositiveReason.live_productive': [G+'live_productive'],
 'PositionedPositiveReason.respond_formation': [G+'respond_formation'],
 'PositionedPositiveReason.nonendorsing_position_with_access_has_reason': [G+'nonendorsing_position_with_access_has_reason'],
 'PositionedPositiveReason.endorsement_without_access_gets_no_route_reason': [G+'endorsement_without_access_gets_no_route_reason'],
 'PositionedPositiveReason.endorsement_independence_is_supplied_by_articulation': [G+'endorsement_independence_is_supplied_by_articulation'],
 # bridge and join
 'Becoming.contingent_generation_of_unrestricted': [G+'contingent_generation_of_unrestricted'],
 'Becoming.every_situated_position_has_reason_of_unrestricted': [G+'every_situated_position_has_reason_of_unrestricted'],
 'Becoming.ReachableFramesInherited.certified_reason_on_scope': [G+'certified_reason_on_scope'],
}
CANONICAL = {'PositiveGroundUncertainty.lean': 'PositiveGround.lean', 'PositionedPositiveReason.lean': 'PositiveGround.lean'}
