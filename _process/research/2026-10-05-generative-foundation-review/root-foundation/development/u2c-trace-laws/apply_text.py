#!/usr/bin/env python3
"""U2c (18 October 2026) landing edits: the receipt in the study's note (section 167), the chapter's section 9
receipt paragraph, and the board row moved to the history file (rule 4). Every edit must match exactly once.

usage (from the repository root): python3 -B apply_text.py RECEIPT BASE AFTER [EARLIER]
                                   python3 -B apply_text.py board RECEIPT     (the board step alone)
RECEIPT is the core checker run, BASE the main commit it ran on, AFTER what BASE adds to the last landing (for the
receipt sentence), EARLIER a receipt these edits already wrote, which RECEIPT replaces after a rerun. The section 9 counts are read from the receipt; a count that differs from the chapter's stops the
script, since U2c adds no theorem."""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
BOARD = '_process/BECOMING-WORKBOARD.md'
HISTORY = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
SR = '../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'


def n(x):
    return f'{x:,}'


def counts(rid):
    d = json.loads((ROOT / PKG / 'becoming-checks' / rid / 'verification.json').read_text())
    assert d['status'] == 'passed', d['status']
    mods = {m['module']: m for m in d['modules']}
    th = lambda names: sum(int(mods[x]['theorems']) for x in names)
    probe = mods['Becoming.ProbeRunsInherited']
    return {
        'core': (len(d['core_modules']), th(d['core_modules'])),
        'foundation': (len(d['foundation_modules']), th(d['foundation_modules'])),
        'closure': (len(d['core_closure']), th(d['core_closure'])),
        'bridge': (len(d['bridge_modules']), th(d['bridge_modules'])),
        'spine': th(d['spine_modules']),
        'audited': sum(len(mods[x]['declarations']) for x in d['spine_modules']),
        'pj': (len(d['periphery_join_modules']), th(d['periphery_join_modules'])),
        'inherited': len(d['inherited_receipts']),
        'compile': len(d['compile_order']),
        'injeq': (len(d['generated_axiom_dependencies']), len(d['bridge_generated_axiom_dependencies'])),
        'ran': len(d['lean_steps']['ran']),
        'reused': len(d['lean_steps']['reused']),
        'probe': (int(probe['theorems']), len(probe['declarations']), probe['axiom_dependencies']),
    }


def same_counts(before, rid):
    """U2c adds and removes no declaration: every module of the run the chapter names has the same theorems and
    declarations in RECEIPT, and the module lists, layers and compile order agree, so every count row stays."""
    load = lambda r: json.loads((ROOT / PKG / 'becoming-checks' / r / 'verification.json').read_text())
    a, b = load(before), load(rid)
    for key in ('core_modules', 'foundation_modules', 'bridge_modules', 'periphery_join_modules', 'core_closure',
                'compile_order', 'spine_modules'):
        assert a[key] == b[key], key
    assert sorted(a['inherited_receipts']) == sorted(b['inherited_receipts'])
    summary = lambda d: {m['module']: (m['layer'], m['theorems'], len(m['declarations'])) for m in d['modules']}
    assert summary(a) == summary(b), 'module counts differ'
    for key in ('generated_axiom_dependencies', 'bridge_generated_axiom_dependencies'):
        assert sorted(a[key]) == sorted(b[key]), key
    print('counts unchanged from', before)


def drop_queue_entry(board):
    """The board's queue line without U2c's entry (`then U2c (...)` after another item, or `U2c (...); then` first)."""
    lines = board.split('\n')
    at = [i for i, line in enumerate(lines) if line.startswith('In the queue')]
    if not at or 'U2c (' not in lines[at[0]]:
        return board
    line = lines[at[0]]
    start = line.index('U2c (')
    depth, end = 0, None
    for j in range(start + len('U2c '), len(line)):
        depth += {'(': 1, ')': -1}.get(line[j], 0)
        if depth == 0:
            end = j + 1
            break
    assert end, 'unbalanced U2c entry'
    running = re.match(r', core checker running on `[0-9a-f]+`', line[end:])
    if running:
        end += running.end()
    if line[:start].endswith('; then '):
        line = line[:start - len('; then ')] + line[end:]
    elif line[end:].startswith('; then '):
        line = line[:start] + line[end + len('; then '):]
    else:
        raise SystemExit('U2c queue entry in an unexpected place')
    lines[at[0]] = line
    return '\n'.join(lines)


def main(rid, base, after, earlier=None):
    c = counts(rid)
    theorems, declarations, axioms = c['probe']
    assert (theorems, declarations) == (21, 22), c['probe']
    for law in ('slow_trace_misses_deadline', 'empty_candidates_trace_fails'):
        assert axioms[f'Becoming.ProbeRunsInherited.{law}'] == ['propext'], law
    # ---------------------------------------------------------------- study, section 167
    p = ROOT / STUDY
    s = p.read_text(encoding='utf-8')
    if earlier:
        assert s.count('`RECEIPT`') == 0 and s.count(earlier) == 2, earlier
        s = s.replace(earlier, rid)
        p.write_text(s, encoding='utf-8')
        print('re-pointed', STUDY)
    elif s.count('`RECEIPT`') == 0 and s.count(f'Core receipt `{rid}`') == 1:
        print('already edited', STUDY)
    else:
        assert s.count('`RECEIPT`') == 1 and s.count('becoming-checks/RECEIPT/') == 1
        s = s.replace('`RECEIPT`', f'`{rid}`').replace('becoming-checks/RECEIPT/', f'becoming-checks/{rid}/')
        p.write_text(s, encoding='utf-8')
        print('edited', STUDY)
    # ---------------------------------------------------------------- chapter, section 9
    p = ROOT / CHAPTER
    ch = p.read_text(encoding='utf-8')
    start = ch.index('**The current receipt.**')
    assert ch.count('**The current receipt.**') == 1
    end = ch.index('\n\n', ch.index('- That run reused', start))
    para = ch[start:end]
    old = re.search(r'is run `([0-9TZ.]+)`', para).group(1)
    assert para.count(old) == 3, old  # the run, the frozen folder's name and its link
    same_counts(old, rid)
    para = para.replace(old, rid)
    para, k = re.subn(
        r'It was checked with Lean 4\.29\.1 on main \S+ (?:\(.*?\) )?with .*? in the working tree, and it passed\.',
        f'It was checked with Lean 4.29.1 on main {base} ({after}) with U2c (the two trace laws of '
        f'`Becoming.ProbeRunsInherited` now state that their traces exist, [study §167]({SR}'
        f'#167-the-unification-follow-through-u2)) in the working tree, and it passed.', para)
    assert k == 1, 'receipt sentence'
    para, k = re.subn(r'That run reused [\d,]+ cached Lean steps from `~/\.cache/becoming-lean` and ran [\d,]+\.',
                      f'That run reused {n(c["reused"])} cached Lean steps from `~/.cache/becoming-lean` and ran '
                      f'{n(c["ran"])}.', para)
    assert k == 1, 'reused sentence'
    expect = {
        '| Core modules (with the root `Becoming`, 0 theorems) |': f' {c["core"][0]} modules, {n(c["core"][1])} theorems |',
        '| Foundation modules |': f' {c["foundation"][0]} modules, {n(c["foundation"][1])} theorems |',
        '| Core closure |': f' {c["closure"][0]} modules, {n(c["closure"][1])} theorems |',
        '| Spine (core and bridge) |': f' {n(c["spine"])} theorems |',
        '| Audited spine declarations |': f' {n(c["audited"])} |',
        '| Modules in the compile order |': f' {c["compile"]} |',
    }
    lines = para.split('\n')
    for line in lines:
        for head, tail in expect.items():
            if line.startswith(head):
                assert line == head + tail, (line, tail)
        if line.startswith('| Bridge modules'):
            assert f'| {c["bridge"][0]} modules, {n(c["bridge"][1])} theorems |' in line, line
        if line.startswith('| Periphery-join modules'):
            assert f'| {c["pj"][0]} modules, {n(c["pj"][1])} theorems,' in line, line
        if line.startswith('| Inherited modules bound'):
            assert f'| {c["inherited"]} (' in line, line
        if line.startswith('| Generated `injEq`'):
            assert f'| {c["injeq"][0]} in the core closure, {c["injeq"][1]} on the bridge side' in line, line
    p.write_text(ch[:start] + para + ch[end:], encoding='utf-8')
    print('edited', CHAPTER, c['ran'], 'ran', c['reused'], 'reused')
    # ---------------------------------------------------------------- board row to the history file
    board_step(rid, earlier)


def board_step(rid, earlier=None):
    p = ROOT / BOARD
    board = p.read_text(encoding='utf-8')
    rows = [line for line in board.split('\n') if line.startswith('| **U2c:')]
    if not rows and earlier:
        p = ROOT / HISTORY
        hist = p.read_text(encoding='utf-8')
        assert hist.count(f'core receipt `{earlier}`') == 1, earlier
        p.write_text(hist.replace(f'core receipt `{earlier}`', f'core receipt `{rid}`'), encoding='utf-8')
        print('re-pointed the U2c row in', HISTORY)
        return
    assert len(rows) == 1
    row = rows[0]
    board = board.replace(row + '\n', '')
    cells = row.split(' | ')
    assert cells[2].startswith('claimed 2026-10-18'), cells[2]
    cells[2] = (f'landed 2026-10-18 (the landing commit moves this row; core receipt `{rid}`): both traces exist, so '
                'neither law is vacuous, and each now states its trace as a conjunct; 21 theorems, axiom reports '
                'unchanged (`propext`); study §167, D43 (en + zh) and item 14 of the decision brief record it')
    moved = ' | '.join(cells).replace('](research/', '](../../research/')
    board = drop_queue_entry(board)
    p.write_text(board, encoding='utf-8')
    p = ROOT / HISTORY
    hist = p.read_text(encoding='utf-8')
    marker = '\n\n## Lapsed claims (18 October 2026)'
    assert hist.count(marker) == 1
    hist = hist.replace(marker, '\n' + moved + marker)
    p.write_text(hist, encoding='utf-8')
    print('moved the U2c row to', HISTORY)


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == 'board':
        board_step(sys.argv[2])
    elif len(sys.argv) in (4, 5):
        main(*sys.argv[1:])
    else:
        sys.exit(__doc__)
