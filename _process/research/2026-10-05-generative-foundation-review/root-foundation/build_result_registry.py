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

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / 'theories/shengsheng-buxi-generative-existence/results'
RECORDS = OUT / 'records'
STATUSES = {'recorded-checked', 'reviewed-scoped', 'open', 'superseded', 'withdrawn'}
KINDS = {'theorem', 'argument', 'assessment', 'target'}
RELATIONS = {'formal-reuse', 'application', 'interpretive'}
ROLES = {'statement', 'proof', 'receipt', 'review', 'integration', 'counterexample', 'provenance'}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pair(value):
    return isinstance(value, dict) and all(isinstance(value.get(k), str) and value[k].strip() for k in ('zh', 'en'))


def bilingual(value):
    return value['zh'] + ' / ' + value['en']


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


def validate(records):
    errors, drift = [], []
    ids, aliases = {}, {}
    for r in records:
        ident = r.get('id', '<missing>')
        def fail(message):
            errors.append(f'{ident}: {message}')
        if not isinstance(ident, str) or not re.fullmatch(r'[a-z][a-z0-9-]+', ident):
            fail('invalid stable id')
        if ident in ids:
            fail('duplicate id')
        ids[ident] = r
        if r.get('schema_version') != 1 or r.get('kind') not in KINDS or r.get('status') not in STATUSES:
            fail('invalid schema, kind or status')
        if r.get('kind') == 'target' and r.get('status') not in {'open', 'superseded', 'withdrawn'}:
            fail('a target cannot be marked completed')
        for key in ('title', 'claim', 'correspondence', 'limitations', 'next_delta', 'validation_scope'):
            if not pair(r.get(key)):
                fail(f'{key} requires nonempty Chinese and English')
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
                # Existence aid only: the linked source establishes namespace and meaning.
                if not re.search(r'^\s*(?:(?:protected|private)\s+)?(?:theorem|lemma|def|abbrev)\s+' + re.escape(name.split('.')[-1]) + r'(?=\s|\{|\(|:)', p.read_text(), re.M):
                    fail(f'declaration not found: {name} in {path}')
        if r.get('canonical_source') not in paths:
            fail('canonical source must be a hashed reference')
        if r.get('status') == 'recorded-checked' and not {'proof', 'receipt'} <= roles:
            fail('recorded-checked needs proof source and existing receipt')
        if r.get('status') == 'recorded-checked' and not r.get('proof_bindings'):
            fail('recorded-checked needs a source hash binding in its existing receipt')
        refs_by_path = {x['path']: x for x in refs}
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
            except (KeyError, IndexError, ValueError, TypeError, OSError) as exc:
                fail(f'invalid proof receipt binding: {exc}')
        if r.get('status') == 'reviewed-scoped' and not {'statement', 'review'} <= roles:
            fail('reviewed-scoped needs statement and review')
        if not isinstance(r.get('dependencies'), list) or not isinstance(r.get('related'), list):
            fail('dependencies and related must be explicit lists')
        if not isinstance(r.get('counterexamples'), list) or not r.get('counterexamples'):
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


def render_record(r):
    base = RECORDS
    lines = [f'# {bilingual(r["title"])}', '',
             '<!-- Generated by build_result_registry.py; edit the matching JSON record. -->', '',
             f'`{r["id"]}` · **{r["status"]}** · {r["kind"]} · {r["family"]}', '',
             f'记录源 / Editable record: [{r["id"]}.json]({r["id"]}.json) · [登记表 / Register](../RESULT-REGISTER.md)', '',
             f'Documentary review UTC: `{r["reviewed_at_utc"]}`. Run the registry checker for source drift; this page is not a fresh proof receipt.', '',
             '## 主张 Claim', '', bilingual(r['claim']), '',
             'Canonical source: ' + link(r['canonical_source'], base), '',
             '## 前提与对应 Hypotheses and correspondence', '']
    lines += ['- ' + bilingual(x) for x in r['hypotheses']]
    lines += ['', bilingual(r['correspondence']), '', '## 检验与边界 Validation and boundaries', '', bilingual(r['validation_scope']), '', bilingual(r['limitations']), '']
    lines += [('Boundary source / 边界来源: ' if c['detail'] == r['limitations'] else '- ' + bilingual(c['detail']) + ' ') + link(c['path'], base) for c in r['counterexamples']]
    lines += ['', '## 依赖与关联 Dependencies and related results', '']
    lines += [f'- **{e["relation"]}**: [{e["id"]}]({e["id"]}.md). {bilingual(e["detail"])}' for e in r['dependencies']]
    if not r['dependencies']:
        lines += ['No dependency on another migrated record is asserted; source imports and supplied premises remain in scope. / 尚无对另一已迁移条目的依赖断言；源码导入与给定前提仍须保留。', '']
    lines += [f'- Related, not a proved adapter / 关联而非已证转换: [{e["id"]}]({e["id"]}.md). {bilingual(e["detail"])}' for e in r['related']]
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
    lines += [f'| `{r["id"]}` | [{bilingual(r["title"])}](records/{r["id"]}.md) | {r["kind"]} | {r["status"]} |' for r in records]
    lines += ['', '## 先查哪一项 Where to look first', '',
             '- Same theorem under two names: `trace-law-equivalence`, `derivation-soundness`. Preserve historical names and receipts; count the underlying result once.',
             '- Similar statements with different semantics: `branching-target-uniqueness`, `joint-target-uniqueness`. Their local test languages differ.',
             '- Three shared-support results: `aggregate-exit-funding`, `exclusive-footprint-support`, `joint-plan-composition`. Their common obstruction does not establish a verified translation between them.',
             '- Completed G0/J argument and its AI application: `practical-judgment-g0-j`, `alignment-direction-g0-j`. The independent targets `universal-practical-warrant` and `wisdom-root` remain open.', '',
             '## 检查与检索 Check and search', '', 'From the repository root:', '', '```sh',
             'python3 _process/research/2026-10-05-generative-foundation-review/root-foundation/build_result_registry.py --check',
             'python3 _process/research/2026-10-05-generative-foundation-review/root-foundation/build_result_registry.py --search support',
             '```', '',
             'The checker verifies record structure, aliases, links, named-declaration presence, dependency cycles, reviewed source hashes and generated views. It does not compile Lean, prove semantic equivalence, establish empirical correspondence or replace substantive review. / 检查器核对结构、别名、链接、声明存在、依赖环、已读源码哈希及生成一致性；不编译 Lean，不证明语义等价、经验对应或伦理前提。']
    return '\n'.join(lines) + '\n'


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--search')
    args = ap.parse_args()
    records, errors = [], []
    for path in sorted(RECORDS.glob('*.json')):
        try:
            r = json.loads(path.read_text())
            if not isinstance(r, dict) or r.get('id') != path.stem:
                errors.append(f'{path.name}: filename/id mismatch or not an object')
            else:
                records.append(r)
        except (ValueError, OSError) as e:
            errors.append(f'{path.name}: {e}')
    if not records:
        errors.append('no records found')
    if args.search:
        needle = args.search.casefold()
        for r in records:
            if needle in json.dumps(r, ensure_ascii=False).casefold():
                print(f'{r["id"]}\t{r["status"]}\t{bilingual(r["title"])}')
        return 1 if errors else 0
    findings, drift = validate(records)
    errors += findings
    outputs = {} if errors else {OUT / 'RESULT-REGISTER.md': render_index(records), **{RECORDS / (r['id'] + '.md'): render_record(r) for r in records}}
    for path, body in outputs.items():
        if args.check:
            if not path.exists() or path.read_text() != body:
                errors.append(f'outdated generated view: {path.relative_to(ROOT)}')
        elif not drift:
            path.write_text(body)
    expected_pages = {r['id'] + '.md' for r in records}
    for p in RECORDS.glob('*.md'):
        if p.name not in expected_pages:
            errors.append(f'orphan generated page: {p.name}; preserve/migrate deliberately')
    print(json.dumps({'records': len(records), 'errors': errors, 'source_drift': drift,
                      'scope': 'Documentary checks only; no Lean build or semantic proof audit.'}, ensure_ascii=False, indent=2))
    return 1 if errors else 2 if drift else 0


if __name__ == '__main__':
    raise SystemExit(main())
