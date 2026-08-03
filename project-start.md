---
type: trigger
scope: global
status: active
event: project_start
enabled: true
condition: "识别到新的项目、仓库或工作目录"
actions:
  - read: "00-System/config.md"
  - read: "00-System/Memory Operating Rules.md"
  - read: "10-User/preferences.md"
  - read: "10-User/work-style.md"
  - read: "10-User/decision-principles.md"
  - read: "20-Projects/<project>/context.md"
  - summarize: "只报告影响当前任务的规则"
ask_confirmation: false
max_frequency: once_per_task
source: user-confirmed
---

# Project start

在新项目开始时加载全局偏好和当前项目背景。若当前项目尚未建立目录，先识别项目名称，再建议从 `20-Projects/_project-template/` 复制模板。
