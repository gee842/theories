#!/usr/bin/env python3
"""Preserve R5's original record history and land its directive after kit make_records.
Usage: finish_record.py W S. Only the integrator runs this against a landing checkout.
"""
import hashlib
import json
import sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
W=Path(sys.argv[1]).resolve()
S=sys.argv[2]
RF='_process/research/2026-10-05-generative-foundation-review/root-foundation'
path=W/'theories/becoming/results/records/entropy-history-and-record.json'
record=json.loads(path.read_text())
provenance=json.loads((HERE/'provenance.json').read_text())
source=W/provenance['lean_source']
assert hashlib.sha256(source.read_bytes()).hexdigest()==provenance['landing_source_sha256'], 'Reconcile source edits before retaining this package claim.'
old=json.loads((HERE/'docs/original-history.json').read_text())
# The old §80 was provisional. Keep its historical reference explicit, not a live current-section claim.
for item in old:
    item['zh']=item['zh'].replace('整合文档 §80','R5 分支历史文档的暂定 §80（当前整合为 §'+S+'）')
    item['en']=item['en'].replace('section 80 of the integration note','provisional section 80 in the R5 branch history (current integration section '+S+')')
record['history']=old+record['history']
plan=f'{RF}/BECOMING-UNIFICATION-PLAN.md'
record['references'].append({'path':plan,'role':'integration','sha256':hashlib.sha256((W/plan).read_bytes()).hexdigest(),'declarations':[]})
path.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')

directives=W/'_process/RESEARCH-DIRECTIVES.md'
s=directives.read_text()
text=(HERE/'docs/directive.md').read_text().rstrip('\n')
prefix="[Ren's zero-premise redirect, 11 October 2026]"
assert s.count(prefix)==1 and "[Ren's reading of the least loss as entropy" not in s, 'Directive moved or already present; reconcile before applying.'
s=s.replace(prefix,text+'\n\n'+prefix,1)
directives.write_text(s)
print('Preserved R5 record history and added the original-scope directive.')
