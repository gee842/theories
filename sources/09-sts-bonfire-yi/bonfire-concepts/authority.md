# Authority

Authority answers who may perform an operation on a resource. Its durable
instrument is a certificate, not an authored-state field and not a Custody
asset shape.

## Certificates

Authority owns the complete certificate record:

- canonical certificate bytes;
- issuer, subject, and optional presenter coordinates;
- covered actions, ports, resources, and caveats;
- use count and maximum-use enforcement;
- issuer epoch, revocation state, and CAS revision.

Issue, present, consume, and revoke certificates through Authority operations.
Each change commits with its Yi root and all cross-facet effects in one
Domain-scoped Occasion. A revoked certificate or stale issuer epoch fails
closed at the same consistency frontier used by the server.

## Declaring authority

Kinds declare semantic Authority contributions with
`facet.authority.role(...)`, `facet.authority.policy(...)`, or
`facet.authority.gate(...)`. A port carries a runtime schema and gate, and
invocation resolves the exact handler artifact installed for that port.

When authority depends on another component, declare the relationship with a
typed `bindFacet.*` artifact. Common examples include:

- deriving the certificate subject from a Custody holder;
- activating authority only while a Relations occurrence is live;
- activating authority while a placeable child occupies a named Containment
  slot;
- applying Authority policy during Custody transfer or extinction.

The binding names both contributions, the execution class, and the deciding
owner. The compiler rejects missing contributions, incompatible owners, absent
endpoint or slot references, and ambiguous overlaps.

## Gates and execution

Every executable port has one schema/gate/authority envelope. Trusted process
handlers, installed workflows, sandbox handlers, and DSL handlers all enter
that envelope and the same Occasion transaction. There is no ambient handler
registry or caller-supplied authority substitution.

Gates may inspect context-owned facts and certificate evidence, but authored
display state is never sufficient authority. In particular:

- possession checks read the Custody holder index;
- membership and role checks read live Relations occurrences and reservations;
- equipped-authority checks read the child's current Containment placement;
- certificate decisions read Authority state and the applied Occasion
  frontier.

Denied operations return the shared Core `BonfireError` contract. SDK error
types extend that same identity.

## Lifecycle vocabulary

Use `certificate` for Authority instruments. Use `issue`, `present`, `consume`,
and `revoke` for certificate operations. Use `extinguish` for the public
Custody/Yi lifecycle. The word `claim` is reserved for Automation or Settlement
work dispatch, not authorization evidence.

See [Kinds and facets](unified-class.md), [Holdings](holdings.md), and the
[SDK delegation guide](../sdk/delegation.md).
