from langgraph.graph import StateGraph

from app.agents.state import AgentState

from app.agents.nodes.fetch_node import fetch_node
from app.agents.nodes.analyze_node import analyze_node
from app.agents.nodes.risk_node import risk_node
from app.agents.nodes.summary_node import summary_node
from app.agents.nodes.decision_node import decision_node


builder = StateGraph(AgentState)

builder.add_node("fetch", fetch_node)
builder.add_node("analyze", analyze_node)
builder.add_node("risk", risk_node)
builder.add_node("summary", summary_node)
builder.add_node("decision", decision_node)

builder.set_entry_point("fetch")

builder.add_edge("fetch", "analyze")
builder.add_edge("analyze", "risk")
builder.add_edge("risk", "summary")
builder.add_edge("summary", "decision")

graph = builder.compile()