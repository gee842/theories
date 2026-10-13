#!/usr/bin/env python3
"""Apply the unchanged P84/P85 draft deltas at their real section and receipt stamps.
Usage: python3 -B record_delta.py W FIRST_SECTION
"""
import json
from pathlib import Path
import subprocess
import sys

W = Path(sys.argv[1]).resolve()
S = int(sys.argv[2])
DEV = W / '_process/research/2026-10-05-generative-foundation-review/root-foundation/development'
RECEIPT = W / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/becoming-verification.json'
r = json.loads(RECEIPT.read_text())
assert r['status'] == 'passed'
assert any(m['module'] == 'Becoming.Succession' for m in r['modules'])
subprocess.run([sys.executable, '-B', str(DEV/'becoming-p84-landing/docs/records/record_delta.py'), str(W), str(S + 4)], check=True)
subprocess.run([sys.executable, '-B', str(DEV/'becoming-p85-landing/docs/records/record_delta.py'), str(W), r['utc'], str(S + 5)], check=True)
