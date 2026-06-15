# Fusion

Fusion is a paradigm for bringing in a model from a *different family* (GPT, Claude, others) to give an independent second opinion — first on its own, then against the plan — instead of letting one model decide alone. The core isn't "call a few more models," it's stopping it from degrading into calling one more model just to nod along.

中文一句话：把一个判断 / 设计问题，先交给"不同家族"的模型各自独立看，再综合分歧，最后人拍板。

## When to use / when not to

- Use it: plan design, architecture judgment, finalizing important writing, audits, retrospectives, high-stakes decisions — where multiple angles matter and the cost of being wrong is high.
- Don't use it: writing code / execution, simple facts, short translation, routine small edits. One model end to end is more reliable there.

## Foundational rule (don't skip it)

- No round-one independent judgment, no fusion. The other model must give its own verdict from the problem, goal, constraints, and evidence **before** it sees the plan.
- Never reveal the plan, the leaning, or the conclusion in round one — that anchors the model and drops its independence to zero. Handing the plan over to "check for problems" makes it a reviewer, not fusion.
- Cross-family > multiple instances of the same family > a single model. Same-company models share blind spots. If you can't get cross-family, tag it "downgraded to same-family review, independence discounted."

## Two rounds, then synthesize

1. Round one: other model gives an independent verdict, blind spots, overturning assumptions, and the smallest verifying action — without seeing the plan.
2. Round two: now show the plan and have it hunt for holes (not polish), including at least one "block / demand more evidence / change direction" call.
3. Synthesize into a disagreement table — never smooth it over with "on balance it works," never silently drop minority views.
4. A human makes the final call. Note one line: what did this fusion actually change?

## Full flow + the copy-paste prompt templates

This is the short version. The complete 7-step flow, the two-round prompt templates (English + Chinese), role assignments, and the self-check live in `SKILL.md` and `references/01-protocol.md`. Read those for the full paradigm.

## Safety

Fusion sends the problem / plan to multiple external models — redact or leave out anything confidential, customer data, or non-public info first.
