from pydantic import BaseModel


class ReviewComment(BaseModel):
    path: str
    body: str
    line: int


class PullRequestReview(BaseModel):
    body: str
    event: str
    comments: list