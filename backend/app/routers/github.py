from fastapi import APIRouter
from fastapi import Header
from fastapi import HTTPException
from fastapi import Request

from app.config.settings import settings
from app.utils.security import verify_github_signature
from app.services.review_orchestrator import ReviewOrchestrator
from app.agents.bug_agent import BugAgent
from app.agents.security_agent import SecurityAgent
from app.agents.performance_agent import PerformanceAgent
from app.agents.style_agent import StyleAgent

router = APIRouter(
    prefix="/github",
    tags=["Github"]
)


@router.post("/webhook")
async def github_webhook(
    request: Request,
    x_github_event: str = Header(None),
    x_hub_signature_256: str = Header(None)
):
    """
    GitHub Webhook Endpoint

    This endpoint receives Pull Request events from GitHub,
    verifies the webhook signature, extracts PR information,
    and starts the AI Code Review pipeline.
    """

    payload = await request.body()

    # -----------------------------------
    # SECURITY CHECK
    # -----------------------------------
    if not settings.DEBUG:

        is_valid = verify_github_signature(
            payload,
            x_hub_signature_256,
            settings.GITHUB_WEBHOOK_SECRET
        )

        if not is_valid:
            raise HTTPException(
                status_code=401,
                detail="Invalid Signature"
            )

    # -----------------------------------
    # PARSE JSON
    # -----------------------------------
    try:
        data = await request.json()

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid JSON"
        )

    # -----------------------------------
    # EXTRACT PULL REQUEST INFORMATION
    # -----------------------------------
    repository = data.get("repository", {}).get("full_name")

    pr_number = data.get("pull_request", {}).get("number")

    sender = data.get("sender", {}).get("login")

    if not repository or not pr_number:
        raise HTTPException(
            status_code=400,
            detail="Pull Request data not found."
        )

    # -----------------------------------
    # START AI REVIEW PIPELINE
    # -----------------------------------
    orchestrator = ReviewOrchestrator()

    response = orchestrator.run(
        repository=repository,
        pr_number=pr_number,
        sender=sender
    )

    # -----------------------------------
    # RETURN RESPONSE
    # -----------------------------------
    return {
        "status": "success",
        "repository": repository,
        "pull_request": pr_number,
        "review": response
    }


@router.post("/test-review")
async def test_review():
    """
    Developer Testing Endpoint

    This endpoint triggers the complete AI review pipeline
    without requiring a GitHub webhook.

    Usage:
    Execute directly from Swagger.
    """

    orchestrator = ReviewOrchestrator()

    response = orchestrator.run(
        repository="username/repo-name",
        pr_number="pr_number",
        sender="local-test"
    )

    return {
        "status": "success",
        "message": "AI Review Pipeline Executed Successfully",
        "review": response
    }

@router.post("/test-bug-agent")
async def test_bug_agent():
    """
    Test endpoint for the Bug Agent.
    This endpoint runs the Bug Agent on a sample Git diff.
    """

    sample_diff = """
diff --git a/main.py b/main.py

+ user = None

+ print(user.name)

+ if x == 10:
+     pass
"""

    agent = BugAgent()

    result = agent.review(sample_diff)

    return {
        "status": "success",
        "agent": "Bug Agent",
        "result": result
    }

@router.post("/test-security-agent")
async def test_security_agent():

    sample_diff = """
diff --git a/app.py b/app.py

+ password = ""

+ API_KEY = "sk_test_123456"

+ cursor.execute(
+     "SELECT * FROM users WHERE id = " + user_id
+ )

+ eval(user_input)
"""

    agent = SecurityAgent()

    result = agent.review(sample_diff)

    return {
        "status": "success",
        "agent": "Security Agent",
        "result": result
    }

@router.post("/test-performance-agent")
async def test_performance_agent():

    sample_diff = """
diff --git a/app.py b/app.py

+ for i in range(len(users)):
+     for j in range(len(users)):
+         print(users[i], users[j])

+ for user in users:
+     user_data = db.get(user.id)

+ for user in users:
+     db.query("SELECT * FROM orders WHERE user_id = " + user.id)
"""

    agent = PerformanceAgent()

    result = agent.review(sample_diff)

    return {
        "status": "success",
        "agent": "Performance Agent",
        "result": result
    }

@router.post("/test-style-agent")
async def test_style_agent():

    sample_diff = """
diff --git a/app.py b/app.py

+ def a(x,y):
+     return x+y

+ def process(d):
+     for i in d:
+         print(i)
"""

    agent = StyleAgent()

    result = agent.review(sample_diff)

    return {
        "status": "success",
        "agent": "Style Agent",
        "result": result
    }

@router.post("/test-full-review")
async def test_full_review():

    sample_diff = """
diff --git a/app.py b/app.py

+ password = ""
+ print(user.name)

+ for i in range(len(users)):
+     for j in range(len(users)):
+         print(i, j)

+ def a(x,y): return x+y
"""

    orchestrator = ReviewOrchestrator()

    result = orchestrator.run_graph(sample_diff)

    return result