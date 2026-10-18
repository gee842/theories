#!/usr/bin/env python3
"""F3Q (18 October 2026): register F3Q's new core modules. Idempotent; rerun after a rebase.

usage (from the checkout root): python3 -B land_q.py [MODULE ...]   (default: every module below)

Adds each module to `CORE` in `check_becoming.py` after its anchor, imports it in `Becoming.lean`
and lists it in that file's module notes, the package README's layer table and import notes, and
the chapter reference's table. Touches no existing core module, bridge or join file, and neither
the `BRIDGE` nor the `PERIPHERY_JOINS` list.
"""
import pathlib
import re
import sys

PKG = pathlib.Path('experiments/integrated-correction/general-framework/generative-basis/lean/becoming')
REF = pathlib.Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING-REFERENCE.md')

# module: (layer, CORE / docstring / reference anchor, README anchor, theorems, text)
MODULES = {
    'Derivation': ('L2', 'Inquiry', 'Inquiry', 32,
                   'premise-tracked derivation from a basis (no premise beyond what each theorem names): a derived '
                   'claim holds wherever the basis and its local premises do (`Derives.sound`), so the whole closure '
                   'holds throughout a domain exactly where the basis does (`closure_throughout_iff`) and a '
                   'countermodel excludes a claim from it (`countermodel_excludes`); with a list covering the basis, '
                   'claims met one by one are met by one configuration (`pointwise_iff_common`), which rows met '
                   'separately need not be (`rows_not_pointwise`); every law is read on the scope of an inquiry '
                   '(`Scope.closure_iff`, `Scope.goal_closure`, `Scope.common_relative`)'),
    'PartialReadout': ('L4', 'LearnableRuns', 'LearnableRuns', 32,
                       'partial readout of a feature through a map on a domain (no premise beyond what each theorem '
                       'names; a section of the map is a hypothesis where a reading must be built): an exact reading '
                       'is sound and needs the feature lumped (`ExactWithin.sound`, `ExactWithin.lumped`), and with a '
                       'section one exists exactly then (`exact_exists_iff`); a sound reading stays silent where the '
                       'map merges two feature values (`SoundWithin.silent`); in the channel model the signal alone is '
                       'read by no exact reading and the signal with a reference is (`signal_no_exact`, '
                       '`paired_exact`); on runs, an extrapolation rests on the feature from a step exactly where it '
                       'reads the prefix exactly from then on (`Runs.exact_iff_restsFrom`)'),
}
IMPORT_NOTES = {
    '; within L3,': '; `Derivation` imports `Inquiry`',
    '). L1–L3 contain': '; `PartialReadout` imports `Readout` and `LearnableRuns`',
}


def after_entry(lines, start, is_entry):
    """Index just past the entry starting at `start` (its continuation lines included)."""
    i = start + 1
    while i < len(lines) and not is_entry(lines[i]) and lines[i].startswith('  '):
        i += 1
    return i


def main(selected):
    checker = PKG / 'check_becoming.py'
    src = checker.read_text()
    core = re.search(r'^CORE = \[(.*?)\]', src, re.S | re.M)
    body = core.group(1)
    for m in selected:
        name = f'"Becoming.{m}"'
        if name in body:
            continue
        anchor = f'"Becoming.{MODULES[m][1]}"'
        assert anchor in body, anchor
        body = body.replace(anchor, f'{anchor}, {name}', 1)
    src = src[:core.start(1)] + body + src[core.end(1):]
    checker.write_text(src)

    root = PKG / 'Becoming.lean'
    lines = root.read_text().split('\n')
    for m in selected:
        layer, anchor, _, _, text = MODULES[m]
        if f'import Becoming.{m}' not in lines:
            i = lines.index(f'import Becoming.{anchor}')
            lines.insert(i + 1, f'import Becoming.{m}')
        if not any(l.startswith(f'* `Becoming.{m}` (') for l in lines):
            i = next(k for k, l in enumerate(lines) if l.startswith(f'* `Becoming.{anchor}` ('))
            j = after_entry(lines, i, lambda l: l.startswith('* `'))
            words, out, cur = f'* `Becoming.{m}` ({layer}): {text}.'.split(' '), [], ''
            for w in words:
                if cur and len(cur) + 1 + len(w) > 98:
                    out.append(cur)
                    cur = '  ' + w
                else:
                    cur = f'{cur} {w}' if cur else w
            out.append(cur)
            lines[j:j] = out
    root.write_text('\n'.join(lines))

    readme = PKG / 'README.md'
    lines = readme.read_text().split('\n')
    for m in selected:
        layer, _, anchor, _, text = MODULES[m]
        if any(l.startswith(f'| {layer} | [`Becoming.{m}`]') for l in lines):
            continue
        i = next(k for k, l in enumerate(lines) if re.match(rf'^\| L\d \| \[`Becoming\.{anchor}`\]', l))
        lines.insert(i + 1, f'| {layer} | [`Becoming.{m}`](Becoming/{m}.lean) | {text} |')
    text = '\n'.join(lines)
    for at, note in IMPORT_NOTES.items():
        if not any(note.startswith(f'; `{m}`') for m in selected):
            continue
        if note not in text:
            assert text.count(at) == 1, at
            text = text.replace(at, note + at, 1)
    readme.write_text(text)

    lines = REF.read_text().split('\n')
    for m in selected:
        layer, anchor, _, count, text = MODULES[m]
        if any(f'[Becoming.{m}](' in l for l in lines):
            continue
        i = next(k for k, l in enumerate(lines) if re.match(rf'^\| L\d \| \[Becoming\.{anchor}\]\(', l))
        link = f'../../../{PKG}/Becoming/{m}.lean'
        lines.insert(i + 1, f'| {layer} | [Becoming.{m}]({link}) | {text[0].upper() + text[1:]}. | {count} |')
    REF.write_text('\n'.join(lines))


if __name__ == '__main__':
    main(sys.argv[1:] or list(MODULES))
