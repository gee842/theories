#!/usr/bin/env python3
"""The schema-2 record learnable-through-registration, before its receipt is known.

Imported by land_record.py, which fills the source hashes, the receipt and the review time, then installs it.
Public fields carry no work-item numbers, dates, receipts or section numbers (schema 2)."""
L = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
LEARNABLE = L + 'Learnable.lean'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-12-learning-wisdom-root-and-induction.md'
N = 'Becoming.Learnable.'


def p(zh, en, **kw):
    return {'zh': zh, 'en': en, **kw}


DECLS = [N + x for x in (
    'course', 'RestsFrom', 'Rests', 'records_same', 'claim_not_right_on_both', 'refuted_on_one',
    'agree_of_rests_both', 'not_rests_on_both', 'orbit_of_still', 'still_not_rests_on_both', 'still_lumped_of_rests',
    'rests_through', 'firstFit_congr', 'withWorldAt', 'withWorld', 'learnable_iff', 'learnable_of_lumped',
    'still_learnable_iff_lumped', 'Pair.still', 'Pair.stays', 'Pair.first_not_rests', 'Pair.not_lumped',
    'Pair.whole_rests')]

# Reused modules: (path, module, declarations reused)
REUSED = [
    (L + 'Learning.lean', 'Becoming.Learning',
     ['Becoming.Learning.record', 'Becoming.Learning.record_congr', 'Becoming.Learning.record_length',
      'Becoming.Learning.Refuted', 'Becoming.Learning.Lumped', 'Becoming.Learning.learner',
      'Becoming.Learning.lassos', 'Becoming.Learning.tri']),
    (L + 'Identification.lean', 'Becoming.Identification',
     ['Becoming.Identification.held_learner_rests', 'Becoming.Identification.record_eq_iff',
      'Becoming.Identification.firstFit', 'Becoming.Identification.firstFit_sound',
      'Becoming.Identification.firstFit_found', 'Becoming.Law.sameFuture_iff_below', 'Becoming.Law.name']),
    (L + 'Unfolding.lean', 'Becoming.Unfolding', ['Becoming.Law.SameFuture']),
    (L + 'Seeking.lean', 'Becoming.Seeking', ['Becoming.Law.fixed_rests']),
    (L + 'Recurrence.lean', 'Becoming.Recurrence', ['Becoming.Law.orbit']),
]


def dep(ident, path, detail, output, input_, conditions):
    return {'id': ident, 'relation': 'formal-reuse', 'detail': detail,
            'interface': {'output': output, 'input': input_, 'conditions': conditions, 'evidence': path}}


RECORD = {
    'schema_version': 2,
    'id': 'learnable-through-registration',
    'title': p('经其识所能学者', 'What a learner can learn through its registration'),
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': 'F11',
    'reviewed_at_utc': None,
    'statement': p(
        '所识的未来相同的配置给每个学习者同样的记录。被列表所持的世界中，某个学习者在每个配置上于目标静止，恰当这样的配置其目标从某步起一致；'
        '律使每个配置不变时，恰当目标经识同去。',
        'Configurations with the same registered future give every learner the same record. In a world a list holds, '
        'some learner rests on a target everywhere exactly where such configurations have targets agreeing from some '
        'step on; under a still law, exactly where it goes alike across the registration.'),
    'laws': [
        p('学习者从所识的记录主张目标：由配置出发之轨道的所识历程（course）；从第 T 步起每步主张目标即从 T 起静止（RestsFrom），'
          '某个 T 存在即静止（Rests）。',
          "A learner claims a target from the registered record: the registered course of a configuration's orbit "
          '(course); claiming the target at every step from T on is resting from T (RestsFrom), and resting is resting '
          'from some T (Rests).',
          declarations=[N + 'course', N + 'RestsFrom', N + 'Rests']),
        p('所识的未来相同的两个配置给每个学习者每一步同样的记录；所以在其目标不同之步，主张至多在一处对，不用判定；目标值可判定时，'
          '主张在一处被否证，而两处记录处处相同。',
          'Two configurations with the same registered future give every learner the same record at every step; so at a '
          'step where their targets differ a claim is right on at most one, with no decision, and with the target values '
          'decided a claim is refuted on one while the two records stay equal at every step.',
          declarations=[N + 'records_same', N + 'claim_not_right_on_both', N + 'refuted_on_one']),
        p('在两处都静止的学习者，其目标从某步起一致；所以目标在任意晚处不同时，没有学习者在两处都静止；律使两个配置不变、识不分辨它们而目标'
          '不同时即如此。',
          'A learner resting on both has targets agreeing from some step on; so where they differ at arbitrarily late '
          'steps no learner rests on both, already where the law leaves both configurations unchanged, the registration '
          'does not tell them apart and their targets differ.',
          declarations=[N + 'agree_of_rests_both', N + 'not_rests_on_both', N + 'orbit_of_still',
                        N + 'still_not_rests_on_both']),
        p('目标从所识读出时，读所识之值的套索假设学习者，其主张经读出，在被列表所持的世界中从辨识的界起静止；它不被给予配置、其数目或目标'
          '的任何值。',
          'Where the target is read off what is registered, the learner over the lasso hypotheses on the registered '
          'values, its claims read off, rests on the target in every world a list holds from the identification bound '
          'on; it is given neither the configurations, nor how many there are, nor any value of the target.',
          declarations=[N + 'rests_through']),
        p('恰当地：在被列表所持的世界中，某个读识的学习者在每个配置上静止，恰当所识的未来相同的配置其目标从某步起一致；必要一侧对每个'
          '学习者成立，充分一侧的学习者被给予世界与目标。',
          'Exactly: in a world a list holds, some learner reading the registration rests at every configuration exactly '
          'where configurations with the same registered future have targets agreeing from some step on; the necessary '
          'side holds of every learner, and the learner of the sufficient side is given the world and the target.',
          declarations=[N + 'learnable_iff', N + 'withWorld', N + 'withWorldAt', N + 'firstFit_congr']),
        p('经识同去的目标总可学；律使每个配置不变时，可学的恰是经识同去者。',
          'Targets going alike across the registration are learnable; under a law leaving every configuration '
          'unchanged, exactly those are.',
          declarations=[N + 'learnable_of_lumped', N + 'still_lumped_of_rests', N + 'still_learnable_iff_lumped']),
        p('两个坐标、律不变：识第一个坐标时，没有学习者在 (true, false) 与 (true, true) 两处都在第二个坐标上静止，第二个坐标不经第一个'
          '同去；识两个坐标时，套索学习者从第 2 步起静止。',
          'Two coordinates under a still law: registering the first, no learner rests on the second at both '
          '(true, false) and (true, true), the second not going alike across the first; registering both, the lasso '
          'learner rests from step 2.',
          declarations=[N + 'Pair.still', N + 'Pair.stays', N + 'Pair.first_not_rests', N + 'Pair.not_lumped',
                        N + 'Pair.whole_rests']),
    ],
    'hypotheses': [
        p('不加公理。所识值的可判定相等（DecidableEq R）只作为套索学习者与 withWorld 的条件，在 rests_through 的陈述与 learnable_iff '
          '的证明中；目标值的可判定相等（DecidableEq V）只在 refuted_on_one。',
          'No axiom. Decidable equality of registered values (DecidableEq R) appears only as a condition of the lasso '
          'learner and of withWorld, in the statement of rests_through and the proof of learnable_iff; decidable equality '
          'of target values (DecidableEq V) only in refuted_on_one.'),
        p('每条定理的条件写在其中：所识的未来相同；目标在任意晚处不同；轨道或世界被列表所持；目标从所识读出（val s = g (reg s)）；'
          '律使配置不变。',
          "Each theorem's conditions are written into it: the same registered future; targets differing at arbitrarily "
          'late steps; the orbit or the world held by a list; the target read off the registration (val s = g (reg s)); '
          'the law leaving configurations unchanged.'),
        p('learnable_iff 及其推论中配置在 Type 中（Identification.firstFit 的类型）；其余定理对任意宇宙成立。',
          'In learnable_iff and its corollaries the configurations live in Type (the type of Identification.firstFit); '
          'the other theorems hold in every universe.'),
    ],
    'does_not_show': [
        p('充分一侧的学习者被给予世界与目标；不被给予什么的学习者只对从现在所识读出的目标证明。',
          'The learner of the sufficient side is given the world and the target; a learner given nothing is shown only '
          'for targets read off the present registration.', kind='scope', witness=N + 'rests_through'),
        p('一般的律下，可学不推出经识同去：读出所识的下一值的目标可学而不必同去。',
          'Under a general law, learnable does not imply going alike across the registration: a target reading the next '
          'registered value is learnable without it.', kind='non-implication'),
        p('条件关于成对的配置，不是逐配置的；读出它需要知道世界。',
          'The condition is on pairs of configurations, not on each; reading it off needs the world.', kind='scope'),
        p('学习者仍须分辨所识的值；所识的值本身不被分辨时的学习没有陈述。',
          'The learner still tells registered values apart; learning where the registered values themselves are not '
          'told apart is not stated.', kind='scope'),
        p('与人的学习、神经网络、注意或感知阈限的对应不由此检查。',
          'No correspondence to human learning, neural networks, attention or perceptual thresholds is checked.',
          kind='correspondence'),
    ],
    'counterexamples': [
        {'path': LEARNABLE, 'detail': p(
            'Pair：识第一个坐标时，没有学习者在 (true, false) 与 (true, true) 两处都在第二个坐标上静止（Pair.first_not_rests）。',
            'Pair: registering the first coordinate, no learner rests on the second at both (true, false) and '
            '(true, true) (Pair.first_not_rests).')},
    ],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                            'names-provisional'],
    'validation_scope': p(
        'Lean 4.29.1 合并检查器实查（回执 @RECEIPT@）：Becoming.Learnable 的 23 项声明（17 项定理）公理报告为空；检查器并核对核心'
        '纯净。作者反审见研究；未经独立审查。',
        'Machine-checked by the consolidated Lean 4.29.1 checker (receipt @RECEIPT@): the 23 declarations of '
        'Becoming.Learnable, 17 of them theorems, have empty axiom reports; the checker verifies core purity. Author '
        'counterreview in the study; not independently reviewed.'),
    'next_delta': p(
        '不被给予世界、对每个可学目标静止的学习者，或其不存在的见证；不确定过程上与概率读法下的可学性；实际的识（阈值、注意）的实例；'
        'Ren 对“识为所学划界”这一读法的判断。',
        'A learner given nothing that rests on every learnable target, or a witness that none does; learnability over '
        'undetermined processes and on a probabilistic reading; instances for actual registrations (thresholds, '
        "attention); Ren's judgment on the reading that registration bounds what is learned."),
    'correspondence': p(
        'Ren 2026-10-12：“please, fully complete, 我觉得理更像是对结构和变化的规律的建模 finish wisdom root, and resolve the '
        'undissolved”。按否证学习的结果留下：识不分辨值时的学习没有陈述。本结果陈述它：经识，学习者所能学的，恰是所识的未来相同者'
        '从某步起一致之处。读法（AI 的，待 Ren）：识为所学划界；依 Ren 的读法，理是对结构与变化之规律的建模，这一建模经识被学到，正如它'
        '经识被检验；阈下的差别（依存而不观察的条件只以阈值被识）只在它在所识的未来中显现、或从目标中消失之处可学；识之外者只经扩大识'
        '到达：新的观察、他者之识。',
        'Ren, 12 October 2026: “please, fully complete, 我觉得理更像是对结构和变化的规律的建模 finish wisdom root, and resolve '
        'the undissolved”. Learning by refutation left learning where registration does not tell values apart '
        'unstated. This result states it: what a learner can learn through a registration is exactly where '
        'configurations with the same registered future agree from some step on. Readings (the AI\'s, pending Ren): '
        "registration bounds what is learned; on Ren's reading 理 is the modeling of the laws of structure and of "
        'change, and that modeling is learned through registration as it is tested through it; a difference below '
        'threshold (a condition depended on and not observed registers only whether it meets the need) is learnable '
        'only where it shows in the registered future or vanishes from the target; what lies beyond registration is '
        "reached only by widening it: new observation, another's registration."),
    'canonical_source': LEARNABLE,
    'aliases': ['learnability through registration', '经识的可学性'],
    'dependencies': [
        dep('learning-by-refutation', L + 'Learning.lean',
            p('复用 record、record_congr、record_length、Refuted、Lumped、learner、lassos 与 tri：学习者、记录、否证与归并。',
              'Reuses record, record_congr, record_length, Refuted, Lumped, learner, lassos and tri: the learner, the '
              'record, refutation and lumping.'),
            p('学习者与所识的记录；按否证学习；归并。', 'Learners and registered records; learning by refutation; lumping.'),
            p('经识的学习者在目标上静止。', 'A learner reading a registration resting on a target.'),
            p('套索学习者要所识的值可判定。', 'The lasso learner needs registered values decided.')),
        dep('identification-where-bounded', L + 'Identification.lean',
            p('复用 held_learner_rests（未给定界的学习者的静止之步）、Law.name、Law.sameFuture_iff_below、record_eq_iff、firstFit、'
              'firstFit_sound 与 firstFit_found。',
              'Reuses held_learner_rests (the step at which the learner not given the bound rests), Law.name, '
              'Law.sameFuture_iff_below, record_eq_iff, firstFit, firstFit_sound and firstFit_found.'),
            p('有界的记录确定所识的未来；未给定界的学习者的静止之步。',
              'A bounded record fixes the registered future; the step at which the learner not given the bound rests.'),
            p('从所识读出的目标在界内学到；被给予世界的学习者。',
              'A target read off the registration learned within the bound; the learner given the world.'),
            p('世界或轨道被列表所持。', 'The world or the orbit held by a list.')),
        dep('configurations-alike-by-relation', L + 'Unfolding.lean',
            p('复用 Law.SameFuture：所识的未来相同。', 'Reuses Law.SameFuture: the same registered future.'),
            p('所识的未来相同的配置。', 'Configurations with the same registered future.'),
            p('同样的记录。', 'The same record.'),
            p('无。', 'None.')),
        dep('seeking-boundary', L + 'Seeking.lean',
            p('复用 Law.fixed_rests：律不变的配置是它自己的轨道。',
              'Reuses Law.fixed_rests: a configuration the law leaves unchanged is its own orbit.'),
            p('不变的配置停在自身。', 'A still configuration stays.'),
            p('两个不变的配置。', 'Two still configurations.'),
            p('律使配置不变。', 'The law leaving the configuration unchanged.')),
        dep('recurrence-without-premise', L + 'Recurrence.lean',
            p('复用 Law.orbit。', 'Reuses Law.orbit.'),
            p('轨道。', 'Orbits.'),
            p('所识的历程。', 'Registered courses.'),
            p('无。', 'None.')),
    ],
    'related': [
        {'id': 'generalization-through-lumping', 'detail': p(
            '在不变的律下，可学的目标恰是经识同去者；推广所经的归并就是识所给的那一个。',
            'Under a still law, the learnable targets are exactly those going alike across the registration; the '
            'lumping generalization goes through is the one the registration gives.')},
        {'id': 'subthreshold-registration', 'detail': p(
            '依存而不观察的条件只以阈值被识；读于学习者，阈下的差别只在它在所识的未来中显现、或从目标中消失之处可学（读法）。',
            'A condition depended on and not observed registers only as a threshold; read for learners, a difference '
            'below threshold is learnable only where it shows in the registered future or vanishes from the target '
            '(a reading).')},
        {'id': 'wisdom-root-part-one', 'detail': p(
            '其学习一项读于识：学习者所能学的，不多于所识的未来所分辨者。',
            'Its learning clause read through registration: a learner learns no more than the registered future '
            'tells apart.')},
    ],
    'references': [],
    'proof_bindings': [],
    'history': [
        p('2026-10-14：新增，按 Ren 2026-10-12 的请求（学习、智慧之根、消解未消解者）；推进 learning-by-refutation 下一步中“识不分辨值时'
          '的学习”一项；研究 §116。',
          "14 October 2026: added under Ren's request of 12 October 2026 (learning, the wisdom root, resolving the "
          'undissolved); advances the item of learning-by-refutation\'s next step on learning where registration does '
          'not tell values apart; study section 116.'),
    ],
    'text_versions': [],
}
