---
type: system-config
scope: global
status: active
---

# Personal Memory configuration

## Vault identity

- Vault name: `Personal Memory`
- Project directory: `20-Projects/`
- Candidate directory: `00-Inbox/`
- Trigger directory: `30-Triggers/`

## Operating preferences

- Load global memory at the start of a relevant task: `true`
- Load project memory when a project is identifiable: `true`
- Propose inferred memory before promoting it: `true`
- Allow direct writes only after explicit user instruction or an active rule: `true`
- Summarize applied memory instead of dumping notes: `true`
- Default review interval for stable preferences: `90 days`

## Integration

Set `PERSONAL_MEMORY_VAULT` to the absolute path of this vault when using the Skill. If the environment variable is unavailable, provide the path in the conversation or create a project-local `.personal-memory/vault-path` file.

## Date convention

Use ISO dates (`YYYY-MM-DD`) and the user's local timezone. Keep dates in frontmatter and use Obsidian links for related notes.

