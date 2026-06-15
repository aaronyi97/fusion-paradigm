# Fusion Protocol (core flow · cross-tool)

This is the soul of the fusion paradigm. Whatever tool you use, this flow doesn't change. Its entire value is in **stopping fusion from degrading into "calling one more model just to nod along."**

## Foundational rule

**No round-one independent judgment, no fusion.**

- ✅ Real fusion: first give the problem (without your plan) to models from different families, let each produce an independent judgment, then have them push back, then synthesize.
- ❌ Fake fusion: handing your plan to another model to "see if there's anything wrong" — it'll follow your lead and tack on a few risks, with blind spots that overlap yours. That's a reviewer, not fusion.

## 7-step flow

### 1 · Trigger judgment
First ask: is this worth a fusion?
- Worth it: plan design / architecture / audit / retrospective / high-stakes decision (many angles, high cost of being wrong)
- Not worth it: coding / execution / simple facts / short translation / routine small edits → one model, no fusion

### 2 · Build the context pack (the key to anti-anchoring)
What you give the called models is **only**: the problem, the goal, the constraints, the known facts.
**Never give**: your plan, your leaning, your conclusion. The moment you do, the called model is anchored to you and its independence drops to zero.

### 3 · Round one · independent output
Have models from different families, working from the context pack, **independently** produce their own plan / objection / risks, without seeing your plan.

### 4 · Round two · adversarial review
Now, and only now, give them your plan and have them hunt for holes and disagreements — not polishing, picking it apart.

### 5 · Synthesize (you do this, and don't fudge it)
Process every view point by point and produce a disagreement table:

| Point of contention | What each side says | How I'm handling it |
|---|---|---|
| Some point | A says X / B says Y | Adopt X / reject / combine / hand to a human |

**Forbidden**: smoothing it over with a one-liner like "on balance it broadly works." Minority opinions must not be silently swallowed — they're often the very one that caught the mistake.

### 6 · Human decides
The real trade-off points go to a human; don't let a model pretend to arbitrate on a human's behalf.

### 7 · Trace and evaluate (prove it actually worked)
Note one line: **what did this fusion actually change about your judgment?**
- "Changed nothing, just confirmed what I already thought" → be wary, you may have been anchored (fake fusion).
- "Caught an X I hadn't seen" → that's where it earns its keep.

## Both-round prompt templates (copy and adapt directly)

Two versions of each round are kept below — an English version and a Chinese version, separately. Don't mix them; pick the language you're working in.

### Round one · anti-anchoring independent judgment

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
你是被调用的跨家族独立模型。你现在看不到我的方案，也别猜我会怎么想。
只基于下面的问题、目标、约束和证据，从第一性原理给出独立判断：
1. 你自己的方案 / verdict
2. 最可能被忽略的盲区
3. 哪些前提如果错了会推翻结论
4. 最小验证动作
禁止"总体可行但需注意"这种空话。证据不足就直接写"不知道 / 需要验证"。

【问题】…
【目标】…
【约束】…
【已知事实】…
```

### Round two · adversarial review

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
先用 3 句话回顾你第一轮的独立判断，然后逐条对照：
- 你同意什么？为什么？
- 你不同意什么？如果我错了，后果是什么？
- 我漏了哪些关键前提？
- 哪些地方该人拍板，而不是模型自动综合？
- 最小验证动作是什么？
必须包含至少一个"我会阻断 / 要求补证 / 改方向"的判断；没有的话，解释为什么。

【我的方案】…
```

## Role assignments (pick 1–2 per task, write into the start of round one)

- **Opposing architecture auditor**: find where this plan is most likely to fail in real use. Default stance — the main plan may be wrong unless the evidence supports it.
- **Fact-checker**: review facts only. Tag every conclusion "verified / inferred / unknown." Anything with no source or that can't be reproduced is never written up as fact.
- **Competing-solution designer**: independently propose a different viable solution. Don't comment on the main plan first — design your own first, then list the costs of your solution.

## Toy self-check (run through it every time)

| Signal | What it means | Toy? |
|---|---|---|
| The called model only added a few "watch the risks" lines | It got anchored to you | ⚠️ Yes |
| Several models all say "it works" | They may be wrong together, especially same-family | ⚠️ Consensus ≠ truth |
| Output got longer but the judgment didn't change | Ceremonial approval button | ⚠️ Yes |
| Caught a blind spot you hadn't seen / changed your judgment | Actually working | ✅ No |

## Three boundaries

1. **Multi-model consensus ≠ truth**. They can be wrong together; the judge / synthesizer isn't a court, it just helps you sort out the dispute.
2. **Cross-family > multiple instances of the same family > a single model**. Same-company models have overlapping blind spots, so cross-review is roughly the same as not switching anyone in. If you can't get cross-family, explicitly tag it "downgraded to same-family review, independence discounted."
3. **You make the final call**, not the models. This gives you a helper; it doesn't outsource the judgment.
