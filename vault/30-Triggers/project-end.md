---
type: trigger
scope: global
status: active
event: project_end
enabled: true
condition: "任务达到一个可交付节点或用户明确要求复盘"
actions:
  - review: "检查项目决策、稳定偏好、新触发候选和开放问题"
  - propose: "把未确认的长期记忆写入 00-Inbox/"
  - write: "把已确认的项目决策写入当前项目 decisions.md"
ask_confirmation: true
max_frequency: once_per_task
source: user-confirmed
---

# Project end

结束时不要保存完整对话，只保存可复用的决策、约束、偏好和待办。

