#!/usr/bin/env python3
"""Resolve the line conflicts of a diff3 merge at the level of characters.

usage: python3 -B charmerge.py DIFF3 OUT

DIFF3 is the output of `git merge-file -p --diff3 OURS BASE THEIRS`. Within each conflict block,
the edits taking BASE to THEIRS are applied to OURS wherever they touch only text that OURS left
unchanged; a block with an edit overlapping one of OURS is reported and left as a conflict.
"""
import sys
from difflib import SequenceMatcher


def blocks(lines):
    out, i = [], 0
    while i < len(lines):
        if lines[i].startswith('<<<<<<<'):
            j, part, mode = i + 1, {'o': [], 'b': [], 't': []}, 'o'
            while not lines[j].startswith('>>>>>>>'):
                if lines[j].startswith('|||||||'):
                    mode = 'b'
                elif lines[j].startswith('=======') and mode == 'b':
                    mode = 't'
                else:
                    part[mode].append(lines[j])
                j += 1
            out.append(('conflict', part))
            i = j + 1
        else:
            out.append(('line', lines[i]))
            i += 1
    return out


def merge(base, ours, theirs):
    """Apply BASE→THEIRS edits to OURS; None where an edit overlaps an edit of OURS."""
    bo = SequenceMatcher(None, base, ours, autojunk=False)
    keep = [None] * (len(base) + 1)       # base index -> ours index, where unchanged
    for tag, i1, i2, j1, j2 in bo.get_opcodes():
        if tag == 'equal':
            for k in range(i1, i2 + 1):
                keep[k] = j1 + (k - i1)
    edits = []
    for tag, i1, i2, j1, j2 in SequenceMatcher(None, base, theirs, autojunk=False).get_opcodes():
        if tag == 'equal':
            continue
        if any(keep[k] is None for k in range(i1, i2 + 1)):
            return None
        if i2 > i1 and keep[i2] - keep[i1] != i2 - i1:
            return None
        edits.append((keep[i1], keep[i1] + (i2 - i1), theirs[j1:j2]))
    for a, b, new in sorted(edits, reverse=True):
        ours = ours[:a] + new + ours[b:]
    return ours


def main():
    lines = open(sys.argv[1], encoding='utf-8').read().split('\n')
    out, unresolved = [], 0
    for kind, item in blocks(lines):
        if kind == 'line':
            out.append(item)
            continue
        merged = merge('\n'.join(item['b']), '\n'.join(item['o']), '\n'.join(item['t']))
        if merged is None:
            unresolved += 1
            out += ['<<<<<<< ours'] + item['o'] + ['||||||| base'] + item['b'] + ['======='] + item['t'] + ['>>>>>>> theirs']
        else:
            out += merged.split('\n')
    open(sys.argv[2], 'w', encoding='utf-8').write('\n'.join(out))
    print('unresolved', unresolved)


if __name__ == '__main__':
    main()
