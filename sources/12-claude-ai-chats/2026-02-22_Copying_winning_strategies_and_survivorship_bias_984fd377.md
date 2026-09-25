# Copying winning strategies and survivorship bias

created: 2026-02-22T07:48:07.807054Z  uuid: 984fd377-d149-4fab-8da0-d0712e5fa304  export: old
messages: 4  total_chars: 5003  human_chars: 279

summary: **Conversation Overview**

The user, Ren, discussed a trading strategy with Claude focused on copying successful players in prediction markets, specifically Polymarket. Ren presented their friend's approach of identifying top performers and replicating their strategies to achieve similar returns. The conversation evolved into a detailed analysis of this "copy the winners" strategy, examining both its potential merits and significant limitations.

Claude initially outlined general problems with copying successful traders, including survivorship bias, temporal mismatches, incomplete information, and crowding effects. However, when Ren specified that the discussion centered on Polymarket as an open prediction market where top player positions are visible, Claude acknowledged the strategy had more merit in this specific context. The transparency of on-chain positions in prediction markets provides genuine information signals that aren't available in traditional finance, potentially offering real edge through observing smart money movements.

The analysis covered practical implementation challenges including timing delays, slippage on thin order books, incomplete portfolio context, adversarial dynamics where top traders might use visible positions strategically, and differences in resolution risk perception. Claude emphasized that while there could be positive expected value in real-time whale movement tracking, the alpha likely gets arbitraged away when copying positions discovered through periodic leaderboard checking. The conversation concluded with Claude asking whether Ren's friend had actually tracked returns from this approach or if it remained theoretical, indicating interest in empirical validation of the strategy's effectiveness.


---
**HUMAN** (2026-02-22T07:48):

Today I was having a conversation with a friend, his strategy is to find the players with the best returns and copy their strategy, Wdyt?

---
**ASSISTANT** (2026-02-22T07:48):

The user is asking about a strategy of copying successful players/investors. This seems like a general discussion about strategy - could be investing, trading, or some game. Let me respond thoughtfully given Ren's background in strategic thinking and game theory.

This doesn't require any tool calls - it's a conversational question about strategy.Interesting topic, Ren. The "copy the winners" strategy is intuitive but has some well-known pitfalls:

**Survivorship bias** is the big one. Your friend is only seeing the players who had the best returns — not the hundreds who used similar strategies and got wiped out. The visible winners may have just been lucky, and there's no easy way to distinguish skill from variance after the fact.

**Temporal mismatch.** By the time you identify someone's returns as "the best," the conditions that produced those returns may have already shifted. You're essentially driving by looking in the rearview mirror. Strategies that worked in one regime (low rates, bull market, specific meta) often fail in the next.

**Incomplete information.** You can usually see *what* someone did but not *why*, when they'd exit, or how it fits into their broader risk profile. Copying the positions without understanding the thesis means you won't know when to adapt or cut losses.

**Crowding effects.** If enough people copy a winning strategy, the edge gets arbitraged away — or worse, the crowded trade becomes fragile and reverses hard.

That said, there's a smarter version of this: instead of copying positions, study the *decision-making frameworks* of consistently successful players. What's their edge? Is it informational, analytical, behavioral? Can you internalize the reasoning rather than just the output?

Given your systems thinking background, you'd probably frame it this way: copying outputs is fragile, copying generative processes is antifragile. The returns are an emergent property of a system — you want to reverse-engineer the system, not screenshot the scoreboard.

What's the domain — investing, crypto, something else?

---
**HUMAN** (2026-02-22T07:50):

But polymarket is an open market, if we see what top players are doing, we should be able to get a lot from that, and infer hidden information

---
**ASSISTANT** (2026-02-22T07:50):

Ren is talking about Polymarket specifically - a prediction market. This changes the analysis somewhat. Let me think about this more carefully.

In prediction markets like Polymarket, the "copy top traders" strategy has some interesting nuances compared to traditional markets.Fair point — Polymarket does change the calculus compared to traditional markets. Let me steelman your friend's case and then push back on what's still tricky.

**What's genuinely valuable here:**

Prediction markets are about *information aggregation*. When you see a top trader take a large position, you're essentially getting a signal that someone with a strong track record believes the market is mispriced. That's real information — it's basically the whole thesis of why prediction markets work. On Polymarket specifically, positions are visible on-chain, so you get transparency you'd never have in traditional finance. You can see *when* they entered, at *what price*, and *how much* they're risking.

So yes — tracking smart money on Polymarket is a legitimate edge, especially on markets where most participants are retail and unsophisticated. You're essentially free-riding on someone else's research.

**Where it still breaks down:**

*Timing and slippage.* By the time you notice a top player's move, the price has likely already shifted. Their entry at 32¢ and your entry at 41¢ are fundamentally different bets with different expected value. On thin Polymarket books, this can be severe.

*You don't know their portfolio.* A top trader might buy YES on some event as a *hedge* against another position. You copy the YES bet in isolation and you're taking on naked risk they aren't.

*Adversarial dynamics.* Once it's known that people copy top wallets, those wallets can be used strategically — take a visible position to move the market, then profit on the other side through a different wallet. This already happens in crypto.

*Resolution risk perception.* Top traders may have different models for how Polymarket resolves ambiguous outcomes, based on past experience with the platform's resolution criteria. That's hard to infer just from watching positions.

**The real question is whether the edge survives the lag.** If you could get *real-time alerts* on whale movements and the books are deep enough to enter near their price, there's probably positive EV there — especially on political and news markets where information asymmetry is high. But if you're checking leaderboards daily and copying, the alpha is likely already priced in by the time you act.

Has your friend actually been tracking his returns doing this, or is it still theoretical?
