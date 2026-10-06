from pathlib import Path
from urllib.parse import urlsplit,unquote
import json,re,hashlib,datetime
root=next(p for p in Path(__file__).resolve().parents if (p/'AGENTS.md').exists());base=Path(__file__).resolve().parent;lp=base/'YITI-REN-DIRECTION-EDITS.json';ledger=json.loads(lp.read_text());edits=ledger['edits'];formal=Path('experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern')
new=[formal/'PurposeCorrection.lean',formal/'PurposeCorrectionHistory.lean',formal/'check_purpose.py',Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/YITI-REN-PURPOSE-MATH.md'),Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/YITI-REN-DIRECTION-ARGUMENT.md')]
sha=lambda x:hashlib.sha256(x).hexdigest()
def slug(s):return ''.join(c for c in s.strip().lower().replace('`','') if c.isalnum() or c in '_ -').replace(' ','-')
def anchors(p):
 out=[];counts={}
 for line in p.read_text().splitlines():
  m=re.match(r'^#{1,6}\s+(.+?)\s*#*$',line)
  if m:
   a=slug(m[1]);n=counts.get(a,0);counts[a]=n+1;out.append(a+(f'-{n}' if n else ''))
 return out
links=[];errors=[];seen=set()
texts=[(e['path'],e['after']) for e in edits]+[(str(p),(root/p).read_text()) for p in new if p.suffix=='.md']
for source,text in texts:
 for link in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)',text):
  u=urlsplit(link.strip('<>'))
  if u.scheme or link.startswith('//'):continue
  if (source,link) in seen:continue
  seen.add((source,link));p=((root/source).parent/unquote(u.path)) if u.path else root/source;valid=p.is_file()
  if valid and u.fragment:valid=unquote(u.fragment) in anchors(p)
  links.append(dict(source=source,reference=link,valid=valid))
  if not valid:errors.append(['link',source,link])
recovery=[]
for path in sorted({e['path'] for e in edits}):
 s=(root/path).read_text();current=s;own=[e for e in edits if e['path']==path];valid=True
 for e in reversed(own):
  if s.count(e['after'])!=1:valid=False;break
  s=s.replace(e['after'],e['before'],1)
 recovery.append(dict(path=path,owned_fragments_reversible_in_memory=valid,baseline_hash_matches=valid and sha(s.encode())==own[0]['before_sha256'],current_sha256=sha(current.encode())))
 if not valid:errors.append(['owned_recovery',path])
allpaths=sorted({e['path'] for e in edits}|{str(p) for p in new});files=[]
for path in allpaths:
 data=(root/path).read_bytes();text=data.decode();trailing=[i for i,l in enumerate(text.splitlines(),1) if l.rstrip()!=l];control=[i for i,c in enumerate(text) if ord(c)<32 and c not in '\n\r\t']
 files.append(dict(path=path,sha256=sha(data),trailing_whitespace_lines=trailing,unexpected_control_character_offsets=control))
 if trailing or control:errors.append(['whitespace',path,trailing,control])
receiptpath=root/formal/'purpose-verification.json';receipt=json.loads(receiptpath.read_text());assert receipt['status']=='passed'
bindings=[]
for row in receipt['modules']:
 source_ok=sha((root/row['source']).read_bytes())==row['sha256'];log_ok=sha((root/formal/row['log']).read_bytes())==row['log_sha256'];bindings.append(dict(module=row['module'],source_matches=source_ok,log_matches=log_ok))
 if not source_ok or not log_ok:errors.append(['proof_binding',row['module']])
source=edits[0];prefix=(root/source['path']).read_text().startswith(source['before'].rstrip());assert prefix
out=dict(checker_sha256=sha(Path(__file__).read_bytes()),status='passed' if not errors else 'failed',checked_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope='Research integration/link and source binding check; does not add a compiler run or certify ethical universality.',owned_edits=len(edits),files=files,links=links,edit_recovery=recovery,source_prefix_preserved=prefix,proof_receipt=str(receiptpath.relative_to(root)),proof_receipt_sha256=sha(receiptpath.read_bytes()),proof_bindings=bindings,new_theorem_audits=receipt['new_audits'],fresh_modules=len(receipt['modules']),independent_review='Separate collaborating task read both final modules, rehashed31sources/logs and receipts, then accepted main12/integration8 scope; no second build.',universal_proof_completed=False,errors=errors,recovery_scope_note='In-memory reversal only; shared index baselines may differ due concurrent changes outside owned fragments, which are not reverted or certified as whole-file equality.')
(base/'YITI-REN-DIRECTION-CHECKS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=out['status'],files=len(files),links=len(links),owned_edits=len(edits),matched_baselines=sum(x['baseline_hash_matches'] for x in recovery),proof_bindings=len(bindings),errors=errors),ensure_ascii=False,indent=2))
