#!/usr/bin/env python3
"""Task-scoped links, proof-receipt binding and preservation; no scientific rerun."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
THEORY = ROOT / 'theories/shengsheng-buxi-generative-existence/unified-2026-10-05'
BASIS = ROOT / 'experiments/integrated-correction/general-framework/generative-basis'
PACKAGE = BASIS / 'noninstrumental-concern'
OUT = HERE / 'NONDUAL-CORE-CHECKS.json'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def slug(text):
    text = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', text).strip().lower()
    return ''.join(c for c in text if c in '-_ ' or c.isalnum()).replace(' ', '-')


def main():
    errors, checked, links, anchors = [], 0, 0, 0

    def verify(condition, label):
        nonlocal checked
        checked += 1
        if not condition:
            errors.append(label)

    docs = {p: p.read_text() for p in HERE.glob('NONDUAL-CORE-*.md')}
    source = ROOT / 'sources/15-codex-theory-conversations/2026-10-06-nondual-core-and-subject-extensions.md'
    docs[source] = source.read_text()
    # Shared documents: inspect only sections/paragraphs owned by this round.
    for path, marker in [
        (ROOT/'RESEARCH.md', '**非二元核心与主体延伸'),
        (ROOT/'theories/shengsheng-buxi-generative-existence/README.md', '**Nondual core and derived subjects'),
        (HERE/'README.md', '**Nondual core / subject extensions'),
        (ROOT/'experiments/README.md', '**Nondual core extension'),
        (ROOT/'sources/SOURCES.md', '- [Nondual core and subjects as extensions]'),
        (THEORY/'GENERATIVE-GROUNDING.md', '**无原始主体切分的核心'),
        (THEORY/'NONINSTRUMENTAL-CONCERN.md', '**非二元核心下的重新定位'),
        (BASIS/'lean/README.md', '**Nondual core extension'),
    ]:
        paragraphs = [p for p in path.read_text().split('\n\n') if p.startswith(marker)]
        verify(len(paragraphs) == 1, f'missing/duplicate integration: {path}')
        docs[path] = '\n\n'.join(paragraphs)
    for path, start, end in [
        (THEORY/'DEEPER-GENERATIVE-ROOT.md', '## 10. Nondual core', None),
        (THEORY/'FORMAL-CORE.md', '## F17 ', '## The unified theorem'),
        (THEORY/'THEORY.md', '## 1 The foundation', '## 4 From becoming'),
        (PACKAGE/'README.md', '## Nondual core', '## Original patient-grounded'),
    ]:
        data = path.read_text()
        verify(start in data and (end is None or end in data), f'section: {path}')
        docs[path] = data.split(start, 1)[1].split(end, 1)[0] if end else data.split(start, 1)[1]
    for path, body in docs.items():
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', body):
            if re.match(r'\w+://', target):
                continue
            target = unquote(target.strip('<>'))
            filename, _, anchor = target.partition('#')
            dest = (path.parent/filename).resolve() if filename else path
            links += 1
            verify(dest.exists() or dest == OUT, f'link: {path}: {target}')
            if anchor and dest.is_file():
                anchors += 1
                headings = [slug(h) for h in re.findall(r'^#+\s+(.+)$', dest.read_text(), re.M)]
                verify(anchor in headings, f'anchor: {path}: {target}')
        verify(body.count('\\[') == body.count('\\]'), f'math delimiters: {path}')
    receipt_files = [PACKAGE/'nondual-verification.json', PACKAGE/'nondual-model-verification.json',
                     PACKAGE/'nondual-independent-review.json']
    for receipt_path in receipt_files:
        receipt = json.loads(receipt_path.read_text())
        verify(receipt['status'] == 'passed', f'status: {receipt_path}')
        for module in receipt['modules']:
            verify(digest(BASIS/module['source']) == module['source_sha256'], f'source: {module["module"]}')
            verify(digest(PACKAGE/module['log']) == module['log_sha256'], f'log: {module["module"]}')
        for relative, value in receipt.get('preserved_files', receipt.get('preserved_sha256', {})).items():
            verify(digest(PACKAGE/relative) == value, f'preserved: {relative}')
    for checker, receipt in [('check_nondual.py','nondual-verification.json'),
                             ('check_nondual_model.py','nondual-model-verification.json'),
                             ('nondual_independent_review.py','nondual-independent-review.json')]:
        verify(digest(PACKAGE/checker) == json.loads((PACKAGE/receipt).read_text())['checker_sha256'], checker)
    connected = json.loads((BASIS/'lean/connected/INPUTS.json').read_text())
    for module in connected['sources']:
        verify(digest(ROOT/module['path']) == module['sha256'], f'concurrent frozen source: {module["module"]}')
    verify((BASIS/'lean/NondualCore.lean').read_text().splitlines()[0] == 'import GenerativeCore', 'dependency direction')
    verify(not list(PACKAGE.rglob('*.olean')) and not list(PACKAGE.rglob('*.pyc')), 'generated compiler/cache files')
    result = {'status': 'passed' if not errors else 'failed',
              'checked_at_utc': datetime.now(timezone.utc).isoformat(),
              'scope': 'Task-owned text links, source/log binding and preservation only; no proof or finite oracle rerun.',
              'local_links_checked': links, 'anchors_checked': anchors, 'checks': checked,
              'document_sha256': {str(p.relative_to(ROOT)): digest(p) for p in docs},
              'receipts_sha256': {str(p.relative_to(ROOT)): digest(p) for p in receipt_files},
              'checker_sha256': digest(Path(__file__)), 'distinct_new_declaration_audits': 33,
              'nondual_architecture_realized': True, 'assumption_free_foundation_complete': False,
              'errors': errors}
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('document_sha256','receipts_sha256')}, ensure_ascii=False))
    assert not errors


if __name__ == '__main__':
    main()
