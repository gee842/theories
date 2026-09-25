# Lifecycle

Lifecycle is context-owned:

- Identity owns principal creation, reparenting, and extinction;
- Custody owns asset activation, transfer, and extinction;
- Containment owns placement and exclusive moves;
- Relations owns occurrence activation and extinction;
- Authority owns certificate issue, use, and revocation.

Every operation uses the Yi's compiled representation plan. Multi-component
writes acquire the Domain transaction and commit one Occasion; a veto, CAS
conflict, or constraint failure rolls the whole ceremony back.

Generic authored-state mutation cannot edit context lifecycle facts. Ports may
call the explicit context verbs exposed by their handler context, and every
port must carry a gate.

See [Yi](yi.md) and [Holdings](holdings.md).
