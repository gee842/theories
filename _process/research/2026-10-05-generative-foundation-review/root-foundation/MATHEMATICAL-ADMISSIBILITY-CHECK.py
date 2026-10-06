"""Check owned admission-study links, mathematical delimiters and preservation.

This is document/provenance validation, not verification of the infinite proofs.
"""
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[4]
NOTES = Path(__file__).resolve().parent
THEORY = ROOT / 'theories/shengsheng-buxi-generative-existence/unified-2026-10-05'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def anchor(heading):
    return re.sub(r'[^\w\s-]', '', heading.strip().lower()).replace(' ', '-')


def main():
    docs = [THEORY / 'GENERATIVE-MATHEMATICAL-ADMISSIBILITY.md',
            NOTES / 'MATHEMATICAL-ADMISSIBILITY-MATH.md',
            NOTES / 'MATHEMATICAL-ADMISSIBILITY-REVIEW.md',
            NOTES / 'MATHEMATICAL-ADMISSIBILITY-SOURCES.md',
            ROOT / 'sources/15-codex-theory-conversations/2026-10-06-mathematical-admissibility-continuation.md']
    manifest_path = NOTES / 'MATHEMATICAL-ADMISSIBILITY-EDITS.json'
    manifest = json.loads(manifest_path.read_text())
    sections = [(path, path.read_text()) for path in docs]
    for name, entry in manifest['owned_insertions'].items():
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
    for name, expected in manifest['preserved_inputs'].items():
        assert digest(ROOT / name) == expected, name
    files = docs + [manifest_path, Path(__file__).resolve()]
    report = dict(scope='Owned text, local links and input preservation; mathematical acceptance by separate hand-proof review',
                  documents_or_owned_sections=len(sections), local_links=links, anchors=anchors,
                  math_delimiters='balanced', preserved_inputs=len(manifest['preserved_inputs']),
                  scientific_experiments_executed=False, new_proof_assistant_audits=0,
                  sha256={str(p.relative_to(ROOT)): digest(p) for p in files})
    (NOTES / 'MATHEMATICAL-ADMISSIBILITY-CHECKS.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'sha256'}))


if __name__ == '__main__':
    main()
