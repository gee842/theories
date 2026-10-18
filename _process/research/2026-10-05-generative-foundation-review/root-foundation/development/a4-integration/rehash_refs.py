#!/usr/bin/env python3
"""A4 (19 October 2026): re-point record references to files the A4 landing changed, after reading the change, with a
history note naming each file. Run after apply_chapter.py and apply_records.py, before rendering.

(a) A reference that matched the file at BASE is re-pointed where the file changed.
(b) A reference already stale at BASE is re-pointed only where it drifts now and did not drift at BASE: every rewritten
    line that bears on the record (a line linking its page, or a line in a section it cites by anchor) is then A4's,
    and the rest of the file changed only outside what the record cites, which the registry treats as needing no new
    review. REVIEWED lists the records whose bearing lines A4 read for rule (b); --dry prints the computed set, and a
    computed set that differs from REVIEWED stops the script before anything is written.
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
# Filled at landing, after reading each record's bearing lines in the --dry output against the chapter diff.
REVIEWED = set()
WHAT = {
    'THE-THEORY-OF-BECOMING.md': 'A4 placed the readings in one account (DELEGATED-CHOICES D45): the legend; section '
                                 '2, the reading of where a level couples into a formation, adopted, and the '
                                 'conjecture on observation in its exact sense; section 3, the readings of 无明, 明, '
                                 '知足 and 知止; the labels and readings of sections 7.2 to 7.5 and the last line of '
                                 '7.7; section 8, its opening, the Origins row of 8.2, the decisions of 8.3, 8.4 (no '
                                 'reading open) and the review row of 8.8; the glossary rows on becoming, coming to '
                                 'rest (停息), enough, 无明, 明 and 识',
    'THE-THEORY-OF-BECOMING.zh.md': 'A4 placed the readings in one account, as in the English, and wrote the rest '
                                    'family as 停息 and becoming as 生成／变化 where bare 生成 meant it (D45 (4), (5))',
}
for rid in EDITED:
    WHAT[rid + '.json'] = 'A4 placed the record\'s readings in one account (D45); the claim is unchanged'


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


plan, found_b = [], {}
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
        elif p.endswith('.md'):
            now = bearing(d, p, r['sha256'], Path(p).read_text())
            if now and not bearing(d, p, r['sha256'], show(p).decode()):
                hits.append((r, p, 'b'))
                found_b[rid] = now
    if hits:
        plan.append((f, d, hits))
missing = sorted({p.rsplit('/', 1)[-1] for _, _, hits in plan for _, p, _ in hits} - set(WHAT))
if missing:
    sys.exit(f'no description for changed files: {missing}')
if '--dry' in sys.argv:
    for f, d, hits in plan:
        print(f.rsplit('/', 1)[-1], [(p.rsplit('/', 1)[-1], rule) for _, p, rule in hits])
    for rid, heads in sorted(found_b.items()):
        print('rule (b), read:', rid, heads)
    sys.exit(f'dry run: {len(plan)} records would be re-pointed, {len(found_b)} by rule (b)')
if set(found_b) != REVIEWED:
    sys.exit(f'rule (b) set differs from REVIEWED; read these first: new {sorted(set(found_b) - REVIEWED)}, '
             f'gone {sorted(REVIEWED - set(found_b))}')
for f, d, hits in plan:
    for r, p, _ in hits:
        r['sha256'] = h(p)
    names = sorted({p.rsplit('/', 1)[-1] for _, p, _ in hits})
    why = '; '.join(f'{x}: {WHAT[x]}' for x in names)
    stale = [p.rsplit('/', 1)[-1] for _, p, rule in hits if rule == 'b']
    extra = (f' {", ".join(stale)} was already older than the base; every line of it that bears on this record and '
             'changed since the record\'s review is A4\'s, and the rest changed only outside what the record cites.'
             if stale else '')
    d['history'].append({
        'en': f'19 October 2026, A4: {", ".join(names)} re-pointed after reading the change ({why}).{extra} The claim '
              'is unchanged.',
        'zh': f'2026年10月19日，A4：读过改动后，{"、".join(names)} 重新指向（诸读法在一个说明中定位，D45）。论断不变。'})
    open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(f.rsplit('/', 1)[-1], [(p.rsplit('/', 1)[-1], rule) for _, p, rule in hits])
print(len(plan), 'records re-pointed;', len(found_b), 'by rule (b)')
