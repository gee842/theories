import os
import json,re,sys
d=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'decls.json')))['decls']
pat=re.compile(sys.argv[1]); field=sys.argv[2] if len(sys.argv)>2 else 'name'
kinds=sys.argv[3].split(',') if len(sys.argv)>3 else None
for x in d:
    if pat.search(x[field]) and (not kinds or x['kind'] in kinds):
        t=' '.join(x['text'].split())[:230]
        print(f"{x['full']} | {x['kind']} | {x['module']}:{x['line']} | {t}")
