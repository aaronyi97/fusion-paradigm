# Fusion 范式 — 多模型协作 Skill

让你的主力 AI 在**判断 / 方案设计**时，先调一个**不同家族**的模型出独立视角，再综合，最后你拍板。核心不是"多调几个模型"，是 **防止它变成多叫一个模型来点赞**。

> ## ⚠️ 边界声明（请先读）
> 这是我自己在用的一套多模型协作**方法** + 当时的脚手架，原样公开做**实验记录**。
> - **不是开箱即用的软件**，没经过大规模测试。
> - **不保证在你的环境能跑**；`scripts/fusion_api.py` 是参考骨架，要你自己按 SDK 补全。
> - 我**不承诺响应 issue / PR**，也不提供个人环境排错——觉得有用就 fork 改成你自己的。
> - 核心价值是**方法和提示词模板**，不是代码。

## 来源
2026 年 6 月 OpenRouter 发布 Fusion（多模型合成）。这个 skill 把同一个范式做成**不接 OpenRouter API 也能用**的本地版——两个不同家族的模型就能跑。（本项目是对这一范式的独立实现，**与 OpenRouter 无关联、非官方**。）

## 什么时候用 / 什么时候别用
- **用**：方案设计、架构判断、重要文章定稿、审计、复盘、重大决策
- **别用**：写代码 / 跑执行、查简单事实、短翻译、日常小改（这些一个模型最稳，多模型反而打架、慢、贵）

## 地基铁律
**没有"第一轮独立判断"，就不叫 fusion。** 只把你的方案丢给另一个模型审，那是 reviewer（它会顺着你补几句风险，盲区和你重合）。第一轮不给主方案，是整个范式的地基。

## 防玩具自检（先看这个，知道怎么算用错了）
| 信号 | 玩具？ |
|---|---|
| 被调模型只补了几句"注意风险" | ⚠️ 被你锚定了 |
| 几个模型都说"可行" | ⚠️ 共识 ≠ 真相 |
| 输出变长了但判断没变 | ⚠️ 赞同按钮 |
| 抓出你没看到的盲区 / 改变了判断 | ✅ 真起作用 |

## 四档配置（按你的工具选一档）
| 档 | 给谁 | 看哪个文件 |
|---|---|---|
| **L0** | 只有网页版 AI（ChatGPT + Claude） | `references/04-webui-manual-sop.md`（纯手动复制粘贴，零门槛） |
| **L1** | 有 API key | `references/03-api-script.md` + `scripts/fusion_api.py` |
| **L2** | Claude Code + Codex | `references/02-claude-code-codex.md` |
| **L3** | Cursor / Windsurf 等单工具 | `references/02-claude-code-codex.md` 的"单工具"段 |

核心流程（所有档通用）：`references/01-protocol.md`

## 怎么用
配好后，对你的 AI 说："**用 fusion 范式帮我看一下 [某方案 / 决策]**"。

## 安装（Claude Code）
把 `fusion/` 拷到 `~/.claude/skills/`。其他支持 Agent Skills 的工具见 [agentskills.io](https://agentskills.io)。

## ⚠️ 安全
`scripts/fusion_api.py` 要你填 API key——**别把 key 写进文件提交上去**，用环境变量。

## License
MIT
