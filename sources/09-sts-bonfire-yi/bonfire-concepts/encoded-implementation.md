# Canonical contribution encoding

Portable Kind installation is byte-oriented. `facet.*`, `bindFacet.*`, family,
interface, and presentation builders validate their input and return deeply
frozen artifacts. `PortableKitInstallSourceV3` carries their canonical semantic
bytes with aliases and migrations.

The server decodes every contribution through its registered owning-context
codec, closes the complete family graph, compiles a deterministic logical
representation plan, and commits immutable Kind and binding revisions. A
semantic change changes revision identity; byte reordering or mutable runtime
metadata cannot.

No detached projection or runtime field-presence inference participates in
this path.

See [Kinds and facets](unified-class.md) and the
[kit author guide](../kit-author-guide.md).
