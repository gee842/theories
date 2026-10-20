#!/usr/bin/env python3
"""R35 step 1: the move plans applied, from the plan rerun on head (rerun/plans, written by plan/scripts/make_moves.py
over rerun/data/refscan.json) with the decisions below. Writes plans/R35-B*.tsv for `research.py move`.

usage (from the checkout root): python3 -B moves_plan.py

Decisions (study section 226):
* B1: the E15 folds and moves (DAO, HANZI, PRE-QIN, WANG-YANGMING into CHINESE-SOURCES) are left: the ZH claim on the
  board reads HANZI's criteria and extends the RO map in CHINESE-SOURCES, so they are its files for now.
  NONINSTRUMENTAL-CONCERN and RELATIONS-ACROSS-SCALES (the plan's "judgment" rows) stay: chapter section 11 calls
  them current argument, and NONINSTRUMENTAL-CONCERN overlaps the Chinese chapters ZH reads.
  Five unmaintained Chinese editions whose English is canonical move (option A); ETHICAL-LEARNING.zh.md, the
  original Chinese text, stays.
* B3: ARGUMENTS-A-L and ARGUMENTS-M-Z move with --keep-references: the curated chain's page links them, so a
  generated stub takes the old path. THEORY-MAP, SESSION-RESULTS and the empty bridge group move.
* B4: as planned, the nineteenth review included (the twentieth supersedes it and R21 applied its fixes).
* B5: as planned; the kits of R28-R35, y1-changes, ro-relational-sources, zhonghua and the pinned kit are not in it.
* B7: _process/reading-notes moves. The untracked leftovers (_process/handoffs, .claude/tmp_done.txt, the two
  untracked kit folders) are not in this checkout; the coordinator removes them.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
RERUN = HERE / 'rerun/plans'
OUT = HERE / 'plans'
OUT.mkdir(exist_ok=True)
CH = 'theories/becoming/chapters/'
TH = 'theories/becoming/history/'
DATE = 'R35 (20 October 2026)'


def rows(name):
    lines = (RERUN / f'{name}.tsv').read_text().splitlines()[1:]
    return [tuple(l.split('\t')) for l in lines if l.strip()]


def write(name, entries):
    (OUT / f'{name}.tsv').write_text('old_path\tnew_path\treason\n' + ''.join('\t'.join(e) + '\n' for e in entries))
    print(name, len(entries))


SKIP_B1 = {'NONINSTRUMENTAL-CONCERN', 'RELATIONS-ACROSS-SCALES', 'DAO-AND-GENERATIVITY', 'HANZI-AND-THEORY-TREE',
           'PRE-QIN-AND-WENYAN', 'WANG-YANGMING'}
b1 = []
for o, n, why in rows('R35-B1-chapters'):
    if o.rsplit('/', 1)[1].split('.')[0] in SKIP_B1:
        continue
    b1.append((o, n, f'{DATE}, batch B1: {why}'))
for name, g in [('PRACTICAL-JUDGMENT.zh', 18), ('BASIC-CONFLICT-JUDGMENT.zh', 13), ('CHOICE-AND-GENERATIVE-CONTEXT.zh', 9),
                ('WISDOM-AND-CONTEXT.zh', 9), ('ALIGNMENT-DIRECTION.zh', 8)]:
    b1.append((CH + name + '.md', TH + name + '.md',
               f'{DATE}, batch B1: E5, an unmaintained Chinese edition (G0 {g} times) of a chapter whose English edition '
               'is canonical; a live document may be English only'))
write('R35-B1-chapters', b1)
write('R35-B2-reference', [(o, n, f'{DATE}, batch B2: {w}') for o, n, w in rows('R35-B2-reference')])
write('R35-B3-generated-keep', [(o, n, f'{DATE}, batch B3: {w}') for o, n, w in rows('R35-B3-generated-keep')])
write('R35-B3-generated', [(o, n, f'{DATE}, batch B3: {w}') for o, n, w in rows('R35-B3-generated')])
write('R35-B4-study', [(o, n, f'{DATE}, batch B4: {w}') for o, n, w in rows('R35-B4-study')])
write('R35-B5-kits', [(o, n, f'{DATE}, batch B5: {w}') for o, n, w in rows('R35-B5-kits')])
write('R35-B7-process', [(o, n, f'{DATE}, batch B7: {w}') for o, n, w in rows('R35-B7-process')])
