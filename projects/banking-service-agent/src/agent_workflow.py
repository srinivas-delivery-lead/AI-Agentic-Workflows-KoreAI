"""Illustrative agentic banking workflow.

No external API or real banking system is used. This demonstrates orchestration,
specialist routing, guardrails, tool calls, and human-approval boundaries.
"""

from dataclasses import dataclass
from enum import Enum


class Risk(str, Enum):
    LOW = "low"
    HIGH = "high"


@dataclass
class Request:
    text: str
    authenticated: bool = False
    human_approved: bool = False


def classify(request: Request) -> dict:
    text = request.text.lower()
    if "lost" in text or "block" in text or "stolen" in text:
        return {"intent": "card_service", "risk": Risk.HIGH}
    if "dispute" in text or "transaction" in text:
        return {"intent": "transaction_dispute", "risk": Risk.HIGH}
    return {"intent": "knowledge_question", "risk": Risk.LOW}


def knowledge_agent(request: Request) -> str:
    # A production implementation would retrieve from an approved knowledge base.
    return "I can provide approved policy guidance or route you to the right service."


def mock_block_card_tool() -> dict:
    # Deterministic mock tool: no real customer/account data.
    return {"status": "blocked", "reference": "DEMO-REF-001"}


def card_service_agent(request: Request) -> str:
    if not request.authenticated:
        return "Authentication is required before a card-blocking action."
    if not request.human_approved:
        return "Human approval is required before this demo side effect."
    result = mock_block_card_tool()
    return f"Mock card action completed: {result['status']}; reference {result['reference']}."


def dispute_agent(request: Request) -> str:
    if not request.authenticated:
        return "Authentication is required before starting a dispute workflow."
    return "Dispute details captured for validation; no financial action was executed."


def orchestrate(request: Request) -> str:
    route = classify(request)
    if route["intent"] == "card_service":
        return card_service_agent(request)
    if route["intent"] == "transaction_dispute":
        return dispute_agent(request)
    return knowledge_agent(request)


if __name__ == "__main__":
    examples = [
        Request("What is the card replacement policy?"),
        Request("I lost my card. Please block it.", authenticated=True),
        Request(
            "I lost my card. Please block it.",
            authenticated=True,
            human_approved=True,
        ),
    ]

    for example in examples:
        print(f"USER: {example.text}")
        print(f"ASSISTANT: {orchestrate(example)}\n")
