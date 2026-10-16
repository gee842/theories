"""Sentence-level preservation check.

Usage (from v6.2/):
    python3 src/sentcheck.py OLD_FILE NEW_FILE [NEW_FILE ...] [--min 0.5] [--all]

Splits OLD_FILE (a keyed source or an assembled document) into sentences, and for each sentence of at least
eight content words reports the share of its word trigrams found anywhere in the NEW files taken together.
Sentences below --min (default 0.5) are printed as possibly lost, with their containment, so that each can be
adjudicated: kept in other words, moved (where), merged with another sentence (where), or deliberately dropped
(why). Markup, maths and citations are stripped before comparison. Pure standard library.
"""
import re, sys

def norm(s):
    s = re.sub(r'\$\$.*?\$\$', ' ', s, flags=re.S)
    s = re.sub(r'\$[^$]*\$', ' ', s)
    s = re.sub(r'\{\{[^}]*\}\}', ' ', s)
    s = re.sub(r'\[[^\]]*\]\([^)]*\)', ' ', s)
    s = re.sub(r'\[(?:def|val|thm|prem|obs|num|conj|rec|corpus)[^\]]*\]', ' ', s)
    return re.findall(r"[a-z0-9][a-z0-9'\-]*", s.lower())

def grams(ws, n=3):
    return {tuple(ws[i:i + n]) for i in range(len(ws) - n + 1)}

def sentences(text):
    text = re.sub(r'\$\$.*?\$\$', ' [eq] ', text, flags=re.S)
    out = []
    for block in re.split(r'\n\s*\n', text):
        b = block.strip()
        if not b or b.startswith('#') and '\n' not in b:
            continue
        b = re.sub(r'^\s*(?:>|\||[-*]|\d+\.)\s*', ' ', b, flags=re.M)
        for s in re.split(r'(?<=[.!?;:])\s+(?=[A-Z*(\[])', b):
            if len(norm(s)) >= 8:
                out.append(' '.join(s.split()))
    return out

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    mn = 0.5
    if '--min' in sys.argv:
        mn = float(sys.argv[sys.argv.index('--min') + 1])
        args = [a for a in args if a != str(mn) and a != sys.argv[sys.argv.index('--min') + 1]]
    show_all = '--all' in sys.argv
    old, new = args[0], args[1:]
    pool = set()
    for f in new:
        pool |= grams(norm(open(f).read()))
    sents = sentences(open(old).read())
    low = 0
    for s in sents:
        g = grams(norm(s))
        c = len(g & pool) / max(len(g), 1)
        if c < mn or show_all:
            low += c < mn
            print(f"{c:4.2f}  {s[:400]}")
    print(f"\n{len(sents)} sentences checked; {low} below {mn}", file=sys.stderr)

if __name__ == '__main__':
    main()
