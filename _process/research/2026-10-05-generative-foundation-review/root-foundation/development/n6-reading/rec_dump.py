"""Print a record's live strings that carry the retired words, for reading (N6)."""
import json, re, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from reading_pass import FROZEN, RECORDS
PAT = re.compile(r'regist\w*|refut\w*|learner\w*|识|否证|学习者|登记|belief|信念|\brecord\w*|记录|hypothes\w*|假设|target|目标', re.I)
KEEP = re.compile(r'知识|意识|认识|辨识|识别|共识|unrefuted|refutable')

def leaves(d, path=()):
    if isinstance(d, str):
        yield path, d
    elif isinstance(d, list):
        for i, v in enumerate(d):
            yield from leaves(v, path + (i,))
    elif isinstance(d, dict):
        for k, v in d.items():
            if k not in FROZEN:
                yield from leaves(v, path + (k,))

def hits(s):
    t = re.sub(r'`[^`]*`', '', s)
    t = re.sub(r'\b\w+[._]\w[\w.]*', '', t)
    t = re.sub(r'\b[a-z0-9]+(?:-[a-z0-9]+)+\b', '', t)
    return [m.group() for m in PAT.finditer(t) if not KEEP.fullmatch(m.group())]

if __name__ == '__main__':
    for stem in sys.argv[1:]:
        d = json.load(open(RECORDS + stem + '.json'))
        print('########', stem)
        for path, s in leaves(d):
            if hits(s):
                print('@', '/'.join(map(str, path)), '::', s)
