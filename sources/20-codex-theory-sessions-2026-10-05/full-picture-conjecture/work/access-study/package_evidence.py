"""Package completed evidence; excludes caches and plotting dependencies."""
from pathlib import Path
import hashlib,json,zipfile
ROOT=Path(__file__).resolve().parents[2]
HERE=ROOT/'work/access-study'
files={}
for p in HERE.iterdir():
    if p.is_file() and p.suffix in ('.py','.json') and p.name!='package_evidence.py':
        files[str(p.relative_to(ROOT))]=p.read_bytes()
for name in ('PROTOCOL.md','implementation-audit.md'):
    files['work/access-study/'+name]=(HERE/name).read_bytes()
files['work/access-study/formal-access.md']=(HERE/'formal-access.md').read_text().replace('Clinical/infrastructure payments','Operational/infrastructure payments').encode()
for p in (HERE/'results').rglob('*'):
    if p.is_file():files[str(p.relative_to(ROOT))]=p.read_bytes()
for name in ('access-outcomes.png','access-outcomes.svg'):
    files['outputs/'+name]=(ROOT/'outputs'/name).read_bytes()
files['README.md']=(HERE/'BUNDLE-README.md').read_bytes()
manifest={'description':'SHA-256 of archived files, excluding this manifest','files':{k:hashlib.sha256(v).hexdigest() for k,v in sorted(files.items())}}
files['MANIFEST.json']=(json.dumps(manifest,indent=2)+'\n').encode()
out=ROOT/'outputs/access-study-evidence.zip'
with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED) as z:
    for name,data in sorted(files.items()):z.writestr(name,data)
with zipfile.ZipFile(out) as z:assert z.testzip() is None
print(json.dumps({'file':str(out),'entries':len(files),'bytes':out.stat().st_size}))
