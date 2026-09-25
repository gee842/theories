# QR payment prototype for Southeast Asia

created: 2026-04-08T04:22:48.925519Z  uuid: 38f82a58-578b-443a-8963-4a0a68b229ee  export: new
messages: 19  total_chars: 42189  human_chars: 885

summary: **Conversation Overview**

Ren is building a QR payment prototype targeting Vietnam, Thailand, and Indonesia, with a focus on micro-transactions (often under $1). The conversation began with researching payment APIs used by apps like Moreta and Yodl, progressing through an evaluation of SePay, Xendit, and ultimately landing on AEON Pay as the most promising infrastructure candidate.

The research established that the three national QR rails — VietQR (Vietnam), PromptPay (Thailand), and QRIS (Indonesia) — are nearly free at the rail level (0–0.3%), but payment gateways like Xendit add prohibitive flat fees ($0.30+ per transaction) that make micro-payments unviable. SePay was ruled out because Ren does not have a Vietnamese bank account. Xendit was ruled out on fee structure grounds. AEON Pay emerged as the preferred solution because it bridges crypto to local fiat QR rails across SEA with percentage-only fees and no apparent flat per-transaction cost.

Through direct examination of AEON's API documentation, the team confirmed the integration flow: scan merchant QR → call `/open/api/scanCode` to decode the EMV string → call `/open/api/scan/payment` to create an order → server sends USDT on-chain to AEON → notify AEON with tx hash → AEON settles fiat to merchant via local rail → webhook confirms success. Critically, end users do not need crypto wallets — Nomad OS can operate a custodial hot wallet model where users hold an internal balance and the platform handles all on-chain operations. A key unresolved question is whether AEON operates on a per-transaction on-chain transfer model or a pre-funded merchant balance model, with the latter being strongly preferred for micro-payment cost efficiency. A list of five concrete questions was compiled for AEON's Telegram onboarding, and Ren asked Claude to draft an outreach message (pending at conversation end).


---
**HUMAN** (2026-04-08T04:22):

can you research the payment api used by moreta, yodl, and similar apps? let's aim for vietnum thailand and indonesia. I want to quickly build a qr payment prototype

---
**ASSISTANT** (2026-04-08T04:23):

Ren wants to research payment APIs for QR payment prototypes in Vietnam, Thailand, and Indonesia - this connects to the Nomad OS work.
```
This block is not supported on your current device yet.
```

Good, now I know Moreta uses Moolahgo's neoConnect for QRIS (Indonesia), and Privy + stablecoin rails. Let me search for Yodl and the specific payment rails/APIs for each country.
```
This block is not supported on your current device yet.
```

Now let me search for the specific APIs - Moolahgo neoConnect, VietQR API, QRIS API, PromptPay API.
```
This block is not supported on your current device yet.
```

Now let me search for VietQR API and direct payment API options for Vietnam and Thailand.
```
This block is not supported on your current device yet.
```

Now let me search for PromptPay API and QRIS API for developers.
```
This block is not supported on your current device yet.
```

Good, I have enough info now. Let me also quickly check Xendit since they cover multiple SEA countries.
```
This block is not supported on your current device yet.
```

I have enough info now to give Ren a solid overview.Ren, here's what I found. The architecture these apps use breaks down cleanly by country rail, and there are multiple paths depending on whether you want to be the payer (scan QR) or the merchant (generate QR).

## The Three National QR Rails

**Vietnam — VietQR** (NAPAS standard, bank-to-bank transfers)
- VietQR is a standardized QR payment system developed by NAPAS in collaboration with the Vietnam Banks Association, enabling fast bank-to-bank transfers via mobile banking apps.
- Has a **public API** at `api.vietqr.io` — you can generate QR codes without even registering. The URL pattern is: `https://img.vietqr.io/image/<BANK_ID>-<ACCOUNT_NO>-<TEMPLATE>.png?amount=&addInfo=&accountName=`
- There's an official Node.js library (`vietqr`) that lets you generate QR base64 images with bank BIN, account number, amount, and memo.
- For **payment confirmation** (knowing when someone paid), you need their payOS/callback service — requires a Vietnamese business bank account (MBBank or BIDV initially) and a formal integration with VietQR's host-to-host API.
- **SePay** is a popular middleware that connects directly to bank APIs and fires webhooks on balance changes, making the payment confirmation loop much simpler for prototyping.

**Thailand — PromptPay** (Bank of Thailand, via National ITMX switch)
- The Bank of Thailand's PromptPay QR standard is based on EMV QRCPS Merchant Presented Mode. QR codes contain a PromptPay ID (phone number, national ID, or e-wallet ID).
- Open-source JS library: `promptpay-qr` by dtinth on GitHub — generates the EMV payload string from a phone number + amount, which you then render as a QR.
- For **merchant-side integration** (accepting payments with confirmation), you'd go through: **Stripe** (supports PromptPay natively), **Xendit**, or **ECOMMPAY**. Stripe displays a QR code at checkout and provides instant confirmation when customers scan and pay via their Thai banking app.
- Direct PromptPay API access requires being a licensed entity or going through a Thai bank's corporate API (e.g. HSBC Omni Collect).

**Indonesia — QRIS** (Bank Indonesia standard)
- QRIS is Indonesia's national QR code payment standard, enabling transactions across all major e-wallets and mobile banking apps through a single unified QR code, accepted by over 34 million merchants.
- No public QR generation API like VietQR — QRIS requires going through a licensed payment switch.
- Best developer paths: **Xendit** (clean REST API, Node SDK) or **Midtrans** (Goto/Tokopedia ecosystem). Both let you create dynamic QRIS codes via API and get webhook callbacks on payment.

## How Moreta & Yodl Wire It

**Moreta** uses a layered stack:
- Privy for embedded programmatic wallets (stablecoin-backed, USDC rails), with smart wallets and gas sponsorship for frictionless UX.
- Moolahgo's neoConnect platform for QRIS integration in Indonesia — a white-label payments-as-a-service API handling connectivity to regional payment rails, real-time processing, compliance, and settlement.
- Plaid for US bank account linking, AiPrise for KYC.

**Yodl** is crypto-native:
- Users deposit USDT (Arbitrum) or USDC (Base), scan local QR codes (VietQR, QR PH, Pix, etc.), and merchants receive local currency.
- They likely have direct integrations or use intermediary APIs to settle into local rails per country.

## Fastest Prototype Path for You

Given you're in Da Nang and want all three countries:

| Country | Generate QR | Confirm Payment | Fastest Option |
|---------|------------|----------------|----------------|
| Vietnam | `vietqr` npm + free API | SePay webhook or VietQR callback (needs VN bank acct) | **VietQR free API** — you can prototype QR generation today with zero signup |
| Thailand | `promptpay-qr` npm | Stripe PromptPay or Xendit | **promptpay-qr** for generation; Stripe for confirmation |
| Indonesia | Xendit or Midtrans API | Same (webhook) | **Xendit** — single API covers QRIS + Thai PromptPay + VietQR |

**Xendit is probably your single-integration answer** — they support QRIS, PromptPay, VietQR, and bank transfers across Indonesia, Thailand, and Vietnam through a single API, with a Node SDK. Free to sign up, pay-per-transaction. That said, for a quick Nomad OS prototype where you're on the *payer* side (scanning merchant QRs), you'd need to understand the EMV QR parsing side rather than the merchant generation side — which is a different problem. Want me to dig into EMV QR code parsing (reading/decoding merchant QR codes) for the scan-and-pay flow?

---
**HUMAN** (2026-04-08T04:26):

if i use sepay, what setup is required? do i need license? what are the limitations

---
**ASSISTANT** (2026-04-08T04:26):

Let me search for SePay specifics.
```
This block is not supported on your current device yet.
```

Let me get the pricing and account requirements.
```
This block is not supported on your current device yet.
```

Good, I have enough to give a clear answer.Here's the full picture on SePay:

## Setup Requirements

**You need a Vietnamese bank account.** That's the core prerequisite. SePay partners directly with banks via official APIs — customers scan a VietQR code, transfer payment, SePay detects the balance fluctuation and fires a webhook to your app, all within about 10 seconds.

SePay has direct API connections to BIDV, MB, VietinBank, ACB, OCB, KienLongBank, and MSB. Other banks are connected via SMS Banking (slower, less reliable). So for best results you'd want an account at one of those seven banks.

**No payment license needed.** SePay isn't a payment gateway in the traditional sense — it's a bank transaction monitoring and webhook service. The money flows directly from customer → your bank account via standard VietQR bank transfer. SePay just watches for the balance change and notifies you. You're not processing payments through an intermediary, so no payment intermediary license is required on your side.

**Account signup:** Register at my.sepay.vn, link your bank account (OTP verification), set up webhook endpoint. Pricing starts completely free with tiered monthly plans. They also mention 500 free transactions/month for the first year for small merchants and freelancers.

## The Flow

1. You generate a VietQR code (using the free vietqr.io API) with your bank account + amount + unique order reference in the memo field
2. Customer scans with any Vietnamese banking app and transfers
3. SePay detects the incoming transaction via bank API
4. SePay fires a webhook to your endpoint with transaction details (amount, memo content, reference code, timestamp)
5. You match the memo to your order and mark it paid

## Limitations

**Vietnamese bank account as a foreigner:** Over the past few years, new laws require customers to have a Temporary or Permanent Resident Card valid for 12 months to open a standard account. On a tourist visa you'll struggle to find any suitable products at all. So you need proper residency status — a work permit or TRC. Given you spend significant time in Vietnam and are based partly in Da Nang, you may already have this sorted, but it's the real blocker.

**Vietnam-only.** SePay only covers Vietnamese banks. It won't help with Thailand (PromptPay) or Indonesia (QRIS) at all.

**Rate limits:** SePay limits API calls to 3 per second, returning HTTP 429 if exceeded.

**Webhook-based confirmation only.** There's no "pull" mechanism to check if a specific QR was paid — you receive webhooks and match by memo/transfer content. If the customer changes the memo or types it wrong, the auto-match fails. This is the fundamental weakness of the VietQR transfer-based approach vs. a real payment gateway.

**No refund API built-in.** You'd need to handle refunds manually or build your own transfer-out flow.

**Personal vs. business accounts:** SePay supports both, but virtual accounts (order-based sub-accounts for cleaner reconciliation) currently only support BIDV business accounts.

## Bottom Line for Nomad OS

SePay is perfect for a Vietnam prototype — zero licensing, free tier, real-time webhooks, and you're already in Da Nang. The main question is whether you have (or can get) a Vietnamese bank account. If you have an MBBank or BIDV account already, you can literally be prototyping today.

For the three-country vision though, SePay is just the Vietnam layer. You'd still need Xendit or Stripe for Thailand/Indonesia. Want me to sketch out a minimal architecture that combines SePay (VN) + Stripe PromptPay (TH) + Xendit QRIS (ID) behind a single API?

---
**HUMAN** (2026-04-08T04:30):

i do not have a bank account, let's look into xendit

---
**ASSISTANT** (2026-04-08T04:30):

Let me search for Xendit's specific requirements, pricing, and how it works for Vietnam/Thailand/Indonesia.
```
This block is not supported on your current device yet.
```

Let me get pricing details and the specific onboarding requirements for Global Account.
```
This block is not supported on your current device yet.
```

Good, I have enough now.Here's the Xendit breakdown:

## Account Types — The Key Decision

If your business is registered outside of Indonesia, Philippines, Malaysia, Thailand, and Vietnam, a Global Account is automatically available. If registered in one of those countries, you'd need to contact help@xendit.co. The Global Account gives you a single dashboard, single API key, and multi-currency/multi-market access.

For **local accounts** (per-country), each market requires local business registration documents. For Indonesia specifically, foreign entities need NIB, legal deed, and authorized director documentation. Similar for each country.

**So the practical question is: where is your business entity registered?** If you have a company registered anywhere (even outside SEA), you can get the Global Account and access all three markets. If you don't have an entity at all, that's the real blocker — Xendit can support international/foreign businesses as long as required documents are provided.

## What You Get

Single integration covering QRIS, PromptPay, VietQR, plus e-wallets (MoMo, ZaloPay, OVO, DANA, ShopeePay), bank transfers, and cards across all markets.

With Xendit Cross Border, you can collect payments in local currencies across Southeast Asia and send cross-border payouts through a single API, consolidating funds back to a central HQ entity.

## Pricing (per successful transaction, no monthly fees)

Based on published rates:

| Method | Fee |
|--------|-----|
| QRIS (Indonesia) | 0.7% + $0.20 |
| QR non-Indonesia (PromptPay, VietQR) | 1.4% + $0.30 |
| E-wallets | 2.70% + $0.40 |
| Bank transfer | 2.13% + $0.60 |
| Domestic cards | 3.0% + $0.80 |
| International cards | 4.0% + $0.80 |

No registration fee, no subscription fee, no maintenance fee, no termination fee.

## Integration

Official Node SDK (`xendit-node`) — instantiate with your secret API key and you're calling endpoints. They also have a test/sandbox mode so no real money during development.

The flow for QR payments: call the payment request API specifying the QR channel (QRIS / PromptPay / VietQR) → Xendit returns a QR code string/image → display to customer → customer scans with their local banking app → Xendit fires webhook to your endpoint on success.

## Limitations & Gotchas

**Entity requirement.** This is the main one. You need a registered business. A sole proprietorship or individual freelancer registration might work for some markets but the Global Account likely needs a proper entity. Do you have anything registered — even a Shenzhen company or a Singapore entity through 706 networks?

**Vietnam coverage is thinner.** Vietnam supports bank transfers, e-wallets (MoMo, ZaloPay), and cards — VietQR is listed in their payment channels but the depth of integration may not be as mature as Indonesia (QRIS) or Thailand (PromptPay). Worth confirming with their sales team.

**Settlement timing.** Funds don't land instantly in your bank — there's a settlement cycle (typically T+2 to T+5 depending on market and method). For a prototype this doesn't matter but for Nomad OS split-pay flows it does.

**You're the merchant side.** Xendit is designed for you to *accept* payments from customers. If the Nomad OS use case is more peer-to-peer (splitting bills between friends who then each pay a merchant), Xendit handles the "pay the merchant" part but the split logic is yours.

## Recommendation

The fastest path to a working prototype across all three countries:

1. Register a Xendit Global Account (if you have any business entity)
2. Use sandbox mode immediately — no entity verification needed to start coding
3. Build against the Node SDK: one `createPaymentRequest` call with different `channel_code` per country
4. Webhook handler for payment confirmation

If entity registration is a blocker, want me to look into alternatives that work for individuals — like using Stripe (which covers PromptPay in Thailand and has lighter individual onboarding) combined with something else for the other markets?

---
**HUMAN** (2026-04-08T04:32):

fee, especially +$0.3, is quite high, many purchases are not even $1

---
**ASSISTANT** (2026-04-08T04:32):

Ren is right - for micro-transactions under $1, a $0.30 fixed fee is a dealbreaker. This is the same problem that plagues all traditional payment gateways for micro-payments. Let me think about what alternatives exist for micro-transactions in SEA.

The key insight: VietQR, PromptPay, and QRIS are all bank-to-bank transfer systems with near-zero fees at the rail level. The fees Xendit charges are their markup as intermediary. If you can connect more directly to the rails, fees drop dramatically.

Options:
1. Direct VietQR generation (free) + SePay for confirmation (but needs VN bank account)


2. Direct PromptPay QR generation (free, open source) - but no confirmation without a Thai entity
3. The stablecoin route (like Yodl) - on-chain fees on L2s are fractions of a cent
4. Look for cheaper intermediaries

I should dig into what the actual underlying fees are for these QR systems to see if there's a viable path forward.Yeah, that flat fee kills micro-transactions. The irony is that the underlying rails (VietQR, PromptPay, QRIS) are nearly free at the bank level — the $0.30 is Xendit's cut as intermediary.
```
This block is not supported on your current device yet.
```

The key insight is clear: the underlying rails are nearly free. The fees come from intermediaries. Let me think about Ren's actual options for micro-transactions.You're hitting the exact problem that Moreta and Yodl exist to solve — and the reason they built their own stacks instead of using Xendit/Stripe.

The underlying rails are essentially free:

- **VietQR**: Bank-to-bank transfers via NAPAS — zero fee to the customer, zero or near-zero to the merchant at the bank level.
- **PromptPay**: Operated by Bank of Thailand with fees that can be charged, but in practice banks usually waive these costs.
- **QRIS**: Bank Indonesia mandates merchant fees at 0.3% for micro-merchants (capped), zero to the customer.

The $0.30 flat fee is pure Xendit/Stripe markup for handling the integration, compliance, settlement, and webhook infrastructure. For a 20k VND coffee (~$0.80), you'd be paying 37% in fees. Absurd.

## Your Real Options for Micro-Transactions

**Option 1: Direct bank integration (the Moreta path)**
Get a bank account in each country, connect directly to VietQR/PromptPay/QRIS. Near-zero fees. But you need local bank accounts and local entity registration — exactly the problem you don't have solved.

**Option 2: Stablecoin rails (the Yodl path)**
User deposits USDC/USDT on an L2 (Base, Arbitrum). Your app holds their balance. When they "pay" a merchant, your backend settles into local rails via a partner. On-chain tx cost on Base/Arbitrum is fractions of a cent. The FX spread becomes your revenue. This is what Yodl does and it sidesteps the entire bank account problem.

**Option 3: Closed-loop ledger (the WeChat/Nomad OS path)**
Users top up a wallet (via card, crypto, or bank transfer — this is where you'd eat a one-time Xendit fee). Then all splits and P2P transfers within the system are free ledger entries — just database writes. You only hit external rails when someone cashes out or pays an external merchant. This amortizes the Xendit fee across many internal transactions.

**Option 3 is probably the most aligned with Nomad OS.** The Pay→Split→Chat→Trust→Coordinate arc you've already mapped works perfectly here. One top-up (absorb the fee on a larger amount), then free internal movement, then occasional settlement out.

For a **quick prototype**, the fastest thing you can build today with zero accounts and zero licensing:

1. Generate VietQR codes client-side using the free `vietqr` npm library or even just the image URL API — point them at a friend's Vietnamese bank account for testing
2. Use the `promptpay-qr` library for Thailand — same deal
3. Wrap both in a simple React Native camera → QR decode → amount display → confirm flow

You won't have automated payment confirmation without a bank account or intermediary, but you'd have the UX and the scanning flow working. That's enough to demo and validate.

Which direction do you want to push — the stablecoin path, the closed-loop ledger, or just getting the QR scanning UX prototyped first?

---
**ASSISTANT** (2026-04-08T04:33):

Ren is right - for micro-transactions under $1, a $0.30 fixed fee is prohibitive. This changes the architecture entirely. Need to think about what works for micro-payments in SEA.

The VietQR direct approach (bank-to-bank transfer) has zero fees. PromptPay is also zero/near-zero for person-to-person transfers. QRIS has very low merchant fees (0.3% capped). The payment gateway layer (Xendit, Stripe) adds the fees.

So the real question is: can Ren go direct to the rails without a gateway? That's what Moreta and Yodl are doing - they're licensed and connected directly.


For a prototype, I could generate QR codes directly using the open EMV standards and handle confirmation manually, accepting the tradeoff of losing auto-confirmation for a much simpler implementation.Yeah, that flat fee kills micro-transactions. A 25k VND coffee (~$1) would eat a 30% fee. The thing is, the underlying rails themselves are nearly free:

- **VietQR**: bank-to-bank transfer, **zero fee** to the recipient
- **PromptPay**: person-to-person transfer, **zero fee** (merchant QR is 0.1-0.2% max)  
- **QRIS**: merchant fee is **0.3% capped** by Bank Indonesia regulation

The expensive layer is the payment gateway sitting on top. Xendit, Stripe, etc. are charging for the abstraction, KYC, cross-border settlement, and webhook infrastructure.

For a micro-payment prototype, you have a few options:

**Option 1: Go direct to the rails (cheapest, hardest)**
Generate EMV QRCPS-compliant QR codes yourself using open-source libraries (`promptpay-qr`, `vietqr-node`, QRIS follows the same EMV spec). The payment itself is free. The problem is **payment confirmation** — without a bank API connection or gateway, you don't know when someone paid. You'd be relying on screenshot verification or honor system.

**Option 2: Vietnam-only with SePay as the confirmation layer**
VietQR transfer is free. SePay only charges for the webhook/monitoring service (their tiered plans), not per-transaction percentage. So the actual payment cost is zero, and SePay's cost is a flat monthly fee. But this needs a VN bank account.

**Option 3: Stablecoin rails like Yodl**
Yodl's approach — hold USDC/USDT, settle to local currency at point of payment. On-chain transfer fees on Base or Arbitrum are fractions of a cent. But then you're building a crypto wallet and need your own local currency settlement partners.

Which direction feels right for Nomad OS? Are you optimizing for the **706 community use case** (friends splitting meals, micro-payments between known/trusted people) or the **merchant payment use case** (paying shops)? Because for peer-to-peer within a trusted network, you might not even need a payment gateway at all — just a ledger with periodic settlement.

---
**HUMAN** (2026-04-08T04:37):

let's try to find better solutions - if they exist, i don't mind to start with crypto, as long as we can pay qr code locally, for example, i found this interesting aeonPay

---
**ASSISTANT** (2026-04-08T04:38):

Let me search for AeonPay.
```
This block is not supported on your current device yet.
```

Now let me search for AEON Pay API/SDK for developers, fees, and how to integrate.
```
This block is not supported on your current device yet.
```

Let me check AEON's actual fees and the developer docs more closely.
```
This block is not supported on your current device yet.
```

Let me fetch their docs properly.
```
This block is not supported on your current device yet.
```

Let me check the AEON Pay QR Code section and fees.
```
This block is not supported on your current device yet.
```

Let me search for fees.
```
This block is not supported on your current device yet.
```

Now I have a good picture of AEON. Let me also quickly check Yodl's fees since it's the closest competitor, and see if there are other low-fee options.This is a great find. AEON is doing exactly the Nomad OS payment layer — crypto in, local QR rails out. Here's what I've pieced together:

## AEON Pay — The Architecture

AEON's scan-to-pay integrates directly with national payment networks — VietQR in Vietnam and ThaiQR in Thailand. Merchants need no additional hardware; payments are automatically settled in local fiat currency.

The flow: user holds crypto (USDT/USDC/BNB/ETH/etc.) → scans any existing merchant VietQR/ThaiQR/QRIS code → AEON parses the QR, converts crypto to local fiat at market rate, and settles to the merchant's bank account via the national rail. Merchant sees a normal bank transfer.

AEON Pay already powers payments for more than 20 million merchants and 10,000+ global brands including McDonald's, Starbucks, and UNIQLO, covering SEA, Nigeria, Mexico, Brazil.

## Fees

This is where it gets interesting for your micro-payment case. For Brazil (PIX), transaction costs are around 0.8% with no flat per-transaction fee. That's a huge difference vs. Xendit's 1.4% + $0.30. I couldn't find published fee schedules for VietQR/ThaiQR specifically — their docs mention "deducting transaction fees" at settlement but don't publish the rate publicly. The on-chain gas costs on Base/Arbitrum/BNB are fractions of a cent, so the real cost is just AEON's spread/commission on the FX conversion.

## Developer Integration

They have SDKs in JavaScript, Python, Go, and Rust. The core API flow involves chain-agnostic endpoints for creating payment orders. Their docs at `aeon-xyz.readme.io` show two relevant APIs for your case:

- **QR Code Parsing API** — decode a local merchant QR (VietQR/ThaiQR/QRIS) into structured payment data
- **QR Code Payment Proxy API** — execute the payment through AEON's settlement network

They also have a sandbox environment and do merchant onboarding through a Telegram group with their team.

## The Catch

AEON is designed for **consumer wallets and super-apps integrating AEON as a payment method** — not as a standalone API you casually call. Their primary integration path is:

1. **DApp listing** — embed AEON Pay inside an existing crypto wallet (Binance Wallet, Bitget, OKX, etc.)
2. **Hosted Cashier** — redirect users to AEON's payment page  
3. **Native API** — direct API integration (what you'd want)

The Native API path requires merchant onboarding. The question is whether AEON would onboard Nomad OS as a "super app" partner that routes payments on behalf of its users, or whether they expect you to be a merchant accepting payments. Given their docs explicitly mention "platform partners and super apps," this seems aligned.

## How This Maps to Nomad OS

The architecture would be:

```
Nomad OS app (user holds USDC/USDT on Base or Arbitrum)
  → user scans merchant VietQR/ThaiQR/QRIS with phone camera
  → app calls AEON QR Parsing API to decode the QR
  → app calls AEON Payment Proxy API to execute
  → AEON settles fiat to merchant via national rail
  → user's stablecoin balance debits
```

This is essentially what Yodl does, but AEON exposes the API for you to build your own UX on top rather than being a closed app.

## Next Steps

I'd suggest reaching out to AEON directly — their onboarding is through Telegram. The key questions to ask:

1. **Exact fee structure** for VietQR/ThaiQR/QRIS settlements (percentage only? any flat fee?)
2. **Minimum transaction size** — can you do 25k VND ($1) payments?
3. **API access for the QR parsing + payment proxy** — can Nomad OS integrate as a super-app partner?
4. **Settlement to user's own wallet vs. AEON custodial** — do they require funds to sit in an AEON wallet, or can they pull from a user's self-custodial wallet?

Want me to also look at whether you could build the QR parsing layer yourself (EMV QRCPS is an open spec) and just use AEON or a similar service for the fiat settlement leg only?

---
**HUMAN** (2026-04-08T04:41):

lets find these out

---
**ASSISTANT** (2026-04-08T04:42):

Let me search for the specific details Ren wants to know about AEON Pay.
```
This block is not supported on your current device yet.
```

The URL was in the table of contents from the earlier fetch. Let me try fetching the QR code parsing API doc and other pages that appeared in the TOC.
```
This block is not supported on your current device yet.
```

The URLs are in the TOC but I can't fetch them because they weren't directly in search results. Let me search for these specific pages.
```
This block is not supported on your current device yet.
```

No results. Let me try fetching AEON Pay's transaction limits and supported tokens pages, and the merchant onboarding page.
```
This block is not supported on your current device yet.
```

Their fee structure isn't publicly documented for SEA QR payments specifically. Let me try to find the AEON Pay docs - transaction limits, merchant onboarding, and the create order API.
```
This block is not supported on your current device yet.
```

The URLs from the TOC aren't fetchable. Let me try the main docs URL which I already fetched and navigate from there. Actually, the issue is the permission check. Let me search for the specific pages.
```
This block is not supported on your current device yet.
```

Let me now fetch the AEON Pay merchant onboarding page and the create order QR code API.
```
This block is not supported on your current device yet.
```

The search results included sandbox and merchant-settlement pages. Let me fetch those.
```
This block is not supported on your current device yet.
```

The sandbox page content is gated behind login. But I got useful info from the search result earlier. Let me now fetch the Google doc with test accounts that was linked.
```
This block is not supported on your current device yet.
```

Now I can see the actual API. The example shows VND with amount 100000 (100k VND ≈ $4), and the feeType field has OUTER_BUCKLE and USER_BUCKLE options. The response shows the USDT equivalent (0.78). Let me also get the Decode QRcode API and the transaction limits.
```
This block is not supported on your current device yet.
```

Excellent! Now I have the actual API. Let me fetch the transaction limits page.
```
This block is not supported on your current device yet.
```

Transaction limits page content is gated. But I got a lot from the API docs. Let me summarize what I found.OK here's what I dug out directly from AEON's API docs. This is very promising for your use case.

## The Actual API Flow (confirmed from docs)

Two-call flow, exactly what you need:

**Step 1 — Decode QR:**
```
POST /open/api/scanCode
{
  "appId": "YOUR_APP_ID",
  "sign": "...",
  "qrCode": "00020101021138580010A000000727..."  // raw EMV string from camera
}
```
Returns: `bankAccountName`, `bankAccountNumber`, `bankCode`, `bankName`, `currency`, `amount` — parsed from the merchant's VietQR/ThaiQR/QRIS code.

**Step 2 — Create Order:**
```
POST /open/api/scan/payment
{
  "appId": "YOUR_APP_ID",
  "merchantOrderNo": "unique-order-id",
  "qrCode": "00020101021138580010A000000727...",
  "amount": "100000",
  "currency": "VND",
  "feeType": "INNER_BUCKLE",
  "userId": "[email protected]",
  "callbackUrl": "https://your-app/webhook"
}
```
Returns: `orderNo` + `amount` in USDT equivalent (e.g. 0.78 USDT for 100k VND). AEON handles the fiat settlement to the merchant's bank account.

## Key Details

**Fee model:** The `feeType` field reveals two options — `OUTER_BUCKLE` (fee added on top, user pays more) and `USER_BUCKLE`/`INNER_BUCKLE` (fee deducted from payment amount). The fee itself isn't published in docs — it's negotiated during merchant onboarding. But based on the Brazil data (~0.8%) and the fact there's no flat per-transaction fee visible in the API response, this looks far better than Xendit's $0.30 flat.

**VND is explicitly supported.** The example in their docs uses `currency: "VND"` with a 100k VND payment. Amount for VND has no decimal places. PHP/BRL retain two decimals.

**Sandbox available:** They provide real merchants' QR codes and bank account details from supported fiat rails for testing. The sandbox single payment limit is $10 USD. They share test accounts via a Google Doc.

**Transaction limits page is gated** behind login — you'd need to ask during onboarding.

**Onboarding:** You need `appId` and `secret` from their business team. For sandbox, you contact them directly. Production environment credentials are provided separately. Onboarding is done via a shared Telegram group with their team.

**Settlement:** Merchants select clearing method during onboarding — either crypto-to-fiat or crypto-to-crypto (stablecoin). Settlement is T0 (same-day), funds immediately available for payout upon clearing.

## What's Still Unknown (ask in Telegram onboarding)

1. **Exact fee %** for VND/THB/IDR settlements — likely ~0.8-1.5% with no flat fee, but need confirmation
2. **Minimum transaction amount** — sandbox is capped at $10 max, but no published minimum
3. **QRIS support** — docs explicitly show VietQR and ThaiQR. Indonesia/QRIS isn't explicitly in the examples but is mentioned in press materials
4. **Can Nomad OS integrate as a super-app partner** rather than a single merchant? Their Enterprise API has sub-merchant management (batch create, enable/disable, query), which is exactly the Nomad OS platform model
5. **KYC requirements for end users** — does AEON require user-level KYC for each payer, or just merchant-level?

## My Read

AEON is the right infrastructure for Nomad OS. The API is clean, the two-step QR decode → pay flow maps directly to the scan-and-pay UX you want, VND is a first-class citizen, and the fee structure looks micro-payment friendly. The Enterprise API with sub-merchant management even supports the 706 cooperative model where each node could be a sub-merchant.

I'd reach out to them on Telegram today. Contact: [email protected] or find @AEON_Community on X/Twitter for the Telegram onboarding link. Want me to draft a brief intro message explaining the Nomad OS use case?

---
**HUMAN** (2026-04-08T04:48):

ok, so user has to have a crypto wallet right? can we use our own wallet?

---
**ASSISTANT** (2026-04-08T04:49):

Ren is asking whether AEON requires each end user to have their own crypto wallet, or whether Nomad OS could hold funds on behalf of users (custodial model) and just call AEON's API to pay from a single Nomad OS wallet.

Looking at the API: the Create Order endpoint takes `userId` (email/phone) and the QR code + amount. It doesn't seem to require a wallet address or on-chain transaction from the user. The question is: where does the crypto come from? Does AEON debit from a user's on-chain wallet, or from the merchant's AEON balance?

Let me re-read the docs. 

The API docs show the merchant calling the API with appId/secret, and the response returns the USDT equivalent. This suggests AEON debits from the merchant's account balance rather than individual user wallets. So if Nomad OS tops up an AEON merchant account with USDT, users just scan QR codes and Nomad OS's balance gets debited—no wallets needed for end users. I should verify this by examining the AEON Pay flow more carefully to confirm how the payment actually gets processed.Good question — this is the architectural fork that determines whether Nomad OS feels like Moreta (simple top-up balance) or like Yodl (bring your own crypto wallet).

Looking back at the API: the Create Order endpoint takes your `appId` + `secret` + `userId` (just an email/phone string) — there's **no wallet address or on-chain signature required from the user**. This strongly suggests AEON debits from **your merchant account balance**, not from each user's wallet.

That means the architecture can be:

```
Nomad OS holds a USDT balance in AEON merchant account
  → User tops up Nomad OS balance (fiat, crypto, whatever)
  → User scans merchant QR
  → Nomad OS calls AEON API with its own appId
  → AEON debits from Nomad OS's balance, settles fiat to merchant
  → Nomad OS debits user's internal ledger
```

Users never touch crypto. They just see a balance in the app. This is exactly the Moreta model — and it's the Pay→Split→Chat→Trust→Coordinate arc you've already designed.

But I want to confirm this. There are two things in the docs that could go either way:

1. The `feeType` OUTER_BUCKLE vs INNER_BUCKLE implies the platform controls fee handling, which fits the custodial model
2. But the AEON AI Payment section mentions "User Wallet Payments" vs "AI Agent Wallet Payments" — suggesting there may also be a mode where the user's own wallet is debited

Let me check the order confirmation flow to see if there's an on-chain step.
```
This block is not supported on your current device yet.
```

The Order Confirm page content is also gated. But from what I've seen in the API, there's no wallet address or transaction hash parameter in the Create Order request. The flow is: Decode QR → Create Order → Order Confirm → Webhook. This looks like AEON handles the crypto side internally.

Let me check the "Order Webhook To AEON" which sounds like AEON expects to receive a payment confirmation (maybe the on-chain tx).
```
This block is not supported on your current device yet.
```

Content is gated. But I have enough to answer. The key evidence:

1. The Create Order API takes no wallet address, no chain, no token type — just appId, QR code, amount, currency, userId (email)
2. The response returns USDT equivalent amount and an order number
3. There's an "Order Confirm" step after Create Order and before the webhook
4. There's an "Order Webhook To AEON" — meaning YOUR system sends a webhook TO AEON (not the other way around)

The flow seems to be:
1. Decode QR


2. Create Order → AEON returns amount in USDT
3. Your app sends the USDT on-chain to AEON's wallet
4. Order Webhook To AEON → you notify AEON that you've sent the crypto
5. AEON confirms receipt and settles fiat to merchant
6. AEON sends webhook back to your callbackUrl

So there IS an on-chain step — your platform needs to send crypto to AEON. But it's YOUR platform sending from YOUR wallet, not the end user. This is the custodial model. Though looking at the AEON AI Payment section, there might be a separate QR Code Payment flow I should examine.

The DApp Listing integration where AEON is embedded in wallet apps like Binance or Bitget works differently — the user's wallet sends directly. But the Native API integration that Nomad OS would use follows the platform-custodial model where Nomad OS holds the funds and calls the API.

I should give Ren a straightforward answer about which model applies here.The detailed API content on Order Confirm and Order Webhook To AEON is gated behind login, but here's what the flow tells us from the structure:

The sequence is: **Decode QR → Create Order → Order Confirm → Order Webhook To AEON → (AEON settles fiat) → Webhook back to you**

The "Order Webhook To AEON" step is critical — that's **your system notifying AEON** that you've sent the crypto. This means there IS an on-chain step, but it's between **your platform wallet and AEON's receiving wallet**, not between the end user and AEON.

So yes — **Nomad OS can use its own wallet.** The model is:

```
User tops up Nomad OS (fiat wire, USDC transfer, card, whatever)
  → Nomad OS internal ledger credits user
  → User scans merchant QR in app
  → Nomad OS backend calls Decode QR → Create Order
  → AEON returns: "this costs 0.78 USDT, send to [address]"
  → Nomad OS sends 0.78 USDT from its hot wallet to AEON
  → Nomad OS calls Order Webhook To AEON (confirms tx)
  → AEON settles VND to merchant bank
  → Nomad OS debits user's internal balance by 0.78 USDT equivalent
```

End users never need a crypto wallet, never see blockchain, never deal with gas fees. They see: "scan QR → confirm 25,000 VND → done." Exactly like Moreta or Grab.

The on-chain cost per transaction is just the USDT transfer on Base/Arbitrum — fractions of a cent. AEON's fee is their FX spread + commission (need to confirm during onboarding).

This is a clean fit for the Nomad OS three-layer architecture you designed: multi-source funding → internal ledger/split engine → multi-network payout. AEON becomes the payout layer, your ledger handles splits, and the funding layer can be anything (bank transfer, crypto, card top-up via Stripe, even cash from a 706 node).

The specific questions for AEON onboarding are now very concrete:

1. **Confirm the Native API flow** — does Create Order → Order Confirm involve an on-chain USDT transfer from our wallet to AEON, or does AEON debit a pre-funded merchant balance?
2. **Hot wallet requirements** — which chains/tokens for settlement? (Base USDC would be ideal for cost)
3. **Fee % on VND/THB settlements** — no flat fee?
4. **Min transaction** — can we do 10k VND (~$0.40)?
5. **Enterprise/sub-merchant API** — can we use this for the 706 cooperative model?

Want me to draft that Telegram intro message now?

---
**HUMAN** (2026-04-08T05:02):

ok, looks like the flow goes like this:
scan qr code -> request order -> my server pays crypto -> aeon takes money and settle -> return if successful
is this correct?

---
**ASSISTANT** (2026-04-08T05:02):

Yes, that's the flow based on what we've seen in the docs.Yes, that's correct. Exactly:

1. **User scans QR** → camera reads EMV string
2. **Decode QR** → `POST /open/api/scanCode` → returns bank name, account, amount, currency
3. **Create Order** → `POST /open/api/scan/payment` → AEON returns order number + USDT amount
4. **Your server sends crypto** → on-chain USDT transfer to AEON's wallet
5. **Notify AEON** → Order Webhook To AEON (confirms your tx hash)
6. **AEON settles fiat** → bank transfer to merchant via VietQR/ThaiQR/QRIS rail
7. **AEON webhooks you back** → callbackUrl confirms success/failure
8. **You debit user's internal balance**

The whole thing from the user's perspective is just: scan → confirm amount → done. Steps 3-7 happen in your backend in seconds.

The one thing to clarify with AEON is whether step 4 is a per-transaction on-chain transfer or if you can pre-fund a balance that gets debited per order (which would be cheaper and faster — no on-chain tx per coffee). Given they have a merchant dashboard with "Pending Withdrawal Account" and "Balance Withdrawal Account" language, pre-funding seems likely as an option. That's a key onboarding question.

Want me to draft the outreach message?

---
**HUMAN** (2026-04-08T05:03):

how does this work? Your server sends crypto → on-chain USDT transfer to AEON's wallet
*

---
**ASSISTANT** (2026-04-08T05:03):

Ren is asking about the mechanics of step 4 - how does the server programmatically send USDT on-chain to AEON. This is a practical implementation question.Your server would have a hot wallet — basically a private key stored securely on your backend that holds USDT. When AEON returns the order with the amount, your server signs and broadcasts an on-chain transaction.

Something like (pseudocode for Base/USDC):

```javascript
// After Create Order returns { amount: 0.78, orderNo: "400017..." }

const tx = await usdcContract.transfer(
  AEON_RECEIVING_ADDRESS,  // provided during onboarding
  parseUnits("0.78", 6),   // USDC has 6 decimals
);

// Wait for confirmation
await tx.wait();

// Then notify AEON with the tx hash
await aeonApi.orderWebhook({ orderNo, txHash: tx.hash });
```

On Base or Arbitrum, this costs <$0.01 in gas per transaction.

**But** — this is the part I'm not 100% sure about. It's possible AEON works differently:

**Option A: Per-transaction on-chain transfer** (what I described above)
- Your wallet sends USDT per order
- More gas cost, slight delay per tx
- AEON verifies on-chain, then settles fiat

**Option B: Pre-funded balance** (more likely for high-volume)
- You deposit a lump sum of USDT to AEON once (say $500)
- AEON maintains an internal balance for your appId
- Each order just debits that balance — no on-chain tx per payment
- You top up when balance gets low

Option B would be way better for micro-payments — zero per-tx gas cost, instant execution. The merchant dashboard language ("Pending Withdrawal Account," "Balance Withdrawal Account") hints at this model.

This is the single most important question for onboarding. It changes the whole cost structure. Want me to draft that message to AEON now?
