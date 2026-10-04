"""Preservation, reference integrity and reproducibility checks for the delivered edition."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT.parent / 'v7'
VERIFY = ROOT / 'verification'
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def audit():
    baseline = json.loads((VERIFY/'v7-baseline-manifest.json').read_text())
    changed = [name for name, value in baseline.items() if not (BASE/name).is_file() or digest(BASE/name) != value]
    previous = json.loads((BASE/'src/keymap.json').read_text())
    current = json.loads((ROOT/'src/keymap.json').read_text())
    identity = lambda row: tuple(row[k] for k in ('kind','number','file'))
    declaration_changes = [k for k in set(previous)|set(current) if k not in previous or k not in current or identity(previous[k]) != identity(current[k])]
    old_claims = (BASE/'src/reg/CLAIMS.md').read_text().split('## 8. Renderings',1)[1]
    new_claims = (ROOT/'src/reg/CLAIMS.md').read_text().split('## 8. Renderings',1)[1].split('\n\n## 10.',1)[0]
    # The separating newlines before the added section are not part of the record.
    decisions_preserved = old_claims.rstrip() == new_claims.rstrip() and (ROOT/'src/reg/CLAIMS.md').read_text().split('## 8. Renderings',1)[1].startswith(old_claims)
    docs = sorted(ROOT.glob('*.md'))
    before = {p.name: digest(p) for p in docs}
    run = subprocess.run([sys.executable,str(ROOT/'src/assemble_v71.py')],capture_output=True,text=True,cwd=ROOT)
    (VERIFY/'assembly.log').write_text(run.stdout+run.stderr)
    after = {p.name: digest(p) for p in docs}
    missing_links = []
    for p in docs:
        for link in re.findall(r'\]\(([^)\n]+)\)',p.read_text()):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',link) or link.startswith('#'):
                continue
            name = re.sub(r':\d+$','',link.split('#',1)[0].strip('<>'))
            if not name:
                continue
            target = (p.parent/name).resolve()
            if not target.exists():
                missing_links.append({'document':p.name,'target':link})
    inputs = sorted({p for p in (ROOT/'src').rglob('*') if p.is_file() and p.suffix in ('.md','.py')} |
                    {ROOT/'checks_v71.py',ROOT/'xref_v71.py'} |
                    set(VERIFY.glob('*_checks.py')) | {Path(__file__).resolve()})
    manifest = {str(p.relative_to(ROOT)): digest(p) for p in inputs}
    (VERIFY/'v71-input-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    result = {
        'v7_files_checked':len(baseline), 'changed_v7_files':changed,
        'stable_declarations':len(current), 'declaration_identity_changes':declaration_changes,
        'ren_claims_sections_8_9_verbatim_content':decisions_preserved,
        'assembly_exit_code':run.returncode, 'assembly_reproducible':before==after,
        'missing_local_document_links':missing_links,
        'verified_input_files':len(manifest), 'document_sha256':after,
    }
    (VERIFY/'preservation.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    return not changed and not declaration_changes and decisions_preserved and run.returncode==0 and before==after and not missing_links

if __name__=='__main__':
    sys.exit(0 if audit() else 1)
