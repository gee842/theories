#!/usr/bin/env python3
"""R33: the Lean README's rows follow the joins (the two joined modules' rows go; the rows of the
modules R33 changed say what they now prove), and the Chinese rows of Learnable say "predicts"
where they said "rests". layers33.py then reorders the tables. Run once after the history move."""
import re
from pathlib import Path

PKG = Path(__file__).resolve().parents[6] / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def row(text, name):
    m = re.search(r'^\| L1 \| \[`Becoming\.' + name + r'`\]\([^)]*\) \| .* \|\n', text, re.M)
    assert m, name
    return m


EN = PKG / 'README.md'
s = EN.read_text()
for name in ['LawThroughCoupling', 'LawThroughChangingCoupling']:
    m = row(s, name)
    s = s[:m.start()] + s[m.end():]

NEW = {
    'LawAlongRun': "a law along one run, under a relation, and exactness (no premise): under an equivalence, some process going alike under it admits a run's steps up to a step exactly where they are consistent under it (`Run.law_under_iff`), the record read under it being the witness, and once failed it fails from then on (`Run.no_law_under_later`); its three readings are corollaries: through a projection (`Run.law_through_iff`, the record read through `π` the least candidate, `Run.record_least`; through the identity `Becoming.Unfolding`'s `exists_law_iff`, `Run.consistent_id_iff`), through coupling that changes along the run (`Dependence.alikeAt_equivalence`, `Run.law_through_dependence_iff`; along a run `Web.AlikeAcross`, `Dependence.alikeAt_iff_alikeAcross`) and through fixed conditions (`Conditions.alikeThrough_iff`, `Run.law_through_coupling_iff`, `Dependence.conditions_alikeAt_iff`; unchanged dependences give one criterion, `Run.consistent_unchanged_iff`); a run can show a law the process lacks (`Constant`); the image is exact in the sense of `Generative.projection_exact_iff` exactly where configurations alike match each other's steps (`image_exact_iff`, `exact_law_iff`), which going alike does not give (`Stuck`); in `Unseen` coupling into an uncoupled level restores the law, in `Changing` a dissolving dependence carries a law a forming one breaks. `Becoming.LawThroughCoupling` and `Becoming.LawThroughChangingCoupling` are joined into it (R33), their declarations kept under their names",
    'Tolerance': None,
    'Learnable': None,
    'Interleavings': None,
    'LimitVerification': None,
    'LoopReturn': None,
    'LearnableRuns': None,
    'PartialReadout': None,
}
m = row(s, 'LawAlongRun')
s = s[:m.start()] + '| L1 | [`Becoming.LawAlongRun`](Becoming/LawAlongRun.lean) | ' + NEW['LawAlongRun'] + ' |\n' + s[m.end():]

PAIRS = [
    ("`Triad` attains each contrast |",
     "`Triad` attains each contrast; on a web where each condition needs `k a` units and is given one by each supported upstream formation, support is the tolerating law's run (`web_tolerating`, `web_activity_tolerating`, `giftWeb_tolerating`), with `k` all upstream `Withholding`'s `answers` (`web_answers`) |"),
    ("a learner resting on both has targets agreeing", "a learner predicting both has targets agreeing"),
    ("so none rests on both where they differ", "so none predicts both where they differ"),
    ("some learner rests at every configuration exactly", "some learner predicts at every configuration exactly"),
    ("the own courses fix the interleaving exactly where every exchange touches a relatum and every two share one (`unique_iff`, `traced_unique_iff`). |",
     "the own courses fix the interleaving exactly where every exchange touches a relatum and every two share one (`unique_iff`, `traced_unique_iff`); the world an interleaving builds (`LocalLaw.world`, a `World` of the spine) balances at every step (`world_balances`), two interleavings of the same courses give every relatum the same course of standings and the same end (`standings_of_courses`, `standings_of_interleavings`, `world_final`), and two adjacent exchanges sharing no relatum leave it alike but at the step between them (`world_swap`, `world_swap_between`). |"),
    ("identification decides each hypothesis in the limit (`Limit.identifies_verifies`, `Limit.identifies_refutes`);",
     "tracking a target in the limit, identification being tracking a constant one (`Limit.Tracks`, `Limit.identifies_iff_tracks`), decides each hypothesis in the limit (`Limit.identifies_verifies`, `Limit.identifies_refutes`);"),
    ("whole-number strengths close at once, keep or run away, nothing between (`whole_strengths`, `nothing_between`) |",
     "whole-number factors close at once, keep or run away, nothing between (`whole_factors`, `nothing_between`); a link's factor is not a coupling strength: on a self-coupled condition of strength `M` the return map by `1 + M` is `Loops`' carried amount and its gap (`geomBound_eq_course`, `selfLoop_carried`, `selfLoop_gap`), and around a cycle the return map by one plus the product of the strengths stays at or below it (`carried_around_course`) |"),
    ("the laws of `Learnable` stated about a determined law's runs and the frame's likeness, proved through those laws |",
     "the laws of `Learnable` stated about a determined law's runs and the frame's likeness, proved through those laws; learning through a map is tracking in the limit by guesses the record fixes (`guess_fixedThrough`, `predicts_iff_tracks`, `tracks_of_learnable`, `learnable_iff_tracks`), identification in the limit where the target is invariant along the law (`learnable_iff_identifies`), and not without that premise (`Merge.learnable_not_identifies`) |"),
    ("on runs, an extrapolation rests on the feature from a step", "on runs, an extrapolation predicts the feature from a step"),
]
for old, new in PAIRS:
    assert s.count(old) == 1, old
    s = s.replace(old, new, 1)
EN.write_text(s)

ZH = PKG / 'README.zh.md'
z = ZH.read_text()
for old, new in [
    ("在两处都静止的学习者", "在两处都预测对的学习者"),
    ("没有学习者在两处都静止", "没有学习者在两处都预测对"),
    ("在辨识的界之内静止", "在辨识的界之内预测对"),
    ("某个学习者在每个配置上静止", "某个学习者在每个配置上预测对"),
    ("`Learnable` 的各律陈述在确定律的运行与框架的相似上，并经由那些律证明 |",
     "`Learnable` 的各律陈述在确定律的运行与框架的相似上，并经由那些律证明；经映射的学习是由记录所定的猜测在极限中跟随目标（`predicts_iff_tracks`、`learnable_iff_tracks`），目标沿律不变时是极限中的辨识（`learnable_iff_identifies`），无此前提则不是（`Merge.learnable_not_identifies`） |"),
]:
    assert z.count(old) == 1, old
    z = z.replace(old, new, 1)
ZH.write_text(z)
print('rows edited')
