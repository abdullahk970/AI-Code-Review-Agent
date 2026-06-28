from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class PullRequestReview(Base):

    __tablename__ = "pull_request_reviews"

    id = Column(Integer, primary_key=True)

    repository = Column(String)

    pr_number = Column(Integer)

    author = Column(String)

    risk_score = Column(Integer)

    decision = Column(String)

    summary = Column(Text)

    created_at = Column(String)

    issues = relationship(
        "ReviewIssue",
        back_populates="review"
    )


class ReviewIssue(Base):

    __tablename__ = "review_issues"

    id = Column(Integer, primary_key=True)

    review_id = Column(
        Integer,
        ForeignKey(
            "pull_request_reviews.id"
        )
    )

    category = Column(String)

    severity = Column(String)

    message = Column(Text)

    file_path = Column(String)

    line_number = Column(Integer)

    review = relationship(
        "PullRequestReview",
        back_populates="issues"
    )