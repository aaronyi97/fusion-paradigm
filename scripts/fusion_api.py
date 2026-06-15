#!/usr/bin/env python3
# ============================================================
# ⚠️ This is a reference SKELETON, not a ready-to-run tool.
# The call() function is empty (NotImplementedError) — you must fill in
# the few lines for your own SDK.
# Running `python fusion_api.py` directly raises NotImplementedError —
# that is expected behavior, not a bug.
# ============================================================
"""
fusion_api.py — fusion paradigm reference script (L1 · for people who only have an API key)

Follows the flow in references/01-protocol.md: two models from different
families judge independently → adversarial review → synthesis → leave the
final call to a human.
This is a reference skeleton, not a finished product — call() has a TODO,
just fill in the few lines for whatever SDK you use.

Usage:
  1. Set the model names in the CONFIG block below; export the two key env vars.
  2. python fusion_api.py --check                 # check that keys are present
  3. python fusion_api.py --question "your problem" # run fusion
  4. python fusion_api.py --lang zh --question ...  # switch prompts to Chinese (default: en)

Dependencies (install what you use): pip install anthropic openai
"""
import argparse
import os

# ============ CONFIG (edit here) ============
# Use two models from DIFFERENT families so their blind spots don't overlap.
# Replace the `name` values below with real model names you can access.
MODEL_A = {"vendor": "anthropic", "name": "claude-opus-4-x", "key_env": "ANTHROPIC_API_KEY"}
MODEL_B = {"vendor": "openai",    "name": "gpt-5-x",         "key_env": "OPENAI_API_KEY"}
# ⚠️ By default one of the contestants (MODEL_A) does the synthesis = the judge
# is also a player, so it may favor its own round-one judgment.
# If you can, swap in a third "non-competing" model for synthesis; if not, take
# its synthesis with a grain of salt — the human's final call is the backstop.
SYNTH_MODEL = MODEL_A
# ============================================

# ---- English prompts (default) ----
ROUND1_EN = """You're an independent model from a different family, pulled in for a genuine second opinion. You can't see my plan — and don't try to guess what I'm leaning toward. Working only from the problem, goal, constraints, and evidence below, give your own judgment from first principles:
1. Your own answer / verdict
2. The blind spot most likely to be missed
3. Which assumptions, if wrong, would overturn the conclusion
4. The smallest action that would verify it
No "broadly workable, but watch out for…" filler. If the evidence isn't enough, just say "don't know / needs verification."

{problem}"""

ROUND2_EN = """[Original problem (here it is again — don't lose the constraints)]
{problem}

[Your own round-one judgment (verbatim, for your review)]
{round1}

Below is my plan. Your job is not to polish it, and not to look for reasons to back it.
First, recap the key points of your round-one judgment in three sentences (if you now think round one was wrong, just say "overturning it" — don't rationalize). Then go point by point: what you agree with and why / what you disagree with (and if I'm wrong, the fallout) / which key assumptions I missed / which calls a human should make rather than a model auto-synthesizing / the smallest verifying action. You must include at least one "I'd block this / demand more evidence / change direction" call.

My plan: {plan}"""

SYNTH_EN = """Same problem, judged by two models from different families. Synthesize them (you get both the round-one independent take and the round-two adversarial review — don't drop round one).
[Problem] {problem}
{plan_block}
Model A ({na}) · round-one independent judgment:
{a1}

Model A ({na}) · round-two adversarial review:
{a2}

Model B ({nb}) · round-one independent judgment:
{b1}

Model B ({nb}) · round-two adversarial review:
{b2}

Lay it out as a disagreement table: consensus / conflicts / blind spots only one side raised. Don't quietly swallow the minority view — it's often the one that caught the mistake. Don't settle it for me; list the points that genuinely need my decision."""

# ---- Chinese prompts (--lang zh) ----
ROUND1_ZH = """你是被调用的跨家族独立模型。你看不到我的方案，也别猜我会怎么想。
只基于下面的问题/目标/约束/证据，从第一性原理给出独立判断：
1) 你自己的方案 2) 最可能被忽略的盲区 3) 哪些前提错了会推翻结论 4) 最小验证动作。
禁止"总体可行但需注意"空话；证据不足直接写"不知道/需要验证"。

{problem}"""

ROUND2_ZH = """【原问题（你第一轮看到的，再给你一次，别丢了约束）】
{problem}

【你第一轮基于上面问题给出的独立判断（原文，供你回顾）】
{round1}

下面是我的方案。任务不是润色，也不是支持它。
先 3 句话回顾你第一轮判断的要点（如果你现在认为第一轮错了，直接说"推翻"，别硬圆）；
再逐条对照：同意什么/不同意什么(我错了的后果)/漏了哪些前提/哪些该人拍板/最小验证。
必须含至少一个"我会阻断/要求补证/改方向"。

我的方案：{plan}"""

SYNTH_ZH = """同一个问题，两个不同家族模型的判断，请你综合（第一轮独立 + 第二轮对抗都给你，别丢第一轮）。
【问题】{problem}
{plan_block}
模型A（{na}）· 第一轮独立判断：
{a1}

模型A（{na}）· 第二轮对抗审查：
{a2}

模型B（{nb}）· 第一轮独立判断：
{b1}

模型B（{nb}）· 第二轮对抗审查：
{b2}

整理成分歧表：共识 / 分歧 / 只有一方提到的盲点。少数派意见不许无声吞掉。
不要替我下结论，把真正要我拍板的点列出来。"""


def call(model, prompt):
    """Call the matching API by vendor and return text. ⚠️ TODO: fill in for your SDK."""
    key = os.environ.get(model["key_env"], "")
    if not key:
        raise RuntimeError(f"Missing environment variable {model['key_env']}")
    # --- TODO: fill in per vendor (example) ---
    # if model["vendor"] == "anthropic":
    #     from anthropic import Anthropic
    #     r = Anthropic(api_key=key).messages.create(
    #         model=model["name"], max_tokens=2000,
    #         messages=[{"role": "user", "content": prompt}])
    #     return r.content[0].text
    # if model["vendor"] == "openai":
    #     from openai import OpenAI
    #     r = OpenAI(api_key=key).chat.completions.create(
    #         model=model["name"],
    #         messages=[{"role": "user", "content": prompt}])
    #     return r.choices[0].message.content
    raise NotImplementedError("Fill in call() for your SDK")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--question", help="Your problem or plan")
    ap.add_argument("--plan", help="(Optional) your plan, used for the strict second adversarial round")
    ap.add_argument("--check", action="store_true", help="Only check that the keys are present")
    ap.add_argument("--lang", choices=["en", "zh"], default="en",
                    help="Prompt language: en (default) or zh")
    args = ap.parse_args()

    # Pick the prompt set by language (en is default).
    round1 = ROUND1_EN if args.lang == "en" else ROUND1_ZH
    round2 = ROUND2_EN if args.lang == "en" else ROUND2_ZH
    synth_prompt = SYNTH_EN if args.lang == "en" else SYNTH_ZH

    if args.check:
        for m in (MODEL_A, MODEL_B):
            ok = bool(os.environ.get(m["key_env"]))
            if args.lang == "en":
                status = "OK" if ok else "MISSING"
            else:
                status = "已就绪" if ok else "缺失"
            print(f"{m['vendor']}/{m['name']}: key {status}")
        return

    q = args.question or input("Problem/plan: " if args.lang == "en" else "问题/方案：")

    # Round 1: two models judge independently (problem only, no hint of my leaning
    # — this is the foundation against anchoring).
    a1 = call(MODEL_A, round1.format(problem=q))
    b1 = call(MODEL_B, round1.format(problem=q))

    # Round 2 (optional · strict): hand them my plan for adversarial review.
    # Key: stitch [original problem q] + [round-one output a1/b1] back into the prompt.
    # The API is stateless and we don't pass state back, so the model can't see its
    # own round one and has lost the original constraints — "recapping round one"
    # would then be fabricated (i.e. a fake two rounds).
    # Round-one a1/b1 are kept and never overwritten; round two is stored separately
    # as a2/b2; if call() returns empty, fall back to round one.
    a2 = b2 = None
    if args.plan:
        a2 = call(MODEL_A, round2.format(problem=q, round1=a1, plan=args.plan)) or a1
        b2 = call(MODEL_B, round2.format(problem=q, round1=b1, plan=args.plan)) or b1

    # Human-facing strings, switched by --lang (en default). The prompt CONSTANTS
    # above are already localized; these are only the labels/placeholders/banners
    # that main() stitches in or prints.
    plan_label = "[My plan]" if args.lang == "en" else "【我的方案】"
    no_round2 = "(round two not run)" if args.lang == "en" else "（未跑第二轮）"
    table_title = ("\n===== Disagreement table (your call) =====\n"
                   if args.lang == "en"
                   else "\n===== 分歧表（待你拍板）=====\n")
    closing = ("\n(You make the call, not the script. Multi-model consensus != truth.)"
               if args.lang == "en"
               else "\n（拍板的是你，不是脚本。多模型共识 != 真相。）")

    # Synthesis → disagreement table: feed in the original problem + my plan + both
    # models' "round-one independent + round-two adversarial" — don't drop the
    # minority view, don't drop round one.
    synth = call(SYNTH_MODEL, synth_prompt.format(
        problem=q,
        plan_block=(f"{plan_label}\n{args.plan}\n" if args.plan else ""),
        na=MODEL_A["name"], a1=a1, a2=(a2 or no_round2),
        nb=MODEL_B["name"], b1=b1, b2=(b2 or no_round2)))
    print(table_title)
    print(synth)
    print(closing)


if __name__ == "__main__":
    main()
