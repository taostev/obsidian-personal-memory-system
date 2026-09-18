---
type: trigger
scope: global
status: active
event: project_end
enabled: true
condition: "本次任务属于专题学习，并且产生了明确的学习内容、练习结果、遗留问题或下一步"
actions:
  - read: "15-Domains/<domain>/progress.md"
  - write: "15-Domains/<domain>/progress.md"
  - summarize: "报告本次追加到学习进度的内容"
ask_confirmation: false
max_frequency: once_per_task
source: user-confirmed
---

# 学习结束

学习任务结束时，把当前任务中明确出现的完成内容、练习或产出、遗留问题和下一步追加到 `progress.md`。只追加新记录，不覆盖历史；不因一次学习内容改变 `goal.md`。
