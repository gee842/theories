"""R36: the board at landing. The Queue line, the R28-R36 row's state, and R36's sub-row in the board history
file after R35's. Each edit asserts the text it replaces occurs exactly once. Usage: python3 -B board_r36.py BASE"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
BASE = sys.argv[1]
BOARD = ROOT / '_process/BECOMING-WORKBOARD.md'
HIST = ROOT / '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'

SUMMARY = ('the chapter once, no Lean and no checker run, study §227, sub-row in the history file; preface, premise '
           'card, body in argument order with "In words." at each section, §6 in five sections, a generated theorem '
           'map of all 282 records with their standing and premises, §8.1 ranked, glossary of core terms with an '
           'index and the retired labels, the Chinese edition mirroring every heading; the 20 October editions '
           'frozen in history with every anchor kept as an alias and the preservation audit passing; the decision '
           'register\'s change clauses restated as conditions in the work')


def replace_once(path, old, new):
    text = path.read_text()
    assert text.count(old) == 1, (path, old[:80], text.count(old))
    path.write_text(text.replace(old, new))


def main():
    board = BOARD.read_text()
    q = [l for l in board.split('\n') if l.startswith('- **Queue:** R36 at the head')]
    assert len(q) == 1
    replace_once(BOARD, q[0], '- **Queue:** empty; R36 landed (' + SUMMARY + '); R35b, the instance and applications '
                 'ring, stays open with its blocker.')
    replace_once(BOARD, '; R36 next | worktrees per item',
                 '; R36 landed (' + SUMMARY + '); the programme is complete except R35b | worktrees per item')
    hist = HIST.read_text()
    r35 = [l for l in hist.split('\n') if l.startswith('| **R35: corpus and records**')]
    assert len(r35) == 1
    row = (
        '| **R36: the chapter, once** (twentieth review step 6, the last of its programme; F1, F10, F11, F12). '
        'The canonical chapter restructured reader-first: preface (one sentence, four standings, where the ethics '
        'is, central results, two targets, scope); §0 the premise card; §1–§7 the body once in argument order, each '
        'section opening "In words." with a few named theorems; §6 in five sections, "instantiation" said once, the '
        'ethics with its two premises in their two roles (the condition fixes scope, C fixes order); the theorem '
        'map, generated (`assemble.py`): all 282 records with standing, the premises of §0 in their hypotheses and '
        'the section stating them; §8.1 twelve ranked items; §9 receipt `20261020T005554.047169Z`, the layers.py '
        'pointer and the 217 Lean files the argument cites (`modules.py`); §10 core terms, an index of formal terms, '
        'the retired labels and Lean names; §11 with the frozen edition. The ZH edition mirrors every heading and '
        'anchor, states each section\'s point and links the English for theorems; the dangling §8.6 reference fixed. '
        'Old editions frozen to `theories/becoming/history/THE-THEORY-OF-BECOMING-2026-10-20(.zh).md` '
        '(receipt `_process/architecture/moves/R36-chapter.json`); every old anchor an alias; preservation audit '
        '(`audit.py`) passing for EN and ZH. 12 records re-pointed by content to the new numbering with history '
        'notes, 166 by hash (`repoint.py`, one log line); the goal\'s premises; OPENING\'s footnotes only (13 links); '
        '35 links in live chapters, the configuration\'s open-programme anchors, `indexes.py`, `navigation.py`. '
        'DELEGATED-CHOICES EN and ZH (F11): 37 change clauses each naming a condition in the work, §0 restated, D14 '
        'and D34 fixed, retired vocabulary in 7 and 6 headings (old slugs kept) and five index rows, notes after D10, '
        'D11 and D20; no decision changed. F12 needed no Lean (`Joining.Neutral` was renamed `TwoSidedUnit` by R30). '
        '| Claude Code session of 20 October (R28-R36 programme) '
        f'| landed 2026-10-20 on `{BASE}`: no Lean changed, no checker run (latest core receipt R34\'s '
        '`20261020T005554.047169Z`); render, check, links and tests pass; no chain source newly pending (120 before); '
        'study §227 '
        '| worktree `.claude/worktrees/agent-a7da58d3e2d03563d`, kit `development/r36-chapter/` '
        '| a chapter read once, with a theorem map → the programme complete except R35b; CHINESE-SOURCES\' tables '
        'and AGENTS.md keep old-anchor citations, which resolve as aliases |')
    replace_once(HIST, r35[0] + '\n', r35[0] + '\n' + row + '\n')
    print('board updated')


if __name__ == '__main__':
    main()
