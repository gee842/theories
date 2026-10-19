#!/usr/bin/env python3
"""Y2b (19 October 2026): put the paragraph on the earlier work on the places into study section 195 of the current
tree, taking its text from the ready commit, so the item can be re-landed on a main that has moved. It stops, writing
nothing, where section 195 no longer has the place the paragraph goes. usage (from the checkout's root):
python3 -B apply_earlier.py READY_COMMIT"""
import subprocess, sys
from pathlib import Path

STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
START = '**Earlier work.** The earlier 生生不息 repository'
NOT_DONE = "**Not done.** 王弼's 《周易略例》 is not preserved here"
OLD = 'the line texts, the 大象 and the 文言 are not censused; an independent review.'
NEW = 'the line texts, the 大象 and the 文言 are not censused; the censuses of the sixty-four by each count (above); an independent review.'

ready = subprocess.run(['git', 'show', f'{sys.argv[1]}:{STUDY}'], capture_output=True, text=True, check=True).stdout
para = ready[ready.index(START):ready.index(NOT_DONE)]
t = Path(STUDY).read_text(encoding='utf-8')
assert START not in t, 'the paragraph is already in the study'
section = t.index('## 195. The relations of the places in the Changes (Y2)')
assert t.count(NOT_DONE) == 1 and t.index(NOT_DONE) > section, 'the place for the paragraph has changed'
assert t.count(OLD) == 1 and t.index(OLD) > section, 'the not-done line of section 195 has changed'
t = t.replace(NOT_DONE, para + NOT_DONE).replace(OLD, NEW)
Path(STUDY).write_text(t, encoding='utf-8')
print('section 195: earlier work added,', len(para), 'characters')
