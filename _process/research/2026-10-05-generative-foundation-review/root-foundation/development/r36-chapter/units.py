"""R36: split a chapter edition into units (one heading, paragraph, bullet or table row each).

Each unit carries its section path, first line, the Lean names it cites (backticked spans that
look like identifiers), the records it links and whether it states something open. The
preservation audit (audit.py) reads these units; `--outline` prints a compact listing used while
restructuring.

Usage: python3 -B units.py CHAPTER.md [--outline] [--json OUT]
"""
import json
import re
import sys
from pathlib import Path

NAME = re.compile(r'`([^`\n]+)`')
REC = re.compile(r'results/records/([a-z0-9][a-z0-9-]*)\.md')
IDENT = re.compile(r"^[A-Za-z_][\w'.₀-₉αβγδεζηθικλμνξοπρστυφχψω]*$")
OPEN = re.compile(r'\*Open[:.*]|\bis open\b|\bstays open\b|\bremain(s)? open\b|\bopen target|\bnot yet\b|\bconjecture\b', re.I)


def names_in(text):
    out = []
    for m in NAME.finditer(text):
        s = m.group(1).strip()
        if IDENT.match(s) and not s.endswith('.md') and not s.endswith('.py') and not s.endswith('.json'):
            out.append(s)
    return out


def units(path):
    lines = Path(path).read_text().split('\n')
    sec = []
    lead = ''
    res = []
    buf, start = [], None

    def flush():
        nonlocal buf, start
        if buf:
            text = '\n'.join(buf)
            res.append({'line': start, 'section': ' / '.join(sec), 'lead': lead,
                        'first': text.strip()[:160], 'names': sorted(set(names_in(text))),
                        'records': sorted(set(REC.findall(text))), 'open': bool(OPEN.search(text)),
                        'bytes': len(text.encode())})
        buf, start = [], None

    for i, l in enumerate(lines, 1):
        h = re.match(r'^(#{1,4}) (.*)', l)
        if h:
            flush()
            depth = len(h.group(1))
            sec = sec[:max(depth - 2, 0)] + [h.group(2).strip()] if depth >= 2 else [h.group(2).strip()]
            lead = ''
            continue
        if not l.strip() or l.startswith('<a id='):
            flush()
            continue
        b = re.match(r'^\s*(?:[-*]|\d+\.)?\s*\*\*([^*]{2,120})\*\*', l)
        new_item = re.match(r'^\s*(?:[-*] |\d+\. |\| )', l)
        if new_item or b:
            flush()
        if b and not l.lstrip().startswith('|'):
            lead = b.group(1).strip().rstrip('.')
        if start is None:
            start = i
        buf.append(l)
    flush()
    return res


if __name__ == '__main__':
    src = sys.argv[1]
    us = units(src)
    if '--json' in sys.argv:
        Path(sys.argv[sys.argv.index('--json') + 1]).write_text(json.dumps(us, ensure_ascii=False, indent=1))
    if '--outline' in sys.argv:
        cur = None
        for u in us:
            if u['section'] != cur:
                cur = u['section']
                print(f'\n## {cur}')
            print(f"{u['line']:5d} {u['bytes']:6d}B [{u['lead'][:40]}] n={len(u['names'])} r={','.join(u['records'])[:200]}{' OPEN' if u['open'] else ''}")
    print(len(us), 'units', file=sys.stderr)
