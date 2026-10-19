import re,glob,os,json,collections
root='/Users/ren/theories/experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
out=[]
declre=re.compile(r'^(\s*)(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*(theorem|lemma|def|abbrev|structure|inductive|class|instance)\s+([^\s:({\[]+)?')
for p in sorted(glob.glob(root+'*.lean')):
    mod='Becoming.'+os.path.basename(p)[:-5]
    lines=open(p).read().split('\n')
    ns=[]; incomment=0
    i=0
    while i<len(lines):
        l=lines[i]
        s=l.strip()
        # crude block comment skip
        if s.startswith('/-') and not s.startswith('/--'):
            if '-/' not in s[2:]:
                j=i+1
                while j<len(lines) and '-/' not in lines[j]: j+=1
                i=j+1; continue
        m=re.match(r'^namespace\s+(\S+)',s)
        if m: ns.append(m.group(1)); i+=1; continue
        m=re.match(r'^section\b(.*)',s)
        if m: ns.append(None); i+=1; continue
        m=re.match(r'^end\b\s*(\S*)',s)
        if m and ns:
            ns.pop(); i+=1; continue
        m=declre.match(l)
        if m and m.group(3):
            kind=m.group(2); name=m.group(3)
            # statement: up to ':=' or 'where' or ' | '
            stmt=[l]; j=i
            while ':=' not in ' '.join(stmt) and ' where' not in ' '.join(stmt) and j+1<len(lines) and len(stmt)<25:
                j+=1; stmt.append(lines[j])
                if lines[j].strip().startswith('|'): break
            st=' '.join(x.strip() for x in stmt)
            st=st.split(':=')[0]
            q='.'.join([x for x in ns if x]+[name])
            out.append({'module':mod,'kind':kind,'name':name,'q':q,'line':i+1,'stmt':st})
        i+=1
json.dump(out,open(os.path.dirname(os.path.abspath(__file__))+'/decls.json','w'))
c=collections.Counter(d['kind'] for d in out); print(len(out),c)
