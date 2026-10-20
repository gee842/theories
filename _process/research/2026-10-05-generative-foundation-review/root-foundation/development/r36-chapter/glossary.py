"""R36: build the glossary's index of formal terms (§10 b) and carry its vocabulary tables.

Reads the glossary table of the frozen edition and writes, for every row whose term is not one of
the core terms of §10 (a) (CORE below), one index row: the term with its Chinese name, the first
sentence of its meaning (section references renumbered to the new chapter, old labels left as the
table had them) and its Lean anchor. Rows naming the same notion are merged (MERGE). The retired
labels, the two tables of retired Lean names and the two crosswalks are copied with section
references renumbered (`renumber`).

Usage: python3 -B glossary.py OLD_CHAPTER.md OUT.md
"""
import re
import sys
from pathlib import Path

# Old glossary terms (first cell, up to the Chinese name) covered by the core terms of §10 (a).
CORE = {
    'Becoming', '生生', 'process', 'frame', 'run', 'world', 'exchange', 'flow', 'web of dependence',
    'renewing / consuming', 'arising', 'ceasing', 'coming to rest', 'openness', 'dissipation', 'census',
    'fed from beyond', 'joint excess', 'roles', 'admission', 'margin', 'widens / keeps the same / mixed',
    'generative / degenerative', 'widens / narrows / mixed', 'significance', 'living significance',
    'continuation condition; unrestricted significance', 'boundary-invariant / standpoint-invariant',
    'presupposition', 'feeding closure', 'influence closure', 'reach closure', 'coupling closure', 'system',
    'selection through the couplings', 'carried amount', 'loop, of couplings', '理 (modeling of laws)', '识 (shí)',
    '明 (seeing, clarity)', '无明 (not-seeing)', 'lifting rule', 'law shown',
}

# Section numbers of the frozen edition -> the restructured chapter.
SECTION = {
    '6.1': '6.2', '6.2': '6.2', '6.3': '6.2', '6.4': '6.2', '6.5': '6.5', '6.6': '6.5', '6.7': '6.2',
    '6.8': '6.4', '6.9': '6.3', '6.10': '6.3', '6.11': '6.5', '6.12': '6.4', '6.13': '6.1', '6.14': '6.1',
    '6.15': '6.4',
}


def renumber(text):
    def sub(m):
        word, num = m.group(1), m.group(2)
        return word + SECTION.get(num, num)
    text = re.sub(r'(§|section |sections )(6\.1[0-5]|6\.[1-9])(?!\d)', sub, text)
    return text


def term_key(cell):
    """The term without its Chinese name in parentheses, for matching CORE."""
    if cell in CORE:
        return cell
    return re.sub(r'\s*\([^()]*\)\s*$', '', cell).strip()


def first_sentence(text):
    """The meaning's first sentence; a sentence ends at '. ' outside parentheses and backticks."""
    depth, tick = 0, False
    for i, ch in enumerate(text):
        if ch == '`':
            tick = not tick
        elif not tick and ch in '(（':
            depth += 1
        elif not tick and ch in ')）':
            depth = max(depth - 1, 0)
        elif not tick and depth == 0 and ch == '.' and (i + 1 == len(text) or text[i + 1] == ' '):
            return text[:i + 1]
    return text


def rows(lines):
    for l in lines:
        if l.startswith('| ') and not l.startswith('|---'):
            yield [c.strip() for c in l.strip().strip('|').split(' | ')]


def build(old):
    lines = old.split('\n')
    start = next(i for i, l in enumerate(lines) if l.startswith('## 10. Glossary'))
    retired = next(i for i, l in enumerate(lines) if l.startswith('### Retired labels'))
    end = next(i for i, l in enumerate(lines) if l.startswith('## 11.'))
    table = [r for r in rows(lines[start:retired]) if r[0] != 'Term (Chinese name)']
    out, seen = [], set()
    for r in table:
        term, meaning, lean = r[0], r[1], (r[2] if len(r) > 2 else '—')
        key = term_key(term)
        if key in CORE or term in CORE:
            continue
        if key in seen:
            continue
        seen.add(key)
        out.append(f'| {term} | {renumber(first_sentence(meaning))} | {lean} |')
    tail = lines[retired:end]
    # the retired tables and crosswalks keep their rows; headings become (c)/(d) subsections
    text = '\n'.join(tail)
    text = text.replace('### Retired labels', '<a id="retired-labels"></a>\n### (c) Retired labels and Lean names')
    text = text.replace('### Retired Lean names (18 October 2026)', '<a id="retired-lean-names-18-october-2026"></a>\n**Retired Lean names (18 October 2026).**')
    text = text.replace('### Retired Lean names (20 October 2026)', '<a id="retired-lean-names-20-october-2026"></a>\n**Retired Lean names (20 October 2026).**')
    text = text.replace('### Crosswalk to the corpus glossary', '<a id="crosswalk-to-the-corpus-glossary"></a>\n### (d) Crosswalk to the corpus glossary')
    text = text.replace('### Closing and opening: a crosswalk', '<a id="closing-and-opening-a-crosswalk"></a>\n### (e) Closing and opening: a crosswalk')
    return out, renumber(text), len(table)


if __name__ == '__main__':
    old = Path(sys.argv[1]).read_text()
    index, tail, n = build(old)
    body = ['| Term (Chinese name) | Meaning | Lean anchor |', '|---|---|---|'] + index
    Path(sys.argv[2]).write_text('\n'.join(body) + '\n\n<!-- tail -->\n' + tail + '\n')
    print(f'{n} rows in the frozen glossary; {len(index)} in the index; {n - len(index)} covered by core terms or merged', file=sys.stderr)
