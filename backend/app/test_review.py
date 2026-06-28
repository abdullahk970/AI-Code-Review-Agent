from app.services.review_builder_service import ReviewBuilderService

builder = ReviewBuilderService()

state = {
    "summary": "AI Review Completed",

    "security_issues": [
        "Hardcoded password detected"
    ],

    "bug_issues": [],
    "performance_issues": [],
    "style_issues": []
}

review = builder.build_review(state)

print(review)