#!/usr/bin/env python3
"""Capture documentary inventory and render the cross-session result map.

--capture refreshes the Lean navigation from one inventory and records a dated
checkpoint. --check checks that checkpoint's rendering and local links; changed
live sources are reported separately, never silently certified or overwritten.
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
HERE = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation'
OUT = ROOT / 'theories/becoming/results'
DATA = OUT / 'data/session-results.json'
SNAPSHOT = HERE / 'SESSION-OUTCOME-SNAPSHOT.json'
INVENTORY = HERE / 'SESSION-PROOF-OVERLAP.json'
BASELINE = HERE / 'SESSION-INTEGRATION-BASELINE.json'
CHECKS = HERE / 'SESSION-RESULT-MAP-CHECKS.json'
REPORT = OUT / 'SESSION-RESULTS.md'


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
    files = {
        OUT / 'data/lean-index.json': json.dumps(manifest, ensure_ascii=False, indent=2) + '\n',
        OUT / 'data/source-index.json': json.dumps(sources, ensure_ascii=False, indent=2) + '\n',
        OUT / 'LEAN-INDEX.md': m.render_index(manifest, sources),
        OUT / 'LEAN-DECLARATIONS.md': m.render_declarations(manifest, sources),
    }
    for key in m.GROUPS:
        files[OUT / 'lean-declarations' / (key + '.md')] = m.render_declarations(manifest, sources, key)
    return files


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


def render(data, inv):
    s = inv['statistics']
    migrated = [read(p) for p in sorted((OUT/'records').glob('*.json'))]
    lines = ['# 会话成果与证明复用地图 Session outcomes and proof reuse', '',
        '2026-10-08 · Research direction: Ren. Mapping and documentary audit: AI-authored.', '',
        '[Current canonical records / 当前成果记录](RESULT-REGISTER.md) maintain migrated claims. This map preserves its dated chat coverage; family links below add navigation to migrated records without expanding the snapshot. / 已迁移主张以成果记录维护；以下成果族链接只补充导航，不扩大会话快照范围。', '',
        data['scope_zh'], '', data['scope_en'], '',
        '**结论：多数近期成果已有正文入口；形式连接须逐项判断。验证副本与重复验收不计作新证明。**', '',
        '**Most recent outcomes have research or theory entries. Formal composition is assessed claim by claim. Verification copies and repeated acceptances are not additional proofs.**', '',
        link('Audit and consolidation decisions / 审计及整合决定', str((HERE/'SESSION-INTEGRATION-AUDIT.md').relative_to(ROOT))) + ' · ' +
        link('Recorded chat outcomes / 会话成果记录', str(SNAPSHOT.relative_to(ROOT))) + ' · ' +
        link('Proof inventory / 证明清单', str(INVENTORY.relative_to(ROOT))), '',
        '## 清点范围 Inventory scope', '',
        f"Snapshot UTC: `{inv['captured_at_utc']}`. Paths are documentary units, not independent theorems.", '',
        '| Item / 项目 | Count / 数量 |', '|---|---:|',
        f"| Mapped chats / 已映射会话 | {len(data['sessions'])} |",
        f"| Result families / 成果族 | {len(data['families'])} |",
        f"| Working Lean sources / 工作源码 | {s['roles']['working-source']} |",
        f"| Audit drivers / 审计入口 | {s['roles']['audit-driver']} |",
        f"| Saved verification or build copies / 检查及构建副本 | {s['roles'].get('saved-copy', 'not listed; bound by their receipts / 不列入，由回执绑定')} |",
        f"| Exact duplicate groups among working sources and audit drivers / 当前源及审计入口相同字节组 | {len(inv['byte_identical_active_groups'])} |", '',
        'No semantic duplicate percentage is asserted. Header matches are review candidates, not proofs of equivalence. New-result denotes a repository contribution, not a literature novelty claim. The result classes may overlap; their counts must not be summed as discoveries.', '',
        '“新成果”仅指仓库中的增量；论证、应用、反例和复用可以同时出现，不将它们简单相加成独立发现数。', '',
        '## 已判定的证明复用 Reviewed proof reuse', '',
        '| Relation / 关系 | Canonical and related names / 原声明及关联名 | Decision / 判定 |', '|---|---|---|']
    for p in data.get('proof_reuse', []):
        lines.append(f"| {p['id']} · {p['classification']} | {link(p['canonical_declaration'], p['canonical_source'])} · {link(p['related_declaration'], p['related_source'])} | {p['finding_zh']} {p['finding_en']} |")
    lines += ['',
        f"The header scan retains {len(inv['matching_header_candidates'])} candidate groups. These match text after removing the theorem name; local definitions and implicit contexts are not resolved. The decisions above are source-inspected examples, not a claim that all candidates are duplicates.", '',
        '声明外形相同只是比较线索。冻结证据副本已从工作源类别移出；不同局部定义的守恒、轨迹和支持证明继续分别保留。', '',
        '## 按会话定位 Find a chat outcome', '',
        'Titles below preserve the app titles exactly. They identify provenance, not the current scientific scope. Active chat work after the recorded turns is outside this snapshot.', '',
        '| Chat / 会话 | Family and class / 成果族与类别 | Outcome / 成果 | Entry and integration / 入口与整合 |', '|---|---|---|---|']
    for r in data['sessions']:
        title = r['title'].replace('|', '\\|')
        lines.append(f"| {title} | [{r['family']}](#{r['family'].lower()}) · {', '.join(r['classification'])} | {r['outcome_zh']} {r['outcome_en']} | {link('Source / 来源', r['primary_source'])} · {r['integration']} |")
    lines += ['', 'Integration labels: **canonical** = recorded theory entry; **study-and-canonical** = study linked into the theory; **study-context** = an existing study supports the discussion; **discussion-context-only** = contextual entry, without a claim that the whole discussion was separately integrated; **review/preservation/export/historical-release** retain those documentary roles.', '',
              '整合标签区分当前正文、已连接研究、讨论上下文、验收、保存及输出；不会把只有上下文链接的会话自动升级为完整整合。', '',
              '## 按命题复用 Reuse by claim family', '']
    for f in data['families']:
        lines += [f"<a id=\"{f['id'].lower()}\"></a>", '', f"### {f['id']} {f['title_zh']} {f['title_en']}", '',
            f['claim_en'], '', '**Hypotheses / 前提:** '+f['hypotheses_en'], '',
            '**Canonical reuse entries / 复用入口:** '+ ' · '.join(link(Path(p).stem, p) for p in f['canonical_sources']), '',
            '**Consolidation / 整合:** '+f['reuse_en'], '', '**Scope still separate / 保留范围:** '+f['remaining_en'], '']
        matches = [r for r in migrated if r['family'] == f['id']]
        if matches:
            lines += ['**Migrated records / 已迁移条目:** ' + ' · '.join(f'[{r["id"]}](records/{r["id"]}.md)' for r in matches), '']
    c = inv['chapter_reading_coverage']
    lines += ['## 双语阅读版的覆盖 Reading edition coverage', '',
        f"The earlier reading registers contain {c['registered']} chapters; the current directory contained {c['current']} at this checkpoint. {len(c['changed_since_reading'])} registered chapters differ from their recorded reading hashes. The Lean navigation is refreshed; old reading hashes are not relabeled as reviewed.", '',
        '旧阅读版的逐章摘要保留其核读版本；新增章节在下方单列，现有摘要的待核读版本不以刷新哈希消除。', '',
        '| Additional chapter / 新增章节 |', '|---|']
    for p in c['unregistered']:
        lines.append('| '+link(Path(p).stem, p)+' |')
    lines += ['', '## 维护 Maintenance', '',
        'Edit `data/session-results.json` for dated session classifications and provenance links. Maintain migrated claim status only in `records/<id>.json`; record links above are generated from those files. Capture new chat evidence explicitly before broadening session coverage. Inventory refreshes do not certify proof validity.', '',
        '```sh', 'python3 -B _process/research/2026-10-05-generative-foundation-review/root-foundation/build_session_result_map.py --check', '```', '',
        'No theoretical claim or generativity-chain entry changes in this documentary consolidation. Existing scientific validation and pending source reviews retain their scopes.', '']
    return '\n'.join(lines)


def check(data, inv, body):
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
    m = module()
    sources = read(OUT/'data/source-index.json')
    for path, expected in catalogue_outputs(m, manifest, sources).items():
        key = str(path.relative_to(ROOT))
        if digest(expected.encode()) != inv['catalogue_output_sha256'].get(key) or path.read_text() != expected:
            errors.append('Catalogue snapshot rendering mismatch: '+key)
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
    return check(data,inv,body)


if __name__ == '__main__':
    raise SystemExit(main())
