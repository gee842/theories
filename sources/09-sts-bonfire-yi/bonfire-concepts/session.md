# Sessions

A session is a product composition of explicit Kind facets. It is not a Yi
subtype and is not recognized from a discriminator or composed sentinel.

## Components

A typical session family declares:

- Identity principal coordinates for its address;
- a durable Streams contribution for content;
- Relations topology/policy for membership;
- Authority policy for protected operations;
- Views/interface surfaces for history, send, join, and presence.

The compiler records those contributions in a closed representation plan.
Runtime manifestation prepares every selected component and commits them in one
Occasion.

## Membership

One live Relations occurrence from the member endpoint to the session endpoint
gates history, writes, and watch delivery. Relations owns endpoints,
cardinality, and lifecycle. The same indexed predicate is used by the kernel
floor and product gates.

An open join policy allows an eligible caller to create its own membership
occurrence. Otherwise an invitation or installed workflow mediates admission.
There is no membership-by-history and no automatic admission on send.

Direct messages, channels, posts, and agent conversations differ in product
policy, not storage representation. Mutual pair sessions canonicalize the pair
and enforce one live occurrence under concurrent creation.

## Message DAG

Messages live in Streams and form a session-local DAG. Every message names its
parents and receives a monotonic session position. The session Kind declares
the durable stream and reply semantics; replies that also need a Relations
occurrence create both through one workflow and one Occasion.

Stream storage remains physically separate, but its append and exact Occasion
effect commit atomically with related Yi and context rows. History and watches
read indexed Occasion commits/effects and preserve commit order.

## Presence

Presence is ephemeral state governed by session policy. It is not durable
authored state and does not create membership. Expiry removes occupancy without
changing the durable relation. Durable sharing/suspension changes, when used,
commit through the owning context and Occasion coordinator.

Use product facades such as `client.chat` and `client.groups` rather than raw
Yi predicates. See [Messages](messages.md) and [Visibility](visibility.md).
