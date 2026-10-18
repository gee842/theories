#!/usr/bin/env python3
"""F3C (18 October 2026): register F3C's new core modules. Idempotent; rerun after a rebase.

usage (from the checkout root): python3 -B land_c.py [MODULE ...]   (default: every module below)

Adds each module to `CORE` in `check_becoming.py` after its anchor, imports it in `Becoming.lean`
and lists it in that file's module notes, the package README's layer table and import notes, and
the chapter reference's table. Touches no existing core module, bridge or join file, and neither
the `BRIDGE` nor the `PERIPHERY_JOINS` list. `IntegerOrder` imports F3R's `Becoming.Integers`, so
it registers only after F3R's sub-chain 1 is on main.
"""
import pathlib
import re
import sys

PKG = pathlib.Path('experiments/integrated-correction/general-framework/generative-basis/lean/becoming')
REF = pathlib.Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING-REFERENCE.md')

# module: (layer, CORE / docstring / reference anchor, README anchor, theorems, text)
# The README's layer table lists no `Readout`, `Viability` or `Keeping`, so its rows follow `Quantum`
# (L2), `Weighted` (L3) and `Coupling` (L4); the other lists follow the module each builds on.
MODULES = {
    'ListTests': ('L2', 'Keeping', 'Quantum', 36,
                  'Boolean tests over lists and options (no premise): `all`, `any`, `contains`, `filter`, `find?`, '
                  '`bind` and `map` say what they test (`all_true_iff`, `any_true_iff`, `find_none_iff`, '
                  '`bind_eq_some`), proved by recursion where the prelude uses `propext`'),
    'Naturals': ('L2', 'ListTests', 'ListTests', 18,
                 'the subtraction and order laws of drawn amounts (no premise): cancellation, `sub_sub`, '
                 '`le_sub_of_add_le` and the bounds of a sum, proved by recursion where the prelude uses `propext`'),
    'ContingentPlans': ('L3', 'Naturals', 'Weighted', 18,
                        'contingent plans, probe then respond by the answer (no premise): a plan\'s run is a trace of '
                        'the interface\'s process (`run_iff_trace`, `passes_iff_completes`); a plan is selected for a '
                        'listed belief exactly where a listed plan completes from every configuration of it '
                        '(`selected_iff_completes`), an empty belief certifies none, and equal answers select the same '
                        'response (`branch_congr`, `branch_incompatible`)'),
    'Actuation': ('L3', 'ContingentPlans', 'ContingentPlans', 46,
                  'issue, delivery and enactment of a command as moves of one installation (no premise): what each '
                  'move needs (`issue_stale`, `enact_revoked`), the reserve and what is drawn conserved along every '
                  'trace (`conserved_trace`), the protocol\'s exact effects (`protocol_exact`), and a timely inquiry '
                  'keeping correction possible where an equally accurate slow one does not (`timely_run`, '
                  '`late_probe_no_run`)'),
    'TreeSearch': ('L3', 'Actuation', 'Actuation', 35,
                   'a finite search of a route tree read as the run of a determined law (no premise): what is found '
                   'is there (`discover_sound`), exhausted is absence within the frontier (`exhausted_dead`), enough '
                   'fuel finds an inhabited tree (`inhabited_discovered`), and step `n` of every run reads as the '
                   'scan with fuel `n` (`run_reads_scan`)'),
    'Dispatch': ('L3', 'TreeSearch', 'TreeSearch', 34,
                 'a found route re-read in the current installation before it is acted on (no premise): dispatch '
                 'fails without the route or the epoch (`dispatch_absent`, `dispatch_revoked`), a search followed by '
                 'its dispatch completes and draws both (`acquired_execution`, `discovery_then_dispatch`), and a '
                 'capture accepted as the current epoch passes the gate (`captured_epoch_passes`)'),
    'FaultEnvelopes': ('L3', 'Dispatch', 'Dispatch', 19,
                       'what a certificate over a roster of domains warrants under supplied fault envelopes (no '
                       'premise): soundness for every admitted fault set (`certificate_sound`), availability exactly '
                       'where the envelope is separated (`availability_iff_separated`), and no warrant from '
                       'duplication, an empty envelope or a stronger one (`duplicated_roster_same`, '
                       '`stronger_envelope_no_new_acceptance`)'),
    'Transactions': ('L3', 'FaultEnvelopes', 'FaultEnvelopes', 59,
                     'a gate of certified readings and approvals, and the monitor process it makes (no premise): an '
                     'open gate finds the route and keeps the scope (`gate_route`, `gate_within_scope`), a transaction '
                     'has exact effects and blocks its replay (`execute_exact`, `replay_no_trace`), the scope guard '
                     'refuses a forbidden command whatever the issuers (`guard_blocks_forbidden`), and correlated '
                     'faults outside the model can admit one (`single_fault_model_admits_forbidden`)'),
    'Reconfiguration': ('L3', 'Transactions', 'Transactions', 51,
                        'fault envelopes induced by root causes, and the step that installs a new roster (no premise): '
                        'readiness is a nonempty separated induced envelope (`ready_iff_nonempty_separated`); the '
                        'step renews epoch and serial, keeps the scope and stales old requests (`step_renews`, '
                        '`step_keeps_scope`, `step_stales_old_epoch`); two members of one cause are not redundant '
                        '(`same_cause_not_redundant`), and a cause the formulas omit still breaks the model'),
    'PooledEnvelopes': ('L3', 'Reconfiguration', 'Reconfiguration', 44,
                        'certificates over the pooled envelopes of several causal models, and the inquiry process that '
                        'narrows them (no premise): the actual model survives faithful tests and a certificate over '
                        'the pool is sound (`pooled_certificate_sound`); each model can be ready while the pool is not '
                        '(`every_candidate_ready_pool_not`); along every run the actual model stays a candidate '
                        '(`actual_kept`), and an equally accurate slower inspection misses the deadline '
                        '(`slow_misses_deadline`)'),
    'WitnessRefinement': ('L4', 'PooledEnvelopes', 'Coupling', 44,
                          'a structural question read jointly with its fallible witnesses (no premise): refinement '
                          'keeps the actual model (`refine_keeps_actual`); on complete transcripts opposite answers '
                          'are always told apart exactly where the envelopes are cross-separated '
                          '(`complete_diagnosability_iff_cross_separation`, through '
                          '`Readout.no_common_report_envelopes_iff`); a fifth witness resolves what four cannot and '
                          'stays fallible, and the audit is a process whose runs only narrow the candidates'),
    'ChanceFloors': ('L3', 'WitnessRefinement', 'PooledEnvelopes', 6,
                     'what pointwise fulfilment of a due protection gives under a finite law of chance (no premise): '
                     'a chance floor (`fulfillment_gives_chance_floor`, through `mass_mono`), repair as an event that '
                     'raises the mass (`repair_adds_new_protection`), and a route of positive chance missing exactly '
                     'the due protection (`positive_chance_can_miss_due_protection`)'),
    'IntegerOrder': ('L2', 'ChanceFloors', 'Integers', 39,
                     'the order laws of `Int` without `propext` (no premise): through the ring laws of '
                     '`Becoming.Integers`, every order law reduces to a sum of naturals being natural and an integer or '
                     'its negative being natural; comparison is decided by cases (`lt_or_le`), without excluded '
                     'middle'),
    'Acceptance': ('L3', 'IntegerOrder', 'ChanceFloors', 17,
                   'an accept bit given priority over a base score, and what it does not protect (no premise): with a '
                   'positive lift a choice is best exactly where it accepts and its move is best by the base score '
                   '(`acceptance_factorization`), so acceptance restores no access the base optimum lacks; diverting '
                   'the resource that keeps correction possible can be best (`accepting_optimum_can_destroy_access`), '
                   'and a value computed without the restriction can prefer the wrong branch '
                   '(`stale_value_shield_suboptimal`)'),
    'GuardHorizon': ('L3', 'Acceptance', 'Acceptance', 32,
                     'keeping a guard by a choice of moves, over a horizon, from readings (choice over the readings '
                     'named where used): the controlled reading of `Viability` (`viable_succ_iff`, `certificate_viable`, '
                     '`kernel_viable`); Bellman values bound every course kept within the guard '
                     '(`bellman_bounds_safe`); a choice uniform on readings exists exactly where each reading has one '
                     'good move, the converse with `Viability.ChoiceOver` (`uniform_policy_iff_fiber_feasible`); '
                     'endpoint access can hide a gap that an overlapping handoff closes '
                     '(`endpoint_access_hides_gap`, `overlapping_handoff_keeps_access`)'),
}
IMPORT_NOTES = {
    '; within L3,': ('; `IntegerOrder` imports `Integers`'),
    '; within L4,': ('; `ContingentPlans` imports `ListTests`; `Actuation` imports `ContingentPlans` and `Naturals`; '
                     '`TreeSearch` imports `Branching`, `ListTests` and `Naturals`; `Dispatch` imports `Actuation` and '
                     '`TreeSearch`; `FaultEnvelopes` imports `ListTests`; `Transactions` imports `Actuation`, '
                     '`TreeSearch` and `FaultEnvelopes`; `Reconfiguration` imports `Transactions`; `PooledEnvelopes` '
                     'imports `Reconfiguration`; `ChanceFloors` imports `Weighted`; `Acceptance` imports '
                     '`IntegerOrder`; `GuardHorizon` imports `Acceptance`'),
    '). L1–L3 contain': ('; `WitnessRefinement` imports `Readout`'),
}


def after_entry(lines, start, is_entry):
    """Index just past the entry starting at `start` (its continuation lines included)."""
    i = start + 1
    while i < len(lines) and not is_entry(lines[i]) and lines[i].startswith('  '):
        i += 1
    return i


def main(selected):
    checker = PKG / 'check_becoming.py'
    src = checker.read_text()
    core = re.search(r'^CORE = \[(.*?)\]', src, re.S | re.M)
    body = core.group(1)
    for m in selected:
        name = f'"Becoming.{m}"'
        if name in body:
            continue
        anchor = f'"Becoming.{MODULES[m][1]}"'
        assert anchor in body, anchor
        body = body.replace(anchor, f'{anchor}, {name}', 1)
    src = src[:core.start(1)] + body + src[core.end(1):]
    checker.write_text(src)

    root = PKG / 'Becoming.lean'
    lines = root.read_text().split('\n')
    for m in selected:
        layer, anchor, _, _, text = MODULES[m]
        if f'import Becoming.{m}' not in lines:
            i = lines.index(f'import Becoming.{anchor}')
            lines.insert(i + 1, f'import Becoming.{m}')
        if not any(l.startswith(f'* `Becoming.{m}` (') for l in lines):
            i = next(k for k, l in enumerate(lines) if l.startswith(f'* `Becoming.{anchor}` ('))
            j = after_entry(lines, i, lambda l: l.startswith('* `'))
            words, out, cur = f'* `Becoming.{m}` ({layer}): {text}.'.split(' '), [], ''
            for w in words:
                if cur and len(cur) + 1 + len(w) > 98:
                    out.append(cur)
                    cur = '  ' + w
                else:
                    cur = f'{cur} {w}' if cur else w
            out.append(cur)
            lines[j:j] = out
    root.write_text('\n'.join(lines))

    readme = PKG / 'README.md'
    lines = readme.read_text().split('\n')
    for m in selected:
        layer, _, anchor, _, text = MODULES[m]
        if any(l.startswith(f'| {layer} | [`Becoming.{m}`]') for l in lines):
            continue
        i = next(k for k, l in enumerate(lines) if re.match(rf'^\| L\d \| \[`Becoming\.{anchor}`\]', l))
        lines.insert(i + 1, f'| {layer} | [`Becoming.{m}`](Becoming/{m}.lean) | {text} |')
    text = '\n'.join(lines)
    for at, note in IMPORT_NOTES.items():
        if note not in text:
            assert text.count(at) == 1, at
            text = text.replace(at, note + at, 1)
    readme.write_text(text)

    lines = REF.read_text().split('\n')
    for m in selected:
        layer, anchor, _, count, text = MODULES[m]
        if any(f'[Becoming.{m}](' in l for l in lines):
            continue
        i = next(k for k, l in enumerate(lines) if re.match(rf'^\| L\d \| \[Becoming\.{anchor}\]\(', l))
        link = f'../../../{PKG}/Becoming/{m}.lean'
        lines.insert(i + 1, f'| {layer} | [Becoming.{m}]({link}) | {text[0].upper() + text[1:]}. | {count} |')
    REF.write_text('\n'.join(lines))


if __name__ == '__main__':
    main(sys.argv[1:] or list(MODULES))
