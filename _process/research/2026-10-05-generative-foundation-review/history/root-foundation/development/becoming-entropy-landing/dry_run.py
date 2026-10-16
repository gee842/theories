#!/usr/bin/env python3
"""Exercise the additive landing scripts in temporary files with stand-in receipts.
No Lean check is performed and no current proof validation is claimed.
"""
import hashlib
import importlib.util
import json
import re
import runpy
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip())
KIT=HERE.parent/'becoming-landing-kit'
spec=importlib.util.spec_from_file_location('kit',KIT/'kit.py')
kit=importlib.util.module_from_spec(spec);spec.loader.exec_module(kit)
sys.modules['kit']=kit


def invoke(script,args):
    prior=sys.argv
    sys.argv=[str(script),*map(str,args)]
    try:runpy.run_path(str(script),run_name='__main__')
    finally:sys.argv=prior


with tempfile.TemporaryDirectory(prefix='dry-',dir=HERE) as scratch:
    W=Path(scratch)
    paths=[kit.STUDY,kit.PLAN,kit.CHAPTER,kit.RECEIPT,kit.PERI_RECEIPT,
           f'{kit.D}/README.md',f'{kit.D}/Becoming.lean',f'{kit.D}/check_becoming.py',
           'theories/becoming/results/data/arguments-m-z.json','_process/RESEARCH-DIRECTIVES.md',
           'sources/15-codex-theory-conversations/2026-10-11-difference-in-becoming.md']
    paths += [str(p.relative_to(ROOT)) for p in (ROOT/kit.D/'Becoming').glob('*.lean')]
    paths += [str(p.relative_to(ROOT)) for p in (ROOT/kit.RECORDS).glob('*.json')]
    for rel in paths:
        dest=W/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/rel,dest)
    # Copy the package without its recursively nested scratch directory.
    target=W/kit.DEV/HERE.name
    target.mkdir(parents=True)
    for child in HERE.iterdir():
        if child==W or child.name.startswith('dry-') or child.name=='__pycache__':continue
        if child.is_dir():shutil.copytree(child,target/child.name)
        else:shutil.copyfile(child,target/child.name)
    # The docs dry run checks against current, already reconciled chapter bytes rather
    # than a hypothetical Git commit; no fake Git history is created.
    chapter=(W/kit.CHAPTER).read_bytes()
    cat=W/'theories/becoming/results/data/arguments-m-z.json'
    entries=json.loads(cat.read_text());entry=next(x for x in entries if x['id']=='the-theory-of-becoming')
    assert entry['source_sha256']==hashlib.sha256(chapter).hexdigest(), 'Current chapter reading entry is stale; wait for integrator to reconcile it.'
    S=1+max(map(int,re.findall(r'^## (\d+)\.',(W/kit.STUDY).read_text(),re.M)))
    invoke(KIT/'land_lean.py',[HERE,W])
    receipt=json.loads((W/kit.RECEIPT).read_text())
    old=json.loads(subprocess.check_output(['git','show','52ff83a4:'+kit.RECEIPT],cwd=ROOT,text=True))
    mod=next(x for x in old['modules'] if x['module']=='Becoming.Entropy')
    reconciliation=json.loads((HERE/'provenance.json').read_text())['helper_name_reconciliation']
    for declaration in mod['declarations']:
        name=declaration['name'] if isinstance(declaration,dict) else declaration
        old_name=name.removeprefix('Becoming.')
        if old_name in reconciliation:
            renamed='Becoming.'+reconciliation[old_name]
            if isinstance(declaration,dict):declaration['name']=renamed
            else:mod['declarations'][mod['declarations'].index(declaration)]=renamed
    receipt['modules'].append(mod)
    receipt['core_closure'].append('Becoming.Entropy')
    receipt['source_sha256']['Becoming.Entropy']=hashlib.sha256((W/kit.lean('Entropy')).read_bytes()).hexdigest()
    (W/kit.RECEIPT).write_text(json.dumps(receipt))
    original_run=subprocess.run
    def fake_base(args,*a,**kw):
        if args[:2]==['git','show']:
            assert args[2]=='DRY-CURRENT:'+kit.CHAPTER
            return subprocess.CompletedProcess(args,0,stdout=chapter)
        return original_run(args,*a,**kw)
    subprocess.run=fake_base
    try:invoke(KIT/'land_docs.py',[HERE,W,S,'DRY-CURRENT'])
    finally:subprocess.run=original_run
    invoke(KIT/'make_records.py',[HERE,W,'2026-10-13T00:00:00+00:00',S])
    rec=json.loads((W/kit.RECORDS/'entropy-history-and-record.json').read_text())
    assert len(rec['history'])==4
    assert len(next(r for r in rec['references'] if r['path']==kit.lean('Entropy'))['declarations'])==233
    for rel in [kit.STUDY,kit.PLAN,kit.CHAPTER]:
        s=(W/rel).read_text()
        assert '@PERI@' not in s and '{N_MODULE}' not in s and '{S_ENTROPY}' not in s
    print(f'DRY RUN PASSED at study section {S}: anchors, 233 declared references, dependency names, preserved history; stand-in receipts only, no Lean validation.')
