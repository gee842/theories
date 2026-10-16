#!/usr/bin/env python3
"""Insert P118's study section and English paragraph into BECOMING-RENEWAL-READING.md.

usage: python3 -B apply_study.py W

W is the checkout. The section goes before "## English summary"; the paragraph goes at the end of
the file. Each insertion asserts that the text is not already there, so a second run fails.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
W = Path(sys.argv[1]).resolve()
study = W / '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
section = (HERE / 'study.md').read_text()
paragraph = (HERE / 'study-en.md').read_text()
text = study.read_text()
assert section.splitlines()[0] not in text, 'the section is already there'
assert paragraph.splitlines()[0][:60] not in text, 'the paragraph is already there'
anchor = '\n## English summary\n'
assert text.count(anchor) == 1
text = text.replace(anchor, '\n' + section.rstrip('\n') + '\n' + anchor)
text = text.rstrip('\n') + '\n\n' + paragraph.rstrip('\n') + '\n'
study.write_text(text)
print('inserted section and paragraph')
