# Visibility

Visibility answers which parts of a Yi, message, or projection a caller may
read. It is enforced by the owning context and the selected Kind's declared
gate policy; it is not inferred from optional authored fields.

## Yi reads

A public Yi read joins only the components the caller may observe:

- Kinds supplies the stable root, binding membership, and authored state;
- Identity supplies principal coordinates;
- Custody supplies holding facts;
- Containment supplies placement facts;
- Relations supplies occurrences and endpoints;
- Authority supplies permitted certificate facts.

Typed `contexts.*` accessors preserve absence. SDK readers must not fabricate
default holder, endpoint, issuer, placement, or lifecycle values.

## Declaring visibility

Put discovery policy on the Kind and authorization policy on each port. Use
Relations policy for endpoint visibility and Authority coverage for protected
operations. Cross-context visibility dependencies require an explicit
`bindFacet.*` contribution; field presence never creates membership or access.

Sessions use one live Relations membership predicate for history reads,
writes, and watch delivery. Direct messages, channels, and posts differ in
product policy, not in their membership representation. Extinguished
principals and occurrences cannot confer visibility.

## Indexed evaluation

Visibility checks use context-owned indexes for Identity paths, Custody
holders, Containment placements, Relations endpoints, Authority subjects and
issuers, and Kind bindings. List and watch operations apply filtering on the
server, preserve Occasion order, and evaluate event-time state. Product code
does not scan Yi roots, sort after pagination, or hydrate one binding catalog
entry per row.

The absence of a readable result does not reveal whether an invisible object
exists. A denied action returns `BonfireError('PermissionDenied', ...)`; a
filtered read returns the product operation's normal empty/not-found shape.

Sigils receive no special bypass. Their host calls the same typed transport and
the same gate/Authority envelope as other clients.
