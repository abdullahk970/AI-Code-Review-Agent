from app.database.database import SessionLocal
from app.database.crud import ReviewRepository


class DatabaseService:

    def __init__(self):

        self.repo = ReviewRepository()


    def save_review(
        self,
        state,
        mapped_comments
    ):

        db = SessionLocal()

        try:

            review = self.repo.create_review(
                db,
                state
            )

            severity_map = {

                "security": "HIGH",

                "bugs": "MEDIUM",

                "performance": "MEDIUM",

                "style": "LOW"
            }

            for item in mapped_comments:

                self.repo.create_review_issue(

                    db=db,

                    review_id=review.id,

                    category=item["category"],

                    severity=severity_map[
                        item["category"]
                    ],

                    message=item["issue"],

                    file_path=item["path"],

                    line_number=item["line"]
                )

            return review

        finally:

            db.close()


    # ✅ UPDATED METHOD (AS REQUESTED)
    def get_review(self, review_id):

        db = SessionLocal()

        try:

            review = self.repo.get_review_with_issues(db, review_id)

            if not review:
                return None

            return {

                "id": review.id,
                "repository": review.repository,
                "pr_number": review.pr_number,
                "risk_score": review.risk_score,
                "decision": review.decision,
                "summary": review.summary,
                "created_at": review.created_at,
                "issues": review.issues
            }

        finally:

            db.close()