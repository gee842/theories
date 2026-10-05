from pathlib import Path
import hashlib,json,re,subprocess,sys,zipfile
root=Path(__file__).resolve().parents[2]
archive=root/'outputs/access-study-evidence.zip'
target=root/'work/access-study-reproduction'
target.mkdir(exist_ok=True)
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    manifest=json.loads(z.read('MANIFEST.json'))
    for name,digest in manifest['files'].items():assert hashlib.sha256(z.read(name)).hexdigest()==digest,name
    z.extractall(target)
base=target/'work/access-study'
names=['main.json','controls.json','partition-checks.json','two-period-witnesses.json']
expected={n:(base/'results'/n).read_bytes() for n in names}
checks=[]
for name in ['run_study.py','formal_access_verify.py','audit_oracle.py','audit_compare.py','audit_controls.py','audit_h4.py','audit_no_output.py','audit_summary.py']:
    proc=subprocess.run([sys.executable,name],cwd=base,text=True,capture_output=True)
    (base/(name+'.run.log')).write_text(proc.stdout+proc.stderr)
    assert proc.returncode==0,(name,proc.stderr)
    checks.append(name)
for n,data in expected.items():assert (base/'results'/n).read_bytes()==data,n
for p in (root/'outputs').glob('*.md'):
    s=p.read_text()
    assert s.count(r'\[')==s.count(r'\]'),p
    assert s.count(r'\(')==s.count(r'\)'),p
    for link in re.findall(r'\]\(([^)]+)\)',s):
        if '://' not in link and not link.startswith('#'):
            assert (p.parent/link.split('#')[0]).exists(),(p,link)
result={'status':'passed','archive_entries_hashed':len(manifest['files']),'numerical_scripts_rerun':checks,'byte_identical_result_files':names,'deliverable_links_and_math_delimiters':'passed'}
(root/'work/access-study/bundle-verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
