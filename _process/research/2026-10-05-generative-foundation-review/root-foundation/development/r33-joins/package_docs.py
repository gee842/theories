#!/usr/bin/env python3
"""R33: the package's index (Becoming.lean imports and notes) and the checker (CORE list and SCOPE
sentences) follow the joins: LawThroughCoupling and LawThroughChangingCoupling are in
Becoming.LawAlongRun (G4); learning through a map tracks in the limit (G5); LoopReturn's factor
and the self-loop join with Loops (G6); the tolerance law as a web's run (G7); the world an
interleaving builds (G10). Run once on the files as on main 7950e8798."""
from pathlib import Path

PKG = Path(__file__).resolve().parents[6] / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def edit(path, pairs):
    s = path.read_text()
    for old, new in pairs:
        assert s.count(old) == 1, (path.name, old[:80], s.count(old))
        s = s.replace(old, new, 1)
    path.write_text(s)
    print(path.name, len(pairs), 'edits')


def cut_note(s, name):
    head = f'* `Becoming.{name}` (L1):'
    i = s.index(head)
    j = s.index('\n* `Becoming.', i + 1)
    return s[i:j + 1]


INDEX = PKG / 'Becoming.lean'
s = INDEX.read_text()
LTC = cut_note(s, 'LawThroughCoupling')
LTCC = cut_note(s, 'LawThroughChangingCoupling')

edit(INDEX, [
    ('import Becoming.LawThroughCoupling\nimport Becoming.LawThroughChangingCoupling\n', ''),
    (LTC, ''),
    (LTCC, ''),
    ('''* `Becoming.LawAlongRun` (L1): a law through a projection along one run, and exactness. Some
  determined process on a description admits a run's steps read through it up to a step exactly
  where two of them alike under it, by the same move, reach configurations alike under it; the
  witness is the record read through the description, the least candidate, and once failed the
  criterion fails from then on. Through the identity at every step it is `Becoming.Unfolding`'s
  history law. A run can show a law the process lacks. The image is an exact finite-path
  projection (`Generative.projection_exact_iff`) exactly where configurations alike match each
  other's steps up to the description; going alike does not give it.
''', '''* `Becoming.LawAlongRun` (L1): a law along one run, under a relation, and exactness. Under an
  equivalence, some process going alike under it admits a run's steps up to a step exactly where
  any two of them alike under it, by the same move, end alike; the record read under it is the
  witness, and once failed the criterion fails from then on. Its three readings are corollaries:
  through a projection (equal images), where the witness is the least candidate and through the
  identity at every step it is `Becoming.Unfolding`'s history law; through coupling that changes
  along the run, with dependences read off the configuration; and through fixed conditions, where
  it is `Web.AlikeThrough` on the runs read through them, unchanged dependences giving one
  criterion. A run can show a law the process lacks. The image is an exact finite-path projection
  (`Generative.projection_exact_iff`) exactly where configurations alike match each other's steps
  up to the description; going alike does not give it. In `Unseen` an uncoupled level decides the
  next coupling and coupling into it restores the law; in `Changing` a dissolving dependence
  carries a law the coupling fixed at the start lacks, and a forming one breaks a law it has.
  `Becoming.LawThroughCoupling` and `Becoming.LawThroughChangingCoupling` were joined into it
  (R33), their declarations kept under their names.
'''),
    ('''  nothing; monotone return maps settle or rise; doubling links run away. With whole-number
  strengths a loop closes at the first turn, keeps the difference or runs away, nothing
  between: closing gradually needs a link that is not a multiplication.
''', '''  nothing; monotone return maps settle or rise; doubling links run away. With whole-number
  factors a loop closes at the first turn, keeps the difference or runs away, nothing between:
  closing gradually needs a link that is not a multiplication. A link's factor is what it
  multiplies by, not a coupling strength: on a condition coupled to itself with strength `M`, the
  return map multiplying by `1 + M` is `Becoming.Loops`' carried amount, turn by turn, and the
  gap against the quiet course (`selfLoop_carried`, `selfLoop_gap`); around a cycle of several
  conditions the return map multiplying by one plus the product of the coupling strengths stays
  at or below the carried amount (`carried_around_course`).
'''),
    ('''  `Becoming.FaultEnvelopes` read as a law of giving keeps a covered set giving under separated
  envelopes, and is available exactly where they are separated.
''', '''  `Becoming.FaultEnvelopes` read as a law of giving keeps a covered set giving under separated
  envelopes, and is available exactly where they are separated. On a web where each condition
  depends only on itself, needs `k` units, and is given one unit by each upstream formation
  supported the step before, support is the run of the tolerating law with tolerance the number
  upstream less `k` (`web_tolerating`), and with `k` all upstream it is `Becoming.Withholding`'s
  law without memory (`web_answers`).
'''),
    ('''  touches a relatum and every two share one. The shared index is a reading of the relations: beyond
  them it orders only exchanges sharing no relatum, which changes no configuration.
''', '''  touches a relatum and every two share one. The shared index is a reading of the relations: beyond
  them it orders only exchanges sharing no relatum, which changes no configuration. From a local
  law on whole-number standings and a list of exchanges, `LocalLaw.world` is a `World` of the
  spine whose steps balance; two interleavings of the same own courses give every relatum the same
  course of standings and the same end, and two adjacent exchanges sharing no relatum, taken in
  either order, leave the world alike at every step but the one between them.
'''),
    ('''  registration give every learner the same record, so in a world a list holds a target is
  learnable along every run exactly where runs beginning alike have targets that agree from some
  step on.
''', '''  registration give every learner the same record, so in a world a list holds a target is
  learnable along every run exactly where runs beginning alike have targets that agree from some
  step on. Learning through a map is `Becoming.LimitVerification`'s tracking in the limit: the
  extrapolation's guesses, fixed by the record, track the target (`predicts_iff_tracks`, and in a
  world a list holds `learnable_iff_tracks`); where the target is invariant along the law this is
  identification in the limit (`learnable_iff_identifies`), and without that premise it is not
  (`Merge.learnable_not_identifies`).
'''),
    ('''  by none. Identification in the limit verifies and refutes each hypothesis in the limit. From not
''', '''  by none. Identification in the limit, tracking a constant target, verifies and refutes each
  hypothesis in the limit. From not
'''),
    ('''  record, so where their targets differ a claim is right on at most one, and a learner resting
  on both has targets that agree from some step on. In a world a list holds, some learner rests
  on a target at every configuration exactly where configurations with the same registered
''', '''  record, so where their targets differ a claim is right on at most one, and a learner
  predicting both has targets that agree from some step on. In a world a list holds, some learner
  predicts a target at every configuration exactly where configurations with the same registered
'''),
    ('''  (`signal_no_exact`, `paired_exact`); on runs, an extrapolation rests on the feature from a step
''', '''  (`signal_no_exact`, `paired_exact`); on runs, an extrapolation predicts the feature from a step
'''),
])

CHECK = PKG / 'check_becoming.py'
c = CHECK.read_text()
i = c.index('    "LawThroughCoupling: under an equivalence')
j = c.index('    "LawThroughChangingCoupling: ')
k = c.index('it has. "\n', j) + len('it has. "\n')
edit(CHECK, [
    ('"Becoming.Rejoining", "Becoming.LawThroughCoupling", "Becoming.LawThroughChangingCoupling", ',
     '"Becoming.Rejoining", '),
    (c[i:k], ''),
    ('''    "LawAlongRun: some determined process on a description admits a run's steps read through it "
    "before a step exactly where two of them from configurations alike under it, by the same move, "
    "reach configurations alike under it, the record read through it being the least candidate and "
    "once failed failing from then on; through the identity at every step this is the history law; "
    "a run can be consistent where the process does not go alike; the image is an exact finite-path "
    "projection exactly where configurations alike match each other's steps, which going alike does "
    "not give. "
''', '''    "LawAlongRun: under an equivalence, some process going alike under it admits a run's steps "
    "before a step exactly where two of them alike under it, by the same move, end alike, the record "
    "read under it being the witness and once failed failing from then on; through equal "
    "projections the record is the least candidate and through the identity at every step this is "
    "the history law; with dependences read off the configuration, what a formation couples into at "
    "each occasion is such an equivalence, fixed conditions being the instance that matches "
    "Web.AlikeThrough and unchanged dependences giving one criterion; a run can be consistent where "
    "the process does not go alike; the image is an exact finite-path projection exactly where "
    "configurations alike match each other's steps, which going alike does not give; in Unseen "
    "coupling into an uncoupled level restores the law, and in Changing a dissolving dependence "
    "carries a law a forming one breaks. "
'''),
    ('''    "within d turns or never fall; doubling links run away; with whole-number strengths a loop "
    "closes at the first turn, keeps the difference or runs away, nothing between. "
''', '''    "within d turns or never fall; doubling links run away; with whole-number factors a loop "
    "closes at the first turn, keeps the difference or runs away, nothing between; on a condition "
    "coupled to itself with strength M the return map multiplying by 1 + M is the carried amount of "
    "Loops and its gap, and around a cycle the return map by one plus the product of the strengths "
    "stays at or below the carried amount. "
'''),
    ('''    "is exactly no chain of n waits clear of sources; the certificate law keeps a covered set giving "
    "under separated envelopes and is available exactly where they are separated. "
''', '''    "is exactly no chain of n waits clear of sources; the certificate law keeps a covered set giving "
    "under separated envelopes and is available exactly where they are separated; on a web whose "
    "conditions each need k units and are given one by each upstream formation supported, support "
    "is the tolerating law's run with tolerance the number upstream less k, and with k all of them "
    "Withholding's law without memory. "
'''),
    ('''    "some step on. "
''', '''    "some step on; learning through a map is tracking in the limit, and where the target is "
    "invariant along the law identification in the limit, which it is not without that premise. "
'''),
    ('''    "targets decided, refuted on one with the records equal; a learner resting on both has targets "
    "agreeing from some step on, so none rests on both where they differ at arbitrarily late steps, "
    "already for two still configurations; where the target is read off the registration, the "
    "learner by refutation over the lasso hypotheses on registered values rests on it in a world a "
    "list holds within the identification bound; in a world a list holds some learner rests on the "
''', '''    "targets decided, refuted on one with the records equal; a learner predicting both has targets "
    "agreeing from some step on, so none predicts both where they differ at arbitrarily late steps, "
    "already for two still configurations; where the target is read off the registration, the "
    "learner by refutation over the lasso hypotheses on registered values predicts it in a world a "
    "list holds within the identification bound; in a world a list holds some learner predicts the "
'''),
])
