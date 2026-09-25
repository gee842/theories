# Planner Context: Single‑Page Meta‑Attractor Website

Purpose: brief the planner on what exists, where it lives, and how to turn it into a production‑ready single‑page site with layered depth (Public, Practitioner, Scholar).

## Goals & Audience
- One page that works for the public, with deeper tracks for practitioners (incl. policy) and scholars.
- Explain the Meta‑Attractor, today’s loops, diagnostics, AI/AGI/ASI readiness, remedies, and actions.

## Directory Map (authoritative sources)
- Originals (essays): `meta_attractor/` — raw materials (no direct rendering).
- Processed context (canonical for the site): `meta_attractor_context/`
  - Copy & structure
    - `site_copy.md` (full Public‑first page copy with [Q..] anchors)
    - `site_outline.md` (sections, aims, word targets)
    - `hero.md` (Public‑first + Policy‑first variants)
    - `audience_layers.md` (what each layer sees)
    - `crosswalk.md` (sections → sources/artifacts)
    - `quotes_and_anchors.md` ([Q..] → source files; add line anchors during build)
    - `section_ids.json` (stable slugs for in‑page navigation)
    - `content_manifest.json` (index of all artifacts for build tooling)
  - Knowledge & guidance
    - `glossary.md`, `claims.md` (core + extended), `diagnostics.md`
    - AI readiness: `ai_agi_asi_readiness.md`, `ai_readiness_variants.md`, `ai_gating.mmd`
    - Governance: `governance_blueprint.md`, `policy_one_pager.md`
  - Visuals & data
    - Concept maps: `knowledge_map.mmd`, `metrics_visuals.mmd`
    - Case studies: `case_studies/*.md` + data CSVs under `data/`
- Working notes (non‑authoritative): `workspace/`

## Rendering Requirements
- Sections: use IDs from `section_ids.json`. Content source is `site_copy.md` (Public), with layer‑specific inserts from variants.
- Layering: toggle display for Public/Practitioner/Scholar per `audience_layers.md`. Keep DOM single‑page; hide/show per layer.
- Footnotes: `[Q..]` IDs in `site_copy.md` map to `quotes_and_anchors.md`; during build, expand to footnotes or popovers.
- Visuals: render Mermaid (`knowledge_map.mmd`, `ai_gating.mmd`, subsets of `metrics_visuals.mmd`) to SVG at build time.
- Charts: read CSVs in `data/` and render PWC/PDI/SC (and simple quadrants) client‑side (e.g., Vega‑Lite) or pre‑generate SVGs.

## Minimal Tech Stack (suggested)
- Static build (Astro/Next SSG/Vite + Remark). Mermaid via `@mermaid-js/mermaid-cli` (SVG). Charts via Vega‑Lite (or prebuilt SVGs).
- Content loader reads `content_manifest.json` to assemble sections; all paths are workspace‑relative.

## Acceptance Checklist
- All sections in `site_outline.md` rendered with anchors from `section_ids.json`.
- Layer toggles working; defaults to Public; Practitioner/Scholar add content blocks not visible to Public.
- Footnotes from `[Q..]` resolve to sources in `quotes_and_anchors.md` (line anchors may be added later).
- Mermaid diagrams and CSV charts display; fallback images provided if JS disabled.
- Mobile‑first, accessible (headings, alt text, keyboard nav), and fast (static assets, no heavy JS by default).

## Planner Task Seeds
- Choose SSG + Markdown pipeline; wire `content_manifest.json`.
- Build Mermaid → SVG step; embed SVGs into the page.
- Implement layer toggle (URL param + local storage).
- Implement footnotes/popovers from `[Q..]` → `quotes_and_anchors.md`.
- Render charts from CSVs (or pre‑generate) for case studies.
- Add tests: broken links, missing IDs, missing footnotes, asset existence.
