---
name: character-creator
description: Create and manage character profiles for the Three Kingdoms AI narrative project. Use when the user wants to create a new character, edit an existing character, or review character design. Triggers on requests like "创建角色", "设计人物", "角色画像", "new character", or when working with files in characters/ directory.
---

# Character Creator

Create character profiles following the project's standardized format. Each character will be driven by an independent AI instance during narrative interactions.

## Character Profile Template

Save character files to `characters/<character-id>.md`. Use the following structure:

```markdown
---
id: <英文短标识，如 zhang-fei、lin-yi>
name: <角色名>
faction: <所属势力>
rank: <品级，如 八品武将、无品平民>
status: active | injured | dead | missing
---

# <角色名>

## 一句话概括
<用一句话定义角色的核心矛盾或独特性>

## 个性
- **核心性格**: <2-3个关键词>
- **行为倾向**: <面对冲突/选择时的本能反应>
- **内心矛盾**: <角色内在的张力>

## 语言风格
- **说话方式**: <口语化 / 文绉绉 / 军令式 等>
- **口头禅或标志性表达**: <1-2句>
- **语言示例**:
  > "<一句典型台词>"

## 属性（百分制）
| 属性 | 值 | 说明 |
|------|-----|------|
| 武力 | XX | <简要说明> |
| 智力 | XX | <简要说明> |
| 体力 | XX | <简要说明> |
| 魅力 | XX | <简要说明> |
| 政治 | XX | <简要说明> |

## 背景
<2-3段背景故事，交代出身、关键转折、当前处境>

## 能力与限制
- **特殊能力**: <如有，描述能力及其表现>
- **代价与限制**: <使用能力的代价、冷却、副作用>
- **弱点**: <明确的短板>

## 人际关系
- **<人物A>**: <关系描述>
- **<人物B>**: <关系描述>

## 对话与行动示例

### 示例1: <情境标题>
**情境**: <简述场景>
**行动**: <角色做了什么>
**台词**: "<角色说了什么>"

### 示例2: <情境标题>
**情境**: <简述场景>
**行动**: <角色做了什么>
**台词**: "<角色说了什么>"
```

## Design Constraints

Create characters adhering to these rules:

1. **无人无敌** — 再强的角色也有明确的上限和克制
2. **皆可殒命** — 任何角色都可能在叙事中死亡
3. **皆会犯错** — 角色的判断失误是剧情张力的来源
4. **超自然有代价** — 若角色拥有异能，必须定义清晰的限制和使用代价

## Attribute Guidelines

Attributes follow a Koei-style Hundred-point scale. See [references/attributes.md](references/attributes.md) for the full attribute system and benchmark characters.

## Character ID Convention

ID 使用全小写英文 + 连字符：`<姓拼音>-<名拼音>`，如 `zhang-fei`、`lin-yi`。原创角色同理。

## Workflow: Create

1. **Clarify concept** — 向用户确认角色核心定位（势力、品级、核心特质）
2. **Draft profile** — 填充模板，重点打磨「个性」和「对话示例」两节
3. **Check constraints** — 逐条验证 Design Constraints
4. **Calibrate attributes** — 对照 references/attributes.md 中的基准角色，确保数值合理
5. **Save file** — Write to `characters/<character-id>.md`
6. **Cross-reference** — 更新相关已有角色的「人际关系」小节

## Workflow: Edit

1. **Load current profile** — 读取 `characters/<character-id>.md`
2. **Identify changes** — 与用户确认要修改的具体部分
3. **Apply edits** — 修改指定内容，确保与其余部分一致
4. **Re-check constraints** — 修改后重新验证 Design Constraints
5. **Update cross-references** — 如人际关系变动，同步更新相关角色文件

## Workflow: Review

1. **Load profile** — 读取目标角色文件
2. **Constraint audit** — 逐条检查 Design Constraints 是否满足
3. **Attribute sanity check** — 对照基准角色校验属性合理性
4. **Completeness check** — 确认模板每个小节都已填充且非占位符
5. **Report** — 向用户报告问题及改进建议
