import requests

from app.config.settings import settings


class GithubService:


    def __init__(self):

        self.base_url = (

            "https://api.github.com"

        )


        self.headers = {

            "Authorization":

            f"Bearer {settings.GITHUB_TOKEN}",

            "Accept":

            "application/vnd.github+json"

        }


    def get_pull_request(

        self,

        owner,

        repo,

        pr_number

    ):

        url = (

            f"{self.base_url}"

            f"/repos/{owner}"

            f"/{repo}"

            f"/pulls/{pr_number}"

        )


        response = requests.get(

            url,

            headers=self.headers

        )


        response.raise_for_status()


        return response.json()


    def get_pull_request_files(

        self,

        owner,

        repo,

        pr_number

    ):

        url = (

            f"{self.base_url}"

            f"/repos/{owner}"

            f"/{repo}"

            f"/pulls/{pr_number}"

            f"/files"

        )


        response = requests.get(

            url,

            headers=self.headers

        )


        response.raise_for_status()


        return response.json()