---
name: personal-memory
description: Manage a user-controlled, Obsidian-backed personal memory system across projects. Use when the user asks to recall or apply personal preferences, long-term plans, work or decision habits, project context, trigger rules, recurring reviews, or to remember, update, correct, archive, or learn a preference from the current task.
---

# Personal Memory

Use the user's Obsidian vault as the canonical, human-editable memory source. Keep durable memory separate from current-task context, apply only rules whose scope matches the task, and make new inferred memories reviewable before promoting them.

## 1. Resolve the vault

Resolve the vault path in this order:

1. Use the `PERSONAL_MEMORY_VAULT` environment variable when present.
2. Use a path supplied by the user in the current conversation.
3. Use a project-local `.personal-memory/vault-path` file when present.
4. If no path is available, ask the user for the absolute path before pretending that memory was loaded.

The vault must contain `00-System/config.md`. Read that file first. Treat the vault as authoritative for memory, but do not assume that a note is applicable merely because it is discoverable.

## 2. Load memory at the right scope

At the beginning of a task, load:

- `00-System/config.md` and `00-System/Memory Operating Rules.md`.
- `10-User/` notes for global preferences, work style, decision principles, and long-term plans.
- The active project's `20-Projects/<project>/` notes when the project can be identified.
- Matching rules under `30-Triggers/`.

Use this scope precedence when instructions conflict:

1. Explicit instruction in the current user message.
2. Active-task or active-project memory.
3. Global user memory.
4. General defaults.

Prefer the more specific rule when two notes have equal authority. If a memory note is marked `status: archived`, `status: rejected`, or has passed `expires`, do not apply it.

Do not dump the whole vault into the response. Summarize only the memory that materially affected the current task, for example: `已应用：先给结论、保留现有改动、项目规则优先于全局偏好。`

## 3. Apply triggers

Treat triggers as declarative rules, not as prose suggestions. A trigger has an event, a condition, an action, a scope, and an enabled state. Common events are:

- `project_start`: identify the project and load relevant memory.
- `task_start`: load only memory relevant to the request.
- `user_correction`: record a candidate preference when the user corrects behavior.
- `repeated_request`: detect a repeated explicit request that may become a trigger.
- `project_end`: extract decisions, stable preferences, and unresolved questions.
- `review_due`: review notes whose `review_after` date has arrived.

For every matched trigger, execute its actions in order. Respect `ask_confirmation`, `max_frequency`, and `cooldown_days`. If a trigger says to update memory but the evidence is only an inference, create a candidate in `00-Inbox/` instead of changing a canonical user note.

## 4. Learn from explicit behavior

Learn cautiously from the user's explicit requests and corrections:

- An explicit `记住/保存/以后都这样/更新偏好` instruction may be recorded directly in the appropriate scope.
- A repeated request, correction, or manually initiated read is a candidate for learning; do not silently promote it after one occurrence.
- When the same behavior appears at least twice, or the user explicitly asks to learn it, create a candidate memory or trigger with `status: candidate` and include evidence dates and examples.
- Ask for confirmation when promoting a candidate to `status: active`, unless the user explicitly authorized automatic promotion for that trigger class.
- Never infer a global preference from a project-specific constraint.

Use `00-Inbox/` for candidates. A candidate must state what was observed, the proposed rule, its scope, confidence, and the decision needed from the user.

## 5. Write and update memory

Write to the narrowest appropriate note:

- Global preference: `10-User/`.
- Project-specific context or decision: `20-Projects/<project>/`.
- Trigger or recurring behavior: `30-Triggers/`.
- Unconfirmed inference: `00-Inbox/`.
- Obsolete material: `40-Archive/`.

Preserve the existing note's structure and history. Prefer a small append or targeted edit over rewriting an entire note. Keep frontmatter valid YAML. Add `source`, `last_confirmed`, and `review_after` when creating or materially changing durable memory.

When the user asks to forget or correct something, update the canonical note and, when useful, retain a short archive record rather than leaving contradictory active notes. Never claim a memory was saved unless the file was actually written successfully.

## 6. End-of-task review

Before finishing a substantial task, check for:

- Decisions that should be recorded for the active project.
- A stable user preference explicitly stated or repeatedly demonstrated.
- A repeated workflow that merits a candidate trigger.
- Unresolved questions or follow-up dates.

Only write directly when the user requested saving/updating or an active trigger explicitly permits it. Otherwise present a concise proposed update and its target note. For an approved update, write it and report the exact note path.

## 7. Handle missing or conflicting data

If the vault is unavailable, say so and continue using only the current conversation; do not fabricate remembered preferences. If a note is ambiguous, show the conflict and ask which rule should win. If the vault contains malformed frontmatter, preserve the content and report the validation issue rather than silently normalizing unrelated notes.

For schemas, statuses, and examples, read [references/memory-schema.md](references/memory-schema.md).
