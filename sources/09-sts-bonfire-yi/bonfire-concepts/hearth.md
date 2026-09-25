# Hearth

Hearth is Bonfire's reference small-community room. The `/hearth` product uses
first-party Kind families and the same public SDK/live server/PostgreSQL stack
required of other shipped products.

## Representation

A Hearth room is an Identity-bearing, Containment-owning conversation root.
Its content lives in the Streams context and its membership roster is a
Relations family with explicit member and room endpoints. Product reads use
the indexed room/message and Relations endpoint queries; the client does not
rebuild a roster by scanning Yi roots.

The room may contain first-party community tools such as the Witness Book,
Wishing Pool, Need Wall, and installed sigils. Each tool is its own Yi root
with the context components selected by its committed Kind binding revision.

## Invitations

`@bonfire.communities.hearth-invite:hearth-invite` is a directed Relations
occurrence from
the inviter to the invitee, paired with an Authority certificate whose use
policy is exactly once.

```ts
const invitation = await client.relations.create(HearthInvitation, {
  from: inviterUid,
  to: inviteeUid,
  state: { hearth: hearthUid },
})
```

Accepting an invitation is one installed workflow and one Occasion:

1. verify that the authenticated invitee may present the attached certificate;
2. consume its one permitted use;
3. create exactly one invitee-to-Hearth membership occurrence; and
4. extinguish the invitation.

Concurrent acceptance attempts produce one membership and one successful
certificate consumption. Declining or issuer revocation extinguishes the
invitation without creating membership. Any failed step rolls back the entire
Occasion.

## Equipped authority

Hearth tools that depend on equipped keys use Containment plus Authority. The
inventory or character is a declared container and the key is a placeable
child. A cross-facet binding activates the key's certificate only while the
child occupies the required slot. Moving or transferring the key, extinguishing
it, or advancing the issuer epoch makes the next Authority decision deny
immediately.

## Realtime and history

Messages and durable product changes are observed from indexed Occasion
effects. Watches preserve Occasion order and resume with an observation cursor.
Presence and typing are ephemeral Signals; they are live-only and are not
reconstructed as durable history.

The Hearth canary is release evidence only when it installs the actual Std
release and drives this behavior through the public remote SDK against a live
server and PostgreSQL. In-process compiler-shape tests do not certify the
product path.
