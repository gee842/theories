#!/usr/bin/env python3
"""O2 landing text, run after O1's apply_text.py on the same tree (O1 and O2 land together on one core checker run):
the study section, the chapter paragraph after O1's, the section 8.2 row "Origins and refutation" as O1 left it, the
section 9 receipt and connectivity sentences as O1 left them, the board row moved to the history file, and the queue
sentence. Every edit must match exactly once.

usage (from the checkout root to edit): python3 -B apply_text.py RECEIPT CONNECTIVITY_LOG O1_STUDY_SECTION
Prints the study section number."""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path.cwd()
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
BOARD = '_process/BECOMING-WORKBOARD.md'
HISTORY = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
MOD = 'Becoming.LimitVerification'
receipt_id, conn_log, n1 = sys.argv[1], sys.argv[2], int(sys.argv[3])


def edit(path, pairs):
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    for old, new in pairs:
        k = text.count(old)
        if k != 1:
            sys.exit(f'{path}: expected one match, found {k}: {old[:100]!r}')
        text = text.replace(old, new)
    p.write_text(text, encoding='utf-8')
    print('edited', path, len(pairs))


rec = json.loads((ROOT / PKG / 'becoming-checks' / receipt_id / 'verification.json').read_text())
core = [m for m in rec['modules'] if m['layer'] == 'core']
assert rec['status'] == 'passed' and rec['core_compiles_from_prelude'] and rec['source_unchanged_during_check']
assert not any(v for m in core for v in m['axiom_dependencies'].values())
mod = next(m for m in core if m['module'] == MOD)
n_mod_thm, n_mod_decl = mod['theorems'], len(mod['declarations'])
n_thm = sum(m['theorems'] for m in core)
t = Path(conn_log).read_text() if conn_log.startswith('/') else (ROOT / conn_log).read_text()
conn = json.loads(t[t.index('{'):t.rindex('}') + 1])
apart = sum(v for k, v in conn['classes'].items() if k.startswith('apart'))
assert conn['spine_theorems'] == n_thm, (conn['spine_theorems'], n_thm)
mod_apart = conn['apart_by_module'].get(MOD, [0])[0]
fmt = lambda n: f'{n:,}'

# Study section: right after O1's.
stext = (ROOT / STUDY).read_text(encoding='utf-8')
last = max(int(x) for x in re.findall(r'^## (\d+)\. ', stext, re.M))
assert last == n1 and stext.split('\n## ')[-1].startswith(f'{n1}. What a finite stretch verifies'), (last, n1)
N = n1 + 1
apart_text = (f'{apart} apart of {fmt(n_thm)}, none in the module' if mod_apart == 0 else
              f'{apart} apart of {fmt(n_thm)}, {mod_apart} in the module')
study = (HERE / 'study_o2.txt').read_text(encoding='utf-8')
study = (study.replace('{N}', str(N)).replace('{RECEIPT}', receipt_id).replace('{THEOREMS}', str(n_mod_thm))
         .replace('{DECLS}', str(n_mod_decl)).replace('{APART}', apart_text))
(ROOT / STUDY).write_text(stext.rstrip('\n') + '\n\n' + study.rstrip('\n') + '\n', encoding='utf-8')
print('appended', STUDY, 'section', N)
SA = '../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#'
ANCHOR_O1 = f'{SA}{n1}-what-a-finite-stretch-verifies-and-what-none-can-refute-o1'
ANCHOR_O2 = f'{SA}{N}-what-a-method-comes-to-say-in-the-limit-o2'

# Chapter.
para = (HERE / 'chapter_paragraph.txt').read_text(encoding='utf-8').strip('\n')
ANCHOR = 'Which readings of an actual inquiry are verifiable, refutable or dense depends on the process they are read on.\n'
OLD82 = ('| Origins and refutation | (Stated: what a finite stretch verifies, the open classes of histories, and the split '
         'of every reading into its hull and a remainder no stretch refutes, `Becoming.Verification`.) The first origin '
         'step where the gated determination is decided; readings verifiable or refutable in the limit, the next levels '
         'above open and closed classes, and where they meet the laws of learning and of settling. | ')
NEW82 = ('| Origins and refutation | (Stated: what a finite stretch verifies, the open classes of histories, and the split '
         'of every reading into its hull and a remainder no stretch refutes, `Becoming.Verification`; readings verified '
         'or refuted in the limit, settling verified there and refuted there by no method, recurrence the other way '
         'round, `Becoming.LimitVerification`.) The first origin step where the gated determination is decided; joins at '
         'the limit levels, and whether the diagonal laws need Markov\'s principle. | ')
OLD82R = '[what-a-finite-stretch-verifies](../results/records/what-a-finite-stretch-verifies.md) |'
NEW82R = ('[what-a-finite-stretch-verifies](../results/records/what-a-finite-stretch-verifies.md), '
          '[what-a-method-comes-to-say-in-the-limit](../results/records/what-a-method-comes-to-say-in-the-limit.md) |')
ch = (ROOT / CH).read_text(encoding='utf-8')
row = next(line for line in ch.split('\n') if line.startswith(OLD82))
assert row.endswith(OLD82R), row[-200:]
newrow = NEW82 + row[len(OLD82):-len(OLD82R)] + NEW82R
OLDINT = f' Rerun with O1 (receipt {receipt_id}), it counts '
NEWINT = f' Rerun with O1 and O2 (receipt {receipt_id}), it counts '
OLDINT2 = 'are registered (five interior lemmas whose run forms are stated, one restatement and one calibration).'
NEWINT2 = (OLDINT2[:-1] + (', and none of `Becoming.LimitVerification`\'s stands apart.' if mod_apart == 0 else
                           f', and {mod_apart} of `Becoming.LimitVerification`\'s stand apart.'))
OLDREC = (f'with O1 (`Becoming.Verification`, [study §{n1}]({ANCHOR_O1})) in the working tree.')
NEWREC = (f'with O1 and O2 (`Becoming.Verification`, [study §{n1}]({ANCHOR_O1}); `Becoming.LimitVerification`, '
          f'[study §{N}]({ANCHOR_O2})) in the working tree.')
edit(CH, [(ANCHOR, ANCHOR + '\n' + para + '\n'), (row, newrow), (OLDINT, NEWINT), (OLDINT2, NEWINT2),
          (OLDREC, NEWREC)])

# Board: the row moves to the history file; the queue sentence names the landing.
board = (ROOT / BOARD).read_text(encoding='utf-8')
history = (ROOT / HISTORY).read_text(encoding='utf-8')
lines = board.split('\n')
rows = [i for i, line in enumerate(lines) if line.startswith('| **O2: readings verified or refuted in the limit')]
assert len(rows) == 1, rows
row = lines.pop(rows[0])
cells = row.split(' | ')
assert len(cells) == 5, len(cells)
cells[2] = (f'landed 2026-10-19 with O1, core receipt `{receipt_id}`; {n_mod_thm} theorems in one core module, empty '
            f'axiom reports; record what-a-method-comes-to-say-in-the-limit; study §{N}')
row = ' | '.join(cells).replace('](../', '](../../../').replace('](research/', '](../../research/')
hist = history.split('\n')
stop = next((i for i, line in enumerate(hist) if line.startswith('## Lapsed claims')), len(hist))
lastrow = max(i for i, line in enumerate(hist[:stop]) if line.startswith('| **'))
hist.insert(lastrow + 1, row)
board = '\n'.join(lines)
OLDQ = f'; O1 landed, core receipt `{receipt_id}`, ahead of W2): W2 ('
assert board.count(OLDQ) == 1, 'queue sentence'
board = board.replace(OLDQ, f'; O1 and O2 landed, core receipt `{receipt_id}`, ahead of W2): W2 (')
(ROOT / BOARD).write_text(board, encoding='utf-8')
(ROOT / HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('board row moved; receipt', receipt_id, 'apart', apart, 'theorems', n_thm)
print('STUDY_SECTION', N)
