from app.services.review_orchestrator import (

    ReviewOrchestrator

)


orchestrator = ReviewOrchestrator()


response = orchestrator.run(

    repository="username/repo-name",

    pr_number="pr_number",

    sender="username"

)


print(response)