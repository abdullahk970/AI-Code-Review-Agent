from app.services.review_builder_service import ReviewBuilderService


builder = ReviewBuilderService()

state = {
    "summary": "AI Review Completed"
}

mapped_comments = [
    {
        "path": "auth.py",
        "line": 3,
        "issue": "Hardcoded password detected",
        "category": "security"
    }
]

review = builder.build_review(state, mapped_comments)

print(review)