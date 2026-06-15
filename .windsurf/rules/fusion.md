---
trigger: always_on
---

# Fusion

Fusion is a paradigm for bringing in a model from a *different family* (GPT, Claude, others) to give an independent second opinion — first on its own, then against your plan — so you don't let one model decide alone. The core isn't "call a few more models," it's **stopping it from degrading into calling one more model just to nod along**.

> 中文一句话：把一个判断 / 设计问题，先交给"不同家族"的模型各自独立看，再综合分歧，最后人拍板。核心是防止它变成多叫一个模型来点赞。

## When to use / when not to

- **Use it**: plan design, architecture judgment, finalizing an important piece of writing, audits, retrospectives, high-stakes decisions — anywhere you need multiple angles and the cost of being wrong is high.
- **Don't use it**: writing code / running execution, looking up a simple fact, short translation, routine small edits. One model end to end is the most reliable here; multiple models just clash, slow you down, and cost more.

## Foundational rule (the bedrock — don't skip it)

**No round-one independent judgment, no fusion.**

- The model you call must give its own verdict **before** it sees your plan. Working only from the problem, goal, constraints, and evidence.
- **Never** show your plan, your leaning, or your conclusion in round one. The moment you do, the called model anchors to you and its independence drops to zero.
- Handing your plan straight to another model to "see if there's anything wrong" makes it a reviewer, not fusion. Withholding your main plan in round one is what makes the whole paradigm work.
- **Cross-family > multiple instances of the same family > a single model.** Same-company models share blind spots. If you can't get cross-family, tag it explicitly: "downgraded to same-family review, independence discounted."

## The two-round prompts (copy and adapt directly)

Run round one first. Get the independent verdict back. *Then* run round two with your plan.

### Round one · anti-anchoring independent judgment

```
You're an independent model brought in for a genuine second opinion. You can't see my plan — and don't try to guess what I'm leaning toward. Working only from the problem, goal, constraints, and evidence below, give your own judgment from first principles:
1. Your own answer / verdict
2. The blind spot most likely to be missed
3. Which assumptions, if wrong, would overturn the conclusion
4. The smallest action that would verify it
No "broadly workable, but watch out for…" filler. If the evidence isn't enough, just say "don't know / needs verification."

[Problem] / [Goal] / [Constraints] / [Known facts]
```

### Round two · adversarial review

```
Below is my plan. Your job is not to polish it, and not to look for reasons to back it.
First, recap your round-one judgment in three sentences (if you now think round one was wrong, just say "overturning it" — don't rationalize). Then, point by point: what you agree with and why / what you disagree with (and if I'm wrong, the fallout) / which key assumptions I missed / which calls a human should make rather than a model auto-synthesizing / the smallest verifying action. You must include at least one "I'd block this / demand more evidence / change direction" call.

[My plan]
```

## Synthesize — disagreement table, then a human decides

After both rounds, the main thread processes every view point by point and produces a disagreement table:

| Point of contention | What each side says | How I'm handling it |
|---|---|---|
| Some point | A says X / B says Y | Adopt X / reject / combine / hand to a human |

**Forbidden**: smoothing it over with a one-liner like "on balance it broadly works." Minority opinions must not be silently swallowed — they're often the very one that caught the mistake. The real trade-offs go to **a human** for the final call; a model doesn't get to arbitrate on a human's behalf. Note one line afterward: what did this fusion actually change about your judgment? "Changed nothing" → be wary you were anchored; "caught an X I hadn't seen" → that's where it earns its keep.

## Full flow

This file is the medium version. The complete 7-step flow, role assignments, both-language prompt templates, and the toy self-check live in **`SKILL.md`** and **`references/01-protocol.md`** — read those for the full paradigm. The flow doesn't change no matter what tool you use.

## ⚠️ Safety

Fusion sends your problem / plan to **multiple external models** — redact or leave out anything confidential, customer data, or non-public info first.
