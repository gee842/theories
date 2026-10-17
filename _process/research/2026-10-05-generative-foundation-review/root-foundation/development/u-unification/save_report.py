"""Save an agent's final message as BATCH/REPORT.md (the harness keeps subagents from writing report files)."""
import json, sys
out, batch, marker = sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None
lines = [json.loads(l) for l in open(out) if l.strip().startswith('{')]
txt = None
for x in reversed(lines):
    m = x.get('message', {})
    if m.get('role') == 'assistant' and isinstance(m.get('content'), list):
        s = ''.join(b.get('text', '') for b in m['content'] if b.get('type') == 'text')
        if s.strip():
            txt = s; break
if marker and marker in txt:
    txt = txt[txt.index(marker):]
open(f'{batch}/REPORT.md', 'w').write(f'# Batch {batch} report (agent, 17 October 2026)\n\nSaved by the integrator from the agent\'s final message.\n\n' + txt.strip() + '\n')
print(batch, len(txt))
