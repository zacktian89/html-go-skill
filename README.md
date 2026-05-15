# HTML Go

Language: [中文](#中文) | [English](#english)

## 中文

HTML Go 是一个 Codex skill，用来把 Markdown、讨论记录、方案文档、评审意见、报告、流程图说明或产品原型描述，转换成可直接在浏览器打开的单文件 HTML 成品。

它的判断很简单：Markdown 适合记录、传输和长期保存；HTML 更适合展示、比较、交互和现场决策。HTML Go 不会要求所有内容都变成 HTML，它只在页面布局、颜色层级、图表、交互控件或可视化结构能明显提升交付质量时触发。

效果预览：[项目首页](https://zacktian89.github.io/html-go-skill/)

## 项目初衷

过去一年，AI 输出正在从“聊天窗口里的 Markdown”转向“可打开、可交互、可复用的 artifact”：

- 2024-10-03，OpenAI 发布 Canvas，把写作和代码任务放进独立工作区，明确面向“超出简单聊天”的协作式编辑。[Source](https://openai.com/index/introducing-canvas/)
- 2025-06-25，Anthropic 为 Claude Artifacts 推出独立空间，并称用户已经创建超过 5 亿个 artifacts；同一公告还把 artifacts 推向可分享、可交互的 AI-powered apps。[Source](https://claude.com/blog/build-artifacts)
- 2026-02-26，Profound 的 Markdown vs HTML AI crawler 实验显示，Markdown 对 AI crawler 流量只有方向性优势，结果不具统计显著性。这提醒我们：Markdown 的机器可读性很重要，但“最终给人看的交付物”不能只按 crawler 假设来设计。[Source](https://www.tryprofound.com/resources/white-papers/markdown-html-llm-test)
- 2026-05，arXiv 上出现 Single-File Test，观察 68 个 single-file HTML generations 和 HTML AI Battle 实验，说明“让模型生成可运行的单文件网页”已经成为一个可被评测和讨论的方向。[Source](https://arxiv.org/abs/2605.06707)
- Thariq Shihipar 的 The Unreasonable Effectiveness of HTML 用 20 个自包含 HTML 示例展示了为什么比较、评审、设计、原型、图表、报告和编辑器类输出不应该总被压扁成 Markdown。[Source](https://thariqs.github.io/html-effectiveness/)

HTML Go 的初衷就是把这个趋势变成一个可复用的 Codex skill：保留 Markdown 的轻便，同时在需要“真正被看懂、被点击、被讨论”的时候，把输出升级成单文件 HTML。

## 实际效果

使用 HTML Go 后，输出会成为一个完整的 `.html` 文件，而非普通 Markdown 渲染页：

- 所有 CSS 和必要 JavaScript 都内联在单文件中
- 不依赖 CDN、外部字体、外部图片或构建工具
- 会根据内容选择合适的信息结构，例如时间线、对比表、风险矩阵、卡片网格、折叠详情、分页演示或编辑器布局
- 中文内容会保留中文表达，并使用适合中文阅读的字体栈
- 页面支持移动端响应式布局，避免横向溢出
- 输出前会运行 `validate_html_artifact.py` 做基础质量检查

示例调用：

```text
Use $html-go to turn this project plan into a standalone HTML artifact.
```

示例输出路径：

```text
html-artifacts/20260514-1015-project-plan.html
```

生成后的页面通常包含：

- 顶部摘要和关键信息
- 分区化正文
- 针对内容选择的图表式结构
- 必要的交互控件，例如 tabs、filters、accordions、copy buttons 或 slide navigation
- 对薄弱输入自动补充的 open questions 或 missing context 区块

## 仓库内容

- `skills/html-go/` - skill 源码
- `dist/html-go.skill` - 可分发的 skill 包
- `marketplaces/codex-skill.json` - 市场上架元数据
- `scripts/package.ps1` - 校验和打包脚本
- `index.html` - 使用 HTML Go 风格生成的 GitHub Pages 首页

## 安装

### Codex

```powershell
git clone git@github.com:zacktian89/html-go-skill.git
cd html-go-skill
New-Item -ItemType Directory "$env:USERPROFILE\.codex\skills" -Force
Copy-Item .\skills\html-go "$env:USERPROFILE\.codex\skills\html-go" -Recurse -Force
```

安装后在 Codex 里使用 `$html-go` 触发。

### Claude Code

Claude Code 支持 Agent Skills，可以把同一个 skill 目录安装到个人 skill 目录：

```powershell
git clone git@github.com:zacktian89/html-go-skill.git
cd html-go-skill
New-Item -ItemType Directory "$env:USERPROFILE\.claude\skills" -Force
Copy-Item .\skills\html-go "$env:USERPROFILE\.claude\skills\html-go" -Recurse -Force
```

安装后在 Claude Code 里使用 `/html-go`，或让 Claude 根据任务自动调用。

### Gemini CLI

Gemini CLI 使用自定义 slash command。先创建命令文件：

```powershell
New-Item -ItemType Directory "$env:USERPROFILE\.gemini\commands" -Force
@'
description = "Create a standalone HTML artifact from Markdown, plans, reviews, reports, or discussion context."
prompt = """
Use the HTML Go workflow: turn the provided Markdown, file path, or conversation context into a polished standalone single-file HTML artifact.

Rules:
- Write one .html file with inline CSS and optional inline JavaScript.
- Do not use CDN, external fonts, external images, or build tools.
- Choose a structure that fits the content, such as a timeline, comparison table, risk matrix, card grid, tabs, accordions, slide deck, or editor layout.
- Preserve the source language.
- Put the output under html-artifacts/YYYYMMDD-HHMM-<slug>.html when filesystem tools are available.
"""
'@ | Set-Content "$env:USERPROFILE\.gemini\commands\html-go.toml" -Encoding UTF8
```

安装后在 Gemini CLI 里使用 `/html-go` 加上你的文件路径或需求。

### 打包文件

`dist/html-go.skill` 是给支持 `.skill` 包导入的工具或市场使用的分发包。如果工具只能读取目录形式的 skill，优先安装 `skills/html-go/`。

## 用法

在 Codex 中显式调用：

```text
[$html-go] 把这份 Markdown 转成一个浏览器可打开的 HTML 页面
```

也可以直接提出目标：

```text
把这份 PR review 整理成一个可展示的 HTML artifact
```

如果提供 Markdown 文件路径，HTML Go 会读取文件内容并转换；如果没有提供文件，它会使用当前对话里最相关的上下文。

默认输出位置是当前工作区下：

```text
html-artifacts/YYYYMMDD-HHMM-<slug>.html
```

### 微信公众号复制粘贴模式

如果目标是粘贴到微信公众号后台编辑器，直接说明 `微信公众号`、`公众号`、`WeChat Paste` 或 `复制粘贴 HTML`。HTML Go 会生成一个单文件测试页，其中包含预览正文和复制按钮；真正要粘贴的正文会尽量使用简单标签和内联样式。

示例：

```text
[$html-go] 把这篇 Markdown 转成微信公众号可复制粘贴的 HTML
```

```text
Use $html-go WeChat Paste mode for this article.
```

使用步骤：

1. 打开生成的 `html-artifacts/YYYYMMDD-HHMM-<slug>.html`。
2. 点击页面里的复制按钮。
3. 到微信公众号后台编辑器中粘贴。
4. 检查标题、引用块、表格、代码块和段落间距是否保留。

图片处理：

- 不要把 `file://` 本地图片路径放进要粘贴的正文。
- 测试页可以用内嵌 PNG 图片，并在复制时尝试同时写入 `image/png` 剪贴板数据。
- 正式发布时，优先让图片通过公众号编辑器上传，或使用发布流程确认可用的稳定 HTTPS 图片地址。
- 发布前检查粘贴后的图片是否已经被公众号编辑器保留或上传。

这个模式关注的是公众号编辑器里的最终效果；浏览器中的页面只是复制和预览入口。

## 打包

运行：

```powershell
.\scripts\package.ps1
```

脚本会先验证 skill，再生成：

```text
dist/html-go.skill
```

## 上架发布

1. 创建或打开 GitHub 仓库 `html-go-skill`。
2. 推送本项目。
3. 创建 GitHub Release。
4. 上传 `dist/html-go.skill`。
5. 将 `marketplaces/codex-skill.json` 提交到目标 skill 市场。

## License

No license has been selected yet. Add a license before public release if you want others to reuse or modify the skill.

## English

HTML Go is a Codex skill that turns Markdown files, conversation context, plans, PR reviews, reports, flow explanations, and prototype notes into polished standalone HTML artifacts that open directly in a browser.

The position is intentionally narrow: Markdown is excellent for capture, transport, and long-term memory; HTML is better when the output needs layout, comparison, interaction, diagrams, or presentation polish. HTML Go does not turn every answer into HTML. It chooses HTML only when the medium materially improves the deliverable.

Live preview: [Project homepage](https://zacktian89.github.io/html-go-skill/)

## Why This Exists

AI output is moving from “Markdown in a chat box” toward artifacts that can be opened, edited, shared, and used:

- On 2024-10-03, OpenAI introduced Canvas as a separate interface for writing and coding work that goes beyond simple chat. [Source](https://openai.com/index/introducing-canvas/)
- On 2025-06-25, Anthropic introduced a dedicated space for Claude Artifacts and said users had created over half a billion artifacts. The same announcement pushed artifacts toward shareable, interactive AI-powered apps. [Source](https://claude.com/blog/build-artifacts)
- On 2026-02-26, Profound published a Markdown vs HTML AI crawler experiment. Markdown showed a directional but statistically insignificant crawler traffic advantage, which is a useful reminder: machine readability matters, but human-facing deliverables should be designed for human use. [Source](https://www.tryprofound.com/resources/white-papers/markdown-html-llm-test)
- In May 2026, the arXiv Single-File Test paper studied 68 single-file HTML generations across public HTML AI Battle experiments, showing that single-file web generation is becoming a trackable evaluation surface. [Source](https://arxiv.org/abs/2605.06707)
- Thariq Shihipar's The Unreasonable Effectiveness of HTML collected 20 self-contained HTML examples showing why comparisons, reviews, design sheets, prototypes, diagrams, reports, decks, and mini-editors should not always be flattened into Markdown. [Source](https://thariqs.github.io/html-effectiveness/)

HTML Go turns that shift into a reusable Codex skill: keep Markdown for lightweight text, but upgrade the final artifact to HTML when people need to scan, compare, click, present, or decide.

## What It Produces

HTML Go generates a complete `.html` file, not a generic Markdown preview:

- Inline CSS and optional inline JavaScript in one file
- No CDN, external fonts, external images, or build step
- Structure chosen for the content: timelines, comparison tables, risk matrices, card grids, accordions, slide decks, or editor-style layouts
- Chinese content stays Chinese, with a modern CJK font stack
- Responsive layout for desktop and mobile
- Validation through `validate_html_artifact.py` before handoff

Example prompt:

```text
Use $html-go to turn this project plan into a standalone HTML artifact.
```

Example output path:

```text
html-artifacts/20260514-1015-project-plan.html
```

The generated page usually includes:

- A compact summary
- Structured sections
- Visual tables, cards, diagrams, or timelines selected for the source
- Useful interaction such as tabs, filters, accordions, copy buttons, or slide navigation
- Open questions or missing context when the input is thin

## Repository Layout

- `skills/html-go/` - skill source
- `dist/html-go.skill` - packaged distributable skill
- `marketplaces/codex-skill.json` - marketplace listing metadata
- `scripts/package.ps1` - validation and packaging helper
- `index.html` - GitHub Pages homepage generated in the style of HTML Go

## Install

### Codex

```powershell
git clone git@github.com:zacktian89/html-go-skill.git
cd html-go-skill
New-Item -ItemType Directory "$env:USERPROFILE\.codex\skills" -Force
Copy-Item .\skills\html-go "$env:USERPROFILE\.codex\skills\html-go" -Recurse -Force
```

Use `$html-go` in Codex after installation.

### Claude Code

Claude Code supports Agent Skills, so the same skill directory can be installed as a personal skill:

```powershell
git clone git@github.com:zacktian89/html-go-skill.git
cd html-go-skill
New-Item -ItemType Directory "$env:USERPROFILE\.claude\skills" -Force
Copy-Item .\skills\html-go "$env:USERPROFILE\.claude\skills\html-go" -Recurse -Force
```

Use `/html-go` in Claude Code, or let Claude invoke it automatically when the request matches.

### Gemini CLI

Gemini CLI uses custom slash commands. Create a command file:

```powershell
New-Item -ItemType Directory "$env:USERPROFILE\.gemini\commands" -Force
@'
description = "Create a standalone HTML artifact from Markdown, plans, reviews, reports, or discussion context."
prompt = """
Use the HTML Go workflow: turn the provided Markdown, file path, or conversation context into a polished standalone single-file HTML artifact.

Rules:
- Write one .html file with inline CSS and optional inline JavaScript.
- Do not use CDN, external fonts, external images, or build tools.
- Choose a structure that fits the content, such as a timeline, comparison table, risk matrix, card grid, tabs, accordions, slide deck, or editor layout.
- Preserve the source language.
- Put the output under html-artifacts/YYYYMMDD-HHMM-<slug>.html when filesystem tools are available.
"""
'@ | Set-Content "$env:USERPROFILE\.gemini\commands\html-go.toml" -Encoding UTF8
```

Use `/html-go` in Gemini CLI with a file path or request.

### Packaged Artifact

`dist/html-go.skill` is the distributable package for tools or marketplaces that support `.skill` imports. If a tool reads skill directories directly, install `skills/html-go/` first.

## Usage

Invoke it explicitly in Codex:

```text
[$html-go] Turn this Markdown file into a browser-ready HTML page.
```

Or ask naturally:

```text
Turn this PR review into a polished HTML artifact.
```

When you provide a Markdown path, HTML Go reads and transforms that file. Without a file path, it uses the most relevant conversation context.

Default output location:

```text
html-artifacts/YYYYMMDD-HHMM-<slug>.html
```

### WeChat Official Account Paste Mode

When the target is the WeChat Official Account editor, mention `WeChat Paste`, `WeChat Official Account`, `微信公众号`, `公众号`, or `copy-paste HTML`. HTML Go will generate a standalone test page with a preview article and a copy button. The article body intended for pasting uses simple tags and inline styles.

Examples:

```text
Use $html-go to turn this Markdown into WeChat Official Account paste-ready HTML.
```

```text
[$html-go] WeChat Paste mode for this article.
```

How to use it:

1. Open the generated `html-artifacts/YYYYMMDD-HHMM-<slug>.html`.
2. Click the copy button in the page.
3. Paste into the WeChat Official Account editor.
4. Check headings, quote blocks, tables, code blocks, and paragraph spacing.

Image handling:

- Do not put `file://` local image paths in the pasted article body.
- A test page may use an embedded PNG and try to include `image/png` clipboard data during copy.
- For production publishing, prefer images uploaded through the WeChat editor or stable HTTPS image URLs accepted by the publishing workflow.
- Before publishing, verify that pasted images are retained or uploaded by the WeChat editor.

This mode optimizes for the final result inside the WeChat editor; the browser page is only the preview and copy surface.

## Package

Run:

```powershell
.\scripts\package.ps1
```

The script validates the skill and writes:

```text
dist/html-go.skill
```

## Publish

1. Open the GitHub repository `html-go-skill`.
2. Push this project.
3. Create a GitHub Release.
4. Upload `dist/html-go.skill`.
5. Submit `marketplaces/codex-skill.json` to the target skill marketplace.

## License

No license has been selected yet. Add a license before public release if you want others to reuse or modify the skill.
