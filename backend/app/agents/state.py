from typing import TypedDict


class AgentState(TypedDict):

    repository: str

    pr_number: int

    sender: str

    ai_input: list

    security_issues: list

    bug_issues: list

    performance_issues: list

    style_issues: list

    risk_score: int

    summary: str

    decision: str