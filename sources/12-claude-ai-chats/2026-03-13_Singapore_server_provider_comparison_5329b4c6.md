# Singapore server provider comparison

created: 2026-03-13T08:10:43.844667Z  uuid: 5329b4c6-ca48-445a-adb3-03bd3a8a98fa  export: old
messages: 6  total_chars: 13729  human_chars: 534

summary: **Conversation overview**

The person is researching server hosting options in Singapore to set up infrastructure for a community platform or SaaS product, with a budget under $20/month. Their priorities include low latency to China and Southeast Asia, managed services and ease of use, and full control with bare metal access. The conversation began with Claude asking clarifying questions about use case, budget, and priorities before generating a comprehensive report.

Claude produced a detailed DOCX report covering budget VPS providers (Vultr, Hetzner, Hostinger, Kamatera, DigitalOcean, Linode), hyperscaler options (AWS, GCP, Azure) in Singapore, China and SEA latency considerations, a recommended architecture stack, and a decision matrix. The initial report incorrectly stated that Hetzner Singapore includes 20 TB of bandwidth — a figure that applies only to Hetzner's EU data centers. The actual Singapore allocation is 0.5 TB.

After reviewing the report, the person asked for a focused plain-text comparison of Vultr versus Hetzner specifically. Claude corrected the bandwidth error upfront and delivered an in-depth comparison covering pricing (Vultr Cloud Compute at $12/mo with 3 TB bandwidth vs. Hetzner CPX22 at ~$9.50/mo with only 0.5 TB), compute performance (broadly comparable AMD EPYC-based VMs), network quality and China/SEA peering (Hetzner's China peering noted as weak by community reports; Vultr more established in the region), managed services ecosystem (Vultr offers managed databases and Kubernetes; Hetzner is bare infrastructure only), API and automation tooling, support quality, and a known Hetzner account rejection issue for users signing up from Asia. The final recommendation was Vultr at $12/mo, with the 0.5 TB Hetzner Singapore bandwidth limit identified as a non-starter for a user-facing community platform. The person expressed no preference for document output on the second request, preferring plain text, which Claude honored.


---
**HUMAN** (2026-03-13T08:10):

i want to setup a server in singapore, which provider should I use? give me a comprehensive report

---
**ASSISTANT** (2026-03-13T08:11):

The user wants a comprehensive report on server/cloud providers in Singapore. Let me search for current information on this topic.Let me research the current landscape of server/hosting providers in Singapore for you.
```
This block is not supported on your current device yet.
```

Let me search for more specific information about cloud providers (AWS, GCP, Azure) in Singapore, and also VPS/bare metal pricing comparisons.
```
This block is not supported on your current device yet.
```

Let me also search for budget/indie VPS providers popular with developers in Singapore, like DigitalOcean, Vultr, Hetzner, etc.
```
This block is not supported on your current device yet.
```

Now let me get info on Singapore-specific data center considerations and connectivity advantages.Before I put this together as a report, let me understand what you need so I can tailor the recommendations:
```
This block is not supported on your current device yet.
```

The user hasn't responded yet to my questions. Let me wait for their response. But actually, looking at the function result, it seems the questions were presented. I should wait for the user's actual response.

Wait, the function result just shows the questions were successfully presented. The user will respond in their next message. Let me provide context while waiting.I've gathered a lot of research on Singapore hosting providers across all tiers — from budget VPS to hyperscalers. Once you answer those, I'll build you a tailored report with specific provider recommendations, pricing comparisons, and the trade-offs that matter for your setup.

---
**HUMAN** (2026-03-13T08:47):

Q: What's the primary use case for this Singapore server?
A: Community platform or SaaS product

Q: What's your rough monthly budget?
A: Under $20/mo (lean VPS)

Q: What matters most to you? (Select all that apply)
A: Low latency to China / SEA, Managed services & ease of use, Full control & bare metal access

---
**ASSISTANT** (2026-03-13T08:50):

The user wants a Singapore server for a community platform/SaaS product, under $20/mo, with low latency to China/SEA, managed services, and full control. Let me create a comprehensive report based on my research. Let me check the skill files for creating a good document.
```
This block is not supported on your current device yet.
```

The user wants a comprehensive report. Given their requirements (community platform/SaaS, under $20/mo, low latency to China/SEA, managed services, full control), let me create a well-structured document. I'll use the docx skill to create a professional report.Let me build you a comprehensive report.
```
This block is not supported on your current device yet.
```

Let me create the comprehensive report as a docx file.
```
This block is not supported on your current device yet.
```

Let me run it.
```
This block is not supported on your current device yet.
```

Let me validate the file.
```
This block is not supported on your current device yet.
```

The file is valid. Let me present it.
```
This block is not supported on your current device yet.
```

Done. Let me give a concise summary.Here's your report. The TL;DR:

**Start with Vultr VX1 at $12/mo** — it's the best fit for a community platform under $20/mo with Singapore presence. You get 2 vCPU / 4 GB / NVMe / 3 TB bandwidth, full root access, and strong API tooling. Layer Cloudflare free tier on top for CDN and DDoS.

**Hetzner CPX22 (~$9.50/mo)** is the value runner-up — slightly better specs and 20 TB bandwidth, but more bare-bones support.

The report covers all the trade-offs in detail, including China latency considerations (which, given your Shenzhen connection, is worth reading carefully — the GFW section is relevant), a recommended architecture stack, and a decision matrix comparing all providers across your priority factors.

---
**HUMAN** (2026-03-13T10:28):

i am considering vultr and hetzner, can you comparing these two in depth? no need to generate document, just output plain text

---
**ASSISTANT** (2026-03-13T10:29):

The user wants a detailed comparison of Vultr vs Hetzner for Singapore VPS hosting. Let me search for more specific comparison data.Let me pull some more specific data on both providers in Singapore.
```
This block is not supported on your current device yet.
```

Let me get more specific data on Hetzner Singapore and the direct comparison.
```
This block is not supported on your current device yet.
```

This is very important - Hetzner Singapore only includes 0.5 TB bandwidth, not 20 TB like in Europe! This changes the comparison significantly. Let me also search for Vultr Singapore specific info.
```
This block is not supported on your current device yet.
```

Now I have a critical correction to make. In my earlier report, I stated Hetzner Singapore includes 20 TB bandwidth. But the actual Hetzner pricing page clearly states: "20 TB of inclusive traffic for cloud servers at EU locations, 1TB in US locations and 0.5 TB in Singapore." This is a HUGE difference. Let me compile the comparison now.Okay, here's the deep dive. And I need to correct something important from the earlier report first.

---

**Critical correction: Hetzner Singapore bandwidth is 0.5 TB, not 20 TB.** The 20 TB figure only applies to EU data centers. Hetzner provides at least 20 TB of inclusive traffic for cloud servers at EU locations, 1 TB in US locations, and only 0.5 TB in Singapore. This completely changes the calculus. I apologize for the error in the earlier document — I conflated their EU and Singapore tiers.

---

**Pricing (apples to apples)**

Hetzner's Singapore offering uses the CPX (Regular Performance) line with AMD EPYC processors. The new structure has three tiers: Cost-Optimized, Regular Performance, and Dedicated General Purpose, but Cost-Optimized and ARM64 series are only available in EU regions. So in Singapore you're limited to CPX (shared) or CCX (dedicated) plans.

The CPX22 (3 vCPU / 4 GB / 80 GB NVMe) is currently €5.99/mo but rises to €7.99/month (~$9.50) from April 1, 2026, with increases of up to 37% across all plans due to rising DRAM and NAND flash costs.

Vultr's comparable option is the Cloud Compute Regular Performance at $12/mo for 2 vCPU / 4 GB / 80 GB NVMe / 3 TB bandwidth. Their newer VX1 tier starts at $43.80/mo for 2 vCPU configurations — so for your budget, it's actually the regular Cloud Compute line, not VX1. VX1 General Purpose and Memory Optimized plans start at $43.80/month, which is well over your $20 ceiling. (I oversimplified this in the report — the $12 VX1 plans are the smaller CPU-only tiers.)

So the real comparison is: Hetzner CPX22 at ~$9.50/mo (3 vCPU / 4 GB / 0.5 TB bandwidth) vs. Vultr Cloud Compute at $12/mo (2 vCPU / 4 GB / 3 TB bandwidth). Hetzner gives you an extra vCPU core for $2.50 less, but Vultr gives you **six times the bandwidth**.

---

**Bandwidth — the dealbreaker**

This is where Hetzner Singapore falls apart for a community platform. Half a terabyte per month is roughly 16 GB/day. For a SaaS or community app serving images, API calls, and page loads to active users, you can blow through that surprisingly fast. Users on LowEndTalk noted the 1 TB limit as the biggest gripe, saying at least 2-3 TB would make more sense for the price. And that was someone quoting the older 1 TB figure — the current Singapore allocation is even lower at 0.5 TB.

Hetzner charges extra per TB of overage in Singapore (pricing varies but is meaningfully higher than EU overage rates because Asian transit is expensive). Community members confirmed that traffic in Asia is costly due to undersea cable installation and maintenance expenses.

Vultr includes 3 TB at the $12/mo tier, and egress bandwidth beyond included allocations is priced at a consistent $0.01/GB worldwide. That's $10/TB for overage, which is predictable and not punitive.

---

**Compute performance**

Hetzner Singapore runs AMD EPYC-Rome processors. Vultr's Singapore Cloud Compute also uses AMD EPYC (Rome or newer depending on which node you land on). Testing showed Vultr Singapore delivering I/O speeds consistently above 1 GB/s, peaking at 1.4 GB/s, with a Geekbench 6 single-core score of 1543 and multi-core of 2675.

Hetzner's CPX22 benchmarks from EU show similar-class performance (AMD EPYC-Rome at ~2445 MHz). The extra vCPU on Hetzner's plan gives it an edge in multi-threaded workloads, but single-core performance (which matters most for web request latency) is comparable between the two.

Both use NVMe SSD storage with KVM virtualization. Neither is meaningfully faster than the other for typical web/database workloads. This is basically a wash.

---

**Network quality and China/SEA latency**

This is where things get nuanced and neither provider is clearly superior.

Hetzner Singapore runs on their own servers inside third-party data centers. They operate Hetzner Cloud products in Singapore on Hetzner's own servers in third-party data centers. Their peering in SEA is decent but not exceptional. Community tests showed that Hetzner's peering within APAC, especially around SEA, was not as strong as providers like SG.GS that have private network interconnects with regional carriers. Specifically, users noted that peering to China from Hetzner Singapore was "really bad."

Vultr has been in Singapore longer and has more established peering relationships. Benchmarks showed strong APAC throughput of 4+ Gbits/sec to Singapore, indicating Vultr's peering extends meaningfully into the region. That said, for mainland China audiences, Singapore won't be optimal from either provider due to Great Firewall routing complexities. Neither offers CN2 or China-optimized transit at these price points.

For your users in Vietnam and broader SEA, both will deliver similar latency (low tens of milliseconds). For Shenzhen/Guangzhou specifically, expect 40–80ms from either, routing through Hong Kong. Neither provider offers a meaningful advantage for China connectivity — that's a problem you solve with Cloudflare or a China-specific CDN layer, not with the origin server choice.

---

**Managed services and ecosystem**

Vultr has a more developed ecosystem around its compute core. Managed Databases including MySQL, PostgreSQL, Valkey, and Apache Kafka are available, with plans starting at $15/month for PostgreSQL. They also offer managed Kubernetes, load balancers, object storage, and a marketplace with one-click apps.

Hetzner keeps things minimal. You get Load Balancers, Volumes (block storage), Firewalls, and Floating IPs. No managed databases, no object storage, no app marketplace. Their philosophy is to provide excellent raw infrastructure cheaply and let you manage everything yourself. For developers comfortable managing their own infrastructure, this isn't a dealbreaker, but many teams have concluded that managing database replication, backup rotation, OS patching, and security hardening is not the best use of their time.

For a community platform, this matters. If you want to eventually add a managed PostgreSQL instance rather than running it yourself, Vultr can do that. Hetzner can't.

---

**API and automation**

Both have solid APIs and Terraform providers. Vultr's API is more mature with better documentation and broader coverage of their service catalog. Hetzner's `hcloud` CLI and API are clean and well-designed but cover fewer services (because there are fewer services). Both support cloud-init for automated provisioning.

Vultr's panel balances simplicity with enough operational control to manage production infrastructure without relying heavily on external tooling. Hetzner's console is similarly clean — fast, minimal, visually uncluttered, with every common operation within two or three clicks.

Both provision instances very quickly. Vultr claims under 60 seconds; Hetzner is similarly fast.

---

**Support**

This is where Vultr pulls ahead, though neither is great at this price tier. Vultr has ticket-based support with generally responsive times. Users report that support is good, responsive, and quick to respond to inquiries. However, some users have experienced hardware issues where support was initially unhelpful, pointing to resources rather than proactively fixing problems.

Hetzner is ticket-only, no phone, no live chat. Response times are decent for EU business hours but can lag if you're in an Asian timezone. For developers who never need support and are comfortable managing everything themselves, Hetzner remains hard to beat on price; for everyone else, the hidden costs emerge during the first real incident.

---

**Account creation quirk (Hetzner)**

Worth mentioning: Hetzner is known for rejecting new accounts, especially from users in Asia. Users who had accounts rejected were advised not to use VPN/proxy during signup and to ensure information matches ID and payment details. This can be a frustrating onboarding experience. Vultr has no such reputation — signup and deployment is straightforward with credit card or PayPal.

---

**Bottom line**

For a community platform under $20/mo serving SEA and China users:

**Go with Vultr at $12/mo.** The 0.5 TB bandwidth limit on Hetzner Singapore is a non-starter for any platform with real users. You'd blow through it within weeks and start paying overage that erases the price advantage. Vultr's 3 TB gives you six times the headroom, the managed services give you a growth path, the support is better, and the peering quality in SEA is at least as good. The $2.50/mo premium over Hetzner buys you dramatically more usable infrastructure.

**Hetzner Singapore makes sense for** a dev/staging server, a personal tool, or a workload with minimal egress (like an internal API or cron job runner). Not for a user-facing community platform.
