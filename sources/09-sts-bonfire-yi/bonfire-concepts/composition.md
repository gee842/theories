# Composition and reusable Kind families

`composes` declares semantic Kind/family references. It is useful for reusable
policy, schema, and interface law, but it never selects physical
representation.

Representation comes from `facet.*` contributions decoded by their owning
contexts. A composed reference must resolve to an installed family or a member
of the same closed install set; string sentinels are rejected at public
authoring ingress.

When a Kind combines several context contributions, use explicit
`bindFacet.*` declarations for their interactions. The compiler rejects
ambiguous overlap and records the deterministic result in the binding
revision.

See [Kinds and facets](unified-class.md).
