from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.database.models import PullRequestReview


router = APIRouter(
    prefix="/stats",
    tags=["Stats"]
)


@router.get("/")
def get_stats(
    db: Session = Depends(get_db)
):

    reviews = db.query(
        PullRequestReview
    ).all()

    total_reviews = len(reviews)

    approvals = len([
        r
        for r in reviews
        if r.decision == "APPROVE"
    ])

    change_requests = len([
        r
        for r in reviews
        if r.decision == "REQUEST_CHANGES"
    ])

    return {

        "total_reviews":
        total_reviews,

        "approvals":
        approvals,

        "change_requests":
        change_requests
    }