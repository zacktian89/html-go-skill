# Scenario Map

Choose exactly one primary scenario. Use the source intent, not only keywords. If multiple scenarios fit, pick the one that makes the artifact most useful to a human reader.

| # | Scenario | Use When | Required Shape |
|---|---|---|---|
| 1 | Three code approaches | Comparing implementation options, architecture choices, libraries, or tradeoffs | Side-by-side option cards, decision criteria, recommendation, risks |
| 2 | Visual design directions | Exploring UI directions, layout/palette options, brand feel | Live-looking design panels, palette/type samples, pros/cons, pick guidance |
| 3 | Annotated PR review | Reviewing a diff, PR, code change, or patch | PR header, risk map, file cards, annotated diff/comments, next steps |
| 4 | Module map | Explaining an unfamiliar package, service, call graph, or dependency flow | Box-and-arrow SVG/module diagram, hot path, entry points, notes |
| 5 | Living design system | Summarizing design tokens, colors, spacing, typography, components | Token swatches, type scale, spacing samples, copyable values |
| 6 | Component variants | Reviewing UI component states, sizes, intents, or accessibility states | Variant grid/contact sheet, state labels, usage notes |
| 7 | Animation sandbox | Testing/tuning motion, easing, duration, transitions | Live preview, sliders/controls, current values, implementation notes |
| 8 | Clickable flow | Demonstrating a multi-screen UX or process | Screen mockups, clickable navigation, state indicator, flow notes |
| 9 | Arrow-key slide deck | Turning a topic into a short presentation | `<section>` slides, left/right keyboard nav, progress indicator |
| 10 | SVG figure sheet | Creating illustrations/figures for an article or explainer | Figure grid, inline SVG, captions, copyable snippets if useful |
| 11 | Weekly status | Summarizing weekly progress, delivery, blockers, metrics | Shipped/slipped/next, compact chart, risks, owner/status labels |
| 12 | Incident timeline | Postmortem, outage, bug incident, operational timeline | Timeline, impact, root cause, logs/evidence, action items |
| 13 | Annotated flowchart | Process, deployment, approval, pipeline, workflow explanation | Clickable/annotated SVG flowchart, details panel, failure paths |
| 14 | Feature explainer | Explaining how a feature works in a repo/product | TL;DR, request/data path, collapsible steps, config/code tabs, FAQ |
| 15 | Concept explainer | Teaching a technical concept or mental model | Interactive or visual explainer, glossary, comparison table, examples |
| 16 | Implementation plan | Planning a feature/build/refactor for handoff | Milestones, data flow, mockups, key code/contracts, risk table, open questions |
| 17 | PR writeup | Preparing author-facing PR notes for reviewers | Motivation, before/after, file tour, review focus, test evidence |
| 18 | Ticket triage board | Prioritizing tickets, backlog, roadmap items, work buckets | Drag/drop or static kanban, filters, estimates, copy/export markdown |
| 19 | Feature flag editor | Reviewing/toggling flags, rollout states, dependencies | Grouped toggles, dependency warnings, changed-state diff/export |
| 20 | Prompt tuner | Editing prompt templates and previewing sample outputs | Editable template, variable chips, sample inputs, live rendered preview |

## Routing Defaults

- If the user asks for a plan/spec/handoff and no better scenario is clear, choose #16 Implementation plan.
- If the source is a code review or diff, choose #3 Annotated PR review.
- If the source is a status update, weekly report, or progress summary, choose #11 Weekly status.
- If the source is an outage, incident, regression, or timeline, choose #12 Incident timeline.
- If the source is educational, choose #14 for a product/repo feature and #15 for a general concept.
- If the source asks the user to manipulate items and export a result, choose #18, #19, or #20.
- If the user only asks for "make this Markdown into HTML" with no clear intent, inspect headings: plan -> #16, report -> #11/#12, review -> #3/#17, explainer -> #14/#15.
