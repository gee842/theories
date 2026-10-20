#!/usr/bin/env python3
"""Capture documentary inventory and render the cross-session result map.

--capture refreshes the Lean navigation from one inventory and records a dated
checkpoint. --check checks that checkpoint's rendering and local links and writes
nothing; changed live sources are reported separately, never silently certified or
overwritten. Historical since R35 (20 October 2026, E2): the map of 8 October 2026 and its inputs are frozen in
history, `make research-render` no longer writes it, and the paths below are their history paths.
This tool performs no Lean build or semantic equivalence check.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / '_process/research/2026-10-05-generative-foundation-review/history/root-foundation'
OUT = ROOT / 'theories/becoming/results'
DATA = OUT / 'data/session-results.json'
SNAPSHOT = HERE / 'SESSION-OUTCOME-SNAPSHOT.json'
INVENTORY = HERE / 'SESSION-PROOF-OVERLAP.json'
BASELINE = HERE / 'SESSION-INTEGRATION-BASELINE.json'
CHECKS = HERE / 'SESSION-RESULT-MAP-CHECKS.json'
REPORT = ROOT / 'theories/becoming/history/SESSION-RESULTS-2026-10-08.md'


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def read(path: Path):
    return json.loads(path.read_text())


def write_json(path: Path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def module():
    spec = importlib.util.spec_from_file_location('lean_catalogue', Path(__file__).with_name('lean_catalogue.py'))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def catalogue_outputs(m, manifest, sources):
    """The Lean catalogue files rendered from one inventory (lean_catalogue.outputs), by path."""
    return {ROOT / name: body for name, body in m.outputs(manifest, sources).items()}


def capture():
    m = module()
    old = read(OUT / 'data/lean-index.json')
    if not BASELINE.exists():
        write_json(BASELINE, {
            'captured_at_utc': datetime.now(timezone.utc).isoformat(),
            'statistics': old['statistics'],
            'output_sha256': {str(p.relative_to(ROOT)): digest(p.read_bytes()) for p in
                [OUT / 'data/lean-index.json', OUT / 'data/source-index.json', OUT / 'LEAN-INDEX.md', OUT / 'README.md']},
            'validation': 'Documentary pre-refresh baseline; not proof validation.',
        })
    manifest, sources = m.catalogue()
    active = [f for f in manifest['files'] if f['role'] in ('working-source', 'audit-driver')]
    by_bytes = defaultdict(list)
    headers = defaultdict(list)
    source_read_races = []
    for f in active:
        by_bytes[f['sha256']].append(f['path'])
        raw = (ROOT / f['path']).read_bytes()
        if digest(raw) != f['sha256']:
            source_read_races.append(f['path'])
            continue
        clean = m.scrub(raw.decode())
        lines = clean.splitlines(keepends=True)
        offsets = [0]
        for line in lines:
            offsets.append(offsets[-1] + len(line))
        content = manifest['contents_by_sha256'][f['sha256']]
        for d in content['declarations']:
            if d['kind'] not in ('theorem', 'lemma'):
                continue
            tail = clean[offsets[d['line']-1]:]
            match = re.match(r'\s*(?:private\s+|protected\s+)?(?:theorem|lemma)\s+\S+\s*', tail)
            if not match or ':=' not in tail[match.end():]:
                continue
            header = re.sub(r'\s+', ' ', tail[match.end():].split(':=', 1)[0]).strip()
            if len(header) < 80:
                continue
            headers[header].append({'path': f['path'], 'name': d['qualified_name_hint'], 'line': d['line']})
    candidates = [{'header': h, 'occurrences': rows} for h, rows in headers.items()
                  if len({r['path'] for r in rows}) > 1]
    chapters = read(OUT / 'data/arguments-a-l.json') + read(OUT / 'data/arguments-m-z.json')
    registered = {r['source'] for r in chapters}
    current = {str(p.relative_to(ROOT)) for p in (OUT.parent / 'chapters').glob('*.md')}
    changed_readings = [r['source'] for r in chapters if (ROOT/r['source']).exists()
                        and digest((ROOT/r['source']).read_bytes()) != r['source_sha256']]
    outputs = catalogue_outputs(m, manifest, sources)
    for path, body in outputs.items():
        path.write_text(body)
    write_json(INVENTORY, {
        'schema_version': 1, 'captured_at_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Same path-based roles as build_lean_catalogue.py. No compilation or semantic equivalence verification. Repeated headers are candidates only: namespaces, local variables, definitions and interpretation can differ.',
        'statistics': manifest['statistics'],
        'baseline_statistics': read(BASELINE)['statistics'],
        'active_sources': active,
        'byte_identical_active_groups': [v for v in by_bytes.values() if len(v) > 1],
        'matching_header_candidates': candidates,
        'source_read_races_excluded_from_header_scan': source_read_races,
        'chapter_reading_coverage': {'registered': len(registered), 'current': len(current),
            'unregistered': sorted(current-registered), 'changed_since_reading': changed_readings},
        'catalogue_output_sha256': {str(p.relative_to(ROOT)): digest(body.encode()) for p, body in outputs.items()},
        'session_snapshot_sha256': digest(SNAPSHOT.read_bytes()),
    })


def link(label, path):
    return f'[{label}]({os.path.relpath(ROOT/path, OUT)})'


def heading(marks, text, former=None):
    return (marks, text, text if former is None else former)


def finish(lines):
    import sys
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from tools.research.registry import finish as join
    return join(lines)


MARKER = '<!-- Generated by tools/research/session_map.py (make research-render). Edit data/session-results.json, not this view. -->'


def en(item, field):
    """The English of a paired field, or its Chinese where no English exists."""
    value = item.get(field + '_en')
    return value if isinstance(value, str) and value.strip() else item.get(field + '_zh', '')


def render(data, inv):
    s = inv['statistics']
    H = heading
    migrated = [read(p) for p in sorted((OUT/'records').glob('*.json'))]
    lines = [H('#', 'Session outcomes and proof reuse', '会话成果与证明复用地图 Session outcomes and proof reuse'), '', MARKER, '',
        '8 October 2026 · Research direction: Ren. Mapping and documentary audit: AI-authored.', '',
        '[Current canonical records](RESULT-REGISTER.md) maintain migrated claims. This map preserves its dated chat coverage; the family links below add navigation to migrated records without expanding the snapshot.', '',
        en(data, 'scope'), '',
        '**Most recent outcomes have research or theory entries. Formal composition is assessed claim by claim. Verification copies and repeated acceptances are not additional proofs.**', '',
        link('Audit and consolidation decisions', str((HERE/'SESSION-INTEGRATION-AUDIT.md').relative_to(ROOT))) + ' · ' +
        link('Recorded chat outcomes', str(SNAPSHOT.relative_to(ROOT))) + ' · ' +
        link('Proof inventory', str(INVENTORY.relative_to(ROOT))), '',
        H('##', 'Inventory scope', '清点范围 Inventory scope'), '',
        f"Snapshot UTC: `{inv['captured_at_utc']}`. Paths are documentary units, not independent theorems.", '',
        '| Item | Count |', '|---|---:|',
        f"| Mapped chats | {len(data['sessions'])} |",
        f"| Result families | {len(data['families'])} |",
        f"| Working Lean sources | {s['roles']['working-source']} |",
        f"| Audit drivers | {s['roles']['audit-driver']} |",
        f"| Saved verification or build copies | {s['roles'].get('saved-copy', 'not listed; bound by their receipts')} |",
        f"| Exact duplicate groups among working sources and audit drivers | {len(inv['byte_identical_active_groups'])} |", '',
        'No semantic duplicate percentage is asserted. Header matches are review candidates, not proofs of equivalence. "New result" denotes a repository contribution, not a literature novelty claim. Argument, application, counterexample and reuse can occur together, so the class counts must not be summed as discoveries.', '',
        H('##', 'Reviewed proof reuse', '已判定的证明复用 Reviewed proof reuse'), '',
        '| Relation | Canonical and related names | Decision |', '|---|---|---|']
    for p in data.get('proof_reuse', []):
        lines.append(f"| {p['id']} · {p['classification']} | {link(p['canonical_declaration'], p['canonical_source'])} · {link(p['related_declaration'], p['related_source'])} | {en(p, 'finding')} |")
    lines += ['',
        f"The header scan retains {len(inv['matching_header_candidates'])} candidate groups. These match text after removing the theorem name; local definitions and implicit contexts are not resolved. The decisions above are source-inspected examples, not a claim that all candidates are duplicates. Frozen evidence copies are outside the working-source class; conservation, trajectory and support proofs over different local definitions remain separate.", '',
        H('##', 'Find a chat outcome', '按会话定位 Find a chat outcome'), '',
        'Titles below preserve the app titles exactly, in their original language. They identify provenance, not the current scientific scope. Active chat work after the recorded turns is outside this snapshot.', '',
        '| Chat | Family and class | Outcome | Entry and integration |', '|---|---|---|---|']
    for r in data['sessions']:
        title = r['title'].replace('|', '\\|')
        lines.append(f"| {title} | [{r['family']}](#{r['family'].lower()}) · {', '.join(r['classification'])} | {en(r, 'outcome')} | {link('Source', r['primary_source'])} · {r['integration']} |")
    lines += ['', 'Integration labels: **canonical** = recorded theory entry; **study-and-canonical** = study linked into the theory; **study-context** = an existing study supports the discussion; **discussion-context-only** = contextual entry, without a claim that the whole discussion was separately integrated; **review/preservation/export/historical-release** retain those documentary roles. A session with only a context link is not counted as fully integrated.', '',
              H('##', 'Reuse by claim family', '按命题复用 Reuse by claim family'), '']
    for f in data['families']:
        lines += [f"<a id=\"{f['id'].lower()}\"></a>", '', H('###', f"{f['id']} {en(f, 'title')}", f"{f['id']} {f['title_zh']} {f['title_en']}"), '',
            f['claim_en'], '', '**Hypotheses:** '+f['hypotheses_en'], '',
            '**Canonical reuse entries:** '+ ' · '.join(link(Path(p).stem, p) for p in f['canonical_sources']), '',
            '**Consolidation:** '+f['reuse_en'], '', '**Scope still separate:** '+f['remaining_en'], '']
        matches = [r for r in migrated if r['family'] == f['id']]
        if matches:
            lines += ['**Migrated records:** ' + ' · '.join(f'[{r["id"]}](records/{r["id"]}.md)' for r in matches), '']
    c = inv['chapter_reading_coverage']
    lines += [H('##', 'Reading edition coverage', '双语阅读版的覆盖 Reading edition coverage'), '',
        f"At this checkpoint the reading registers contained {c['registered']} chapters and the chapter directory {c['current']}. {len(c['changed_since_reading'])} registered chapters differed from their recorded reading hashes. Old reading hashes are not relabelled as reviewed; the [reading catalogue](README.md) marks entries whose source changed since. The additional chapters of that checkpoint:", '',
        '| Additional chapter |', '|---|']
    for p in c['unregistered']:
        lines.append('| '+link(Path(p).stem, moves_current(p))+' |')
    lines += ['', H('##', 'Maintenance', '维护 Maintenance'), '',
        'Edit `data/session-results.json` for dated session classifications and provenance links. Maintain migrated claim status only in `records/<id>.json`; record links above are generated from those files. Capture new chat evidence explicitly before broadening session coverage. Inventory refreshes do not certify proof validity.', '',
        '```sh', 'make research-render                                # writes this page with the other generated views', 'python3 -B tools/research/session_map.py --check   # snapshot checks; writes nothing', '```', '',
        'No theoretical claim or generativity-chain entry changes in this documentary consolidation. Existing scientific validation and pending source reviews retain their scopes.', '']
    return finish(lines)


def moves_current(path):
    """`path`, or where the move receipts moved it."""
    import sys
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from tools.research import moves
    return moves.current_path(path, ROOT)


def render_output():
    """{repository path: body} for `research.py render`."""
    return {str(REPORT.relative_to(ROOT)): render(read(DATA), read(INVENTORY))}


def check(data, inv, body, write=True):
    errors = []
    records = {r['id']:r for r in read(SNAPSHOT)['records']}
    ids = [r['thread_id'] for r in data['sessions']]
    if len(ids) != len(set(ids)) or set(ids) != set(records):
        errors.append('Session coverage mismatch or duplicate IDs')
    family_ids = {f['id'] for f in data['families']}
    for r in data['sessions']:
        if r['title'] != records[r['thread_id']]['title']:
            errors.append('Changed app title: '+r['thread_id'])
        if r['family'] not in family_ids:
            errors.append('Missing family: '+r['family'])
        available = {it['id'] for t in records[r['thread_id']]['turns'] for it in t['items'] if it['type']=='agentMessage'}
        if not set(r['evidence_message_ids']) <= available:
            errors.append('Unbound message IDs: '+r['thread_id'])
    for f in data['families']:
        for p in f['canonical_sources']:
            if not (ROOT/p).exists(): errors.append('Missing family source: '+p)
    manifest = read(OUT/'data/lean-index.json')
    indexed = {f['path']: f for f in manifest['files']}
    for p in data.get('proof_reuse', []):
        for prefix in ('canonical', 'related'):
            source, name = p[prefix+'_source'], p[prefix+'_declaration']
            entry = indexed.get(source)
            names = [] if entry is None else [d['qualified_name_hint'] for d in manifest['contents_by_sha256'][entry['sha256']]['declarations']]
            if name not in names: errors.append('Unresolved proof reuse declaration: '+source+' '+name)
    if not REPORT.exists() or REPORT.read_text() != body:
        errors.append('Result map rendering differs from recorded input')
    checked_links = 0
    for match in re.finditer(r'\[[^\]\n]*\]\(([^)]+)\)', body):
        target = match.group(1)
        if urlsplit(target).scheme: continue
        pathname, _, anchor = target.partition('#')
        if pathname and not (OUT/unquote(pathname)).resolve().exists():
            errors.append('Missing map target: '+target)
        if not pathname and anchor and f'id="{anchor}"' not in body:
            errors.append('Missing map anchor: '+target)
        checked_links += 1
    # The Lean catalogue is a live generated view (research.py render); its pages must be the
    # rendering of the saved inventory. The capture's `catalogue_output_sha256` records the pages
    # as they were at the dated capture and stays as evidence; the pages are not compared to it.
    m = module()
    sources = read(OUT/'data/source-index.json')
    for path, expected in catalogue_outputs(m, manifest, sources).items():
        key = str(path.relative_to(ROOT))
        if not path.exists() or path.read_text() != expected:
            errors.append('Lean catalogue page is not the rendering of data/lean-index.json: '+key)
    missing_inventory_paths = [f['path'] for f in manifest['files'] if not (ROOT/f['path']).exists()]
    if missing_inventory_paths:
        errors.extend('Missing inventoried path: '+p for p in missing_inventory_paths)
    live_changed = [f['path'] for f in inv['active_sources'] if not (ROOT/f['path']).exists()
                    or digest((ROOT/f['path']).read_bytes()) != f['sha256']]
    result = {'checked_at_utc': datetime.now(timezone.utc).isoformat(), 'passed':not errors,
        'errors':errors, 'mapped_chats':len(ids), 'families':len(family_ids), 'local_map_links_checked':checked_links,
        'inventory_paths_checked':len(manifest['files']),
        'live_active_sources_changed_after_capture':live_changed,
        'semantics':'Snapshot documentary checks, not theorem validity, whole-repository freshness or independent scientific review.',
        'input_sha256':{str(p.relative_to(ROOT)):digest(p.read_bytes()) for p in [DATA,SNAPSHOT,INVENTORY,REPORT]}}
    if write:
        write_json(CHECKS,result)
    print(json.dumps({k:v for k,v in result.items() if k!='input_sha256'},ensure_ascii=False,indent=2))
    return 0 if not errors else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--capture',action='store_true')
    parser.add_argument('--check',action='store_true')
    args = parser.parse_args()
    if args.capture: capture()
    data, inv = read(DATA), read(INVENTORY)
    body = render(data,inv)
    if not args.check: REPORT.write_text(body)
    # --check writes nothing; a writing run also records its check result in CHECKS.
    return check(data,inv,body,write=not args.check)


if __name__ == '__main__':
    raise SystemExit(main())
