# L2 setup · Claude Code + Codex (author's own stack · semi-automated)

Best for: using Claude Code as your main conversation, with the official codex plugin installed (cross-family GPT). This is the most automated tier and the closest to "real fusion."

## One-time setup (≤3 steps)

1. Confirm the codex plugin is installed: you can call the `Agent` tool with `subagent_type: "codex:codex-rescue"`. (Note: `codex:codex-rescue` is the subagent name in the author's environment — yours may differ. Swap in whatever name your installed codex plugin actually uses.)
2. (Optional) Set up a same-family opus subagent for a second viewpoint: drop an agent into `.claude/agents/` with `model: opus` in its frontmatter.
3. Make sure the `CLAUDE_CODE_SUBAGENT_MODEL` env var **isn't set to a string** (especially not `inherit`, which overrides each subagent's model tiering). The safest move is to `unset` it.

## How calls work

- **Calling cross-family Codex (GPT)**: the `Agent` tool with `subagent_type: "codex:codex-rescue"` (again, this is the author's name — replace it with the actual subagent name from your installed codex plugin), set to **read-only explicitly** (see the hard constraint below).
- **Calling the same-family opus subagent**: the `Agent` tool with `subagent_type` set to your agent's name, or pass `model: opus`.

## ⚠️ Read-only hard constraint (required)

codex-rescue may default to `--write` (able to edit your files). Fusion is about **surfacing viewpoints, not taking action** — when you dispatch codex you **must state read-only explicitly in the prompt and forbid `--write`**, and require the reply to print its actual sandbox mode. Only trust it once you've confirmed read-only.

## Running fusion (follow the 7 steps in 01-protocol)

1. Trigger judgment (is it worth it?)
2. Build the context pack (**don't include the main conversation's plan**)
3. Round one: dispatch codex (cross-family) and the opus subagent (same-family) in parallel, each using the "round one prompt" from 01-protocol, **invisible to each other**
4. Round two: give the main conversation's plan to codex and run the "round two prompt" for adversarial review
5. The main conversation synthesizes → disagreement table
6. A human decides
7. Trace it

## Anti-recursion / anti-runaway (the author's field experience — recommended as-is)

- A codex reply **does not auto-trigger the next codex call** (prevents the infinite "review triggers review" loop).
- Set a cap on the cumulative number of auto-dispatched codex calls per session; stop and ask a human once you hit it.
- Feeding cross-family models each other's output carries a cache-proximity contamination risk — keep each round isolated.

## Single-tool variant (Cursor / Windsurf / Trae)

These tools support switching between models, but don't expose an "auto-call another model" API to the skill, so this tier is **manual multi-round**:

1. Run the "round one prompt" with model X, save the output.
2. Switch to model Y (**a different family**), run round one again, save it.
3. Feed both outputs + your plan to the current model and run the "synthesis" (the disagreement-table template from step 5 of 01-protocol).

What the skill does here: provide the two-round prompts + the disagreement-table template — you string them together by hand. It's essentially the same as L2, just with the model-switching step done manually.
