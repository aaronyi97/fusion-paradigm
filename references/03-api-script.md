# L1 setup · API keys only (automation skeleton · you supply the SDK calls)

Best for: you have API keys for two different-family models (e.g. Anthropic's Claude + OpenAI's GPT, or DeepSeek + Kimi). **The most portable tier** — it doesn't depend on any IDE; anyone who can call an API can use it.

## One-time setup

1. Get two API keys from **different companies**.
2. Fill the model names into the CONFIG block at the top of `scripts/fusion_api.py`, or set the matching environment variables (keys).
3. Run `python scripts/fusion_api.py --check` once to verify the keys are present.

## How to use

```
python scripts/fusion_api.py --question "your question or plan"
```

The script follows 01-protocol: it sends the problem (without your leaning) to two different-family models in turn → each produces an independent round-one output → it synthesizes a disagreement table → it leaves the decision to you. **Note that `call()` is empty (see below); the script can't actually run until you wire up the SDK calls.**

## Notes

- The script is a **reference skeleton**, and the `call()` function is empty (it raises `NotImplementedError` outright) — wire up those few lines for whatever SDK you use (anthropic / openai / other). The logic skeleton is already in place. **It is not ready to run out of the box: until you fill `call()` in, `--question` will fail — that's expected, not a bug.**
- By default the script **doesn't decide for you**; it only outputs the disagreement table + the points left to call.
- Strict two rounds is implemented: once you pass `--plan`, round two feeds the model **the round-one output + the original problem together** (no more stateless fake recap), so the round-one independent judgment isn't overwritten and it takes part in the synthesis.
- This tier is the best one to turn into your own little tool and embed into any workflow.
