# The 周易 and the 易传: Chinese Wikisource revisions

Retrieved 19 October 2026 through the MediaWiki API of zh.wikisource.org. Each page is kept at the revision named in the [provenance](PROVENANCE.json), with the SHA-256 of its bytes and of its wikitext. The texts are pre-modern and in the public domain; Wikisource's punctuation and markup are CC BY-SA 4.0. This is a punctuated electronic edition, not a scan, and it is not collated with a printed edition.

- [`yizhuan/`](yizhuan/): 繫辭上, 繫辭下, 序卦, 說卦 and 文言, each the API's response body as received.
- [`hexagrams/`](hexagrams/): the sixty-four hexagram pages, 乾 to 未濟, read by following each page's link to the next, each the page object of the API's response with its wikitext unchanged.
- [`commentary/`](commentary/): 孔穎達《周易正義》 (page 周易正義/10) and 王夫之《周易外傳》卷五, as received.
- [`lueli/`](lueli/): 王弼's 《周易略例》, the index page and its seven pages (明彖, 明爻通變, 明卦適變通爻, 明象, 辯位, 略例下, 卦略), as received. The edition gives 邢璹's notes after 王弼's paragraphs; only 明彖 marks 王弼's text (the template `{{yw|…}}`).

The [passage map](../../theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md) quotes these revisions, and [`verify_mapping.py`](../../_process/research/2026-10-05-generative-foundation-review/root-foundation/development/y1-changes/verify_mapping.py) checks every quotation against them. Retaining whole pages does not imply reading them whole.
