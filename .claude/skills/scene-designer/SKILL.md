---
name: scene-designer
description: Design and manage narrative scenes for the Three Kingdoms AI project. Use when the user wants to create a new scene, edit an existing scene, or prepare a stage for character interactions. Triggers on requests like "设计场景", "创建场景", "new scene", or when working with files in scenes/ directory.
---

# Scene Designer

Design scenes that serve as stages for AI-driven character interactions. Each scene defines the physical, temporal, and social context where characters collide.

## Scene Template

Save scene files to `scenes/<scene-id>.md`:

```markdown
---
id: <英文短标识，如 yidu-market、chibi-ruins>
name: <场景名称>
time: <时间点描述>
location: <地理位置>
status: draft | ready | used
# draft=设计中  ready=可用于互动  used=已产出内容
---

# <场景名称>

## 时间与背景
- **时间**: <具体到季节/月份，需在赤壁之战之后>
- **已发生的关键事件**: <列出影响此场景的历史/故事事件>

## 地理风貌
<2-3段描写，包含地形、气候、标志性景观>

## 人文风貌
- **当地势力**: <哪方控制此地，控制力度>
- **民生状况**: <百姓生活、经济、社会氛围>
- **流言与暗流**: <当地传闻、暗中势力>

## 环境细节示例

### 细节1: <感官类别>
<一段沉浸式的环境描写，调动特定感官>

### 细节2: <感官类别>
<一段沉浸式的环境描写>

### 细节3: <感官类别>
<一段沉浸式的环境描写>

## 场景张力
- **核心冲突**: <此场景天然存在的矛盾/张力>
- **潜在引爆点**: <哪些元素可能激化冲突>

## 可用道具与资源
<场景中可被角色利用的物件、地形、机关等>
```

## Design Principles

1. **时间锚定** — 所有场景设定在赤壁之战之后，确保历史一致性
2. **感官丰满** — 环境细节应覆盖视觉、听觉、嗅觉、触觉中至少三种
3. **内建张力** — 好场景自带冲突种子，不需要角色刻意制造矛盾
4. **可交互性** — 场景中应包含角色可以利用的物理元素

## Scene ID Convention

ID 使用全小写英文 + 连字符，格式为 `<地点>-<特征>`，如 `yidu-market`、`chibi-ruins`、`changsha-prison`。

## Workflow: Create

1. **Determine purpose** — 向用户确认：这个场景要承载什么样的冲突或故事节点？
2. **Set temporal context** — 确定时间点，列出此刻已发生的关键事件
3. **Build geography** — 先粗后细：大地理 → 具体地点 → 微观细节
4. **Layer humanity** — 添加人文层：势力、民生、暗流
5. **Add sensory details** — 写 2-3 个不同感官维度的环境片段
6. **Define tension** — 明确核心冲突和潜在引爆点
7. **Save file** — Write to `scenes/<scene-id>.md`，status 设为 `draft`

## Workflow: Edit

1. **Load scene** — 读取 `scenes/<scene-id>.md`
2. **Identify changes** — 与用户确认要修改的部分
3. **Apply edits** — 修改内容，确保与时间线和已有场景一致
4. **Re-check principles** — 重新验证 Design Principles（感官丰满度、内建张力等）
5. **Update status** — 如有重大改动，将 status 退回 `draft`

## Workflow: Review

1. **Load scene** — 读取目标场景文件
2. **Principle audit** — 逐条检查 Design Principles
3. **Completeness check** — 确认模板每个小节已填充且非占位符
4. **Tension quality** — 评估核心冲突是否足够驱动角色互动
5. **Report** — 向用户报告问题及改进建议

## References

`references/` 目录用于存放地理、历史等参考资料。添加参考资料时直接放入该目录即可。
