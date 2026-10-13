#!/usr/bin/env python3
"""Reconcile the verified P58c source against the current landing checkout.

Usage: apply_latest.py ROOT [--check | --output-tree TREE | --apply]

The default is --check. Each of the 18 supplied modules is merged using the
recorded verification base, never copied over newer work. Current modules that
arrived later receive the exact identifier renames. P77's two uses of the old
World.rests conjunction are routed through its proved consequence. No receipt,
document, record, historical package, or OPENING wording is changed here.
This preparation is not a Lean check; run the consolidated checkers afterward.
"""
import argparse
from pathlib import Path
import subprocess
import tempfile

import p58c_names as names
from finish_listing import listing_delta


HERE = Path(__file__).resolve().parent
BASE = '9a70ff1a'
CORE = Path('experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming')


def merged(root, path, supplied):
    relative = path.relative_to(root)
    base = subprocess.run(
        ['git', '-C', str(root), 'show', f'{BASE}:{relative.as_posix()}'],
        check=True, capture_output=True,
    ).stdout
    current = path.read_bytes()
    if current == base or current == supplied:
        return supplied.decode()
    with tempfile.TemporaryDirectory(prefix='p58c-merge-') as temporary:
        temporary = Path(temporary)
        latest, original, proposed = [temporary / name for name in ('latest', 'base', 'p58c')]
        for target, value in ((latest, current), (original, base), (proposed, supplied)):
            target.write_bytes(value)
        result = subprocess.run(
            ['git', 'merge-file', '-p', str(latest), str(original), str(proposed)],
            capture_output=True, text=True,
        )
    if result.returncode:
        raise SystemExit(f'{relative}: reconciliation conflict; source files left unchanged\n{result.stdout}')
    return result.stdout


def following_module(path, text):
    """P77 keeps its statement; derive its conjunction from P58c's stronger one."""
    if path.name == 'Listing.lean':
        old = '(World.rests finite balanced dissipative embodied)'
        new = ('(World.not_recurring_of_rests_unrefuted\n'
               '        (World.rests_unrefuted finite balanced dissipative embodied))')
        count = text.count(old)
        if count not in (0, 2):
            raise SystemExit(f'{path}: expected zero or two old P77 uses, found {count}')
        text = text.replace(old, new)
        text = listing_delta(text)
    return names.rename(text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--check', action='store_true')
    mode.add_argument('--output-tree', type=Path)
    mode.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    root = args.root.resolve()
    source = root / CORE
    supplied = {p.name: p for p in (HERE / 'lean/Becoming').glob('*.lean')}
    assert len(supplied) == 18, f'expected 18 verified modules, found {len(supplied)}'
    assert all((source / name).is_file() for name in supplied)
    changed = {}
    for path in sorted(source.glob('*.lean')):
        original = path.read_text()
        text = (merged(root, path, supplied[path.name].read_bytes())
                if path.name in supplied else original)
        text = following_module(path, text)
        remaining = names.old_left(text)
        if remaining:
            raise SystemExit(f'{path}: unresolved renamed references: {remaining}')
        if text != original:
            changed[path] = text
    # All merges and adaptations have succeeded before any source is written.
    for path, text in changed.items():
        if args.apply:
            path.write_text(text)
        elif args.output_tree:
            target = args.output_tree.resolve() / 'Becoming' / path.name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text)
        print(path.relative_to(root))
    print(f'P58c: {len(changed)} current modules reconciled; '
          + ('applied' if args.apply else 'overlay written' if args.output_tree else 'check only'))
    print('No Lean check performed. Check this exact source before recording the landing.')


if __name__ == '__main__':
    main()
