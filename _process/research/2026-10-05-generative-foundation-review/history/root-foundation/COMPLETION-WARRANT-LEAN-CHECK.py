"""Validate owned integration, exact preservation, links and Lean receipt binding.

Mathematical checking is performed by the formal package's fresh Lean build.
This file does not infer ethical warrant from successful compilation.
"""
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[4]
NOTES = Path(__file__).resolve().parent
FORMAL = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/completion/formal'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def anchor(heading):
    return re.sub(r'[^\w\s-]', '', heading.strip().lower()).replace(' ', '-')


def main():
    manifest_path = NOTES / 'COMPLETION-WARRANT-LEAN-EDITS.json'
    manifest = json.loads(manifest_path.read_text())
    canonical = ROOT / manifest['canonical']
    docs = [canonical, FORMAL / 'README.md',
            ROOT / 'sources/15-codex-theory-conversations/2026-10-07-lean-proof-requirement.md']
    docs += [NOTES / ('COMPLETION-WARRANT-LEAN-' + suffix + '.md')
             for suffix in ['INTEGRATION', 'IDEALS', 'ROLE', 'PREFIX', 'HISTORIES', 'REVIEW']]
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

    receipt_path = FORMAL / 'verification.json'
    receipt = json.loads(receipt_path.read_text())
    assert receipt['fresh_build'] and not receipt['proof_holes'] and not receipt['custom_axioms']
    assert digest(FORMAL / 'check.py') == receipt['checker_sha256']
    for name, expected in receipt['source_sha256'].items():
        assert digest(FORMAL / name) == expected, name
    review = (NOTES / 'COMPLETION-WARRANT-LEAN-REVIEW.md').read_text()
    reviewed = re.findall(r'\| `([^`]+\.lean)` \| `([a-f0-9]{64})` \|', review)
    assert len(reviewed) == 6
    for name, expected in reviewed:
        assert digest(FORMAL / name) == expected, name
    report = {
        'scope': 'Integration, source preservation and binding to the separately executed Lean receipt',
        'documents_or_owned_sections': len(sections), 'local_links': links, 'anchors': anchors,
        'preserved_inputs': len(manifest['preserved_inputs']),
        'previous_canonical_reconstructed_exactly': True,
        'reviewed_source_hashes_matched': len(reviewed),
        'lean_modules': receipt['modules'], 'lean_theorems': receipt['theorems'],
        'lean_audited_declarations': receipt['audited_declarations'],
        'custom_axioms': [], 'proof_holes': False,
        'scientific_experiments_executed': False, 'normative_grounding_proved': False,
        'sha256': {str(path.relative_to(ROOT)): digest(path)
                   for path in docs + [manifest_path, receipt_path, Path(__file__).resolve()]},
    }
    (NOTES / 'COMPLETION-WARRANT-LEAN-CHECKS.json').write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({key: value for key, value in report.items() if key != 'sha256'}))


if __name__ == '__main__':
    main()
