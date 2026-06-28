from app.services.llm_service import LLMService


def analyze_node(state):

    print("AI Analysis Running...")

    llm = LLMService()

    security = []
    bugs = []
    performance = []
    style = []

    for chunk in state["ai_input"]:

        result = llm.analyze_chunk(chunk)

        security.extend(result.get("security", []))
        bugs.extend(result.get("bugs", []))
        performance.extend(result.get("performance", []))
        style.extend(result.get("style", []))

    state["security_issues"] = security
    state["bug_issues"] = bugs
    state["performance_issues"] = performance
    state["style_issues"] = style

    return state