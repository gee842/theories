#!/bin/sh
# R46: scratch build of Becoming.Interleavings (passed steps reused from the shared cache) and the
# axiom report of each declaration it states. A working check, not the receipt.
# usage: sh scratch.sh BUILD_DIR
here=$(cd "$(dirname "$0")" && pwd)
python3 -B "$here/buildall.py" "$1" Becoming.Interleavings | tail -40
python3 -B "$here/axioms.py" "$1" Becoming.Interleavings | head -20
