#!/usr/bin/env python3
"""R32: the source text of declarations, by full name (the R30 parser on this checkout).

usage: python3 -B decltext.py NAME ...   (prints each declaration's text)
As a module: `texts()` maps every full name to its parsed declaration (module, line, text, stmt, body)."""
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("r30parse", HERE.parent / "r30-names" / "parse.py")
parse = importlib.util.module_from_spec(spec)
spec.loader.exec_module(parse)
ROOT = Path(__file__).resolve().parents[6] / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'


def texts():
    out = {}
    for path in sorted(ROOT.glob('*.lean')):
        ds, _ = parse.parse(str(path))
        for d in ds:
            out.setdefault('Becoming.' + d['full'] if not d['full'].startswith('Becoming.') else d['full'], d)
    return out


if __name__ == '__main__':
    t = texts()
    for n in sys.argv[1:]:
        d = t.get(n)
        print('==', n, (d or {}).get('module'), (d or {}).get('line'))
        if d:
            print(d['text'].rstrip())
