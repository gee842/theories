"""Owned document checks; scientific receipts are checked, not regenerated."""
from pathlib import Path
from hashlib import sha256
from urllib.parse import unquote
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
THEORY = ROOT/'theories/shengsheng-buxi-generative-existence/unified-2026-10-05'
EXP = ROOT/'experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access'


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
    full = [THEORY/'EXPERIMENTAL-ACCESS.md',
            HERE/'EXPERIMENTAL-ACCESS-MATH.md',
            HERE/'EXPERIMENTAL-ACCESS-REVIEW.md',
            HERE/'EXPERIMENTAL-ACCESS-COMPARATORS.md',
            EXP/'README.md', EXP/'PROTOCOL.md',
            ROOT/'sources/15-codex-theory-conversations/2026-10-06-experimental-access-continuation.md']
    sections = {
        ROOT/'RESEARCH.md': '**Experimental access from an acquired model,',
        THEORY/'GENERATIVE-GROUNDING.md': '**Retained abstraction → tests of experimental access → qualified diagnosis,',
        THEORY.parent/'README.md': '**Testing experimental access,',
        HERE/'README.md': '**Experimental access,',
        ROOT/'sources/SOURCES.md': 'Recorded 2026-10-06: [Continuation through experimental access]',
        THEORY/'ABSTRACTION-ACQUISITION.md': '**Experimental-access continuation,',
        EXP.parent/'README.md': '**Experimental-access continuation,',
        ROOT/'experiments/README.md': '**Paid experimental access,',
    }
    texts = {p: p.read_text() for p in full}
    for p, start in sections.items():
        paragraphs = [s for s in p.read_text().split('\n\n') if s.startswith(start)]
        assert len(paragraphs) == 1, (p, start)
        texts[p] = paragraphs[0]
    integration = HERE/'MATHEMATICS-REVIEW.md'
    texts[integration] = integration.read_text().split('## Experimental access continuation\n', 1)[1].split('\n## ', 1)[0]
    links, fragments = 0, 0
    for p, text in texts.items():
        assert text.count(r'\[') == text.count(r'\]'), p
        assert text.count(r'\(') == text.count(r'\)'), p
        for href in re.findall(r'\]\(([^\s)]+)\)', text):
            if re.match(r'^[a-zA-Z]+:', href):
                continue
            path, sep, fragment = unquote(href).partition('#')
            target = (p.parent/path).resolve() if path else p
            expected_receipt = HERE/'EXPERIMENTAL-ACCESS-CHECKS.json'
            assert target.exists() or target == expected_receipt, (p, href)
            links += 1
            if sep:
                assert fragment in anchors(target), (p, href)
                fragments += 1
    science = json.loads((EXP/'results.json').read_text())
    independent = json.loads((EXP/'independent-check.json').read_text())
    for name, expected in science['source_hashes'].items():
        assert digest(EXP/name) == expected, name
    for name, expected in science['handoff']['source_hashes'].items():
        assert digest(ROOT/name) == expected, name
    for name, expected in independent['hashes'].items():
        assert digest(EXP/name) == expected, name
    assert len(science['fixtures']) == 18
    assert len(science['family']) == 144
    assert independent['primary_class']['independent_policy_and_update_matches'] == 48
    assert independent['factored_continuation']['probe_complete'] == 36
    assert independent['retained_model_relabelling']['state_renamings'] == 6
    record = dict(scope='document/link/snapshot and scientific receipt currency only',
                  documents_or_owned_sections=len(texts), local_links=links, anchors=fragments,
                  formula_delimiters='balanced',
                  full_file_sha256={str(p.relative_to(ROOT)): digest(p) for p in full},
                  owned_section_sha256={str(p.relative_to(ROOT)): sha256(t.encode()).hexdigest()
                                        for p, t in texts.items() if p not in full},
                  scientific_receipt_sha256={p.name: digest(p) for p in
                                             [EXP/'results.json', EXP/'independent-check.json']},
                  checker_sha256=digest(Path(__file__)))
    (HERE/'EXPERIMENTAL-ACCESS-CHECKS.json').write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({k: record[k] for k in ('documents_or_owned_sections', 'local_links', 'anchors', 'formula_delimiters')}))


if __name__ == '__main__':
    run()
