# Obsidian + Personal Memory

这是一套“Obsidian 记忆库 + Codex Skill”模板。

## 1. 初始化 Obsidian

1. 在 Obsidian 中创建或选择一个 Vault。
2. 将本目录的 `vault/` 文件夹内容复制到该 Vault 根目录。
3. 打开 `00-System/config.md`，确认目录和配置符合你的习惯。
4. 在 `10-User/` 中补充你已经确定的长期偏好、工作方式、决策原则和长期规划。

## 2. 安装 Skill

将 `skill/personal-memory/` 复制到 Codex 的 Skill 目录，并保持目录名为 `personal-memory`。常见位置是：

```text
~/.codex/skills/personal-memory/
```

如果使用了自定义 `CODEX_HOME`，则复制到：

```text
$CODEX_HOME/skills/personal-memory/
```

本交付物没有自动修改全局 Skill 目录。

## 3. 让 Skill 找到 Vault

优先设置环境变量：

```text
PERSONAL_MEMORY_VAULT=/absolute/path/to/your/obsidian-vault
```

如果当前 Codex 会话无法设置环境变量，也可以在对话中提供 Vault 的绝对路径，或在项目根目录建立：

```text
.personal-memory/vault-path
```

文件内容只放 Vault 的绝对路径。

## 4. 推荐的首次使用方式

可以直接对 Codex 说：

```text
使用 $personal-memory，读取我的全局偏好和当前项目记忆，然后开始处理这个任务。
```

任务结束时可以说：

```text
使用 $personal-memory，复盘本次任务，提出应该保存的项目决策、长期偏好和新增触发规则；未经我确认不要固化长期记忆。
```

当你明确希望保存时，可以说：

```text
记住：以后处理这类项目时，先检查现有约束，再提出实施方案。保存为全局工作偏好。
```

## 5. 触发机制的边界

触发规则保存在 `30-Triggers/`，Skill 会在被调用、项目开始、任务结束或复盘时评估它们。仅把规则写入 Obsidian 不会让文件系统主动唤醒 Codex；真正的定时唤醒仍需要日历、系统任务或其他自动化工具来调用 Codex。

## 6. 验证模板

可运行：

```bash
python3 skill/personal-memory/scripts/validate_vault.py vault
```

它只检查模板目录和基本 frontmatter，不会修改任何文件。
