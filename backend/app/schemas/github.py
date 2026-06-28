from pydantic import BaseModel


class Repository(BaseModel):

    full_name: str


class PullRequest(BaseModel):

    number: int

    title: str

    state: str

    diff_url: str

    html_url: str


class Sender(BaseModel):

    login: str


class PullRequestPayload(BaseModel):

    action: str

    repository: Repository

    pull_request: PullRequest

    sender: Sender