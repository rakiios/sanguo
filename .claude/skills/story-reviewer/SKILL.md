---
name: story-reviewer
description: Review and score AI-generated narrative content for quality. Use when the user wants to evaluate a draft, score a scene interaction, compare multiple drafts, or decide whether to keep, revise, or discard generated content. Triggers on requests like "审阅", "评分", "review", "打分", or when working with draft files in content/ directory.
---

# Story Reviewer

Evaluate AI-generated narrative drafts against quality criteria. Produce structured scores and actionable feedback to guide iteration.

## Scoring Rubric

Rate each dimension on a 1-10 scale:

| Dimension | Weight | What to Evaluate |
|-----------|--------|------------------|
| **角色一致性** | 25% | Dialogue and actions match character profiles? Language style preserved? Attributes respected? |
| **叙事张力** | 25% | Does tension escalate naturally? Are there meaningful stakes? Does the reader want to keep reading? |
| **世界观融洽** | 20% | Consistent with Three Kingdoms setting? Sci-fi elements blend naturally? No anachronisms? |
| **文学质感** | 15% | Prose quality? Sensory details? Show-don't-tell? Rhythm and pacing? |
| **创意新鲜度** | 15% | Surprises? Avoids clichés? Offers fresh angles on familiar tropes? |

**Weighted total = final score (1-10)**

## Verdict Thresholds

| Score | Verdict | Action |
|-------|---------|--------|
| 8-10 | **优秀** | Keep as-is. Flag for inclusion in story assembly. |
| 6-7.9 | **可用** | Keep with targeted revisions based on feedback. |
| 4-5.9 | **待改** | Identify core issues. Re-run the scene with adjusted parameters. |
| 1-3.9 | **重来** | Discard. Analyze root cause before retrying. |

## Review Output Template

```markdown
# Review: <draft filename>

## Scores

| Dimension | Score | Notes |
|-----------|-------|-------|
| 角色一致性 | X/10 | <one-line note> |
| 叙事张力 | X/10 | <one-line note> |
| 世界观融洽 | X/10 | <one-line note> |
| 文学质感 | X/10 | <one-line note> |
| 创意新鲜度 | X/10 | <one-line note> |
| **总分** | **X/10** | |

## Verdict: <优秀 / 可用 / 待改 / 重来>

## Highlights
- <what worked well, 2-3 points>

## Issues
- <what needs fixing, 2-3 points with specific line references>

## Revision Suggestions
- <concrete, actionable suggestions for improvement>
```

## Workflow

1. **Read draft** — Load the content file from `content/`
2. **Load context** — Read the character profiles and scene file referenced in the draft
3. **Score each dimension** — Evaluate against the rubric with specific evidence
4. **Determine verdict** — Calculate weighted total and assign verdict
5. **Write feedback** — Produce the review using the template above
6. **Save review** — Write to `content/reviews/review-<draft-filename>.md`

## Comparative Review

When multiple drafts exist for the same scene:

1. Score each draft independently first
2. Produce a comparison table:

```markdown
| Dimension | Draft A | Draft B | Draft C |
|-----------|---------|---------|---------|
| 角色一致性 | X/10 | X/10 | X/10 |
| 叙事张力 | X/10 | X/10 | X/10 |
| 世界观融洽 | X/10 | X/10 | X/10 |
| 文学质感 | X/10 | X/10 | X/10 |
| 创意新鲜度 | X/10 | X/10 | X/10 |
| **总分** | **X** | **X** | **X** |
```

3. Recommend which draft to use as the base for further iteration
4. Identify the best elements from each draft that could be merged

## Red Flags (Auto-Deduct)

Automatically deduct 2 points from the relevant dimension per occurrence (可叠加，同一维度最多扣至 1 分):

- Character breaks language style mid-scene → 角色一致性
- A low-attribute character performs at a high-attribute level without narrative justification → 角色一致性
- Supernatural ability used without paying the defined cost → 世界观融洽
- Modern vocabulary/concepts that break immersion → 世界观融洽
- A character behaves in direct contradiction to their core personality → 角色一致性

## Hard Rules

- **必须加载原始资料** — 审阅时必须读取原始角色档案和场景文件作为对照，不可凭印象评分
- **多 draft 走对比流程** — 如果同一场景存在多个 draft，优先使用上方 Comparative Review 流程
- **缺失引用即暂停** — 如果 draft 引用的角色或场景文件不存在，先向用户报告缺失资料，不进行评分
