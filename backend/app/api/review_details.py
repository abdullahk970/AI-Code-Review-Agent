from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.database.models import (
    PullRequestReview
)


router = APIRouter(
    prefix="/review-details",
    tags=["Review Details"]
)


@router.get("/{review_id}")
def get_review_details(

    review_id: int,

    db: Session = Depends(get_db)
):

    review = db.query(
        PullRequestReview
    ).filter(
        PullRequestReview.id == review_id
    ).first()

    if not review:

        return {
            "error":
            "Review not found"
        }

    issues = []

    for issue in review.issues:

        issues.append({

            "category":
            issue.category,

            "severity":
            issue.severity,

            "message":
            issue.message,

            "file_path":
            issue.file_path,

            "line_number":
            issue.line_number
        })

    return {

        "id":
        review.id,

        "repository":
        review.repository,

        "pr_number":
        review.pr_number,

        "risk_score":
        review.risk_score,

        "decision":
        review.decision,

        "summary":
        review.summary,

        "issues":
        issues
    }