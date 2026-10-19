"""R30: OPENING's body is in Ren's voice and changes only through a proposal; its footnotes are AI-written and
follow the current names. This renames by the table (text.py's rule) on the footnote lines only (lines beginning
`[^`), and lists any renamed name a body line carries (to be proposed, not renamed). Run from the checkout root."""
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('r30text', HERE / 'text.py')
text = importlib.util.module_from_spec(spec)
spec.loader.exec_module(text)
F = 'theories/becoming/OPENING.md'
lines = open(F, encoding='utf-8').read().split('\n')
changed, body = 0, []
for i, line in enumerate(lines):
    new = text.rewrite_text(line)
    if new == line:
        continue
    if line.startswith('[^'):
        lines[i] = new
        changed += 1
    else:
        body.append(i + 1)
open(F, 'w', encoding='utf-8').write('\n'.join(lines))
print('footnote lines changed', changed, '; body lines naming a renamed declaration', body)
