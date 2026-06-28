from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.database.crud import ReviewRepository


router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"]
)

repo = ReviewRepository()


@router.get("/")
def get_reviews(
    db: Session = Depends(get_db)
):

    reviews = repo.get_reviews(db)

    result = []

    for review in reviews:

        result.append({

            "id": review.id,

            "repository": review.repository,

            "pr_number": review.pr_number,

            "author": review.author,

            "risk_score": review.risk_score,

            "decision": review.decision,

            "summary": review.summary

        })

    return result