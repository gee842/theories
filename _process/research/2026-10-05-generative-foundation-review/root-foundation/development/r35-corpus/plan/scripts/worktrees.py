#!/usr/bin/env python3
"""Read-only worktree audit for R35 (E12). Run from the repository root.

For each worktree: HEAD, branch, ancestor of main?, commits not on main, and for those whether
their content is on main: (a) `git cherry` patch-id equivalence per commit, (b) per file the
branch changed since the merge base: does main hold the same blob ('same'), has main changed the
file since the merge base ('main-changed', i.e. relanded or superseded with edits), or is the
branch's version absent from main ('only-branch'). Also: uncommitted changes (git status) and
last modification time of the worktree folder. No command writes.
"""
import json, os, subprocess, sys, time

OUT = sys.argv[1]


def git(*a, cwd=None):
    r = subprocess.run(['git', *a], capture_output=True, text=True, cwd=cwd, env={**os.environ, 'GIT_OPTIONAL_LOCKS': '0'})
    return r.stdout.strip(), r.returncode


main, _ = git('rev-parse', 'main')
rows = []
raw, _ = git('worktree', 'list', '--porcelain')
wts, cur = [], {}
for line in raw.splitlines() + ['']:
    if not line:
        if cur:
            wts.append(cur)
        cur = {}
        continue
    k, _, v = line.partition(' ')
    cur[k] = v or True
for w in wts:
    path, head = w['worktree'], w.get('HEAD', '')
    if path == os.getcwd():
        continue
    branch = w.get('branch', 'detached').replace('refs/heads/', '')
    _, rc = git('merge-base', '--is-ancestor', head, 'main')
    anc = rc == 0
    info = {'worktree': os.path.relpath(path), 'head': head[:9], 'branch': branch, 'locked': 'locked' in w,
            'ancestor_of_main': anc}
    st, _ = git('status', '--porcelain', '--untracked-files=normal', cwd=path) if os.path.isdir(path) else ('MISSING', 1)
    info['dirty_entries'] = len([l for l in st.splitlines() if l]) if st != 'MISSING' else 'folder missing'
    info['dirty_sample'] = st.splitlines()[:4] if st != 'MISSING' else []
    try:
        info['folder_mtime'] = time.strftime('%Y-%m-%d %H:%M', time.localtime(os.stat(path).st_mtime))
    except OSError:
        info['folder_mtime'] = None
    if not anc:
        base, _ = git('merge-base', head, 'main')
        commits, _ = git('log', '--format=%h %cs %s', f'main..{head}')
        info['merge_base'] = base[:9]
        info['commits_not_on_main'] = [c[:160] for c in commits.splitlines()]
        cherry, _ = git('cherry', 'main', head)
        info['cherry'] = {'equivalent_on_main(-)': cherry.count('\n-') + cherry.startswith('-'),
                          'not_on_main(+)': cherry.count('\n+') + cherry.startswith('+')}
        files, _ = git('diff', '--name-only', base, head)
        same = main_changed = only_branch = deleted = 0
        detail = []
        for f in files.splitlines():
            bh, rb = git('rev-parse', f'{head}:{f}')
            mh, rm = git('rev-parse', f'main:{f}')
            if rb != 0:
                deleted += 1
                kind = 'deleted-on-branch' + ('' if rm == 0 else ' (also gone on main)')
            elif rm == 0 and bh == mh:
                same += 1
                kind = 'same'
            else:
                changed, _ = git('diff', '--quiet', base, 'main', '--', f)
                _, rcc = git('diff', '--quiet', base, 'main', '--', f)
                if rcc != 0:
                    main_changed += 1
                    kind = 'main-changed-since-base'
                else:
                    only_branch += 1
                    kind = 'only-branch'
            if kind != 'same':
                detail.append(f'{kind}: {f}')
        info['files_changed_on_branch'] = len(files.splitlines())
        info['same_blob_on_main'] = same
        info['main_changed_since_base'] = main_changed
        info['only_on_branch'] = only_branch
        info['deleted_on_branch'] = deleted
        info['detail_sample'] = detail[:25]
    rows.append(info)
json.dump(rows, open(OUT, 'w'), indent=1, ensure_ascii=False)
for r in rows:
    print(r['worktree'], r['head'], r['branch'], 'ANC' if r['ancestor_of_main'] else 'NOT', r.get('cherry', ''),
          'same=%s mainchg=%s only=%s' % (r.get('same_blob_on_main'), r.get('main_changed_since_base'), r.get('only_on_branch')),
          'dirty=%s' % r['dirty_entries'], r['folder_mtime'])
