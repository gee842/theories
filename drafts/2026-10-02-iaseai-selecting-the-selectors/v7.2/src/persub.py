import re,sys
t=open(sys.argv[1] if len(sys.argv)>1 else 'THEORY.md').read()
def words(s):
    s=re.sub(r'\$\$.*?\$\$',' x ',s,flags=re.S); s=re.sub(r'\$[^$]*\$',' x ',s)
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-]*",s))
for part in re.split(r'(?m)^(?=#{2,3} )',t):
    if part.strip(): print(f"{words(part):5}  {part.splitlines()[0][:70]}")
