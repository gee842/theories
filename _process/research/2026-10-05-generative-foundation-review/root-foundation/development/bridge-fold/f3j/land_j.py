#!/usr/bin/env python3
"""F3J (19 October 2026): list F3J's new core modules in the package README and the chapter reference.

usage (from the checkout root): python3 -B land_j.py RECEIPT_ID MODULE ...

The CORE entries and the root imports and module notes are in the branch commits (they are checked
inputs, so they are final before the checker runs). This adds, for each module, a row after the
previous one (the first after `Becoming.Relevance`) to the package README's layer table and the
chapter reference's table, with the module's note from `Becoming.lean` and, in the reference, its
theorem count from the receipt; and the modules' imports to the README's import notes. Idempotent.
"""
import json
import pathlib
import re
import sys

PKG = pathlib.Path('experiments/integrated-correction/general-framework/generative-basis/lean/becoming')
REF = pathlib.Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING-REFERENCE.md')
RID, MODS = sys.argv[1], sys.argv[2:]
receipt = json.load(open(PKG / 'becoming-checks' / RID / 'verification.json'))
count = {m['module']: m['theorems'] for m in receipt.get('modules', [])}

root = (PKG / 'Becoming.lean').read_text().split('\n')


def note(m):
    i = next(k for k, l in enumerate(root) if l.startswith(f'* `Becoming.{m}` ('))
    layer = re.match(r'\* `[^`]*` \((L\d)\): ', root[i]).group(1)
    text = [root[i].split('): ', 1)[1]]
    j = i + 1
    while j < len(root) and root[j].startswith('  ') and not root[j].startswith('* '):
        text.append(root[j].strip())
        j += 1
    return layer, ' '.join(text).rstrip('.')


def imports(m):
    deps = [l.split()[1] for l in (PKG / 'Becoming' / f'{m}.lean').read_text().split('\n')
            if l.startswith('import ')]
    deps = [f'`{d.removeprefix("Becoming.")}`' for d in deps]
    return f'`{m}` imports ' + (' and '.join(deps) if len(deps) < 3 else ', '.join(deps[:-1]) + ' and ' + deps[-1])


readme = PKG / 'README.md'
lines = readme.read_text().split('\n')
prev = 'Relevance'
for m in MODS:
    layer, text = note(m)
    if not any(l.startswith(f'| {layer} | [`Becoming.{m}`]') for l in lines):
        i = next(k for k, l in enumerate(lines) if re.match(rf'^\| L\d \| \[`Becoming\.{prev}`\]', l))
        lines.insert(i + 1, f'| {layer} | [`Becoming.{m}`](Becoming/{m}.lean) | {text} |')
    prev = m
text = '\n'.join(lines)
at = '). L1–L3 contain'
for m in MODS:
    n = '; ' + imports(m)
    if n not in text:
        assert text.count(at) == 1, at
        text = text.replace(at, n + at, 1)
readme.write_text(text)

lines = REF.read_text().split('\n')
prev = 'Relevance'
for m in MODS:
    layer, text = note(m)
    if not any(f'[Becoming.{m}](' in l for l in lines):
        i = next(k for k, l in enumerate(lines) if re.match(rf'^\| L\d \| \[Becoming\.{prev}\]\(', l))
        link = f'../../../{PKG}/Becoming/{m}.lean'
        n = count[f'Becoming.{m}']
        lines.insert(i + 1, f'| {layer} | [Becoming.{m}]({link}) | {text[0].upper() + text[1:]}. | {n} |')
    prev = m
REF.write_text('\n'.join(lines))
print({m: count.get(f'Becoming.{m}') for m in MODS})
