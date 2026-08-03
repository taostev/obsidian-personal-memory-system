# Obsidian Personal Memory System

一个由 Obsidian 知识库和 Codex Skill 组成的个人长期记忆系统。

它将：

- 全局用户偏好、工作方式、决策原则和长期规划保存为可编辑的 Markdown。
- 项目背景、项目决策和项目专属偏好按项目隔离。
- 触发规则保存于 `vault/30-Triggers/`，支持项目开始、项目结束、复盘和候选规则学习。
- AI 推断出的新记忆先进入 `vault/00-Inbox/`，经用户确认后再固化。

## 目录

- `vault/`：Obsidian Vault 模板。
- `skill/personal-memory/`：Codex Skill，负责读取、应用、学习和更新记忆。
- `START-HERE.md`：安装与使用说明。

## 核心原则

1. 当前用户指令优先于历史记忆。
2. 项目规则优先于全局偏好，但不能反向污染全局偏好。
3. 一次性行为不会自动成为长期记忆。
4. 未确认的推断进入 Inbox，不直接修改正式记忆。

## 快速开始

请先阅读 [`START-HERE.md`](START-HERE.md)，然后将 `vault/` 内容复制到你的 Obsidian Vault，并将 `skill/personal-memory/` 安装到 Codex Skill 目录。

## 触发机制说明

触发规则会保存于 Obsidian 并由 Skill 在任务启动、任务结束或复盘时评估。真正的系统级定时唤醒仍需要日历、系统任务或其他自动化工具调用 Codex。

