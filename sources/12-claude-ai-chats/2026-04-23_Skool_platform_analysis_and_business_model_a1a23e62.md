# Skool platform analysis and business model

created: 2026-04-23T16:37:22.449938Z  uuid: a1a23e62-b2be-4b1e-8765-06f1a21df677  export: new
messages: 12  total_chars: 110160  human_chars: 502

summary: **Conversation Overview**

The person conducted a deep research session on Skool.com, starting with a broad investigation of the platform's functions, features, business model, and growth strategy. Claude provided a comprehensive research report covering Skool's four core product tabs (Community, Classroom, Calendar, Gamification), its two-tier pricing structure ($9/month Hobby and $99/month Pro per group), and its strategic growth mechanisms including the affiliate flywheel, the Skool Games tournament, SEO-indexed public communities, and the influence of founders Sam Ovens and Alex Hormozi.

The conversation then narrowed to specific technical areas. The person asked how Skool's automation and plugin layer actually works, and Claude broke down the AutoDM mechanism (a single-message onboarding DM with two variables and no sequencing), the Zapier integration (triggers on membership lifecycle events, actions for course unlocking and member inviting), raw webhooks for external checkout platforms, and the full plugin list including tracking pixels, AutoMod, and affiliate hooks. The person then requested a feature-level breakdown of Skool's four main competitors — Kajabi, Circle, Mighty Networks, and Teachable — and Claude detailed each platform's distinct product philosophy and feature sets.

The conversation culminated in a deep structural/architectural analysis. The person asked Claude to reverse-engineer the primitive type systems of all five platforms and how those types connect, then specifically focused on space and group container structures. Claude produced a detailed comparative analysis mapping each platform's container topology, access primitives, content type vocabulary, and the structural trade-offs involved. Key domain terminology used throughout included: polymorphic Space types, AccessGroups, Enrollment, Offer/Product separation, CRM Contact vs. Member distinction, capability-set orthogonality, containment trees, and per-group vs. per-plan billing scopes. The person demonstrated strong systems-architecture intuition, gravitating toward questions about type systems, primitive concepts, orthogonality of access vs. containment, and how structural choices constrain or enable business model flexibility — consistent with someone building or evaluating platform infrastructure.


---
**HUMAN** (2026-04-23T16:37):

do a deep research on  https://www.skool.com/
what functions they have? what features they have? what is their model and strategy ?

---
**ASSISTANT** (2026-04-23T16:39):

  I need to dig into Skool.com to understand what they actually do—their core features, business model, and overall strategy. Let me pull some detailed information directly from their site to get a comprehensive picture.
```
This block is not supported on your current device yet.
```

 Now I'm digging into Skool's business model, key features, and overall strategy to get a fuller picture.
```
This block is not supported on your current device yet.
```

 I need to look up Skool's official pricing information and dig deeper into what they're actually offering and how they're positioning themselves in the market.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

 I need to check the about and features pages to understand what functionality this product actually offers.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

 Let me round out my understanding by examining the Skool Games and their discovery strategy.
```
This block is not supported on your current device yet.
```

 I should look into Skool Games and their discovery page to better understand how they're approaching growth.I have comprehensive information. Let me put together a thorough research report on Skool.

---

# Deep Research: Skool.com

## Company snapshot

Skool is a community-first platform built around the idea that online communities, courses, events, and gamification should live under one roof. It was founded in 2019 by Sam Ovens (CEO) and Daniel Kang (CTO), with roughly 30 employees, based in Los Angeles. Alex Hormozi partnered with Skool in 2024 to create The Skool Games. Hormozi is now both a major investor and the public face of Skool's growth push — reportedly calling it "the biggest investment of my life," and widely assumed to hold around a 50/50 ownership split with Sam Ovens.

Positioning: Skool sits between Facebook Groups, Discord, Kajabi, Circle, and Patreon — trying to collapse "community + course + calendar + payments" into a single, intentionally simple product.

---

## Core functions and features

Skool organizes everything around a single unit called a **group**. A group can be public or private, free or paid. Inside each group there are four primary tabs, which map to the four feature pillars:

**1. Community (the feed).** A Facebook-style feed where members can post, comment, like, and reply. Limitations include no group chats, only one main community feed per group (no sub-groups), and basic moderation. Posts are categorized, and there is universal search across every post, comment, and lesson.

**2. Classroom (courses).** A drag-and-drop course builder where you structure content into modules and lessons, embed videos from external platforms, or use native video hosting. You can control course access based on member activity or payment. Courses can be free and open to everyone, restricted to logged-in users with a particular level membership, or restricted to paying members only. Notably missing: quizzes, assessments, certificates, drip scheduling, and advanced analytics — this is a deliberate minimalism.

**3. Calendar (events).** Built-in event scheduling for live Zoom calls, workshops, webinars, and meetups, with automatic timezone handling and sync to external calendars such as Outlook and Google Calendar. A recent addition is a native **webinar** feature for more professional live sessions.

**4. Gamification (points, levels, leaderboards).** This is Skool's signature mechanic. Points are earned when others like your posts, comments, and replies — 1 like = 1 point. After a member obtains a certain number of points, they level up, and admins can set courses to unlock at certain levels to further drive participation. There are currently nine levels in total, and leaderboards can be viewed over the past 7 days, 30 days, or all time. The loop is: engage → earn likes → level up → unlock content → keep engaging.

**Supporting features:**
- Member profiles, DMs (admin-enabled), notifications across all joined groups.
- Native iOS and Android apps.
- **Skool Payments** (native billing, no Stripe setup required) with automatic sales tax compliance.
- **Custom URL / domain** on both plans.
- **Affiliates** — both Skool-wide and member-referral affiliate programs baked in.
- **Tier management** with drag-and-drop benefits and a "view as member" mode (recent additions).
- **Lifetime value tracking** and expanded analytics (recent additions).
- **Automation / plugins** — AutoDM, Zapier-style integrations (Pro plan).
- **Discovery page** — a public leaderboard of top communities on skool.com that drives organic traffic to paid groups.
- **SEO-friendly pages** — each community post is a fully SEO-optimized web page that can rank on Google — on most platforms like FB Groups, Discord, and Slack, the content you post inside a community stays private and invisible to the outside world.

What's intentionally missing: quizzes/assessments, certificates, sub-groups, group chats, multiple membership tiers per group (you pay once per tier structure), deep white-labeling, native live video streaming, and rich segmentation. Skool has chosen "few features, done simply" over parity with Kajabi or Circle.

---

## Business model

**Pricing (two plans, both with 14-day free trial, no permanent free plan):**

- **Hobby — $9/month.** 10% + 30¢ transaction fee. Unlimited members, courses, videos, live calls, custom URL, affiliates.
- **Pro — $99/month.** No Skool platform fee on sales up to $899 per transaction — then 1% platform fee on sales above $899 (effective rate 3.9% + 30¢ including Stripe). Adds team admins, automations/plugins, member referral system, ownership transfer, cleaner branding. Both prices are per group — running multiple communities means paying for each one separately. Annual billing saves ~17%.

**Break-even logic:** The break-even point is roughly $1,200–$1,400/month in membership revenue. Below that, Hobby is usually cheaper. Above that, Pro typically saves you money.

**Revenue streams for Skool itself:**
1. Monthly subscription fees from creators ($9 or $99 × number of groups).
2. Transaction fees on every paid membership or course sale.
3. Payment processing margin on Skool Payments.

**Revenue streams Skool enables for creators:**
- Recurring monthly/yearly memberships (most popular — visible on their homepage: $9–$6,000/year ranges).
- One-time course purchases.
- Free communities that act as funnels to paid offers elsewhere.

This creates strong alignment: Skool makes more money when creators make more money.

---

## Growth strategy — how Skool actually scales

Skool's growth playbook is unusually disciplined and relies almost entirely on *compounding loops* rather than paid advertising. Five interlocking mechanisms:

**1. Dogfooding as marketing.** From the very beginning, team Skool set up a meta community to discuss the product and started using the platform — they started using Skool to discuss Skool. The official "Skoolers" group has ~196k members and functions simultaneously as customer support, feature discovery, onboarding, and a live product demo.

**2. The affiliate flywheel (the core growth engine).** Skool is free for community members and charges $99/month from community creators for each group they want to create. All users — creators and members — can refer Skool to others and earn 40% of their monthly subscription fee for life. That's a lot of commission for a long time when most SaaS companies offer 20% for just 12 months. The best part is when you realize that you can start a group on Skool by paying $99 a month, bring in members to your group, and if just three of your members start their groups, you can use Skool for free forever. Skool runs the program through FirstPromoter with a 60-day cookie window. If a user pays $99/month, an affiliate earns $39.60 every month — over $475 from one referral kept 12 months. This turns every creator into a distribution channel.

**3. Member-level affiliates inside groups.** Separate from the Skool-wide program, each community owner can enable 10–50% commission rates for member referrals inside their own group. Members become ambassadors for individual communities — another flywheel layer.

**4. The Skool Games (the PR and acquisition engine).** The Skool Games started in February 2024 and has been running monthly since then. It's a monthly tournament where participants can win prizes, including a trip to Vegas to spend a day with Alex Hormozi. From September to December 2024, the 1st place finisher each month won a Tesla Cybertruck. The concept includes leaderboards that rank participants in real-time based on how much money they're making on the Skool platform from monthly subscriptions. This does three things at once: (a) massive social proof, since winners publicly celebrate hitting real revenue numbers; (b) content generation, since Hormozi streams the events and clips propagate everywhere; (c) it manufactures a cohort of power-users who themselves recruit.

**5. SEO from public content + the Discovery page.** The homepage itself *is* an acquisition channel — a public leaderboard of top communities with preview snippets and member counts, ranked and browsable by category (Hobbies, Money, Spirituality, Tech, Health, Sports, Self-improvement, Relationships). Every community has a discoverable public page; every public post is indexable. Top groups like AI Automation Society with 330.8k members, Skoolers with 196k members, and Day by Day Wellness Club with 61.3k members pull search traffic that funnels into the platform.

**6. Celebrity founder gravity.** Sam Ovens brings a pre-existing audience of online entrepreneurs. Hormozi brings mass reach (millions of YouTube/IG followers) plus instant credibility with high-ticket coaches. Skool's user base reportedly went from 3–5 million to over 15 million users in less than a year after Hormozi's involvement.

---

## Strategic philosophy — what makes Skool *Skool*

Reading between the lines of the product, the pricing, and the growth loops, the strategy rests on four deliberate bets:

**Bet 1: Simplicity is a moat.** Competitors like Kajabi, Circle, Mighty Networks, and Teachable compete on feature breadth. Skool competes on feature *restraint* — four tabs, one price structure, one core loop. This lowers onboarding friction (a creator is live in under 30 minutes) and keeps churn down because there's less to configure, misconfigure, or outgrow-before-mastering.

**Bet 2: Gamification > pedagogy.** Skool doesn't try to win on "best learning outcomes." It wins on *engagement*, because engagement drives retention, and retention drives creator MRR, and creator MRR drives Skool's fees. The consistent critique — Skool's engagement tools and gamification are excellent for community retention, but they don't guarantee your students actually complete your course and get results — is arguably a feature, not a bug, from Skool's P&L perspective.

**Bet 3: Align incentives through the affiliate stack.** The 40%-for-life commission plus the "3 referrals = free forever" math turns the cost line on a creator's P&L into a potential profit line. This is the single most important strategic choice: it converts customers into a distributed, self-funding sales force.

**Bet 4: Community-first, course-second.** Most competitors are LMS-first. Skool explicitly inverts the stack — the community is the primary object, and courses are something that live *inside* a community. This matches where the coaching/creator economy has been heading (cohorts, accountability, peer-learning) and makes Skool harder to substitute with a pure LMS.

**Risks and tensions worth noting:**
- Per-group pricing is friction for creators who want multiple offers or tiered products.
- Skool currently has a 1.9 out of 5 on Trustpilot — most complaints relate to billing issues and support responsiveness.
- The hard identification with high-ticket coaching / "make money online" culture (via Hormozi, the Games, the Cybertruck prizes) is a double-edged sword — great for acquisition in that niche, a turnoff for more academic, enterprise, or hobbyist verticals.
- Feature minimalism has a ceiling: serious course businesses that need assessments, certificates, drip, or segmentation eventually migrate to Kajabi/Circle/Thinkific.

---

## TL;DR

Skool is a deliberately simple, community-first SaaS platform (four tabs: Community, Classroom, Calendar, Gamification) priced at $9 or $99 per group per month, monetized through subscriptions plus transaction fees. Its strategic engine is a tightly designed set of growth loops — meta-community dogfooding, a 40%-for-life two-tier affiliate program, the Skool Games tournament, public SEO-indexed community pages, and celebrity founder gravity (Ovens + Hormozi) — that together convert customers into a compounding distribution network. The bet is that feature restraint + gamified engagement + aligned affiliate incentives beats the feature-breadth strategy of Kajabi, Circle, and Mighty Networks, at least in the coaching/creator-economy segment where it has clearly found its wedge.

---
**HUMAN** (2026-04-23T16:42):

how does their "Automation / plugins — AutoDM, Zapier-style integrations" work?

---
**ASSISTANT** (2026-04-23T16:43):

  The user is asking about a specific feature I mentioned — Skool's automation and plugin capabilities like AutoDM and Zapier-style integrations. I need to search for current information on how these features actually work since this is a factual question about a present-day product.
```
This block is not supported on your current device yet.
```

 I should pull up the specific Zapier triggers to provide some concrete examples of what's available.
```
This block is not supported on your current device yet.
```

 I've got what I need to give Ren a solid technical breakdown. Since they're deep in systems architecture themselves, I should skip the marketing angle and focus on the mechanics—where automation lives in the interface, how triggers and actions connect, what the actual constraints are. I'll keep it tight and systems-focused.# How Skool's automation layer actually works

Skool's automation sits under a single **Plugins** tab inside each group's admin settings. It's not a general-purpose workflow engine — it's a small set of discrete toggles, plus a Zapier integration that exposes the interesting hooks. All of it is Pro-plan only.

## AutoDM — the simplest piece

AutoDM is a single-message onboarding automation. It's not a sequence, not a drip, not conditional — just one welcome DM sent to each new member.

Mechanically: you go to Plugins → edit the message → the editor supports two variables, `#NAME#` and `#GROUPNAME#`. You pick which admin account the DM appears to come from (only admins can be the sender). Toggle it on. When a new member joins the group, they receive the message within 1 to 5 minutes. If a conversation already exists between them and the sending admin, they will not receive an AutoDM.

That's the entire feature. The recommended pattern Skool's own docs push is "Ask an open and a closed question" — e.g. "Hey #NAME#, welcome to #GROUPNAME#! Are you new at Skool? And what motivated you to join?" — because the closed question boosts reply rate and the open one gives you sales intel.

There's no native support for multi-step sequences, delays, branching, or re-triggers. Skool has minimal automation. It offers AutoDM (a single automated welcome message to new members) and basic membership screening, but unlike Circle or Mighty Networks, Skool provides no post scheduling, no multi-step DM sequences, no AI moderation, and no workflow automation. This gap is why a small ecosystem of third-party tools (SkoolMate, StickyHive, etc.) has grown up around it.

## Zapier integration — the real automation surface

The Zapier integration is where anything non-trivial happens. You enable the plugin, Skool gives you an API key and group URL, and you paste those into Zapier. From there you get a standard trigger/action model.

**Triggers Skool exposes to Zapier:**
- Answered Membership Questions — fires when a potential member submits answers to group membership questions
- New paid member — fires when a new member successfully completes payment and joins the group
- New course member, course content updates, published posts (per Zapier's listing)

**Actions Skool exposes (things Zapier can do *to* Skool):**
- Unlock a given course for a specific member in your group
- Invite a new member (via webhook catch)
- Create/update member records

So the integration is fundamentally *event-out, command-in*: Skool emits membership lifecycle events, and external systems can reach in to manipulate course access and memberships. There's no action for posting to the feed, no action for sending a DM, no scheduling primitive — the things you'd most want to automate editorially aren't in the API surface.

## The webhook path

Separate from Zapier, Skool also has a raw webhook plugin. You enable it, Skool gives you a webhook URL, and any external system can POST to that URL to invite members. Members who send an email to this customized webhook URL will receive a unique invitation link to join your group immediately without having to go through the approval process. This is how checkout platforms like CopeCart, ThriveCart, and GoHighLevel integrate — they post purchase events to the Skool webhook and the buyer gets auto-invited.

## The broader plugin list for context

Beyond AutoDM and Zapier, the Plugins tab includes:

- **Membership Questions** — up to three custom questions shown before a member joins; used for screening and lead-capture. Answers can be routed to a CRM via Zapier.
- **Onboarding video** — a welcome video shown to new members.
- **Meta (Facebook) Pixel tracking** and **Google Ads tracking** — fire conversion events from the About page and signup flow.
- **Hyros integration** — for attribution/ads-remarketing folks.
- **AutoMod** — spam moderation, recommended once a group hits ~1,000 members.
- **Cancellation video** — plays when a member tries to churn.
- **Instant Membership Approval** — auto-approves all join requests (no vetting).
- **Developer-only invite hook** — for custom checkout flows with external payment processors.

## Practical architecture

The common pattern creators use is a three-layer stack: Skool holds community + course + billing; Zapier or Make holds the orchestration logic; an email/CRM platform (ActiveCampaign, GHL, ConvertKit) holds the sequences and segmentation. The typical flows look like:

- *Lead capture:* Membership Question answered → Zapier → contact created in CRM with tags.
- *Course unlock on external payment:* Stripe/ThriveCart webhook → Zapier → Skool "unlock course for member" action.
- *Post-purchase onboarding:* new paid member → Zapier → multi-step email sequence in ActiveCampaign (because Skool itself can't run the sequence).
- *Churn / refund:* CRM tag change → Zapier → remove member / revoke course in Skool.

## Honest read on the architecture

The design is intentionally thin. Skool exposes just enough hooks to plug into the standard creator stack (Stripe checkout, ESP, ads pixel, CRM) and leaves real orchestration to Zapier. The model is closer to a set of discrete webhook endpoints wrapped in a UI than to a workflow engine. Given your background with capability-style systems, the mental model that fits is: each plugin is a capability edge to an external system, and Skool deliberately keeps its own execution layer almost empty. That's why the third-party ecosystem exists — the space between "event emitted" and "action taken" is where all the real product work happens, and Skool has chosen not to build there.

---
**HUMAN** (2026-04-23T16:48):

I what to know what exactly they have

[attachment excerpt_from_previous_claude_message.txt]
Competitors like Kajabi, Circle, Mighty Networks, and Teachable compete on feature breadth


---
**ASSISTANT** (2026-04-23T16:49):

  The user is asking for a detailed breakdown of what features each of these platforms actually offers — Kajabi, Circle, Mighty Networks, and Teachable. I need to search for current information on each platform's core capabilities to give them an accurate comparison.You want a feature-level breakdown of each of the four competitors I referenced. Let me pull current info on each.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

 Moving on to gather information about Teachable now.
```
This block is not supported on your current device yet.
```

 I've got solid information on all four platforms now. Rather than just listing features, I should focus on the architectural choices each one made—especially what Skool deliberately kept minimal compared to where competitors invested heavily. I'll organize this by showing what each platform fundamentally is, then map out the feature dimensions where they diverge.Here's a feature-level rundown of each. I'll group them by what they're actually trying to be at the core, because that's what drives the feature sets.

---

## Kajabi — a marketing-and-sales platform that happens to host courses

Kajabi was founded in 2010 and positions itself as an "operating system for knowledge entrepreneurs" rather than a community platform. Courses, email, website, funnels, community, coaching, and podcasting are all in one platform. The center of gravity is the funnel-to-sale pipeline, not the community feed.

**What you get:**
- **Courses** with modules, lessons, assessments, drip schedules, quizzes, and cohort-based delivery (cohort is a 2026 addition), plus completion certificates.
- **Coaching products** with native call scheduling, intake forms, milestone tracking, and one-on-one or group formats.
- **Email marketing** — broadcasts, sequences, and advanced automations with if/then branching (Growth and above). This is arguably their signature feature — no competitor on this list ships a comparable built-in ESP.
- **Sales funnels / Pipelines** — pre-built funnel templates (opt-in → sales page → checkout → thank-you → upsell).
- **Website builder** — full sites with landing pages, sales pages, blog, custom domain, analytics.
- **Checkout** with payment plans, coupons, order bumps, upsells, multi-currency (140+ currencies).
- **Community** — added later as a second-class feature. 1 community on Basic and Growth, 3 on Pro. Features include discussion threads, member directories, content gating, and event scheduling. Kajabi recently added gamification (leaderboards, points, challenges) to the community module.
- **Mobile app** for members, podcast hosting, newsletters, affiliate management, AI assistant ("Cofounder"), API access (2026 addition), video translations/transcriptions.
- **0% platform transaction fees** on all plans.

**Pricing (after the January 2026 restructure, annual billing):** Basic $143/mo, Growth $199/mo, Pro $399/mo.

**What Skool doesn't have but Kajabi does:** real email marketing, funnels, website builder, quizzes/certificates/drip, coaching scheduler, podcast hosting.

---

## Circle — the "professional community" platform

Circle is the closest to Skool in intent — community-first — but it's built for scale, customization, and branding rather than simplicity. It's used by organizations like Ali Abdaal's Productivity Club, Dr. Becky's Good Inside, Jay Shetty's Coaching Program, Harvard's CrimsonConnect, SpaceX's Starbase community, and Oprah's Daily Inside club.

**What you get:**
- **Spaces and Space Groups** — dedicated areas for courses, off-topic chats, and events, neatly organized in a sidebar. Public, private, or secret for paying members only. This is the core architectural difference vs. Skool — Circle gives you rooms; Skool gives you one feed.
- **Courses** with video/audio/text content, completion tracking, and up to 15 additional file resources (PDFs, images, videos) per course.
- **Live Rooms & Streams** — native livestreaming (no Zoom needed), workshops, group coaching.
- **Email Hub** — email broadcasts, marketing automations, and audience management. Circle in 2025–2026 has pushed hard into being a full ESP replacement.
- **Workflows** — visual workflow automation for onboarding, access, reminders, and engagement. This is Circle's equivalent of Zapier, built in.
- **AI Agents** (Enterprise+) — clone your knowledge into a 24/7 assistant that answers member questions, shares resources, and offers personalized support, trained on your posts, comments, courses, and resources.
- **Branded mobile apps** via Circle Plus — fully white-labeled iOS/Android apps with push notifications and in-app purchases.
- **Payments** — native checkout with custom branding, memberships, tiered access, paywalls on any space.
- **APIs** on the Business plan and up.

**Pricing (annual):** Professional $89/mo, Business $199/mo, Enterprise $419/mo, Circle Plus custom. Transaction fees range 0.5%–2% depending on plan.

**What Skool doesn't have but Circle does:** sub-spaces/rooms, native livestreaming, workflow automation, AI agents, branded mobile apps, paywalls on individual spaces, built-in ESP with segmentation.

---

## Mighty Networks — community + courses + native branded apps, with a "Community Design" opinion

Mighty Networks is the oldest of the three community-first platforms (founded by Gina Bianchini, who previously built Ning). Its distinctive bet is that community structure is a *design methodology*, not just a feature set — they ship something called "Community Design™" as a framework and Mighty Co-Host™, an AI community builder powered by Community Design and GPT-4.

**What you get:**
- **Unlimited members and Spaces** on all paid plans, with multiple space types (feed, chat, courses, events, livestream, Q&A, polls).
- **Courses** with lessons, sections, native video, quizzes, tests, and instant course outline generation via AI.
- **Native livestreaming** — 5 hours/month with 50 participants on Community plan, scaling to 40 hours monthly with up to 1,000 concurrent viewers on Growth.
- **Events** — online and in-person, with built-in livestreaming or Zoom integration.
- **Gamification** — leaderboards, referral programs, chat spaces, polls, questions.
- **AI Cohost** — an assistant tuned to your community that helps with content creation, engagement strategy, and runs "Daily Questions."
- **Mighty Pro** — custom branded iOS and Android mobile apps, starting at $33,000 annually for the Essential package. This is the serious play — Tony Robbins Arena, etc.
- **Memberships, bundles, cohort-based courses, challenges** — Mighty has a strong narrative around "paid challenges" as the onboarding funnel.
- **Integrations** (Zapier, Kit, Google Analytics) gated to Scale plan.
- **API access** on Scale tier and up.

**Pricing (annual):** Launch $79/mo (2% fees), Scale (higher), Growth $425/mo (1% fees), Mighty Pro from $33k/year.

**What Skool doesn't have but Mighty does:** native livestreaming at scale, multiple space types, cohort/challenge structures, Community Design framework, AI Cohost, truly white-labeled branded apps, member video upload.

---

## Teachable — a pure course-sales platform, not a community platform

Teachable is the odd one out on this list. It's not really trying to be a community platform — it's a course storefront and LMS that has *added* community as an included feature. Founded 2014, used by over 100,000 creators, processed over $2 billion in creator revenue.

**What you get:**
- **Courses** — drag-and-drop builder, video/PDF/text, quizzes, certificates, course compliance (enforced lesson completion), drip schedules.
- **Coaching products** — appointment scheduling, milestone tracking, intake forms, custom pages, one-on-one or group coaching.
- **Digital downloads** as a standalone product type (PDFs, templates, audio, video).
- **Memberships and bundles** — now unlimited on all plans (memberships and bundles don't count toward the published product limit).
- **Community** — basic threaded discussions and comments inside courses. It's a lightweight feature, not a social feed.
- **Native iOS and Android student app** on all paid plans.
- **teachable:pay** — native payment processor, with tax compliance handled automatically (their standout feature).
- **Sales & marketing** — abandoned cart emails, coupons, order bumps and upsell funnels, on all plans, affiliate program (Builder+), custom domain, email marketing (basic).
- **API and webhooks** on Advanced.
- **AI assistant** for course creation.

**Pricing (annual):** Starter $29/mo (7.5% transaction fee), Builder $69/mo (0% fee), Growth $139/mo, Advanced $309/mo. **Published products are gated per plan** (1, 5, 25, 100+), which is a hard constraint.

**What Skool doesn't have but Teachable does:** quizzes/assessments/certificates, enforced lesson completion, abandoned cart recovery, native digital downloads product type, coaching scheduler, full tax compliance, proper LMS structure.

**What Teachable doesn't have but Skool does:** any real community engine, gamification, points/levels/leaderboards, public discoverability.

---

## The synthesis — where Skool's feature minimalism actually cuts

Lined up against each other, the axes Skool chose *not* to compete on are clear:

| Axis | Kajabi | Circle | Mighty | Teachable | Skool |
|---|---|---|---|---|---|
| Community depth (sub-spaces, rooms) | basic | strong | strong | minimal | one feed only |
| Email marketing / automation | full ESP | full ESP | via Zapier | basic | none (Zapier only) |
| Funnels / landing pages / website builder | full | full | partial | partial | none |
| Course assessments (quizzes/certs) | yes | yes | yes | yes | **no** |
| Native livestreaming | partial | yes | yes | no | no |
| Branded white-label mobile apps | no | yes (Plus) | yes (Pro) | no | no |
| Gamification (points/levels/leaderboards) | yes (new) | limited | yes | no | **signature feature** |
| AI agents trained on your content | Cofounder | yes | Cohost | basic | no |
| Public community discovery / SEO | no | partial | no | no | **signature feature** |
| Per-group vs all-in-one billing | 1–3 comms | 1 per plan | 1 per plan | multi-product | **per group** |

So what you were paying for with Skool versus each competitor:

- Kajabi = email + funnels + coaching scheduler + multi-product business stack.
- Circle = rooms + workflow automation + livestreaming + AI agents + white-label apps.
- Mighty Networks = structured spaces + Community Design methodology + branded apps + livestreaming scale.
- Teachable = real LMS features (assessments, certs, compliance) + digital product types.

The pattern across all four is feature accumulation as a defense against churn: once a creator has built a funnel in Kajabi, a workflow in Circle, a branded app in Mighty, or a certified course in Teachable, switching costs are high. Skool's counter-bet is that the two things it kept (gamified feed + public SEO-indexed community) create stronger weekly engagement than any of the above, so the creator's *members* generate the lock-in instead of the creator's own configuration work.

Whether that bet holds depends on whether you're building a learning business (Teachable/Kajabi win on outcomes), a scaled branded community business (Circle/Mighty win on infrastructure), or a viral-loopy engagement-first community (Skool wins).

---
**HUMAN** (2026-04-23T17:05):

so structurally, what primitive concepts/types are there for each? and how do they connect? ultrathink

---
**ASSISTANT** (2026-04-23T17:10):

  The user is asking me to reverse-engineer the core data models and type systems of three platforms—not their features, but their fundamental primitives and how those primitives compose and relate to each other. They're deeply technical and work on SST, so they want me to dig into the architectural foundations of each system.

For Skool, I'm mapping out the core entities: Users form the base identity layer, Groups are the root containers and billing units, and Members represent the relationship between them with role-based access. The content layer includes Posts and Comments in the community feed, with Likes serving as the engagement/points mechanism. There's a separate educational structure with Courses containing Modules and Lessons, plus Events for scheduling and DMs for direct communication. Levels appear to be a gamification primitive, though the thought cuts off there. Almost everything in Skool lives within a Group context, with User being the only entity that spans across groups—this is what enables their per-group billing model. The structural choice to have exactly one feed per group with Categories as simple post tags reflects their design philosophy of minimalism.

Now looking at Kajabi's architecture: it's built around Users (account owners as Admins), Sites (the root billing unit with domain and branding), and Products (the monetization layer that come in various types like Courses, Communities, Coaching Programs, and Memberships). Products are configured through Offers, which represent different purchasable options like one-time purchases or subscription plans.

The rest of Kajabi's system revolves around managing customer relationships and engagement: Contacts are the core CRM primitive (distinct from Users), Tags segment those Contacts, and the platform provides Pages for web presence, Pipelines to structure funnels, and an ESP layer with Emails, Sequences, and Broadcasts. Automations tie it together with conditional logic, while Forms and Opt-ins capture leads that become Contacts.

The product layer breaks down into specific types—Courses organize into Categories and Lessons, Coaching manages Sessions and Appointments, Communities feature Circles with Posts and Comments, and Memberships wrap everything in subscription logic. Cofounder sits as a separate AI layer operating across these primitives.

The architecture hinges on a few key relationships: a Site contains all products, pages, contacts, and pipelines; Products map to multiple Offers (same product sold different ways); Contacts and Products connect many-to-many through purchases; and Pipelines are built from Pages, Emails, and Automations wired together. What distinguishes Kajabi is that Community is a Product type itself, not a root-level container.

The real graph centers on Contact as the CRM atom and Product as the monetization atom, with Pipelines connecting them. Kajabi's defining choice is treating Contact as the first-class primitive rather than Community Member—you can have Contacts who never purchase anything, and they only become Students or Members once they buy into a Product. That's what gives Kajabi its marketing-first feel.

Now looking at Circle's structure, it's built around User/Member as the core, with Community as the root (usually one per account with per-plan billing), and Space as the main container type that can be configured as a Post Space for feeds, Chat Space for messaging, or Event Space.

Circle ships multiple Space types natively—there's also Course Space for structured learning, Members Space, and Images Space. Spaces can be grouped in the sidebar using Space Groups, and monetization happens through Paywalls attached to either individual Spaces or Space Groups rather than to memberships themselves. Access Groups define which Members can see which Spaces, serving as Circle's role and permission system. Within Course Spaces, you get Courses with Sections and Lessons, and there's a Workflow system for visual automation.

Workflows trigger on member events, post events, or time-based conditions and execute actions. The platform also includes an Email Hub for broadcasts and campaigns, an AI Agent trained on community content with its own configuration, and Stripe-backed checkout that creates Members and assigns them to Access Groups. The architecture flows from Community down through Space Groups to individual Spaces and their content, while Access Groups operate as an orthogonal permission layer—when someone purchases a Paywall, it grants them Access Group membership and unlocks the associated Spaces.

What makes Circle's design distinct is that Space is a polymorphic primitive with subtypes like Post, Chat, Event, and Course, giving communities that "rooms" feeling with multiple typed containers. Access Groups are a separate primitive from membership levels, creating a more orthogonal structure than competitors like Skool or Kajabi.

Now looking at Mighty Networks, the core primitives are Host (the creator/owner) and Member, with the Mighty Network itself as the root container.

Mighty Networks uses a similar Space concept with multiple types—Activity feed, Chat, Events, Q&A, Polls, Articles, Courses, and Livestream—but distinguishes itself by treating Articles, Questions, and Polls as first-class content types rather than just post variations. Courses within a Course Space have a Sections → Lessons structure, and there's a Space Host role that grants elevated permissions on specific Spaces. Events support RSVP and livestream integration, while Members have customizable profile fields and access is managed through Plans.

Plans are the monetization layer—they can be bundled together and grant access to specific Spaces in a many-to-many relationship. There's also a Challenge type, which is essentially a time-boxed cohort-based course with daily content delivery, and a built-in referral program. The overall graph structure mirrors Circle's, with Mighty Network containing Spaces that contain content, and Host/Space Host functioning as a role-on-relationship rather than a standalone entity type.

The key differentiator is that Mighty treats content types as distinct primitives—Articles, Questions, and Polls aren't just Posts, they're their own types. Plans serve as both the monetization and access control mechanism. Community Design™ is a meta-methodology for composing Spaces together.

Now looking at Teachable's structure: it uses School as the root container with per-school billing, and Product as the monetization primitive, which can be subdivided into Course types that contain Sections and Lectures.

Teachable also has Coaching Products with Milestones and Appointments, Digital Downloads for files, and Pricing Plans that attach to Products with multiple variants like Free, One-Time, Subscription, or Payment Plan. There's also Bundles for multi-Product packages, Memberships as subscription wrappers, and Enrollment representing a student's access to a specific Product. The atomic content unit is Lecture, which can be polymorphic across video, text, quiz, and PDF formats, plus Quiz as a distinct content type with graded questions, and Certificate for issuance.

Beyond that, the system includes Sales and Checkout Pages per Product, Coupons for discounts, Email and Email Campaigns for basic ESP functionality, Affiliates as a User role for referrals, and Community as a new lightweight feature attached to products or at the school level. The key relationships are School containing Products with their Lectures, Lessons, and Milestones, Products having multiple Pricing Plans (Teachable's distinctive pattern where a Course can be sold four different ways), Products having many Enrollments linking Students to Products, Quizzes attaching to Lectures with grades feeding into completion state, and Certificates triggered by Enrollment completion.

The Published Product Limit is a billing constraint counting Courses, Coaching, and Digital Downloads but excluding Memberships and Bundles—a structural distinction that explains why Ruzuku separated them. The overall graph is Product-centric with Enrollment as the core student-product relation, Lecture is polymorphic, and Community feels bolted on rather than foundational. The deeper architectural choice is making Product polymorphic across Course, Coaching, and Download types while separating Pricing Plan as a distinct entity with a many-to-one relationship, treating Enrollment as a first-class entity that represents the unit of access.

Now I'm mapping the root containers and access primitives across platforms. Each system has a different "thing you pay for"—Skool uses Group, Kajabi uses Site, Circle uses Community, Mighty uses Mighty Network, and Teachable uses School. The access model varies too: Skool grants access through Group Membership and Level (derived from Points), Kajabi uses Offer purchases with Contact tags, Circle uses Access Groups that unlock Spaces through paywalls, Mighty uses Plans to gate Spaces, and Teachable relies on Enrollment as the direct student-product relation. I'm starting to see the monetization primitives diverge as well, with each platform anchoring differently. subscription (member pays to join Group, period)
   - Kajabi: Offer on a Product
   - Circle: Paywall on Space/Space Group
   - Mighty: Plan
   - Teachable: Pricing Plan on Product

4. **Is the content container polymorphic or monolithic?**
   - Skool: monolithic (one Feed per Group, no room types)
   - Kajabi: polymorphic Products (Course/Community/Coaching/etc.)
   - Circle: polymorphic Spaces (Post/Chat/Event/Course)
   - Mighty: polymorphic Spaces (wider type set than Circle, including Article/Q&A/Poll)
   - Teachable: polymorphic Lectures within Courses (video/text/quiz/download)

5. **Where does the CRM / Contact layer sit?**
   - Skool: doesn't exist as a separate primitive. A User is their Membership.
   - Kajabi: Contact is *the* central primitive, separate from Student/Member. This is uniquely central.
   - Circle: Member is the primitive, Email Hub operates on Members
   - Mighty: Member with custom profile fields
   - Teachable: Student is the primitive, basic Contact/email layer

6. **How do they handle engagement loops?** Skool uses a closed system where interactions trigger points that unlock levels and features without needing external integrations. Kajabi takes a hub-and-spoke approach where user behaviors get tagged, then automations and emails fire based on those tags.

Circle uses visual event-driven workflows that trigger actions, while Mighty prescribes specific patterns through AI coaching and time-bound challenges. Teachable keeps it linear with progress tracking that leads to course completion and certificates.

7. **What's the cross-cutting orthogonal dimension?** Each platform has a different core organizing principle: Skool uses per-member-per-group levels, Kajabi relies on many-to-many tags on contacts, Circle maps many-to-many access groups to spaces, Mighty bundles everything into plans, and Teachable tracks individual student-product enrollments.

Now I'm thinking about how to present this so Ren can see the actual architecture. Given their background with SST—a capability-based graph protocol—they'll appreciate seeing which primitives each platform chose to make fundamental versus derived. Skool's notably minimal type system is actually a significant architectural decision. I should structure this by showing each platform's primitive types and their relationships, then visualize how they connect. Diagrams would really help here—something like entity-relationship diagrams for each platform so the graph structure becomes visible. understanding of the architecture, so a clear prose explanation with maybe one comparative diagram showing how each platform's type system connects would be the sweet spot — detailed enough to satisfy the technical depth without overwhelming the reader. I'm settling on a structure: detailed prose breakdown of each platform's type system and relationships, then a visual comparison at the end to let them see the architectural patterns side-by-side. I'll organize it by root container, primitive types, key relationships, and what makes each platform's graph structure distinctive. I'm mapping each platform onto Ren's tripartite framework—Spirit (identity), Space (container), and Token (capability)—to see how their type systems align with that conceptual model. I'll structure this by platform, showing their core primitives and distinctive architectural choices, then synthesize across those three dimensions at the end. I'm going to draft this in prose first rather than jumping to visuals, and I want to make sure I'm accurate about each platform's actual types rather than guessing. For Skool specifically, I'm confident about the core entities: Groups and Users form Members with roles, Posts and Comments create the feed, Points and Levels drive engagement, Courses contain modular lessons, and there's infrastructure for Events, DMs, Questions, Plugins, and Categories.

Now I'm mapping out Kajabi's structure—it's more of a platform-as-a-product builder, so Site is the root, and Product is polymorphic across Courses, Communities, Coaching, Memberships, Podcasts, Newsletters, and Downloads. There's Offers for pricing, Contacts for CRM, Tags, Pages, Pipelines for funnels, and automation through Email Sequences, Broadcasts, and Workflows. Communities might be their own Product type with Feeds, or they could use Circles—I need to be careful here since I'm not entirely certain. For Circle, I'm confident about Communities, Spaces with different types like Posts, Chat, Events, and Courses, Space Groups, Access Groups, Paywalls, and Workflows, though my notes cut off there.

Mighty Networks has a similar structure but with some distinct differences—their Spaces are typed differently (Activity, Chat, Events, Q&A, Polls, Articles, Courses, Livestream), and they have first-class Articles, Questions, Polls, and Events with RSVP. They also support Challenges as time-bound experiences, Plans for access and billing, Bundles, and an AI Cohost feature. Teachable takes a different approach with Schools as the root, polymorphic Products for Courses, Coaching, and Digital Downloads, and Pricing Plans that can be configured in multiple ways.

I'm feeling solid on the overall structure now—some of the finer details around Kajabi's community setup are a bit fuzzy, but the high-level architecture is clear. Time to write this up in a way that's substantial but concise, and I should probably include a unified visual comparison at the end to tie everything together. Since the user explicitly asked for ultrathink, they're expecting depth, so I can go longer here without worrying too much about brevity.

For the visual, I'm torn between showing individual ER diagrams for each platform versus one unified diagram that highlights how different systems solve the same problems differently. The individual approach is more structurally honest and makes it easier to compare the actual graph shapes across platforms. I'll go with five compact ER diagrams arranged in a grid, each showing the core primitives and how they connect.

Building the SVG layout... I'm leaning toward five compact mini-diagrams to show the actual graph structure of each platform, but I'm second-guessing whether visuals are really the best vehicle here — the real insight is in the primitives and relationships themselves, so maybe I should prioritize prose and treat any visualization as secondary. Let me draft the written explanation first, walking through each platform's type system and which concepts it treats as primitive versus derived.

For Skool specifically, the architecture centers on `Group` as the root billing unit, with `User` as a global primitive and `Membership` defining the relationship between them along with role and points. The feed is deliberately minimal — just `Post` and `Comment` as the only content types, with `Like` as the engagement mechanism that feeds into a `Points` scalar, which then derives `Level` through a fixed ladder.

Beyond the core feed, there's a structured learning path through `Course` → `Module` → `Lesson`, calendar `Event`s, cross-group `DM`/`Chat` between users, and administrative layers like `MembershipQuestion` gates and `Plugin` toggles. `AffiliateLink` tracks referral attribution as a User↔Group edge.

The key insight is that Group functions almost as an isolated island — everything except the global User is scoped to exactly one Group, which is why the per-group billing model works so cleanly.

There's exactly one Feed per Group with no rooms or channels; categories are just metadata on Posts. `Level` unlocks act as the orthogonal access control — admins can gate a Course behind a Level requirement, and a Member's derived Level determines what they see. Monetization is straightforward: `Membership.paid = true` opens the entire Group, no per-space paywalls or multi-tier pricing within a single Group. The engagement loop itself is baked into the type system — `Like → Points → Level → Unlock` — with no configurable workflow layer on top. This is the most minimal type system of the five platforms I'm comparing.

The platform has no CRM primitive, no Workflow primitive, no Space primitive. Moderation, automation, and segmentation either don't exist or get outsourced to plugins that call out to Zapier. The entire engagement logic is locked inside that one derivation chain.

Now I'm looking at Kajabi. The root is `Site` — the billing unit with its own domain, branding, and theme. The key primitives are `User` for admins, `Contact` as a first-class CRM record that exists independently of any purchase the moment someone opts into a Form, and `Tag` for many-to-many labeling on Contacts. `Product` is polymorphic with subtypes like `Course` and `Community`.

`Offer` is the monetization atom — a specific purchasable configuration attached to a Product, so a single Course can have multiple pricing options. Then there's `Page` for landing and sales pages, `Pipeline` as an ordered funnel of Pages, Emails, and Automations, plus `Email`, `EmailSequence`, and `Broadcast` for messaging. `Automation` handles trigger/condition/action rules, and `Form` or `OptIn` creates a Contact when someone submits.

Looking at the internal structure, `Course` breaks down into `Category` and `Lesson` with polymorphic lesson types like video, audio, text, quiz, or file. `CoachingProgram` has `Session`, `Appointment`, `IntakeForm`, and `Milestone`. `Community` contains internal circles, posts, and comments. `Membership` acts as a wrapper that grants access to other Products.

The key relationships are that `Contact` sits at the center — everything operates on Contacts. `Product` and `Offer` have a one-to-many relationship, cleanly separating what you teach from how you sell it. `Contact` and `Product` connect many-to-many through Offer purchases.

`Tag` is the segmentation layer that cuts across everything — Automations read and write Tags, Pipelines use them as gates, and Emails target by Tags. Community is actually a Product subtype, not the root. The flow goes funnel → purchase → access, and community is just one of several things you can purchase. The distinctive choice here is separating `Contact` from `Member` — most platforms merge them, but Kajabi's CRM-first approach means everyone starts as a Contact, some purchase Offers to access Products, which may include Community. That's why the email and automation layer is so robust.

Now looking at the Circle structure, `Community` is the billing unit, and I'm seeing `Member` and `User` as the primitives... Events live inside EventSpaces with RSVP and native livestream capabilities, while Workflows function as first-class visual automation primitives with trigger-condition-action logic. AIAgents are trained on community content, there's an Email Hub managing broadcasts and campaigns, and Members can be tagged for segmentation. The whole system connects through a three-layer containment model (Community → SpaceGroup → Space), but AccessGroups sit orthogonally to this hierarchy—a Member can belong to multiple AccessGroups, each controlling which Spaces they can access.

Paywalls attach directly to AccessGroup membership rather than abstract tiers, so you're monetizing specific Space access. Workflows run natively as graphs with triggers from Member events, Posts, Space joins, and time-based schedules. Courses are just a Space variant, which keeps the design clean without a separate classroom concept. What makes this architecture distinctive is that Spaces are polymorphic while AccessGroups operate independently—these two axes create a much denser graph than competitors, letting you layer free intro areas, paid inner circles, and VIP tiers all within the same structural framework.

Mighty Networks roots everything in the `MightyNetwork` billing unit, with Hosts and Members as the core roles, plus SpaceHost for granular Space-level permissions. Spaces here are more specialized—ActivityFeed, ChatSpace, EventSpace, QASpace, PollSpace, ArticlesSpace, CourseSpace, and LivestreamSpace—and content types like Articles, Questions, Polls, Events, and Livestreams are elevated to first-class primitives rather than being nested under Posts.

The platform also introduces Courses with a hierarchical structure of Sections and Lessons, Challenges as time-boxed cohort-based variants, and Plans as the core monetization primitive that bundles access to specific Spaces—similar to Circle's AccessGroups but directly tied to billing. Members can also be packaged into Bundles, profiles support custom fields, and there's an AICohost concept following a Community Design pattern. monthly themes, weekly events, daily questions)
- `ReferralProgram` — built-in member referral mechanic

**How they connect:**
- `MightyNetwork → Space (typed) → content (also typed)`. More granular content typing than Circle.
- `Plan ↔ Space` is many:many. One Plan can grant access to many Spaces; one Space can be unlocked by many Plans.
- `Plan` conflates access and billing. Where Circle separates `AccessGroup` (access) from `Paywall` (billing), Mighty fuses them into `Plan`.
- `Challenge` is a specific composition pattern — it's a Space with a time axis, cohort semantics, and daily delivery.
- The Community Design™ methodology is essentially a prescribed composition of these primitives: Plans should bundle Feed Spaces, Weekly Event Spaces, Daily Question Spaces, and Course Spaces organized around Monthly Themes.

**Distinctive structural choice:** Mighty has a richer vocabulary for content types—Articles, Posts, Questions, and Polls are all distinct—and treats `Plan` as a unified billing-and-access primitive rather than separating them. The platform actively promotes Community Design as a methodology, essentially codifying a specific composition pattern into best practice.

**Teachable**

**Root:** `School` — billing unit.

**Primitives:**
- `User` / `Student` / `Admin`
- `Product` — polymorphic: `Course`, `CoachingProduct`, `DigitalDownload`
- `PricingPlan` — attaches to a Product, many:1

. Types: Free / OneTime / Subscription / PaymentPlan
- `Bundle` — packages multiple Products as one offer
- `Membership` — subscription wrapper granting access to Products
- `Enrollment` — the Student ↔ Product access edge. **First-class** — this is Teachable's access primitive.
- Course internals: `Section` → `Lecture` (polymorphic: video, text, quiz, PDF, file)
- `Quiz` — graded, attaches to Lectures
- `Certificate` — issued on Enrollment completion
- `SalesPage` / `CheckoutPage` per Product
- `Coupon`
- `Affiliate` — a User referring Products

Now I'm mapping out Teachable's core primitives. The key insight is that `Enrollment` is the first-class access primitive—it's the direct Student-to-Product relationship. Pricing is flexible with multiple plan types, and the platform supports polymorphic Products and Lectures. Certificates and Affiliates round out the ecosystem for completion tracking and referral mechanics.

I'm also considering the structural hierarchy: Schools contain Products, which contain Sections and Lectures. Memberships and Bundles are separate entity types because they affect billing constraints differently—specifically, the Published Product Limit only counts individual Products, not these wrapper types. This separation lets Teachable enforce plan-based constraints while still allowing flexible packaging options.

Community features feel bolted on rather than integral to the design—there's no dedicated Space type or Feed primitive, just threaded discussions attached to content. The real architectural strength here is how cleanly Enrollment serves as the single access primitive, with progress and completion state living directly on it. That's the most LMS-like approach of the bunch, though it comes at the cost of having a thinner community layer.

Now I'm mapping out how these platforms differ across their fundamental structural choices. The root container—the billing scope—varies significantly: Skool uses Groups (multiple per account with per-group pricing), Kajabi uses a single Site per account, Circle and Mighty Networks are built around a single Community or Network per plan, and Teachable uses Schools as the top-level container.

Skool's per-Group billing model is unusual because it fragments the type graph—every logically separate thing needs its own billing unit, but that keeps each Group's schema lean. The bigger differentiator though is whether the content container itself is polymorphic. Skool doesn't have this at all, just a single feed. Kajabi only gets polymorphism at the Product level. Circle and Mighty both support multiple Space subtypes, with Mighty going deeper by treating Article, Q&A, and Poll as distinct primitives rather than variations. Teachable sits in the middle with polymorphic Lectures within Courses. This polymorphism question is actually the single biggest architectural split between them.

Looking at how access is modeled, each platform takes a different approach. Skool uses a Level primitive derived from Points earned within a Group—access is behavioral, earned through engagement. Kajabi ties it to Purchases of Offers that unlock Products, with Tags layered on for segmentation. Circle uses AccessGroups as an orthogonal set-membership model. Mighty fuses access with billing through Plans. Teachable keeps it atomic with Enrollments as direct Student-to-Product edges. Circle's approach is the cleanest from a permissions standpoint, Skool's is the most engagement-driven, and Teachable's is the most straightforward transactionally.

On the CRM question, only Kajabi truly separates the layers by making Contact a first-class primitive above Member. Skool conflates User and Member entirely. Circle and Mighty have partial CRM capabilities—Circle's Email Hub can reach external subscribers, Mighty allows custom profile fields on Members, and Teachable has a basic contact layer beneath the Student primitive. This structural choice in Kajabi is what sets it apart.

For automation, the platforms diverge significantly. Skool has no native automation, relying on Zapier and webhooks. Kajabi offers Automation rules that operate on Tags. Circle treats Workflow as a first-class visual graph primitive. Mighty provides prescribed automation patterns plus AICohost, with integrations handling the rest.

Looking at engagement loops, I'm noticing a split between closed and open systems. Skool and Teachable both close their loops, but for different reasons—Skool around gamified mechanics like Points and Levels, Teachable around the linear course progression from enrollment to completion. Kajabi, Circle, and Mighty all keep their loops open, allowing behavior to trigger automations or workflows that can lead anywhere rather than following a predetermined path.

Now I'm mapping these platforms onto the Spirit/Space/Token framework. Every platform has some notion of user identity, but only Kajabi actually separates a public-facing Contact from a scoped Member within the system. For Space, Skool is monolithic with just one Group-as-feed, while Circle and Mighty offer typed Spaces. Kajabi and Teachable have container-like structures in their Products and Courses, though Teachable's isn't really social. Token—the capability layer—is where the real differentiation starts to emerge.

Looking at how each platform handles capabilities, they're all over the map. Skool uses Levels as earned scalar tokens, Kajabi's Tags are more like imperatively-manipulated labels through Automations rather than declarative capabilities, Circle's AccessGroups come closest to a real capability primitive with named rights on Spaces, Mighty conflates capability with billing through Plans, and Teachable treats Enrollment as a one-to-one non-transferable access token. If I were to impose a capability-graph discipline on these systems, Circle's structure would map most cleanly—Spaces as containers, AccessGroups as capability sets, Paywalls as the events that grant access. Skool would need the most restructuring.

Now I'm weighing whether a visual would actually help here. The response is already quite substantial and structural, so maybe one clean comparison grid showing all five platforms across the key axes would be genuinely useful rather than overwhelming. A single matrix is probably cleaner than five separate ER diagrams.

Actually, I keep second-guessing myself on this. Let me just commit to the prose approach — the question is fundamentally about type systems, which are best explained through clear type listings and structural descriptions rather than diagrams that risk oversimplifying the nuance. I'll offer to diagram specific platforms if they want to dig deeper.

Now I'm reviewing the draft for clarity and conciseness. I need to tighten up the SST framing so it doesn't come across as condescending, eliminate any redundancy between the individual platform breakdowns and the synthesis section, and cut anything that doesn't pull its weight.# The type systems, platform by platform

Each of these is a typed graph underneath the UI. The real insight is seeing which concepts each one elevates to primitive status, which it derives, and which it collapses. Skool's feature minimalism becomes much more legible next to these.

## Skool

**Root:** `Group` — billing unit, scope for almost everything.

**Primitives (inside a Group unless noted):**
- `User` — global identity
- `Membership` — the User↔Group edge with a role (owner/admin/moderator/member) and a per-group `Points` scalar
- `Post` — single content type in the feed, tagged with a `Category`
- `Comment` — shallow replies
- `Like` — User→Post/Comment; each Like on your content increments the author's per-group Points
- `Points` — per-member-per-group scalar
- `Level` — *derived* from Points via a fixed 1–9 ladder
- `Course` → `Module` → `Lesson` (tree, lives in Classroom)
- `Event` — Calendar item
- `DM` / `Chat` — between Users, cross-group
- `MembershipQuestion` — up to 3 pre-join gates
- `Plugin` — admin toggle on a Group (AutoDM, Zapier, pixels, etc.)
- `AffiliateLink` — attributed User↔Group edge

**How they connect:**
- Group is almost an island. Aside from User and DMs, everything is scoped inside exactly one Group. This is why per-group billing works cleanly — each Group is structurally a near-isolated subgraph.
- **Exactly one Feed per Group.** No rooms, no channels. Categories are metadata on Posts, not containers.
- `Level` is the single orthogonal access axis: a Course can require Level 3, and a Member's derived Level gates it.
- Monetization is flat: `Membership.paid = true` grants access to the whole Group.
- The engagement loop is hard-coded in the types: `Like → Points → Level → Unlock`. No user-configurable workflow layer.

**Distinctive choice:** smallest type system of the five. No Space primitive, no CRM primitive, no Workflow primitive. The whole engagement logic is closed inside one derivation chain.

## Kajabi

**Root:** `Site` — billing unit, with domain, branding, theme.

**Primitives:**
- `User` — admin/owner
- `Contact` — **first-class CRM record, orthogonal to any purchase.** Exists from opt-in. This is the central hub.
- `Tag` — many:many labels on Contacts
- `Product` — **polymorphic**: `Course`, `Community`, `CoachingProgram`, `Membership`, `Podcast`, `Newsletter`, `DigitalDownload`
- `Offer` — a purchasable configuration attached to a Product (one-time, subscription, payment plan). Many Offers per Product.
- `Page` — landing / sales / website
- `Pipeline` — funnel: a graph of Pages + Emails + Automations
- `Email` / `EmailSequence` / `Broadcast`
- `Automation` — trigger/condition/action rules operating on Tags
- `Form` / `OptIn` — creates a Contact
- Subtype internals: Course → Category → polymorphic Lesson; Coaching → Session/Appointment/IntakeForm; Community → internal spaces/Posts

**How they connect:**
- `Contact` is the hub. Products, Emails, Automations, Pipelines all operate on Contacts.
- `Product ↔ Offer` is 1:many — clean separation of "what you teach" vs "how you sell it."
- `Contact ↔ Product` is many:many via Offer purchases.
- `Tag` is the cross-cutting segmentation primitive. Automations read/write tags; Pipelines gate on them; Emails target them.
- Community is *a Product subtype* alongside Course and Coaching.

**Distinctive choice:** `Contact` is split from `Member`/`Student`. Most platforms conflate them. Kajabi's model is CRM-first — everyone is a Contact, some purchase Offers, which grants access to Products. This is why the email/automation layer is thick and why Kajabi feels marketing-first.

## Circle

**Root:** `Community` — billing unit.

**Primitives:**
- `Member` (+ `User` as global identity)
- `Space` — **polymorphic typed container**, subtypes: `PostSpace`, `ChatSpace`, `EventSpace`, `CourseSpace`, `MembersSpace`, `ImagesSpace`
- `SpaceGroup` — a folder of Spaces in the sidebar
- `AccessGroup` — a named set of Members with defined Space permissions, **orthogonal to Spaces**
- `Paywall` — attaches to a Space or SpaceGroup; purchase grants AccessGroup membership
- `Course` (inside CourseSpace) → `Section` → `Lesson`
- `Event` (inside EventSpace) with RSVP, native livestream
- `Workflow` — visual automation graph (trigger → condition → action), first-class
- `AIAgent` — trained on Community content
- Email Hub: `Broadcast`, `Campaign`, `Automation`
- `Tag` on Members

**How they connect:**
- `Community → SpaceGroup → Space → content`. Three-layer containment tree.
- `AccessGroup` is **orthogonal** to the tree. A Member can be in multiple AccessGroups; each grants/denies access to specific Spaces. Cleanest access primitive of the five.
- `Paywall` binds payment to AccessGroup membership. You don't paywall "a tier" — you paywall *access to specific Spaces via AccessGroups*.
- `Workflow` is a first-class graph in-platform, not a Zapier escape hatch.
- `Course` is just a Space flavor — no separate "classroom" concept.

**Distinctive choice:** Space is polymorphic *and* AccessGroup is orthogonal. The two axes together make the graph much denser than Skool's. "Free intro area / paid inner circle / VIP mastermind" is three AccessGroups cutting across the same Space tree — no need for three Communities.

## Mighty Networks

**Root:** `MightyNetwork` — billing unit.

**Primitives:**
- `Host` / `Member` — Host is the owner-side role
- `SpaceHost` — role scoped to a single Space (orthogonal to global Host)
- `Space` — polymorphic, **wider type set than Circle**: `ActivityFeed`, `ChatSpace`, `EventSpace`, `QASpace`, `PollSpace`, `ArticlesSpace`, `CourseSpace`, `LivestreamSpace`
- **Content types elevated to primitives:** `Post`, `Article`, `Question`, `Poll`, `Event`, `Livestream`. Article is *not* a Post — distinct type, different editor.
- `Course` → `Section` → `Lesson`
- `Challenge` — a time-boxed, cohort-based Space variant with daily delivery. First-class.
- `Plan` — the monetization + access primitive fused. Buying a Plan grants access to a configured set of Spaces.
- `Bundle` — packaged Plans
- `MemberProfile` — with custom profile fields (not a fixed schema)
- `AICohost` — assistant following Community Design patterns
- `ReferralProgram`

**How they connect:**
- `MightyNetwork → Space (typed) → content (also typed)`. More granular content typing than Circle.
- `Plan ↔ Space` is many:many. One Plan unlocks many Spaces; one Space can belong to many Plans.
- `Plan` **conflates access and billing** — where Circle separates AccessGroup from Paywall, Mighty fuses them.
- `Challenge` is a specific composition: Space + time axis + cohort semantics + daily delivery.
- Community Design™ is essentially a *prescribed composition* of these primitives: "your Plan should include a Feed + Weekly Event + Daily Question + Course Space, structured around Monthly Themes."

**Distinctive choice:** richer content-type vocabulary (Article ≠ Post ≠ Question ≠ Poll) and `Plan` as a fused billing+access primitive. The platform also ships an *opinion* about how you should compose these types, promoted to methodology.

## Teachable

**Root:** `School` — billing unit.

**Primitives:**
- `User` / `Student` / `Admin`
- `Product` — polymorphic: `Course`, `CoachingProduct`, `DigitalDownload`
- `PricingPlan` — attaches to a Product, 1:many. Types: Free / OneTime / Subscription / PaymentPlan
- `Bundle` — packaged Products
- `Membership` — subscription wrapper granting access to Products
- `Enrollment` — **first-class Student↔Product access edge**. Progress, completion, certificate eligibility all live on it.
- `Section` → `Lecture` (polymorphic: video, text, quiz, PDF, file)
- `Quiz` — graded, attaches to Lectures
- `Certificate` — issued on Enrollment completion
- `SalesPage` / `CheckoutPage`
- `Coupon`
- `Affiliate`
- Basic `Community` — lightweight threaded discussions
- `Email` / `EmailCampaign`

**How they connect:**
- `School → Product → Section → Lecture`. Clean LMS tree.
- `Product ↔ PricingPlan` is 1:many — the same Course can be sold free, one-time, and subscription simultaneously.
- `Enrollment` is *the* access atom. One per Student×Product.
- `Published Product Limit` (a plan-enforced billing constraint) counts Products but **not** Memberships or Bundles — that's why those are structurally separate types: they're composition primitives, not content primitives.
- Community is structurally thin: no Space type, no Feed primitive, no engagement graph.

**Distinctive choice:** `PricingPlan` is cleanly separated from `Product`; `Enrollment` is the single access primitive with first-class state. Cleanest LMS typing of the five, but community is an afterthought.

---

# Synthesis: six orthogonal axes

**1. Billing scope (root container).** Skool: per-Group (multi per account). Kajabi/Circle/Mighty/Teachable: per-root (one per plan). Skool's per-Group model keeps each subgraph small but forces every logical separation into a separate billing unit.

**2. Is the content container polymorphic?** Skool: **no** (one feed, no Space type). Kajabi: at the Product level only. Circle: yes (6 subtypes). Mighty: yes, richer (8+ subtypes; Article/Q&A/Poll elevated). Teachable: partial (polymorphic Lecture inside Course). This is the single biggest architectural difference — Skool is the only platform without a typed container primitive.

**3. Access primitive.** Skool: `Level` (scalar, derived from behavior). Kajabi: Offer-purchase → Product-access, with Tag as segmentation overlay. Circle: `AccessGroup` (orthogonal set-membership). Mighty: `Plan` (fused with billing). Teachable: `Enrollment` (atomic Student↔Product edge). Circle's is the most orthogonal; Skool's is the most behavioral (earned, not purchased); Teachable's is the most atomic.

**4. CRM layer separate from membership?** Only Kajabi elevates `Contact` to first-class above Member/Student. Everyone else conflates them to some degree. This is Kajabi's defining structural choice and why its email/automation layer is so thick.

**5. Automation primitive.** Skool: none internal (Zapier only). Kajabi: Automations on Tags. Circle: `Workflow` (visual graph, first-class). Mighty: prescribed patterns + AICohost + Zapier. Teachable: minimal. Only Circle has a real in-platform workflow graph as a first-class type.

**6. Engagement loop — closed in the types or open?** Skool: **closed** around gamified engagement (`Like → Points → Level → Unlock`). Teachable: **closed** around linear completion (`Enroll → Progress → Complete → Cert`). Kajabi / Circle / Mighty: **open** — trigger/action graphs the creator wires up. Skool and Teachable close their loops for opposite reasons; the others expose the loop as configurable.

---

# One framing you'll see anyway

Since it maps onto the Spirit/Space/Token distinction — each platform handles the three axes unevenly:

- **Identity.** Every platform has User/Member. Only Kajabi splits this into Contact (public-facing identity) vs Member (scoped-within-container).
- **Container.** Skool has only Group-as-container (monolithic). Circle and Mighty have typed polymorphic Spaces. Kajabi's Product is container-ish. Teachable's Course is container-ish but not social.
- **Capability.** This is where they diverge most.
  - Skool's `Level` is a derived-scalar capability, *earned* not granted.
  - Kajabi's `Tag` is capability-ish but imperatively mutated by Automations.
  - Circle's `AccessGroup` is the closest to a real capability primitive — named set with defined rights, first-class membership.
  - Mighty's `Plan` conflates capability with billing.
  - Teachable's `Enrollment` is a 1:1 non-transferable access edge.

If you imposed capability-graph discipline on any of these, Circle would be the least painful refactor (Spaces as containers, AccessGroups as capability sets, Paywalls as capability-acquisition events). Skool would need the most reshaping — you'd have to introduce a Space primitive, which is precisely the thing they've explicitly chosen not to have. The minimalism isn't an oversight; it's a bet that one closed behavioral loop beats an open composable graph for the specific audience they serve.

---
**HUMAN** (2026-04-23T17:36):

I am particularly interested in how their space/group structures like

---
**ASSISTANT** (2026-04-23T17:38):

 # Space/Group structures, side by side

This is where the five platforms diverge most sharply. The container topology determines almost everything downstream — how you gate access, how you scale, how members navigate, what "switching rooms" even means.

## Skool — single-feed monolith

```
User
 └── Membership ─── Group ───────────────┐
                     │                    │
                     ├── Feed (exactly 1) │
                     │    └── Post (Category: string tag)
                     │         └── Comment
                     ├── Classroom
                     │    └── Course[]
                     │         └── Module[]
                     │              └── Lesson[]
                     ├── Calendar
                     │    └── Event[]
                     ├── Leaderboard (view over Members)
                     └── Plugins[]
```

`Group` is the *only* container. There is no sub-container primitive. Categories on Posts are **tags**, not rooms — every Post lands in the same single feed regardless of its Category, filtering is client-side. There is exactly one Classroom, one Calendar, one Leaderboard per Group.

**Connection topology:** Groups are disjoint islands. A User can be a Member of many Groups, but content, points, levels, and DMs-with-admins are all scoped to exactly one Group. Points earned in Group A are invisible in Group B. The only cross-Group object is the User identity itself (and global DMs).

**Access control inside a Group:** two axes only.
- `Membership.paid`: binary (you're in or you're not)
- `Level`: 1–9 derived scalar, used to gate individual Courses

That's it. No private sub-spaces. No member tiers. No "VIP room."

**Consequence:** if you want two logical spaces (a free funnel group + a paid inner-circle group), you pay for two Groups. The billing unit *is* the container. The simplicity of the type system and the per-group pricing are the same design decision seen from two angles.

---

## Circle — typed Spaces inside SpaceGroups, with orthogonal AccessGroups

```
Community
 ├── SpaceGroup[]                    (sidebar folder)
 │    └── Space[]                    (typed container)
 │         ├── PostSpace    → Post → Comment
 │         ├── ChatSpace    → Message (real-time)
 │         ├── EventSpace   → Event → RSVP
 │         ├── CourseSpace  → Section → Lesson
 │         ├── MembersSpace → (directory view)
 │         └── ImagesSpace  → Image
 │
 └── AccessGroup[]                   ← ORTHOGONAL TO THE TREE
      ├── Member[]                   (set membership)
      └── Paywall[] → grants AccessGroup on purchase
```

Three-level containment tree: `Community → SpaceGroup → Space`. A Space is the typed leaf — it *is* a post feed or *is* a course or *is* a chatroom; it cannot be mixed.

The critical structural move: **`AccessGroup` is not in the tree.** It's a parallel primitive — a named set of Members. Each Space declares which AccessGroups can view/post/comment. A Member can belong to many AccessGroups simultaneously.

**What this gives you:**
- A Member can be in "Free Intro" and "Paid Cohort" and "VIP Mastermind" at once, each unlocking a different subset of Spaces.
- A Paywall is an *acquisition event* for an AccessGroup — purchase → join AccessGroup → gain access to Spaces granted to that group.
- Access and content structure are completely decoupled. You can re-tier your community without restructuring your Spaces.

**Access axes:** three, and orthogonal. Tree position (which SpaceGroup/Space), AccessGroup membership, and per-Space role (admin/moderator/member).

**Consequence:** "free funnel + paid inner-circle + VIP" is *one* Community with three AccessGroups and, say, eight Spaces partitioned across them. One billing unit. One navigation sidebar. Circle's model is the densest — and the most refactor-friendly when your business model changes.

---

## Mighty Networks — typed Spaces composable into Plans

```
MightyNetwork
 ├── Space[]                         (polymorphic, richer typing)
 │    ├── ActivityFeed   → Post
 │    ├── ChatSpace      → Message
 │    ├── EventSpace     → Event
 │    ├── QASpace        → Question (distinct type)
 │    ├── PollSpace      → Poll     (distinct type)
 │    ├── ArticlesSpace  → Article  (distinct from Post)
 │    ├── CourseSpace    → Section → Lesson
 │    ├── LivestreamSpace
 │    └── Challenge      (time-boxed + cohort semantics)
 │
 └── Plan[]                          (billing + access, FUSED)
      └── includes Space[]           (many-to-many)
```

Flatter than Circle — no SpaceGroup layer in the tree. Spaces live directly under the Network. But the content type vocabulary is **wider**: an Article is not a Post, a Question is not a Post, a Poll is not a Post. Each has its own editor, its own interaction semantics, its own Space type.

The access primitive is `Plan`, and it is **fused** with billing. A Plan is simultaneously "what the Member pays for" and "which Spaces the Member can enter." Plans are many-to-many with Spaces: one Plan can include multiple Spaces; one Space can belong to multiple Plans.

**Access axes:** two. Plan membership + per-Space role. `SpaceHost` is a role scoped to a single Space, orthogonal to network-wide Host.

**Challenge as a composed type.** Worth singling out — a Challenge is Space + time axis + cohort + daily delivery, fused into one primitive. Mighty elevates this because their "paid challenge → membership" funnel is a canonical pattern in their Community Design™ framework.

**Consequence:** re-tiering is cheaper than Skool (you can reshape Plans without new billing units) but harder than Circle (Plan fuses two concerns Circle separates). Mighty's richer content typing means the platform "knows" a poll from an article from a question — downstream UI, notifications, and analytics can specialize per type.

---

## Kajabi — Products as containers, Contact as the hub

```
Site
 ├── Contact[]                       ← HUB (CRM identity, orthogonal)
 │    └── Tag[]
 │
 ├── Product[]                       (polymorphic, each a container)
 │    ├── Course       → Category → Lesson (polymorphic)
 │    ├── Coaching     → Session / Appointment / IntakeForm
 │    ├── Community    → internal Spaces → Post
 │    │                    (1 on Basic/Growth, 3 on Pro)
 │    ├── Membership
 │    ├── Podcast
 │    ├── Newsletter
 │    └── DigitalDownload
 │
 ├── Offer[]                         (Product ↔ Offer is 1:many)
 ├── Page[], Pipeline[]              (sales infrastructure)
 └── Automation[]                    (operates on Tags)
```

Kajabi does not have a Space primitive at the site level. Its container is `Product`, and Product is polymorphic. A Community is *one kind of Product* — structurally it sits beside Course and Coaching, not above or below them.

Inside a Community Product there's a minimal Space substructure (a few discussion threads / topic areas), but it's shallow. Kajabi's community tree is: `Site → CommunityProduct → internal spaces → Post`.

**The critical move:** `Contact` floats above everything. A Contact exists from the first email opt-in, before any purchase. Purchases of Offers grant access to Products. `Tag` is a cross-cutting label applied to Contacts and mutated by Automations.

**Access axes:** three. Product access (via Offer purchase), Tag membership (many:many), and per-Community role.

**Consequence:** Kajabi's navigation is not "a sidebar of rooms." It's "a storefront of Products, each with its own member portal." The community feature exists but is architecturally peripheral — you can tell this from the fact that it's capped at 1–3 per plan. Kajabi assumes your primary engagement surface is email and your funnel, not a feed.

---

## Teachable — School as storefront, no real space tree

```
School
 ├── Product[]                       (polymorphic container)
 │    ├── Course        → Section → Lecture (video/text/quiz/PDF)
 │    ├── CoachingProduct
 │    └── DigitalDownload
 │
 ├── PricingPlan[]                   (attaches to Product, 1:many)
 ├── Bundle[]                        (packages Products)
 ├── Membership[]                    (subscription wrapping Products)
 │
 ├── Enrollment[]                    ← ATOMIC Student↔Product edge
 │    └── progress, completion, certificate state
 │
 └── Community (thin)                → threaded discussions per Course
```

Teachable has the **weakest space structure** of the five because it wasn't built as a community platform. There is no Space primitive, no sidebar of rooms, no feed concept. The container is `Product` (Course, Coaching, or Digital Download), and the social surface — such as it is — lives *inside* a Course as threaded discussion on Lectures.

`Enrollment` is the key primitive: one per (Student, Product) pair, carrying progress state. All access is per-Enrollment.

**Access axes:** one-ish. You are Enrolled or you aren't. Memberships and Bundles are composition primitives that generate Enrollments across multiple Products.

**Consequence:** Teachable can't *be* a community in the Skool/Circle/Mighty sense because the type system doesn't have the container for it. You have a storefront and a set of LMS trees; you don't have rooms.

---

# Lined up

| Aspect | Skool | Circle | Mighty | Kajabi | Teachable |
|---|---|---|---|---|---|
| Depth of container tree | 1 level (Group) | 3 levels (Community→SpaceGroup→Space) | 2 levels (Network→Space) | 2 levels (Site→Product) | 2 levels (School→Product) |
| Container polymorphism | none | 6 Space types | 8+ Space types | Product polymorphic | Product polymorphic |
| Content type vocabulary | Post only | per-Space type | wide (Article ≠ Post ≠ Q ≠ Poll) | per-Product type | Lecture polymorphic |
| Access ⊥ to tree? | no (tree = billing) | **yes (AccessGroup)** | partial (Plan fused w/ billing) | yes (Contact+Tag overlay) | no (Enrollment atomic) |
| Re-tiering cost | new Group (new bill) | reshape AccessGroups only | reshape Plans | reshape Offers+Tags | reshape Bundles/Memberships |
| Primary navigation metaphor | single feed + 4 tabs | sidebar of Spaces | sidebar of Spaces | storefront of Products | storefront of Products |
| Cross-space identity | none (per-Group scalar) | Member across AccessGroups | Member across Plans | Contact (global) | Student across Enrollments |

---

# The underlying structural trade

The four competitors all split **container structure** from **access structure**, though they do it differently:

- **Circle** does it most cleanly: Spaces form a tree; AccessGroups are an orthogonal set-membership layer; Paywalls are the acquisition events that move Members between AccessGroups.
- **Mighty** does it with some coupling: Plan is both access and billing, but still orthogonal to the Space tree.
- **Kajabi** does it with CRM overlay: Contact + Tag are orthogonal to the Product tree, and Offer purchases move Contacts into Product-access.
- **Teachable** barely separates them: Enrollment is nearly a 1:1 atomic edge.

Skool **fuses** them completely. The container (`Group`) *is* the billing unit *is* the scope of access *is* the scope of gamification. There is no orthogonal layer. The only sliver of orthogonality is `Level`, and it's a behavioral scalar, not a set-membership capability.

If you're thinking about this in capability terms: Circle's AccessGroup is the one primitive on this list that *behaves* like a capability set — named, grantable, revocable, orthogonal to containment, with explicit acquisition events (Paywalls). Everything else is either a tree edge (Membership, Enrollment) or an imperatively-mutated attribute (Tag, Points, Level, Plan).

That's why Circle can express "free intro + paid cohort + VIP mastermind" in a single Community with three AccessGroups cutting across one Space tree, while Skool needs three separate Groups, three separate bills, three separate feeds, three separate leaderboards, and three separate per-group Point scalars per Member — with no structural way to say "these three things are facets of one offering."

Skool's monolith is a deliberate collapse. The cost is exactly what you'd predict from the type system: every axis of variation in your business model has to be resolved by paying for another instance of the whole container.

---
**HUMAN** (2026-04-24T12:03):

Let's go in depth on this, function, design, interface, and more detailed structures

[attachment excerpt_from_previous_claude_message.txt]
Skool — single-feed monolith
User
 └── Membership ─── Group ───────────────┐
                     │                    │
                     ├── Feed (exactly 1) │
                     │    └── Post (Category: string tag)
                     │         └── Comment
                     ├── Classroom
                     │    └── Course[]
                     │         └── Module[]
                     │              └── Lesson[]
                     ├── Calendar
                     │    └── Event[]
                     ├── Leaderboard (view over Members)
                     └── Plugins[]


---
**ASSISTANT** (2026-04-24T12:06):

  The user is asking for a detailed breakdown of Skool's Group structure—how it's organized, what functions it contains, its design patterns, and the underlying data structures. Since we've been analyzing these platforms as typed graphs and the user thinks in terms of primitives and combinators, I should frame this as an architectural deep dive into how Group acts as the core monolith and what components live within it.

Rather than relying on general knowledge, I need to dig into primary sources to understand the actual mechanics: how posts are structured with their various types and attachments, how the feed handles pinning and sorting, what lesson types exist and what they contain, how events and calendar work with RSVP and integrations, the specifics of member profiles and messaging, leaderboard calculation logic, permission hierarchies, notification systems, discovery mechanisms, and the mobile implementation details. Let me pull concrete information from Skool's help documentation to map out these structures precisely.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

 I see there's a Tier concept mentioned in the course permissions — that's interesting since it might be a recent addition. Let me dig into that.
```
This block is not supported on your current device yet.
```

 So Skool actually made a major architectural shift in late 2025 by introducing five distinct pricing models—Free, Subscription, Freemium, Tiers with 2-3 paid options, and One-time purchases. This means Tiers is now a proper primitive that can gate courses and events, which fundamentally changes how access control works on the platform and validates my earlier intuition about how Skool fuses different access mechanisms together.

For the points system, I'm seeing a clear exponential progression where each level threshold roughly quadruples: Level 2 starts at 5 points, Level 3 at 20, Level 4 at 65, Level 5 at 155, Level 6 at 515, and it continues scaling up to Level 9 at 33,015—these thresholds are fixed globally across all communities. The role hierarchy is also clearer now: Owner at the top, then up to 30 Admins (with a Pro-only requirement for multiple admins), Billing Managers as a flag on admin accounts, Moderators, and regular Members, with none of the elevated roles appearing on leaderboards.

I'm also tracking that posts support text, video, GIFs, polls, links, and images, plus something called "Action Posts" and attachments, with the ability to email-broadcast posts. Categories are limited to 10 and stay flat with no nesting, and admins can enforce posting restrictions per category. For lesson content, there's support for multiple video platforms like YouTube, Vimeo, Wistia, Loom, and Bunny.net, though I'm seeing conflicting information about whether Skool hosts video natively.

Now I'm moving into the access control layer: courses can combine Level Locks, Time Unlocks for drip content, Buy Now options, and Tier restrictions—all stackable with OR logic. Events include webinars up to 10,000 participants on Pro with 14-day recording retention and tier/course-specific restrictions. Privacy-wise, groups can be public and SEO-indexable or private for members only, and course content stays locked even in public groups. There's also a unified DM and notification system across groups, custom sidebar links, and up to 3 membership questions during signup.

Now I need to synthesize all these details into a structured explainer covering function, design rationale, interface behavior, and detailed data structures for Ren.

I'm planning a layered walkthrough: starting with the Group Shell (the container, billing, privacy, identity, and branding), then moving through the Five T's—whatever those core primitives are—and drilling into each node's type, stored state, affordances, connections, UI surface, constraints, and design rationale. ab System (the main UI surfaces)**
- Community tab
- Classroom tab
- Calendar tab
- Members tab
- Leaderboards tab (+ About tab for public)

**Tier 3: Identity and Roles**
- User (global)
- Membership (User↔Group edge)
- Roles: Owner, Admin, Moderator, Member, Billing Manager
- Profile
- Member-level state: Points, Level, Tier, TimeInGroup

**Tier 4: Content Primitives**
- Post types (text, poll, video, link, GIF, image)
- Comments (threaded)
- Likes (the whole gamification atom)
- Categories (up to 10, flat)
- Pinning (per feed, per category, per course page)
- Email broadcast of post

**Tier 5: Classroom**
- Course → Module → Lesson tree structure
- Lesson content includes video, description, attachments, action items, and transcript
- Video hosting through embedded players and native Mux integration
- Per-lesson comments toggle
- Access rules with Level Lock, Time Unlock for drip content, Buy Now, and Tier gates that can be combined with OR logic

**Tier 6: Calendar**
- Events with recurrence support
- Webinar events with Zoom links or external event links
- Event access gating by tier or course completion
- RSVP functionality

**Tier 7: Leaderboards**
- Time-based rankings for 7-day, 30-day, and all-time periods
- Admins excluded from rankings
- Points-based scoring system

Now I'm mapping out the higher-tier features. Tier 8 covers direct messaging and notifications, Tier 9 is the admin control panel with settings and plugins, and then there's the orthogonal dimension of access controls—Level, Tier, one-time course purchases, and public/private flags all work independently. I should circle back to how these systems interconnect and what doesn't touch what, then think about how to present this as a dense technical reference for builders. I need to refine the type model before writing—the earlier version was incomplete. I'm adding Tier as a core primitive, expanding Membership to include role, tier, points, level, joinedAt, and status, and recognizing that Group needs PricingModel (5 variants), Privacy settings, and an About page. I also need to account for polymorphic Post and Lesson subtypes, plus multiple Roles per user.

Now I'm mapping out the complete structure: User sits at the top with global DMs and Notifications, then has Memberships per Group. Each Group is a billing unit with Branding, PricingModel variants, optional Tiers (0-3), MembershipQuestions, an AboutPage, and flat Categories for organizing posts.

Within each Group, Memberships define the User↔Group relationship with role-based permissions, optional tier assignment, points, and derived level. The Feed contains polymorphic Posts that can be text, polls, media, or links—each with category assignment, pinning, email broadcast options, and nested Comments.

Now I'm mapping out the educational and event structures: Classrooms contain Courses with access rules that combine level locks, time unlocks, purchase gates, and tier requirements. Courses have Modules containing Lessons with video, text, or embedded content plus attachments and optional Comments. There's also a Calendar system supporting both external links and native webinars (Pro tier, up to 10k attendees) with recurrence and timezone awareness, where access can be gated by tier or course completion.

The platform also includes a Leaderboard with customizable time windows, a sidebar for custom links, and a plugin ecosystem with toggles for automation features like AutoDM, Zapier integration, webhooks, pixels, moderation, instant approval, chat unlocks at L2, and video triggers.

I need to shift focus now to how users actually interact with these structures—the interface layer, how different content types render, and the design reasoning behind these architectural choices.

I'm planning to structure this as a walkthrough starting from the initial Skool experience, moving through each layer to show what's visible, what types power it, what interactions are possible, and what's intentionally absent. I'll keep it concise and scannable with clear sections, aiming for around 1800-2200 words.# Skool's Group, opened up

I'll walk through it as a layered tour — what renders on screen, what types sit behind the render, what you can do with each, what's conspicuously absent, and why the designers chose that shape. I've verified the details against current Skool docs and help articles, since the platform has shipped real structural changes in late 2025 (Tiers, native webinars, refined course access rules).

## 0. The global shell — User, Membership, the multi-Group account

When you log in, you land on a personal home that aggregates across every Group you've joined. The only global primitives are:

- `User` — identity, profile, avatar, name, bio. One per human.
- `Membership` — the `User ↔ Group` edge. This is where almost all your "state" actually lives, because **points, level, tier, and role are per-Group, not per-User**.
- `DM` — direct messages are cross-Group. You message a person, not a person-within-a-group.
- `Notification inbox` — unified across every Group you're in, sorted by recency.
- `Settings` — your global profile + password + notification prefs.

A single User can sit in hundreds of Groups. Someone at Level 7 in "Road to 10k" may be Level 1 in "Skoolers" — the counters don't cross. This is foundational: the Group is an almost-sealed world, and the User is just a passport.

## 1. The Group shell itself

A Group is the billing unit, the privacy unit, the monetization unit, and the container for everything below. Its shell-level state:

- **Identity**: name (≤30 chars), description (≤150 chars), icon, cover image.
- **URL**: `skool.com/{slug}` by default, or a custom domain on both plans.
- **Privacy**: `public` (content SEO-indexed, posts visible to Google, About page open) or `private` (content gated, About page becomes a sales page). Toggleable at any time.
- **Pricing model**: as of the late-2025 rebuild, five mutually exclusive modes — `Free`, `Subscription`, `Freemium`, `Tiers`, `OneTime`. The choice changes the signup flow and what primitives exist below.
- **Tier[]**: 0–3 tiers, each with its own price, billing cadence, benefit-description text, and set of unlocked courses/events. Tiers are new. They are the closest Skool has to an orthogonal access primitive.
- **MembershipQuestion[]**: 0–3 pre-join gates. Answers flow into Zapier if you want to route them to a CRM.
- **About page**: for private groups, this is the public sales page non-members see.

The Group has exactly **six first-class tabs**: `Community`, `Classroom`, `Calendar`, `Members`, `Leaderboards`, `About`. Admins see a seventh, `Settings`. This five-tab-plus-settings shape is the entire navigational surface of the product. There is no sidebar tree, no room list, no folder structure.

## 2. The Community tab — one feed, ten categories

This is the landing tab for members. You see a single reverse-chronological feed with a composer at top.

**The post primitive.** A `Post` is polymorphic on content but monomorphic on container. It can hold text, image, video (embedded or native), GIF, link, or poll — admins note internally that "Action Posts" are just text posts with a pinned homework prompt. Every post carries:

- `title`, `body` (plain text with links and images; no rich formatting on regular posts — this is a deliberate feature ceiling)
- `category` (exactly one)
- `pinned` flag (admin-only)
- `emailBroadcast` flag (admins can choose to email the post out when publishing)
- `Comment[]` — flat, with one level of reply nesting
- `Like[]` on Post and on each Comment

**Likes are the atom of the entire engagement economy.** When someone likes your post or comment, +1 point goes to your per-Membership counter in this Group. That's the only way points are minted. Not for posting. Not for commenting. Not for completing lessons. Only for receiving likes on things you wrote.

**Categories.** Up to 10 per Group. Flat — no nesting. Each category has its own post-permission (e.g., admin-only for "Announcements") and default sort (newest activity, newest post, top week, top month). Crucially, **categories are filters, not containers.** Every post still goes into the one Feed; a category just tags it. When you click a category, you get a filtered view of that same feed. This is why "sub-community" doesn't exist in Skool — there is only ever one stream.

**What's absent.** No channels, no group chats inside a Group, no threaded sub-rooms, no rich-text on posts, no Markdown, no reactions beyond Like, no @mentions in the classic Slack sense (you can link profiles but not ping rooms), no post scheduling, no drafts, no polls with conditional branching. The negative space is as much a design choice as the positive space.

## 3. The Classroom — a strict three-level tree

The structure is rigid: **Course → Module → Lesson**. Always three levels, never more, never fewer. The Skool UI calls these "Sets / Modules / Lessons" in some older surfaces, which creates minor confusion, but the type tree is three-deep.

**Lesson internals.** Each Lesson holds one primary content payload — a video (embedded from YouTube, Vimeo, Wistia, Loom, Bunny.net, or uploaded natively to Skool's own Mux-backed host), or text. Alongside the payload: a description field that supports timestamped links into the video, an attachments list (PDFs, files), an "action items" block, an auto-generated transcript, and a comments toggle. That's the full lesson schema.

**Course access rules — the interesting part.** Since the late-2025 rebuild, a Course can be gated by any combination of:

- `Level Lock` — requires Member's level ≥ N (1–9)
- `Time Unlock` — requires `now() - joinedAt ≥ N days` (this is Skool's drip)
- `Buy Now` — one-time purchase, Course is a product
- `Tier` — requires Membership.tier ∈ {specified tiers}

These are combinable as `(LevelLock OR Tier)`, `(TimeUnlock OR Tier)`, `(BuyNow OR Tier)`. The `OR Tier` pattern is how you let paying members skip the engagement wall a free member would hit. This is the richest access logic Skool has — and it all lives on the Course, not lower.

**What's absent.** No quizzes, no assessments, no graded work, no certificates, no enforced completion, no branching paths, no prerequisites beyond level/tier/time/buy, no peer review, no downloadable SCORM, no course-wide analytics beyond basic view counts. If you want any of those, you link out to Typeform or build it yourself.

## 4. The Calendar — events, with a new webinar primitive

An `Event` holds: title, description, datetime, timezone (auto-detected per viewer), optional recurrence, and a connection. The connection is either an external link (Zoom, Meet, anything) or, on Pro, a **native Skool Webinar** that can host up to 10,000 participants, with screen sharing, recording, and auto-posted replay. Recordings are retained for 14 days unless downloaded.

Events can be gated by `tier` or by `course` — "only VIPs can attend" or "only Module 3 completers." This is the *only* place besides the Classroom where Tier and course-membership reach into access control.

RSVP is weak — members can click "Going," but admins don't get a useful attendance dashboard. Reminders are basic and automated; no custom pre/post-event email sequences. The calendar syncs out to Google/Outlook/Apple via standard iCal subscription.

## 5. The Members tab, Leaderboards, and the role system

The Members directory is a searchable list of every Membership in the Group. For each you see: avatar, name, level, points, tier badge (if paid), location (if set), bio, and social links. Admins can filter by role, tier, or level, and can open a membership-settings popover to change role, revoke access, refund, or export.

**Role tree.** Exactly four roles, plus one flag:

- `Owner` — one per Group, cannot be transferred except on Pro ("ownership transfer" is a Pro-only feature).
- `Admin` — up to 30, Pro-only for more than 1. Full access except billing unless flagged.
- `Admin + Billing Manager` — flagged Admin who can see and manage billing.
- `Moderator` — approve/decline joins, delete reported posts and comments, invite members, run scheduled events and record calls. **No access to Classroom or Calendar settings.**
- `Member` — base role.

Owner, Admins, and Billing Managers are **excluded from the leaderboard** — so staff can't dominate the gamification ladder. Moderators are still on it.

**Leaderboards.** Three views only: `past 7 days`, `past 30 days`, `all-time`. All derived from the same Points counter. Ties are broken by earlier-reaching timestamp. The leaderboard is where the gamification loop becomes visible to everyone — and it's the one surface where Skool's points-economy is publicly competitive.

## 6. The Tier primitive (the newest layer)

Worth singling out because it changes earlier diagrams I drew. Until late 2025, a Group had essentially binary access: paid or not. Now a Membership carries an optional `tier: Tier | null` field, and up to three paid Tiers can coexist inside one Group. Each Tier has:

- `price`, `cadence` (monthly, annual, both)
- `benefits` — free-text bullets shown on the upgrade page
- `includedCourses[]`, `includedEvents[]` — the actual capability set

This is Skool's only set-membership access primitive, and it's orthogonal-ish to the Classroom tree: one Tier can unlock a subset of Courses, a Course can be unlocked by a Tier *or* by reaching a Level. But it's still not as clean as Circle's AccessGroup — a Tier is a billing SKU fused with a capability set, not a pure named capability. And a Member can only be in one Tier at a time (or Free), not multiple.

The Tier primitive also cannot reach into the Community feed. There is no way to say "this category is VIP-tier-only" — because Categories are tags on Posts in one shared Feed, and the Feed itself isn't gatable below the Group level. Access gating stops at the Classroom and Calendar boundaries.

## 7. Settings and Plugins — the admin-only surface

The Settings area is where admins configure the Group. It has tabs for General (branding, privacy, slug), Pricing (pick one of the five models and configure tiers), Membership Questions, Categories, Roles, Billing, Affiliates (both the Skool-wide commission and member referrals), Analytics (light), and **Plugins**.

Plugins are admin toggles, each a single-purpose behavior:

- `AutoDM` — one-message welcome to new members (within 1–5 min of join)
- `Zapier` — exposes API key + webhook triggers
- `Webhook` — raw POST endpoint for external systems to invite members
- `Meta Pixel`, `Google Ads`, `Hyros` — ad conversion tracking
- `AutoMod` — spam filter (recommended ≥1k members)
- `Instant Membership Approval` — skip vetting
- `Unlock Chat at Level 2` — require level to DM admins
- `Onboarding Video` — shown on first login
- `Cancellation Video` — shown on churn flow
- `Membership Questions` — (also surfaced here)

These are purely declarative toggles — no workflow engine, no branching. Each is a leaf behavior.

## 8. The complete corrected tree

With everything layered in:

```
User (global)
 ├── DMs (1:1, cross-group)
 ├── Notifications (aggregated across all Groups)
 └── Memberships[]

Group  ────── (billing unit, public|private)
 ├── Branding, customURL, AboutPage
 ├── PricingModel: Free | Subscription | Freemium | Tiers | OneTime
 ├── Tier[] (0..3) ─── price, cadence, benefits, includedCourses, includedEvents
 ├── MembershipQuestion[] (0..3)
 ├── Category[] (0..10, flat, per-cat post-permission + sort)
 ├── Membership[]       ─── User↔Group edge
 │      ├── role: Owner | Admin(+billingFlag) | Moderator | Member
 │      ├── tier: Tier | null
 │      ├── points: int             ← minted only by received Likes
 │      ├── level: derived 1..9     ← thresholds: 5/20/65/155/515/2015/8015/33015
 │      └── joinedAt, status
 ├── Feed (exactly 1)
 │      └── Post (text | image | video | gif | link | poll)
 │             ├── category, pinned, emailBroadcast
 │             ├── Comment[] (one-level nested)
 │             └── Like[] on Post and each Comment
 ├── Classroom
 │      └── Course[]  ─── accessRules: { LevelLock? | TimeUnlock? | BuyNow? | Tier? }
 │             └── Module[]
 │                    └── Lesson[]
 │                           ├── content: Video(embed|native) | Text
 │                           ├── attachments[], actionItems, transcript
 │                           └── Comment[] (toggleable)
 ├── Calendar
 │      └── Event[]  ─── external-link | nativeWebinar(≤10k on Pro)
 │             └── accessRules: tier? | course-gate?
 ├── Leaderboard (view, 7d/30d/all-time, excludes Owner+Admins+BillingMgrs)
 ├── CustomLink[] (sidebar)
 └── Plugin[] (AutoDM, Zapier, Webhook, Pixels, AutoMod, etc.)
```

## 9. The two axes of access, and what they can't do

Skool now has three quasi-orthogonal access axes inside a Group:

1. **Role** — coarse (Owner/Admin/Mod/Member), governs administrative power.
2. **Tier** — a billing-fused capability set, gates Courses and Events.
3. **Level** — a behavioral scalar, gates Courses only.

Plus two one-off gates: `TimeUnlock` (drip) and `BuyNow` (one-time purchase, Course as product).

What this system **cannot** express natively, no matter how you configure it:

- "Only VIP members see this post" — the Feed is ungated below the Group.
- "Only cohort A sees Module 3" — no cohort primitive.
- "Only my top 10 leaderboard members can DM each other" — no set-membership beyond Tier.
- "This sub-community is for advanced students" — no sub-community primitive.
- "This member belongs to Tier A *and* Tier B simultaneously" — Tier is single-valued.

Every one of these requires **a new Group**, which is a new billing line. The monolith design and the per-Group pricing are still the same decision, seen from two sides.

## 10. What this shape is actually optimized for

If you look at the type tree as a whole, three things jump out:

**The Like → Point → Level → Course-unlock chain is hardcoded through four different primitives.** Likes mint Points on Membership; Points derive Level; Level can gate a Course. That's four type connections carrying one loop. No other loop in the system gets this architectural weight. Not completion, not cohort, not purchase, not content-creation. Just receiving likes.

**The Feed is the platform's gravitational center.** It's the only truly always-on, always-visible surface. Classroom is something you navigate to when you need it; Calendar is something you check before an event; but the Feed is what opens when you tap the Group. Every other primitive is downstream of or peripheral to it.

**The whole shape flattens hard at the Group boundary.** Inside a Group, the type tree is dense and opinionated. Across Groups, there's almost nothing — no cross-group roles, no cross-group points, no cross-group content, no cross-group tiers. This isn't an engineering limitation; it's what makes the per-Group pricing model coherent. You're not buying a seat in a shared platform; you're buying an instance of a small, sealed world.

That's the real design thesis. Not "community + courses + calendar" — the bundle description is the marketing summary, not the architecture. The architecture is: a sealed, feed-gravitational world where engagement is minted by peer approval and spent on course access, sold in discrete billing units per world. The minimalism in every direction — one feed, three levels of course depth, flat categories, no rich text, no chat, no sub-spaces — serves that thesis. Each absence keeps the gravitational center of the Group on the Feed, which keeps the Like economy running, which keeps points flowing, which keeps members returning.

Once you see that, the rest of the product follows.
