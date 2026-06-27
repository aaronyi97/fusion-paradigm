# Fusion: Blind Second-Model Review for Hard AI Workflow Decisions

Don't let one AI grade its own homework.

Fusion is a simple protocol for hard AI work:
before showing a model your plan, give a different model family only the raw problem, goal, constraints, and evidence.

Ask it for an independent verdict first.
Then show your plan.
Then synthesize the disagreement yourself.

## Use Fusion when:
- architecture decisions
- spec planning
- verification design
- audits / retrospectives
- important writing

## Avoid Fusion when:
- small edits
- ordinary implementation
- latency-sensitive work
- simple facts or low-stakes drafting

## Try it in 30 seconds

Open two AIs from different companies (for example, ChatGPT + Claude).
Paste this block into each one before showing your current plan:

**English — Round 1 prompt:**

```
You're an independent model brought in for a genuine second opinion. You can't see my plan — and don't try to guess what I'm leaning toward. Working only from the problem, goal, constraints, and evidence below, give your own judgment from first principles:
1. Your own answer / verdict
2. The blind spot most likely to be missed
3. Which assumptions, if wrong, would overturn the conclusion
4. The smallest action that would verify it
No "broadly workable, but watch out for…" filler. If the evidence isn't enough, just say "don't know / needs verification."

[Problem] …
[Goal] …
[Constraints] …
[Known facts] …
```

**中文 · 第一轮 prompt：**

```
你是被调用的独立模型，看不到我的方案，也别猜我会怎么想。
只基于下面的问题/目标/约束/证据，从第一性原理给出独立判断：
1) 你自己的方案 2) 最可能被忽略的盲区 3) 哪些前提错了会推翻结论 4) 最小验证动作。
禁止"总体可行但需注意"空话；证据不足就直接写"不知道/需要验证"。
【问题】…【目标】…【约束】…【已知事实】…
```

If this protocol helps or breaks, tell me what happened.
If you want me to diagnose your AI workflow asynchronously, I'm opening 5 free workflow snapshots.

## Limitations

This is a multi-model collaboration **method** I actually use, plus the scaffolding I built around it, published as-is as an **experiment log**.
- **Not turnkey software.** It hasn't been broadly tested.
- **No promise it runs in your environment.** `scripts/fusion_api.py` is a reference skeleton — you wire up your own SDK calls.
- **I won't promise to answer issues or PRs**, and I don't debug personal setups. If it's useful, fork it and make it yours.
- The value is in the **method and the prompts**, not the code.

## The Problem

A single AI reviewing its own plan is **grading its own homework**. It already believes the answer, so it defends it.

The obvious "fix" is fake fusion: you hand your plan to a second model and ask it to "check for issues." But that model just reads your plan and pads it with a few risks — its blind spots overlap with yours, because you anchored it to your conclusion. You added a step and learned nothing.

Real fusion never shows the plan first. A different family of model, working blind from the raw problem, fails in *different* places than you do — and that non-overlap is the whole point.

## Before / After

```text
Before (fake fusion)

You → Model B: "Here's my plan to migrate to microservices. Any issues?"

Model B: "Solid plan! A few things to watch:
- Network latency between services
- Distributed tracing complexity
- Make sure you version your APIs
Overall this looks workable."

(It read your plan and agreed with reasons. Same blind spots, longer answer.)
```

```text
After (real fusion)

You → Model B (blind, no plan shown): "Problem: our monolith is hard to
ship. Goal: faster, safer releases. Constraints: 4 engineers, no platform
team. What's your independent call?"

Model B: "With 4 engineers and no platform team, microservices is the most
likely wrong move here — you'd add operational surface you can't staff.
The blind spot: 'hard to ship' is usually a CI/test problem, not an
architecture problem. Smallest check: measure where your deploy time
actually goes before splitting anything."

(It never saw your plan. It found the assumption you couldn't see.)
```

## Install

The value of fusion is the **content of the prompts and protocol** — the actual text. Copy the **full files**; sending an AI a link to this repo won't work, because it can't open the link and read the content. (中文：fusion 的价值是 prompt 和协议**正文本身**。请复制**完整文件**——只把 GitHub 链接发给 AI，它打不开链接、看不到里面的内容。)

### Claude Code

1. Download the `fusion/` folder from this repo
2. Drop it into `~/.claude/skills/`
3. Start a new Claude Code session. Done.

### Cursor

1. Download the `fusion/` folder from this repo
2. Drop it into your skills directory and read `references/01-protocol.md`
3. Tell Cursor to run the fusion protocol, using `references/02-claude-code-codex.md`'s "single-tool" section. Done.

### Codex

1. Download the `fusion/` folder from this repo
2. Keep it where Codex can read it, and open `references/02-claude-code-codex.md`
3. Codex plays the cross-family reviewer. Done.

### VS Code / GitHub Copilot

1. Download the `fusion/` folder, especially `references/01-protocol.md`
2. Open it alongside your chat so Copilot has the protocol in context
3. Run the two rounds manually with a second-family model. Done.

### Windsurf

1. Download the `fusion/` folder from this repo
2. Read `references/01-protocol.md`, then `references/02-claude-code-codex.md`'s "single-tool" section
3. Start a new Windsurf session and run the protocol. Done.

### OpenClaw

1. Download `fusion/SKILL.md` and the `references/` folder
2. Place them under `skills/fusion/` in your workspace
3. Restart OpenClaw. Done.

### Only have an API key

1. Download `scripts/fusion_api.py` and `references/03-api-script.md`
2. Wire up your own SDK calls (the script is a skeleton, not a finished tool)
3. Run it against two different-family models. Done.

### Only have web chat (ChatGPT + Claude, etc.)

1. Open `references/04-webui-manual-sop.md`
2. Follow the pure copy-paste steps — zero setup
3. Run the two rounds by hand across two different vendors. Done.

## When To Use / When Not To Use

✅ Plan design, architecture judgment, finalizing an important piece of writing, audits, retrospectives, high-stakes decisions

✅ When being wrong is expensive and a second, *genuinely independent* angle is worth the time

❌ Writing or running code, looking up a simple fact, short translations, small day-to-day edits

❌ Anything where one model is the most stable choice — multiple models just fight, slow you down, and cost more

## How It Works

Fusion is one idea: most "second opinions" aren't independent. If a model can see your plan, it anchors to it. So the protocol forces a blind first round, *then* an adversarial second round, *then* you decide. Seven steps (full version in `references/01-protocol.md`):

1. **Trigger check** — is this even worth fusion? If not, say "one model is enough."
2. **Build the context pack** — give only the problem, goal, constraints, and evidence. **Never** your plan or your leaning (this is the anti-anchoring step).
3. **Round 1 · independent** — a different-family model produces its own answer / objection, blind to your plan.
4. **Round 2 · adversarial** — *now* show your plan and ask it to find holes, not to polish.
5. **Synthesize** — work through every disagreement into a diff table; no "broadly workable" hand-waving, and minority views don't get silently dropped.
6. **Human decides** — the real trade-offs go to a person, not to the model pretending to arbitrate.
7. **Traceability note** — write one line: what did this fusion actually change?

> **The foundation rule: no independent first round, no fusion.** Just handing your plan to another model to review is a *reviewer* — it'll pad your plan with a few risks, and its blind spots overlap with yours. Withholding the plan in round 1 is the bedrock the whole method stands on.

**Anti-toy self-check** (run it every time — this is how you know you used it wrong):

| Signal | Explanation | Toy? |
|---|---|---|
| The called model only added a few "watch out for…" lines | It got anchored by you | ⚠️ yes |
| Several models all say "workable" | They can be wrong together — especially same-family | ⚠️ consensus ≠ truth |
| The output got longer but the judgment didn't change | A ceremonial approval button | ⚠️ yes |
| It caught a blind spot you missed / changed your judgment | It actually worked | ✅ no |

## Source

In June 2026, OpenRouter shipped Fusion (multi-model synthesis). This skill turns the same paradigm into a **local version that works without the OpenRouter API** — two models from different families are enough. (This project is an independent implementation of that paradigm, **unaffiliated with and not endorsed by OpenRouter**.)

## 30-Second Try

You don't need to install anything. The copy-paste Round 1 prompt (English + 中文) is at the top of this README under [**Try it in 30 seconds**](#try-it-in-30-seconds): open two AIs from **different companies** (e.g. ChatGPT + Claude), fill in your problem, and send the block to each — **without telling them your leaning**. Let both answer independently, then synthesize. That's the smallest possible fusion. Full 7 steps in `references/01-protocol.md`.

## Safety

- **API key**: `scripts/fusion_api.py` asks for your key — **don't commit the key into the file.** Use an environment variable.
- **Content leaves your machine**: fusion sends your problem and your plan to **multiple models from different companies** / web AIs. Confidential info, customer data, unpublished material — redact it first, or just don't use fusion for it. You're handing the same material to several vendors at once, and each has its own logging and training policy, so check before you send.

## 中文说明

一句话定位：fusion 是一套多模型协作方法——重要判断时，让你的主力 AI 先调一个**不同家族**的模型独立出视角，再综合，最后**你**拍板。核心不是"多调几个模型"，是**防止第二个模型只是给第一个点赞**。

为什么这么做：单个 AI 审自己的方案 = 自己给自己作业打分，它早信了那个答案，只会替它辩护。把方案丢给另一个模型"看看有没有问题"也是假 fusion——它顺着你补几句风险，盲区跟你重合。真 fusion 第一轮不给方案：一个不同家族的模型从干净的问题出发，会在**和你不一样**的地方犯错，这个"不重合"才是它值钱的地方。

安装（复制**完整文件**，别只发链接给 AI——它打不开）：

- Claude Code：下载 `fusion/` 文件夹，放到 `~/.claude/skills/`，重新开会话
- Cursor / Windsurf / Codex：下载 `fusion/`，先读 `references/01-protocol.md`，再看 `references/02-claude-code-codex.md` 的"单工具"段，让它跑两轮流程
- VS Code / Copilot：把 `references/01-protocol.md` 开在旁边给它当上下文，手动跑两轮
- OpenClaw：把 `SKILL.md` + `references/` 放到工作区 `skills/fusion/` 下并重启
- 只有 API key：下载 `scripts/fusion_api.py` + `references/03-api-script.md`，自己补 SDK 调用
- 只有网页版 AI：看 `references/04-webui-manual-sop.md`，纯手动复制粘贴，零门槛

什么时候用：方案设计、架构判断、重要文章定稿、审计、复盘、重大决策——错了代价大、值得多看一个独立视角的场合。什么时候别用：写代码 / 跑执行、查简单事实、短翻译、日常小改——这些一个模型最稳，多模型反而打架、慢、贵。

地基铁律：没有"第一轮独立判断"，就不叫 fusion。完整 7 步流程、两轮 prompt 模板、防玩具自检都在 `references/01-protocol.md`。

---

Built by AaronYi

---

## Stay in touch

- **X / Twitter:** [@AaronYiaazw](https://x.com/AaronYiaazw)
- **Substack:** [@aaronyi97](https://substack.com/@aaronyi97)
- **Free Async AI Workflow Snapshot:** Send me one workflow, one failed AI task, or one place where your AI process keeps breaking. I'll tell you where I think it breaks. No live call required.

This snapshot is an AI workflow diagnostic. It is not a certified code audit, security audit, or architecture certification.

## License

MIT
