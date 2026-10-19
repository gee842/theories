#!/usr/bin/env python3
"""Join V's five modules to the core package: copy each in, import it after Becoming.Hexagrams, add its
root doc bullet after Hexagrams', its CORE entry and scope text in check_becoming.py, and its README row.
usage: python3 -B integrate.py   (V_ROOT names the checkout to edit; each edit must match exactly once)"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['V_ROOT']).resolve() if os.environ.get('V_ROOT') else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
MODS = [('v1', 'Withholding'), ('v2', 'Widening'), ('v3', 'Pace'), ('v4', 'Passing'), ('v5', 'JointKeeping')]


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


for v, m in MODS:
    shutil.copyfile(HERE / v / 'Becoming' / f'{m}.lean', PKG / 'Becoming' / f'{m}.lean')

DOC = (
    '* `Becoming.Withholding` (L3): giving that waits on giving. With memory (a formation gives\n'
    '  where it gave and all it waits on gave), a formation gives at a step exactly where every\n'
    '  formation within that many waits of it gave at the start; withholding stays, spreads\n'
    '  downstream, and one withholding ends all giving in a family reached from it. Without memory\n'
    '  (a formation gives where all it waits on gave the step before), withholding passes out where\n'
    '  no chain of waits is long enough and returns around every loop. More waiting is less giving\n'
    '  under both laws, and in a ring of three a formation giving whatever it waits on restores\n'
    '  every formation from the third step on, which no course of the law with memory does.\n'
    '* `Becoming.Widening` (L4): whether a loop closes, keeps or widens a difference, read on runs\n'
    '  of the return map. A loop closes a difference only through a link that gives back less than\n'
    '  it received; a return map below what it receives closes within as many turns as the\n'
    '  difference, exactly, and a closing loop merges; taking a constant off closes at the least\n'
    '  turn it covers the difference; a cut closes at once where what follows gives nothing for\n'
    '  nothing; monotone return maps settle or rise; doubling links run away. With whole-number\n'
    '  strengths a loop closes at the first turn, keeps the difference or runs away, nothing\n'
    '  between: closing gradually needs a link that is not a multiplication.\n'
    '* `Becoming.Pace` (L4): how fast a rule may change. A two-level course, the fast\n'
    '  configuration stepping by a rule that changes only at reading steps, is a run of one law. A\n'
    '  rule that never reads is kept from then on: nothing the fast level meets reaches it, and under it\n'
    '  what is lost stays lost and merges lose configurations; a fast difference reaches the rule\n'
    '  only at a reading step, exactly; regaining needs a change of rule. Given two values, a\n'
    '  stretch of `L` steps fixes every pair of courses with at most `N` states that held rules\n'
    '  generate exactly when `L ≥ 2N - 1`; a course of configurations read whole is fixed by its\n'
    '  first `N + 1` steps, exactly.\n'
    '* `Becoming.Passing` (L4): a pattern that outlasts each of its carriers lasts only through\n'
    '  passing. Read on a web whose activity is carrying, a pattern present at every step from `T`\n'
    '  on with carriers brief for `d` has a carrier beginning within every `d` steps; under the\n'
    '  passing premise every beginning is a passing, the pattern is passed across one of every `d`\n'
    '  steps, one step with no carrier is followed by none with one, and where passing stops it ends\n'
    '  within `d` steps. Each bound is attained in `PatternRelay`. The passing premise is supplied.\n'
    '* `Becoming.JointKeeping` (L4): conditions kept together, and a part kept under every course.\n'
    '  No course leaves two guards, or a list of guards, together exactly where no course leaves\n'
    '  any. Along some course this fails: in `ChoicePoint` each of two guards is keepable and the\n'
    '  two together are not, and no rule on the separate keepabilities decides the joint one. In\n'
    '  `Renewable` no course leaves the guard "the focal formation is active" from any\n'
    '  configuration, while from one configuration one run renews and another consumes the\n'
    '  sustaining formation\'s condition: keeping a part decides neither renewal nor what the run\n'
    '  does to others.\n')
SCOPE = (
    '    "Withholding: with memory a formation gives at a step exactly where every formation within "\n'
    '    "that many waits of it gave at the start, withholding stays, spreads downstream and, from one "\n'
    '    "formation reaching a family, ends all giving in it; without memory withholding passes out "\n'
    '    "where no chain of waits is long enough and returns around every loop; more waiting is less "\n'
    '    "giving; in Ring a formation giving whatever it waits on restores every formation from step "\n'
    '    "three on. "\n'
    '    "Widening: on runs of a return map, a loop closes a difference only through a link giving back "\n'
    '    "less than it received; a return map below what it receives closes within d turns, exactly, "\n'
    '    "and merges; taking a constant off closes at the least turn covering the difference; a cut "\n'
    '    "closes at once where what follows gives nothing for nothing; monotone return maps settle "\n'
    '    "within d turns or never fall; doubling links run away; with whole-number strengths a loop "\n'
    '    "closes at the first turn, keeps the difference or runs away, nothing between. "\n'
    '    "Pace: a two-level course whose rule changes only at reading steps is a run of one law; a rule "\n'
    '    "that never reads is kept, nothing the fast level meets reaches it, and what it loses stays "\n'
    '    "lost; a fast difference reaches the rule only at a reading step; regaining needs a change of "\n'
    '    "rule; given two values a stretch of L steps fixes every pair of courses with at most N states "\n'
    '    "that held rules generate exactly when L is at least 2N - 1; a course read whole is fixed by "\n'
    '    "its first N + 1 steps, exactly. "\n'
    '    "Passing: on a web whose activity is carrying, a pattern present from T on with carriers brief "\n'
    '    "for d has a carrier beginning within every d steps; under the supplied passing premise it is "\n'
    '    "passed across one of every d steps, a step with no carrier is followed by none with one, and "\n'
    '    "where passing stops it ends within d steps; PatternRelay attains each bound. "\n'
    '    "JointKeeping: no course leaves guards together exactly where no course leaves any; along some "\n'
    '    "course each of two guards can be keepable and the two together not, and no rule on the "\n'
    '    "separate keepabilities decides the joint one; in Renewable no course leaves the focal "\n'
    '    "formation\'s activity while one run renews and another consumes: keeping a part decides "\n'
    '    "neither renewal nor what the run does to others. "\n')
README_ROWS = [
    '| L3 | [`Becoming.Withholding`](Becoming/Withholding.lean) | giving that waits on giving (no premise beyond the '
    'relation of waits): with memory, closed form (`waitsAll_closed`), withholding stays and spreads downstream, one '
    'withholding ends all giving in a family reached from it (`withholding_absorbs`); without memory, closed form '
    '(`answers_closed`), withholding passes out where no chain is long enough (`gives_without_chain`, exact in `Line`) '
    'and returns around a loop (`withholding_returns`); more waiting, less giving; in `Ring` a formation giving first '
    'restores all from step 3, exactly (`Ring.givesFirst_restores`) |',
    '| L4 | [`Becoming.Widening`](Becoming/Widening.lean) | whether a loop closes, keeps or widens a difference, on '
    'runs of the return map (no premise beyond the hypotheses named): closing needs a link that gives back less than '
    'it received (`closing_needs_less`); a return map below what it receives closes within `d` turns, exactly '
    '(`closes_within`, from `Lasting.Variant.reaches`) and merges (`closing_merges`); taking a constant off '
    '(`sub_const_closes`, `sub_const_open`); a cut (`cut_closes`, `cut_reopened`); monotone return maps settle or rise '
    '(`settles_within`); doubling links run away (`runs_away`); whole-number strengths close at once, keep or run away, '
    'nothing between (`whole_strengths`, `nothing_between`) |',
    '| L4 | [`Becoming.Pace`](Becoming/Pace.lean) | how fast a rule may change (no premise beyond the hypotheses named): '
    'a two-level course whose rule changes only at reading steps is a run of one law (`paced_run`); a rule that never '
    'reads is kept and unreached (`rule_unreached`) and loses what it merges (`never_reads_loses`); a fast difference '
    'reaches the rule only at a reading step (`rule_until_reading`, exact in `Copying`); regaining needs a change of rule '
    '(`Switching.changing_regains`); a stretch of `L` steps fixes every pair of held courses with at most `N` states '
    'exactly when `L ≥ 2N - 1` (`pace_law`, `dissolving`, `held_fixed`); a course read whole is fixed by `N + 1` steps, '
    'exactly (`whole_fixed`, `whole_fixed_exact`) |',
    '| L4 | [`Becoming.Passing`](Becoming/Passing.lean) | a pattern that outlasts each carrier lasts only through '
    'passing (the passing premise `Web.ByPassing` is a hypothesis): carriers begin within every `d` steps '
    '(`Web.begins_within`, an instance of `Covered.arises_within`); the pattern is passed across one of every `d` steps '
    '(`Web.ByPassing.passes_within`); one empty step ends it (`Web.ByPassing.empty_stays`); stopped passing ends it '
    'within `d` steps (`Web.ByPassing.ends_within`); `PatternRelay` attains each bound |',
    '| L4 | [`Becoming.JointKeeping`](Becoming/JointKeeping.lean) | conditions kept together (no premise): under every '
    'course they decompose exactly (`kernel_and_iff`, `kernel_allOf_iff`); along some course they do not '
    '(`Keepable`, `ChoicePoint.each_not_joint`), and no rule on the separate keepabilities decides the joint one '
    '(`ChoicePoint.no_rule_decides_joint`); kept for `n` steps likewise (`ChoicePoint.keptFor_each_not_joint`); keeping a '
    'part decides neither renewal nor what the run does to others (`Renewable.kept_part_not_renewal`) |',
]

root = (PKG / 'Becoming.lean').read_text()
root = once(root, 'import Becoming.Hexagrams\n',
            'import Becoming.Hexagrams\n' + ''.join(f'import Becoming.{m}\n' for _, m in MODS))
root = once(root, '* `Becoming.Contacts` (L4): registration through addressed contacts.',
            DOC + '* `Becoming.Contacts` (L4): registration through addressed contacts.')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.Hexagrams",',
           '"Becoming.Hexagrams", ' + ' '.join(f'"Becoming.{m}",' for _, m in MODS))
chk = once(chk, '    "Description: describing the parts separately gives back a whole of two parts exactly where it "\n',
           SCOPE + '    "Description: describing the parts separately gives back a whole of two parts exactly where it "\n')
(PKG / 'check_becoming.py').write_text(chk)

rd = (PKG / 'README.md').read_text()
lines = rd.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| L4 | [`Becoming.Hexagrams`](Becoming/Hexagrams.lean) |')]
assert len(idx) == 1, idx
lines[idx[0] + 1:idx[0] + 1] = README_ROWS
(PKG / 'README.md').write_text('\n'.join(lines))
print('integrated')
