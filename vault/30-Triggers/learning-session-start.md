---
type: trigger
scope: global
status: active
event: task_start
enabled: true
condition: "当前任务是在 15-Domains/<domain>/ 下学习某个专题内容"
actions:
  - read: "15-Domains/<domain>/README.md"
  - read: "15-Domains/<domain>/goal.md"
  - read: "15-Domains/<domain>/progress.md"
  - summarize: "先报告该专题总体目标、当前进度和本次学习与目标的关系"
  - propose: "如果专题缺少 goal.md 或 progress.md，先建立这两个文件再继续学习"
ask_confirmation: false
max_frequency: once_per_task
source: user-confirmed
---

# 学习开始

识别到专题学习任务时，先读取总体目标和学习进度。目标与进度是两个独立文件，不合并。
