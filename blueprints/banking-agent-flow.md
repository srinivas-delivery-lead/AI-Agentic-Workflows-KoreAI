# Banking Conversational AI Blueprint

## Example: Lost or Stolen Card

```mermaid
flowchart TD
    A[Customer reports lost card] --> B{Authenticated?}
    B -- No --> C[Initiate secure authentication]
    C --> D{Authentication successful?}
    D -- No --> E[Offer human-agent transfer]
    D -- Yes --> F[Confirm card and intent]
    B -- Yes --> F
    F --> G[Call card-status API]
    G --> H{API available?}
    H -- No --> I[Explain temporary issue and offer agent transfer]
    H -- Yes --> J[Block card]
    J --> K[Confirm block status]
    K --> L[Offer replacement-card workflow]
    L --> M[Capture delivery preference]
    M --> N[Create service request]
    N --> O[Return reference number]
```

## Delivery considerations

- Authentication must be handled outside free-form LLM generation.
- Sensitive card data must never be inserted into prompts unnecessarily.
- API failures require deterministic fallback handling.
- High-risk actions should generate auditable events.
- Customer-facing confirmations should use API truth, not model inference.
