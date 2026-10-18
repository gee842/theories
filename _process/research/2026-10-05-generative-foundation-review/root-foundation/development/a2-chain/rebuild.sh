#!/bin/zsh
# A2: rebuild the landing on the current main, from the repository root of a fresh branch at main that holds this
# folder. Every edit is made by the scripts next to this one, in this order:
#   apply_chain_links.py  the chain's M15 and M26 links (data only)
#   apply_text.py         chapter section 8.4, the brief's item 19 and the maintenance record's entry
#   rehash_refs.py BASE   references that matched at BASE re-pointed to the files A2 changed, with a note
#   make research-render  the generated views
#   keep_views.py BASE    the Lean catalogue's pages put back at BASE, with their manifest entries
#   record_reading.py     fingerprints of the sources read, where unchanged since reading or changed only by A2's note
#   render_chain.py       GENERATIVITY-CHAIN.md from the data
# then the checks: research-check, research-links on the changed files, research-test. Before it, on the fresh
# branch: reread_at_landing.py BASE --show lists the sources A2 read that later landings changed; read each change,
# record what was read with --accept, and state it in index-entry.txt's sentence on the sources read again.
set -e
D=_process/research/2026-10-05-generative-foundation-review/root-foundation/development/a2-chain
BASE=$(git rev-parse HEAD)
python3 -B $D/apply_chain_links.py
python3 -B $D/apply_text.py
python3 -B $D/rehash_refs.py $BASE --dry || true  # the dry run prints its plan and exits 1
python3 -B $D/rehash_refs.py $BASE
make research-render
python3 -B $D/keep_views.py $BASE
python3 -B $D/record_reading.py $BASE
python3 -B $D/render_chain.py
make research-check
python3 -B tools/research/research.py links --paths $(git diff --name-only $BASE -- '*.md')
make research-test
echo "rebuilt on $BASE"
