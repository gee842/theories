#!/usr/bin/env python3
"""Retrieve unchanged original MAT files from the public mirror and verify official hashes."""
import concurrent.futures,hashlib,json,requests,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
REPO=next(p for p in HERE.parents if (p/'RESEARCH.md').exists())
ROOT=REPO/'sources/situated-recovery/heald-2021'
ROOT.mkdir(parents=True,exist_ok=True)
(ROOT/'originals').mkdir(exist_ok=True)
files=[]
for page in range(1,4):
 p=ROOT/f'dryad-files-page{page}.json'
 if not p.exists():
  r=requests.get(f'https://datadryad.org/api/v2/versions/140790/files?page={page}',timeout=40);r.raise_for_status();p.write_bytes(r.content)
 files += json.loads(p.read_text())['_embedded']['stash:files']
chosen=[f for f in files if 'recovery_participant' in f['path']]
assert len(chosen)==16
(ROOT/'selected-files.json').write_text(json.dumps(chosen,indent=2)+'\n')
def fetch(f):
 p=ROOT/'originals'/f['path'];u='https://zenodo.org/records/5516490/files/'+f['path']+'?download=1'
 for attempt in range(3):
  try:
   if not p.exists():
    r=requests.get(u,timeout=(20,90));r.raise_for_status()
    assert len(r.content)==f['size'] and hashlib.sha256(r.content).hexdigest()==f['digest'],f['path']
    p.write_bytes(r.content)
   b=p.read_bytes();assert len(b)==f['size'] and hashlib.sha256(b).hexdigest()==f['digest']
   print(f['path'],'verified',len(b),flush=True)
   return {'path':f['path'],'url':u,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'dryad_digest_matches':True}
  except Exception as e:
   print(f['path'],'attempt',attempt+1,type(e).__name__,str(e)[:150],flush=True)
   if attempt==2:raise
   time.sleep(2)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:records=list(pool.map(fetch,chosen))
print('All 16 original MAT files verified against deposited SHA-256 values; retained retrieval.json is not overwritten.')
