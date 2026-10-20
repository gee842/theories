#!/usr/bin/env python3
"""R33 (G5): the two declarations R30 left named for "rests in accord with" whose statements are
`LearnableRuns.Predicts` / `PredictsFrom` take the R30 name ("predicts"), and the prose saying an
extrapolation "rests in accord with" or "rests on" a feature says it predicts it. The family of
elimination's candidate coming to rest (Learning.lasso_of_rest, Learning.Alternate.rests,
Identification.byElimination_rests, LearningRuns.alternate_rests, held_rest_unrefuted,
merged_unrested) keeps its names: there the candidate does stop changing, which is rest in the
sense of Seeking and Enough. Run once on the files as on main 7950e8798."""
from pathlib import Path

B = Path(__file__).resolve().parents[6] / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'

EDITS = {
    'LearningRuns.lean': [
        ('''  unchanged, no extrapolation through the map to the first rests in accord with the second at
  both `(true, false)` and `(true, true)` (`pair_first_not_rests`), none rests in accord with it''',
         '''  unchanged, no extrapolation through the map to the first predicts the second at both
  `(true, false)` and `(true, true)` (`pair_first_not_predicts`), none predicts it'''),
        ('candidates rests in accord with the second from step `2` (`pair_whole_rests`).',
         'candidates predicts the second from step `2` (`pair_whole_predicts`).'),
        ('''/-- **Through the map to the first coordinate, no extrapolation rests in accord with the second
along the runs from both''', '''/-- **Through the map to the first coordinate, no extrapolation predicts the second along the
runs from both'''),
        ('theorem pair_first_not_rests (pred', 'theorem pair_first_not_predicts (pred'),
        ('''/-- **Through the map to the first coordinate, no extrapolation rests in accord with the second
along every run.**''', '''/-- **Through the map to the first coordinate, no extrapolation predicts the second along every
run.**'''),
        ('''/-- **Through the map to both, elimination over the lasso candidates rests in accord with the
second along every run from step `2`.**''', '''/-- **Through the map to both, elimination over the lasso candidates predicts the second along
every run from step `2`.**'''),
        ('theorem pair_whole_rests (r', 'theorem pair_whole_predicts (r'),
    ],
    'PartialReadout.lean': [
        ('an extrapolation rests on the feature from `T` exactly', 'an extrapolation predicts the feature from `T` exactly'),
        ('an extrapolation rests on the feature from `T` exactly', 'an extrapolation predicts the feature from `T` exactly'),
    ],
}

for name, edits in EDITS.items():
    p = B / name
    s = p.read_text()
    for old, new in edits:
        assert old in s, (name, old)
        s = s.replace(old, new, 1)
    p.write_text(s)
    print(name, 'edited')
