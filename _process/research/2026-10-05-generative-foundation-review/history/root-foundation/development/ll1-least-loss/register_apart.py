#!/usr/bin/env python3
"""Register LL1's apart roots in THEOREM-CONNECTIVITY-APART.json (each with its category and reason).
usage: python3 -B register_apart.py   (from the checkout root; an entry already present is replaced)"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
F = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY-APART.json'
M = 'Becoming.LeastLoss'
ENTRIES = {
    'Becoming.Amounts.family_rests': ('general-structure',
        'the family law of rest for any amounts, with the bound of the stock by m least losses named; the base reads '
        'amounts only as whole numbers, where it is used in its Archimedean form, Amounts.family_rests_of_archimedean, '
        'by Flow.taking_not_recurring_whole'),
    'Becoming.Dyadic.half_below': ('model-witness',
        'density of the dyadic amounts: below every amount above nothing lies its half, above nothing; a fact about '
        'one constructed model of the amounts, which the base does not read'),
    "Becoming.Layered.ext'": ('support',
        'two layered amounts with equal layers are equal; a one-line unpacking of the structure, used by the '
        'definition Layered.amounts'),
    'Becoming.Layered.never_rests': ('model-witness',
        'the counterexample in one constructed model of the amounts (a least loss, the stock beyond every multiple of '
        'it, never resting): it shows the bound premise of Amounts.rests is needed; not a law of the unfolding'),
    'Becoming.whole_falls_not_recurring': ('restates',
        'falls_not_recurring (Becoming.Renewal) proved again from the least-loss law at whole-number amounts, with the '
        'same statement; on the base its use is restated by Flow.taking_not_recurring_whole '
        '(Flow.taking_not_recurring_from) and Flow.takers_within_on_whole'),
    'Becoming.whole_falls_stop_unrefuted': ('restates',
        'falls_stop_unrefuted (Becoming.Space) proved again from the least-loss law at whole-number amounts, with the '
        'same statement; on the base its use is restated by Flow.change_stops_unrefuted_whole '
        '(Flow.change_stops_unrefuted) and World.rests_unrefuted_enclosed_whole'),
    'Becoming.Amounts.whole_losing_steps': ('general-structure',
        'the approach law at whole-number amounts, stated for any sequences of stocks and losses: no more steps lose '
        'anything than the stock counts; the base reads the same descent through Flow.takers_within_on_whole and '
        'Flow.taking_not_recurring_whole'),
    'Becoming.Halving.approaches_without_reaching': ('model-witness',
        'the halving stock in one constructed model of the amounts approaches rest (an instance of '
        'Amounts.few_large_losses_of_archimedean and Amounts.approaches_rest) and falls at every step: approach '
        'without rest; not a law of the unfolding'),
    'Becoming.Layered.not_archimedean': ('model-witness',
        'one constructed model of the amounts is not Archimedean: the Archimedean premise of the approach law is '
        'needed; not a law of the unfolding'),
    'Becoming.Law.loss_needs_merge': ('restates',
        'Branching.loss_needs_merge states it on a run of every process, needing only the run\'s configurations listed; '
        'at Law.process next it is this law through Branching.law_lossless_iff. The orbit form is proved where it '
        'stands, as Recurrence\'s Law.rise_not_lossless is beside Branching.rise_not_lossless'),
}
data = json.loads(F.read_text())
for name, (category, reason) in ENTRIES.items():
    assert category in data['categories'], category
    data['roots'][name] = {'module': M, 'category': category, 'reason': reason}
F.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n')
print('registered', len(ENTRIES))
