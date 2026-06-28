from app.agents.graph import graph


state = {
    "repository": "user/project",
    "pr_number": "pr_number",
    "sender": "user",

    "ai_input": [
        {
            "filename": "auth.py",
            "language": "python",
            "code": """
password="1234"

def login():
    print(password)
"""
        }
    ],

    "security_issues": [],
    "bug_issues": [],
    "performance_issues": [],
    "style_issues": [],

    "risk_score": 0,
    "summary": "",
    "decision": ""
}


result = graph.invoke(state)

print(result)