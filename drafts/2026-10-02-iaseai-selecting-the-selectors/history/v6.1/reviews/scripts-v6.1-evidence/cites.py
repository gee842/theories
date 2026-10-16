import re, pathlib, collections
V=pathlib.Path('/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1')
YR=r'(?:1[5-9]|20)\d\d[ab]?'
def refs(text):
    out={}
    for line in text.splitlines():
        if not line.startswith('- '): continue
        s=line[2:]
        first=s.split(',')[0].split(' ')[0].strip('.*')
        for pre,k in (('Dal Bó','Dal'),('Bueno de','Bueno'),('Van Evera','Van'),('Maynard Smith','Maynard'),('Yan Fu','Yan'),('Pérez','Pérez-Castrillo')):
            if s.startswith(pre): first=k
        # year = first year after authors
        m=re.search(r'\b('+YR+r')(?:/\d+)?\.',s)
        if not m: m=re.search(r'\b('+YR+r')',s)
        years=[m.group(1)] if m else []
        # multi-year entries like Schelling 1960; 1966
        years+= [y for y in re.findall(r'; ('+YR+r')\.',s)]
        for y in years: out[(first,y)]=line
    return out
# broad in-text: any capitalized surname followed within 60 chars by a year
CIT=re.compile(r"([A-Z][A-Za-zÀ-ÿ'’\-]+)(?:(?:,| and|,? and) (?:[A-Z][A-Za-zÀ-ÿ'’\-]+|de|van|von|Bó)(?: [A-Z][A-Za-zÀ-ÿ'’\-]+)?)*(?: et al\.)?(?:['’]s)? \(?("+YR+r")(?:/\d+)?(?:, ("+YR+r"))?")
SKIP={'Section','Sections','Proposition','Propositions','Theorem','Lemma','Remark','Definition','Corollary','Assumption','Stage','Convention','Treaty','Protocol','September','October','December','November','July','August','June','April','March','February','January','In','Test','The','EV','Branch','Since','Over','By','From','Until','After','Before','Plan','A','Ψ','IASEAI','V','Theory','Report','Summit','Action','Framework','Policy','Studies','Cor','Prop','Lem','Def','Rem','Thm'}
ALIAS={'Mesquita':'Bueno','Bó':'Dal','Evera':'Van'}
for doc in ('THEORY','SUPPLEMENT','DISCUSSION'):
    t=(V/f'{doc}.md').read_text()
    body,_,rl=t.partition('\n## References')
    R=refs(rl)
    cited=collections.Counter(); unresolved=set()
    for m in CIT.finditer(body):
        a=re.sub(r"['’]s$","",m.group(1)); a=ALIAS.get(a,a)
        if a in SKIP: continue
        for y in (m.group(2),m.group(3)):
            if not y: continue
            if (a,y) in R: cited[(a,y)]+=1
            else: unresolved.add(f'{a} {y}')
    print('=='*10,doc,'refs',len(R))
    print('UNRESOLVED in-text (check by eye):',sorted(unresolved))
    print('LISTED BUT NOT FOUND IN TEXT:')
    for k,l in sorted(R.items()):
        if k not in cited: print('   ',k, l[:110])
