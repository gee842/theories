#!/bin/zsh
# A3: rebuild the landing on the current main, from the repository root of a branch at main that holds this folder
# and the proposal page. Before it: reread_at_landing.py BASE --show lists the sources A3 read that later landings
# changed; read each change and record it with --accept; if RESULTS.md or GOALS.md changed, read them again and update
# their sha256 under `newly_linked` in reading.json. Then, in this order:
#   apply_entries.py DATE   the entry revisions and the two re-pointed links (chain data only)
#   record_reading.py       fingerprints of the sources read, where the file is still the version read
#   apply_text.py           the maintenance record's entry (pass --reread-zh/--reread-en when sources were read again)
#   make research-render    the generated views
#   generative_chain.py --render
# then the checks: generative_chain.py --check, research-check, research-links on the changed .md files, research-test.
set -e
D=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/a3-chain
BASE=$(git rev-parse HEAD)
python3 -B $D/apply_entries.py 2026-10-19
python3 -B $D/record_reading.py
python3 -B $D/apply_text.py "$@"
make research-render
python3 -B tools/research/generative_chain.py --render
python3 -B tools/research/generative_chain.py --check
make research-check
python3 -B tools/research/research.py links --paths $(git diff --name-only $BASE -- '*.md') \
  _process/research/2026-10-05-generative-foundation-review/root-foundation/CHAIN-RELABELLING-PENDING-REN.md
make research-test
echo "rebuilt on $BASE"
