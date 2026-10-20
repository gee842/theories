#!/usr/bin/env python3
"""R35: classify the worktree audit (worktrees.py output) into merged, unmerged and salvage-needed. Read-only.

merged          the branch head is an ancestor of main and the folder has no uncommitted entries: build output
                and registration may go once no session uses them.
merged-dirty    ancestor of main, but the folder holds uncommitted entries: look at them before removing anything.
unmerged        commits not on main whose every changed file main holds or has changed since (only_on_branch 0):
                the content was relanded or superseded; the commits still need a refs/salvage/ ref before the
                branch goes, since a commit is data until reachable.
salvage-needed  commits not on main with files only the branch holds (only_on_branch > 0): give the head a
                refs/salvage/ ref and ask the owner before anything else.
usage: python3 -B worktree_classes.py <worktrees.json> <out.tsv>"""
import json
import sys

rows = json.load(open(sys.argv[1]))
out = ['class\tworktree\tbranch\thead\tcommits_not_on_main\tonly_on_branch\tdirty_entries\tfolder_mtime']
count = {}
for r in rows:
    if r['branch'] == 'main':
        continue
    dirty = r['dirty_entries']
    if r['ancestor_of_main']:
        cls = 'merged' if dirty == 0 else 'merged-dirty'
    elif r.get('only_on_branch', 0) > 0:
        cls = 'salvage-needed'
    else:
        cls = 'unmerged'
    count[cls] = count.get(cls, 0) + 1
    out.append('\t'.join(str(x) for x in (cls, r['worktree'], r['branch'], r['head'],
                                           len(r.get('commits_not_on_main', [])), r.get('only_on_branch', 0), dirty,
                                           r['folder_mtime'])))
out.sort(key=lambda l: (l.split('\t')[0] != 'class', l))
open(sys.argv[2], 'w').write('\n'.join(out) + '\n')
print(count)
