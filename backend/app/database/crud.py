from datetime import datetime

from app.database.models import (
    PullRequestReview,
    ReviewIssue
)


class ReviewRepository:


    def create_review(
        self,
        db,
        state
    ):

        review = PullRequestReview(

            repository=state["repository"],

            pr_number=state["pr_number"],

            author=state["sender"],

            risk_score=state["risk_score"],

            decision=state["decision"],

            summary=state["summary"],

            created_at=str(
                datetime.utcnow()
            )
        )

        db.add(review)

        db.commit()

        db.refresh(review)

        return review


    def create_issue(
        self,
        db,
        issue
    ):

        row = ReviewIssue(

            review_id=issue["review_id"],

            category=issue["category"],

            severity=issue["severity"],

            message=issue["message"],

            file_path=issue["file_path"],

            line_number=issue["line_number"]
        )

        db.add(row)

        db.commit()

        db.refresh(row)

        return row


    def get_reviews(
        self,
        db
    ):

        return db.query(
            PullRequestReview
        ).order_by(
            PullRequestReview.id.desc()
        ).all()


    def get_review(
        self,
        db,
        review_id
    ):

        return db.query(
            PullRequestReview
        ).filter(
            PullRequestReview.id == review_id
        ).first()


    # ✅ EXISTING METHOD (UNCHANGED)
    def get_review_by_id(
        self,
        db,
        review_id
    ):
        """
        Compatibility method used by DatabaseService.
        """

        return self.get_review(
            db,
            review_id
        )


    # 🆕 NEW METHOD ADDED (AS REQUESTED)
    def get_review_with_issues(
        self,
        db,
        review_id
    ):

        return db.query(
            PullRequestReview
        ).filter(
            PullRequestReview.id == review_id
        ).first()


    def create_review_issue(
        self,
        db,
        review_id,
        category,
        severity,
        message,
        file_path,
        line_number
    ):

        issue = ReviewIssue(

            review_id=review_id,

            category=category,

            severity=severity,

            message=message,

            file_path=file_path,

            line_number=line_number
        )

        db.add(issue)

        db.commit()

        db.refresh(issue)

        return issue