# L1 落地 · 只有 API key（最省事的自动化）

适合：你有两个不同家族模型的 API key（如 Anthropic 的 Claude + OpenAI 的 GPT，或 DeepSeek + Kimi）。**通用化程度最高**——不依赖任何 IDE，谁都能调 API。

## 一次性配置

1. 准备两个**不同公司**的 API key。
2. 填进 `scripts/fusion_api.py` 顶部 CONFIG 区的 model 名，或设好对应环境变量（key）。
3. 跑一次 `python scripts/fusion_api.py --check` 验证 key 在不在。

## 怎么用

```
python scripts/fusion_api.py --question "你的问题或方案"
```

脚本按 01-protocol 跑：把问题（不含你的倾向）依次发给两个不同家模型 → 各自第一轮独立输出 → 综合成分歧表 → 把拍板留给你。

## 注意

- 脚本是**参考骨架**，`call()` 函数留了 TODO——按你用的 SDK（anthropic / openai / 其他）补全那几行调用即可，逻辑骨架已经搭好。
- 脚本默认**不替你拍板**，只输出分歧表 + 待决点。
- 想要严格两轮（第一轮独立 + 第二轮拿你的方案对抗），把你的方案单独走 `ROUND2`，脚本里已留位置。
- 这一档最适合做成你自己的小工具，嵌进任何工作流。
