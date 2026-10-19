import re,sys
from pathlib import Path
src=Path(sys.argv[1]); out=Path(sys.argv[2])
pat=re.compile(r"(:\s*World\s*:=\s*)⟨")
def split_top(s):
    parts,depth,cur=[],0,''
    for ch in s:
        if ch in '([{⟨': depth+=1
        if ch in ')]}⟩': depth-=1
        if ch==',' and depth==0: parts.append(cur); cur=''
        else: cur+=ch
    parts.append(cur); return [p.strip() for p in parts]
total=0
for f in sorted(src.glob('*.lean')):
    s=f.read_text(); n=0
    while True:
        m=pat.search(s)
        if not m: break
        start=m.end()-1; depth=0
        for k in range(start,len(s)):
            if s[k] in '([{⟨': depth+=1
            elif s[k] in ')]}⟩':
                depth-=1
                if depth==0: end=k; break
        parts=split_top(s[start+1:end])
        if len(parts)!=3:
            print('skip',f.name,parts[:1]); s=s[:start]+'⟪'+s[start+1:]; continue
        repl='World.of ('+') ('.join(parts)+')'
        s=s[:start]+repl+s[end+1:]; n+=1
    s=s.replace('⟪','⟨')
    if n:
        (out/f.name).write_text(s); total+=n; print(f.name,n)
print('total',total)
