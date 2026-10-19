"""R30 rename spec (draft, read-only planning). Each entry: old, new, kind, reason, confidence, justified, note.
kind: decl | namespace | module | binder | docstring | delete | port | keep.
`fam(...)` expands a family: declarations whose full name matches a regex, renamed by a substitution."""
import re

B = 'Becoming.'
E = []  # entries


def add(old, new, kind, reason, conf='high', justified=True, note=''):
    E.append(dict(old=old, new=new, kind=kind, reason=reason, confidence=conf, justified=justified, note=note))


def fam(decls, cond, sub, reason, conf='high', justified=True, note='', skip=()):
    for x in decls:
        if cond(x) and x['full'] not in skip:
            new = sub(x['full'])
            if new != x['full']:
                add(x['full'], new, 'decl', reason, conf, justified, note)


def build(decls):
    # ---------------- Returns: the other senses (Law.Returns is R28's abbrev; Branching.Returns is the core word) ----
    r = 'B2/F §2f #16: "return" is a configuration had again (Branching.Returns); here the condition\'s level comes back to meet a need, which the core vocabulary calls restored'
    add(B + 'Web.Returns', B + 'Web.Restored', 'decl', r)
    add(B + 'Web.ReturnsWithin', B + 'Web.RestoredWithin', 'decl', r)
    add(B + 'Web.RenewedWithin.returns', B + 'Web.RenewedWithin.restored', 'decl', r + ' (family)')
    add(B + 'Web.Returns.not_consumed', B + 'Web.Restored.not_consumed', 'decl', r + ' (family)')
    add(B + 'Slowing.returns', B + 'Slowing.restored', 'decl', r + ' (witness family)')
    for a, b in [('phase_after_return', 'phase_after_restoration'), ('phase_next_return', 'phase_next_restoration'),
                 ('met_at_return', 'met_at_restoration'), ('unmet_before_return', 'unmet_before_restoration')]:
        add(B + 'Slowing.' + a, B + 'Slowing.' + b, 'decl', r + ' (witness family; the witness\'s "return" event)', 'medium',
            note='optional: names an event of the witness, not the definition; rename only for one word per notion')
    add(B + 'Return', B + 'Restoration', 'module', r + '; the module defines Restored/RestoredWithin and renewal over cycles', 'medium',
        note='file Return.lean -> Restoration.lean (R22 precedent: modules + paths maps); importers: grep "import Becoming.Return$"')
    r = 'B2/F §2f #16: a carried difference coming back around a loop of couplings in time order; F\'s core vocabulary calls this a round trip, not a return'
    add(B + 'Returns', B + 'RoundTrip', 'decl', r + '; at root it also shadows Branching.Returns wherever Branching is opened')
    add(B + 'Returns.of_couplesAt', B + 'RoundTrip.of_couplesAt', 'decl', r + ' (family)')
    add(B + 'carried_doubles_return', B + 'carried_doubles_roundTrip', 'decl', r + ' (family)')
    add(B + 'carried_returns', B + 'carried_roundTrip', 'decl', r + ' (family)', 'medium')
    add(B + 'runaway_of_returns', B + 'runaway_of_roundTrip', 'decl', r + ' (family)')
    add(B + 'Frequency.SelfLoop.returns', B + 'Frequency.SelfLoop.roundTrip', 'decl', r + ' (witness family)')

    # ---------------- Lossless: the amount sense ----------------
    r = 'B2: Lossless is injective steps (Branching/Law); Flow.Lossless is every closed family\'s exchanges giving what they take: amount conserved'
    add(B + 'Flow.Lossless', B + 'Flow.Conserving', 'decl', r, 'medium',
        note='B proposed Flow.AmountLossless; Conserving is the structural word and is the exact complement of Flow.Dissipative on closed families. Records of R5 cite "lossless"; rebind')
    add(B + 'Flow.LosslessOn', B + 'Flow.ConservingOn', 'decl', r, 'medium')
    for a, b in [('Flow.LosslessOn.gainlessOn', 'Flow.ConservingOn.gainlessOn'), ('Flow.Lossless.gainless', 'Flow.Conserving.gainless'),
                 ('Flow.DissipatesOn.idle_of_lossless', 'Flow.DissipatesOn.idle_of_conserving'), ('Flow.LosslessOn.lost_zero', 'Flow.ConservingOn.lost_zero'),
                 ('Flow.losslessOn_withRecord_iff', 'Flow.conservingOn_withRecord_iff'), ('Flow.Balances.changes_within_lossless', 'Flow.Balances.changes_within_conserving'),
                 ('Flow.Balances.returns_of_lossless', 'Flow.Balances.returns_of_conserving'), ('Flow.Balances.not_lossless_of_arrow', 'Flow.Balances.not_conserving_of_arrow'),
                 ('Flow.Balances.not_lossless_of_dissipates', 'Flow.Balances.not_conserving_of_dissipates'),
                 ('Passing.lossless', 'Passing.conserving'), ('Settling.lossless', 'Entropy.Settling.conserving'), ('Gathering.lossless', 'Gathering.conserving')]:
        add(B + a, B + b, 'decl', r + ' (family)', 'medium')

    # ---------------- Settles / Rests / RestsFrom ----------------
    r = 'B2/D42: "settle" = unchanged from some step on (Enough.Settles, Becoming.Settling); this definition says an ideal of words has a longest word'
    add(B + 'HistoryIdeals.Settles', B + 'HistoryIdeals.HasLongest', 'decl', r)
    add(B + 'HistoryIdeals.settles_principal', B + 'HistoryIdeals.hasLongest_principal', 'decl', r + ' (family)')
    add(B + 'HistoryIdeals.principal_settles', B + 'HistoryIdeals.principal_hasLongest', 'decl', r + ' (family)')
    r = 'B2/D42: an ideal of stretches with one reaching the latest horizon among them, not a run unchanged from some step'
    add(B + 'Stretches.Settles', B + 'Stretches.HasLatest', 'decl', r)
    add(B + 'Stretches.settles_principal', B + 'Stretches.hasLatest_principal', 'decl', r + ' (family)')
    add(B + 'Stretches.principal_settles', B + 'Stretches.principal_hasLatest', 'decl', r + ' (family)')
    add(B + 'Stretches.cut_settles_iff', B + 'Stretches.cut_hasLatest_iff', 'decl', r + ' (family)')
    r = 'B2/D42: a belief all of whose rules give one answer to the question decides it; nothing settles in the run sense'
    add(B + 'Narrowing.Settles', B + 'Narrowing.Decides', 'decl', r, 'medium',
        note='theorem names keep the English "settles/unsettled" (a question settled is idiomatic); only the definition and answer_of_settles/settles_learn_iff move. Alternative: leave Narrowing alone (justified=false) if the board judges "settles a question" exact')
    add(B + 'Narrowing.answer_of_settles', B + 'Narrowing.answer_of_decides', 'decl', r + ' (family)', 'medium')
    add(B + 'Narrowing.settles_learn_iff', B + 'Narrowing.decides_learn_iff', 'decl', r + ' (family)', 'medium')
    r = 'B2/F9/F14: nothing rests: the run may keep changing; the extrapolation\'s prediction is right from T on'
    for ns in ('Learnable', 'LearnableRuns'):
        add(B + ns + '.RestsFrom', B + ns + '.PredictsFrom', 'decl', r, 'medium',
            note='F9 proposed AccordsFrom; Learning.Accords (N5) already means a hypothesis agreeing with a prefix, so Accords would collide. D45(4) "extrapolation that comes to rest takes 停息" must be revised in the same landing. R29 may fold LearnableRuns into Learnable (B2a); then only Learnable keeps a row')
        add(B + ns + '.Rests', B + ns + '.Predicts', 'decl', r, 'medium')
    for a, b in [('Learnable.agree_of_rests_both', 'Learnable.agree_of_predicts_both'), ('Learnable.not_rests_on_both', 'Learnable.not_predicts_on_both'),
                 ('Learnable.still_not_rests_on_both', 'Learnable.still_not_predicts_on_both'), ('Learnable.still_lumped_of_rests', 'Learnable.still_lumped_of_predicts'),
                 ('Learnable.rests_through', 'Learnable.predicts_through'), ('Learnable.Pair.first_not_rests', 'Learnable.Pair.first_not_predicts'),
                 ('Learnable.Pair.whole_rests', 'Learnable.Pair.whole_predicts'), ('LearnableRuns.restsFrom_iff', 'LearnableRuns.predictsFrom_iff'),
                 ('LearnableRuns.rests_iff', 'LearnableRuns.predicts_iff'), ('LearnableRuns.agree_of_rests_both', 'LearnableRuns.agree_of_predicts_both'),
                 ('LearnableRuns.not_rests_on_both', 'LearnableRuns.not_predicts_on_both'), ('LearnableRuns.rests_through', 'LearnableRuns.predicts_through')]:
        add(B + a, B + b, 'decl', r + ' (family)', 'medium')
    r = 'F9/F14: 停息 (World.RestsFrom) is "nothing arises or ceases from N on"; Enough\'s definition is a state the run leaves unchanged with its target met (静), "stays" being D42\'s word for an unchanged step'
    add(B + 'Enough.RestsFrom', B + 'Enough.StaysMetFrom', 'decl', r, 'medium',
        note='D42 adopted "come to rest = settle with the target met" and D45(4) gives it 停息: renaming needs a D42/D45(4) revision in the same landing (F14\'s 静/停息 split). If that revision is not taken, mark justified=false and keep RestsFrom')
    add(B + 'Enough.Rests', B + 'Enough.StaysMet', 'decl', r, 'medium')
    add(B + 'Enough.possibly_rests_iff', B + 'Enough.possibly_staysMet_iff', 'decl', r + ' (family; cited in D41)', 'medium')
    r = 'F9/F14: the witness is a pause (one step inactive though supported), not 停息 or 静'
    add(B + 'Ranking.Rest', B + 'Ranking.Pause', 'namespace', r, note='module=Becoming.Relevance (the witness sits in Relevance.lean); also one of the 28 Unfolding port sites')
    add(B + 'Ranking.Rest.courses', B + 'Ranking.Pause.courses', 'decl', r)
    add(B + 'Ranking.Rest.rest_ranked_below', B + 'Ranking.Pause.pause_ranked_below', 'decl', r + '; cited in chapter en/zh glossary')
    add(B + 'World.RestsFrom', B + 'World.RestsFrom', 'keep', 'F14: the one 停息 sense; keeps its name', 'high', False)
    add(B + 'Enough.Settles', B + 'Enough.Settles', 'keep', 'D42: "settle" = unchanged from some step on; the sense the other Settles leave', 'high', False)

    # ---------------- Keeps / Closed / Continues / Balanced / Alike / Merges ----------------
    r = 'B2/F §2f #23: Web.Keeps is the order word (includes both ways); Branching.Keeps is "every configuration reachable from s reaches s", the standard essential-state property'
    add(B + 'Branching.Keeps', B + 'Branching.Essential', 'decl', r, 'medium',
        note='alternative KeepsReturnable; Junctures\' processes `keeping`/`losing` keep their names')
    for o, why in [('Dependence.Keeps', 'need met at s and at t; pairs with Breaks; exact and local'),
                   ('Joining.Keeps', 'p is a homomorphism of joinings; "keeps" exact and local'),
                   ('Footprinted.Keeps', 'a renumbering keeps the order of joined exchanges; exact and local'),
                   ('Registration.Keeps', 'the new lumping keeps the old distinctions; exact and local')]:
        add(B + o, B + o, 'keep', 'B2 counted it among 7 Keeps; ' + why + '. Fails AGENTS\' bar (no wrong meaning, no Lean collision)', 'high', False)
    add(B + 'Ideals.Closed', B + 'Ideals.ScottClosed', 'decl', 'B2/F §2f #18: "closed" is closure under a relation; this is a lower class closed under directed unions, the standard Scott-closed class', 'high')
    for a in ('same', 'principal_of_mem', 'refutable_iff', 'hull_iff'):
        add(B + 'Ideals.Closed.' + a, B + 'Ideals.ScottClosed.' + a, 'decl', 'B2/F §2f #18 (family)')
    add(B + 'GuardHorizon.Closed', B + 'GuardHorizon.ControlledInvariant', 'decl',
        'B2/F §2f #18: a set within the guard from each of whose members some enabled move stays in the set; the control-theory term is controlled invariant', 'medium',
        note='its theorem is already `closed_viable`; alternative: keep Closed (local)')
    add(B + 'GuardHorizon.closed_viable', B + 'GuardHorizon.controlledInvariant_viable', 'decl', 'family of the above', 'medium')
    for o, why in [('OneStep.Closed', 'the law of a closed family of passages: "closed" in the enclosure sense the glossary uses'),
                   ('SharedCodes.Closed', 'a hearing closed for a group; exact and local'),
                   ('Undecided.Closed', 'the first N sentences speak only of one another: closed in the standard logical sense')]:
        add(B + o, B + o, 'keep', 'B2 counted 5 Closed; ' + why, 'high', False)
    for o, why in [('Web.Continues', 'f continues as an active successor: the continuation sense'),
                   ('Lasting.Continues', 'a process can continue n steps: the continuation sense'),
                   ('OneStep.Continues', 'continuity of what stands across steps; the docstring says so')]:
        add(B + o, B + o, 'keep', 'B2 counted 3 Continues; ' + why + '. No wrong meaning', 'high', False)
    for o in ('Passage.Balanced', 'World.Balanced', 'Stock.Balanced'):
        add(B + o, B + o, 'keep', 'B2 counted 3 Balanced: all three are one notion (after + taken = before + given) at three levels; one name is right, a join is R33 work', 'high', False)
    add(B + 'Law.Merges', B + 'Law.Merges', 'keep', 'B2 counted 3 Merges; only Law.Merges and Branching.Merges exist (one notion, R28 makes Law.Merges an abbrev). Entropy:87/98 docstrings cite `Web.Merges`/`Web.merges_of_settles`, which do not exist: fix the docstrings', 'high', False)
    r = 'B2/F §2f #15: Alike is bisimilar; these say two assignments agree on a plan, which Learning.Training.AgreeOn already names'
    add(B + 'ReferencePlan.Alike', B + 'ReferencePlan.AgreeOn', 'decl', r, 'high', note='Labelled:304 docstring calls it "another sense"; ReferencePlan.alike_iff_agreeOn becomes a restatement (R29 may delete it)')
    add(B + 'ReferencePlan.alike_iff_agreeOn', B + 'ReferencePlan.agreeOn_iff', 'decl', r + ' (family)', 'medium')
    add(B + 'Contacts.Alike', B + 'Contacts.AgreeOn', 'decl', r + '; it is an abbrev of Learning.Training.AgreeOn', 'high', note='or delete the abbrev and use Learning.Training.AgreeOn')
    add(B + 'Contacts.Alike.refl', B + 'Contacts.AgreeOn.refl', 'decl', r + ' (family)')
    add(B + 'ReferencePlan.alikeOnInstalled', B + 'ReferencePlan.alikeOnInstalled', 'keep', 'N5 name; reads alike-on-installed, a lumping; leave', 'high', False)

    # ---------------- generation_* -> arising ----------------
    r = 'F3: "generation" is reserved for widening (D2, AGENTS); these state that embodied members arise at arbitrarily late steps'
    fam(decls, lambda x: re.match(r'Becoming\.Web\.generation_', x['full']),
        lambda f: f.replace('Web.generation_', 'Web.embodiedArising_'), r)
    add(B + 'Web.dissipation_generation_not_recurring', B + 'Web.dissipation_arising_not_recurring', 'decl', 'F3: the statement is about Web.Unceasing (arising at arbitrarily late steps), not generation')
    add(B + 'Renewable.renewal_without_generation', B + 'Renewable.renewal_without_arising', 'decl', 'F3: the statement is "renewed and nothing arises"')
    r = 'F3/F §2f #22: an active formation renewing a condition of the family; "regeneration" reads as generation; the theory\'s word for raising a family\'s level is replenishment (generation_needs_replenishment, standing_needs_replenishment_from)'
    add(B + 'Web.Regenerating', B + 'Web.Replenishing', 'decl', r, 'medium')
    add(B + 'Web.Unceasing.regeneration_recurs', B + 'Web.Unceasing.replenishment_recurs', 'decl', r + ' (family)', 'medium')
    add(B + 'Generation', B + 'Arising', 'module', 'F3: the module reads arising, unceasing arising and renewal; generation is reserved for widening', 'high',
        note='namespace Becoming.Arising exists as an Order witness (Order:1896); qualify it as Order.Arising in the same sweep (row below). Header "Generation: arising, ..." and Web.Unceasing\'s docstring "Generation does not cease" change by reading')
    r = 'F3/F9: "generation" here is new living content absent before (the SecuresPositiveGround sense), not widening'
    add(B + 'PositiveGround.contingent_generation', B + 'SecuredContent.contingent_newContent', 'decl', r)
    add(B + 'PositiveGround.contingent_generation_of_unrestricted', B + 'SecuredContent.contingent_newContent_of_unrestricted', 'decl', r)
    add(B + 'Handoff.generation_by_bound', B + 'Handoff.newContent_by_bound', 'decl', r)
    add(B + 'Handoff.revised_generation_by_bound_of_unrestricted', B + 'Handoff.revised_newContent_by_bound_of_unrestricted', 'decl', r)
    add(B + 'Handoff.generation_by_bound_on_runs', B + 'Handoff.newContent_by_bound_on_runs', 'decl', r)
    add(B + 'Handoff.positive_ground_by_bound', B + 'Handoff.securesNewContent_by_bound', 'decl', 'F9: named after SecuresPositiveGround')
    add(B + 'Handoff.positive_ground_by_bound_of_unrestricted', B + 'Handoff.securesNewContent_by_bound_of_unrestricted', 'decl', 'F9: named after SecuresPositiveGround')
    r = 'F3: the determined process an exchange law generates (Law.process of its next-step map); "generation" is reserved'
    add(B + 'ExchangeLaw.generation', B + 'ExchangeLaw.process', 'decl', r, 'high', note='parallels Law.process')
    add(B + 'ExchangeLaw.generation_runs', B + 'ExchangeLaw.process_runs', 'decl', r + ' (family)')
    add(B + 'ExchangeLaw.courseWorld_generation', B + 'ExchangeLaw.courseWorld_process', 'decl', r + ' (family)')
    r = 'F3: SharedCodes.generation is the next cohort of codes (one step of the population map), not generation'
    add(B + 'SharedCodes.generation', B + 'SharedCodes.nextCohort', 'decl', r, 'high', note='F3 proposed `cohort`; the definition is the step map, so nextCohort')
    add(B + 'SharedCodes.generation_of_resolved', B + 'SharedCodes.nextCohort_of_resolved', 'decl', r + ' (family)')
    add(B + 'SharedCodes.every_generation_resolves', B + 'SharedCodes.every_cohort_resolves', 'decl', r + ' (family)')
    add(B + 'SharedCodes.generation_merges', B + 'SharedCodes.nextCohort_merges', 'decl', r + ' (family)')
    r = 'F3: "generation" here is a cohort of programs (`cohort p n`, already the definition\'s name); generation is reserved for widening'
    for a, b in [('every_generation_holds', 'every_cohort_holds'), ('every_generation_corresponds', 'every_cohort_corresponds'),
                 ('distinction_lost_every_generation', 'distinction_lost_every_cohort'), ('run_generation', 'run_cohort')]:
        add(B + 'ResponseLearning.' + a, B + 'ResponseLearning.' + b, 'decl', r, 'medium')
    r = 'F3: a witness of members each alive two steps under a lasting lineage formation; "generations" is the lineage sense, exact in biology but the reserved word'
    add(B + 'Generations', B + 'OverlappingLives', 'namespace', r, 'medium', note='optional; `Lineage` (Identity:1761) and `Succession` (Identity:1857) are taken. Theorem Generations.generations -> OverlappingLives.summary')
    fam(decls, lambda x: x['full'].startswith(B + 'Generations.'),
        lambda f: f.replace('Generations.generations', 'OverlappingLives.summary').replace('Generations.', 'OverlappingLives.'), r + ' (members)', 'medium')

    # ---------------- G0, g0_*, positive, PositiveGround, SelfGood ----------------
    r = 'F9: G0 is a retired label kept as a live definition; the definition is living significance on the frame'
    add(B + 'G0', B + 'LivingSignificance', 'decl', r, 'high', note='claim form stays Valuation.Significant; R34 may restate both')
    fam(decls, lambda x: re.search(r'(^|[._])g0(_|$)|_g0_|\.g0$|G0\.|g0Relevant', x['full']) and x['full'] != B + 'G0',
        lambda f: (f.replace('G0.', 'LivingSignificance.').replace('g0Relevant', 'livingSignificanceRelevant')
                   .replace('.g0_', '.livingSignificance_').replace('_g0_', '_livingSignificance_').replace('_g0', '_livingSignificance')
                   .replace('Valuation.g0', 'Valuation.livingSignificance').replace('PositiveGround.', 'SecuredContent.')
                   .replace('self_good_', 'selfSignificance_')),
        'F9: g0_* family named after the retired label', 'high')
    add('positive (binder, relevance sense)', 'relevance', 'binder',
        'F9: the chapter documents `positive` as "a parameter, not a valence": the name states what it does not mean', 'medium',
        note='rename only binders typed X -> Y -> Prop in G0/SecuresPositiveGround/articulates/PositionedArticulation and their users (~53 tokens in 8 modules); arithmetic `positive` (0 < k) stays. Frame.relevance is reached by dot notation, so a binder named relevance does not shadow it; check `open Frame` sites')
    r = 'F9: "positive ground" names what the definition calls content absent before, held by every admitted outcome; no valence'
    add(B + 'SecuresPositiveGround', B + 'SecuresNewContent', 'decl', r, 'medium', note='F9 wording; with positive -> relevance the body reads "some relevant content absent before"')
    add(B + 'securesPositiveGround_total', B + 'securesNewContent_total', 'decl', r + ' (family)', 'medium')
    add(B + 'PositiveGround', B + 'SecuredContent', 'module', r + '; module and namespace (67 declarations)', 'medium',
        note='namespace PositiveGround -> SecuredContent for every member; `positive_integral_*`, `positiveDomain` are arithmetic signs (> 0) and keep "positive"; `acquired_evidence_secures_good_and_leaves_both_opennesses` carries "good" (F10) -> `acquired_evidence_secures_content_and_leaves_both_opennesses`')
    fam(decls, lambda x: x['full'].startswith(B + 'PositiveGround.') and not re.search(r'g0|contingent_generation', x['full']),
        lambda f: f.replace('PositiveGround.', 'SecuredContent.').replace('secures_good_', 'secures_content_'),
        'F9: namespace PositiveGround -> SecuredContent (member)', 'medium')
    r = 'F8/F9: self-significance (glossary row) is the definition (own living claims significant from p); "good" states a valence it lacks'
    add(B + 'Valuation.SelfGood', B + 'Valuation.SelfSignificance', 'decl', r)
    add(B + 'ProfileReach.SelfGood', B + 'ProfileReach.SelfSignificance', 'decl', r)
    add(B + 'Valuation.seed_of_selfGood', B + 'Valuation.seed_of_selfSignificance', 'decl', r + ' (family)')
    add(B + 'ProfileReach.self_good_reaches_at_least_as_connected', B + 'ProfileReach.selfSignificance_reaches_at_least_as_connected', 'decl', r + ' (family)')
    add(B + 'ProfileReach.selfGood_valuation', B + 'ProfileReach.selfSignificance_valuation', 'decl', r + ' (family)')
    add(B + 'ProfileReach.threshold_selfGood', B + 'ProfileReach.threshold_selfSignificance', 'decl', r + ' (family)')

    # ---------------- other wrong meanings ----------------
    add(B + 'Coupling', B + 'MoveFormation', 'module', 'F9/D45(2): coupling (couples-into) is the primitive; this module is "where a move is formed"', 'high',
        note='namespace Becoming.Coupling (arith helpers, `alt`) moves with it')
    fam(decls, lambda x: x['full'].startswith(B + 'Coupling.'), lambda f: f.replace('Coupling.', 'MoveFormation.'),
        'F9: namespace of module Coupling (member)', 'high')
    add(B + 'Onward.DependentSelection', B + 'Onward.DependentChoice', 'decl', 'F1/F9: the definition is the dependent-choice principle (its docstring says so); "selection" is reserved for selection through couplings', 'high')
    add(B + 'Joining.Neutral', B + 'Joining.TwoSidedUnit', 'decl', 'F9/F12: Neutral is boundary neutrality (∀, Metaethics); this is a fragment leaving its partner unchanged on either side, beside LeftUnit', 'medium',
        note='"neutral element" is standard algebra; the collision is with the ethics word. `Unit` alone would shadow Lean\'s Unit')
    for a, b in [('Joining.Neutral.self', 'Joining.TwoSidedUnit.self'), ('Joining.neutral_transport', 'Joining.twoSidedUnit_transport'),
                 ('Joining.Neutral.of_iff', 'Joining.TwoSidedUnit.of_iff'), ('Joining.atMostOnce_neutral', 'Joining.atMostOnce_twoSidedUnit'),
                 ('Fragment.idle_neutral', 'Fragment.idle_twoSidedUnit'), ('Fragment.neutral_iff_idle', 'Fragment.twoSidedUnit_iff_idle'),
                 ('Fragment.neutral_stays_once', 'Fragment.twoSidedUnit_stays_once')]:
        add(B + a, B + b, 'decl', 'F12 (family)', 'medium')
    add(B + 'Clearing.free_rider_loses', B + 'Clearing.clearer_loses_dweller', 'decl', 'F9/F10: "free rider" is contest vocabulary failing D54\'s test; the theorem says the clearer\'s part loses the dweller under the continuation condition', 'high',
        note='F9 proposed nonDependent_loses; the witness\'s own roles state it exactly')
    add('Becoming.Metaethics (module header)', '"Valuation and significance on the Becoming spine"', 'docstring',
        'F9: header "The Universal Metaethical Core on the Becoming spine" is a retired label; module name kept', 'high',
        note='docstrings with N_rel/N_std/S0 (Metaethics:141, 152, 157 "S0 at a position", "N_rel\'s rule") also change by reading')

    # ---------------- namespace collisions (B13) ----------------
    r = 'B13: namespace holds unrelated witnesses; qualify by module (N3 rule)'
    coll = [('Crossing', 'Becoming.Order', 'Order.Crossing', 'exchange-order witness vs the dependence-outcome witness of Dependence/Labelled'),
            ('Arising', 'Becoming.Order', 'Order.Arising', 'Order witness; frees Becoming.Arising for the renamed module'),
            ('Halving', 'Becoming.Order', 'Order.Halving', 'stuttering witness vs LeastLoss\'s dyadic stock'),
            ('Cycle', 'Becoming.Gluing', 'Gluing.Cycle', 'parity cycle vs Flow/Population\'s renewers-as-takers'),
            ('Loop', 'Becoming.Weighted', 'Weighted.Loop', 'one configuration, two moves vs Response/Counterfactual/PoolResponse\'s loop'),
            ('Copying', 'Becoming.Pace', 'Pace.Copying', 'Pace\'s reading-step witness inside module Copying\'s namespace'),
            ('Settling', 'Becoming.Entropy', 'Entropy.Settling', 'one passing then rest vs module Settling'),
            ('Parting', 'Becoming.Likeness', 'Likeness.Parting', 'three-configuration witness vs module Parting'),
            ('Fork', 'Becoming.Identity', 'Identity.Fork', 'identity fork vs Unfolding\'s origin-and-two-ends process'),
            ('Circulation', 'Becoming.Labelled', 'Labelled.Circulation', 'one relatum round vs Resolution\'s fixed-size exchange')]
    for ns, mod, new, why in coll:
        add(B + ns + ' (in ' + mod + ')', B + new, 'namespace', r + ': ' + why, 'high', note='module=' + mod)
        fam(decls, lambda x, ns=ns, mod=mod: x['module'] == mod and (x['full'].startswith(B + ns + '.')),
            lambda f, ns=ns, new=new: f.replace(B + ns + '.', B + new + '.', 1), r + ' (member)', 'high')
    add(B + 'RuleCapture.Counts', B + 'RuleCapture.CarrierCounts', 'decl', 'G9: three Counts; this is two counts, carriers and others (others positive); root Counts (Decidedness) is the count relation and keeps its name', 'medium',
        note='G9 proposed ShareCounts; the fields are carrier/other. Namespace RuleCapture.Counts (38 members, incl. arithmetic lemmas) moves with it; the arithmetic lemmas go to Becoming.Prelude in R31')
    fam(decls, lambda x: x['full'].startswith(B + 'RuleCapture.Counts.'), lambda f: f.replace('RuleCapture.Counts.', 'RuleCapture.CarrierCounts.'), 'G9 (member)', 'medium')
    add(B + 'Countdown.Counts', B + 'Countdown.CountedWork', 'decl', 'G9: the structure is a specification of counted work (its docstring\'s words), not a count', 'medium')
    add(B + 'Counts', B + 'Counts', 'keep', 'G9: the general count relation (Decidedness:207); keeps the name the other two leave', 'high', False)
    add(B + 'SharedCodes.Image', B + 'SharedCodes.Relabels', 'decl', 'B3 (adjacent): a relation "Y is X with places permuted by π and forms renamed by τ", not an image; shares the name Image', 'medium')

    # ---------------- history / course (A10) ----------------
    add(B + 'Activation.History', B + 'Activation.TwoSteps', 'decl', 'A10: a two-step record (first event, middle, second event, final), not a history', 'high')
    add(B + 'Registration.History', B + 'Registration.AlikeUpTo', 'decl', 'A10: alike under every lumping drawn up to t (a relation), not a history', 'medium',
        note='A10 proposed AgreedThrough; Web.AlikeThrough (N5) is another notion. theorem history_keeps -> alikeUpTo_keeps. Namespace `Registration` is N1\'s retired word (study §7) and was left by N5: out of R30\'s list, noted')
    add(B + 'Registration.history_keeps', B + 'Registration.alikeUpTo_keeps', 'decl', 'A10 (family)', 'medium')
    add(B + 'Flow.history', B + 'Flow.exchangeCount', 'decl', 'A10: a number, the count of the family\'s exchanges over N steps from T; history is a sequence', 'medium',
        note='R5\'s records and chapter say "history grows"; keep that prose (the count measures the kept history) and cite exchangeCount')
    add(B + 'HistoryIdeals.History', B + 'HistoryIdeals.History', 'keep', 'A10 (?): a finite or infinite word, the base notion of history in ideal form; keep', 'high', False)
    for o, why in [('ExchangeLaw.history', 'the levels at each stage, a step-indexed sequence: history in the base sense'),
                   ('Viability.history', 'the states along moves, Nat -> S'), ('ContinuingRevision.history', 'a growing list of acts, a finite history'),
                   ('Parting.course', 'values of a run read through a map: the glossary\'s course'), ('Learnable.course', 'the same, along an orbit'),
                   ('LearnableRuns.course', 'the same, on runs'), ('Regulation.course', 'Nat -> Nat level sequence'),
                   ('RuleCapture.Alternating.course', 'Nat -> Counts x Counts sequence'), ('RuleCapture.Reversed.course', 'the same'),
                   ('RuleCapture.Second.course', 'the same'), ('ExchangeLaw.course', 'the law\'s flow along its levels; family with courseWorld/courseRun'),
                   ('Ranking.course', 'Course -> unfolding: each alternative whole course of the world; ported with Unfolding')]:
        add(B + o, B + o, 'keep', 'A10 listed 7 courses / 4 histories; ' + why + ' (F §2f #13: course = any step-indexed sequence)', 'high', False)

    # ---------------- Image (B3, owned by R29) ----------------
    add(B + 'Image', B + 'Readout.image', 'delete', 'B3: identical to Readout.image; R29\'s item ("Image removed"); listed so R30 does not rename it', 'high',
        note='users: Mechanism (factors_image, Image.least, image_determined_iff), LawAlongRun:160-180, Likeness:260-314; if R29 has not landed, R30 does it')
    # ---------------- Unfolding: port, not rename (board rule 8: deeper/RelationalRenewal.lean keeps its bytes) ----------------
    from parse import strip_comments as _sc
    for x in decls:
        t = _sc(x['text'])
        if re.search(r'(?<![\w.])Unfolding(?![\w.])', t) and not x['full'].startswith('Becoming.Web.static') and x['full'] != 'Becoming.Web.static':
            add(x['full'], 'restate over Web (U : W -> Web F C, or Web.static U at the call sites)', 'port',
                'F9/F §2f #1: `Unfolding` (RelationalRenewal:104) is a static-dependence record; the name states the theory\'s master term. Port through Dependence.static (Web.static) rather than rename', 'medium',
                note='proof work: Renewed/Dependent/ConsumingIn of RelationalRenewal are used on U; Web.static_renewed/_dependent/_consumingIn give the Web forms. Ranking/Relevance witnesses (`where level ... draws ...`) become Web literals with constant requires/need/draws')
    add('Becoming.Web.static (+ static_supported/_dependent/_renewed/_consumed/_renewingIn/_consumingIn)', 'unchanged (the bridge; 7 uses of Unfolding stay)', 'keep',
        'F9: Dependence.lean:232-260 is the static reading itself; it keeps the RelationalRenewal type by design', 'high', False)
    return E
