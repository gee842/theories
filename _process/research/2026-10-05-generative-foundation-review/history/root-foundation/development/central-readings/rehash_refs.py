#!/usr/bin/env python3
"""A1 (18 October 2026): re-point record references to files the A1 landing changed, after reading the change, with a
history note naming each file.

(a) A reference that matched the file at BASE is re-pointed where the file changed.
(b) A reference already stale at BASE is re-pointed only where it drifts now and did not drift at BASE: every rewritten
    line that bears on the record (a line linking its page, or a line in a section it cites by anchor) is then A1's,
    and the rest of the file changed only outside what the record cites, which the registry treats as needing no new
    review. A1 read those lines for each record in REVIEWED: the chapter's labels and readings for the records A1
    edited, the section 8.2 row "One relational start", the situations note of section 3 and the list of open readings
    in section 8.4. A computed set that differs from REVIEWED stops the script before anything is written.
Any other stale reference is left as it was, as is drift that predates BASE. A changed file that no entry of WHAT
describes also stops the script. usage (from the repository root): python3 -B rehash_refs.py BASE [--dry]
(--dry prints the plan and writes nothing)"""
import difflib, glob, hashlib, json, subprocess, sys
from pathlib import Path

sys.path.insert(0, '.')
from tools.research import registry  # noqa: E402
from tools.research.reading_catalogue import anchors_from_text  # noqa: E402

BASE = sys.argv[1]
changed = set(subprocess.run(['git', 'diff', '--name-only', BASE], capture_output=True, text=True).stdout.split())
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
show = lambda p: subprocess.run(['git', 'show', BASE + ':' + p], capture_output=True).stdout
BASE_SHA = {p: hashlib.sha256(show(p)).hexdigest() for p in changed}
EDITED = {f.rsplit('/', 1)[-1][:-len('.json')] for f in changed
          if f.startswith('theories/becoming/results/records/') and f.endswith('.json')}
REVIEWED = {
    # records A1 edited: the chapter lines that bear on them are the labels and readings A1 changed for them
    'counting-where-the-counts-exist', 'how-a-carried-difference-grows', 'how-much-difference-arrives',
    'how-often-couplings-act', 'lifting-where-branching-is-finite', 'observation-is-a-route',
    'the-step-index-from-own-courses', 'unity-of-readings', 'what-a-cut-loses',
    'what-a-law-of-the-whole-and-no-part-takes', 'where-a-run-goes-on', 'where-novelty-gain-comes-from',
    'whole-first-and-bounded-centers',
    # records linked from the section 8.2 row "One relational start", where A1 replaced only the sentence on the run
    'configurations-alike-by-relation', 'imbalance-as-relatum', 'premises-read-off-the-exchange',
    'process-and-frame-as-readings', 'returning-novelty-forgetting-on-levels', 'where-a-move-is-formed',
    # the situations note of section 3 (the by-construction sentence the record already states)
    'weights-count-situations',
    # the list of open readings in section 8.4 (its entry quotes the record's open reading)
    'where-a-level-couples',
}
WHAT = {
    'DELEGATED-CHOICES.md': 'A1 revised D1, D5, D22 and D39, each keeping its original text under a dated revision, and '
                            'added D43, the other readings Ren took on 18 October, with their index rows',
    'DELEGATED-CHOICES.zh.md': 'A1 revised D1, D5, D22 and D39 and added D43, as in the English',
    'THE-THEORY-OF-BECOMING.md': 'A1 applied the readings Ren took on 18 October, the revised readings of 生生, 生生不息 '
                                 'and "entangled" and the brief\'s Part B: the legend and item 11 of the statement in '
                                 'full, the premise card\'s row on the readings of `living`, labels and reading '
                                 'paragraphs in sections 1, 2, 3 and 6, the section 8.2 row on the relational start, '
                                 'sections 8.3 and 8.4, and the glossary and crosswalk rows; section 8.4 lists the '
                                 'open readings, with M1\'s line for section 7',
    'THE-THEORY-OF-BECOMING.zh.md': 'A1 applied the readings Ren took on 18 October; section 8 gained a list of open '
                                    'readings, and five of its block headings their closing bold marker',
}
for rid in EDITED:
    WHAT[rid + '.json'] = 'A1 applied the reading Ren took on 18 October; the claim is unchanged'


def bearing(record, path, sha, text):
    """The registry's scoped drift (registry.scoped_drift) of `text` against the reviewed version `sha`."""
    old = registry.reviewed_version(path, sha)
    if old is None:
        return ['(reviewed version not in history)']
    a, b = old.splitlines(), text.splitlines()
    heads = registry.sections(a)
    changes = [(heads[i1], a[i1:i2], b[j1:j2]) for op, i1, i2, j1, j2
               in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes() if op in ('replace', 'delete')]
    anchors = registry.cited_headings(record, path)
    located = bool(anchors) or registry.links_record(record, text)
    return sorted({hd or '(before the first heading)' for hd, rm, ad in changes
                   if not located or hd is None or registry.links_record(record, '\n'.join(rm + ad))
                   or anchors & anchors_from_text(hd)})


plan, found_b = [], set()
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    rid = f.rsplit('/', 1)[-1][:-len('.json')]
    hits = []
    for r in d.get('references', []):
        p = r.get('path')
        if p not in changed or r.get('sha256') == h(p):
            continue
        if r.get('sha256') == BASE_SHA[p]:
            hits.append((r, p, 'a'))
        elif p.endswith('.md') and bearing(d, p, r['sha256'], Path(p).read_text()) \
                and not bearing(d, p, r['sha256'], show(p).decode()):
            hits.append((r, p, 'b'))
            found_b.add(rid)
    if hits:
        plan.append((f, d, hits))
if found_b != REVIEWED:
    sys.exit(f'rule (b) set differs from REVIEWED; read these first: new {sorted(found_b - REVIEWED)}, '
             f'gone {sorted(REVIEWED - found_b)}')
missing = sorted({p.rsplit('/', 1)[-1] for _, _, hits in plan for _, p, _ in hits} - set(WHAT))
if missing:
    sys.exit(f'no description for changed files: {missing}')
if '--dry' in sys.argv:
    for f, d, hits in plan:
        print(f.rsplit('/', 1)[-1], [(p.rsplit('/', 1)[-1], rule) for _, p, rule in hits])
    sys.exit(f'dry run: {len(plan)} records would be re-pointed, {len(found_b)} by rule (b)')
for f, d, hits in plan:
    for r, p, _ in hits:
        r['sha256'] = h(p)
    names = sorted({p.rsplit('/', 1)[-1] for _, p, _ in hits})
    why = '; '.join(f'{x}: {WHAT[x]}' for x in names)
    stale = [p.rsplit('/', 1)[-1] for _, p, rule in hits if rule == 'b']
    extra = (f' {", ".join(stale)} was already older than the base; every line of it that bears on this record and '
             'changed since the record\'s review is A1\'s, and the rest changed only outside what the record cites.'
             if stale else '')
    d['history'].append({
        'en': f'18 October 2026, A1: {", ".join(names)} re-pointed after reading the change ({why}).{extra} The claim '
              'is unchanged.',
        'zh': f'2026年10月18日，A1：读过改动后，{"、".join(names)} 重新指向。论断不变。'})
    open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(f.rsplit('/', 1)[-1], [(p.rsplit('/', 1)[-1], rule) for _, p, rule in hits])
print(len(plan), 'records re-pointed;', len(found_b), 'by rule (b)')
