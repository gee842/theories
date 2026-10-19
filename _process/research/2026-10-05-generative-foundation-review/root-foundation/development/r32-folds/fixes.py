#!/usr/bin/env python3
"""R32: the hand edits after remove.py, where a use of a removed forwarder is not a renaming.

A forwarder whose explicit arguments its target takes as implicit, or that is a projection of its
target (`.mp`, `.mpr`, `.symm`), leaves uses that the rewriter renamed but whose arguments or
direction must follow the target. Each edit is exact and must apply as often as it says.
usage: python3 -B fixes.py"""
import sys
from pathlib import Path

B = Path(__file__).resolve().parents[6] / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'

EDITS = [
    # ContingentPlans: passes_iff_run, chosen_none_iff, chosen_isSome_iff took explicit arguments their targets infer
    ('ContingentPlans.lean', '(ListTests.option_any_true_iff m p s)', 'ListTests.option_any_true_iff', 2),
    ('ContingentPlans.lean', '(ListTests.find_none_iff m [] plans)', 'ListTests.find_none_iff', 1),
    ('ContingentPlans.lean', '(ListTests.find_none_iff m states plans)', 'ListTests.find_none_iff', 1),
    ('ContingentPlans.lean', '(ListTests.find_isSome_iff m states plans)', 'ListTests.find_isSome_iff', 1),
    ('Actuation.lean', '(ListTests.option_any_true_iff interface p s).trans', 'ListTests.option_any_true_iff.trans', 1),
    # projections: run_is_trace = trace_iff_run.mpr; beq_ne = beq_false_iff.mpr
    ('RuleHandoff.lean', 'nonadopting_trace_keeps_rule (RuleHandoff.trace_iff_run h) hn',
     'nonadopting_trace_keeps_rule (RuleHandoff.trace_iff_run.mpr h) hn', 1),
    ('Actuation.lean', 'rw [ListTests.beq_false_iff h, Bool.and_false]', 'rw [ListTests.beq_false_iff.mpr h, Bool.and_false]', 2),
    # liftsFromEach_of_kernel = (liftsFromEach_iff_of_kernel kernel).mpr
    ('Composition.lean', 'liftsFromEach_iff_of_kernel sense (JointAlike.matchesParts F)',
     '(liftsFromEach_iff_of_kernel sense).mpr (JointAlike.matchesParts F)', 1),
    ('Composition.lean', 'liftsFromEach_iff_of_kernel kernel (SameJointTests.matchesParts compact stable)',
     '(liftsFromEach_iff_of_kernel kernel).mpr (SameJointTests.matchesParts compact stable)', 1),
    # Registration.keeps_iff = (Learning.Training.keeps_through_iff ...).symm
    ('Contacts.lean', '''(Learning.Training.keeps_through_iff (alike := fun s => Learning.Training.AgreeOn (V := Bool) (D s))
    (s := s) (t := t) (fun _ _ _ => rfl) (fun _ _ h i m => (h i m).symm)
    (fun _ _ _ h k i m => (h i m).trans (k i m))).symm.trans (keeps_data_iff s t decided)''',
     '''(Learning.Training.keeps_through_iff (old := Learning.Training.AgreeOn (V := Bool) (D s))
    (new := Learning.Training.AgreeOn (D t)) (fun _ _ _ => rfl) (fun _ _ h i m => (h i m).symm)
    (fun _ _ _ h k i m => (h i m).trans (k i m))).trans (keeps_data_iff s t decided)''', 1),
    ('ReferencePlan.lean', '(fun _ _ _ h k j hj => (h j hj).trans (k j hj))).mp (added_keeps m i)',
     '(fun _ _ _ h k j hj => (h j hj).trans (k j hj))).mpr (added_keeps m i)', 1),
    # World.kind_balanced_iff_roles L W = (L.roles_balances (W := W)).symm
    ('CourseRoles.lean', '\n  Flow.roles_balances _ _\n', '\n  (Flow.roles_balances _).symm\n', 1),
    # withinInfluence_iff_withinReach = WithinClosure.converse.symm
    ('MutualDependence.lean', 'WithinClosure.converse.mp (dependent g f)', 'WithinClosure.converse.mpr (dependent g f)', 1),
    ('MutualDependence.lean', 'WithinClosure.converse.mpr (reach g f)', 'WithinClosure.converse.mp (reach g f)', 1),
    # verifyingClass_iff = verified_iff_interiorBy.symm
    ('Verification.lean', 'verified_iff_interiorBy.mpr (verifiable r inside)', 'verified_iff_interiorBy.mp (verifiable r inside)', 1),
    ('Verification.lean', '(verified_iff_interiorBy.mp meets).holds', '(verified_iff_interiorBy.mpr meets).holds', 1),
    # Census.over_stretch_on and DependenceCensus.over_stretch_on gave Listed.over_stretch_on its predicate
    ('Population.lean', '  Listed.over_stretch_on fun s _ _ => census s\n',
     '  Listed.over_stretch_on (p := fun (d : F × C) t => W.requires t d.1 d.2) fun s _ _ => census s\n', 1),
    ('Population.lean', '  Listed.over_stretch_on W fun s _ _ => census s\n',
     '  Listed.over_stretch_on (p := fun f t => W.active t f) fun s _ _ => census s\n', 1),
    # World.arisingRecurs_ofRoles L W = W.roles_unceasing (the flow is not read)
    ('Space.lean', '(Web.roles_unceasing _ _)', '(Web.roles_unceasing _)', 2),
    # SharedCodes.impose_reads c X i j = self_reads_iff c
    ('SharedCodes.lean', '(SharedCodes.self_reads_iff c X i j)', '(SharedCodes.self_reads_iff c)', 1),
    # Web.arising_of_ceasing census = Listed.coming_of_ceasing census (a use through dot notation)
    ('Listing.lean', '  W.arising_of_ceasing (Listed.of_listing (p := fun f t => W.active t f) lists dec) ceasing',
     '  Listed.coming_of_ceasing (Listed.of_listing (p := fun f t => W.active t f) lists dec) ceasing', 1),
    # ceasings_counts t, comings_counts t = counts_total as; ceasings_exist_iff alive t = counts_iff_decided
    ('CensusCounts.lean', 'fun t => ⟨rfl, counts_total t, counts_total t⟩', 'fun _ => ⟨rfl, counts_total _, counts_total _⟩', 1),
    ('CensusCounts.lean', '(counts_iff_decided alive t).trans', 'counts_iff_decided.trans', 1),
    # chsh_in_context r t, square_in_context r t = CHSH.indexed_met, Square.indexed_met
    ('ContextualRuns.lean', '(CHSH.indexed_met r t)', 'CHSH.indexed_met', 1),
    ('ContextualRuns.lean', '(Square.indexed_met r t)', 'Square.indexed_met', 1),
    # ExchangeLaw.world_balances_iff na present start W = course_balances_iff na W
    ('CounterfactualRuns.lean', '(ExchangeLaw.course_balances_iff na present start W)',
     '(ExchangeLaw.course_balances_iff (present := present) (start := start) na W)', 2),
]


def main():
    texts = {}
    for name, old, new, count in EDITS:
        path = B / name
        s = texts.get(path) or path.read_text()
        found = s.count(old)
        if found != count:
            sys.exit(f'{name}: {old[:70]!r} found {found} times, expected {count}')
        texts[path] = s.replace(old, new)
    for path, s in texts.items():
        path.write_text(s)
    print(len(EDITS), 'edits')


if __name__ == '__main__':
    main()
