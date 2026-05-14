# HTML Go Store Submission

## Name

HTML Go

## Slug

html-go

## Short Description

Create polished standalone HTML artifacts from Markdown, plans, reviews, reports, diagrams, and prototypes.

## Long Description

HTML Go is a Codex skill for turning Markdown files, conversation context, project plans, PR reviews, reports, flow explanations, and prototype notes into browser-ready single-file HTML artifacts.

Markdown remains excellent for capture, transport, and long-term memory. HTML Go focuses on final deliverables that benefit from layout, visual hierarchy, comparison, diagrams, interaction, slides, or lightweight editing controls.

The skill writes one self-contained `.html` file with inline CSS and optional inline JavaScript. It avoids external CSS, scripts, fonts, images, and CDNs. Generated artifacts are validated before handoff.

## Categories

- Productivity
- Writing
- Developer Tools

## Tags

- html
- artifact
- markdown
- report
- presentation
- single-file
- codex-skill

## Repository

https://github.com/zacktian89/html-go-skill

## Release

https://github.com/zacktian89/html-go-skill/releases/tag/v0.1.0

## Packaged Skill

https://github.com/zacktian89/html-go-skill/releases/download/v0.1.0/html-go.skill

## Promotional HTML

https://github.com/zacktian89/html-go-skill/releases/download/v0.1.0/README.html

## Marketplace Metadata

https://github.com/zacktian89/html-go-skill/releases/download/v0.1.0/codex-skill.json

## Example Prompts

```text
[$html-go] Turn this project plan into a standalone HTML artifact.
```

```text
[$html-go] 把这份 PR review 整理成一个可展示的 HTML artifact。
```

```text
Use $html-go to convert this Markdown report into a browser-ready page with summary, timeline, risks, and open questions.
```

## Review Notes

- No external network dependency is required for generated artifacts.
- The distributed `.skill` package contains `SKILL.md`, `agents/openai.yaml`, references, and validation script.
- The repository includes a GitHub Actions workflow that creates releases from `v*` tags and uploads the distributable assets.
