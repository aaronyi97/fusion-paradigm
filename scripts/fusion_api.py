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
SYNTH_MODEL = MODEL_A  # 用哪个做最后综合，随意（建议用你更信任的那个）
# =======================================

ROUND1 = """你是被调用的跨家族独立模型。你看不到我的方案，也别猜我会怎么想。
只基于下面的问题/目标/约束/证据，从第一性原理给出独立判断：
1) 你自己的方案 2) 最可能被忽略的盲区 3) 哪些前提错了会推翻结论 4) 最小验证动作。
禁止"总体可行但需注意"空话；证据不足直接写"不知道/需要验证"。

{problem}"""

ROUND2 = """下面是我的方案。任务不是润色，也不是支持它。
先 3 句话回顾你第一轮判断，再逐条对照：同意什么/不同意什么(我错了的后果)/漏了哪些前提/哪些该人拍板/最小验证。
必须含至少一个"我会阻断/要求补证/改方向"。

我的方案：{plan}"""

SYNTH = """这是同一个问题，两个不同家族模型各自独立的判断。
整理成分歧表：共识 / 分歧 / 只有一方提到的盲点。不要替我下结论，把要拍板的点列给我。

模型A（{na}）：
{a}

模型B（{nb}）：
{b}"""


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

    # 第二轮（可选·严格版）：把你的方案给它们对抗审查
    # 注意：API 无状态，这里只传了方案、没回传第一轮输出；要严格"回顾第一轮"，
    # 需你在 call() 里把对应的第一轮输出(a1/b1)一起拼进 prompt。当前为骨架简化版。
    if args.plan:
        a1 = call(MODEL_A, ROUND2.format(plan=args.plan)) or a1
        b1 = call(MODEL_B, ROUND2.format(plan=args.plan)) or b1

    # 综合 → 分歧表（不替你拍板）
    synth = call(SYNTH_MODEL, SYNTH.format(
        na=MODEL_A["name"], nb=MODEL_B["name"], a=a1, b=b1))
    print("\n===== 分歧表（待你拍板）=====\n")
    print(synth)
    print("\n（拍板的是你，不是脚本。多模型共识 != 真相。）")


if __name__ == "__main__":
    main()
