"""Validate this continuation's documents and preservation, not its proofs.

The infinite-domain arguments are checked in COMPLETION-WARRANT-REVIEW.md.
No earlier scientific experiment or proof-assistant build is rerun here.
"""
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[4]
NOTES = Path(__file__).resolve().parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def anchor(heading):
    return re.sub(r'[^\w\s-]', '', heading.strip().lower()).replace(' ', '-')


def main():
    manifest_path = NOTES / 'COMPLETION-WARRANT-EDITS.json'
    manifest = json.loads(manifest_path.read_text())
    canonical = ROOT / manifest['canonical']
    docs = [canonical,
            NOTES / 'COMPLETION-WARRANT-MATH.md',
            NOTES / 'COMPLETION-WARRANT-REVIEW.md',
            NOTES / 'COMPLETION-WARRANT-SOURCES.md',
            ROOT / 'sources/15-codex-theory-conversations/2026-10-06-completion-warrant-continuation.md']
    sections = [(path, path.read_text()) for path in docs]
    for name, insertion in manifest['owned_insertions'].items():
        path = ROOT / name
        assert path.read_text().count(insertion) == 1, name
        sections.append((path, insertion))

    restored = canonical.read_text()
    for addition in manifest['canonical_additions'].values():
        assert restored.count(addition) == 1
        restored = restored.replace(addition, '', 1)
    assert sha256(restored.encode()).hexdigest() == manifest['canonical_before_sha256']
    for name, expected in manifest['preserved_inputs'].items():
        assert digest(ROOT / name) == expected, name

    links = anchors = 0
    for path, content in sections:
        for opening, closing in ((r'\[', r'\]'), (r'\(', r'\)')):
            assert content.count(opening) == content.count(closing), path
        assert all(line == line.rstrip() for line in content.splitlines()), path
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

    files = docs + [manifest_path, Path(__file__).resolve()]
    report = dict(
        scope='Owned documents, local links and exact preservation; proof acceptance by separate independent hand review',
        documents_or_owned_sections=len(sections),
        local_links=links,
        anchors=anchors,
        math_delimiters='balanced',
        owned_text_whitespace='clean',
        preserved_inputs=len(manifest['preserved_inputs']),
        previous_canonical_reconstructed_exactly=True,
        scientific_experiments_executed=False,
        new_proof_assistant_audits=0,
        sha256={str(path.relative_to(ROOT)): digest(path) for path in files})
    (NOTES / 'COMPLETION-WARRANT-CHECKS.json').write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({key: value for key, value in report.items() if key != 'sha256'}))


if __name__ == '__main__':
    main()
