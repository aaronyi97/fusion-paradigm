# L0 setup · Web-UI AI only (zero barrier · anyone can do it)

Best for: you only have the web versions of ChatGPT, Claude, DeepSeek, etc. — no API, no coding tools. **This tier needs no technical skill at all and is fully manual, yet it's still real fusion.** The prompts are inlined below, so you never have to jump between files.

## Step 1 · Decide whether it's worth it
Only use it for plan design / important decisions / retrospectives. Don't bother for checking a fact or writing something small.

> ⚠️ **Desensitize first**: this tier sends your problem and plan to two external web AIs. Strip out — or just don't include — anything confidential / customer data / non-public information. You're handing the material to multiple vendors at once.

## Step 2 · Round one (two different-family AIs each answer independently)
Open two AIs from **different companies** (say, one ChatGPT and one Claude). **Don't tell them your own thinking yet**; send each of them the block below (fill in your problem).

**English:**

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

**中文：**

```
你是被调用的独立模型。你现在看不到我的方案，也别猜我会怎么想。
只基于下面的问题、目标、约束和证据，从第一性原理给出独立判断：
1) 你自己的方案 2) 最可能被忽略的盲区 3) 哪些前提错了会推翻结论 4) 最小验证动作。
禁止"总体可行但需注意"这种空话；证据不足就直接写"不知道 / 需要验证"。

【问题】（填）
【目标】（填）
【约束】（填）
【已知事实】（填）
```

Save each of their answers.

## Step 3 · Round two (have them pick holes in your plan)
Now take your own plan, add the block below, and send it to each of them.

**English:**

```
Below is my plan. Your job is not to polish it, and not to look for reasons to back it.
First, recap your round-one judgment in three sentences (if you now think round one was wrong, just say "overturning it" — don't rationalize). Then, point by point:
- What do you agree with, and why?
- What do you disagree with — and if I'm wrong, what's the fallout?
- Which key assumptions did I miss?
- Which calls should a human make, instead of a model auto-synthesizing them?
- What's the smallest verifying action?
You must include at least one "I'd block this / demand more evidence / change direction" call.

[My plan] …
```

**中文：**

```
下面是我的方案。你的任务不是润色，也不是找理由支持它。
先用 3 句话回顾你第一轮的判断，再逐条对照：
- 你同意什么？为什么？
- 你不同意什么？如果我错了，后果是什么？
- 我漏了哪些关键前提？
- 哪些地方该我自己拍板，而不是让 AI 替我决定？
- 最小验证动作是什么？
必须给至少一个"我会阻断 / 要求补证 / 改方向"的判断。

我的方案：（填）
```

## Step 4 · Synthesize (open a third conversation, or just drop it into any AI)
Take both AIs' answers + your plan, drop them into any conversation, and say:

**English:**

```
Same problem, two independent judgments from different-family models, plus my plan.
Lay it out as a disagreement table: consensus / conflicts / blind spots only one side raised.
Don't settle it for me — list the points that genuinely need my decision.
```

**中文：**

```
这是同一个问题，两个不同模型各自独立的判断，加上我的方案。
帮我整理成一张分歧表：哪些是共识、哪些有分歧、哪些是只有一方提到的盲点。
不要替我下结论，把真正要我拍板的点列出来。
```

## Step 5 · You decide
Look at the disagreement table and decide for yourself. **The final call is yours, not the AI's.**

## In one line
No API, no coding tools, and you can still do fusion — the core was never the tooling, it's the act of "letting different-family AIs look independently first, then synthesizing yourself." Asking one AI twice is much weaker (overlapping blind spots); always use **different companies**.
