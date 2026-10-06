"""Validate owned prose, links and current scientific receipts; no reruns."""
from pathlib import Path
from hashlib import sha256
from urllib.parse import unquote
import json
import re

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
THEORY=ROOT/'theories/shengsheng-buxi-generative-existence/unified-2026-10-05'
EXP=ROOT/'experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/revision/metarevision/methods'


def digest(p):
    return sha256(p.read_bytes()).hexdigest()


def anchors(p):
    found,counts=set(),{}
    for title in re.findall(r'^#{1,6}\s+(.+)$',p.read_text(),re.M):
        base=re.sub(r'[^\w\- ]','',title.lower()).replace(' ','-')
        count=counts.get(base,0)
        found.add(base if not count else f'{base}-{count}')
        counts[base]=count+1
    return found


def run():
    full=[THEORY/'METHOD-REVISION.md',HERE/'METHOD-REVISION-MATH.md',
          HERE/'METHOD-REVISION-REVIEW.md',HERE/'METHOD-REVISION-COMPARATORS.md',
          EXP/'README.md',EXP/'PROTOCOL.md',
          ROOT/'sources/15-codex-theory-conversations/2026-10-06-method-revision-continuation.md']
    texts={p:p.read_text() for p in full}
    owned=json.loads((HERE/'METHOD-REVISION-INDEX-EDITS.json').read_text())
    for name,paragraph in owned.items():
        p=ROOT/name
        assert p.read_text().count(paragraph)==1,name
        texts[p]=paragraph
    integration=HERE/'MATHEMATICS-REVIEW.md'
    texts[integration]=integration.read_text().split('## A finite native-consequence-to-method connection\n',1)[1].split('\n## ',1)[0]
    links=fragments=0
    for p,text in texts.items():
        assert text.count(r'\[')==text.count(r'\]'),p
        assert text.count(r'\(')==text.count(r'\)'),p
        for href in re.findall(r'\]\(([^\s)]+)\)',text):
            if re.match(r'^[a-zA-Z]+:',href):
                continue
            path,sep,fragment=unquote(href).partition('#')
            target=(p.parent/path).resolve() if path else p
            assert target.exists() or target==HERE/'METHOD-REVISION-CHECKS.json',(p,href)
            links+=1
            if sep:
                assert fragment in anchors(target),(p,href)
                fragments+=1
    science=json.loads((EXP/'results.json').read_text())
    independent=json.loads((EXP/'independent-check.json').read_text())
    for hashes in (science['source_hashes'],science['handoff']['source_hashes'],independent['source_hashes']):
        for name,expected in hashes.items():
            assert digest(ROOT/name)==expected,name
    assert digest(EXP/'results.json')==independent['checked_results_sha256']
    assert len(science['fixtures'])==independent['fixtures']==19
    assert len(science['family'])==independent['finite_histories']==896
    assert len(science['renamings'])==len(independent['renamed_cases'])==12
    assert len(independent['prefix_denials'])==8
    assert science['summaries']['feedback']['retained_wrong']==48
    assert science['summaries']['broad']['retained_correct']==224
    record=dict(scope='owned document/link/formula/source-currency checks, no scientific rerun',
        documents_or_owned_sections=len(texts),local_links=links,anchors=fragments,
        formula_delimiters='balanced',
        full_file_sha256={str(p.relative_to(ROOT)):digest(p) for p in full},
        owned_section_sha256={str(p.relative_to(ROOT)):sha256(t.encode()).hexdigest()
                              for p,t in texts.items() if p not in full},
        scientific_receipt_sha256={p.name:digest(p) for p in (EXP/'results.json',EXP/'independent-check.json')},
        checker_sha256=digest(Path(__file__)),
        index_edit_manifest_sha256=digest(HERE/'METHOD-REVISION-INDEX-EDITS.json'))
    (HERE/'METHOD-REVISION-CHECKS.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ('documents_or_owned_sections','local_links','anchors','formula_delimiters')}))


if __name__=='__main__':
    run()
