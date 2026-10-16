import re, pathlib
V=pathlib.Path('/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1')
YR=r'(?:1[5-9]|20)\d\d[ab]?'
def parse(line):
    s=line[2:]
    m=re.search(r'\s('+YR+r')(?:/\d+)?\.',s)
    if not m: return None
    auth=s[:m.start()].strip().rstrip('.')
    year=m.group(1)
    if auth.startswith('Yan Fu'): return (['Yan'],year)
    if auth.startswith('Larsen, Dean'): return (['Larsen'],year)
    # split authors: "Surname, I., Surname2, I. and Surname3, I." or "Surname, I. and Surname2, I." or "Surname, I. et al"
    auth=auth.replace(' et al','')
    parts=re.split(r',? and |, (?=[A-ZÀ-Ý][^,]*?, [A-Z]\.)',auth)
    sur=[]
    for p in parts:
        p=p.strip()
        name=p.split(',')[0].strip()
        if name: sur.append(name)
    return (sur,year)
for doc in ('THEORY','SUPPLEMENT','DISCUSSION'):
    t=(V/f'{doc}.md').read_text()
    body,_,rl=t.partition('\n## References')
    print('=='*8,doc)
    for line in rl.splitlines():
        if not line.startswith('- '): continue
        p=parse(line)
        if not p: print('  unparsed',line[:80]); continue
        sur,year=p
        s1=re.escape(sur[0])
        y=year
        if len(sur)==1:
            pat=s1+r"(?:['’]s)? \(?(?:[^)]{0,12}?)?"+y
            # exclude "s1 and X y" (multi-author with same first author)
            hits=[m for m in re.finditer(s1+r"(?:['’]s)?(?: \(| )"+y, body)]
            hits+= [m for m in re.finditer(s1+r" \d{4}[^;)]{0,10}, "+y, body)]
            hits+= [m for m in re.finditer(s1+r" \d{4}/\d\d, "+y, body)]
        elif len(sur)==2:
            hits=list(re.finditer(s1+r",? and "+re.escape(sur[1])+r"(?:['’]s)?(?: \(| )"+y,body))+list(re.finditer(s1+r" et al\. \(?"+y,body))
        else:
            hits=list(re.finditer(s1+r" et al\.(?:['’]s)? \(?"+y,body))+list(re.finditer(s1+r", "+re.escape(sur[1])+r"[^()]{0,60}?\(?"+y,body))
        if not hits:
            print('  NOT CITED AS LISTED:',sur,year,'|',line[:100])
