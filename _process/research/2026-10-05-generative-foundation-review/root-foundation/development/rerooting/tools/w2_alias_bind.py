"""W2: keep an alias elaborated only by a retired module bound to a receipt that elaborated it."""
import hashlib, json, subprocess, sys
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
for arg in sys.argv[1:]:
    rid, want = arg.split('=')
    f = f'theories/becoming/results/records/{rid}.json'
    d = json.load(open(f))
    old = json.loads(subprocess.run(['git', 'show', 'HEAD:' + f], capture_output=True, text=True).stdout)
    bound = {b['receipt'] for b in d['proof_bindings']}
    for alias in [want]:
        found = None
        for b in old['proof_bindings']:
            r = json.load(open(b['receipt']))
            for m in (r.get('modules') if isinstance(r.get('modules'), list) else []):
                if 'module' in m and any((x['name'] if isinstance(x, dict) else x) == alias for x in m['declarations']):
                    found = (b['receipt'], m['module'], r)
            if found:
                break
        if not found or found[0] in bound:
            continue
        receipt, module, r = found
        refs = [q for q in d['references'] if q['path'].endswith('/' + module.split('.')[-1] + '.lean')]
        assert len(refs) == 1, (rid, module, [q['path'] for q in refs])
        src = refs[0]['path']
        sha = hashlib.sha256(open(src, 'rb').read()).hexdigest()
        assert r['source_sha256'][module] == sha, (rid, module, 'bytes differ from the receipt')
        d['proof_bindings'].append({'source': src, 'receipt': receipt, 'sha256_pointer': '/source_sha256/' + module,
                                    'success_pointer': '/status', 'success_value': 'passed'})
        last = d['history'][-1]
        assert last['en'].startswith('19 October 2026, W2')
        name = src.rsplit('/', 1)[-1]
        last['en'] = last['en'][:-len(' The claim is unchanged.')] + (
            f' The alias {alias} is elaborated only in {module} ({name}, retired by the F3 sweep with its bytes kept), '
            f'so that file stays bound to receipt {receipt.split("/")[-2]}, whose hash of it matches.'
            ' The claim is unchanged.')
        print(rid, alias, module, receipt.split('/')[-2])
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
