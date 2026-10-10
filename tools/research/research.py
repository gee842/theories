#!/usr/bin/env python3
"""One entry point for research navigation, focused validation and discovery."""
from __future__ import annotations
import argparse
from collections import defaultdict
from contextlib import contextmanager
import fcntl
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from tools.research import registry, navigation, lean_catalogue, reading_catalogue


@contextmanager
def render_lock():
    """Serialize cooperating writers; arbitrary prose editors retain hash guards."""
    path = subprocess.check_output(['git', 'rev-parse', '--git-path', 'research-navigation.lock'], cwd=ROOT, text=True).strip()
    with (ROOT / path).open('a') as stream:
        try:
            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise ValueError('Another research renderer is active; retry after it finishes.') from None
        try:
            yield
        finally:
            fcntl.flock(stream, fcntl.LOCK_UN)


def input_snapshot():
    """Bind a render to the exact metadata/source inventory it began reading."""
    config = navigation.read(navigation.CONFIG)
    paths = {navigation.CONFIG, navigation.HISTORY}
    if isinstance(config.get('readme_opening'), str):
        paths.add(ROOT / config['readme_opening'])
    paths.update((ROOT / config['goal_directory']).glob('*.json'))
    for directory in config['record_directories']:
        for path in (ROOT / directory).glob('*.json'):
            paths.add(path)
            try:
                data = json.loads(path.read_text())
                paths.update(ROOT / ref['path'] for ref in data.get('references', []) if isinstance(ref, dict) and isinstance(ref.get('path'), str))
            except (ValueError, AttributeError):
                pass  # The ordinary validator reports malformed input.
    return {str(p): registry.digest(p) if p.is_file() else None for p in paths}


def unchanged_inputs(before):
    return before == input_snapshot()


def changed_paths(base):
    # Git validates the revision; never interpolate it into a shell command.
    rev = subprocess.check_output(['git', 'rev-parse', '--verify', base + '^{commit}'], cwd=ROOT, text=True).strip()
    changed = subprocess.check_output(['git', 'diff', '--name-only', '-z', rev, '--'], cwd=ROOT).decode().split('\0')
    new = subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard', '-z'], cwd=ROOT).decode().split('\0')
    return set(changed + new) - {''}


def inventory():
    files = subprocess.check_output(['git', 'ls-files', '--cached', '--others', '--exclude-standard', '-z'], cwd=ROOT).decode().split('\0')
    return sorted({p for p in files if p and (ROOT / p).is_file()})


def working(path):
    parts = Path(path).parts
    if path.endswith('.lean'):
        return lean_catalogue.role(path, {'declarations': [True], 'print_axioms_commands': 0}) == 'working-source'
    if parts[0] not in {'theories', '_process', 'tools', 'experiments'}:
        return len(parts) == 1 and path.endswith('.md')
    if any(x in parts for x in ['history', 'development', 'snapshots', 'verification-history']) or any(x.endswith(('-checks', '-verification', '-development')) for x in parts):
        return False
    if '/results/records/' in path and path.endswith('.md'):
        return False  # Search the editable record once, not its generated copy.
    return path.endswith(('.md', '.py'))


def search(query, archives=False, limit=30):
    records, errors = registry.load_records()
    needle = query.casefold()
    results = []
    for r in records:
        text = json.dumps({k: r[k] for k in ('id', 'title', 'claim', 'aliases')}, ensure_ascii=False)
        if needle in text.casefold():
            results.append({'kind': 'result', 'path': str(registry.record_path(r).relative_to(ROOT)), 'id': r['id'], 'summary': registry.bilingual(r['title'])})
    for path in inventory():
        if not archives and not working(path):
            continue
        if Path(path).suffix not in {'.md', '.lean', '.py', '.json', '.txt'}:
            continue
        if len(results) >= limit:
            break
        if needle in path.casefold():
            results.append({'kind': 'source', 'path': path})
            continue
        # Bound reading for large frozen evidence files when archives are requested.
        if (ROOT / path).stat().st_size > 2_000_000:
            continue
        body = (ROOT / path).read_text(errors='replace')
        for n, line in enumerate(body.splitlines(), 1):
            at = line.casefold().find(needle)
            if at >= 0:
                results.append({'kind': 'source', 'path': path, 'line': n, 'snippet': line[max(0, at-60):at+180]})
                break
    return {'archives_included': archives, 'results': results[:limit], 'errors': errors}


def import_graph():
    paths = [p for p in inventory() if p.endswith('.lean') and working(p)]
    names = defaultdict(list)
    for path in paths:
        names[Path(path).stem].append(path)
    edges, unresolved = [], []
    for path in paths:
        for mod in re.findall(r'^\s*import\s+(\S+)', lean_catalogue.scrub((ROOT / path).read_text()), re.M):
            matches = names.get(mod.split('.')[-1], [])
            if len(matches) == 1:
                edges.append({'consumer': path, 'producer': matches[0], 'module': mod, 'kind': 'textual-import-candidate'})
            else:
                unresolved.append({'consumer': path, 'module': mod, 'candidates': matches, 'reason': 'external-or-unresolved' if not matches else 'ambiguous-local-module'})
    return {'working_modules': len(paths), 'edges': edges, 'unresolved': unresolved, 'scope': 'Textual import candidates, not elaborated Lean resolution or proof of conceptual composition. Frozen copies are excluded.'}


def check_links(outputs, planned=()):
    errors = []
    available = {(ROOT / p).resolve() for p in planned}
    for name, body in outputs.items():
        for target in re.findall(r'\]\((<[^>]+>|[^\s)]+)\)', body):
            part = urlsplit(target.strip('<>'))
            if part.scheme or not part.path:
                continue
            p = ((ROOT / name).parent / unquote(part.path)).resolve()
            if not p.exists() and p not in available:
                errors.append(f'{name}: missing link {target}')
            elif part.fragment and p.suffix == '.md':
                relative = str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else None
                body = outputs.get(relative) if relative in planned else None
                found = reading_catalogue.anchors_from_text(body) if body is not None else reading_catalogue.anchors(p)
                if unquote(part.fragment) not in found:
                    errors.append(f'{name}: missing anchor {target}')
    return errors


def check_or_render(render=False, base=None, ids=None):
    before = input_snapshot()
    records, errors = registry.load_records()
    findings, drift = registry.validate(records)
    errors += findings + registry.orphan_pages(records) + navigation.validate_goals(records) + navigation.validate_history()
    selected = set(ids) if ids else registry.affected_ids(records, changed_paths(base)) if base else {r['id'] for r in records}
    errors += ['unknown result id: ' + x for x in selected - {r['id'] for r in records}]
    if errors:
        return 1, {'errors': errors, 'source_drift': drift}
    outputs = navigation.render_views(records)
    stale = {d['id'] for d in drift}
    record_outputs = {str(registry.record_path(r).with_suffix('.md').relative_to(ROOT)): registry.render_record(r) for r in records if r['id'] in selected and r['id'] not in stale}
    record_outputs[str((registry.OUT / 'RESULT-REGISTER.md').relative_to(ROOT))] = registry.render_index(records)
    planned = set(outputs) | set(record_outputs) if render else set()
    errors += check_links({**outputs, **record_outputs}, planned)
    if render and not errors:
        initial = {}
        for path in record_outputs:
            p = ROOT / path
            if p.is_file() and '<!-- Generated by ' in p.read_text():
                initial[path] = registry.digest(p)
        if not unchanged_inputs(before):
            errors.append('Research inputs changed during validation; no views written. Retry with current records.')
        else:
            errors += navigation.write_views({**outputs, **record_outputs}, initial)
    elif not render:
        for path, body in {**outputs, **record_outputs}.items():
            if not (ROOT / path).exists() or (ROOT / path).read_text() != body:
                errors.append('generated view differs; reconcile and run make research-render: ' + path)
    if not unchanged_inputs(before):
        errors.append('Research inputs changed during this operation; rerun against the latest source versions.')
    scoped = [d for d in drift if d['id'] in selected]
    return (1 if errors else 2 if scoped else 0), {'records': len(records), 'selected_records': sorted(selected), 'errors': errors, 'source_drift': scoped, 'unrelated_source_drift': [d for d in drift if d['id'] not in selected], 'scope': 'Metadata, navigation, preserved history and proof-receipt bindings only. No new Lean or empirical validation.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for cmd in ('check', 'render'):
        p = sub.add_parser(cmd)
        p.add_argument('--changed-since')
        p.add_argument('--ids', nargs='+')
    p = sub.add_parser('find')
    p.add_argument('query', nargs='?', default=os.environ.get('QUERY', ''))
    p.add_argument('--archives', action='store_true')
    p.add_argument('--limit', type=int, default=30)
    sub.add_parser('imports')
    p = sub.add_parser('preserve-view', help='After reading and reconciling added prose, preserve it before rendering')
    p.add_argument('path')
    p.add_argument('--note', required=True, help='Where the reviewed additions were integrated, with their scope')
    args = parser.parse_args()
    if args.command == 'find':
        if not args.query.strip():
            parser.error('supply a query or use make research-find QUERY=topic')
        result, code = search(args.query, args.archives, args.limit), 0
    elif args.command == 'imports':
        result, code = import_graph(), 0
    elif args.command == 'preserve-view':
        with render_lock():
            result, code = navigation.preserve_view(args.path, args.note), 0
    elif args.command == 'render':
        with render_lock():
            code, result = check_or_render(True, args.changed_since, args.ids)
    else:
        code, result = check_or_render(False, args.changed_since, args.ids)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return code


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, OSError) as exc:
        print(json.dumps({'errors': [str(exc)]}))
        raise SystemExit(1)
