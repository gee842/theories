"""Owned integration, link and source-currency checks; no scientific reruns."""
from pathlib import Path
from hashlib import sha256
from urllib.parse import unquote
import json
import re

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
THEORY=ROOT/'theories/becoming/chapters'
EXP=ROOT/'experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/revision/metarevision/methods/formation'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def anchors(path):
    result,counts=set(),{}
    for title in re.findall(r'^#{1,6}\s+(.+)$',path.read_text(),re.M):
        base=re.sub(r'[^\w\- ]','',title.lower()).replace(' ','-')
        n=counts.get(base,0)
        result.add(base if not n else f'{base}-{n}')
        counts[base]=n+1
    return result


def run():
    full=[THEORY/'AUTONOMOUS-METHOD-FORMATION.md',THEORY/'MATHEMATICAL-ROOT-FRONTIER.md',
          HERE/'AUTONOMOUS-METHOD-FORMATION-MATH.md',HERE/'AUTONOMOUS-METHOD-FORMATION-REVIEW.md',
          HERE/'MATHEMATICAL-ROOT-FRONTIER-MATH.md',HERE/'MATHEMATICAL-ROOT-FRONTIER-SOURCES.md',
          HERE/'MATHEMATICAL-ROOT-FRONTIER-REVIEW.md',EXP/'README.md',EXP/'PROTOCOL.md',
          ROOT/'sources/15-codex-theory-conversations/2026-10-06-autonomy-and-mathematical-root-frontier.md']
    texts={p:p.read_text() for p in full}
    owned=json.loads((HERE/'AUTONOMY-ROOT-FRONTIER-INDEX-EDITS.json').read_text())
    for name,paragraph in owned.items():
        p=ROOT/name
        assert p.read_text().count(paragraph)==1,name
        texts[p]=paragraph
    integration=HERE/'MATHEMATICS-REVIEW.md'
    texts[integration]=integration.read_text().split('## Autonomous connections and reconstruction of the mathematical root\n',1)[1].split('\n## ',1)[0]
    links=fragments=0
    for p,text in texts.items():
        assert text.count(r'\[')==text.count(r'\]'),p
        assert text.count(r'\(')==text.count(r'\)'),p
        for href in re.findall(r'\]\(([^\s)]+)\)',text):
            if re.match(r'^[a-zA-Z]+:',href):
                continue
            path,sep,fragment=unquote(href).partition('#')
            target=(p.parent/path).resolve() if path else p
            assert target.exists() or target==HERE/'AUTONOMY-ROOT-FRONTIER-CHECKS.json',(p,href)
            links+=1
            if sep:
                assert fragment in anchors(target),(p,href)
                fragments+=1
    science=json.loads((EXP/'results.json').read_text())
    reference=json.loads((EXP/'independent-check.json').read_text())
    previous=json.loads((EXP.parent/'results.json').read_text())
    dependencies={}
    for name,expected in science['source_hashes'].items():
        assert digest(EXP/name)==expected,name
        dependencies[str((EXP/name).relative_to(ROOT))]=expected
    for hashes in (science['inherited_hashes'],science['handoff']['source_hashes'],
                   reference['source_hashes'],previous['source_hashes']):
        for name,expected in hashes.items():
            assert digest(ROOT/name)==expected,name
            dependencies[name]=expected
    assert digest(EXP/'results.json')==reference['checked_producer_results_sha256']
    assert len(science['family'])==reference['histories']==448
    assert len(science['fixtures'])==reference['checked_saved_fixtures']==35
    assert len(science['renamings'])==reference['renamed_cases']==24
    assert len(reference['guards'])==8
    assert science['summary']['rejected_and_replaced']==128
    assert reference['retained_correctness']=={'True':448}
    assert science['fixtures']['four_first_0']['fuel']=='4209/65536'
    assert science['fixtures']['outside_delayed']['retained']
    assert science['fixtures']['outside_delayed']['predictively_equivalent'] is False
    record=dict(scope='document and source-currency checks; formal arguments are hand proofs with separate internal review',
        documents_or_owned_sections=len(texts),local_links=links,anchors=fragments,
        formula_delimiters='balanced',
        full_file_sha256={str(p.relative_to(ROOT)):digest(p) for p in full},
        owned_section_sha256={str(p.relative_to(ROOT)):sha256(text.encode()).hexdigest()
                              for p,text in texts.items() if p not in full},
        scientific_dependency_sha256=dependencies,
        scientific_receipt_sha256={p.name:digest(p) for p in (EXP/'results.json',EXP/'independent-check.json')},
        checker_sha256=digest(Path(__file__)),
        index_edit_manifest_sha256=digest(HERE/'AUTONOMY-ROOT-FRONTIER-INDEX-EDITS.json'))
    (HERE/'AUTONOMY-ROOT-FRONTIER-CHECKS.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ('documents_or_owned_sections','local_links','anchors','formula_delimiters')}))


if __name__=='__main__':
    run()
