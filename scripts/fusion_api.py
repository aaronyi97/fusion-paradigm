#!/usr/bin/env python3
# ============================================================
# ⚠️ 这是参考骨架（SKELETON），不是开箱即用的成品。
# call() 函数是空的（NotImplementedError）——你必须按自己的 SDK 补全那几行。
# 直接 `python fusion_api.py` 会报 NotImplementedError，这是预期行为，不是 bug。
# ============================================================
"""
fusion_api.py — fusion 范式参考脚本（L1 · 只有 API key 的人用）

按 references/01-protocol.md 的流程跑：两个不同家族模型独立判断 → 综合 → 留给人拍板。
这是参考骨架，不是成品——call() 函数留了 TODO，按你用的 SDK 补全那几行即可。

用法：
  1. 填下面 CONFIG 区的 model 名；设好两个 key 的环境变量。
  2. python fusion_api.py --check               # 验证 key 在不在
  3. python fusion_api.py --question "你的问题"   # 跑 fusion

依赖（按你用的补）：pip install anthropic openai
"""
import argparse
import os

# ============ CONFIG（改这里）============
# 用两个"不同家族"的模型，盲区才不重叠。下面的 name 换成你能用的真实模型名。
MODEL_A = {"vendor": "anthropic", "name": "claude-opus-4-x", "key_env": "ANTHROPIC_API_KEY"}
MODEL_B = {"vendor": "openai",    "name": "gpt-5-x",         "key_env": "OPENAI_API_KEY"}
# ⚠️ 默认用参赛者之一(MODEL_A)做综合 = 裁判也是运动员，它可能偏向自己第一轮的判断。
# 有条件就换第三个"没参赛"的模型做综合；做不到就对它的综合多留个心眼——最后人拍板兜底。
SYNTH_MODEL = MODEL_A
# =======================================

ROUND1 = """你是被调用的跨家族独立模型。你看不到我的方案，也别猜我会怎么想。
只基于下面的问题/目标/约束/证据，从第一性原理给出独立判断：
1) 你自己的方案 2) 最可能被忽略的盲区 3) 哪些前提错了会推翻结论 4) 最小验证动作。
禁止"总体可行但需注意"空话；证据不足直接写"不知道/需要验证"。

{problem}"""

ROUND2 = """【原问题（你第一轮看到的，再给你一次，别丢了约束）】
{problem}

【你第一轮基于上面问题给出的独立判断（原文，供你回顾）】
{round1}

下面是我的方案。任务不是润色，也不是支持它。
先 3 句话回顾你第一轮判断的要点（如果你现在认为第一轮错了，直接说"推翻"，别硬圆）；
再逐条对照：同意什么/不同意什么(我错了的后果)/漏了哪些前提/哪些该人拍板/最小验证。
必须含至少一个"我会阻断/要求补证/改方向"。

我的方案：{plan}"""

SYNTH = """同一个问题，两个不同家族模型的判断，请你综合（第一轮独立 + 第二轮对抗都给你，别丢第一轮）。
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
    """按 vendor 调对应 API，返回文本。⚠️ TODO：按你的 SDK 补全。"""
    key = os.environ.get(model["key_env"], "")
    if not key:
        raise RuntimeError(f"缺少环境变量 {model['key_env']}")
    # --- TODO 按 vendor 补全（示例）---
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
    raise NotImplementedError("按你的 SDK 补全 call()")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--question", help="你的问题或方案")
    ap.add_argument("--plan", help="（可选）你的方案，用于严格第二轮对抗")
    ap.add_argument("--check", action="store_true", help="只验证 key 在不在")
    args = ap.parse_args()

    if args.check:
        for m in (MODEL_A, MODEL_B):
            ok = bool(os.environ.get(m["key_env"]))
            print(f"{m['vendor']}/{m['name']}: key {'OK' if ok else '缺失'}")
        return

    q = args.question or input("问题/方案：")

    # 第一轮：两家独立（只给问题，不给你的倾向 —— 防锚定的地基）
    a1 = call(MODEL_A, ROUND1.format(problem=q))
    b1 = call(MODEL_B, ROUND1.format(problem=q))

    # 第二轮（可选·严格版）：把你的方案给它们对抗审查。
    # 关键：把【原问题 q】+【第一轮输出 a1/b1】一起拼进 prompt——API 无状态，不回传，
    # 模型就看不到自己第一轮、也丢了原约束，"回顾第一轮"只能靠编（那就是假两轮）。
    # 第一轮 a1/b1 保留不覆盖；第二轮单独存 a2/b2；call() 返回空时兜底回退第一轮。
    a2 = b2 = None
    if args.plan:
        a2 = call(MODEL_A, ROUND2.format(problem=q, round1=a1, plan=args.plan)) or a1
        b2 = call(MODEL_B, ROUND2.format(problem=q, round1=b1, plan=args.plan)) or b1

    # 综合 → 分歧表：原问题 + 你的方案 + 两家"第一轮独立 + 第二轮对抗"全喂进去，不丢少数派、不丢第一轮。
    synth = call(SYNTH_MODEL, SYNTH.format(
        problem=q,
        plan_block=(f"【我的方案】\n{args.plan}\n" if args.plan else ""),
        na=MODEL_A["name"], a1=a1, a2=(a2 or "（未跑第二轮）"),
        nb=MODEL_B["name"], b1=b1, b2=(b2 or "（未跑第二轮）")))
    print("\n===== 分歧表（待你拍板）=====\n")
    print(synth)
    print("\n（拍板的是你，不是脚本。多模型共识 != 真相。）")


if __name__ == "__main__":
    main()
