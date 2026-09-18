---
type: trigger
scope: global
status: active
event: task_start
enabled: true
condition: "用户要求新建、发布或委派一个 Codex 对话或任务"
actions:
  - remind: "调用 create_thread 时默认使用已保存项目的本地目录，即 environment.type=local；不要自动选择 Git worktree"
  - remind: "只有用户在当前请求中明确要求独立 Git 工作树时，才使用 environment.type=worktree"
  - remind: "该规则只决定新任务的运行环境，不禁止项目本身使用 Git"
ask_confirmation: false
max_frequency: once_per_task
source: user-stated
created: 2026-08-31
last_confirmed: 2026-08-31
review_after: 2026-11-29
priority: high
---

# 新建 Codex 任务时本地目录优先

以后用户要求新建对话、发布任务或委派到另一个 Codex 任务时，默认直接使用已保存项目目录运行，不自动创建 Git 工作树。

只有用户在当次请求中明确提出“使用工作树”“隔离分支”或等价要求时，才选择 Git worktree。若必须使用工作树，应先只读确认仓库至少已有一个提交及有效起始分支；条件不满足时，继续使用本地目录并说明原因。

## Evidence

- 2026-08-31：在无初始提交的仓库中连续出现 `fatal: invalid reference: main`，用户明确要求以后创建聊天时先不用 Git。
