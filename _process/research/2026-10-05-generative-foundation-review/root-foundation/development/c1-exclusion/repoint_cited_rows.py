#!/usr/bin/env python3
"""L2 and C1, 18 October 2026: after joint_landing.py rehash, research-check reported source drift for eight records
whose chapter reference was already stale at HEAD (hashed at 77dc88103 or bd5252f96) and which are cited from the two
section 8.2 rows the landing edits ("Continuation (§6.7) and feeding", "Learning"). The citing lines were read: in each
case the only changed citing line is the row C1 or L2 edited. Run once (already applied); kept for provenance.
usage (from the repository root): python3 -B repoint_cited_rows.py"""
import json, hashlib
CH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
h = hashlib.sha256(open(CH, 'rb').read()).hexdigest()
C = ('the section 8.2 row "Continuation (§6.7) and feeding" that cites it now reads C1\'s result (how taking all that is '
     'given forms, ending another serving taking all that is given, forced endings in the witnesses of §6.7, a comparison '
     'that registers an ending through exclusion) and links what-taking-all-excludes', '引用它的第 8.2 节“延续（§6.7）与供给”一行现读 C1 的结果')
L = ('the section 8.2 row "Learning" that cites it now names Becoming.Labels (a table found rather than given, and whether '
     'fewer names suffice, stay open)', '引用它的第 8.2 节“学习”一行现指 Becoming.Labels')
ITEMS = {'closure-verdict-meets-axiom': ('77dc88103', C), 'consumption-ends-with-feeders': ('77dc88103', C),
         'feeding-closure': ('77dc88103', C), 'presupposition-scopes': ('77dc88103', C),
         'what-an-extrapolation-given-nothing-fixes': ('bd5252f96', L), 'generalization-through-lumping': ('bd5252f96', L),
         'learnable-through-registration': ('bd5252f96', L), 'learning-by-refutation': ('bd5252f96', L)}
# (closure-verdict-meets-axiom and what-an-extrapolation-given-nothing-fixes were re-pointed first, with notes worded as
# above except that the latter's also names the D40 reading extended with L2.)
for rid, (rev, (en, zh)) in ITEMS.items():
    f = f'theories/becoming/results/records/{rid}.json'
    d = json.load(open(f))
    n = 0
    for r in d['references']:
        if r['path'] == CH and r.get('sha256') != h:
            r['sha256'] = h
            n += 1
    assert n == 1, (rid, n)
    d['history'].append({
        'en': f'18 October 2026, L2 and C1 (Becoming.Labels, Becoming.Exclusion): THE-THEORY-OF-BECOMING.md re-pointed after '
              f'reading the change since {rev} ({en}). The claim is unchanged.',
        'zh': f'2026年10月18日，L2 与 C1（Becoming.Labels、Becoming.Exclusion）：读过自 {rev} 以来的改动后（{zh}），'
              f'THE-THEORY-OF-BECOMING.md 重新指向。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
