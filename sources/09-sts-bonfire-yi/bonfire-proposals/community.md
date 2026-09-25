# Community Kit Proposal

Status: archived proposal.

This page preserves the original Community Kit reference target used by the
worked examples. The maintained package reference lives in
[`docs/packages/std.md`](../../packages/std.md#community-kit), and the runnable
examples live in [`docs/examples`](../../examples/).

The proposal framed a small community operating system built from the Bonfire
substrate: held surfaces, lifecycle transitions, named helper spirits, and
private-by-default message spaces. The examples are the executable form of that
proposal.

## 5.2 Heron

Heron is the presence and roster spirit. It helps a community distinguish
`here`, `away`, and `not_joining` without making absence punitive.

See [`presence`](../../examples/presence/).

## 5.4 Fox

Fox is the repair and mediation spirit. It supports private repair queues and
release-oriented conflict handling without turning conflict into a leaderboard.

See [`repair-queue`](../../examples/repair-queue/).

## 5.5 Sage

Sage is the doorway and welcome spirit. It supports bounded entry, host and
arrival roles, and graduation from temporary welcome into durable membership.

See [`doorway`](../../examples/doorway/).

## 5.6 Owl

Owl is the ritual and cadence spirit. It supports recurring community practice
through lifecycle ticks rather than a separate scheduling substrate.

See [`ritual`](../../examples/ritual/).

## 8. Surfaces

The proposal's surfaces map to deployable `@bonfire/std/community` components:
Wishing Pool, Need Wall, Witness Book, Doorway, Repair Queue, Ritual, and
Presence/Roster.

## 9.1.1 Witness Book

Witness Book records moments as crystallized entries and mints witness holdings
for participants while preserving the source event.

See [`witness-book`](../../examples/witness-book/).

## 10. Entry And Exit

Doorway, welcome tokens, graduation, deactivation, release, composting, and
commemoration model entry and exit as explicit lifecycle transitions.

## 11. Anti-Patterns

The kit avoids public repair leaderboards, coercive presence tracking, erased
history, unbounded authority, and conflating a helper spirit's suggestion with
permission to act.

## 12.1 Small Coliving (12 People)

The coliving worked example composes the kit into one community: arrival,
wishes, needs, rituals, presence, repair, graduation, crystallization, release,
compost, and commemoration.

See [`coliving`](../../examples/coliving/).

## 14.0.4 Wave 4 Lessons

Repair queues demonstrated that private mediation and release transitions can
be expressed with ordinary holdings, sessions, and lifecycle state.

## 14.0.5 Wave 6 Lessons

Rituals demonstrated that recurring behavior is a composition pattern over
lifecycle ticks, not a new primitive.

## 14.0.6 Wave 7 Lessons

Presence closed the named-spirit set by treating absence as explicit
information while preserving caller-sensitive visibility.
