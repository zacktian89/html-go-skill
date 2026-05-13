# HTML Artifact Generator Skill

Generate polished standalone single-file HTML artifacts from Markdown files, conversation context, reports, plans, PR reviews, diagrams, explainers, prototypes, and editor-style workflows.

This repository is prepared for GitHub distribution and skill marketplace submission.

## Contents

- `skills/html-artifact-generator/` - source skill folder
- `dist/html-artifact-generator.skill` - packaged distributable skill archive
- `marketplaces/codex-skill.json` - generic marketplace listing metadata
- `scripts/package.ps1` - local packaging helper

## Install

Use the packaged archive:

```powershell
Copy-Item .\dist\html-artifact-generator.skill $env:USERPROFILE\Downloads\
```

Or install from source by copying the skill folder into your Codex skills directory:

```powershell
Copy-Item .\skills\html-artifact-generator "$env:USERPROFILE\.codex\skills\" -Recurse
```

## Package

Run:

```powershell
.\scripts\package.ps1
```

The script validates the skill and writes `dist/html-artifact-generator.skill`.

## Publish Checklist

1. Create a GitHub repository named `html-artifact-generator-skill`.
2. Push this project to GitHub.
3. Create a GitHub Release and attach `dist/html-artifact-generator.skill`.
4. Replace the placeholder GitHub URL in `marketplaces/codex-skill.json`.
5. Submit `marketplaces/codex-skill.json` to any skill marketplace that accepts JSON listings, adapting field names if required.

## License

No license has been selected yet. Add a license before public release if you want others to reuse or modify the skill.
