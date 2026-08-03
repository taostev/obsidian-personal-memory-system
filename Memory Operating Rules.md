---
type: system-rules
status: active
priority: high
---

# Memory operating rules

1. Treat the current user message as the highest-priority instruction.
2. Keep global preferences, project rules, temporary task instructions, and inferred candidates separate.
3. Never promote a one-off project constraint into a global preference.
4. Store explicit user requests directly in the narrowest valid scope when the user asks to remember or update them.
5. Store inferred or repeated behavior as `status: candidate` until confirmed, unless an active trigger explicitly authorizes automatic promotion.
6. When two active notes conflict, prefer current instruction, narrower scope, higher priority, and newer confirmation date in that order.
7. If a memory is expired, archived, or rejected, do not apply it.
8. At the end of substantial work, propose project decisions and stable preferences that are worth saving.
9. Keep notes concise, actionable, and understandable without the AI.
10. Report the exact note path after a successful write.
