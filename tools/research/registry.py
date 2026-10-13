#!/usr/bin/env python3
"""Render and check canonical claim records. Never compiles Lean or refreshes hashes.

Run from any directory. --check is read-only; --search searches claims and aliases.
Exit 1: invalid metadata/rendering. Exit 2: reviewed source bytes changed.
Source hashes mark documentary review, not a proof build or semantic equivalence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'theories/becoming/results'
RECORDS = OUT / 'records'
STATUSES = {'recorded-checked', 'reviewed-scoped', 'open', 'superseded', 'withdrawn'}
KINDS = {'theorem', 'argument', 'assessment', 'target'}
RELATIONS = {'formal-reuse', 'application', 'interpretive'}
ROLES = {'statement', 'proof', 'receipt', 'review', 'integration', 'counterexample', 'provenance'}
# Schema 1 keeps its fields; schema 2 leads with a short statement and splits limitations
# into typed items, shared boundary keys, target scope and progress (see RESULT-WORKFLOW.md).
REQUIRED = {1: ('title', 'claim', 'correspondence', 'limitations', 'next_delta', 'validation_scope'),
            2: ('title', 'statement', 'correspondence', 'next_delta', 'validation_scope')}
V2_LISTS = ('laws', 'does_not_show', 'not_required', 'progress', 'standard_boundaries', 'text_versions')
NOT_SHOWN = {'non-implication', 'converse', 'correspondence', 'scope'}
SHA256 = re.compile(r'[0-9a-f]{64}')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pair(value):
    return isinstance(value, dict) and all(isinstance(value.get(k), str) and value[k].strip() for k in ('zh', 'en'))


def bilingual(value):
    return value['zh'] + ' / ' + value['en']


def valid_overview(value):
    return isinstance(value, dict) and all(pair(value.get(key)) for key in ('title', 'summary', 'evidence'))


def path_in_repo(value):
    if not isinstance(value, str) or not value or Path(value).is_absolute():
        return None
    p = (ROOT / value).resolve()
    return p if p.is_relative_to(ROOT) and p.is_file() else None


def at_pointer(value, pointer):
    for token in pointer.strip('/').split('/'):
        token = token.replace('~1', '/').replace('~0', '~')
        value = value[int(token)] if isinstance(value, list) else value[token]
    return value


def declaration_in_source(text, name):
    """Existence aid only; receipt bindings check the full elaborated name.

    Lean instances may have a name and a priority before that name. Require the
    actual identifier after the command, so an anonymous instance's result type
    or binder cannot be mistaken for a named declaration.
    """
    command = (r'(?:theorem|lemma|def|abbrev|structure|inductive|'
               r'instance(?:\s+\(priority\s*:=\s*[^)\n]+\))?)')
    return re.search(
        r'^[ \t]*(?:@\[[^\]\n]*\]\s*)*'
        r'(?:(?:protected|private|noncomputable)\s+)*' + command +
        r'\s+(?:[\w\'.]+\.)?' + re.escape(name.split('.')[-1]) +
        r'(?=\s|\{|\(|\[|:)', text, re.M) is not None


def config():
    return json.loads((ROOT / '_process/research-config.json').read_text())


def standard_boundaries_path(settings=None):
    path = (config() if settings is None else settings).get('standard_boundaries')
    return path if isinstance(path, str) else None


def standard_boundaries(settings=None):
    """Shared bilingual boundary sentences, defined once and cited by key."""
    path = standard_boundaries_path(settings)
    if path is None or path_in_repo(path) is None:
        return {}
    try:
        data = json.loads((ROOT / path).read_text())
    except ValueError:
        return {}
    return data.get('boundaries', {}) if isinstance(data, dict) and isinstance(data.get('boundaries'), dict) else {}


def validate_standard_boundaries(settings=None):
    path = standard_boundaries_path(settings)
    if path is None:
        return []
    p = path_in_repo(path)
    if p is None:
        return [f'standard boundaries file missing: {path}']
    try:
        data = json.loads(p.read_text())
    except ValueError as exc:
        return [f'standard boundaries file is not JSON: {exc}']
    if not isinstance(data, dict) or not isinstance(data.get('boundaries'), dict):
        return ['standard boundaries file needs a "boundaries" object']
    errors = []
    for key, value in data['boundaries'].items():
        if not re.fullmatch(r'[a-z][a-z0-9-]+', key):
            errors.append(f'standard boundary key is not a stable name: {key}')
        if not pair(value):
            errors.append(f'standard boundary {key} requires nonempty Chinese and English')
        elif path_in_repo(value.get('source')) is None:
            errors.append(f'standard boundary {key} needs an existing source')
    return errors


def snapshot_directory(settings=None):
    path = (config() if settings is None else settings).get('record_snapshots')
    return path.rstrip('/') if isinstance(path, str) and path.strip('/') else None


def validate_v2_fields(r, settings=None):
    """Structure of the schema-2 fields; readability rules come from style.lint."""
    settings = config() if settings is None else settings
    errors = []
    if 'limitations' in r:
        errors.append('schema 2 replaces limitations with does_not_show, hypotheses, standard_boundaries and not_required')
    if 'claim' in r and not pair(r['claim']):
        errors.append('claim, when present, requires nonempty Chinese and English')
    malformed = [key for key in V2_LISTS if not isinstance(r.get(key, []), list)]
    if malformed:
        return errors + ['expected lists: ' + ', '.join(malformed)]
    if any(not isinstance(x, dict) for key in V2_LISTS if key != 'standard_boundaries' for x in r.get(key, [])):
        return errors + ['laws, does_not_show, not_required, progress and text_versions entries must be objects']
    for key in ('laws', 'does_not_show', 'not_required', 'progress'):
        if not all(pair(item) for item in r.get(key, [])):
            errors.append(f'{key} items require nonempty Chinese and English')
    references = [x for x in r.get('references', []) if isinstance(x, dict)]
    paths = {x.get('path') for x in references}
    declared = {d for x in references for d in x.get('declarations', []) if isinstance(d, str)}
    for item in r.get('laws', []):
        names = item.get('declarations', [])
        if not isinstance(names, list):
            errors.append('law declarations must be a list')
            continue
        unknown = [d for d in names if not isinstance(d, str) or d not in declared]
        if unknown:
            errors.append('law names undeclared references: ' + ', '.join(map(str, unknown)))
    for item in r.get('does_not_show', []):
        if not isinstance(item.get('kind'), str) or item['kind'] not in NOT_SHOWN:
            errors.append(f'does_not_show kind must be one of {", ".join(sorted(NOT_SHOWN))}')
        if 'witness' in item and (not isinstance(item['witness'], str) or item['witness'] not in declared | set(map(str, r.get('aliases', [])))):
            errors.append(f'does_not_show witness is not a declared reference or alias: {item["witness"]}')
    from tools.research.reading_catalogue import anchors
    for item in r.get('progress', []):
        source = item.get('source')
        file, _, anchor = source.partition('#') if isinstance(source, str) else ('', '', '')
        if file not in paths:
            errors.append(f'progress source must be a hashed reference: {source}')
        elif anchor and file.endswith('.md') and anchor not in anchors(ROOT / file):
            errors.append(f'progress anchor missing: {source}')
    known = standard_boundaries(settings)
    keys = r.get('standard_boundaries', [])
    if len(keys) != len(set(map(str, keys))):
        errors.append('standard_boundaries lists a key twice')
    for key in keys:
        if not isinstance(key, str) or key not in known:
            errors.append(f'unknown standard boundary {key}')
    directory = snapshot_directory(settings)
    for version in r.get('text_versions', []):
        path, expected = version.get('path'), version.get('sha256')
        p = path_in_repo(path)
        if not pair(version.get('note')):
            errors.append('text version needs a bilingual note')
        if p is None or not isinstance(expected, str) or not SHA256.fullmatch(expected) or digest(p) != expected:
            errors.append(f'text version missing or changed: {path}')
            continue
        if directory is None or not path.startswith(directory + '/'):
            errors.append(f'text version must be stored under record_snapshots ({directory}): {path}')
        try:
            earlier = json.loads(p.read_text())
        except ValueError:
            earlier = None
        if not isinstance(earlier, dict) or earlier.get('id') != r.get('id'):
            errors.append(f'text version is not an earlier version of this record: {path}')
    return errors


def snapshot_record(ident, settings=None):
    """Store a record's exact current bytes before migration; return its text_versions entry.

    The copy lives at <record_snapshots>/<sha256[:16]>/<id>.json, next to the preserved
    overview editions, and is never overwritten. The record itself is not edited.
    """
    settings = config() if settings is None else settings
    if not re.fullmatch(r'[a-z][a-z0-9-]+', ident):
        raise ValueError('not a record id: ' + ident)
    directory = snapshot_directory(settings)
    if directory is None:
        raise ValueError('record_snapshots is not configured in _process/research-config.json')
    source = next((ROOT / d / (ident + '.json') for d in settings['record_directories'] if (ROOT / d / (ident + '.json')).is_file()), None)
    if source is None:
        raise ValueError('no record with id ' + ident)
    raw = source.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    target = ROOT / directory / sha[:16] / source.name
    if target.exists() and target.read_bytes() != raw:
        raise ValueError('Refusing to overwrite preservation artifact: ' + str(target.relative_to(ROOT)))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(raw)
    schema = json.loads(raw).get('schema_version')
    return {'path': str(target.relative_to(ROOT)), 'sha256': sha,
            'note': {'zh': f'迁移前的记录原始字节（schema {schema}）。', 'en': f'Exact record bytes before the migration (schema {schema}).'}}


def validate(records):
    from tools.research import style
    errors, drift = [], []
    ids, aliases = {}, {}
    settings = config()
    errors += validate_standard_boundaries(settings)
    for r in records:
        ident = r.get('id', '<missing>')
        def fail(message):
            errors.append(f'{ident}: {message}')
        if not isinstance(ident, str) or not re.fullmatch(r'[a-z][a-z0-9-]+', ident):
            fail('invalid stable id')
        if ident in ids:
            fail('duplicate id')
        ids[ident] = r
        schema = r.get('schema_version')
        if type(schema) is not int or schema not in REQUIRED or r.get('kind') not in KINDS or r.get('status') not in STATUSES:
            fail('invalid schema, kind or status')
        v2 = schema == 2
        malformed = [key for key in ('hypotheses', 'history', 'aliases', 'references', 'dependencies', 'related', 'counterexamples') if not isinstance(r.get(key), list)]
        if malformed:
            fail('expected lists: ' + ', '.join(malformed))
            ids.pop(ident, None)
            continue
        if any(not isinstance(x, dict) for key in ('references', 'dependencies', 'related', 'counterexamples') for x in r[key]):
            fail('reference, edge and boundary entries must be objects')
            ids.pop(ident, None)
            continue
        if r.get('kind') == 'target' and r.get('status') not in {'open', 'superseded', 'withdrawn'}:
            fail('a target cannot be marked completed')
        for key in REQUIRED[2 if v2 else 1]:
            if not pair(r.get(key)):
                fail(f'{key} requires nonempty Chinese and English')
        if v2:
            for message in validate_v2_fields(r, settings):
                fail(message)
        else:
            if 'statement' in r and not pair(r['statement']):
                fail('statement, when present, requires nonempty Chinese and English')
            later = [key for key in V2_LISTS if key in r]
            if later:
                fail('schema-2 fields need schema_version 2: ' + ', '.join(later))
        for finding in style.lint(r):
            if finding['severity'] == 'error':
                fail(f'{finding["field"]}: {finding["rule"]}: {finding["detail"]}')
        if 'overview' in r and not valid_overview(r['overview']):
            fail('overview requires bilingual title, summary and evidence')
        if not r.get('hypotheses') or not all(pair(x) for x in r['hypotheses']):
            fail('explicit bilingual hypotheses required')
        if not re.fullmatch(r'F\d\d', r.get('family', '')):
            fail('session-map family required')
        if not isinstance(r.get('reviewed_at_utc'), str) or not r['reviewed_at_utc'].endswith('+00:00'):
            fail('UTC documentary review timestamp required')
        if not r.get('history') or not all(pair(x) for x in r['history']):
            fail('bilingual provenance/history required')
        for alias in [ident] + r.get('aliases', []):
            if not isinstance(alias, str) or not alias.strip():
                fail('invalid alias')
                continue
            key = alias.casefold()
            if key in aliases:
                fail(f'duplicate alias {alias!r}; already owned by {aliases[key]}')
            aliases[key] = ident
        refs = r.get('references', [])
        paths, roles = set(), set()
        for ref in refs:
            path, role = ref.get('path'), ref.get('role')
            if path in paths:
                fail(f'duplicate reference {path}')
            paths.add(path)
            roles.add(role)
            if role not in ROLES:
                fail(f'invalid reference role {role}')
            p = path_in_repo(path)
            if p is None:
                fail(f'missing or unsafe reference {path}')
                continue
            expected = ref.get('sha256', '')
            if not re.fullmatch(r'[0-9a-f]{64}', expected):
                fail(f'invalid reviewed hash {path}')
            elif digest(p) != expected:
                drift.append({'id': ident, 'path': path, 'reviewed_sha256': expected, 'current_sha256': digest(p)})
            for name in ref.get('declarations', []):
                if not declaration_in_source(p.read_text(), name):
                    fail(f'declaration not found: {name} in {path}')
        if r.get('canonical_source') not in paths:
            fail('canonical source must be a hashed reference')
        if r.get('status') == 'recorded-checked' and not {'proof', 'receipt'} <= roles:
            fail('recorded-checked needs proof source and existing receipt')
        if r.get('status') == 'recorded-checked' and not r.get('proof_bindings'):
            fail('recorded-checked needs a source hash binding in its existing receipt')
        refs_by_path = {x['path']: x for x in refs}
        listed = set()
        for binding in r.get('proof_bindings', []):
            try:
                source = refs_by_path[binding['source']]
                receipt = refs_by_path[binding['receipt']]
                if source['role'] != 'proof' or receipt['role'] != 'receipt':
                    raise ValueError('binding roles must be proof and receipt')
                data = json.loads((ROOT / receipt['path']).read_text())
                if at_pointer(data, binding['sha256_pointer']) != source['sha256']:
                    raise ValueError('receipt does not bind the reviewed proof source')
                if at_pointer(data, binding['success_pointer']) != binding['success_value'] or binding['success_value'] not in (True, 'passed'):
                    raise ValueError('receipt has no recorded success at the specified field')
                # Where the receipt lists the declarations Lean elaborated for the bound
                # module, each declaration the record names must be among them by full name.
                module = binding['sha256_pointer'].rsplit('/', 1)[-1]
                elaborated = {d.get('name') for m in data.get('modules', []) if isinstance(m, dict) and m.get('module') == module
                              for d in m.get('declarations', []) if isinstance(d, dict)}
                listed |= {d.get('name') for m in data.get('modules', []) if isinstance(m, dict)
                           for d in m.get('declarations', []) if isinstance(d, dict) and d.get('name')}
                unknown = [n for n in source.get('declarations', []) if elaborated and n not in elaborated]
                if unknown:
                    raise ValueError(f'declarations not elaborated in {module}: {", ".join(unknown)}')
            except (KeyError, IndexError, ValueError, TypeError, OSError) as exc:
                fail(f'invalid proof receipt binding: {exc}')
        # An alias written as a Lean name, in a namespace the bound receipts list, must be
        # among the declarations they list.
        roots = {n.split('.')[0] for n in listed}
        for alias in r.get('aliases', []):
            if isinstance(alias, str) and re.fullmatch(r"[A-Za-z_][\w']*(?:\.[\w'!?]+)+", alias) \
                    and alias.split('.')[0] in roots and alias not in listed:
                fail(f'alias not elaborated in the bound receipts: {alias}')
        if r.get('status') == 'reviewed-scoped' and not {'statement', 'review'} <= roles:
            fail('reviewed-scoped needs statement and review')
        if not isinstance(r.get('dependencies'), list) or not isinstance(r.get('related'), list):
            fail('dependencies and related must be explicit lists')
        if not isinstance(r.get('counterexamples'), list) or not (r.get('counterexamples') or (v2 and r.get('does_not_show'))):
            fail('counterexamples or explicit scoped boundary required')
        for c in r.get('counterexamples', []):
            if not pair(c.get('detail')) or c.get('path') not in paths:
                fail('counterexample/boundary needs bilingual scope and a hashed source')
    for ident, r in ids.items():
        for edge in r.get('dependencies', []) + r.get('related', []):
            if edge.get('id') not in ids or edge.get('id') == ident:
                errors.append(f'{ident}: missing or self result link {edge.get("id")}')
            if not pair(edge.get('detail')):
                errors.append(f'{ident}: result link needs bilingual scope')
        for edge in r.get('dependencies', []):
            if edge.get('relation') not in RELATIONS:
                errors.append(f'{ident}: dependency requires an explicit relation type')
            if 'interface' in edge:
                contract = edge['interface']
                if not isinstance(contract, dict) or not all(pair(contract.get(k)) for k in ('output', 'input', 'conditions')):
                    errors.append(f'{ident}: dependency interface needs bilingual output, input and conditions')
                elif contract.get('evidence') not in {x['path'] for x in r['references']}:
                    errors.append(f'{ident}: dependency interface evidence must be a reviewed reference')
        if r.get('status') == 'superseded' and r.get('superseded_by') not in ids:
            errors.append(f'{ident}: superseded status needs replacement id')
    # Only declared dependencies are directed inference edges; analogies are separate.
    visiting, done = set(), set()
    def visit(ident):
        if ident in visiting:
            errors.append(f'{ident}: circular result dependency')
            return
        if ident in done or ident not in ids:
            return
        visiting.add(ident)
        for edge in ids[ident].get('dependencies', []):
            visit(edge.get('id'))
        visiting.remove(ident)
        done.add(ident)
    for ident in ids:
        visit(ident)
    return errors, drift


def link(path, base, label=None):
    return f'[{label or Path(path).name}]({os.path.relpath(ROOT / path, base)})'


def statement_lines(statement):
    return ['> ' + statement['en'], '>', '> ' + statement['zh'], '']


def render_record_v2(r):
    """Schema 2: what the result does first, then exact conditions; sources and history folded."""
    base = record_path(r).parent
    def result_link(ident):
        target = r.get('_record_links', {}).get(ident)
        return link(str(Path(target).with_suffix('.md')), base, ident) if target else f'[{ident}]({ident}.md)'
    def both(value):
        return value['en'] + '<br>' + value['zh']
    def anchored(source):
        file, sep, anchor = source.partition('#')
        return f'[study]({os.path.relpath(ROOT / file, base)}{sep}{anchor})'
    lines = [f'# {r["title"]["en"]} / {r["title"]["zh"]}', '',
             '<!-- Generated by tools/research/registry.py; edit the matching JSON record. -->', '',
             f'`{r["id"]}` · **{r["status"]}** · {r["kind"]} · {r["family"]} · [record]({r["id"]}.json) · ' + link('RESULTS.md', base, 'register'), '']
    lines += statement_lines(r['statement'])
    if 'overview' in r:
        o = r['overview']
        lines += ['<details><summary>README overview / 首页摘要</summary>', '', '**' + bilingual(o['title']) + '**', '',
                  bilingual(o['summary']), '', '**Evidence / 证据:** ' + bilingual(o['evidence']), '', '</details>', '']
    progress = ['## Progress / 已接通', ''] + [f'{i}. ' + both(x) + ' ' + anchored(x['source']) for i, x in enumerate(r.get('progress', []), 1)] + ['']
    if r.get('progress') and r['kind'] == 'target':
        lines += progress  # for an open target, what is already connected comes first
    if 'claim' in r:
        lines += ['## Exact statement / 确切陈述', '', r['claim']['en'], '', r['claim']['zh'], '']
    if r.get('laws'):
        lines += ['## Laws / 规律', '']
        for i, law in enumerate(r['laws'], 1):
            names = ', '.join('`' + d + '`' for d in law.get('declarations', []))
            lines += [f'{i}. ' + both(law) + (f' ({names})' if names else '')]
        lines += ['']
    lines += ['## Conditions / 条件', '']
    lines += ['- ' + both(x) for x in r['hypotheses']]
    if r.get('not_required'):
        lines += ['', '**Not required by this target / 本目标不要求:**', '']
        lines += ['- ' + both(x) for x in r['not_required']]
    if r.get('does_not_show') or r.get('counterexamples'):
        lines += ['', '## Does not show / 未表明', '']
        lines += ['- ' + both(x) + (f' Witness: `{x["witness"]}`.' if x.get('witness') else '') for x in r.get('does_not_show', [])]
        lines += ['- **Counterexample / 反例:** ' + both(c['detail']) + ' ' + link(c['path'], base, 'source') for c in r['counterexamples']]
    if r.get('standard_boundaries'):
        known = standard_boundaries()
        lines += ['', '**Standard boundaries / 通用边界:** ' + ' · '.join(known[k]['en'] + ' ' + known[k]['zh'] for k in r['standard_boundaries'])]
    if r.get('progress') and r['kind'] != 'target':
        lines += [''] + progress[:-1]
    lines += ['', '## Evidence / 证据', '', both(r['validation_scope']), '', 'Canonical source: ' + link(r['canonical_source'], base), '',
              '## Next / 下一步', '', both(r['next_delta']), '',
              '<details><summary>Correspondence, dependencies, sources and history / 对应、依赖、来源与沿革</summary>', '',
              '### Correspondence / 对应', '', both(r['correspondence']), '', '### Dependencies / 依赖', '']
    for e in r['dependencies']:
        lines += [f'- **{e["relation"]}**: {result_link(e["id"])}. {bilingual(e["detail"])}']
        if 'interface' in e:
            c = e['interface']
            lines += ['  - Output / 输出: ' + bilingual(c['output']), '  - Input / 输入: ' + bilingual(c['input']),
                      '  - Preserved conditions / 保留条件: ' + bilingual(c['conditions']) + ' ' + link(c['evidence'], base)]
    if not r['dependencies']:
        lines += ['- none / 无']
    lines += [f'- related, not a proved adapter / 关联而非已证转换: {result_link(e["id"])}. {bilingual(e["detail"])}' for e in r['related']]
    lines += ['', '### Sources / 来源', '', '| Role | Source | Declarations |', '|---|---|---|']
    lines += [f'| {x["role"]} | {link(x["path"], base)} | {", ".join("`" + d + "`" for d in x.get("declarations", [])) or "—"} |' for x in r['references']]
    lines += ['', 'Aliases / 别名: ' + (', '.join('`' + a + '`' for a in r['aliases']) or '—'), '', '### History / 沿革', '']
    lines += ['- ' + bilingual(h) for h in r['history']]
    if r.get('text_versions'):
        lines += ['', '### Earlier text / 早期文本', '']
        lines += ['- ' + link(v['path'], base, Path(v['path']).name) + f' (sha256 `{v["sha256"][:16]}…`): ' + bilingual(v['note']) for v in r['text_versions']]
    lines += ['', '</details>', '',
              f'Documentary review UTC: `{r["reviewed_at_utc"]}`. Hashes in the record bind the reviewed sources; the checker does not audit transitive Lean imports or establish premise warrant, and this page is not a proof receipt. / JSON 哈希绑定读过的版本；登记检查不审计全部 Lean 导入，也不证明前提根据；本页不是证明回执。']
    return '\n'.join(lines) + '\n'


def render_record(r):
    if r.get('schema_version') == 2:
        return render_record_v2(r)
    base = record_path(r).parent
    def result_link(ident):
        target = r.get('_record_links', {}).get(ident)
        return link(str(Path(target).with_suffix('.md')), base, ident) if target else f'[{ident}]({ident}.md)'
    lines = [f'# {bilingual(r["title"])}', '',
             '<!-- Generated by build_result_registry.py; edit the matching JSON record. -->', '']
    if 'statement' in r:
        lines += statement_lines(r['statement'])  # optional on schema 1: what the result does, first
    lines += [f'`{r["id"]}` · **{r["status"]}** · {r["kind"]} · {r["family"]}', '',
             f'记录源 / Editable record: [{r["id"]}.json]({r["id"]}.json) · ' + link('RESULTS.md', base, '登记表 / Register'), '',
             f'Documentary review UTC: `{r["reviewed_at_utc"]}`. Run the registry checker for source drift; this page is not a fresh proof receipt.', '']
    if 'overview' in r:
        overview = r['overview']
        lines += ['## Overview / 首页摘要', '', '**' + bilingual(overview['title']) + '**', '',
                  bilingual(overview['summary']), '', '**Evidence / 证据:** ' + bilingual(overview['evidence']), '']
    lines += ['## 主张 Claim', '', bilingual(r['claim']), '',
             'Canonical source: ' + link(r['canonical_source'], base), '',
             '## 前提与对应 Hypotheses and correspondence', '']
    lines += ['- ' + bilingual(x) for x in r['hypotheses']]
    lines += ['', bilingual(r['correspondence']), '', '## 检验与边界 Validation and boundaries', '', bilingual(r['validation_scope']), '', bilingual(r['limitations']), '']
    lines += [('Boundary source / 边界来源: ' if c['detail'] == r['limitations'] else '- ' + bilingual(c['detail']) + ' ') + link(c['path'], base) for c in r['counterexamples']]
    lines += ['', '## 依赖与关联 Dependencies and related results', '']
    lines += [f'- **{e["relation"]}**: {result_link(e["id"])}. {bilingual(e["detail"])}' for e in r['dependencies']]
    for e in r['dependencies']:
        if 'interface' in e:
            c = e['interface']
            lines += ['', '**Output / 输出:** ' + bilingual(c['output']), '', '**Input / 输入:** ' + bilingual(c['input']), '', '**Preserved conditions / 保留条件:** ' + bilingual(c['conditions']) + ' ' + link(c['evidence'], base), '']
    if not r['dependencies']:
        lines += ['No dependency on another migrated record is asserted; source imports and supplied premises remain in scope. / 尚无对另一已迁移条目的依赖断言；源码导入与给定前提仍须保留。', '']
    lines += [f'- Related, not a proved adapter / 关联而非已证转换: {result_link(e["id"])}. {bilingual(e["detail"])}' for e in r['related']]
    lines += ['', '## 来源与既有回执 Sources and existing receipts', '', '| Role | Source | Declarations |', '|---|---|---|']
    lines += [f'| {x["role"]} | {link(x["path"], base)} | {", ".join("`" + d + "`" for d in x.get("declarations", [])) or "—"} |' for x in r['references']]
    lines += ['', 'Hashes in the editable record bind the reviewed source versions. The checker does not audit transitive Lean imports or establish premise warrant. / JSON 哈希绑定读过的版本；登记检查不审计全部 Lean 导入，也不证明前提根据。', '', '## 复用与下一增量 Reuse and next delta', '', bilingual(r['next_delta']), '', 'Aliases / 别名: ' + (', '.join('`' + a + '`' for a in r['aliases']) or '—'), '', '## 沿革 History', '']
    lines += ['- ' + bilingual(h) for h in r['history']]
    return '\n'.join(lines) + '\n'


def render_index(records):
    lines = ['# 成果登记表 Canonical result register', '', '<!-- Generated by build_result_registry.py; edit records/*.json. -->', '',
             '**每项已迁移主张只有一个可编辑记录；本表及阅读页由记录生成。** 尚未迁移的成果仍以原理论／研究来源为准。会话地图是有日期的导航，文件数和验收次数不等于独立成果数。', '',
             '**One editable record per migrated claim.** This index and its reading pages are generated. Unmigrated results retain their existing sources. The session map is dated navigation; files, checks and repeated acceptances are not independent results.', '',
             link('_process/RESULT-WORKFLOW.md', OUT, 'Contribution workflow / 贡献流程') + ' · [Session map / 会话地图](SESSION-RESULTS.md) · [Full catalogue / 完整目录](README.md)', '',
             f'{len(records)} migrated records: {sum(r["kind"] != "target" for r in records)} scoped results/arguments/assessments and {sum(r["kind"] == "target" for r in records)} open targets. This is a bounded migration, not a repository-wide semantic deduplication.', '',
             '`recorded-checked` credits an existing Lean receipt; `reviewed-scoped` credits an existing substantive review; `open` marks an unmet target. None certifies a stronger claim. Hash drift requires reading the changed source before updating its record.', '',
             '| ID | Claim / 主张 | Kind | Recorded status |', '|---|---|---|---|']
    lines += [f'| `{r["id"]}` | {link(str(record_path(r).with_suffix(".md").relative_to(ROOT)), OUT, bilingual(r["title"]))} | {r["kind"]} | {r["status"]} |' for r in records]
    lines += ['', '## 先查哪一项 Where to look first', '',
             '- Same theorem under two names: `trace-law-equivalence`, `derivation-soundness`. Preserve historical names and receipts; count the underlying result once.',
             '- Similar statements with different semantics: `branching-target-uniqueness`, `joint-target-uniqueness`. Their local test languages differ.',
             '- Three shared-support results: `draws-on-a-shared-stock`, `exclusive-footprint-support`, `joint-plan-composition`. Their common obstruction does not establish a verified translation between them.',
             '- Completed G0/J argument and its AI application: `practical-judgment-g0-j`, `alignment-direction-g0-j`. The independent targets `universal-practical-warrant` and `wisdom-root` remain open.', '',
             '## 检查与检索 Check and search', '', 'From the repository root:', '', '```sh',
             'make research-check',
             'make research-find QUERY=support',
             '```', '',
             'The checker verifies record structure, aliases, links, named-declaration presence, dependency cycles, reviewed source hashes and generated views. It does not compile Lean, prove semantic equivalence, establish empirical correspondence or replace substantive review. / 检查器核对结构、别名、链接、声明存在、依赖环、已读源码哈希及生成一致性；不编译 Lean，不证明语义等价、经验对应或伦理前提。']
    return '\n'.join(lines) + '\n'


def record_path(record):
    return ROOT / record.get('_record_path', str((RECORDS / (record['id'] + '.json')).relative_to(ROOT)))


def load_records():
    config = json.loads((ROOT / '_process/research-config.json').read_text())
    records, errors = [], []
    for directory in config['record_directories']:
        for path in sorted((ROOT / directory).glob('*.json')):
            try:
                r = json.loads(path.read_text())
                if not isinstance(r, dict) or r.get('id') != path.stem:
                    errors.append(f'{path.name}: filename/id mismatch or not an object')
                else:
                    r['_record_path'] = str(path.relative_to(ROOT))
                    records.append(r)
            except (ValueError, OSError) as e:
                errors.append(f'{path.name}: {e}')
    if not records:
        errors.append('no records found')
    paths = {r['id']: r['_record_path'] for r in records}
    for r in records:
        r['_record_links'] = paths
    return sorted(records, key=lambda r: r['id']), errors


def affected_ids(records, changed):
    shared = standard_boundaries_path() in changed  # its text renders on every citing page
    selected = {r['id'] for r in records if str(record_path(r).relative_to(ROOT)) in changed or any(x['path'] in changed for x in r['references'])
                or any(v.get('path') in changed for v in r.get('text_versions', []) if isinstance(v, dict))
                or (shared and r.get('standard_boundaries'))}
    while True:
        more = {r['id'] for r in records if any(e['id'] in selected for e in r['dependencies'])}
        if more <= selected:
            return selected
        selected |= more


def orphan_pages(records):
    expected = {record_path(r).with_suffix('.md') for r in records}
    directories = json.loads((ROOT / '_process/research-config.json').read_text())['record_directories']
    return [f'orphan generated page: {p.relative_to(ROOT)}; preserve/migrate deliberately'
            for directory in directories for p in (ROOT / directory).glob('*.md') if p not in expected]


def write_views(records, drift, selected=None):
    """One stale record never prevents healthy records or the index rendering."""
    stale = {d['id'] for d in drift}
    (OUT / 'RESULT-REGISTER.md').write_text(render_index(records))
    written = []
    for r in records:
        if r['id'] not in stale and (selected is None or r['id'] in selected):
            path = record_path(r).with_suffix('.md')
            path.write_text(render_record(r))
            written.append(r['id'])
    return written


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--search')
    ap.add_argument('--ids', nargs='+', help='Limit freshness and per-record rendering; global metadata remains checked')
    args = ap.parse_args()
    if not args.check and not args.search:
        from tools.research import research
        with research.render_lock():
            code, result = research.check_or_render(True, ids=args.ids)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return code
    records, errors = load_records()
    if args.search:
        needle = args.search.casefold()
        for r in records:
            if needle in json.dumps(r, ensure_ascii=False).casefold():
                print(f'{r["id"]}\t{r["status"]}\t{bilingual(r["title"])}')
        return 1 if errors else 0
    findings, drift = validate(records)
    errors += findings
    selected = set(args.ids) if args.ids else {r['id'] for r in records}
    errors += [f'unknown result id: {x}' for x in selected - {r['id'] for r in records}]
    stale = {d['id'] for d in drift}
    outputs = {} if errors else {OUT / 'RESULT-REGISTER.md': render_index(records), **{record_path(r).with_suffix('.md'): render_record(r) for r in records if r['id'] in selected and r['id'] not in stale}}
    for path, body in outputs.items():
        if args.check:
            if not path.exists() or path.read_text() != body:
                errors.append(f'outdated generated view: {path.relative_to(ROOT)}')
        else:
            path.write_text(body)
    errors += orphan_pages(records)
    scoped_drift = [d for d in drift if d['id'] in selected]
    print(json.dumps({'records': len(records), 'errors': errors, 'source_drift': scoped_drift, 'other_record_drift': [d for d in drift if d['id'] not in selected],
                      'scope': 'Documentary checks only; no Lean build or semantic proof audit.'}, ensure_ascii=False, indent=2))
    return 1 if errors else 2 if scoped_drift else 0


if __name__ == '__main__':
    raise SystemExit(main())
