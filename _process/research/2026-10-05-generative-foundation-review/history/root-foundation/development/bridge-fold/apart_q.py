#!/usr/bin/env python3
"""F3Q (18 October 2026): register the apart roots of F3Q's six new core modules in THEOREM-CONNECTIVITY-APART.json.

usage (from the checkout root): python3 -B apart_q.py        idempotent

Each root's periphery counterpart (port-q.md) is already registered, almost always as a model witness; the core
statement keeps that category, with the reason restated against the core. The periphery entries stay until the sweep
retires their modules.
"""
import json
import pathlib

REG = pathlib.Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY-APART.json')
MW = 'model-witness'
CA, DE, LG, PR, RF = ('Becoming.CodeAcquisition', 'Becoming.Derivation', 'Becoming.LearnedGrouping',
                      'Becoming.PartialReadout', 'Becoming.RouteFormation')
ROOTS = {
    CA + '.choice_keeps_content': (MW, 'a fact about the one acquired code of `usual` and two picks of a primitive; no run or world reads it'),
    CA + '.equal_primitives_unresolved': (MW, 'a fact about two constructed codes with equal primitives'),
    CA + '.missing_composite_no_code': (MW, 'a fact about one constructed list of records without the composite probe'),
    CA + '.nonuniform_agrees_on_probes': (MW, 'a fact about one constructed response function `nonuniform` on the three probes'),
    CA + '.nonuniform_fails_transfer': (MW, 'a fact about one constructed response function `nonuniform`, which no program runs'),
    CA + '.novel_not_probe': (MW, 'a decidable inequality of four constructed expressions'),
    CA + '.primitives_no_exact': (MW, 'the code model\'s instance of `PartialReadout.ExactWithin.lumped`: the primitive probes read by no exact reading of the order; the general law is joined on runs as `PartialReadout.Runs.exact_lumped`'),
    CA + '.probe_readings': ('support', 'a definitional (rfl) statement about the evaluation of the two atoms and the composite probe, a structural recursion of the module\'s own grammar'),
    CA + '.records_form_interpretation': (MW, 'a fact about the records of the constructed code `usual`; the step that installs it is read on the training process (`step_installs`)'),
    CA + '.renaming_keeps_values': ('support', 'invariance of the module\'s own expression evaluation under renaming the atoms, a structural recursion with no reading as a process, run or world'),
    CA + '.reversed_composite_switches': (MW, 'a fact about one constructed list of records with the composite reversed'),
    CA + '.wrong_order_fails_transfer': (MW, 'a fact about two constructed codes (`usual`, `switched`) on one expression'),
    DE + '.claim_implies_itself': (MW, 'a single derivation over the Bool countermodel (implication introduction discharging one premise)'),
    DE + '.claim_not_closed': (MW, 'the Bool countermodel instance of `countermodel_excludes`, which is read on the scope of an inquiry as `Scope.countermodel`'),
    DE + '.claim_not_throughout': (MW, 'a fact about one constructed two-point countermodel on Bool'),
    DE + '.rows_each_met': (MW, 'a fact about the control basis `rows` on Bool, an inference control, not two worlds'),
    DE + '.rows_not_pointwise': (MW, 'a fact about the control basis `rows` on Bool, an inference control, not two worlds'),
    LG + '.gap_breaks_edge': (MW, 'a computed fact about the edges and bond of three supplied logs, not about a configuration or a trace of reception'),
    LG + '.ideal_two_word': (MW, 'the instance of `two_word_iff` at the supplied ideal relation; the learned relation is read along the trace of reception (`grouping_assembles`)'),
    LG + '.repetition_joins_words': (MW, 'a computed fact about grouping one supplied list by the bond of that list read as a log'),
    PR + '.direct_exact_unreversed': (MW, 'a fact about the constructed two-bit channel model, which has no evident reading as a run or world'),
    PR + '.direct_not_sound': (MW, 'a fact about the constructed two-bit channel model, which has no evident reading as a run or world'),
    PR + '.direct_right_once': (MW, 'one evaluation at one channel of the constructed model'),
    PR + '.exactWithin_univ_iff': ('general-structure', 'on the whole domain, an exact partial reading is a decoder in the sense of `Readout.Decodes`, for every type; it joins two core notions, and the run forms are `PartialReadout.Runs`'),
    PR + '.lumpedWithin_univ_iff': ('general-structure', 'on the whole domain, lumping within the domain is `Learning.Lumped`, for every type; it joins two core notions, and the run forms are `PartialReadout.Runs`'),
    PR + '.negated_exact': (MW, 'a fact about the constructed channel model (double reversal read exactly)'),
    PR + '.parity_exact': (MW, 'a fact about the constructed channel model (exactness surviving compression); the general law is read on runs as `Runs.retained_exact`'),
    PR + '.safe_of_holds': ('support', 'a statement using only the prelude: a true proposition follows from any hypotheses'),
    PR + '.signal_no_exact': (MW, 'the channel model\'s instance of `ExactWithin.lumped`; the general law is read on runs as `Runs.exact_lumped`'),
    PR + '.signal_sound_silent': (MW, 'the channel model\'s instance of `SoundWithin.silent`; the general law is read on runs as `Runs.sound_silent`'),
    RF + '.reversal_unseen': ('support', 'invariance of the module\'s own expression evaluation under reversing the join order when the primitives agree, with no reading as a process, run or world'),
    RF + '.two_socket_routes': (MW, 'a computed list: the routes the supplied grammar generates with two sockets'),
}

d = json.loads(REG.read_text())
added = 0
for name, (cat, reason) in ROOTS.items():
    assert cat in d['categories'], cat
    if name not in d['roots']:
        d['roots'][name] = {'module': name.rsplit('.', 1)[0],
                            'category': cat, 'reason': reason}
        added += 1
REG.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
print(added, 'roots added')
