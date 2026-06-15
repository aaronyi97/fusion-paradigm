# L1 落地 · 只有 API key（自动化骨架 · 需自己补 SDK 调用）

适合：你有两个不同家族模型的 API key（如 Anthropic 的 Claude + OpenAI 的 GPT，或 DeepSeek + Kimi）。**通用化程度最高**——不依赖任何 IDE，谁都能调 API。

## 一次性配置

1. 准备两个**不同公司**的 API key。
2. 填进 `scripts/fusion_api.py` 顶部 CONFIG 区的 model 名，或设好对应环境变量（key）。
3. 跑一次 `python scripts/fusion_api.py --check` 验证 key 在不在。

## 怎么用

```
python scripts/fusion_api.py --question "你的问题或方案"
```

脚本按 01-protocol 跑：把问题（不含你的倾向）依次发给两个不同家模型 → 各自第一轮独立输出 → 综合成分歧表 → 把拍板留给你。**注意 `call()` 是空的（见下），补全 SDK 调用前脚本不能真跑。**

## 注意

- 脚本是**参考骨架**，`call()` 函数是空的（直接 `NotImplementedError`）——按你用的 SDK（anthropic / openai / 其他）补全那几行调用，逻辑骨架已经搭好。**补全前 `--question` 跑不通，这是预期、不是 bug。**
- 脚本默认**不替你拍板**，只输出分歧表 + 待决点。
- 严格两轮已实现：传 `--plan` 后，第二轮会**带上第一轮输出 + 原问题**一起喂给模型（不再是无状态假回顾），第一轮独立判断不被覆盖、综合时一并参与。
- 这一档最适合做成你自己的小工具，嵌进任何工作流。
