#!/usr/bin/env python3
"""Finish the P77 call-site/name delta after applying P58c; no theorem proposition changes.

Usage: python3 -B finish_listing.py ROOT
Touches only current Listing.lean and one stale backticked reference in Space.lean.
History and Learning's unrelated rest names are untouched. Run actual checks afterward.
"""
from pathlib import Path
import sys

import p58c_names as names


def once_or_done(text, before, after):
    if before not in text:
        assert after in text, before
        return text
    assert text.count(before) == 1, (before, text.count(before))
    return text.replace(before, after)


def listing_delta(text):
    text = names.rename(text)
    text = once_or_done(text,
        'dissipative.finite_ceases balances',
        'dissipative.finite_taking_not_recurring balances')
    text = once_or_done(text,
        '  and dissipation brings every world to rest where some list, repetition allowed, holds every\n'
        '  relatum (`World.Enumerated.not_recurring`).',
        '  and under balance, dissipation and embodied arising, neither arising nor ceasing recurs\n'
        '  where some list, repetition allowed, holds every relatum (`World.Enumerated.not_recurring`).')
    text = once_or_done(text,
        '/-- **With the unit fixed from some step on, taking from a closed family stops, however the\n'
        'family is listed** (`Flow.taking_not_recurring`). -/',
        '/-- **With the unit fixed from some step on, taking from a closed family does not recur, however\n'
        'the family is listed** (`Flow.taking_not_recurring`). -/')
    text = once_or_done(text,
        '/-- **Dissipation brings every enumerated world to rest**, with no listing once and no decided\n'
        'identity (`World.rests_unrefuted`): where the flow balances and dissipates and whatever arises is\n'
        'embodied, neither arising nor ceasing recurs. -/',
        '/-- **Neither arising nor ceasing recurs in an enumerated world** under balance, dissipation\n'
        'and embodied arising, with no listing once and no decided identity. The statement keeps this\n'
        'non-recurrence strength, obtained from `World.rests_unrefuted` by its proved consequence. -/')
    return text


def space_delta(text):
    return once_or_done(text, 'Each premise of `rests` is needed', 'Each premise of `rests_unrefuted` is needed')


def main():
    root = Path(sys.argv[1]).resolve()
    core = root / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
    edits = [(core / 'Listing.lean', listing_delta), (core / 'Space.lean', space_delta)]
    prepared = [(path, transform(path.read_text())) for path, transform in edits]
    for path, text in prepared:
        if text != path.read_text():
            path.write_text(text)
            print('updated', path.relative_to(root))
    print('P58c Listing names and call site prepared; statements unchanged; actual checks required')


if __name__ == '__main__':
    main()
