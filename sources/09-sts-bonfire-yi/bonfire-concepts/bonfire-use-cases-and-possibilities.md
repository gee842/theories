# What Bonfire Makes Possible

Bonfire is a substrate for building persistent social worlds: communities,
economies, games, organizations, agent systems, and collaborative spaces whose
identity, authority, history, and possessions matter beyond one screen or one
host.

It is not primarily a collection of product features. Its value comes from
making several difficult semantic systems compose without assigning all of
their meaning to one application-specific database row or service.

A person, item, relationship, credential, message anchor, room, treasury, or
agent can have one stable Yi UID while participating in several bounded
contexts. Custody decides who holds an asset. Containment decides where
something is placed. Relations decide how two participants are connected.
Authority decides which actions are justified. Occasion preserves committed
history. Settlement coordinates work that crosses Domain boundaries. Views
serve declared product reads. Packages and Handlers carry exact computation
and consent. Portability gives people and worlds an exit artifact.

That combination makes Bonfire especially useful when a product involves
ownership, placement, revocable power, durable history, constrained
automation, governance, conserved exchange, or migration between hosts.

This document explores concrete applications and longer-term possibilities.
It deliberately distinguishes architectural possibilities from claims that a
finished product already ships. Current implementation status remains in the
[structural-arc handoff](../yi/49-structural-arc/HANDOFF.md).

## The central leverage: one thing, several truths

Consider a sword in a persistent game. It can simultaneously be:

- a conserved asset held by a player;
- a child placed in a backpack;
- an object equipped in a hand slot;
- the source of permission to perform a particular attack;
- an endpoint in a trade or loan relation;
- part of a cross-Domain escrow transaction;
- an item listed in inventory, equipment, market, and audit Views; and
- a stable object with a recoverable Occasion history.

Those facts overlap, but they are not interchangeable. Moving the sword out of
the equipped slot should affect its conferred authority without changing its
owner. Transferring it should conserve the asset, remove the old holder's
standing, and make retries safe. Listing it should not redefine ownership.
Destroying it should affect every active representation exactly once.

In a conventional application, these rules tend to accumulate in a central
item service, a large transaction script, or a collection of loosely
synchronized event handlers. Bonfire instead gives each context ownership of
its law and compiles the declared overlaps into a closed execution and
representation plan.

The same pattern applies far beyond games:

| Thing | Custody | Containment | Relations | Authority | Durable behavior |
|---|---|---|---|---|---|
| House key | current holder | equipped keyring or lockbox | issued-to resident | opens named doors | loss, transfer, and revocation |
| Membership badge | member-held credential | active wallet or profile slot | membership occurrence | accesses member operations | expiry and cancellation |
| Agent token | controlled capability object | installed agent workspace | delegation chain | invokes limited ports | use count and revocation |
| Event ticket | attendee holding | admitted zone | attendee/event relation | permits entry | one-use extinction |
| Treasury approval | governed instrument | proposal or budget scope | voter/proposal relation | authorizes a payment | quorum and deadline |
| Research artifact | stewarded object | collection or project | citation and authorship | controls publication | revision and provenance |

## Recurring capabilities

### Semantic composition without a god object

Product nouns can participate in multiple contexts while each fact retains one
owner. This makes complex overlap explicit and testable instead of relying on
conventions between unrelated columns and background jobs.

### Explainable, revocable authority

Authority is evidence, not a boolean attached to an account. A decision can
state which intrinsic standing, certificate, role, possession, placement,
relationship, issuer epoch, or causal frontier justified an action. The same
model can express expiry, attenuation, presenter restrictions, use limits, and
revocation.

### Durable behavior rather than database snapshots

Occasion, checkpoints, and consumer positions make recovery part of the
architecture. The aim is not merely to reconstruct rows, but to preserve the
committed meaning observed by Views, automation, authority, and product reads.

### Reliable work across boundaries

Domains define logical atomicity and isolation. Settlement makes work crossing
those boundaries explicit, retryable, compensatable, and visible as pending,
completed, or failed. Bonfire does not pretend that every distributed action
is one local transaction.

### Constrained computation

Handlers and installed workflows execute with declared identities, artifacts,
capabilities, resources, and consent. An application does not need to hand an
agent, bot, plugin, or package ambient access to the runtime.

### Sovereignty and exit

Portable bundles can carry a signed, normalized graph, retained history,
identity mapping, Kind families, exact artifacts, license decisions, and
certificate provenance. Foreign authority remains evidence; the destination
reissues active local authority under its own policy.

### Logical identity independent of topology

A Domain can move between physical shards without changing the logical IDs
visible to products. The SDK does not need to know which database currently
serves a community, channel, zone, or organization.

## Community and social products

### 1. A sovereign community operating system

A community can combine membership, roles, discussion, directories, events,
shared objects, working groups, moderation, and treasury activity without
making one platform account table the owner of all community truth.

Membership can remain a Relation. Moderator or steward power can remain an
Authority certificate. A sanction can be an explicit Gate fact rather than a
destructive edit to membership history. Channels and groups can occupy their
own Domains. Directories and feeds can be declared Views. Community-specific
automation can run through installed Handlers.

If the operator becomes unsuitable, the community can approve a governed
world export. Kind policy, member consent, private-row redaction, artifact
licenses, identity mapping, and destination Authority reissue remain separate
decisions. This creates meaningful operator competition: hosting can be a
service without becoming ownership of the community's ontology.

### 2. Creator and fandom worlds

A creator community might contain public channels, paid circles, live events,
collectibles, contribution badges, moderation teams, commissions, and shared
archives.

Payment or possession can confer scoped access without being confused with
social membership. A collectible may be transferable while a contribution
credential remains non-transferable. A backstage pass can expire after an
event. A moderator role can be revoked without touching purchased holdings.
Members can export their own identities and portable holdings, while migration
of the complete world remains a governed ceremony.

### 3. Forum networks with local constitutional differences

Reddit-like communities can model subscriptions and votes as Relations,
moderation as Authority, posts and replies as streams plus relation
occurrences, and ranked listings as named Views with explicit pagination.

Each community can install a different moderation or ranking package while
the product surface remains structurally consistent. A federation of such
communities does not need one universal moderator hierarchy: remote proofs can
be evaluated or reissued according to local policy.

### 4. Chat and collaboration spaces

Discord-like servers can use channel Domains, message streams, ordered role
templates, local overrides, bot Handlers, and Signals for typing, voice, or
presence.

Durable membership and messages remain distinct from ephemeral activity.
Revoking a bot certificate can stop future privileged work without deleting
the bot's historical messages. A hot channel can be moved or isolated
physically without exposing storage topology to clients.

### 5. Private groups and family spaces

A family, care circle, or private club needs more than a public-feed product
with an `is_private` flag. It may need invitation use limits, nested groups,
guardianship, private archives, shared assets, emergency delegates, and clear
rules for who may export which records.

Bonfire can distinguish group governance from subject consent. A world vote
cannot silently broaden the inclusion of a member's private rows. An
invitation can be a one-use Authority instrument whose successful use
extinguishes it.

### 6. Member-owned professional networks

A professional association can combine membership, committees,
qualifications, referrals, publications, elections, and continuing education.
Qualifications are certificates issued by recognized authorities;
participation is a Relation; committee powers are scoped and expiring
Authority; publications are stable artifacts; and member data remains subject
to portable policy and consent.

## Games and persistent simulations

### 7. MMORPG economies

MMORPGs are an unusually complete stress test because the same objects cross
almost every context:

- currency must conserve units;
- items must not duplicate under retry or failure;
- containers enforce capacity, order, and equipment slots;
- equipped items can confer abilities or access;
- guild roles and sanctions affect Authority;
- zones and guild buckets create Domain boundaries;
- auctions and trades require Settlement and escrow;
- cooldowns and deadlines require durable automation;
- position and nearby presence may remain ephemeral Signals.

Bonfire can represent these as interacting laws instead of a monolithic game
state machine. That makes it possible for distinct packages to define item
families, guild constitutions, crafting systems, or trade protocols while
still sharing conservation and authority guarantees.

### 8. Player-run realms

A game can allow communities to operate their own towns, guilds, markets, or
realms. Realm governance controls local packages and policies. Players retain
portable identity and eligible holdings. A realm can move to another host or
fork with explicit lineage instead of beginning as an unrelated copy.

This supports a spectrum between one official world and completely separate
private servers. Federation remains visible and eventual: two realms may
recognize selected credentials or assets without pretending to share one
atomic database.

### 9. Mod and extension ecosystems

A mod can declare new Kinds, facets, Views, Handlers, migrations, and requested
capabilities. Installation produces an exact lock and stored consent rather
than loading arbitrary process code because a package name matched.

Content-addressed artifacts and versioned family lineage make it possible to
reason about which implementation interpreted an object. Older installed
worlds can retain executable revisions while newer worlds adopt a successor.

### 10. Strategy games and governed factions

Factions can possess territory, appoint officers, issue scoped commands,
manage treasuries, form alliances, and conduct time-bounded campaigns.

Territory is not merely a role. An alliance is not merely a permission. An
officer certificate can be attenuated by region, action, or deadline. A treaty
can be a durable relationship and workflow with explicit breach or expiry
behavior. Views can derive maps, rosters, supply lists, and active fronts from
the same underlying semantics.

### 11. Simulation and digital-twin worlds

Facilities, fleets, or simulated environments can use stable identities for
equipment and locations; Containment for placement; Custody for stewardship;
Relations for dependencies; certificates for operator qualifications; and
Occasion for auditable changes.

Bonfire cannot prove that a physical sensor is truthful. It can, however,
preserve which principal or admitted Handler asserted a fact, under which
authority, and what committed behavior followed from it.

## Markets, exchange, and shared resources

### 12. Escrow marketplaces

A marketplace can separate listing, possession, payment, delivery entitlement,
dispute authority, and reputation instead of compressing them into one order
status.

A trade workflow may reserve a conserved holding, await payment, wait for a
delivery event, complete both transfers, or compensate after a deadline.
Retries use stable identities and idempotency rather than hoping a payment API
was called only once. Arbitrators receive narrow certificates scoped to the
dispute instead of administrator access to the marketplace.

### 13. Community currencies and mutual-credit systems

Currency Kinds can declare fungibility, unit scale, transfer, consolidation,
extinction, and portability policies. Conservation remains owned by Custody;
membership and governance remain separate.

Different worlds can operate different issuers and acceptance policies. A
remote balance need not automatically become trusted local money. Exchange or
bridging can be an explicit Settlement protocol with priced failure and local
Authority decisions.

### 14. Equipment libraries

Libraries, studios, laboratories, and cooperatives lend tools whose use may
require both current possession and a valid qualification.

The system can express:

- who currently holds an item;
- which room, cabinet, or kit contains it;
- whether it is reserved or checked out;
- whether the holder is certified to operate it;
- when it must return;
- which damage or maintenance record applies;
- which steward may override a lockout.

Possession, placement, qualification, and scheduling remain distinct facts
that can be combined at the Gate.

### 15. Licensing and usage-limited digital goods

A digital resource can be accompanied by a certificate that permits named
operations, limits the presenter, expires, or allows a fixed number of uses.
The underlying asset and the permission to execute it need not be the same
thing.

This could support commissioned media, private datasets, model access,
software extensions, game content, or community archives. Bonfire provides
the authorization and durable-use semantics; it does not replace external
legal enforcement or digital-rights law.

### 16. Provenance-aware supply networks

Assets can move between custodians while certificates record inspections,
origin claims, handling qualifications, or acceptance decisions. Fork lineage
and signed artifacts preserve provenance when data crosses hosts.

The architecture can demonstrate who asserted a claim and how it was used. It
does not turn assertions into physical truth, so external attestations and
audits remain necessary.

## Physical spaces and local organizations

### 17. Co-living and housing cooperatives

A co-living world can represent residents, rooms, leases, keys, guest passes,
chores, common funds, equipment, and governance.

Containment can express occupancy and room capacity. Relations can express
residency and working groups. Custody can express keys and shared equipment.
Authority can combine residency, current possession, time windows, and
sanctions. A one-use guest invitation can extinguish on entry. A departing
resident can lose access without erasing their historical participation.

### 18. Makerspaces and laboratories

Machines occupy physical locations, have maintenance state, and require
qualifications. Projects can reserve equipment; operators can receive
certificates; dangerous operations can require current issuer checks rather
than causally stale Authority.

Automation can schedule inspections and lockouts. Views can serve available
machines, expiring qualifications, maintenance queues, and active projects.
The same equipment identity survives moves between rooms or physical shards.

### 19. Festivals, conferences, and temporary cities

Events combine tickets, zones, staff roles, schedules, vendors, equipment,
temporary credentials, and highly ephemeral presence.

Durable admission rights should not be confused with live occupancy. Tickets
can be one-use holdings or certificates. Zone access can depend on staff role,
time, and current placement. Presence can remain a Signal. After the event,
the world can retain its archive without retaining unnecessary live tracking.

### 20. Clubs, sports leagues, and associations

Teams, seasons, venues, equipment, officials, sanctions, eligibility, and
results all have different lifecycles. A referee credential may apply only to
a league and season. A player can belong to a club without being eligible for
every match. Equipment can be held by a team but placed at a venue.

The model can explain eligibility and authority rather than relying on a
single account role.

### 21. Shared infrastructure and neighborhood networks

Neighborhood groups can coordinate gardens, tools, meeting spaces, energy
assets, transport, or local funds. Access can combine membership, bookings,
possession, training, and time. Decisions can use declared quorum workflows.
The community can change host without surrendering its history and Kind
definitions.

## Agents, bots, and automation

### 22. Governed agent workforces

An agent can receive a certificate restricted by action, port, resource,
world, presenter, duration, use count, and delegation depth. It can claim work
through Settlement and execute an exact content-addressed Handler.

The resulting system can answer:

- Which principal authorized this agent?
- Which artifact executed?
- What resources could it access?
- Which causal revocations were known?
- Did the work commit, retry, compensate, or expire?
- Can the same request execute twice?

This is substantially safer than sharing a service account or embedding a
long-lived API key in an agent process.

### 23. Personal representative agents

A person may delegate narrow tasks to an agent: scheduling within one group,
moderating replies on one publication, purchasing within a budget, or
maintaining a collection.

The agent does not become the person. Its presenter identity and delegated
certificate remain explicit. The delegation can expire or be revoked without
rotating every credential owned by the person.

### 24. Moderation agents with bounded reach

Automated moderation can be separated into detection, recommendation, and
action. One Handler may label content; another may propose a sanction; only a
certificate-bearing principal may execute a destructive operation.

Communities can install different moderation packages and retain evidence of
which policy and artifact produced a decision. Appeals can operate on durable
decision records instead of screenshots of an opaque model response.

### 25. Cross-organization automation

Two organizations may coordinate orders, approvals, deliveries, or service
requests without sharing one database or root administrator. Remote
certificates remain presented proofs; each destination evaluates or reissues
local Authority.

Settlement makes delivery eventual and explicit. A failed remote host does not
masquerade as a successful atomic transaction.

### 26. Agent marketplaces

Agents or Handler packages can advertise typed capabilities and exact
conformance evidence. A world may install a provider only after checking
artifact identity, declared imports and effects, requested Authority, license,
publisher continuity, and consent.

This creates the basis for a computation market where compatibility means
more than exporting a function with the expected name.

## Knowledge, culture, and education

### 27. Research commons

Papers, datasets, experiments, reviews, citations, and research groups can be
stable objects with explicit relations and provenance. Publication Authority
can be distinct from authorship. A dataset license can constrain export of its
artifact bytes while still allowing an exact reference.

Views can serve citation graphs, review queues, project collections, and
release feeds. A research community can fork or migrate without losing the
lineage of its local decisions.

### 28. Collaborative archives

Communities can curate oral histories, media, annotations, exhibits, and
access policies. Subjects may consent to some records but not others. World
governance cannot automatically broaden private inclusion during export.

Curator roles, embargoes, provenance attestations, and public Views remain
separate semantic layers. The archive can preserve its interpretation
artifacts along with its content references.

### 29. Publishing collectives

Writers, editors, reviewers, publications, editions, and licenses form a
relationship-rich world. Editorial Authority can be scoped to a publication
or issue. Publication workflows can require review, approval, deadlines, and
compensation without granting every editor global administrator access.

Fork lineage is particularly useful here: a collective can split while
preserving which works, policies, and revisions came from the shared history.

### 30. Learning communities

Courses, cohorts, projects, mentors, qualifications, and portfolios can live
across institutions. Completion evidence can be a certificate; participation
can be a Relation; access can depend on prerequisites and current enrollment;
portfolio artifacts can remain owned by the learner.

A receiving institution does not need to trust every foreign certificate as
active local Authority. It can verify provenance and reissue the qualification
it recognizes under its own policy.

### 31. Apprenticeship and competency networks

Competency is often contextual: an electrician may be certified for certain
equipment, jurisdictions, or dates. Bonfire certificates can describe that
coverage and issuer epoch explicitly. Equipment Gates can require a current
qualification and local membership together.

Revoking one issuer or qualification need not rewrite the person's complete
identity or unrelated credentials.

## Governance and collective action

### 32. Cooperatives

A cooperative can model members, working groups, elected roles, proposals,
budgets, treasuries, shared equipment, paid work, and constitutional packages.

Membership remains distinct from office. A treasurer certificate can expire.
A spending workflow can require quorum and a budget scope. Settlement can pay
for claimed work exactly once. Sanctions can limit particular actions without
deleting membership history.

### 33. Participatory budgeting

Proposals, endorsements, votes, funding pools, milestones, and disbursements
have different ownership and lifecycle rules. Vote uniqueness can be enforced
as a Relation constraint. Quorum and deadlines can be workflow rules.
Disbursement remains a conserved Custody transfer authorized by the decision,
not an incidental effect of changing a proposal status.

### 34. Mutual-aid networks

Requests, offers, volunteers, resources, locations, and sensitive subject data
can be coordinated without making all information public to every member.
Authority can be scoped to a case or resource. Subject consent and world
governance remain separate during export.

Bonfire is not presently an offline-first emergency system, so deployments
that must operate through network loss would require additional product and
protocol work.

### 35. Constitutional organizations

An organization can treat its operational constitution as versioned packages,
Kinds, Authority policy, and workflows rather than prose interpreted manually
by one privileged backend.

Not every social norm should become code. The opportunity is to make the
rules that do control digital effects explicit, inspectable, versioned, and
bounded by owner-defined codecs.

## New product forms enabled by the combination

### Portable worlds as a normal competitive pressure

If a world export carries its normalized graph, retained history, Kind
families, exact executable artifacts, licenses, identity mapping, and signed
provenance, migration can become an ordinary governance option rather than a
catastrophic reconstruction project.

Hosts could compete on reliability, moderation services, jurisdiction,
latency, price, or community support. A host signs what it exported but cannot
unilaterally broaden subject consent. The destination admits artifacts and
reissues Authority according to local policy.

### Forking without amnesia

Communities and projects sometimes need to split. Conventional exports create
copies whose relationship to the source rapidly becomes ambiguous. Durable
fork lineage can preserve source and destination coordinates without granting
the source continuing control.

This could support:

- a game realm separating from its original operator;
- a cooperative division;
- a software or research community fork;
- a local chapter creating an independent world; or
- a temporary experimental branch that may later exchange evidence.

### Capability-bearing objects

Physical and digital objects can confer Authority because of their current
Custody or Containment state. A key, badge, equipped item, signed instrument,
or installed module can become part of an explainable decision.

The important property is revocation by semantic change. Moving a key out of
an equipped slot, transferring an item, advancing an issuer epoch, or
extinguishing a one-use invitation can remove the standing without a second
application-specific permission database.

### Relationship-native applications

Many products treat relationships as join tables subordinate to accounts or
content. Bonfire can make a relationship occurrence a stable Yi with its own
Kind, state, Authority, lifecycle, constraints, and history.

This opens product designs around mentorships, contracts, collaborations,
alliances, care relationships, subscriptions, endorsements, disputes, or
commitments rather than treating them as boolean flags.

### Worlds composed from constitutional packages

A world can install packages that introduce exact Kind families, Views,
Handlers, workflows, and requested Authority. Because install consent and
artifact identity are durable, a community can know not merely that a plugin
is enabled, but which revision and capabilities it admitted.

This suggests an ecosystem of reusable constitutional components:

- election and quorum protocols;
- moderation systems;
- escrow and trade workflows;
- membership and invitation policies;
- equipment and qualification systems;
- publishing and review workflows; and
- agent delegation templates.

### Semantic interoperability instead of universal schemas

Bonfire does not require every host to share one global database schema or
trust root. Interoperability can occur through exact Kind identities,
content-addressed artifacts, typed operations, signed evidence, and explicit
local admission.

Two worlds may recognize the same Kind family while retaining different
Authority, governance, and storage. Alternatively, they may exchange only a
reference or provenance evidence. The boundary is part of the design rather
than something hidden beneath a nominally universal API.

### Infrastructure that can move under a live product

Logical Domain identity is independent of physical shard placement. This
makes it possible to move a hot community, channel, zone, or organization to
another database without changing its product address.

Combined with queue and coordination budgets, this creates a path toward
isolating noisy worlds without teaching every application feature about
shards.

## Five illustrative end-to-end scenarios

### A one-use community invitation

1. A community issues an invitation certificate with one permitted use,
   destination-world coverage, a validity interval, and a named presenter.
2. The recipient presents it to the join operation.
3. Authority verifies issuer state, coverage, presenter, expiry, and use
   count.
4. The membership Relation is formed.
5. The invitation use commits in the same governed operation and the
   instrument extinguishes.
6. A retry returns the prior result rather than forming duplicate membership.

### An equipped guild key

1. A guild key is a conserved holding owned by a member.
2. It is placed in an equipment slot governed by Containment.
3. A cross-facet binding makes that equipped evidence confer access to the
   guild treasury.
4. Moving the key into a backpack removes the standing without transferring
   ownership.
5. Selling the key uses Settlement to transfer it exactly once.
6. The former owner loses access; the buyer gains access only after valid
   placement.
7. Advancing the issuer epoch can revoke all keys from a compromised issue.

### A governed community migration

1. Governance approves the exact destination, external-reference, UID, key,
   fork, and consent policy.
2. Each Kind contributes its inclusion and artifact-license decision.
3. Private subject rows without consent become signed redaction evidence or
   are excluded.
4. The source forms one signed export from a consistent representation
   snapshot.
5. The destination verifies host signature, graph closure, history, Kind
   lineage, artifact bytes, and licenses.
6. Identities and Domains are preserved or deterministically remapped.
7. Foreign certificates remain provenance; destination policy reissues local
   certificates.
8. Behavioral checks prove reads, writes, Views, and governance rather than
   merely comparing row counts.

### An agent purchasing within a budget

1. A person delegates a certificate allowing one agent to invoke a purchase
   workflow for a named resource family and maximum budget.
2. The package and Handler artifacts are pinned by digest.
3. The agent claims a Settlement task with a stable idempotency key.
4. Gates evaluate presenter, coverage, budget, expiry, and current revocation
   requirements.
5. Payment enters escrow and the asset transfer proceeds.
6. Failure triggers declared compensation; success commits exactly once.
7. Occasion records which agent, certificate, artifact, and effects were
   involved.

### A makerspace machine reservation

1. A member forms a reservation Relation to a machine and time window.
2. A View lists upcoming reservations without scanning every Yi.
3. At activation time, a Gate checks membership, qualification certificate,
   sanction state, reservation, and machine maintenance state.
4. Live occupancy is recorded separately from durable qualification.
5. A maintenance lockout or issuer revocation immediately changes the
   decision.
6. An automation Handler closes expired reservations and schedules inspection
   without receiving global administrative access.

## Where Bonfire is not the right tool

Bonfire's semantic machinery has a real cost. A simple blog, brochure site,
small CRUD dashboard, or stateless API probably does not need Domains,
Settlement, certificate Authority, portable Kind lineage, or governed world
exports.

Bonfire also does not automatically provide:

- truth about external physical events;
- legal recognition of a digital credential;
- permissionless global consensus;
- atomic transactions across independent hosts;
- dead-host recovery beyond retained export artifacts;
- offline-first synchronization; or
- a substitute for product governance and human judgment.

The architecture is most justified when several hard requirements overlap:

- ownership or conservation;
- containment or capacity;
- relationship cardinality and lifecycle;
- revocable, explainable Authority;
- durable history and recovery;
- retries, compensation, or deadlines;
- constrained third-party computation;
- governed policy evolution;
- subject privacy and consent;
- world or identity portability; and
- physical distribution without topology leakage.

## The larger possibility

Most platforms make a quiet trade: they provide convenient product features
in exchange for becoming the permanent owner of identity, authority, data
shape, history, and execution. Export usually means a collection of files or
rows that cannot reproduce the behavior of the original community.

Bonfire points toward a different arrangement. A host can operate the
infrastructure without owning the world's constitution. A package can add
behavior without receiving ambient power. An agent can act without becoming
its principal. An object can confer capability without becoming a hidden ACL
entry. A community can leave without pretending that foreign Authority remains
valid everywhere. A logical world can move physically without changing what
its products believe it is.

The deepest opportunity is therefore not any single application listed above.
It is a reusable foundation for digital institutions whose semantics survive
growth, automation, operator changes, and distribution.

## Related reading

- [Yi](yi.md)
- [Authority](authority.md)
- [Holdings](holdings.md)
- [Relationships](relationships.md)
- [Lifecycle](lifecycle.md)
- [Ports and faces](ports-and-faces.md)
- [Portability and federation constitution](../yi/49-structural-arc/constitution/portability.md)
- [Product proof](../yi/49-structural-arc/constitution/product-proof.md)
- [Current structural-arc handoff](../yi/49-structural-arc/HANDOFF.md)
