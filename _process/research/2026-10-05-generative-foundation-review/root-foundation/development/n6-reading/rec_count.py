"""Count the core retired words in each record's live strings (N6)."""
import json, glob, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rec_dump import leaves
from reading_pass import RECORDS
P = re.compile(r'regist\w*|refut\w*|learner\w*|识|否证|学习者|登记|belief|信念', re.I)
K = re.compile(r'知识|意识|认识|辨识|识别|共识|unrefuted|refutable|irrefutable', re.I)
def core(s):
    t = re.sub(r'`[^`]*`', '', s); t = re.sub(r'\b\w+[._]\w[\w.]*', '', t); t = re.sub(r'\b[a-z0-9]+(?:-[a-z0-9]+)+\b', '', t)
    t = K.sub('', t)
    return len(P.findall(t))
if __name__ == "__main__":
    out = []
    for f in sorted(glob.glob(RECORDS + '*.json')):
        d = json.load(open(f)); n = sum(core(s) for _, s in leaves(d))
        if n: out.append((n, os.path.basename(f)[:-5]))
    for n, s in sorted(out, reverse=True): print(n, s)
    print(len(out), sum(n for n, _ in out))
