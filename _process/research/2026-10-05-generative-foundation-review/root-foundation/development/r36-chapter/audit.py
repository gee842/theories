"""R36: preservation audit of the restructured canonical chapter against its frozen edition.

Checks, and prints a summary with every item it could not account for:
  1. anchors: every anchor of the frozen edition (heading slugs and explicit ids) is an anchor of the
     new edition;
  2. records: every record the frozen edition links is linked by the new edition, and every record the
     new edition links exists;
  3. Lean names: every Lean name the frozen edition cites (a backticked identifier) is accounted for:
     cited by the new edition (`chapter`), cited there under another qualification (`qualified`), or
     named in a record the new edition links (`record`); names in neither are listed;
  4. existence: every Lean name the new edition cites occurs in the Lean sources (its last component
     as a token of some .lean file under experiments/);
  5. open statements: every unit of the frozen edition stating something open (units.py) has its names
     and records accounted for as in 2 and 3;
  6. links: every relative link of the new edition resolves to a file (and, within the chapter, to an
     anchor), the frozen copies excepted before the move.

Exit status 1 if anything is unaccounted. Usage:
  python3 -B audit.py ROOT FROZEN NEW [--chapter-dir theories/becoming/chapters] [--json OUT] [--allow-missing PATH ...]
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import units as U  # noqa: E402

LINK = re.compile(r'\]\(([^)\s]+)\)')
TOKEN = re.compile(r"[A-Za-z_][\w'₀-₉]*")
SKIP_NAMES = {'Init', 'Std', 'Mathlib', 'Prop', 'Nat', 'Bool', 'True', 'False', 'Type', 'Iff.rfl', 'sorry'}
# Backticked names that are not Lean: a record field, a field of the connectivity measure's output and
# the checker's list of superseded modules.
NOT_LEAN = {'next_delta': 'record field', 'families_reach_each_other': 'connectivity measure output',
            'SUPERSEDED': 'list in check_becoming.py'}
COMMIT = re.compile(r'^[0-9a-f]{7,40}$')


def anchors(root, text):
    sys.path[:0] = [str(root), str(root / 'tools' / 'research')]
    from tools.research import moves
    return moves.anchors(text)


def lean_tokens(root):
    toks = set()
    for f in (root / 'experiments').rglob('*.lean'):
        if '.lake' in f.parts or '.build' in f.parts:
            continue
        try:
            toks.update(TOKEN.findall(f.read_text(errors='replace')))
        except OSError:
            pass
    return toks


def record_texts(root, ids):
    out = {}
    for rid in ids:
        p = root / 'theories/becoming/results/records' / f'{rid}.json'
        if p.exists():
            out[rid] = p.read_text()
    return out


def main():
    args = sys.argv[1:]
    root, frozen, new = Path(args[0]), Path(args[1]), Path(args[2])
    chapter_dir = root / (args[args.index('--chapter-dir') + 1] if '--chapter-dir' in args else 'theories/becoming/chapters')
    allow = set()
    if '--allow-missing' in args:
        allow = set(a for a in args[args.index('--allow-missing') + 1:] if not a.startswith('--'))
    old_text, new_text = frozen.read_text(), new.read_text()
    report = {}

    # 1. anchors
    a_old, a_new = anchors(root, old_text), anchors(root, new_text)
    report['anchors'] = {'frozen': len(a_old), 'new': len(a_new), 'missing': sorted(a_old - a_new)}

    # 2. records
    r_old, r_new = set(U.REC.findall(old_text)), set(U.REC.findall(new_text))
    recs = record_texts(root, r_new)
    report['records'] = {'frozen': len(r_old), 'new': len(r_new), 'dropped': sorted(r_old - r_new),
                         'nonexistent': sorted(r for r in r_new if r not in recs)}
    all_records = '\n'.join(recs.values())

    # 3. Lean names of the frozen edition
    n_old = set(U.names_in(old_text)) - SKIP_NAMES
    n_new = set(U.names_in(new_text))
    classes = {'chapter': [], 'qualified': [], 'record': [], 'unaccounted': []}

    def account(n):
        if n in n_new or re.search(r'(?<![\w.])' + re.escape(n) + r'(?![\w])', new_text):
            return 'chapter'
        # the same declaration written with more or less of its namespace (`Flow.excess_bounded` for
        # `excess_bounded`, `Clearing` for `Becoming.Clearing`)
        if any(m.endswith('.' + n) or n.endswith('.' + m) for m in n_new):
            return 'qualified'
        if re.search(r'(?<![\w])' + re.escape(n) + r'(?![\w])', all_records):
            return 'record'
        return 'unaccounted'

    acc = {}
    for n in sorted(n_old):
        c = account(n)
        acc[n] = c
        classes[c].append(n)
    report['lean_names'] = {k: (len(v) if k != 'unaccounted' else v) for k, v in classes.items()}
    report['lean_names']['frozen'] = len(n_old)

    # 4. existence of the new edition's names
    toks = lean_tokens(root)
    absent = []
    for n in sorted(n_new):
        parts = [p for p in n.split('.') if p]
        if not parts or n in SKIP_NAMES or n in NOT_LEAN or COMMIT.match(n):
            continue
        if parts[-1] not in toks:
            absent.append(n)
    report['existence'] = {'cited': len(n_new), 'absent_from_lean_sources': absent}

    # 5. open statements
    open_bad = []
    for u in U.units(frozen):
        if not u['open']:
            continue
        lost = [n for n in u['names'] if acc.get(n) == 'unaccounted'] + [r for r in u['records'] if r not in r_new]
        if lost:
            open_bad.append({'line': u['line'], 'section': u['section'], 'first': u['first'][:100], 'lost': lost})
    report['open_units'] = {'frozen_open_units': sum(1 for u in U.units(frozen) if u['open']), 'with_something_unaccounted': open_bad}

    # 6. links (a link to a peer edition, `--peer NAME=PATH`, is checked against that edition's anchors)
    peers = {}
    for k, a in enumerate(args):
        if a == '--peer':
            name, _, path = args[k + 1].partition('=')
            peers[name] = anchors(root, Path(path).read_text())
    broken = []
    for m in LINK.finditer(new_text):
        target = m.group(1)
        if re.match(r'^[a-z]+:', target):
            continue
        path, _, frag = target.partition('#')
        if not path:
            if frag and frag not in a_new:
                broken.append(target)
            continue
        p = (chapter_dir / path).resolve()
        rel = str(p.relative_to(root.resolve())) if str(p).startswith(str(root.resolve())) else str(p)
        if path in peers:
            if frag and frag not in peers[path]:
                broken.append(target)
            continue
        if not p.exists() and rel not in allow:
            broken.append(target)
    report['links'] = {'checked': len(LINK.findall(new_text)), 'broken': sorted(set(broken))}

    out = json.dumps(report, ensure_ascii=False, indent=1)
    if '--json' in args:
        Path(args[args.index('--json') + 1]).write_text(out + '\n')
    print(out)
    if '--mirror' in args:
        # a shorter edition mirroring the canonical one: its content is preserved by the canonical
        # edition, so only its anchors, its records' existence, its Lean names and its links are checked
        report['mode'] = 'mirror: content preserved by the canonical edition; checks 1, 2 (existence), 4 and 6'
        bad = (report['anchors']['missing'] or report['records']['nonexistent'] or absent or report['links']['broken'])
    else:
        bad = (report['anchors']['missing'] or report['records']['dropped'] or report['records']['nonexistent']
               or classes['unaccounted'] or absent or open_bad or report['links']['broken'])
    if '--mirror' in args:
        print(json.dumps({k: report[k] for k in ('mode', 'anchors', 'existence', 'links')}, ensure_ascii=False, indent=1))
    print('AUDIT', 'FAILED' if bad else 'PASSED', file=sys.stderr)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
