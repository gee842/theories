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
