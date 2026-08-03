# Memory schema

Use YAML frontmatter for notes that the skill may select or update. Keep the body readable in Obsidian.

## Common fields

```yaml
type: preference | principle | plan | project-context | decision | trigger | review
scope: global | project:<slug> | task
status: active | candidate | archived | rejected
confidence: high | medium | low
source: user-stated | user-confirmed | repeated-behavior | assistant-inference
created: YYYY-MM-DD
last_confirmed: YYYY-MM-DD
review_after: YYYY-MM-DD
expires: YYYY-MM-DD
priority: low | normal | high
```

Use only fields that are meaningful. `expires` is appropriate for temporary project rules; `review_after` is appropriate for preferences and plans that may change.

## Trigger fields

```yaml
type: trigger
scope: global | project:<slug>
status: active | candidate | archived | rejected
event: project_start | task_start | user_correction | repeated_request | project_end | review_due
enabled: true
condition: "A plain-language condition the agent can evaluate"
actions:
  - read: "10-User/preferences.md"
  - read: "20-Projects/<project>/context.md"
  - propose: "Create a candidate when the condition repeats"
ask_confirmation: true
cooldown_days: 7
max_frequency: once_per_task
source: user-confirmed
```

Actions use one of these verbs: `read`, `summarize`, `propose`, `write`, `review`, `archive`, or `remind`. Paths are relative to the vault root.

## Candidate format

Candidates belong in `00-Inbox/` and must not be treated as active memory:

```yaml
type: trigger
scope: global
status: candidate
confidence: medium
source: repeated-behavior
observed_on:
  - YYYY-MM-DD
proposed_event: task_start
proposed_condition: "The user starts a task of this kind"
proposed_actions:
  - "Read the relevant preference note"
decision_needed: "Confirm, edit, or reject this candidate"
```

The body should include:

1. Observation: what the user explicitly requested or corrected.
2. Proposed rule: what should happen in future.
3. Scope: global or project-specific, with a reason.
4. Evidence: links or dates for the observations.
5. Confirmation: what the user needs to approve or change.

## Conflict resolution

Resolve by current explicit instruction, then narrower scope, then higher `priority`, then newer `last_confirmed`. If the conflict remains, ask the user. Do not resolve a conflict by silently deleting either note.

