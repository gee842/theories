# Community

A community is a first-party product composition, not a special Yi storage
shape. Its Kind families combine Identity, Streams, Relations, Authority,
Containment, Views, and other context contributions as needed.

## Core model

- Identity gives the community its canonical public principal path.
- Streams stores channels, posts, replies, and other high-volume content.
- Relations stores membership, subscriptions, friendships, replies, votes,
  and role affiliations as normalized occurrences.
- Authority certificates and policies decide moderation, hierarchy, sanctions,
  and installation rights.
- Containment stores ordered tabs, inventories, equipment, and other true
  parent/child placements.
- Views declares the public interface and presentation surfaces.

Every family is authored with `defineKind` and explicit family genesis from
`defineKindFamily`. Relations topology and policy are `facet.relations.*`
contributions on those Kinds; there is no separate relation declaration role.
Installed declarations compile to immutable binding revisions and closed
representation plans rather than ordinary Yi rows.

## Membership and roles

Membership is a directed Relations occurrence from the member to the
community. Relations owns the endpoints, active/extinguished lifecycle, and
one-live-occurrence-per-pair rule. Join time or a product label may be authored
state, but endpoint and lifecycle facts may not be duplicated there.

A role combines a live affiliation with an Authority contribution. Bind the
Authority subject to the member endpoint and its activation to the live
Relations occurrence. Revocation, sanctions, and issuer epochs remain
Authority facts. Tier ordering is expressed by distinct compile-time families
or revisions with explicit hierarchy, not a contradictory mutable priority
field.

The same indexed membership predicate gates session history, writes, and live
delivery. There is no membership-by-history or automatic promotion on send.

## Channels, posts, replies, and votes

Channels and posts use Streams for content and Relations for product topology.
A reply workflow creates its relation occurrence and stream content in one
Occasion, so no endpoint can outlive missing content and no content can lose
its occurrence.

Votes use a per-voter/proposal Relations reservation. The reservation and vote
occurrence commit atomically, enforcing one live vote under concurrent
requests. Counts and ordering use context-owned indexed queries; products do
not scan Yi roots, sort after pagination, or maintain authored-state counters.

Mutual friendship canonicalizes its endpoint pair and enforces one live
occurrence per pair, including concurrent creation from opposite directions.

## Invitations

An invitation combines a directed Relations occurrence with a one-use
Authority certificate. The relation runs from inviter to invitee. Acceptance
atomically consumes the certificate, creates exactly one membership, and
extinguishes the invitation. Concurrent acceptance admits one winner and
leaves no partial state.

## Installation and portability

Community Kits install through the normal package/workflow path and the same
Authority envelope as other operations. `PortableKitInstallSourceV3` carries
family genesis, contribution bytes, exact surfaces, aliases, handlers, views,
workflows, migrations, and expected-source inventory together.

Export policy is operation-owned metadata declared with
`portable.familyPolicy(kind, policy)`. It is stored with package-installation
provenance and does not participate in a Kind's semantic contributions or
representation plan.

## Transactions and reads

Founding, installation, replies, votes, invitations, and multi-component
manifestation use the Domain-scoped Occasion coordinator. One transaction
materializes all required owner rows, records exact effects, advances affected
Yi roots to the actual commit id, and commits once.

List surfaces use cursor pagination and context-owned indexes for membership,
forum order, role revocation, placement, and Kind binding. Watches preserve
Occasion order and evaluate event-time state on the server.

See the [SDK quickstart](../sdk/quickstart.md), [Relationships](relationships.md),
[Authority](authority.md), and the [kit author guide](../kit-author-guide.md).
