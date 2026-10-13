"""P58c: the rename map (namemap.json, read from the declarations) and an identifier-aware text rename.
A name with an underscore is renamed bare or qualified; a name without one (rests, quiet, stills) and
Conditions.drawdown_finite (Space's drawdown_finite is a different theorem) only qualified."""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAP = json.loads((HERE / 'namemap.json').read_text())
FULL = {o: n for _, o, n in MAP['renames']}
SHORT = {}
for o, n in FULL.items():
    so, sn = o.split('.')[-1], n.split('.')[-1]
    SHORT.setdefault(so, set()).add(sn)
NEED_QUAL = {'rests', 'quiet', 'stills', 'drawdown_finite'}
TOKEN = re.compile(r'(?<![\w.])((?:[A-Za-z]\w*\.)*)(' + '|'.join(sorted(map(re.escape, SHORT), key=len, reverse=True)) + r')(?![\w])')


def _sub(m):
    qual, short = m.group(1), m.group(2)
    q = qual[len('Becoming.'):] if qual.startswith('Becoming.') else qual
    if q:
        matches = {new.split('.')[-1] for old, new in FULL.items()
                   if old == q + short or old.endswith('.' + q + short)}
        if len(matches) == 1:
            return qual + next(iter(matches))
        return m.group(0)          # unrelated namespace or receiver; adapt known receiver calls explicitly
    if short in NEED_QUAL or len(SHORT[short]) != 1:
        return m.group(0)
    return qual + next(iter(SHORT[short]))


def rename(text):
    return TOKEN.sub(_sub, text)


def old_left(text):
    """Renamed names still present (qualified correctly or bare with an underscore)."""
    return [m.group(0) for m in TOKEN.finditer(text) if _sub(m) != m.group(0)]
