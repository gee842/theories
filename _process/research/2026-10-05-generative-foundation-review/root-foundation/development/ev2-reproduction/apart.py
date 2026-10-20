#!/usr/bin/env python3
"""EV2: register Becoming.Reproduction's apart roots (laws of any finite family or listed generations read by offspring
number, and one witness).

Selection on offspring number itself and its course over generations read by offspring number hold of any finite
family and any listed generations, with no world. The base laws (Flow.closed_lineage_lowered, Flow.closed_not_exact)
go through the generational laws they need (search, fell_step, falls_step_iff, empty_from, ByNumber.sum_eq,
ByNumber.discord_none); the roots below are the ones no base law goes through: registered as general structure, and the
witness Spread as a model witness. Becoming.SelectionTerm.Generations.raises_exact_iff is no longer an apart root:
ByNumber.rises_exact_iff uses it, so its entry is retired (apart-retired.json keeps it).

usage: python3 -B apart.py   (once, from the checkout root)"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REGISTER = HERE.parents[1] / 'THEOREM-CONNECTIVITY-APART.json'
register = json.loads(REGISTER.read_text())
M = 'Becoming.Reproduction'
B = 'Becoming.Reproduction.Generations.ByNumber.'
GEN = ('a law of any listed generations read by offspring number, with no world; generations of descent in a flow '
       '(SelectionTerm.Flow.Descended) are one case, read on the base by Flow.closed_lineage_lowered through '
       'ByNumber.sum_eq and ByNumber.discord_none')
FAM = ('a law of any finite family read with its own weights, with no world; offspring numbers of a generation of '
       'descent are one case')
NEW = {
    B + 'not_lower_step': ('general-structure',
        'where transmission lowers no offspring number the mean offspring number does not fall: ' + GEN),
    B + 'rises_exact_iff': ('general-structure',
        'with exact transmission the mean offspring number rises exactly where offspring numbers vary (Fisher\'s '
        'theorem with exact transmission, in counting form): ' + GEN),
    B + 'kept_exact_iff': ('general-structure',
        'with exact transmission the mean offspring number is kept exactly where offspring numbers are uniform: ' + GEN),
    'Becoming.Reproduction.concord_self': ('general-structure',
        'concordance of the weights with themselves is the squared differences over ordered pairs, by definition: ' + FAM),
    'Becoming.Reproduction.number_variation': ('general-structure',
        'selection on offspring number itself is the square of the number of offspring with the squared differences: '
        + FAM),
    'Becoming.Reproduction.number_never_against': ('general-structure',
        'over offspring the mean parental offspring number is at least the mean over parents: ' + FAM),
    'Becoming.Reproduction.number_none_iff': ('general-structure',
        'the two means are equal exactly where offspring numbers are uniform: ' + FAM),
    'Becoming.Reproduction.Spread.spread': ('model-witness',
        'a parent with two offspring beside one with none: the squared difference four, the mean parental offspring '
        'number two over offspring and one over parents; a fact about one constructed family, not a law of the unfolding'),
}
for name, (category, reason) in NEW.items():
    assert name not in register['roots'], name
    register['roots'][name] = {'module': M, 'category': category, 'reason': reason}
RETIRED = 'Becoming.SelectionTerm.Generations.raises_exact_iff'
if RETIRED in register['roots']:
    retired = {RETIRED: register['roots'].pop(RETIRED)}
    (HERE / 'apart-retired.json').write_text(json.dumps(retired, ensure_ascii=False, indent=1) + '\n')
REGISTER.write_text(json.dumps(register, ensure_ascii=False, indent=1) + '\n')
print('registered', len(NEW))
