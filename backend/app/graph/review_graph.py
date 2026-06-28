from langgraph.graph import StateGraph, END
from pydantic import BaseModel, Field
from typing import List, Dict, Any

from app.agents.bug_agent import BugAgent
from app.agents.security_agent import SecurityAgent
from app.agents.performance_agent import PerformanceAgent
from app.agents.style_agent import StyleAgent
from app.agents.aggregator import AggregatorAgent

bug_agent = BugAgent()
security_agent = SecurityAgent()
performance_agent = PerformanceAgent()
style_agent = StyleAgent()
aggregator = AggregatorAgent()


# ========================================
# PROPER STATE DEFINITION FOR LANGGRAPH
# ========================================
class ReviewState(BaseModel):
    """
    Properly defined state schema for LangGraph.
    This ensures state persistence and proper merging between nodes.
    """
    diff: str = Field(default="")
    repository: str = Field(default="")
    pr_number: int = Field(default=0)
    sender: str = Field(default="")
    bugs: List[Dict[str, Any]] = Field(default_factory=list)
    security: List[Dict[str, Any]] = Field(default_factory=list)
    performance: List[Dict[str, Any]] = Field(default_factory=list)
    style: List[Dict[str, Any]] = Field(default_factory=list)
    final: Dict[str, Any] = Field(default_factory=dict)


def bug_node(state: ReviewState) -> ReviewState:
    diff = state.diff

    print("[BUG NODE INPUT]", diff[:100] if diff else "")

    result = bug_agent.review(diff)

    print("[BUG NODE OUTPUT]", result)

    # Create new state with updated bugs
    state_dict = state.model_dump()
    state_dict["bugs"] = result.get("bugs", [])
    return ReviewState(**state_dict)


def security_node(state: ReviewState) -> ReviewState:
    diff = state.diff

    print("[SECURITY NODE INPUT]", diff[:100] if diff else "")

    result = security_agent.review(diff)

    print("[SECURITY NODE OUTPUT]", result)

    # Create new state with updated security
    state_dict = state.model_dump()
    state_dict["security"] = result.get("security", [])
    return ReviewState(**state_dict)


def performance_node(state: ReviewState) -> ReviewState:
    diff = state.diff

    print("[PERFORMANCE NODE INPUT]", diff[:100] if diff else "")

    result = performance_agent.review(diff)

    print("[PERFORMANCE NODE OUTPUT]", result)

    # Create new state with updated performance
    state_dict = state.model_dump()
    state_dict["performance"] = result.get("performance", [])
    return ReviewState(**state_dict)


def style_node(state: ReviewState) -> ReviewState:
    diff = state.diff

    print("[STYLE NODE INPUT]", diff[:100] if diff else "")

    result = style_agent.review(diff)

    print("[STYLE NODE OUTPUT]", result)

    # Create new state with updated style
    state_dict = state.model_dump()
    state_dict["style"] = result.get("style", [])
    return ReviewState(**state_dict)


def aggregator_node(state: ReviewState) -> ReviewState:

    print("\n========== FINAL STATE BEFORE AGGREGATION ==========")
    print("BUGS:", state.bugs)
    print("SECURITY:", state.security)
    print("PERFORMANCE:", state.performance)
    print("STYLE:", state.style)
    print("====================================================\n")

    result = aggregator.aggregate(
        state.bugs,
        state.security,
        state.performance,
        state.style
    )

    print("[AGGREGATOR RESULT]")
    print(result)

    # Create new state with aggregator result
    state_dict = state.model_dump()
    state_dict["final"] = result
    return ReviewState(**state_dict)


# ========================================
# LANGGRAPH CONFIGURATION
# ========================================
graph = StateGraph(ReviewState)

graph.add_node("bug", bug_node)
graph.add_node("security", security_node)
graph.add_node("performance", performance_node)
graph.add_node("style", style_node)
graph.add_node("aggregator", aggregator_node)

graph.set_entry_point("bug")

graph.add_edge("bug", "security")
graph.add_edge("security", "performance")
graph.add_edge("performance", "style")
graph.add_edge("style", "aggregator")
graph.add_edge("aggregator", END)

app = graph.compile()