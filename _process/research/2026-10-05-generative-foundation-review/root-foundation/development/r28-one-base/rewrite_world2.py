import re,sys
from pathlib import Path
src=Path(sys.argv[1]); out=Path(sys.argv[2])
def split_top(s):
    parts,depth,cur=[],0,''
    for ch in s:
        if ch in '([{⟨': depth+=1
        if ch in ')]}⟩': depth-=1
        if ch==',' and depth==0: parts.append(cur); cur=''
        else: cur+=ch
    parts.append(cur); return [p.strip() for p in parts]
def match_end(s,start):
    depth=0
    for k in range(start,len(s)):
        if s[k] in '([{⟨': depth+=1
        elif s[k] in ')]}⟩':
            depth-=1
            if depth==0: return k
total=0
for f in sorted(src.glob('*.lean')):
    s=f.read_text(); n=0; k=0
    while True:
        k=s.find('⟨',k)
        if k<0: break
        e=match_end(s,k)
        if e and re.match(r'\s*:\s*World\)',s[e+1:]):
            parts=split_top(s[k+1:e])
            if len(parts)==3:
                repl='World.of ('+') ('.join(parts)+')'
                s=s[:k]+repl+s[e+1:]; n+=1
        k+=1
    if n:
        (out/f.name).write_text(s); total+=n; print(f.name,n)
print('total',total)
