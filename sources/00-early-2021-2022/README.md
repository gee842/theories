# Early documents, 2021–2023

Recovered on 2026-09-03 from `~/Desktop` (Apple Pages files) and `~/Documents`, and decoded on 2026-09-04.

**Correction.** An earlier version of this file said the Pages bodies could not be decoded here and that only the first page of each was readable. That was wrong. A Pages file is a zip whose `Index/*.iwa` members are chunked, Snappy-compressed protobuf; a short decoder recovers the text. The decoder used is kept beside the extracts as `recovered-text/decode-pages-iwa.py`. What the decoding showed is more interesting than the assumption it replaced.

| file | date | what it is | full text |
|---|---|---|---|
| `World of Possibilities.pages` | 2022-04-07 (edited) | A book that was started and stopped. **The twelve lines below are the entire document** — the chapter heading "C1 - possibilities" is followed by nothing. | `recovered-text/2022-04-07_World-of-Possibilities.txt` |
| `proposal.pages` | 2021-10-18 | 元社区 Metamunity: the community-infrastructure proposal. About 10,000 characters, of which the first page was previously all that was known. | `recovered-text/2021-10-18_proposal_元社区-Metamunity.txt` |
| `「“？P；。.pages` | 2022-04-07 (content 2022-01) | 706 元宇宙荣誉积分系统, the badge system. The document is mostly a table and images, so the recovered prose is thin; the rendered first page (`「“？P；。.jpg`) carries more than the text extraction does. | `recovered-text/2022-01_706-元宇宙荣誉积分系统.txt` |
| `麦.pages` | 2021-05-29 (content 2021-05-21) | Dali field notes, 102 paragraphs — far more than the one page previously known. Ethnography of the 706 Dali house-building workshop and the people it drew. **Not by Ren** — see the authorship note below. | `recovered-text/2021-05-21_麦_dali-field-notes.txt` |
| `社区.pages` | 2021-05-29 | **Empty.** Contains styles and no content, which is why its preview rendered blank. No extract file. | — |
| `706 元宇宙荣誉积分系统.pdf` | (undated) | PDF of the badge system, no text layer. | — |

`2023-12-11-wamotopia_v1.0-downloads.md` is a duplicate of the manifesto in `02-wamotopia/`.

## What this changes

**`World of Possibilities` is a first page, not a lost book.** In April 2022 Ren wrote out a complete primitive-set — difference → structure → change → space → time → dynamic → possibility → thing → manifestation → system — typed the heading of chapter one, and stopped. The corpus therefore does not contain a hidden 2022 ontology that later work re-derived. It contains the moment the vocabulary of possibility was fixed, and four years of the argument arriving that would have given that vocabulary something to do.

That makes the twelve lines more significant rather than less. They define *possibility* by construction rather than invoking it as a value word: "If change may happen to a structure, it possesses possibility." They define a system as pattern-maintained-through-change rather than as substance. Both moves are load-bearing in the 2026 documents, where 开 is given four conditions and where 生生不息 is grounded in process rather than in things. And the reason the book stopped is legible in what it lacks: there is no agent in it, no feedback, no compounding, no harm. Ren had the ontology and no dynamics. The dynamics arrive in February 2025 with the selfishness spiral, and the affirmative statement only in 2026.

**The Metamunity proposal is a real precursor and is now readable in full.** It coins 元社区 by the same back-formation as Metaverse; argues that a metaverse is a narrative facing the future rather than a technology, and that the present world is already one relative to 200 years ago; grounds a physical community in the post-2020 remote-work shift and the rise of distributed labour; names the specific places surveyed as candidates — 大理, 沙溪, elsewhere in Yunnan, 万宁 on Hainan, and abroad Chiang Mai, Bali, Costa Rica, north-central California — with the criterion of being within ninety minutes of an airport and having paved roads and working networks; records that 706 landed a community in Dali at the pandemic's turning point; and then makes the argument that matters most, that natural beauty alone goes stale, because the real deficit of city life is structural rather than environmental: 城市中社会联结机制的结构性问题 — the structural problem of the city's social-connection mechanism — is what produces loneliness and the absence of belonging. That is the community-infrastructure thesis, four years before Bonfire and Nomad OS, and it is stated as a mechanism rather than as a mood.

The critique that carries it deserves quoting, because two of the corpus's terms are dated from here. The premise is about design intent: 「城市本质是为了实现生产效率最大化而设计出来的巨大社会机器，并非人作为人对更好的生活体验和幸福追求而创造的乐土」 (the city is essentially a giant social machine designed to maximise production efficiency, not a paradise created by people, as people, out of the pursuit of better experience and happiness). What it does to the people in it: 「结构把人规训成了劳动力，然后一个个塞进了钢筋混凝土的盒子里」 (the structure disciplines people into labour-power, then packs them one by one into reinforced-concrete boxes) and 「它的结构在无形中把一个个人变成了原子化的个体」 (its structure invisibly turns persons, one by one, into atomised individuals). What is lost on the way: 「充满人情味和友邻气息的附近消失了」 (the 附近 — the nearby, full of human warmth and neighbourly air — has disappeared), and 「它剥夺了我们向目的前进过程中的过程的意义」 (it strips the meaning out of the process of going toward a destination). The design target is that same 附近 restored — 「生活的一切可以在步行十五分钟之内的附近得到满足」, everything life needs met inside a fifteen-minute walk. Before this decoding, **原子化** appeared in the organised layer only through the 2025-11 Wamo field guide and **附近** only from 2026, so both would have been dated four to five years late. Both are Ren's from 2021-10-18, and `GLOSSARY.md` now carries an entry for each with that first use.

**The 706 badge system is the first token design in the corpus**, three years before the Spirit–Token–Space paper. Members issue badges to each other and the community issues badges; honour and contribution are recorded by the badge and computed into points; three families — Kudos (Appreciation, Greatness, Community contribution, Accomplishment), Communal (Proposal, Suggestion, Complaint), and Others, whose entry is "Anything else you'd like to inform/broadcast. Create your own mechanism." Paper first, "gradually digitised and eventually on-chain." Peer-issued claimable meaning with a user-extensible mechanism is STS's Token primitive in embryo. The rendered page `「“？P；。.jpg` is the better source here, since the badge families live in a table the text extraction flattens.

**The Dali field notes are ethnography, and they are the practice side of everything else.** A house-building workshop run by 安琪 for about twenty people, met through 706; a Cambridge earth-sciences student who "felt very small studying it, so wanted to do something practical"; the question the notes actually write down — 这样的连接是怎样的价值交换 ("what kind of value exchange is this connection?") — which is the coordination question that the later theories answer abstractly, asked here about a specific roof.

**Authorship: `麦.pages` is not Ren's writing.** The file opens 「在任的电脑上记录田野笔记，不习惯的苹果系统」 — recording field notes on Ren's computer, not used to the Apple system — and a later section is headed 「和任在古城聊天」, chatting with Ren in the old town. The author is a companion doing fieldwork who borrowed his laptop and who, in that section, is writing Ren down. So the notes are a third party's ethnography, and the parts that record Ren are **recorded speech, not authored text**. This matters for attribution in two directions: nothing in the file should be quoted as Ren's prose, and the file's own observations (the value-exchange question, the anthropology-seminar notes on how to write down speech) belong to their author rather than to this corpus's subject. Where the file is cited in the organised layer — `TIMELINE.md`, and the genealogies of `theories/selfishness-spiral-and-narrative-value-frames/` and `theories/drives-narrative-attractors-and-mind/` — it is marked as recorded speech.

**Two items in the 古城 conversation are the corpus's own theory, five years early.** Both sit under 「和任在古城聊天」 and carry the caveat above: they come out of a conversation with Ren, written down by someone else, and the file does not separate whose turn is whose.

1. *A narrative that changes what it describes.* 「中医：有一套 Bio-politic 的叙述，可以改变脑海中对于自身病痛的建构，不再激起负面的想法，而是建构起一套中药会起作用…让人产生积极正面的感觉」 — Chinese medicine carries a bio-political narrative that changes how a person constructs their own illness in their mind, so that instead of igniting negative thoughts it builds an account in which the medicine will work — with the chain stated outright: 「一套新的话语及神经机制的建构会导向新的心理状态进而改善身体状况」, a new discourse and its neural construction lead to a new psychological state and thence to an improved bodily one, scoped to conditions that are 「本身就是心理-身体疾病」. That is the narrative-value-frame mechanism at the scale of one body, four years before the frame is named.

2. *「现代人的分裂」, the split in modern people.* 「社会有一套"你该成为怎样的人"的论述，但每个人有其个性化的真实感受，常常与单一的作为劳动力/高效参与到生产过程中的社会期待的"我"相异。这样的分裂就是不自洽的状态」 — society holds a discourse about who you should become; each person has their own felt reality; the two are routinely at odds with the single "I" expected of them as labour-power efficiently participating in production; and the split is a state of not being self-consistent. Two exits are named: 「要么去完成社会期望的我压制住感觉，彻底变成某种人；要么去正视自己的感受，重新审视社会期待，去选择为自己负责的个性化道路」 — suppress the feeling and become the expected person entirely, or face the feeling, re-examine the social expectation, and take an individual path you answer for. The socially imposed self is already specified as labour-power in a production process, which is the same framing the October proposal applies to the city.

Neither item has a selection dynamic attached — nothing about frames out-competing frames, nothing about compounding — so what 2021 contributes is the frame and the split, not the spiral. The earlier verdict in this file, that the 麦 notes are material for the community-practice side of the corpus rather than for a theory, was written when only the first page had been read and is withdrawn.

## The transcribed first page of World of Possibilities

> # World of possibilities
>
> For any world to have structure, there must be difference.
>
> A structure is the arrangement, or aggregation of differences.
>
> For any world to have dynamic, there must be change.
>
> Structures list in order defines space.
>
> Changes of structure(s) happen in sequence defines time.
>
> A dynamic is a structure that changes, a structure in space-time.
>
> If change may happen to a structure, it possesses possibility.
>
> A thing is a structure, or a dynamic, which can be identified, that may happen, or be the case.
>
> When a structure becomes another structure, we can say, its possibilities manifest.
>
> A thing that maintains certain dynamic pattern over time, is a system.
>
> We couldn't make every concept, such as ''world', order', 'pattern' and many others well defined. Or it will inevitably become self-referencal. But I hope you will get the point, eventually, at least.
>
> A world of possibility is a world of differences, of changes. And it is the world we are going to talk about the rest of this book.
>
> ## C1 - possibilities

*(document ends)*
