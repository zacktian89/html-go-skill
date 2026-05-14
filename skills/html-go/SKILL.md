---
name: html-go
description: Generate polished standalone single-file HTML artifacts from conversation context, Markdown files, plans, PR reviews, reports, diagrams, explainers, prototypes, editor-like workflows, or requests for Thariq-style "Unreasonable Effectiveness of HTML" deliverables. Use when the user asks to convert discussion or .md content into a browser-ready HTML file, requests an AI-generated HTML artifact instead of Markdown, or invokes html-go.
---

# HTML Go

## Overview

Turn a finished discussion, plan, review, report, or Markdown source into a browser-ready HTML artifact. The artifact must be a single `.html` file with inline CSS and optional inline JavaScript, visually following the Thariq-style HTML examples without copying their source verbatim.

## Workflow

1. Determine the source:
   - If the user provides a Markdown file path, read it and transform its intent into an artifact.
   - Otherwise, use the relevant conversation context and the user's latest request.
2. Load references as needed:
   - Read `references/scenario-map.md` to choose the primary scenario.
   - Read `references/style-system.md` before writing the HTML.
   - Read `references/pattern-prompts.md` for the chosen scenario's structure.
3. Select exactly one primary scenario from the 20 scenario map. Combine a secondary pattern only when the source clearly needs it, such as an implementation plan with an embedded flowchart.
4. Write the artifact to `./html-artifacts/YYYYMMDD-HHMM-<slug>.html` relative to the current workspace. Create the directory when needed.
5. Run `scripts/validate_html_artifact.py <path-to-html>` and fix blocking errors before responding.
6. Reply with the generated file path and one concise summary of what the artifact contains. Do not paste the full HTML unless the user explicitly asks.

## Output Rules

- Produce original standalone HTML: one file, inline `<style>`, optional inline `<script>`, no external CSS, JS, fonts, images, or CDNs. Ordinary clickable source/reference links using `<a href="https://...">` are allowed when they do not load external page assets into the artifact.
- Do not add boilerplate or self-referential footer text such as "this is a single-file HTML artifact", "all styles are inline", or generic generation notes. Only include a footer when it adds user-facing content, such as required attribution, source links, legal notes, or domain-specific caveats.
- Preserve the source language. Chinese input should produce Chinese page labels and content; English input should produce English labels and content.
- For Chinese artifacts, prefer a modern CJK font stack: `Noto Sans SC`, `Source Han Sans SC`, `PingFang SC`, `Hiragino Sans GB`, `Microsoft YaHei UI`, `Microsoft YaHei`, `system-ui`, `sans-serif`. Use `Noto Serif SC` / `Source Han Serif SC` only for pull quotes or editorial accents.
- Transform Markdown into an artifact. Do not simply render Markdown paragraphs in a generic page.
- Use interaction only where it improves the artifact: filters, tabs, accordions, copy buttons, drag/drop boards, slide navigation, or live preview.
- For presentation or slide-deck artifacts, primary content must be paginated into additional slides when it exceeds the current viewport. Do not make the presenter rely on vertical scrolling to see core content; internal slide scrolling is only a fallback for appendix-style material.
- Include copy/export buttons only for editor-style artifacts.
- If the source is thin, create a useful page anyway and include a small "Open questions" or "Missing context" section.
- Escape untrusted source text before placing it in HTML. Treat generated JavaScript as code that must be simple and auditable.

## Quality Bar

- The page should feel like a finished deliverable someone would open in a browser, not a decorated transcript.
- Use strong visual hierarchy: eyebrow, serif title, compact summary, numbered sections, tables/cards/diagrams chosen to fit the content.
- Keep text scannable. Prefer side-by-side comparison, timelines, risk tables, annotated blocks, and collapsible details over long prose.
- For slide decks, verify each slide fits in desktop presentation mode without vertical scrolling. Split dense diagrams, tables, and multi-card comparisons across slides.
- Ensure mobile responsiveness with grid fallbacks and no horizontal overflow except intentional code/diff panels.
