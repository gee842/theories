#!/usr/bin/env python3
"""R32 (B7(a), B15): fold reading modules and small modules into the module they read.

usage: python3 -B fold.py [--dry]

For each fold X -> S of FOLDS, in order:
* X's text after its imports is appended to S as a final section (`section X ... end X`), its module
  doc becoming the section's heading (`# T` -> `## T`, "This module" -> "This section");
* S takes the imports of X it lacks (none that S's closure already holds, never S itself);
* every importer of X imports S instead (once);
* comments of the package's Lean files and the Lean README name `Becoming.S` and `Becoming/S.lean`
  where they named X's;
* X leaves the checker's CORE list and `Becoming.lean`'s imports (layers.py drops its note).
Declarations keep their names and statements: X's namespaces are reopened inside the section.
X's file is deleted from `Becoming/`; history_move.py restores its bytes at the old path and moves
them to the Lean history folder with `research.py move`.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = HERE.parents[5] / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
B = PKG / 'Becoming'
DRY = '--dry' in sys.argv

FOLDS = [
    ('PresentationFrames', 'Presentations'),
    ('CensusWebs', 'Listing'),
    ('MoveRuns', 'MoveFormation'),
    ('CaptureWorlds', 'Capture'),
    ('CountdownCourses', 'Countdown'),
    ('DependenceWebs', 'Units'),
    ('ExchangeFlows', 'Sampling'),
    ('JointPlanFrames', 'Composition'),
    ('LevelWebs', 'Entropy'),
    ('ListedOutcomeFrames', 'Likeness'),
    ('OrderWorlds', 'OrderNormal'),
    ('PassageWorlds', 'OneStep'),
    ('RecurrenceRuns', 'Branching'),
    ('RetrodictionRuns', 'Courses'),
    ('CandidateRuns', 'Courses'),
    ('ReducedRuns', 'Courses'),
    ('RevisionRuns', 'Revision'),
    ('StockTraces', 'Stock'),
    ('TallyWorlds', 'Counting'),
    ('BoundaryFlows', 'Boundaries'),
    ('BoundaryWorlds', 'Boundaries'),
    ('DiagonalRuns', 'Diagonal'),
    ('TailRuns', 'Tail'),
    ('Grains', 'Granularity'),
    ('SupportRecovery', 'RenewalFlow'),
    ('AcceptanceFrames', 'FrontierFrames'),
]
IMPORT = re.compile(r'^import\s+(\S+)\s*$')


def split(text):
    """Imports, the module doc (without its delimiters) and the rest."""
    lines = text.split('\n')
    k = 0
    imports = []
    while k < len(lines) and (IMPORT.match(lines[k]) or not lines[k].strip()):
        if lines[k].strip():
            imports.append(IMPORT.match(lines[k]).group(1))
        k += 1
    rest = '\n'.join(lines[k:])
    m = re.match(r'/-!(.*?)-/\n', rest, re.S)
    assert m, 'no module doc'
    return imports, m.group(1).strip('\n'), rest[m.end():]


def closure_of(name, texts, seen=None):
    seen = set() if seen is None else seen
    if name in seen or name not in texts:
        return seen
    seen.add(name)
    for i in split(texts[name])[0]:
        closure_of(i, texts, seen)
    return seen


def comments(text, fn):
    """Apply fn to the comment parts of a Lean text (block comments, nested, and line comments)."""
    out, i, depth, start = [], 0, 0, 0
    code_start = 0
    n = len(text)
    while i < n:
        if depth == 0 and text.startswith('--', i):
            j = text.find('\n', i)
            j = n if j < 0 else j
            out.append(text[code_start:i])
            out.append(fn(text[i:j]))
            i = code_start = j
            continue
        if text.startswith('/-', i):
            if depth == 0:
                out.append(text[code_start:i])
                start = i
            depth += 1
            i += 2
            continue
        if depth and text.startswith('-/', i):
            depth -= 1
            i += 2
            if depth == 0:
                out.append(fn(text[start:i]))
                code_start = i
            continue
        if depth == 0 and text[i] == '"':
            j = i + 1
            while j < n and text[j] != '"':
                j += 2 if text[j] == '\\' else 1
            i = j + 1
            continue
        i += 1
    out.append(text[code_start:] if depth == 0 else fn(text[start:]))
    return ''.join(out)


def mention(x, s):
    pat = re.compile(r'(?<![\w.])Becoming\.' + x + r'(?![\w\'])(?!\.[A-Za-z_])')
    path = re.compile(r'\b' + x + r'\.lean\b')
    return lambda t: path.sub(s + '.lean', pat.sub('Becoming.' + s, t))


def main():
    texts = {'Becoming.' + p.stem: p.read_text() for p in B.glob('*.lean')}
    root = (PKG / 'Becoming.lean').read_text()
    check = (PKG / 'check_becoming.py').read_text()
    readmes = {n: (PKG / n).read_text() for n in ('README.md', 'README.zh.md')}
    gone = []
    for x, s in FOLDS:
        X, S = 'Becoming.' + x, 'Becoming.' + s
        assert X in texts and S in texts, (x, s)
        imports, doc, body = split(texts[X])
        s_imports, _, _ = split(texts[S])
        have = closure_of(S, texts)
        assert X not in have, (x, 'already in the closure of', s)
        add = [i for i in imports if i != S and i not in have]
        for i in add:
            assert S not in closure_of(i, texts), (x, s, 'cycle through', i)
        # the section
        doc = re.sub(r'^# ', '## ', doc.lstrip('\n'), count=1)
        doc = doc.replace('This module', 'This section').replace('this module', 'this section')
        body = comments(body, lambda t: t.replace('This module', 'This section').replace('this module', 'this section'))
        section = f'\nsection {x}\n\n/-!\n{doc}\n-/\n{body.rstrip()}\n\nend {x}\n'
        target = texts[S].rstrip('\n') + '\n' + section
        if add:
            lines = target.split('\n')
            last = max(k for k, l in enumerate(lines) if IMPORT.match(l))
            lines[last + 1:last + 1] = [f'import {i}' for i in add]
            target = '\n'.join(lines)
        texts[S] = target
        del texts[X]
        gone.append(X)
        # importers
        for name, t in list(texts.items()):
            lines = t.split('\n')
            if f'import {X}' not in lines:
                continue
            already = f'import {S}' in lines or name == S
            new = []
            for l in lines:
                if l == f'import {X}':
                    if not already:
                        new.append(f'import {S}')
                        already = True
                    continue
                new.append(l)
            texts[name] = '\n'.join(new)
        # mentions
        fix = mention(x, s)
        for name in texts:
            texts[name] = comments(texts[name], fix)
        root_lines = [l for l in root.split('\n') if l != f'import {X}']
        root = comments('\n'.join(root_lines), fix)
        for n in readmes:
            lines = readmes[n].split('\n')
            readmes[n] = '\n'.join(l if f'[`{X}`]' in l else fix(l) for l in lines)
        a = check.index('\nCORE = [') + 1
        b = check.index(']\n', a) + 2
        core_block = check[a:b]
        assert core_block.count(f'"{X}", ') == 1, x
        check = check[:a] + core_block.replace(f'"{X}", ', '', 1) + check[b:]
        # the receipt's scope text names the section of S that now holds X's laws
        scope = re.findall(r'(?m)^    "' + x + r'( \([^)]*\))?: ', check)
        if not scope:
            print(f'  ({x} has no entry in the scope text)')
        check = re.sub(r'(?m)^    "' + x + r'( \([^)]*\))?: ', lambda m: f'    "{s}, section {x}{m.group(1) or ""}: ', check)
        others = [l for l in check.split('\n') if f'"{X}"' in l]
        # the superseded periphery modules X stated are stated by S
        for l in others:
            m = re.match(r'^(    "\w+": )\[(.*)\],$', l)
            assert m, l
            names = []
            for n in re.findall(r'"([\w.]+)"', m.group(2)):
                n = S if n == X else n
                if n not in names:
                    names.append(n)
            check = check.replace(l, m.group(1) + '[' + ', '.join(f'"{n}"' for n in sorted(names)) + '],', 1)
        print(f'{x} -> {s}' + (f' (imports {", ".join(add)})' if add else ''))
    if DRY:
        return
    for name, t in texts.items():
        p = B / (name[len('Becoming.'):] + '.lean')
        if p.read_text() != t:
            p.write_text(t)
    for X in gone:
        (B / (X[len('Becoming.'):] + '.lean')).unlink()
    (PKG / 'Becoming.lean').write_text(root)
    (PKG / 'check_becoming.py').write_text(check)
    for n, t in readmes.items():
        (PKG / n).write_text(t)
    print(len(gone), 'folded')


if __name__ == '__main__':
    main()
