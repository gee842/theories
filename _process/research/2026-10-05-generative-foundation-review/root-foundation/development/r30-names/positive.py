#!/usr/bin/env python3
"""R30: the binder `positive` -> `relevance` where it is the relevance parameter (F9).

usage: python3 -B positive.py TREE

A declaration binds the relevance parameter when it has a binder `positive : ... → Prop` (explicit, implicit
or in a `∀ positive,` whose type is a relation). In such a declaration every code token `positive` becomes
`relevance`; the arithmetic `positive : 0 < k` of other declarations stays. A declaration that already uses a
bare `relevance` is reported, not changed. Docstrings change by reading."""
import re
import sys
from pathlib import Path

TREE = Path(sys.argv[1]).resolve()
CORE = TREE / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
START = re.compile(r"^(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable)\s+)*(?:theorem|def|abbrev|structure|instance|inductive|lemma|example)\b", re.M)
REL = re.compile(r"[({]\s*(?:[\w']+\s+)*positive(?:\s+[\w']+)*\s*:\s*[^(){}]*(?:\([^()]*\)[^(){}]*)*→\s*Prop\s*[)}]|∀\s+positive\s*,|∀\s+positive\s*:\s*[^,]*→\s*Prop")
TOK = re.compile(r"(?<![\w.'])positive(?![\w'])")


def code_spans(text):
    """Offsets of code (outside comments and strings)."""
    out, i, n, start = [], 0, len(text), 0
    while i < n:
        if text.startswith('--', i):
            out.append((start, i)); j = text.find('\n', i); i = start = (n if j < 0 else j)
        elif text.startswith('/-', i):
            out.append((start, i)); d, j = 1, i + 2
            while j < n and d:
                if text.startswith('/-', j): d += 1; j += 2
                elif text.startswith('-/', j): d -= 1; j += 2
                else: j += 1
            i = start = j
        elif text[i] == '"' and (i == 0 or text[i - 1] != "'"):
            out.append((start, i)); j = i + 1
            while j < n and text[j] != '"':
                j += 2 if text[j] == '\\' else 1
            i = start = j + 1
        else:
            i += 1
    out.append((start, n))
    return out


report = {'changed': {}, 'skipped': []}
for p in sorted(CORE.glob('*.lean')):
    text = p.read_text()
    spans = code_spans(text)
    code = ''.join(text[a:b] if True else '' for a, b in spans)
    # declaration chunks over the original text: from one START in code to the next
    starts = [m.start() for m in START.finditer(text) if any(a <= m.start() < b for a, b in spans)]
    # variable lines can bind it too
    starts += [m.start() for m in re.finditer(r'^variable\b', text, re.M)]
    starts = sorted(set(starts)) + [len(text)]
    edits = []
    for s, e in zip(starts, starts[1:]):
        chunk_code = ''.join(text[max(a, s):min(b, e)] for a, b in spans if a < e and b > s)
        if not REL.search(chunk_code):
            continue
        if re.search(r"(?<![\w.'])relevance(?![\w'])", chunk_code):
            report['skipped'].append(f'{p.name}:{text.count(chr(10), 0, s) + 1}')
            continue
        for a, b in spans:
            a2, b2 = max(a, s), min(b, e)
            if a2 >= b2:
                continue
            for m in TOK.finditer(text, a2, b2):
                edits.append(m.start())
    if edits:
        out, last = [], 0
        for o in sorted(set(edits)):
            out.append(text[last:o]); out.append('relevance'); last = o + len('positive')
        out.append(text[last:])
        p.write_text(''.join(out))
        report['changed'][p.name] = len(set(edits))
print(report, sum(report['changed'].values()))
