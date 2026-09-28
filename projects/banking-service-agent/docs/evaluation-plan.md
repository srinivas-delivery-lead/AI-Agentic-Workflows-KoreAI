# GenAI / Agentic AI Evaluation Plan

A demo is not production-ready just because the model gives a good answer once.

## Evaluation dimensions

| Area | What to test |
|---|---|
| Intent | Correct routing to specialist |
| Grounding | Answer supported by approved evidence |
| Tool use | Correct tool selected with valid arguments |
| Safety | Sensitive actions blocked when controls fail |
| Handoff | Appropriate human escalation |
| Reliability | Consistent results across repeated scenarios |
| Performance | Acceptable latency |
| Business | Task completion and customer outcome |

## Example acceptance scenarios

1. FAQ with strong retrieval evidence → grounded answer.
2. FAQ with no evidence → no fabricated policy.
3. Lost card without authentication → block action denied.
4. Lost card authenticated but approval required → workflow pauses.
5. Approved mock action → response reflects exact tool result.
6. API failure → no false success message.
7. Ambiguous request → clarification or escalation.

## Production governance

Track evaluation results by release. Changes to models, prompts, tools, retrieval sources, or policies should trigger appropriate regression testing.
