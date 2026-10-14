#!/usr/bin/env python3
"""Field-level three-way merge of canonical result records (integration helper).

usage: merge_records.py BASE OURS THEIRS [--write] [--renames MAP.json] [--ids id ...]

BASE, OURS, THEIRS are git revisions. For every record JSON that differs between
OURS and THEIRS (or the given ids), merge field by field:
- a field changed on one side only takes that side;
- `history`, `text_versions`: base entries, then ours' additions, then theirs';
- `references`: per path, three-way per entry, additions from both sides;
- `proof_bindings`: per (receipt or path, declarations) key, three-way;
- `aliases`: three-way set merge, order kept;
- `reviewed_at_utc`: the later; `schema_version`: the higher;
- a text field ({zh, en}) or anything else changed on both sides: conflict,
  reported; with --renames the rename map is applied to the side that did not
  only rename, and if that equals the other side after renaming the merge takes it.
Writes into the working tree (with --write) or reports only.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path.cwd()
RECORDS = 'theories/becoming/results/records'


def show(rev, path):
    try:
        return json.loads(subprocess.check_output(['git', 'show', f'{rev}:{path}'], cwd=ROOT,
                                                  stderr=subprocess.DEVNULL))
    except subprocess.CalledProcessError:
        return None


def changed(a, b):
    out = subprocess.check_output(['git', 'diff', '--name-only', a, b, '--', RECORDS], cwd=ROOT, text=True)
    return [p for p in out.split() if p.endswith('.json')]


def key_of(entry):
    if isinstance(entry, dict):
        return json.dumps({k: entry.get(k) for k in ('path', 'receipt', 'checker', 'source', 'module')
                           if k in entry}, sort_keys=True, ensure_ascii=False) or json.dumps(entry, sort_keys=True)
    return json.dumps(entry, sort_keys=True, ensure_ascii=False)


def appended(base, side):
    base = base or []
    n = len(base)
    if side[:n] != base:
        return None
    return side[n:]


def merge_list_append(base, ours, theirs):
    a, b = appended(base, ours), appended(base, theirs)
    if a is None or b is None:
        return None
    return (base or []) + a + [x for x in b if x not in a]


def merge_keyed(base, ours, theirs):
    base, ours, theirs = base or [], ours or [], theirs or []
    bk = {key_of(x): x for x in base}
    ok = {key_of(x): x for x in ours}
    tk = {key_of(x): x for x in theirs}
    order = []
    for lst in (ours, theirs):
        for x in lst:
            k = key_of(x)
            if k not in order:
                order.append(k)
    out, conflicts = [], []
    for k in order:
        b, o, t = bk.get(k), ok.get(k), tk.get(k)
        if o == t:
            v = o
        elif o == b:
            v = t
        elif t == b:
            v = o
        else:
            conflicts.append(k)
            v = o
        if v is not None:
            out.append(v)
    # entries removed on one side and unchanged on the other stay removed
    return out, conflicts


def merge_set(base, ours, theirs):
    base, ours, theirs = base or [], ours or [], theirs or []
    removed = (set(base) - set(ours)) | (set(base) - set(theirs))
    out = []
    for x in ours + theirs:
        if x not in removed and x not in out:
            out.append(x)
    return out


def rename_name(name, renames):
    for old, new in renames:
        name = re.sub(r'(?<![A-Za-z0-9_])' + re.escape(old) + r'(?![A-Za-z0-9_])', new, name)
    return name


def rename_text(value, renames):
    """Rename identifiers inside `code` spans only; prose words stay."""
    if isinstance(value, str):
        return re.sub(r'`[^`]*`', lambda m: rename_name(m.group(0), renames), value)
    if isinstance(value, list):
        return [rename_text(v, renames) for v in value]
    if isinstance(value, dict):
        return {k: rename_text(v, renames) for k, v in value.items()}
    return value


def merge(base, ours, theirs, renames=()):
    base = base or {}
    out, conflicts = {}, []
    first, second = (theirs, ours) if (theirs.get('schema_version') or 1) > (ours.get('schema_version') or 1) else (ours, theirs)
    keys = list(first.keys()) + [k for k in second.keys() if k not in first]
    for k in keys:
        b, o, t = base.get(k), ours.get(k), theirs.get(k)
        if o == t:
            v = o
        elif o == b:
            v = t
        elif t == b:
            v = o
        elif k in ('history', 'text_versions'):
            v = merge_list_append(b, o or [], t or [])
            if v is None:
                conflicts.append(k)
                v = o
        elif k in ('references', 'proof_bindings'):
            v, c = merge_keyed(b, o, t)
            conflicts += [f'{k}:{x}' for x in c]
        elif k == 'aliases':
            v = merge_set(b, o, t)
            if renames:
                v = list(dict.fromkeys(rename_name(x, renames) for x in v))
        elif k == 'reviewed_at_utc':
            v = max(o or '', t or '')
        elif k == 'schema_version':
            v = max(o or 1, t or 1)
        else:
            if renames and rename_text(b, renames) == t and o is not None:
                v = rename_text(o, renames)   # theirs only renamed: rename ours
            elif renames and rename_text(b, renames) == o and t is not None:
                v = rename_text(t, renames)
            elif renames and (o is None or t is None) and rename_text(b, renames) in (o, t):
                v = None   # removed on one side, only renamed on the other
            else:
                conflicts.append(k)
                v = o
        if k in ours or k in theirs:
            if v is None and (k not in ours or k not in theirs):
                # removed on one side, unchanged on the other
                continue
            out[k] = v
    # a field removed on one side (e.g. limitations in a migration) and changed on the other
    for k in list(out):
        if k in base and ((k not in ours) != (k not in theirs)):
            other = theirs if k not in ours else ours
            if renames and rename_text(base[k], renames) == other.get(k):
                del out[k]
            elif other.get(k) == base[k]:
                del out[k]
            else:
                conflicts.append(f'{k} (removed on one side, changed on the other)')
    if renames:
        # renamed identifiers in code spans of every public field, including text
        # written by the side that did not rename (e.g. a migration)
        for k in list(out):
            if k not in ('id', 'history', 'text_versions', 'references', 'proof_bindings', 'aliases'):
                out[k] = rename_text(out[k], renames)
        for item in out.get('laws') or []:
            if isinstance(item, dict) and isinstance(item.get('declarations'), list):
                item['declarations'] = [rename_name(d, renames) for d in item['declarations']]
        for item in out.get('does_not_show') or []:
            if isinstance(item, dict) and isinstance(item.get('witness'), str):
                item['witness'] = rename_name(item['witness'], renames)
    return out, conflicts


def main():
    args = sys.argv[1:]
    write = '--write' in args
    renames = []
    if '--renames' in args:
        i = args.index('--renames')
        renames = json.loads(Path(args[i + 1]).read_text())
        renames = sorted(renames.items(), key=lambda kv: -len(kv[0]))
        del args[i:i + 2]
    ids = []
    if '--ids' in args:
        i = args.index('--ids')
        ids = args[i + 1:]
        args = args[:i]
    args = [a for a in args if a != '--write']
    base, ours, theirs = args
    paths = [f'{RECORDS}/{x}.json' for x in ids] if ids else sorted(set(changed(base, ours)) & set(changed(base, theirs)))
    report = {}
    for p in paths:
        b, o, t = show(base, p), show(ours, p), show(theirs, p)
        if o is None or t is None:
            report[p] = 'added/removed on one side'
            continue
        m, c = merge(b, o, t, renames)
        report[p] = c or 'clean'
        if write:
            (ROOT / p).write_text(json.dumps(m, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
