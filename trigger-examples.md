# Trigger examples

These examples illustrate the format; copy only the rules that match the user's actual habits.

## Load memory at project start

```yaml
---
type: trigger
scope: global
status: active
event: project_start
enabled: true
condition: "A new project or repository is identified"
actions:
  - read: "10-User/preferences.md"
  - read: "10-User/decision-principles.md"
  - read: "20-Projects/<project>/context.md"
  - summarize: "State only the rules that affect this task"
ask_confirmation: false
max_frequency: once_per_task
source: user-confirmed
---
```

## Capture repeated corrections

```yaml
---
type: trigger
scope: global
status: active
event: user_correction
enabled: true
condition: "The user corrects the same output behavior for the second time"
actions:
  - propose: "Create a candidate preference in 00-Inbox/"
  - remind: "Ask whether to promote it to 10-User/"
ask_confirmation: true
cooldown_days: 14
max_frequency: once_per_pattern
source: user-confirmed
---
```

## Review plans monthly

```yaml
---
type: trigger
scope: global
status: active
event: review_due
enabled: true
condition: "A note in 10-User/long-term-plans.md has review_after <= today"
actions:
  - review: "Check progress, change, archive, or extend the plan"
ask_confirmation: true
max_frequency: once_per_month
source: user-confirmed
---
```
