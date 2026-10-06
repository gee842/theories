"""Editorial checks only: no scientific execution or theorem verification."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def blocks(text, pattern):
    return re.findall(pattern, text, re.MULTILINE | re.DOTALL)


def anchors(text):
    result = set(re.findall(r'<a\s+(?:id|name)="([^"]+)"', text))
    counts = {}
    for heading in re.findall(r'^#{1,6}\s+(.+)$', text, re.MULTILINE):
        heading = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', heading)
        slug = re.sub(r'[^\w\-\s]', '', heading.lower()).replace(' ', '-')
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(slug if not count else f'{slug}-{count}')
    return result


def broken_links(path, text):
    destinations = re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)', text)
    destinations += re.findall(r'^\[[^]]+\]:\s*(\S+)', text, re.MULTILINE)
    problems = []
    checked = 0
    for link in destinations:
        link = link.strip('<>')
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', link):
            continue
        name, _, fragment = unquote(link).partition('#')
        target = (path.parent / name).resolve() if name else path
        checked += 1
        if not target.exists():
            problems.append({'link': link, 'issue': 'missing target'})
        elif fragment and target.suffix == '.md':
            if fragment not in anchors(target.read_text()):
                problems.append({'link': link, 'issue': 'unresolved anchor'})
    return checked, problems


def main():
    records = []
    files = []
    for metadata in sorted(HERE.glob('review-*.json')):
        for item in json.loads(metadata.read_text())['files']:
            rel = item['path']
            before = HERE / 'before' / rel
            current = ROOT / rel
            old, new = before.read_text(), current.read_text()
            checked, problems = broken_links(current, new)
            _, old_problems = broken_links(current, old)
            new_problems = [p for p in problems if p not in old_problems]
            old_fences = blocks(old, r'^```[^\n]*\n.*?^```')
            new_fences = blocks(new, r'^```[^\n]*\n.*?^```')
            label_change = (
                rel.endswith('/START-HERE.md')
                and [s.replace('Changed conditions and delivered capacities',
                               'Changed conditions and capacities for further activity')
                     for s in old_fences] == new_fences
            )
            row = {
                'path': rel,
                'snapshot_sha256_matches': sha(before) == item['before_sha256'],
                'current_sha256': sha(current),
                'display_math_unchanged': blocks(old, r'\\\[.*?\\\]') == blocks(new, r'\\\[.*?\\\]'),
                'indented_formula_lines_unchanged': re.findall(r'^ {4}\S.*$', old, re.MULTILINE) == re.findall(r'^ {4}\S.*$', new, re.MULTILINE),
                'fenced_blocks_unchanged': old_fences == new_fences,
                'documented_mermaid_label_only': label_change and old_fences != new_fences,
                'local_links_checked': checked,
                'new_link_problems': new_problems,
                'all_current_link_problems': problems,
            }
            records.append(row)
            files.append(rel)
    supplemental = []
    for p in [HERE / 'README.md', ROOT / 'sources/15-codex-theory-conversations/2026-10-06-generative-language-revision.md']:
        checked, problems = broken_links(p, p.read_text())
        supplemental.append({'path': str(p.relative_to(ROOT)), 'local_links_checked': checked, 'problems': problems})
        files.append(str(p.relative_to(ROOT)))
    old_receipt = json.loads((HERE.parent / 'continuity-correction-checks.json').read_text())
    source_hashes = {p: sha(ROOT / p) == digest for p, digest in old_receipt['source_versions_sha256'].items()}
    check = subprocess.run(['git', 'diff', '--check', '--', *files], cwd=ROOT, capture_output=True, text=True)
    result = {
        'date': '2026-10-06',
        'scope': 'Editorial preservation and relative-link checks; not scientific verification.',
        'files': records,
        'supplemental_documents': supplemental,
        'prior_inspected_source_hashes_unchanged': source_hashes,
        'diff_check_exit_code': check.returncode,
        'diff_check_output': check.stdout + check.stderr,
        'scientific_rerun': False,
    }
    result['passed'] = all(
        r['snapshot_sha256_matches'] and r['display_math_unchanged'] and r['indented_formula_lines_unchanged']
        and (r['fenced_blocks_unchanged'] or r['documented_mermaid_label_only'])
        and not r['new_link_problems'] for r in records
    ) and all(not r['problems'] for r in supplemental) and all(source_hashes.values()) and check.returncode == 0
    concurrent_record = HERE / 'concurrent-link-observations.json'
    concurrent = json.loads(concurrent_record.read_text())['links'] if concurrent_record.exists() else []
    result['concurrent_link_observations'] = concurrent
    result['editorial_scope_passed'] = all(
        r['snapshot_sha256_matches'] and r['display_math_unchanged'] and r['indented_formula_lines_unchanged']
        and (r['fenced_blocks_unchanged'] or r['documented_mermaid_label_only'])
        and all({'path': r['path'], **p} in concurrent for p in r['new_link_problems'])
        for r in records
    ) and all(not r['problems'] for r in supplemental) and all(source_hashes.values()) and check.returncode == 0
    (HERE / 'checks.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'full_document_check_passed': result['passed'], 'editorial_scope_passed': result['editorial_scope_passed'], 'files': len(records),
                      'local_links_checked': sum(r['local_links_checked'] for r in records + supplemental),
                      'new_link_problems': [{'path': r['path'], 'problems': r['new_link_problems']} for r in records if r['new_link_problems']],
                      'supplemental_problems': [r for r in supplemental if r['problems']],
                      'source_hashes': source_hashes,
                      'diff_check_exit_code': check.returncode}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
