from app.database.database import SessionLocal
from app.database.crud import ReviewRepository


db = SessionLocal()

repo = ReviewRepository()

review = repo.create_review(
    db=db,
    state={
        "repository": "test/repo",
        "pr_number": 1,
        "sender": "test-user",
        "risk_score": 30,
        "decision": "APPROVE",
        "summary": "Test review inserted manually"
    }
)

print("Inserted Review ID:", review.id)

db.close()