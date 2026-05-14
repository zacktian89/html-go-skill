# HTML Go

HTML Go 是一个 Codex skill，用来把 Markdown、讨论记录、方案文档、评审意见、报告、流程图说明或产品原型描述，转换成可直接在浏览器打开的单文件 HTML 成品。

它适合用在这些场景：

- 把一篇 Markdown 文章做成视觉层次更强的网页稿
- 把需求分析、架构方案、PR review 或复盘报告做成可展示页面
- 把长讨论整理成带时间线、风险表、对比卡片或折叠详情的 HTML artifact
- 把演示材料做成分页式浏览器 slides
- 把轻量编辑器、看板、筛选器或复制导出工具做成一个本地 HTML 文件

## 实际效果

使用 HTML Go 后，输出不是普通 Markdown 渲染页，而是一个完整的 `.html` 文件：

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

## 安装

从源码安装：

```powershell
Copy-Item .\skills\html-go "$env:USERPROFILE\.codex\skills\" -Recurse
```

或者使用打包产物：

```powershell
Copy-Item .\dist\html-go.skill $env:USERPROFILE\Downloads\
```

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

1. 创建 GitHub 仓库 `html-go`。
2. 推送本项目。
3. 创建 GitHub Release。
4. 上传 `dist/html-go.skill`。
5. 把 `marketplaces/codex-skill.json` 里的 GitHub URL 替换为真实仓库地址。
6. 将 `marketplaces/codex-skill.json` 提交到目标 skill 市场。

## License

No license has been selected yet. Add a license before public release if you want others to reuse or modify the skill.
