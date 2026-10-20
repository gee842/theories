#!/bin/sh
# W2: apply the planned moves to the Becoming package at PACKAGE.
# usage: w2_apply.sh PACKAGE MOVE_PLAN RANGES IMPORT_PLAN
set -e
T=$(cd "$(dirname "$0")" && pwd)
python3 "$T/move_decls.py" "$1" "$2" "$3"
python3 "$T/apply_imports.py" "$1" "$4"
python3 "$T/tidy_scopes.py" "$1" $(python3 -c "
import json, sys
p, q = json.load(open(sys.argv[1])), json.load(open(sys.argv[2]))
print(' '.join(sorted({x for v in p['moves'].values() for x in v} | set(q['lost_labelled_process']))))" "$2" "$4")
python3 "$T/w2_notes.py" "$1"
python3 "$T/w2_register.py" "$1"
