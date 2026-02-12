# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

三国 AI 叙事创作项目——用 AI 作为核心创作引擎，产出三国背景下的科幻故事（披着玄幻外衣的硬科幻）。遵循"先剧本、后游戏"路线，全部精力集中在剧情质量上。

## Architecture: Content Pipeline

```
人类设计角色+场景 → 导演AI编排互动 → 独立角色AI自由碰撞
    → 审阅AI评分 → 低分砍掉/中分优化/高分保留 → 人类串联成章
```

四个 Claude Code skill 对应流水线的四个环节：

| Skill | 职责 | 输出路径 |
|-------|------|----------|
| `character-creator` | 创建/编辑角色档案 | `characters/<id>.md` |
| `scene-designer` | 设计场景舞台 | `scenes/<id>.md` |
| `director-ai` | 编排多角色互动 | `content/draft-<scene>-<timestamp>.md` |
| `story-reviewer` | 评分与审阅 | `content/reviews/review-<draft>.md` |

## Directory Structure

- `characters/` — 角色档案（kebab-case ID，如 `lin-yi.md`、`zhang-fei.md`）
- `scenes/` — 场景档案（如 `yidu-market.md`、`chibi-ruins.md`）
- `content/` — 产出内容：章节 `chapter-NNN.md`、草稿 `draft-*`、审阅 `reviews/`
- `design/` — 设计文档
  - `design/worldbuilding.md` — 世界观：双层嵌套现实、能量品级体系、权限逻辑、揭秘节奏
  - `design/style-guide.md` — 风格指南：叙事声音、隐喻替代系统、禁用词汇表、写作约束
- `.claude/skills/` — 四个 skill 的定义和参考资料

## Key Design Constraints

所有创作内容必须遵守：

1. **无人无敌** — 再强的角色也有明确上限和克制
2. **皆可殒命** — 任何角色都可能死亡
3. **皆会犯错** — 判断失误是剧情张力的来源
4. **超自然有代价** — 异能必须定义清晰的限制和使用代价
5. **时间锚定** — 所有场景设定在赤壁之战之后
6. **隐喻包装** — 里世界叙事中科幻概念必须通过古风隐喻表达，严禁现代计算机术语（详见 `design/style-guide.md`）

## Attribute System

五维属性采用光荣三国志式十分制：武力、智力、体力、魅力、政治。基准校准见 `.claude/skills/character-creator/references/attributes.md`。主角（如林一）不应有极端属性值，留出成长空间。

## ID & Naming Conventions

- 角色 ID：`<姓拼音>-<名拼音>`（如 `lin-yi`、`guan-yu`）
- 场景 ID：`<地点>-<特征>`（如 `yidu-market`、`changsha-prison`）
- 所有 ID 全小写 + 连字符，文件名与 frontmatter 中的 `id` 字段一致

## Multi-AI Team Setup

使用 Claude Code teams 进行多角色模拟时，Director 作为 team lead，每个角色由独立 general-purpose agent 驱动。完整配置方案见 `.claude/skills/director-ai/references/team-setup.md`。

## Language

项目叙事内容和文档使用简体中文。ID、文件名、代码层面使用英文。与用户交流使用简体中文。
