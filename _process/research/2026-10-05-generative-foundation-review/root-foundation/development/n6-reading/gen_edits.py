"""Write an edit file from (sense, old, new) replacements read off a module's current text.

gen(out, header, target, path, reps): replacements apply in order; each block's count is the
count at that point, so the edit file applies exactly as written (reading_pass.py apply checks
the counts again against the base).
"""
import subprocess

def base_text(path):
    base = subprocess.run(['git', 'merge-base', 'HEAD', 'main'], capture_output=True, text=True).stdout.strip()
    return subprocess.run(['git', 'show', base + ':' + path], capture_output=True, text=True, check=True).stdout

def gen(out, header, target, path, reps):
    src = base_text(path)
    lines = ['# ' + header, '### ' + target]
    for sense, a, b in reps:
        n = src.count(a)
        assert n >= 1, ('not found', a)
        src = src.replace(a, b)
        lines.append('= ' + sense + (' %d' % n if n > 1 else ''))
        lines += ['- ' + l if l else '-' for l in a.split('\n')]
        lines += ['+ ' + l if l else '+' for l in b.split('\n')]
    open(out, 'w').write('\n'.join(lines) + '\n')


def gen_records(out, header, recs):
    """recs = [(stem, [(sense, old, new), ...]), ...]: replacements in a record's live strings, in order,
    counted on the base record as they apply (reading_pass.py apply rechecks the counts)."""
    import json
    from reading_pass import RECORDS, count_live, live_strings
    lines = ['# ' + header]
    for stem, reps in recs:
        d = json.loads(base_text(RECORDS + stem + '.json'))
        lines.append('### record:' + stem)
        for sense, a, b in reps:
            if a.startswith('@'):
                # a field path, e.g. '@laws/3/en': the whole current string at that path is the old text,
                # replaced at that path only
                keys = [int(k) if k.isdigit() else k for k in a[1:].split('/')]
                x = d
                for k in keys[:-1]:
                    x = x[k]
                pth, a = '/'.join(map(str, keys)), x[keys[-1]]
                x[keys[-1]] = b
                lines.append('= ' + sense + ' @' + pth)
            else:
                n = count_live(d, a)
                assert n >= 1, (stem, 'not found', a)
                d = live_strings(d, lambda s: s.replace(a, b))
                lines.append('= ' + sense + (' %d' % n if n > 1 else ''))
            lines += ['- ' + l if l else '-' for l in a.split('\n')]
            lines += ['+ ' + l if l else '+' for l in b.split('\n')]
    open(out, 'w').write('\n'.join(lines) + '\n')
