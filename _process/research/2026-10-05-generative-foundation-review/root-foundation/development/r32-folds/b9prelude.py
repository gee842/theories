#!/usr/bin/env python3
"""R32 (B9 remainder): the same-statement groups no member of which lay below the others, where the
statement names nothing but the prelude's types (Init): one name is kept and stated in
`Becoming.Prelude`, under its full name; the others are removed and their uses point at it.

usage: python3 -B b9prelude.py removals.json DUMP.json plan     (writes b9-prelude.json: the rows)
       python3 -B b9prelude.py removals.json DUMP.json move     (after remove.py b9-prelude.json DUMP.json:
                                                                 moves each kept declaration into the prelude)

The kept name: the one already in the prelude; else the one a text that is not re-pointed cites (a group
where two are cited is left); else a name of the root namespace `Becoming`; else the earliest in the
import order (the module with the smallest closure). A group with a member outside the core is left."""
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'r31-support'))
import decltext  # noqa: E402
import dups  # noqa: E402

spec = importlib.util.spec_from_file_location('fwclass', HERE / 'fwclass.py')
fwclass = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fwclass)
spec = importlib.util.spec_from_file_location('layers', HERE.parent / 'r31-support' / 'layers.py')
layers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(layers)

TABLE = json.load(open(sys.argv[1]))
DUMP = json.load(open(sys.argv[2]))['c']
OUT = HERE / 'b9-prelude.json'
PRELUDE = 'Becoming.Prelude'


def plan():
    core, mods, clo, layer, direct = layers.layers()
    index = fwclass.citation_index()
    fwclass.unique_last(DUMP)
    rows, left = [], []
    for g in TABLE['left']:
        members = [n for n, _ in g['theorems']]
        homes = {n: decltext.decls() and next((d['module'] for d in decltext.decls() if d['full'] == n), None) for n in members}
        if any(h is None or h not in layer for h in homes.values()):
            left.append((members, 'a member outside the core'))
            continue
        if any(c.startswith(('Becoming.', 'Generative.')) for n in members for c in DUMP[n]['t']):
            left.append((members, 'the statement names a definition of the run'))
            continue
        cited = [n for n in members if any(k not in fwclass.REPOINTED for k, _ in fwclass.cited(index, n))]
        if len(cited) > 1:
            left.append((members, 'two members cited by texts that are not re-pointed'))
            continue
        in_prelude = [n for n in members if homes[n] == PRELUDE]
        root = [n for n in members if n.count('.') == 1]
        keep = (in_prelude or cited or root or sorted(members, key=lambda n: (len(clo[homes[n]]), n)))[0]
        for n in members:
            if n != keep:
                rows.append({'old': n, 'new': keep, 'why': 'same statement, kept in the prelude (B9)', 'module': homes[n]})
        rows.append({'keep': keep, 'module': homes[keep]})
    json.dump({'rows': [r for r in rows if 'old' in r], 'keep': [r for r in rows if 'keep' in r],
               'left': [{'theorems': m, 'why': w} for m, w in left]}, open(OUT, 'w'), indent=1, ensure_ascii=False)
    for r in rows:
        print(r)
    for m, w in left:
        print('left:', w, m)


def move():
    data = json.load(open(OUT))
    prelude = dups.ROOT / 'Prelude.lean'
    blocks = []
    cuts = {}
    for r in data['keep']:
        if r['module'] == PRELUDE:
            continue
        path, a, b = decltext.span(r['keep'])
        lines = path.read_text().split('\n')
        text = '\n'.join(lines[a - 1:b])
        cuts.setdefault(path, []).append((a, b))
        parts = r['keep'].split('.')[1:-1]
        # the declaration's own last component, written under its namespaces
        short = r['keep'].rsplit('.', 1)[1]
        m = re.search(r'\b(theorem|lemma)\s+(\S+)', text)
        assert m, r
        text = text[:m.start(2)] + short + text[m.end(2):]
        head = ''.join(f'namespace {p}\n' for p in parts)
        tail = ''.join(f'end {p}\n' for p in reversed(parts))
        blocks.append(f'{head}\n{text}\n\n{tail}'.rstrip('\n'))
    for path, spans in cuts.items():
        lines = path.read_text().split('\n')
        gone = set()
        for a, b in spans:
            gone.update(range(a - 1, b))
            if b < len(lines) and lines[b].strip() == '':
                gone.add(b)
        path.write_text('\n'.join(l for i, l in enumerate(lines) if i not in gone))
    s = prelude.read_text().rstrip('\n')
    assert s.endswith('end Becoming'), 'the prelude ends its namespace last'
    s = s[:-len('end Becoming')].rstrip('\n')
    s += ('\n\n/-! ## Statements stated once (R32)\n\nEach of these was stated, in the same words, in two or more modules '
          'of the run; it is stated here once, under the name kept. -/\n\n' + '\n\n'.join(blocks) + '\n\nend Becoming\n')
    prelude.write_text(s)
    print(len(blocks), 'moved into the prelude')


if __name__ == '__main__':
    {'plan': plan, 'move': move}[sys.argv[3]]()
