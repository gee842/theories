import os
import sys,re,glob,os,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from parse import strip_comments
ROOT=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), *[".."]*6)) + "/experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming"
pat=re.compile(sys.argv[1]); mode=sys.argv[2] if len(sys.argv)>2 else 'lines'
tot=0;files=0
for f in sorted(glob.glob(ROOT+'/*.lean')):
    src=strip_comments(open(f).read()).split('\n'); n=0
    for i,l in enumerate(src,1):
        ms=pat.findall(l)
        if ms:
            n+=len(ms)
            if mode=='lines': print(f"{os.path.basename(f)}:{i}: {l.strip()[:150]}")
    if n: files+=1; tot+=n
    if n and mode=='files': print(os.path.basename(f), n)
print('TOTAL',tot,'FILES',files)
