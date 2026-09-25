#!/usr/bin/env python3
"""Regenerate the complete, portable Edition 05 reading companions.

Only Python's standard library is needed. Page copy comes verbatim from
content-v5.json; line breaks used for print composition become whitespace.
Descriptions below were authored after inspecting every actual source image.
The diagram labels supplement the JSON with text used in build-v5.py.
"""
from html import escape
from html.parser import HTMLParser
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
DATE = "7 September 2026"

DESCRIPTIONS = {
    "cover": "From a shaded terrace, a group of adults and a child lean around a large circular model of a settlement. Miniature buildings, gardens, waterways and a translucent blue structure occupy the table; loose model pieces and drawings lie at its edges. Beyond the group, a much larger garden city descends toward the sea. An open, planted tower rises near the center, while slender industrial structures stand on the distant coast. The model and the surrounding city put shared discussion about a place beside an imagined place people could inhabit.",
    "production": "An elevated gallery overlooks a large, bright industrial hall. People at the foreground rail examine equipment and talk. Below them, white robot arms work inside organized production cells; a humanoid-shaped machine stands among fixtures and parts. Low wheeled carriers move loads along a marked central aisle. Racks, overhead services and another occupied gallery extend through the building. Through an open end, cranes and the frame of a further structure are visible. This is an imagined production commons, rather than a photograph of any factory named in the evidence list.",
    "freedom-day": "Three adjacent panels follow the same person with short curly hair, a teal overshirt and an orange shoulder bag. At left, she sits beside a bright window with a cup, an open book and fruit; planted terraces are visible outside her private room. In the center, she holds a plate at a food counter beside an older person using a wheelchair. Dishes, food, people and a robot arm occupy the shared kitchen behind them. At right, she examines a small instrument with another person in a workshop or equipment library, surrounded by parts, shelves, cases and machinery. The three places give the accompanying account of Mira's day a recurring person and tangible settings.",
    "garden-arrival": "A broad planted neighborhood opens around a stone path and water. People eat together at a table on the left, sit beside the route and stroll through the center. A person tends plants at the lower right near a small wheeled machine. Low buildings and terraces have large open or glazed rooms: a lit communal room above, a red-toned activity room below it, and other occupied spaces at ground level. Trees, climbing plants and roof gardens connect the rooms visually to the paths. Beyond the settlement are water, hills and warm evening light.",
    "garden-walk": "The view is at a pedestrian's height: a hand rests on the rough, reachable edge of a low stone wall in the foreground. A gently curving path follows a planted water garden. A small group, including a wheelchair user, moves ahead; other people pause beside the water or sit along its edge. Homes with balconies and abundant planting rise on the right. A small service vehicle stands farther along that side, with a recessed service opening and pipes visible beneath the nearby planting. Overhanging leaves shade the route while sunlight reaches the terraces.",
    "garden-section": "An architectural cutaway opens a garden neighborhood from the side. Above ground are stacked rooms, terraces, trees and a planted walkway with people and a small mobile machine. Below the walkway, a blue water tank at left connects to visible vertical pipework. Workbenches, shelving and service rooms occupy the central lower level; a vehicle sits in a service passage at right. Structural columns and floor layers divide the occupied landscape from the equipment below. The cutaway suggests locations for water and maintenance infrastructure. The accompanying route labels and text provide the intended connections; the image does not resolve a continuous pipe network or certify structural performance.",
    "university-arrival": "In a small leafy courtyard, two people of different ages lean together over papers at a wooden table. A microscope, books, specimens and a shallow tray of objects make the inquiry concrete. Open rooms around the courtyard hold shelves and tables. Farther back, two people face each other in a movement practice on the paved court, while a seated person watches from the right. Trees, flowering plants and planted roofs soften the boundary between the shared learning rooms and the outdoor space. The scene places conversation, close observation, bodily practice and rest within one university setting.",
    "university-cosmos": "From a first-person position at a table, two hands hold small circular objects around a central instrument. Beyond them, people stand, gesture, sit or work at tables in a dark, warm-lit learning hall. A luminous astronomical model fills the upper space with planets, points of light and sweeping orbital lines. A large telescope sits under an opening high in the roof; bookshelves and lamps line the occupied room below. The displayed cosmos extends the apparent subject of study across the hall, while furniture, hand-held objects and other people retain a bodily scale.",
    "university-workshop": "A visitor rests a hand on a rail at the entrance to a sunlit workshop. At the central bench, an older person and a younger person handle a dark cylindrical part together. A glazed machine enclosure with a robot arm stands to the left. At right, a monitor shows separated component shapes beside a stool, tools and shelves of stored parts. A low wheeled carrier holds components between the benches. More people work beyond the central table, with green trees visible through the open or glazed boundary. The scene joins learning by hand to shared machinery and stored design information.",
    "exploration-arrival": "People gather around a long model or instrument on a foreground table overlooking a coastal spacecraft campus. Another visitor looks through a telescope at right. Behind them, an enormous assembly hall contains a horizontal white spacecraft, surrounded by scaffolding, mechanical arms and handling equipment. Its cylindrical body and dark end face dominate the right half of the view. At left, open air reveals a distant upright rocket and launch structures near the sea. Planted paths and smaller buildings sit between the social terrace and the industrial facilities.",
    "exploration-launch": "From a garden terrace above a bay, a group watches a distant rocket rise into a sunset sky. Its bright point and vertical exhaust trail appear across the water, separated from the viewers by a wide expanse of sea. People stand close together, sit at the terrace edge or use a wheelchair; cups and a folded blanket rest on a low stone wall in the foreground. An observatory dome stands behind the group at left, while smaller homes and gardens step down toward the shore. The composition emphasizes a shared moment of watching from an inhabited community.",
    "exploration-section": "A cutaway reveals several connected levels of a mission and learning campus. At left, a large seated audience faces a screen showing a planet and spacecraft. A tall central work volume contains a suspended spacecraft-related assembly. Open floors on the right contain people, tables, workshops and galleries. A telescope under a dome crowns the upper terrace. At the bottom, racks, crates, a loaded vehicle and equipment rooms form a receiving and service level. The arrangement puts public learning and observation beside controlled technical work; the separate route strip states the proposed movement of parts through assembly and testing to mission integration.",
    "quest-arrival": "At dusk, a richly detailed canal city glows with lanterns and warm windows. Bridges, balconies, towers and narrow waterside streets recede into the distance. In the foreground, people in varied cloaks and costumes gather around a circular table carrying a luminous miniature scene. Other residents eat, walk or meet along the street; a small wheeled service machine appears at right. A large blue, star-like creature or dragon stretches across the sky above the roofs. The caption identifies the extraordinary creature and shared story elements as AR within a physical city.",
    "quest-bridge": "A first-person hand holds an ornate round token above a folded map at the stone railing of a bridge. Two companions wearing glasses and cloaks look back toward the viewer; one gestures along the canal. Boats, waterside paths, inhabited balconies and lit windows continue beneath them. Over the far roofs, a long luminous blue creature bends across the dusk sky. The close hand, object and bridge rail provide reachable physical anchors, while the shared apparent creature makes the urban scene part of an unfolding adventure.",
    "quest-backstage": "This cutaway continues a canal street downward into the spaces supporting its stories. Timber-framed homes and warmly lit rooms sit above and beside a bridge. On the next visible level, a workshop holds hanging clothes, costumes and props, while a neighboring room contains people around a large tabletop world model. Below them, repair and fabrication spaces contain benches, robot arms, parts storage, equipment racks and service passages. Pipes and conduits follow the floor edges. A faint blue creature remains above the street, linking the experienced fantasy to the ordinary material work beneath it.",
    "changing-rules": "Three panels show the same lantern-lit table beside an arched opening onto a canal. At left, two people wearing glasses lean over a detailed map and model towers, while a third person with a rust-colored outer layer stands behind them, holding a small object. In the middle, that third person joins the others at the table and points to a blue river on the map; hands move among counters and model buildings. At right, the group, now with another participant in the foreground, works around a bridge model and glowing blue connections. The visible change is from watching at the edge to helping compose the scene. The surrounding story supplies the proposed institutional change behind that participation.",
    "expressive": "A smiling person in a warm red outfit takes the viewer's hand and draws them toward a gathering. Around them, people dance, play or listen inside a high, curved timber room. Purple and amber light falls through hanging translucent forms overhead. A person using a wheelchair takes part near the center-right. Curving benches line the edges, and a person reclines separately in a deep alcove at the far right. Musicians and listeners occupy the left side. The offered hand, open floor and quiet places show different degrees of participation within one expressive space.",
    "ar-megastructure": "A monumental rectangular building contains three very broad stacked hall volumes, separated by narrow amber-toned technical bands. Dark vertical cores stand at the left and right ends, with glazed or open-looking shafts showing their height. The large hall faces are pale and translucent, with tiny figures or details emphasizing the proposed scale. At ground level, a generous plaza contains pedestrians, a wheelchair user, planted islands and entrances. Smaller terraces step down along the left edge. This exterior establishes the three-hall form and opposing cores used throughout the House of Worlds sequence.",
    "ar-portal": "Two neighboring views look out through the open doors of the same warm-lit lift cabin. Three people, seen from behind, stand in the same arrangement in each panel; a padded bench and handrail remain visible at the sides. At left, the doorway opens toward an ordinary planted urban courtyard with stone arches. At right, it opens onto a bright fantasy harbor of towers, clouds and sail-like forms. The repeated cabin and companions make the perceptual transition legible. As the page text explains, this experienced image assumes future occlusive or passthrough eyewear; the image alone does not demonstrate a display technology.",
    "ar-worldhall": "Five people wearing dark eyewear gather on a curved promenade beside a round wooden music table. One plays a bronze-colored percussion instrument, another uses a compact keyboard, a standing person joins them, a wheelchair user faces the table, and a fifth person looks outward from the rail. An ochre curved bench borders the table. A dark doorway and solid overhead soffit remain visible at left. Beyond the rail appears a cloud-filled harbor with floating settlements and a large sailing vessel. The table, instruments, floor, rail and bench are the physical anchors; the extended harbor is the proposed shared experienced environment.",
    "ar-reality-pair": "A side-by-side pair repeats five people, a round music table, instruments, an ochre bench, a wheelchair, a curved rail, the near floor and canopy, and a left doorway. Everyone wears dark eyewear in both panels. In the left panel, the view beyond the rail opens across an immense enclosed hall with a broad deck, distant wall, trusses and tiny figures. In the right panel, the distant envelope opens into clouds, floating settlements and a large sailing vessel. Nearby contact surfaces correspond, with small differences in people's poses and the framing of the scene. These are matched concept illustrations, not exact outputs of a verified shared 3D model; the apparent sky adds no physical floor area.",
    "ar-section": "A frontal cutaway exposes three immense world halls stacked over a logistics base. Each hall contains a broad deck with people and formed terrain, surrounded by tall structural walls and pale blue sensory imagery. Narrow amber equipment bands run between the halls. A tall dark shaft stands along the left edge, while the right edge contains a vertical core with visible stairs or platforms. At ground level, service vehicles and equipment occupy open work bays. Planted smaller terraces adjoin the left side. The accompanying text assigns passenger movement to the left core and freight and service movement to the right; the cutaway is a spatial proposal without resolved dimensions or engineering calculations.",
    "materials": "A material-service setting opens onto a leafy courtyard. At left, shelves hold rows of durable metal cups beside a glazed washing area where someone works at a sink. People sit and talk outside in the center. At right, a repair worker handles a component at a bench surrounded by stored fittings, equipment and long members on upper racks; a compact wheeled robot stands near the bench. Warm timber, open doors and planting connect the service rooms to ordinary social life. Cleaning vessels and caring for components appear as visible parts of the shared material setting.",
    "beam-lives": "Three panels follow a recognizable pale portal frame with indigo connection plates and a triangular corner plate containing a round opening. At left, it supports a slatted garden pavilion above people sharing a table. In the middle, a hoist suspends the top member in a workshop; separated upright members, a mobile robot arm, stacked pieces and a person inspecting a component surround it. A foreground tray holds dark rings and small fittings. At right, the recognizable frame forms the opening of a music room where a cellist and a percussionist play for seated listeners. The sequence proposes successive use of the frame, rather than multiple buildings simultaneously made from the same material.",
    "garden-choice": "Neighbors gather around a detailed physical model beneath a large mature tree. The model includes a small tree, paths, planting, a modular building frame and loose bays in a tray at the near edge. Several people point or reach toward it; a wheelchair user sits close to the table at right. The real tree's trunk and canopy dominate the background, with garden homes beyond. A construction robot stands farther back near stacked components. The image gives the discussion about a revised footprint a tangible model and a valued existing place; the caption supplies the decision to protect the tree and revise the proposed rooms.",
}

DIAGRAMS = {
    "recursion": "Two separate four-step loops run left to right, with a return arrow beneath each row. In the production loop, useful production supplies robots, tools and components; these equip and commission cells; the larger productive base then contributes to further useful production. In the knowledge loop, observing operation leads to testing a changed design, publishing usable knowledge, and deploying and checking results; those results supply the next observations. Opposing arrows between the loops identify operating experience as a source of learning and tested knowledge as a way to improve production. The nearby notes state the continuing outside inputs, maintenance burden and conditions for compounding. These are proposed causal relationships, not a measured growth forecast.",
    "provision": "Four boxes read left to right. A plus sign joins the first two: productive and maintenance capacity, and durable common access. These are two requirements to build together. Arrows then lead to necessities and creative means, and onward to meaningful refusal and association. The common-access arrangement does not automatically result from productive capacity; having automated machinery does not by itself ensure that people can use its output. The cards below give a service example, the desired material provision and the account of remaining human attention.",
    "principles": "Four boxes run from shared understandings to choices and institutions, then to lived environments, then to further lives and beginnings. A return arrow from the fourth box to the first closes the loop. The intended relationship is reciprocal: people's understandings influence what they construct, and lives within those environments can revise the understandings from which a next round of choices begins. The six principles elaborate this proposed orientation. The arrows express relationships to learn about, rather than an inevitable prediction of how everyone will behave.",
    "garden-section": "The route strip has three boxes read left to right: terrace drainage, treatment and storage, then irrigation above. The caption adds the return from irrigation and landscape use to later drainage, and distinguishes a machine's separate journey to repair and back to the garden. The strip states an intended water connection within the cutaway; it does not specify pipe sizes, treatment performance or structural design.",
    "exploration-section": "Three boxes read left to right: parts received, assembly and testing, then mission integration. They follow the proposed journey of an instrument through the campus. Public halls overlook the work while the route for controlled handling remains separate. The cutaway locates complementary activities; the strip expresses their intended sequence without resolving logistics capacity or operating procedures.",
    "quest-backstage": "Three boxes read left to right: props returned, inspection and repair, then guild workshop. This follows a costume or prop from the canal street through the lower service spaces and back to a place where people can prepare its next use. The sequence clarifies the material support for the city's shared stories.",
    "ar-section": "The strip lists left passenger core, middle world hall, and right service core in the same left-to-right orientation as the section. It identifies related locations. A passenger enters the middle hall from the left core; the right core carries service activity. The next page distinguishes the two routes, rather than treating all three boxes as one passenger journey.",
    "ar-routes": "A central rectangle labeled as the middle harbor hall lies between a left passenger core and a right freight and service core. The visitor route goes from the left core to the curved promenade, then to the music table for First Arrival, then to the quiet edge and ordinary return, and back toward the passenger core. A separate service route connects ground repair and storage with the right core in both directions. From that core a module enters a closed change area. Opposing arrows connect the change area with a distinct tactile setting, showing delivery and return; the setting is separate from the music-table visitor route. The old module returns for inspection, and the completed setting is checked before the public route reopens. Green indicates the visit and terracotta indicates module delivery and return; these written route names carry the meaning without depending on color. Positions express conceptual connections and separation of operations, not measured spans or final circulation design.",
    "circulation": "Four boxes run from useful stock in service to return and inspection, then to reuse of compatible parts, then to a next useful setting. A return arrow closes the loop from that setting to useful stock in service. This means that a material can serve successive uses. It does not create a second simultaneous copy of the material. The adjacent cards distinguish preserved form, losses and replacement, and the additional stock required for net expansion; the closing text distinguishes material circulation from ecological regeneration.",
}

# Labels composed directly by the PDF layout code, in addition to JSON copy.
PRINT_LABELS = {
    "recursion": ["01 / PRODUCTION FEEDBACK", "02 / KNOWLEDGE FEEDBACK", "Operation teaches; tested knowledge improves production"],
    "provision": ["+"],
    "ar-routes": ["LEFT\nPassenger\ncore", "RIGHT\nFreight &\nservice core", "MIDDLE HALL / HARBOR", "Curved promenade", "Music table\nFirst Arrival", "Quiet edge &\nordinary return", "Closed change\narea / module", "Tactile\nsetting", "Checked before\nreopening", "Ground repair & storage", "VISIT (green) | MODULE DELIVERY & RETURN (terracotta)"],
    "circulation": ["Finite stock moving through successive lives. The arrow back enables another cycle, not another simultaneous copy."],
    "provenance": ["MATERIAL FOUNDATIONS / FURTHER READING"],
}

INTRO = (
    "This reading companion contains the complete substantive text of the 34-page atlas, "
    "including its captions, labels, evidence details, source URLs and credit. It adds "
    "descriptions of all 25 illustrations and the diagrams. Page numbers follow the PDF. "
    "Descriptions and diagram explanations are AI-authored additions, clearly identified "
    "below; they do not replace the atlas's text."
)
BOUNDARY = (
    "The worlds, named episodes, institutions and architectural arrangements are concepts "
    "and proposed scenarios. The evidence supports bounded existing capabilities; it does "
    "not establish a fully autonomous industrial network or engineering validation of these "
    "designs. Ren's quoted words are retained verbatim. This companion is a separate way "
    "to read the work and makes no claim of accessibility certification."
)


def norm(text):
    return re.sub(r"\s+", " ", text).strip()


def strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for key, value in obj.items():
            if key not in {"id", "layout", "image"}:
                yield from strings(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from strings(value)


def generate(book):
    events = []

    def emit(kind, text="", **extra):
        events.append({"kind": kind, "text": text, **extra})

    for number, page in enumerate(book["pages"], 1):
        pid = page["id"]
        emit("page", page["title"], id=pid, number=number)
        emit("kicker", page["kicker"])
        if page.get("quote"):
            emit("quote", page["quote"])
            emit("attribution", page["attribution"])
        if page.get("intro"):
            emit("paragraph", page["intro"])
        if page.get("caption"):
            emit("paragraph", page["caption"])
        if page.get("image"):
            if pid not in DESCRIPTIONS:
                raise ValueError("Missing inspected image description: " + pid)
            emit("description", DESCRIPTIONS[pid])
        for key, label in [("loops", "Feedback loops"), ("loop", "Loop labels"), ("chain", "Connection labels"), ("flow", "Route strip"), ("passenger", "Visitor route"), ("service", "Service route")]:
            if key not in page:
                continue
            emit("heading", label)
            items = page[key]
            if key == "loops":
                for i, loop in enumerate(items):
                    emit("subheading", PRINT_LABELS[pid][i])
                    emit("ordered", items=loop)
            else:
                emit("ordered", items=items)
        if pid in DIAGRAMS:
            emit("diagram", DIAGRAMS[pid])
        labels = PRINT_LABELS.get(pid, [])
        if labels and pid != "provenance":
            emit("heading", "Additional diagram labels")
            emit("unordered", items=labels[2:] if pid == "recursion" else labels)
        for key in ["parts", "cards", "notes", "principles", "steps", "blocks"]:
            for heading, copy in page.get(key, []):
                emit("heading", heading)
                emit("paragraph", copy)
        if page.get("pins"):
            emit("heading", "Illustration labels")
            emit("unordered", items=list(strings(page["pins"])))
        if page.get("closing"):
            emit("paragraph", page["closing"])
        if page.get("note"):
            emit("note", page["note"])
        if pid == "evidence":
            for evidence in book["evidence"]:
                emit("heading", evidence["id"] + " / " + evidence["title"], id=evidence["id"])
                emit("paragraph", evidence["detail"])
                emit("source", evidence["url"], label=evidence["title"])
        if page.get("references"):
            emit("heading", PRINT_LABELS["provenance"][0])
            for label, url in page["references"]:
                emit("source", url, label=label)
        if pid in {"cover", "provenance"}:
            emit("paragraph", book["credit"])
        emit("page-end")

    known_keys = {"id", "layout", "image", "title", "kicker", "quote", "attribution", "intro", "caption", "loops", "loop", "chain", "flow", "passenger", "service", "parts", "cards", "notes", "principles", "steps", "blocks", "pins", "closing", "note", "references"}
    for page in book["pages"]:
        if set(page) - known_keys:
            raise ValueError("Unhandled page-copy field: " + str(set(page) - known_keys))
    return events


def html_text(text, citations=True):
    result = escape(norm(text))
    result = result.replace("生生不息", '<span lang="zh-Hans">生生不息</span>')
    if citations:
        result = re.sub(r"\[(E\d+)\]", lambda match: '<a href="#' + match[1] + '" aria-label="Evidence ' + match[1] + '">[' + match[1] + ']</a>', result)
    return result


CSS = """
:root { color-scheme: light; font-size: 100%; }
* { box-sizing: border-box; }
body { margin: 0; color: #203c32; background: #f5f1e8; font-family: system-ui, sans-serif; line-height: 1.7; }
header, main, footer, nav.contents { max-width: 78ch; margin: auto; padding: 1.5rem; }
header { padding-top: 3rem; }
h1, h2, h3, h4 { line-height: 1.3; overflow-wrap: anywhere; }
h1 { font-size: clamp(2rem, 6vw, 3.2rem); }
h2 { font-size: 1.85rem; margin-top: 0; }
h3 { font-size: 1.16rem; margin-top: 1.7rem; }
h4 { font-size: 1rem; }
a { color: #175b47; text-decoration-thickness: .09em; text-underline-offset: .18em; overflow-wrap: anywhere; }
a:focus-visible { outline: .2rem solid #a24722; outline-offset: .25rem; }
.skip { display: block; padding: .75rem 1.5rem; background: #e8e9df; }
.edition, .kicker { font-weight: 650; }
.kicker { font-size: .88rem; letter-spacing: .035em; }
.page { border-top: 2px solid #879c8b; padding: 2.2rem 0; scroll-margin-top: 1rem; }
.reading-note, .description, .diagram { background: #e8e9df; border-left: .25rem solid #576c5d; padding: .4rem 1.25rem; margin: 1.5rem 0; }
blockquote { margin: 1.5rem 0; padding: .25rem 1.25rem; border-left: .25rem solid #a65a38; font-size: 1.2rem; }
blockquote p { margin: .5rem 0; }
li { margin-bottom: .45rem; }
.page-navigation { margin-top: 2rem; font-size: .92rem; }
.source-url { font-size: .94rem; overflow-wrap: anywhere; }
.note { font-size: .96rem; }
@media (max-width: 420px) { header, main, footer, nav.contents { padding-left: 1rem; padding-right: 1rem; } }
@media print { body { background: white; color: black; } .skip, .page-navigation { display: none; } a { color: black; } .page { break-before: page; } }
"""


def write_html(book, events):
    out = ["<!doctype html>", '<html lang="en">', '<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">',
           '<title>' + escape(book["title"] + " — Edition 05 reading companion") + '</title>',
           '<meta name="description" content="Complete atlas text, image and diagram descriptions, and source links. Edition 05, 7 September 2026.">',
           '<style>' + CSS + '</style></head><body>',
           '<a class="skip" href="#reading-start">Skip to the atlas text</a>',
           '<header id="top"><h1>' + html_text(book["title"]) + '</h1>',
           '<p class="edition">' + html_text(book["edition"]) + '</p>',
           '<p>Reading companion · <time datetime="2026-09-07">' + DATE + '</time></p>',
           '<p>' + html_text(book["credit"]) + '</p>',
           '<div class="reading-note"><p>' + INTRO + '</p><p>' + BOUNDARY + '</p>',
           '<p>This HTML file contains all reading content and styling. It uses no scripts, external fonts or image files. Source links open external publications.</p></div></header>',
           '<nav class="contents" id="contents" aria-labelledby="contents-heading"><h2 id="contents-heading">Contents</h2><ol>']
    for page in book["pages"]:
        out.append('<li><a href="#' + page["id"] + '">' + html_text(page["title"]) + '</a></li>')
    out.extend(['</ol></nav>', '<main id="reading-start">'])
    for e in events:
        kind, value = e["kind"], e["text"]
        text = html_text(value)
        if kind == "page":
            out.append(f'<section class="page" id="{e["id"]}" aria-labelledby="heading-{e["id"]}"><h2 id="heading-{e["id"]}">{e["number"]:02d} · {text}</h2>')
        elif kind == "page-end":
            out.append('<p class="page-navigation"><a href="#contents">Return to contents</a></p></section>')
        elif kind in {"heading", "subheading"}:
            level = "h3" if kind == "heading" else "h4"
            ident = ' id="' + e["id"] + '"' if "id" in e else ""
            out.append(f'<{level}{ident}>{text}</{level}>')
        elif kind == "quote":
            out.append('<blockquote><p>' + text + '</p></blockquote>')
        elif kind == "description":
            out.append('<aside class="description"><h3>Illustration description</h3><p>' + text + '</p></aside>')
        elif kind == "diagram":
            out.append('<aside class="diagram"><h3>Diagram description</h3><p>' + text + '</p></aside>')
        elif kind in {"ordered", "unordered"}:
            tag = "ol" if kind == "ordered" else "ul"
            out.append('<' + tag + '>' + ''.join('<li>' + html_text(item) + '</li>' for item in e["items"]) + '</' + tag + '>')
        elif kind == "source":
            out.append('<p><a href="' + escape(value, quote=True) + '">' + html_text(e["label"]) + '</a><br><span class="source-url">' + text + '</span></p>')
        else:
            out.append('<p class="' + kind + '">' + text + '</p>')
    out.extend(['</main><footer><p>' + html_text(book["credit"]) + ' · Edition 05 · ' + DATE + '</p><p><a href="#top">Return to the beginning</a></p></footer></body></html>'])
    return '\n'.join(out) + '\n'


def md_text(text):
    return re.sub(r"\[(E\d+)\]", lambda m: '[' + m[0] + '](#' + m[1] + ')', norm(text))


def write_markdown(book, events):
    out = ['# ' + book["title"], book["edition"], 'Reading companion · ' + DATE, book["credit"], INTRO, BOUNDARY,
           'This Markdown file contains all reading content. It requires no image files; source links open external publications.', '<a id="contents"></a>\n## Contents']
    out.append('\n'.join(f'{i}. [{norm(page["title"])}](#{page["id"]})' for i, page in enumerate(book["pages"], 1)))
    for e in events:
        kind, value = e["kind"], e["text"]
        text = md_text(value)
        if kind == "page":
            out.append(f'<a id="{e["id"]}"></a>\n## {e["number"]:02d} · {text}')
        elif kind == "page-end":
            out.append('[Return to contents](#contents)')
        elif kind in {"heading", "subheading"}:
            anchor = '<a id="' + e["id"] + '"></a>\n' if "id" in e else ""
            out.append(anchor + ('### ' if kind == "heading" else '#### ') + text)
        elif kind == "quote":
            out.append('> ' + value)
        elif kind == "description":
            out.append('### Illustration description\n\n' + text)
        elif kind == "diagram":
            out.append('### Diagram description\n\n' + text)
        elif kind in {"ordered", "unordered"}:
            out.append('\n'.join((f'{i}. ' if kind == "ordered" else '- ') + md_text(item) for i, item in enumerate(e["items"], 1)))
        elif kind == "source":
            out.append('[' + norm(e["label"]) + '](' + value + ')\n\nSource URL: ' + value)
        elif kind == "kicker":
            out.append('**' + text + '**')
        else:
            out.append(text)
    return '\n\n'.join(out) + '\n'


class AuditParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.texts, self.ids, self.links, self.assets = [], [], [], []
        self.skip = 0
        self.stack = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {"style", "script"}:
            self.skip += 1
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "a":
            self.links.append(attrs.get("href", ""))
        if tag in {"script", "img", "link", "iframe"}:
            self.assets.append((tag, attrs))

    def handle_endtag(self, tag):
        if tag in {"style", "script"}:
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip:
            self.texts.append(data)


def audit(book, events, html, markdown):
    parser = AuditParser()
    parser.feed(html)
    visible = norm(' '.join(parser.texts))
    missing = [s for s in strings(book) if norm(s) not in visible]
    if missing:
        raise ValueError("HTML missing source copy: " + repr(missing))
    # Check Markdown copy with its added evidence links removed, preserving labels.
    md_plain = re.sub(r"\[\[(E\d+)\]\]\(#E\d+\)", r"[\1]", markdown)
    missing_md = [s for s in strings(book) if norm(s) not in norm(md_plain)]
    if missing_md:
        raise ValueError("Markdown missing source copy: " + repr(missing_md))
    if len(parser.ids) != len(set(parser.ids)):
        raise ValueError("Duplicate HTML IDs")
    broken = [link for link in parser.links if link.startswith('#') and link[1:] not in parser.ids]
    if broken or parser.assets:
        raise ValueError("Broken navigation or external asset dependency: " + repr((broken, parser.assets)))
    image_pages = {page['id'] for page in book['pages'] if page.get('image')}
    if image_pages != set(DESCRIPTIONS):
        raise ValueError("Image descriptions do not match the current page images")
    if len(image_pages) != 25 or len(book['pages']) != 34:
        raise ValueError("Expected 34 pages and 25 images")
    print(json.dumps({"pages": len(book['pages']), "illustration_descriptions": len(DESCRIPTIONS), "diagram_descriptions": len(DIAGRAMS), "evidence_sources": len(book['evidence']), "all_source_copy_present": True, "internal_html_links_valid": True, "external_asset_dependencies": len(parser.assets), "html_bytes": len(html.encode()), "markdown_bytes": len(markdown.encode())}, indent=2))


if __name__ == '__main__':
    book = json.loads((ROOT / 'content-v5.json').read_text(encoding='utf-8'))
    events = generate(book)
    html = write_html(book, events)
    markdown = write_markdown(book, events)
    audit(book, events, html, markdown)
    (ROOT / 'reader-v5.html').write_text(html, encoding='utf-8')
    (ROOT / 'reader-v5.md').write_text(markdown, encoding='utf-8')
