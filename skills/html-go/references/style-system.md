# Style System

Use this visual language for all artifacts. Reproduce the feel of the original HTML examples without copying their source verbatim.

## Core Tokens

```css
:root {
  --ivory: #FAF9F5;
  --slate: #141413;
  --clay: #D97757;
  --clay-dark: #B85C3E;
  --oat: #E3DACC;
  --olive: #788C5D;
  --rust: #B04A3F;
  --gray-50: #F7F5EE;
  --gray-150: #F0EEE6;
  --gray-300: #D1CFC5;
  --gray-500: #87867F;
  --gray-700: #3D3D3A;
  --white: #FFFFFF;
  --display: "Noto Sans SC", "Source Han Sans SC", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", system-ui, sans-serif;
  --sans: "Noto Sans SC", "Source Han Sans SC", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", system-ui, -apple-system, "Segoe UI", sans-serif;
  --serif: "Noto Serif SC", "Source Han Serif SC", "Songti SC", "STSong", "SimSun", serif;
  --mono: "Cascadia Mono", "SF Mono", Consolas, "Liberation Mono", ui-monospace, monospace;
}
```

## Page Chrome

- Use `body` background `var(--ivory)`, text `var(--gray-700)`, sans font, line-height around `1.55`.
- Use a centered page container with max width between `920px` and `1180px`.
- Use generous page padding: about `48px 24px 80px`, with smaller mobile padding.
- Use `var(--display)` for `h1`, `h2`, and important Chinese headings; prefer weight 650-760, slate color.
- Use `var(--serif)` only for quotation-style pull quotes or editorial accents in Chinese pages, not as the default heading font.
- Use mono uppercase eyebrows, labels, tags, and metadata.
- Use 1.5px borders in `var(--gray-300)`, radius `8px` to `12px`.

## Common Components

- Header: eyebrow, strong display title, short summary or prompt box.
- Summary strip: 2-4 small stat cells, white background, compact labels.
- Section header: numbered mono pill plus serif section title.
- Cards: white or gray-150 background, subtle border, compact padding.
- Tags: mono text, small radius or pill, clay/olive/oat status colors.
- Tables: bordered rows, mono header labels, severity/status chips.
- Code/diff panels: slate background, mono text, horizontal overflow allowed.
- Diagrams: inline SVG with slate text, gray lines, clay emphasis, olive success paths. Keep explanatory notes outside the SVG when they are not part of a node or edge label.

## Responsive Rules

- Use CSS grid with `@media (max-width: 900px)` to collapse multi-column layouts.
- For slide-deck or presentation-style artifacts, desktop presentation mode must fit inside the current viewport: set the outer deck to `height: 100vh` and prevent body-level scrolling.
- Do not rely on vertical scrolling to deliver primary slide content in presentation mode. If a slide is taller than the remaining viewport, split it into additional slides by idea, diagram, table, or appendix segment. Use active-slide internal scrolling only as a last-resort fallback for appendix-style content.
- Avoid fixed-width content except code panels and SVG diagrams with `overflow-x: auto`.
- Put `min-width: 0` on grid/flex children that contain cards, diagrams, tables, prompts, code-like text, or nested grids. CSS grid items default to `min-width: auto`, which can make long text push cards into the right border.
- Put `overflow-wrap: anywhere` or `word-break: break-word` on labels, node titles, prompt boxes, URLs, commands, identifiers, and inline-code-heavy paragraphs. This is required for long names such as `docs_researcher`, `report_agent_job_result`, package names, and file paths.
- For multi-node flow diagrams inside cards, prefer vertical flow or `grid-template-columns: repeat(auto-fit, minmax(150px, 1fr))` for node groups. Avoid squeezing three or more nodes into a half-width column.
- Keep at least `12px` of inner breathing room between nested flow/table/card content and its parent border. If content visually touches the right border at common widths, collapse the nested grid earlier or stack it.
- When an SVG diagram is part of a presentation slide, prefer scaling it to the container with `width: min(100%, <natural-width>px); height: auto;` before falling back to horizontal scroll.
- In SVG diagrams, reserve clear space for every label and never place free-floating text over boxes, connector lines, or other labels. If a sentence explains the diagram as a whole, render it as an HTML callout below or above the diagram.
- Keep interactive controls reachable on mobile. Sticky toolbars are allowed for editor pages.
- Do not use external fonts, images, stylesheets, scripts, or icon libraries.

## Overflow-Safe CSS Pattern

Use this pattern for dense cards, flow diagrams, prompt blocks, and nested grids:

```css
.card,
.flow,
.flow-node,
.prompt-line,
.table-wrap {
  min-width: 0;
}

.flow-stack {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
}

.flow-node strong,
.prompt-line,
.long-text {
  overflow-wrap: anywhere;
  word-break: break-word;
}
```

## Interaction Rules

- Use vanilla JavaScript only.
- Keep scripts short and local to the page.
- Prefer progressive enhancement: the artifact should still be readable if JavaScript fails.
- Use buttons for copy/export, tabs, filters, toggles, slide navigation, and editor interactions.
- Do not add decorative animations unless the selected scenario is an animation/prototype artifact.
