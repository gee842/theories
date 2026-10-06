"""Owned document checks; scientific receipts are checked, not regenerated."""
from pathlib import Path
from hashlib import sha256
from urllib.parse import unquote
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
THEORY = ROOT/'theories/shengsheng-buxi-generative-existence/unified-2026-10-05'
EXP = ROOT/'experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/revision'


def digest(p):
    return sha256(p.read_bytes()).hexdigest()


def anchors(p):
    result, counts = set(), {}
    for title in re.findall(r'^#{1,6}\s+(.+)$', p.read_text(), re.M):
        base = re.sub(r'[^\w\- ]', '', title.lower()).replace(' ', '-')
        n = counts.get(base, 0)
        result.add(base if n == 0 else f'{base}-{n}')
        counts[base] = n+1
    return result


def run():
    full = [THEORY/'MODEL-FAMILY-REVISION.md',
            HERE/'MODEL-FAMILY-REVISION-MATH.md',
            HERE/'MODEL-FAMILY-REVISION-REVIEW.md',
            HERE/'MODEL-FAMILY-REVISION-COMPARATORS.md',
            EXP/'README.md', EXP/'PROTOCOL.md',
            ROOT/'sources/15-codex-theory-conversations/2026-10-06-model-family-revision-continuation.md']
    sections = {
        ROOT/'RESEARCH.md': '**Model-family revision through fresh evidence,',
        THEORY/'GENERATIVE-GROUNDING.md': '**Retained abstraction → enlarged family → reacquired current prediction,',
        THEORY.parent/'README.md': '**Revising the model family,',
        HERE/'README.md': '**Model-family revision,',
        ROOT/'sources/SOURCES.md': 'Recorded 2026-10-06: [Continuation through model family revision]',
        THEORY/'EXPERIMENTAL-ACCESS.md': '**Model-family continuation,',
        EXP.parent/'README.md': '**Model-family continuation,',
        ROOT/'experiments/README.md': '**Paid model-family revision,',
    }
    texts = {p: p.read_text() for p in full}
    for p, start in sections.items():
        paragraphs = [s for s in p.read_text().split('\n\n') if s.startswith(start)]
        assert len(paragraphs) == 1, (p, start)
        texts[p] = paragraphs[0]
    integration = HERE/'MATHEMATICS-REVIEW.md'
    texts[integration] = integration.read_text().split('## Model family revision continuation\n', 1)[1].split('\n## ', 1)[0]
    links, fragments = 0, 0
    for p, text in texts.items():
        assert text.count(r'\[') == text.count(r'\]'), p
        assert text.count(r'\(') == text.count(r'\)'), p
        for href in re.findall(r'\]\(([^\s)]+)\)', text):
            if re.match(r'^[a-zA-Z]+:', href):
                continue
            path, sep, fragment = unquote(href).partition('#')
            target = (p.parent/path).resolve() if path else p
            expected_receipt = HERE/'MODEL-FAMILY-REVISION-CHECKS.json'
            assert target.exists() or target == expected_receipt, (p, href)
            links += 1
            if sep:
                assert fragment in anchors(target), (p, href)
                fragments += 1
    science = json.loads((EXP/'results.json').read_text())
    independent = json.loads((EXP/'independent-check.json').read_text())
    for name, expected in science['source_hashes'].items():
        assert digest(EXP/name) == expected, name
    for name, expected in science['inherited_hashes'].items():
        assert digest(ROOT/name) == expected, name
    for name, expected in independent['hashes'].items():
        assert digest(EXP/name) == expected, name
    assert len(science['fixtures']) == 14
    assert len(science['family']) == 14
    assert len(independent['inherited_family_runs']) == 14
    assert independent['family_statuses'] == science['family_statuses']
    assert independent['state_relabellings'] == 6
    record = dict(scope='document/link/snapshot and scientific receipt currency only',
                  documents_or_owned_sections=len(texts), local_links=links, anchors=fragments,
                  formula_delimiters='balanced',
                  full_file_sha256={str(p.relative_to(ROOT)): digest(p) for p in full},
                  owned_section_sha256={str(p.relative_to(ROOT)): sha256(t.encode()).hexdigest()
                                        for p, t in texts.items() if p not in full},
                  scientific_receipt_sha256={p.name: digest(p) for p in
                                             [EXP/'results.json', EXP/'independent-check.json']},
                  checker_sha256=digest(Path(__file__)))
    (HERE/'MODEL-FAMILY-REVISION-CHECKS.json').write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({k: record[k] for k in ('documents_or_owned_sections', 'local_links', 'anchors', 'formula_delimiters')}))


if __name__ == '__main__':
    run()
