---
name: html-go
description: Generate polished standalone single-file HTML artifacts from conversation context, Markdown files, plans, PR reviews, reports, diagrams, explainers, prototypes, editor-like workflows, WeChat Official Account paste-ready rich text, or requests for Thariq-style "Unreasonable Effectiveness of HTML" deliverables. Use when the user asks to convert discussion or .md content into a browser-ready HTML file, requests an AI-generated HTML artifact instead of Markdown, asks for WeChat/微信公众号 copy-paste HTML output, or invokes html-go.
---

# HTML Go

## Overview

Turn a finished discussion, plan, review, report, or Markdown source into a browser-ready HTML artifact. The artifact must be a single `.html` file with inline CSS and optional inline JavaScript, visually following the Thariq-style HTML examples without copying their source verbatim.

HTML Go has two output modes:

- `Artifact`: the default mode for browser-ready visual deliverables.
- `WeChat Paste`: a compatibility mode for WeChat Official Account / 微信公众号 editors. It produces a browser test page with a copy button and a paste-ready article body that uses simple HTML and inline styles.

## Workflow

1. Determine the source:
   - If the user provides a Markdown file path, read it and transform its intent into an artifact.
   - Otherwise, use the relevant conversation context and the user's latest request.
2. Determine the output mode:
   - Use `WeChat Paste` when the user asks for WeChat Official Account, 微信公众号, 公众号, rich-text editor, copy-paste HTML, paste-ready HTML, or similar wording.
   - Otherwise use `Artifact`.
3. Load references as needed:
   - Read `references/scenario-map.md` to choose the primary scenario.
   - Read `references/style-system.md` before writing the HTML.
   - Read `references/pattern-prompts.md` for the chosen scenario's structure.
4. For `Artifact`, select exactly one primary scenario from the 20 scenario map. Combine a secondary pattern only when the source clearly needs it, such as an implementation plan with an embedded flowchart.
5. For `WeChat Paste`, create a paste test page:
   - Include a visible preview and a copy button.
   - Put the actual WeChat article body in one clearly identified container such as `<article id="wechatArticle">`.
   - The copy button must write both `text/html` and `text/plain` when the browser supports `ClipboardItem`.
   - If the article includes a generated or local test image, include a PNG representation in the clipboard payload when possible.
   - Add a manual fallback that selects the article body when rich clipboard access is unavailable.
6. Write the artifact to `./html-artifacts/YYYYMMDD-HHMM-<slug>.html` relative to the current workspace. Create the directory when needed.
7. Run `scripts/validate_html_artifact.py <path-to-html>` and fix blocking errors before responding.
8. Reply with the generated file path and one concise summary of what the artifact contains. For `WeChat Paste`, also tell the user to open the file, click the copy button, and paste into the WeChat Official Account editor. Do not paste the full HTML unless the user explicitly asks.

## Output Rules

### Artifact Mode

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
- Prevent layout clipping and border crowding: every card, grid child, flow node, table wrapper, and prompt/code-like text container that sits inside CSS grid/flex must be allowed to shrink with `min-width: 0`; long identifiers, URLs, command lines, and inline-code-heavy text must use `overflow-wrap: anywhere` or an equivalent safe wrapping rule.

### WeChat Paste Mode

- The file is still a standalone HTML test page, but the copy target must be a simple article body designed for pasting into WeChat Official Account editors.
- Put all important visual styling inside the copy target as inline `style=""` attributes. The surrounding test page may use normal inline `<style>` and short JavaScript.
- Keep the copy target single-column and editor-friendly. Prefer `section`, `p`, `span`, `h1`, `h2`, `blockquote`, `ol`, `ul`, `li`, `table`, `thead`, `tbody`, `tr`, `th`, `td`, `pre`, and `code`.
- Avoid complex layout in the copy target: no CSS Grid, flexbox, fixed positioning, external assets, custom fonts, embedded scripts, forms, iframes, canvas, or SVG-only content.
- Use conservative widths and spacing for the copy target: max width around `677px`, line-height around `1.75` to `1.9`, and mobile-safe text sizes.
- Do not rely on class selectors for the pasted article body. WeChat may strip or alter classes, but inline styles are more likely to survive.
- For images, never use `file://` paths in the copy target. Use one of these paths:
  - For a compatibility test page, generate or embed a PNG data URL and also write `image/png` to the clipboard when `ClipboardItem` supports it.
  - For production articles, prefer images uploaded through the WeChat editor or stable HTTPS image URLs that the publishing workflow accepts.
  - If image persistence matters, tell the user to verify that the pasted image is uploaded or retained by the WeChat editor before publishing.
- Include a visible note in the test page telling the user how to test: open the file, click the copy button, paste into the WeChat editor, then inspect headings, quote blocks, tables, code blocks, and spacing.
- Treat the WeChat editor as the final compatibility check. Browser appearance is only a preview.

## Quality Bar

- The page should feel like a finished deliverable someone would open in a browser, not a decorated transcript.
- Use strong visual hierarchy: eyebrow, serif title, compact summary, numbered sections, tables/cards/diagrams chosen to fit the content.
- Keep text scannable. Prefer side-by-side comparison, timelines, risk tables, annotated blocks, and collapsible details over long prose.
- For slide decks, verify each slide fits in desktop presentation mode without vertical scrolling. Split dense diagrams, tables, and multi-card comparisons across slides.
- Ensure mobile responsiveness with grid fallbacks and no horizontal overflow except intentional code/diff panels. Visually check dense card grids and flow diagrams at both desktop and narrow widths; content should never touch or cross the right border of its parent.
