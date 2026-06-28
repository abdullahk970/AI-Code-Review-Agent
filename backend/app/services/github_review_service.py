import requests
from app.config.settings import settings


class GithubReviewService:

    def __init__(self):

        self.base_url = "https://api.github.com"

        self.headers = {
            "Authorization": f"Bearer {settings.GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json"
        }

    def publish_review(self, owner, repo, pr_number, review):

        url = (
            f"{self.base_url}/repos/"
            f"{owner}/{repo}/pulls/"
            f"{pr_number}/reviews"
        )

        response = requests.post(
            url,
            headers=self.headers,
            json=review
        )

        response.raise_for_status()

        return response.json()