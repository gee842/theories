#!/usr/bin/env python3
"""Z1 (19 October 2026): the opening takes the version 7 proposal's third-pass edits (oo) and (oo'), which Ren agreed to
(sources/15-codex-theory-conversations/2026-10-19-opening-v7.md: each lander applies its body edit and its note
together), and the AI-written notes [^aligned] and [^race] cite the record relative-position-is-zero-sum. Each edit
must match once. Run from the checkout root."""
P = 'theories/becoming/OPENING.md'
OLD = ('That a game of relative position is zero-sum is a matter of counting, not yet stated on the formal spine. '
       'That the present race ends badly even for its winner is a judgment.')
NEW = ('That a game of relative position is zero-sum is a counting law: for any amounts and any change of them, one '
       'part\'s rise in position is the rest\'s summed fall, and no change raises every part, even where every amount '
       'grows (`RelativePosition.change_balances`, `RelativePosition.not_all_rise`, `DrawingMore.grow_and_fall`, '
       '[record](results/records/relative-position-is-zero-sum.md)). That its winners lose is proved under a stated '
       'dependence: where a race draws a shared condition down jointly beyond its renewal, the renewal depends on that '
       'condition, and those ahead depend on it at a need above what the race leaves, the race ends them with the '
       'condition, whatever their position (`Flow.race_ends_greatest`). One ahead that does not depend on what it draws '
       'down can continue (`Clearing.greatest_continues`); what it loses then is a continuation with significance, '
       'which counts under the continuation condition and under no significance at all does not '
       '(`Clearing.loss_needs_significance`). That the present race draws down conditions its leaders depend on is the '
       'empirical premise of the entangled Earth; that it ends badly even for its winner is a judgment on that premise.')
OO = ('a zero-sum game of relative position, which, as I see it, all its winners will lose.[^aligned]',
      'a zero-sum game of relative position, which all its winners will lose wherever they live on what it draws '
      'down.[^aligned]')
OO2 = ('Each of us is rewarded for the move that takes all of us where none of us wants to go: where the whole gains '
       'nothing, every reward',
       'Each of us is rewarded for the move that takes all of us where none of us wants to go. A race of position '
       'cannot raise everyone, and where the whole gains nothing, every reward')
RACE = ('The theorem finds some such formation, not necessarily the one rewarded, and that the containing family gains '
        'nothing is its premise.',
        'The theorem finds some such formation, not necessarily the one rewarded, and that the containing family gains '
        'nothing is its premise. That a race of position cannot raise everyone needs no premise: for any amounts and '
        'any change of them, some part\'s position does not rise (`RelativePosition.not_all_rise`, '
        '[record](results/records/relative-position-is-zero-sum.md)).')
t = open(P).read()
for old, new in [(OLD, NEW), OO, OO2, RACE]:
    assert t.count(old) == 1, (old[:60], t.count(old))
    t = t.replace(old, new)
open(P, 'w').write(t)
print('opening note')
