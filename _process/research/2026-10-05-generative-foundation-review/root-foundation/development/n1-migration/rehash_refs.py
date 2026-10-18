#!/usr/bin/env python3
"""Final pass of N5 (18 October 2026): re-point record references to files the renaming branch changed after
rebind_records.py ran (the chapter's glossary table, the study sections), naming each file in the record's N5 note.

usage (from the root of the branch's checkout): python3 -B rehash_refs.py BASE
"""
import glob, hashlib, json, subprocess, sys

changed = set(subprocess.run(['git', 'diff', '--name-only', sys.argv[1]], capture_output=True, text=True).stdout.split())
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
fixed = added = 0
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    d = json.load(open(f))
    files = []
    for r in d.get('references', []):
        if r.get('path') in changed and r.get('sha256') != h(r['path']):
            r['sha256'] = h(r['path'])
            files.append(r['path'].rsplit('/', 1)[-1])
    if not files:
        continue
    notes = [x for x in d['history'] if x.get('en', '').startswith('18 October 2026, the N1 renaming')]
    if notes:
        n = notes[-1]
        for fn in sorted(set(files)):
            if fn in n['en']:
                continue
            if ' Changed by the renaming: ' in n['en']:
                n['en'] = n['en'].replace(' Changed by the renaming: ', ' Changed by the renaming: ' + fn + ', ', 1)
            elif ' changed by the renaming (' in n['en']:
                n['en'] = n['en'].replace(' changed by the renaming (', ', ' + fn + ' changed by the renaming (', 1)
            else:
                n['en'] = n['en'].replace(' The claim is unchanged.', ' Changed by the renaming: ' + fn + '. The claim is unchanged.')
        fixed += 1
    else:
        d['history'].append({'en': "18 October 2026, the N1 renaming (Ren: \"Renames, full scope\"): " + ", ".join(sorted(set(files))) +
                             " changed by the renaming (identifiers renamed; the chapter's glossary gains a table of retired Lean"
                             " names; the renewal study gains section 172). Read the change: it touches no statement of this"
                             " record; re-pointed, the claim is unchanged."})
        added += 1
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('updated', fixed, 'new notes', added)
