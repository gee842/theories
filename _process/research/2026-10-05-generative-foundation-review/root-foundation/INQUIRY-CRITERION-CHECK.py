"""Validate this round's owned text, receipts and preserved scientific inputs."""
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[4]
NOTES = Path(__file__).resolve().parent
THEORY = ROOT / 'theories/shengsheng-buxi-generative-existence/unified-2026-10-05'
EXP = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/inquiry/criteria'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def anchor(heading):
    return re.sub(r'[^\w\s-]', '', heading.strip().lower()).replace(' ', '-')


def main():
    docs = [THEORY / 'ATTAINABLE-MATHEMATICAL-QUESTIONS.md',
            NOTES / 'INQUIRY-CRITERION-MATH.md',
            NOTES / 'INQUIRY-CRITERION-REVIEW.md',
            NOTES / 'INQUIRY-CRITERION-SOURCES.md',
            ROOT / 'sources/15-codex-theory-conversations/2026-10-06-attainable-question-continuation.md',
            EXP / 'README.md', EXP / 'PROTOCOL.md']
    sections = [(p, p.read_text()) for p in docs]
    edits_path = NOTES / 'INQUIRY-CRITERION-INDEX-EDITS.json'
    for name, entry in json.loads(edits_path.read_text()).items():
        path = ROOT / name
        assert path.read_text().count(entry) == 1, name
        sections.append((path, entry))
    links = anchors = 0
    for path, content in sections:
        for opening, closing in ((r'\[', r'\]'), (r'\(', r'\)')):
            assert content.count(opening) == content.count(closing), path
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
            if re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', link):
                continue
            name, sep, fragment = link.partition('#')
            target = (path.parent / name).resolve() if name else path
            assert target.exists(), (path, link)
            links += 1
            if sep and fragment:
                headings = re.findall(r'^#{1,6}\s+(.+)$', target.read_text(), re.M)
                assert fragment in {anchor(h) for h in headings}, (path, link)
                anchors += 1
    result = json.loads((EXP / 'results.json').read_text())
    review = json.loads((EXP / 'review-check.json').read_text())
    assert result['decision_count'] == 8100
    assert result['parent_decisions_preserved'] == 1080
    assert result['inherited_retained_probes'] == 36
    assert result['inherited_retention_failures'] == 12
    assert result['original_experiments_executed'] is False
    assert result['checker_sha256'] == digest(EXP / 'check.py')
    assert result['protocol_sha256'] == digest(EXP / 'PROTOCOL.md')
    assert review['producer_results_sha256'] == digest(EXP / 'results.json')
    assert review['review_checker_sha256'] == digest(EXP / 'review_check.py')
    assert review['checked_decisions'] == 8100 and review['checked_partitions'] == 15
    assert review['parent_decisions_preserved'] == 1080
    assert review['source_bindings_verified'] == len(result['source_bindings']) == 11
    assert review['original_experiments_executed'] is False
    for name, expected in result['source_bindings'].items():
        assert digest(ROOT / name) == expected, name
    files = docs + [edits_path, EXP / 'results.json', EXP / 'review-check.json',
                    EXP / 'check.py', EXP / 'review_check.py', Path(__file__).resolve()]
    receipt = dict(scope='Owned documents/insertions and finite verification receipts; no old scientific rerun',
                   documents_or_owned_sections=len(sections), local_links=links, anchors=anchors,
                   math_delimiters='balanced', saved_decisions=8100, preserved_parent_decisions=1080,
                   unchanged_source_bindings=len(result['source_bindings']),
                   sha256={str(p.relative_to(ROOT)): digest(p) for p in files})
    (NOTES / 'INQUIRY-CRITERION-CHECKS.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: v for k, v in receipt.items() if k != 'sha256'}))


if __name__ == '__main__':
    main()
