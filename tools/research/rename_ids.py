"""Rename result records (R35, twentieth review E4): `research.py rename-id --plan PLAN.tsv [--apply]`.

A plan is a TSV with the columns old_id, new_id, reason. For each row the record's JSON moves to the new id with
`git mv`, its `id` becomes the new id and the old id is appended to `former_ids`. References are rewritten in live
files only (tools/research/paths.py roles; history, evidence and sources keep the old id):
- Markdown links and repository-relative path strings to records/OLD.json and records/OLD.md, through the move
  tool's rewriter (moves.Plan), so a link resolves exactly as `research.py links` resolves it;
- JSON string values equal to the old id in the files named by `move_rewrite_json` (record dependencies, related,
  superseded_by, research-config, goals, results data), as exact JSON string tokens, so formatting is kept;
- the old id as a whole word in the prose and code of the live current-facing Markdown files (MENTION_PATHS) and
  of `tools/research/*.py`, outside link targets and outside `move_mentions_exclude`; study logs, reviews and the
  board keep the id of their time.
Generated pages are rendered afterwards: the record page takes the new path, and `records/OLD.md` becomes a
generated redirect page that links the new one, so links in history and sources still resolve. A receipt is
written to `_process/architecture/renames/<batch>.json` with every changed file and its sha256 before and after.

Refusals: an unknown old id, a new id that exists or is some record's former id, an id named in the curated
generativity chain's data (those change only through its maintenance record), or a dirty record directory.
"""
from __future__ import annotations

import datetime as _dt
import json
import re
from pathlib import Path

from tools.research import moves, paths as path_roles

ROOT = path_roles.ROOT
ID = re.compile(r'[a-z][a-z0-9-]+')
CHAIN = 'theories/becoming/results/data/generativity-chain.json'
RECEIPTS = '_process/architecture/renames'
# Bare id mentions are rewritten in the current-facing text (theory documents, package READMEs, the research tools),
# not in study logs, reviews or the board under _process/, which record what was done under the id of the time;
# their links are rewritten, and the old id resolves through former_ids and the redirect page.
MENTION_PATHS = ['theories/**', 'experiments/**/README*.md', 'README.md', 'MAP.md']


def read_plan(path):
    rows = []
    for n, line in enumerate(Path(path).read_text().splitlines(), 1):
        if not line.strip() or line.startswith('#'):
            continue
        cells = [c.strip() for c in line.split('\t')]
        if n == 1 and cells[0] == 'old_id':
            continue
        if len(cells) < 3 or not all(cells[:3]):
            raise ValueError(f'{path}:{n}: expected old_id<TAB>new_id<TAB>reason')
        rows.append({'old': cells[0], 'new': cells[1], 'reason': cells[2]})
    return rows


def word(ident):
    return re.compile(r'(?<![A-Za-z0-9_-])' + re.escape(ident) + r'(?![A-Za-z0-9_-])')


def mention_rewrite(text, pairs, skip=()):
    """Replace whole-word old ids by new ids outside the (start, end) spans in `skip`; return (text, count)."""
    count = 0
    for old, new in pairs:
        out, last = [], 0
        for m in word(old).finditer(text):
            if moves.inside(m.start(), skip):
                continue
            out += [text[last:m.start()], new]
            last = m.end()
            count += 1
        out.append(text[last:])
        text = ''.join(out)
        skip = moves.link_spans(text) if skip else ()
    return text, count


def json_rewrite(text, pairs):
    count = 0
    for old, new in pairs:
        token = json.dumps(old)
        count += text.count(token)
        text = text.replace(token, json.dumps(new))
    return text, count


def run(plan_path, apply=False, batch=None, root: Path = ROOT):
    settings = path_roles.load_config(root)
    record_dir = settings['record_directories'][0]
    rows = read_plan(plan_path)
    records = {}
    for directory in settings['record_directories']:
        for p in (root / directory).glob('*.json'):
            records[p.stem] = json.loads(p.read_text())
    former = {f: r['id'] for r in records.values() for f in r.get('former_ids', [])}
    chain = (root / CHAIN).read_text() if (root / CHAIN).is_file() else ''
    errors = []
    olds = [x['old'] for x in rows]
    news = [x['new'] for x in rows]
    for x in rows:
        if x['old'] not in records:
            errors.append(f"unknown record {x['old']}")
        if not ID.fullmatch(x['new']):
            errors.append(f"not a record id: {x['new']}")
        if x['new'] in records or x['new'] in former:
            errors.append(f"{x['new']} is a record or a former id")
        if f'records/{x["old"]}.' in chain or json.dumps(x['old']) in chain:
            errors.append(f"{x['old']} is named in the generativity chain's data; rename it through its maintenance record")
    if len(set(olds)) != len(olds) or len(set(news)) != len(news) or set(olds) & set(news):
        errors.append('an id appears twice in the plan')
    if apply:
        dirty = moves.git(root, 'status', '--porcelain', '--', *settings['record_directories']).decode().strip()
        if dirty:
            errors.append('uncommitted record changes; commit them first')
    if errors:
        return {'errors': errors}
    pairs = [(x['old'], x['new']) for x in rows]
    entries = []
    for n, (old, new) in enumerate(pairs, 1):
        for suffix in ('.json', '.md'):
            entries.append({'line': n, 'old': f'{record_dir}/{old}{suffix}', 'new': f'{record_dir}/{new}{suffix}',
                            'reason': 'record id renamed'})
    plan = moves.Plan(entries, root, settings, batch=batch)
    plan.analyse()
    texts = {r['path']: r['_text'] for r in plan.rewrites}
    moved = set(plan.file_map)
    json_globs = settings.get('move_rewrite_json', moves.DEFAULT_REWRITE_JSON)
    exclude = settings.get('move_mentions_exclude', [])
    counts = {}
    for path in sorted(plan.candidates(set(olds)) | set(texts)):
        if path in moved or path == CHAIN:
            continue
        p = root / path
        if not p.is_file():
            continue
        is_tool = path.startswith('tools/research/') and path.endswith('.py') and '/tests/' not in path
        if plan.classifier.role(path) != 'live' and not is_tool:
            continue
        text = texts.get(path)
        if text is None:
            try:
                text = p.read_text()
            except (OSError, UnicodeDecodeError):
                continue
        if path.endswith('.md') and moves.GENERATED_MARK in text[:2000]:
            continue
        n = 0
        if path.endswith('.json') and path_roles.matches(path, json_globs):
            text, n = json_rewrite(text, pairs)
        elif (path.endswith('.md') and path_roles.matches(path, MENTION_PATHS) and not path_roles.matches(path, exclude)) or is_tool:
            text, n = mention_rewrite(text, pairs, moves.link_spans(text) if path.endswith('.md') else ())
        if n or path in texts:
            texts[path] = text
            counts[path] = n
    changed = {path: text for path, text in texts.items() if (root / path).read_text() != text}
    result = {'batch': plan.batch, 'apply': apply, 'renames': rows,
              'files_changed': len(changed), 'id_mentions_rewritten': sum(counts.values()),
              'conflicts': [c for c in plan.conflicts if not c['old'].endswith('.md')],
              'changed': sorted(changed)}
    if result['conflicts'] or not apply:
        return result
    files = []
    for path, text in sorted(changed.items()):
        before = moves.sha256(root / path)
        moves.write_atomic(root / path, text.encode())
        files.append({'path': path, 'sha256_before': before, 'sha256_after': moves.sha256(root / path)})
    for old, new in pairs:
        src, dst = f'{record_dir}/{old}.json', f'{record_dir}/{new}.json'
        moves.git(root, 'mv', src, dst)
        # The renamed record's own links to other renamed records follow too (its id is set just below).
        record = json.loads(json_rewrite((root / dst).read_text(), pairs)[0])
        record['id'] = new
        record['former_ids'] = record.get('former_ids', []) + [old]
        (root / dst).write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
        files.append({'path': dst, 'former_path': src, 'sha256_after': moves.sha256(root / dst)})
    receipt = root / RECEIPTS / f'{plan.batch}.json'
    if receipt.exists():
        raise ValueError('Refusing to overwrite rename receipt: ' + str(receipt.relative_to(root)))
    receipt.parent.mkdir(parents=True, exist_ok=True)
    data = {'batch': plan.batch, 'date': _dt.date.today().isoformat(), 'renames': rows, 'files': files,
            'scope': 'Record ids renamed with former_ids kept; live references rewritten; history, evidence and sources '
                     'keep the old ids, and records/OLD.md is a generated redirect page.'}
    receipt.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n')
    result['receipt'] = str(receipt.relative_to(root))
    return result
