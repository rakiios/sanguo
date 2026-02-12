# Multi-Character Team Setup

## Using Claude Code Teams for Multi-Character Simulation

### Team Structure

```
Director (team lead)
├── Character Agent A (general-purpose agent, loaded with character A profile)
├── Character Agent B (general-purpose agent, loaded with character B profile)
└── Character Agent C (general-purpose agent, loaded with character C profile)
```

### Setup Steps

1. Create a team using TeamCreate with a descriptive name (e.g., "scene-yidu-encounter")
2. Create tasks for each interaction beat using TaskCreate
3. Spawn character agents using Task tool with `team_name` parameter
4. Each character agent's prompt should include:
   - The full character profile (read from `characters/<id>.md`)
   - The scene context (read from `scenes/<id>.md`)
   - Instruction to stay in character at all times
   - The current narrative context (what has happened so far)

### Director Agent Responsibilities

- Manage turn order via task assignments
- Send scene updates and other characters' actions to each character agent via SendMessage
- Collect character responses and weave them into narrative prose
- Make environmental narration decisions
- Track character health/status changes during the scene

### Character Agent Prompt Template

```
You are role-playing as [CHARACTER_NAME] in a Three Kingdoms narrative.

Your character profile:
[INSERT FULL CHARACTER PROFILE]

Current scene:
[INSERT SCENE DESCRIPTION]

What has happened so far:
[INSERT NARRATIVE CONTEXT]

Respond ONLY as [CHARACTER_NAME]. Stay true to your personality, language style, and abilities. Your actions must be consistent with your attribute levels.
```

### Collecting and Assembling Output

After the interaction concludes:
1. Director collects all character responses in sequence
2. Director writes transitional narration between beats
3. Full output is assembled and saved to `content/draft-<scene-id>-<timestamp>.md`
