# L2 落地 · Claude Code + Codex（作者同款 · 半自动）

适合：用 Claude Code 当主对话，且装了官方 codex 插件（跨族 GPT）。自动化程度最高、最接近"真 fusion"的一档。

## 一次性配置（≤3 步）

1. 确认装了 codex 插件：能调 `Agent` 工具、`subagent_type: "codex:codex-rescue"` 即可。（注：codex:codex-rescue 是作者环境里的 subagent 名，你的环境可能不同，按你装的 codex 插件实际名称调整。）
2. （可选）配一个同族 opus 子 agent 做第二视角：`.claude/agents/` 放一个 frontmatter 写 `model: opus` 的 agent。
3. 确认环境变量 `CLAUDE_CODE_SUBAGENT_MODEL` **没被设成字符串**（尤其别设 `inherit`，会碾压子 agent 的 model 分级）。`unset` 它最稳。

## 调用机制

- **调跨族 Codex（GPT）**：`Agent` 工具，`subagent_type: "codex:codex-rescue"`，**显式只读**（见下硬约束）。
- **调同族 opus 子 agent**：`Agent` 工具，`subagent_type` 填你的 agent 名，或传 `model: opus`。

## ⚠️ 只读硬约束（必须）

codex-rescue 默认可能带 `--write`（能改你的文件）。fusion 是"出视角"不是"动手"——派 codex 时**必须在 prompt 里显式写 read-only、禁 `--write`**，并要求回包打印实际 sandbox 模式，确认 read-only 才采信。

## 跑 fusion（按 01-protocol 的 7 步）

1. 触发判断（值不值得）
2. 构造上下文包（**不塞主对话方案**）
3. 第一轮：并行派 codex（跨族）+ opus 子 agent（同族），各用 01-protocol 的"第一轮 prompt"，**互相不可见**
4. 第二轮：把主对话方案给 codex，用"第二轮 prompt"对抗审查
5. 主对话综合 → 分歧表
6. 人拍板
7. 留痕

## 防递归 / 防失控（作者实战经验，建议照搬）

- codex 回包**不自动触发下一个 codex**（防"审查触发审查"的无限环）。
- 单次会话累计自动派 codex 设上限，到顶停下问人。
- 跨族模型互相喂结果有 cache 近邻污染风险，注意各轮隔离。

## 单工具变体（Cursor / Windsurf / Trae）

这些工具支持多模型切换，但不开放"自动调另一个模型"的 API 给 skill，所以这一档是**手动多轮**：

1. 用模型 X 跑"第一轮 prompt"，存下输出。
2. 切到模型 Y（**不同家**），再跑一遍第一轮，存下。
3. 把两份 + 你的方案，喂给当前模型跑"综合"（01-protocol 第 5 步的分歧表模板）。

skill 在这里的作用：提供两轮 prompt + 分歧表模板，你手动串起来。本质和 L2 一样，只是切模型这一步靠手动。
