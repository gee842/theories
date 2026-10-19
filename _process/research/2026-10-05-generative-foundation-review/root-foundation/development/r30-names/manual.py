#!/usr/bin/env python3
"""R30: the edits the compiler asked for after apply.py and positive.py (dot notation after an expression,
whose type the resolver cannot see), and docstrings changed by reading. Each is an exact replacement that must
match once (or `count` times). usage: python3 -B manual.py TREE"""
import sys
from pathlib import Path

TREE = Path(sys.argv[1]).resolve()
CORE = TREE / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
EDITS = [
    # (file, old, new, count)
    ('Restoration.lean', '(renewing t c (Or.inr drawn)).returns.not_consumed', '(renewing t c (Or.inr drawn)).restored.not_consumed', 1),
    # Docstrings by reading (twentieth review F3, F9, F10): the module headers and the definitions renamed.
    ('Arising.lean', '# Generation: arising, unceasing arising and renewal', '# Arising: unceasing arising and renewal', 1),
    ('Arising.lean', 'active after it (`Arises`). Generation is *unceasing* when', 'active after it (`Arises`). Arising is *unceasing* when', 1),
    ('Arising.lean', '/-- Generation does not cease: some formation arises at arbitrarily late steps. -/',
     '/-- Arising does not cease: some formation arises at arbitrarily late steps. -/', 1),
    ('Metaethics.lean', '# The Universal Metaethical Core on the Becoming spine', '# Valuation and significance on the Becoming spine', 1),
    ('Metaethics.lean', '/-- S0 at a position. -/', '/-- Self-significance at a position (S0): its own living claims have significance from it. -/', 1),
    ('Metaethics.lean', "/-- N_rel's rule. -/", '/-- The rule of relational neutrality (N_rel): significance passes along a formed relation to\nliving content. -/', 1),
    ('Metaethics.lean', "/-- N_std's rule. -/", '/-- The rule of standpoint neutrality (N_std): significance of living content holds from every\nstandpoint. -/', 1),
    ('Metaethics.lean', '/-- Every admitted outcome of the response holds positive content absent before it. -/',
     '/-- Every admitted outcome of the response holds relevant content absent before it. -/', 1),
    ('Metaethics.lean', 'secures positive\n    content from its standpoint', 'secures new\n    content from its standpoint', 1),
    ('Metaethics.lean', 'Living significance, C, D and the secured positive\nground are', 'Living significance, C, D and the secured new\ncontent are', 1),
    ('SecuredContent.lean', '# Certain positive ground with open future form, addressed to every situated position',
     '# Secured new content with open future form, addressed to every situated position', 1),
    ('SecuredContent.lean', 'A response secures positive ground at a visible scope where every admitted continuation holds\npositive content absent before it',
     'A response secures new content at a visible scope where every admitted continuation holds\nrelevant content absent before it', 1),
    ('SecuredContent.lean', '(the\nparameter is named `positive`, but the name carries no valence; read from significance it is\nsignificance from every standpoint);',
     '(the\nparameter `relevance` carries no valence; read from significance it is significance from every\nstandpoint);', 1),
    ('SecuredContent.lean', '/-! ## Positive ground on a frame -/', '/-! ## Secured content on a frame -/', 1),
    ('SecuredContent.lean', '/-- The reason this route supplies: access plus secured positive ground. -/',
     '/-- The reason this route supplies: access plus secured new content. -/', 1),
    ('Handoff.lean', '/-- **The producer\'s output is the formation premise of positive ground.**',
     '/-- **The producer\'s output is the formation premise of secured new content.**', 1),
    ('ActiveReading.lean', 'fall under the relevance `positive`, a parameter whose\n  name carries no valence', 'fall under `relevance`, a parameter whose\n  name carries no valence', 1),
    ('ActiveReading.lean', 'fall under the relevance `positive`; it says', 'fall under `relevance`; it says', 1),
    ('ActiveReading.lean', 'falls under the relevance `positive`. -/', 'falls under `relevance`. -/', 1),
    ('ValuationFrames.lean', 'falls under the\nrelevance `positive` there. The parameter\'s name carries no valence',
     'falls under the\nrelevance `relevance` there. The parameter carries no valence', 1),
    ('Relevance.lean', '“Positive relevance” names `LivingSignificance`\'s parameter\n`positive`; the name carries no valence.',
     '“Positive relevance” names `LivingSignificance`\'s parameter\n`relevance` (named `positive` before R30); it carries no valence.', 1),
    ('Significance.lean', '/-- The continuation condition counts what a free rider ends.', '/-- The continuation condition counts what the clearer\'s part ends.', 1),
    ('Significance.lean', '/-- Centers bounded by their dependence license the free rider and disagree.',
     '/-- Centers bounded by their dependence license the clearer\'s part and disagree.', 1),
    ('ProfileReach.lean', "# How a standpoint's own good reaches beyond its own region, through formed profiles",
     "# How a standpoint's self-significance reaches beyond its own region, through formed profiles", 1),
    ('ProfileReach.lean', 'a self-good grounded in persistence alone', 'a self-significance grounded in persistence alone', 1),
    ('ProfileReach.lean', '**Any monotone self-good standpoint here', '**Any monotone self-significant standpoint here', 1),
    ('ProfileReach.lean', 'step one binds a self-good\nled by formative contribution, not self-good as such.',
     'step one binds a self-significance\nled by formative contribution, not self-significance as such.', 1),
    ('../Becoming.lean', 'unceasing generation needs their renewal to recur; renewal does not\n  imply generation; substitution among unrenewed conditions defers the end; and\n  dissipation ends generation, while a closed cycle need not.',
     'unceasing arising needs their renewal to recur; renewal does not\n  imply arising; substitution among unrenewed conditions defers the end; and\n  dissipation ends unceasing arising, while a closed cycle need not.', 1),
    ('../Becoming.lean', '(L4): the Universal Metaethical Core: the premise card,', '(L4): valuation and significance: the premise card,', 1),
    ('../Becoming.lean', '(L4): certain positive ground with open future form: one response', '(L4): secured new content with open future form: one response', 1),
    ('../Becoming.lean', "(L4): how a standpoint's own good reaches beyond its own region", "(L4): how a standpoint's self-significance reaches beyond its own region", 1),
]
for f, old, new, n in EDITS:
    p = CORE / f
    s = p.read_text()
    k = s.count(old)
    assert k == n, (f, old, k)
    p.write_text(s.replace(old, new))
print(len(EDITS), 'edits')
