import json,hashlib,subprocess,sys,re,difflib
chk=json.loads((t:=open(sys.argv[1]).read())[t.index('{'):])
def version_by_hash(path,sha):
    revs=subprocess.run(['git','log','--format=%H','-40','--',path],capture_output=True,text=True).stdout.split()
    for r in revs:
        b=subprocess.run(['git','show',f'{r}:{path}'],capture_output=True).stdout
        if hashlib.sha256(b).hexdigest()==sha: return b.decode()
    return None
for x in chk['source_drift']+chk['unrelated_source_drift']:
    rid,path=x['id'],x['path']
    old=version_by_hash(path,x['reviewed_sha256']); new=open(path).read()
    if old is None: print('##',rid,path,'OLD VERSION NOT FOUND'); continue
    rec=json.load(open(f'theories/becoming/results/records/{rid}.json'))
    title=rec.get('title',{}); title=title.get('en') if isinstance(title,dict) else title
    print(f'\n## {rid} — {title}  [{path.split("/")[-1]}]')
    ol,nl=old.split('\n'),new.split('\n')
    sm=difflib.SequenceMatcher(None,ol,nl,autojunk=False)
    secs=set(x['changed_sections'])
    def sec_of(lines,i):
        for j in range(i,-1,-1):
            if lines[j].startswith('## '): return lines[j]
        return '(pre)'
    shown=0
    for op,a1,a2,b1,b2 in sm.get_opcodes():
        if op=='equal': continue
        for i in range(a1,a2):
            line=ol[i]; s=sec_of(ol,i)
            links=rid in line
            if links or (s in secs and len(secs)<5):
                n='\n'.join(nl[b1:b2])
                # show changed region compactly
                w=difflib.SequenceMatcher(None,line,n,autojunk=False)
                parts=[]
                for o,c1,c2,d1,d2 in w.get_opcodes():
                    if o!='equal': parts.append(f'[-{line[c1:c2][:400]}-]{{+{n[d1:d2][:400]}+}}')
                print(f'  {"LINK " if links else ""}{s[:40]} :: '+' … '.join(parts)[:1500]); shown+=1
    if not shown: print('  (no changed line links this record; changes elsewhere in cited sections)')
