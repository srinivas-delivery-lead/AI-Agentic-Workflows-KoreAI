# Prompt Chaining Template

## Use case
Banking customer-service assistant handling a customer query that may require both knowledge retrieval and an authenticated API action.

## Stage 1 — Intent understanding

**System goal:** Identify the customer's primary intent and required entities.

**Inputs**
- Customer message
- Channel
- Authentication state

**Output schema**
- intent
- confidence
- entities
- requires_authentication
- requires_transaction
- risk_level

## Stage 2 — Retrieval / grounding

Retrieve approved knowledge only from governed enterprise sources.

**Rules**
- Do not invent banking policy.
- Prefer current approved content.
- If evidence is insufficient, route to clarification or human support.

## Stage 3 — Action planning

Determine whether the assistant should:
- answer from knowledge,
- invoke an API,
- request authentication,
- ask a clarification question,
- or transfer to a human agent.

## Stage 4 — Response generation

Response should be:
- concise,
- grounded,
- transparent,
- free of unsupported guarantees,
- aligned with privacy and regulatory controls.

## Stage 5 — Validation

Before returning the answer:
- verify retrieved evidence,
- validate API response status,
- ensure no restricted data is exposed,
- confirm the requested action is within policy,
- record telemetry for monitoring.

## Example control pattern

```text
User Query
   |
Intent Classification
   |
Risk + Authentication Check
   |
Retrieval or API Action
   |
Policy / Safety Validation
   |
Response Generation
   |
Confidence Check
   |
Answer OR Human Handoff
```
