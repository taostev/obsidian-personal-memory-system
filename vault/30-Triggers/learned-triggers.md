---
type: trigger-index
scope: global
status: active
---

# Learned triggers

这里登记已经由用户确认的新增触发机制。候选规则先放在 `00-Inbox/`，确认后再移动到本目录或拆成独立规则文件。

## Promotion rule

- 同类行为至少出现两次，或用户明确说“以后遇到这种情况自动做”。
- 记录证据日期和适用范围。
- 默认先询问是否升级为 `status: active`。
- 如果规则只适用于一个项目，保持 `scope: project:<project-slug>`。

