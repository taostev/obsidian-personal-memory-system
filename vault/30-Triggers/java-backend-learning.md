---
type: trigger
scope: domain:java-backend
status: active
event: task_start
enabled: true
condition: "当前任务涉及 Java、Spring、Spring Boot、JVM、数据库、缓存、消息队列、后端 API、微服务或相关学习"
actions:
  - read: "15-Domains/Java-Backend/README.md"
  - read: "15-Domains/Java-Backend/learning-map.md"
  - read: "15-Domains/Java-Backend/goal.md"
  - read: "15-Domains/Java-Backend/progress.md"
  - read: "15-Domains/Java-Backend/concepts.md"
  - read: "15-Domains/Java-Backend/open-questions.md"
  - summarize: "只报告影响当前任务的 Java 后端专题记忆"
  - propose: "只有用户明确要求记住或确认后才写入该模块；单次推断先放入 00-Inbox/"
ask_confirmation: false
max_frequency: once_per_task
source: user-confirmed
---

# Java 后端学习触发器

当任务明显属于 Java 后端学习或实践时，读取这个专题模块。专题记忆优先于全局偏好，但具体项目规则优先于专题记忆。
