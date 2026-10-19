import re,glob,sys,json
L='experiments/integrated-correction/general-framework/generative-basis/lean/'
files=[f for f in glob.glob(L+'**/*.lean',recursive=True) if not any(x in f for x in ['/history/','becoming-checks','.lake','verification-history','.build','legacy-replays'])]
decl=re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable|partial|unsafe)\s+)*(theorem|lemma|def|structure|inductive|abbrev|class|instance|opaque|axiom)\s+([^\s:({\[]+)')
names=set(); core=set()
for f in files:
    ns=[]
    try: lines=open(f,encoding='utf8').read().split('\n')
    except: continue
    for l in lines:
        m=re.match(r'^\s*namespace\s+(\S+)',l)
        if m: ns.append(m.group(1)); continue
        m=re.match(r'^\s*end\s+(\S+)',l)
        if m and ns and ns[-1]==m.group(1): ns.pop(); continue
        m=decl.match(l)
        if m:
            full='.'.join(ns+[m.group(2)]); parts=full.split('.')
            for i in range(len(parts)):
                names.add('.'.join(parts[i:]))
                if '/becoming/Becoming/' in f: core.add('.'.join(parts[i:]))
            # structure fields etc not handled
json.dump({'all':sorted(names),'core':sorted(core)},open(sys.argv[1],'w'))
print(len(names),len(core),len(files))
