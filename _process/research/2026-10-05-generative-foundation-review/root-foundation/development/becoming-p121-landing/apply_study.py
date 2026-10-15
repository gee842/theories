#!/usr/bin/env python3
"""Insert the P121 and P122 study sections and their English paragraphs into BECOMING-RENEWAL-READING.md.

usage: python3 -B apply_study.py W

W is the checkout, with P120's section in place. The sections go before "## English summary", P121's
first; the paragraphs go at the end of the file. Each insertion asserts that the text is not already
there, so a second run fails.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
W = Path(sys.argv[1]).resolve()
study = W / '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
sections = [(HERE / name).read_text() for name in ('study-p121.md', 'study-p122.md')]
paragraph = (HERE / 'study-en.md').read_text()
text = study.read_text()
for section in sections:
    assert section.splitlines()[0] not in text, 'a section is already there'
assert paragraph.splitlines()[0][:60] not in text, 'the paragraph is already there'
anchor = '\n## English summary\n'
assert text.count(anchor) == 1
text = text.replace(anchor, '\n' + '\n'.join(s.rstrip('\n') + '\n' for s in sections) + anchor)
text = text.rstrip('\n') + '\n\n' + paragraph.rstrip('\n') + '\n'
study.write_text(text)
print('inserted sections and paragraphs')
