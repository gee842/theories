"""Read-only integration, receipt, local-link and preservation checks."""
from pathlib import Path
import hashlib
import json
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p/'AGENTS.md').exists())
THEORY = REPO/'theories/becoming/chapters'
EXPERIMENT = next(REPO.glob('experiments/**/plasticity/inquiry-revision/README.md')).parent
FORMAL = EXPERIMENT.parent/'formal/inquiry-revision'


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def check_links(path, content):
    checked = []
    for raw in re.findall(r'\]\(([^)]+)\)', content):
        if re.match(r'^[a-z]+:', raw):
            continue
        target, _, anchor = unquote(raw).partition('#')
        destination = (path.parent/target).resolve() if target else path
        assert destination.exists(), (path, raw)
        if anchor and destination.suffix == '.md':
            headings = re.findall(r'^#+\s+(.+)$', destination.read_text(), re.M)
            slugs = [re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings]
            assert anchor in slugs, (path, raw, 'missing heading')
        checked.append(dict(source=str(path.relative_to(REPO)), target=raw))
    return checked


def main():
    numerical = json.loads((EXPERIMENT/'independent-check.json').read_text())
    formal = json.loads((FORMAL/'verification.json').read_text())
    correspondence = json.loads((EXPERIMENT/'formal-correspondence.json').read_text())
    assert numerical['status'] == 'accepted_independent_finite_replay'
    assert formal['status'] == 'passed' and formal['fresh_build'] and formal['source_unchanged']
    assert correspondence['status'] == 'passed'
    assert correspondence['milestones'] == 13 and correspondence['coordinates'] == 30
    bound = {}
    for receipt in (numerical, correspondence):
        for path, expected in receipt['source_sha256'].items():
            assert digest(REPO/path) == expected, path
            bound[path] = expected
    for module in formal['modules']:
        assert module['passed'] and digest(REPO/module['source']) == module['sha256']
        bound[module['source']] = module['sha256']
    expected_old = {
        'PairedPlasticity.lean':'6ce4f08cb9f2b497a409482bbfc2281fd6d83a5efad14d2cabb7fbc2d3792b83',
        'PlasticityWitness.lean':'df54d86981213e4dbb14d6b707793a244971dbe084d2ac9123b21bf49e0b6e9a'}
    for name, expected in expected_old.items():
        assert digest(FORMAL.parent/name) == expected
    files = [THEORY/'INQUIRY-REVISION.md', EXPERIMENT/'README.md', EXPERIMENT/'PROTOCOL.md',
             HERE/'INQUIRY-REVISION-MECHANISM.md', HERE/'INQUIRY-REVISION-REVIEW.md',
             HERE/'INQUIRY-REVISION-APPLICATION.md',
             REPO/'sources/15-codex-theory-conversations/2026-10-06-concern-inquiry-revision.md']
    links = []
    for path in files:
        links += check_links(path, path.read_text())
        bound[str(path.relative_to(REPO))] = digest(path)
    integration = json.loads((HERE/'INQUIRY-REVISION-INTEGRATION.json').read_text())
    for edit in integration['edits']:
        path = REPO/edit['path']
        assert path.read_text().count(edit['addition']) == 1, edit['path']
        links += check_links(path, edit['addition'])
    for path in (EXPERIMENT/'independent-check.json', FORMAL/'verification.json',
                 EXPERIMENT/'formal-correspondence.json', HERE/'INQUIRY-REVISION-INTEGRATION.json',
                 Path(__file__)):
        bound[str(path.relative_to(REPO))] = digest(path)
    report = dict(status='passed', scope='Receipt/source binding and integration checks; no scientific rerun.',
                  local_links=len(links), integration_entries=len(integration['edits']),
                  new_lean_audits=formal['new_audits'], inherited_lean_audits=formal['inherited_audits'],
                  original_laws_preserved=expected_old, source_sha256=bound, links=links)
    (HERE/'INQUIRY-REVISION-CHECKS.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('status','local_links','integration_entries','new_lean_audits','inherited_lean_audits')}))


if __name__ == '__main__':
    main()
