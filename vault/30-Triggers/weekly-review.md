---
type: trigger
scope: global
status: active
event: review_due
enabled: true
condition: "用户主动要求周复盘，或 review_after 已到期"
actions:
  - read: "00-Inbox/"
  - review: "检查候选记忆、到期偏好、近期项目决策和长期计划"
  - propose: "提出确认、修改、归档或删除建议"
ask_confirmation: true
cooldown_days: 7
max_frequency: once_per_week
source: user-confirmed
---

# Weekly review

周复盘只整理变化，不重复输出整个知识库。
