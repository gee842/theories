"""U2 (17 October 2026): retired labels in the spine's Lean docstrings and comments, replaced by the current terms.

usage: python3 -B relabel_docstrings.py [--apply] FILE ...

Edits only comment text (`/- ... -/`, `/-- ... -/`, `/-! ... -/`, `-- ...`) of Lean files, never code or names; with a
`.py` file, only the string literals of `SCOPE`. The map follows the chapter's glossary (retired labels, 17 October):
G0 -> living significance, the one axiom / the axiom (`Unrestricted`) -> the continuation condition, Part I -> the theory
without axiom, Part II -> the conditional section (chapter section 6.15). Backticked identifiers (`G0`,
`GenerativeComparison.G0`) stay: they name declarations. Text inside quotation marks (Ren's words) is not touched.
"""
import re
import sys
from pathlib import Path

PROTECT = [r'axiom reports?', r'axiom of (?:dependent )?choice', r'axioms\b', r'`[^`]*`', r'“[^”]*”', r'"[^"]*"']
RULES = [
    (r"\bwith G0's(\s+)unindexed significance", r"with living significance read\1with unindexed significance"),
    # Historical narration first: Ren's acts keep their dates, in the current terms.
    (r"Ren folded Part II into Part I as one conditional section", "Ren folded what was \u27e6\u2461\u27e7 into the theory without axiom as one conditional section"),
    (r"Ren folded Part II\b", "Ren folded what was \u27e6\u2461\u27e7"),
    (r"into Part I as that conditional section", "into the theory without axiom as that conditional section"),
    (r"with no axiom in Part I and a theorem of the axiom in Part II", "with no axiom in the theory without axiom and a theorem of the continuation condition in the conditional section"),
    (r"Ren proposed one axiom:", "Ren proposed what is now the continuation condition:"),
    (r"ends with one axiom:", "ends with what is now the continuation condition:"),
    (r"aim first for the route with one axiom", "aim first for the route under the continuation condition"),
    (r"to add this axiom after it", "to add this condition after it"),
    (r"Ren's one axiom", "Ren's proposal, the continuation condition,"),
    (r"The one-axiom case\.", "The case of the continuation condition."),
    (r"the one axiom, the condition of chapter §6\.15 \(not asserted\)", "the continuation condition, the condition of chapter §6.15 (not asserted)"),
    (r"The one axiom, the condition of chapter §6\.15 \(not asserted\)", "The continuation condition, the condition of chapter §6.15 (not asserted)"),
    (r"the one axiom\b", "the continuation condition"),
    (r"The one axiom\b", "The continuation condition"),
    (r"one axiom\b", "the continuation condition"),
    (r"the axiom of `Becoming\.Significance`", "the continuation condition of `Becoming.Significance`"),
    (r"\bthe axiom's condition on\b", "the continuation condition on"),
    (r"\bWith the axiom as a condition\b", "With the continuation condition supplied"),
    (r"\bwith the axiom as a condition\b", "with the continuation condition supplied"),
    (r"\bthe axiom's\b", "the continuation condition's"),
    (r"\bThe axiom's\b", "The continuation condition's"),
    (r"\bthe axiom\b", "the continuation condition"),
    (r"\bThe axiom\b", "The continuation condition"),
    (r"\bthis axiom\b", "this condition"),
    (r"\bthe results of Part I\b", "the results of the theory without axiom"),
    (r"\bwithin Part I\b", "within the theory without axiom"),
    (r"\bthat Part I's\b", "that the theory without axiom's"),
    (r"\bin Part I\b", "in the theory without axiom"),
    (r"\bPart I\b", "the theory without axiom"),
    (r"\bPart II\b", "the conditional section"),
    (r"\bG0's uses\b", "the uses of living significance"),
    (r"\bG0's\b", "living significance's"),
    (r"\bRen folded G0\b", "Ren folded living significance (\u27e6\u2460\u27e7)"),
    (r"\bG0\b", "living significance"),
]


SENTINELS = {'\u27e6\u2461\u27e7': 'Part II', '\u27e6\u2460\u27e7': '`G0`'}
START = re.compile(r'((?:^|[.!?]\s+|/--\s*|/-!\s*(?:#+\s*)?|\*\*|\n\s*[-*]\s+|^\s*[-*]\s+|#\s+))(living significance|the continuation condition|the theory without axiom|the conditional section)')


def capitalize(text):
    return START.sub(lambda m: m.group(1) + m.group(2)[0].upper() + m.group(2)[1:], text)


def relabel(text):
    """Apply RULES to prose, leaving PROTECT spans as they are."""
    parts = re.split('(' + '|'.join(PROTECT) + ')', text)
    out = []
    for i, part in enumerate(parts):
        if part is None:
            continue
        if i % 2 == 1 or re.fullmatch('|'.join(PROTECT), part or ''):
            out.append(part)
            continue
        for pat, rep in RULES:
            part = re.sub(pat, rep, part)
        out.append(part)
    text = capitalize(''.join(out))
    for k, v in SENTINELS.items():
        text = text.replace(k, v)
    return text


def comment_spans(src):
    """Spans of Lean comment text (block comments nest; strings are skipped)."""
    spans, i, n = [], 0, len(src)
    while i < n:
        if src.startswith('/-', i):
            depth, j = 1, i + 2
            while j < n and depth:
                if src.startswith('/-', j):
                    depth, j = depth + 1, j + 2
                elif src.startswith('-/', j):
                    depth, j = depth - 1, j + 2
                else:
                    j += 1
            spans.append((i, j))
            i = j
        elif src.startswith('--', i):
            j = src.find('\n', i)
            j = n if j < 0 else j
            spans.append((i, j))
            i = j
        elif src[i] == '"':
            j = i + 1
            while j < n and src[j] != '"':
                j += 2 if src[j] == '\\' else 1
            i = j + 1
        else:
            i += 1
    return spans


def scope_spans(src):
    start = src.index('\nSCOPE = (')
    end = src.index('\n)\n', start)
    return [m.span() for m in re.finditer(r'"(?:[^"\\]|\\.)*"', src[start:end])] and \
        [(start + a, start + b) for a, b in (m.span() for m in re.finditer(r'"(?:[^"\\]|\\.)*"', src[start:end]))]


def process(path):
    src = path.read_text()
    spans = scope_spans(src) if path.suffix == '.py' else comment_spans(src)
    out, last = [], 0
    for a, b in spans:
        out.append(src[last:a])
        seg = src[a:b]
        if path.suffix == '.py':
            seg = '"' + relabel(seg[1:-1]) + '"'
        else:
            seg = relabel(seg)
        out.append(seg)
        last = b
    out.append(src[last:])
    return src, ''.join(out)


if __name__ == '__main__':
    apply = '--apply' in sys.argv
    for f in [a for a in sys.argv[1:] if a != '--apply']:
        p = Path(f)
        old, new = process(p)
        if old != new:
            print(p, sum(1 for a, b in zip(old.split('\n'), new.split('\n')) if a != b), 'lines')
            if apply:
                p.write_text(new)
