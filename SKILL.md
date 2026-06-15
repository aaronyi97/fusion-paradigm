---
name: fusion
description: Multi-model "fusion paradigm" — instead of letting your main model decide alone, you bring in models from different families (GPT, Claude, others) to give independent views first, then synthesize consensus, disagreement, and remaining risk, and a human makes the final call. For plan design, architecture judgment, audits, retrospectives, and high-stakes decisions; not for coding/execution, simple facts, or routine edits. Triggers when the user says "use fusion / use the fusion paradigm / cross-family review / get a second opinion from another model / have another model look at this independently" or in Chinese "用 fusion 范式 / 叫不同模型看一下 / 跨家族交叉验证 / 多模型会诊 / 让另一个模型也独立看看".
disable-model-invocation: true
allowed-tools: Agent
version: 0.1.0
author: AaronYi
---

# Fusion Paradigm

Take a judgment or design problem and hand it to models from *different families* to look at independently first, then synthesize. The core isn't "call a few more models" — it's **stopping it from degrading into calling one more model just to nod along**.

> 中文触发说明：把一个判断 / 设计问题，先交给"不同家族"的模型各自独立看，再综合。核心不是"多调几个模型"，是防止它变成多叫一个模型来点赞。说"用 fusion 范式 / 叫不同模型看一下 / 跨家族交叉验证 / 多模型会诊"即可触发。

## When to use / when not to

- **Use it**: plan design, architecture judgment, finalizing an important piece of writing, audits, retrospectives, high-stakes decisions — anywhere you need multiple angles and the cost of being wrong is high.
- **Don't use it**: writing code / running execution, looking up a simple fact, short translation, routine small edits — one model doing it end to end is the most reliable here; multiple models just clash, slow you down, and cost more.

> **Foundational rule**: if there's no "round-one independent judgment," don't call it fusion. Just handing your plan to another model for review makes it a reviewer, not fusion — withholding your main plan in round one is the bedrock of the whole paradigm.

## First time: configure once (wizard)

On the first trigger, ask the user two things and pick a setup path from the answers —

1. **What tools do you mainly use?** (Claude Code / Cursor / Windsurf / web ChatGPT + Claude only / API key only)
2. **Which different model families can you call?** (at least two from different companies, e.g. Claude + GPT, DeepSeek + Kimi)

Load the matching setup based on the answer (load only the one row that matches, don't read them all):

| User's situation | Load | Automation level |
|---|---|---|
| Web AI only | `references/04-webui-manual-sop.md` | Zero setup · pure manual copy-paste |
| Has an API key | `references/03-api-script.md` + `scripts/fusion_api.py` | Script skeleton · you fill in the SDK calls |
| Claude Code + Codex | `references/02-claude-code-codex.md` | Author's own setup · semi-automated |
| Cursor / Windsurf, single tool | the "single-tool" section of `references/02-claude-code-codex.md` | Manual multi-round + synthesis template |

## After setup: how to use it

When the user says "use fusion to look at [some plan / decision]," run the 7-step flow in `references/01-protocol.md`:

1. Judge whether this is worth a fusion (if not, say "one model is enough")
2. Build a context pack — give only the problem / constraints / evidence, **don't slip in the main thread's conclusion** (anti-anchoring)
3. Round one: have models from different families produce independent verdicts / objections (without seeing your plan)
4. Round two: now give them your plan and have them hunt for holes
5. The main thread processes disagreements point by point and produces a disagreement table (no smoothing it over with "on balance…")
6. Hand the real trade-offs to a human
7. Note one line: what did this fusion change about your judgment

## Where the soul lives

The full 7-step flow, both-round prompt templates, role assignments, and the toy self-check all live in **`references/01-protocol.md`** — that's the cross-tool core, and the flow doesn't change no matter what tooling you use. Read it first, then read the setup file for your row.

## ⚠️ One-line safety

Fusion sends your problem / plan to **multiple external models** — anything confidential, customer data, or non-public info should be redacted first or left out. See the "Safety" section of the README.
