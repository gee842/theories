#!/usr/bin/env python3
"""A1 (18 October 2026): the board at A1's landing. In "Decisions pending Ren" the rows Ren took on 18 October are
removed (R1, R2/R2b, P120, P123, P125, P126, P127, P130 twice, U, U2, I4b-4, whole-first-and-bounded-centers), the
D1-D39 row narrows to D-f (the brief's Part C) and the intro says the rows were removed; the A1 row moves to the history
file after M1's (board rule 4: landed rows move in the landing commit). Every edit must match exactly once; a board
already edited is left alone. usage (from the repository root): python3 -B apply_board.py"""
import sys

BOARD = '_process/BECOMING-WORKBOARD.md'
HIST = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
RF = 'research/2026-10-05-generative-foundation-review/root-foundation/'
BRIEF = RF + 'READINGS-PENDING-REN.md'

TAKEN = ['| R1 Interleavings: ', '| R2 CensusCounts and R2b CensusBinding: ', '| P120 Remainder: ', '| P123 Frequency: ',
         '| P125 Observation: ', '| P126 Tail: ', '| P127 Onward: ', '| P130, first reading: ', '| P130, second reading: ',
         "| U: the joins' readings ", "| U2: the periphery joins' readings ", '| I4b-4: readings of lifting ',
         '| whole-first-and-bounded-centers: ']
DF_OLD = '| D1-D39: whether Ren\'s 16 October "agree with other readings" ratifies all of them (R18 D-f); '
DF_NEW = ('| D-f (the brief\'s Part C): whether Ren\'s 16 October "agree with other readings" ratifies the readings of '
          'D1-D39 that Ren has not taken by name (R18 D-f). The brief recommends no blanket ratification: a reading of '
          'one of Ren\'s phrases waits on his word on that phrase, and a reading of a theorem is decided by argument | '
          f'[brief, Part C]({BRIEF}#c-the-register-itself-d-f-review-item-50); '
          f'[DELEGATED-CHOICES.md]({RF}DELEGATED-CHOICES.md) |')
INTRO = [('; A1 removes those rows when it lands.',
          '; A1 removed those rows when it landed: D1, D5, D22 and D39 are revised, and the rest are decided as D43 in '
          f'[DELEGATED-CHOICES]({RF}DELEGATED-CHOICES.md#d43-其余的待决读法--the-other-pending-readings).'),
         ('Also with Ren, from the old board (not readings): ',
          f'Also with Ren, from the old board (not readings; the brief\'s [Part D]({BRIEF}#d-waiting-on-ren-not-readings)): ')]
A1 = '| **A1: applying Ren\'s readings of 18 October** '
M1 = '| **M1: chapter §7, AI alignment, restated around 明 and pooled coupling** '
STATE = ('landed 2026-10-18 in the commit "A1 landing" (docs and records, no Lean: D1, D5, D22 and D39 revised and D43 '
         'added in DELEGATED-CHOICES, en + zh; the chapter\'s labels, readings, §8.3, §8.4 and glossary, with the Chinese '
         'edition\'s list of open readings and M1\'s line for §7; 19 records\' readings and labels; the board\'s register)')
FEEDS = ('Ren\'s answer → DELEGATED-CHOICES, chapter, records, register; N6 rebases over A1; the brief\'s Parts C and D '
         'stay with Ren; the generativity chain\'s change (review item 51) goes through its maintenance record, a '
         'separate step')


def one(lines, prefix, where):
    hits = [i for i, l in enumerate(lines) if l.startswith(prefix)]
    if len(hits) != 1:
        sys.exit(f'{where}: expected one line starting {prefix!r}, found {len(hits)}')
    return hits[0]


def main():
    board = open(BOARD, encoding='utf-8').read()
    if '; A1 removed those rows when it landed' in board:
        print('already edited', BOARD)
        return
    for old, new in INTRO:
        if board.count(old) != 1:
            sys.exit(f'{BOARD}: expected one match: {old!r}')
        board = board.replace(old, new)
    lines = board.split('\n')
    reg = lines.index('## Decisions pending Ren')
    for prefix in TAKEN:
        i = one(lines, prefix, BOARD)
        assert i > reg, prefix
        del lines[i]
    i = one(lines, DF_OLD, BOARD)
    lines[i] = DF_NEW
    i = one(lines, A1, BOARD)
    row = lines.pop(i)
    cells = row.split(' | ')
    assert len(cells) == 5 and cells[2] == 'claimed 2026-10-18', cells[2:]
    cells[0] = cells[0].replace('](../', '](../../../').replace('](research/', '](../../research/')
    cells[2], cells[4] = STATE, FEEDS + ' |'
    hist = open(HIST, encoding='utf-8').read().split('\n')
    j = one(hist, M1, HIST)
    hist.insert(j + 1, ' | '.join(cells))
    open(BOARD, 'w', encoding='utf-8').write('\n'.join(lines))
    open(HIST, 'w', encoding='utf-8').write('\n'.join(hist))
    print('edited', BOARD, 'and', HIST, '; rows removed', len(TAKEN))


if __name__ == '__main__':
    main()
