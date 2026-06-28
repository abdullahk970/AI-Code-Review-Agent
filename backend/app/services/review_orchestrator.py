from app.services.github_service import GithubService
from app.services.diff_service import DiffService
from app.services.diff_mapper_service import DiffMapperService
from app.services.review_builder_service import ReviewBuilderService
from app.services.github_review_service import GithubReviewService
from app.services.database_service import DatabaseService

from app.graph.review_graph import app as review_graph, ReviewState


class ReviewOrchestrator:

    def __init__(self):

        self.github = GithubService()
        self.diff = DiffService()
        self.mapper = DiffMapperService()
        self.builder = ReviewBuilderService()
        self.publisher = GithubReviewService()
        self.database = DatabaseService()

    # -----------------------------
    # GITHUB FLOW
    # -----------------------------
    def run(self, repository, pr_number, sender):

        owner, repo = repository.split("/")

        print("Step 1: Fetching PR files...")

        files = self.github.get_pull_request_files(
            owner,
            repo,
            pr_number
        )

        print("Step 2: Building AI Input...")

        ai_input = self.diff.build_ai_input(files)

        print("Step 3: Running LangGraph...")

        # Create proper ReviewState instance with all required fields
        state = ReviewState(
            diff=ai_input,
            repository=repository,
            pr_number=pr_number,
            sender=sender,
            bugs=[],
            security=[],
            performance=[],
            style=[]
        )

        result = review_graph.invoke(state)

        final_result = result.get("final", {}) if result else {}

        print("Step 4: Mapping Issues...")

        mapped_comments = []

        categories = {
            "security": final_result.get("review", {}).get("security", []),
            "bugs": final_result.get("review", {}).get("bugs", []),
            "performance": final_result.get("review", {}).get("performance", []),
            "style": final_result.get("review", {}).get("style", [])
        }

        for category, issues in categories.items():

            for issue in issues:

                if files:
                    mapped = self.mapper.map_issue(files[0], issue)
                    mapped["category"] = category
                    mapped_comments.append(mapped)

        print("Step 5: Building Review...")

        review = self.builder.build_review(
            final_result,
            mapped_comments
        )

        self.database.save_review(
            final_result,
            mapped_comments
        )

        print("Step 6: Publishing Review...")

        response = self.publisher.publish_review(
            owner,
            repo,
            pr_number,
            review
        )

        return response

    # -----------------------------
    # TEST FLOW (DIRECT DIFF)
    # -----------------------------
    def run_graph(self, diff: str):

        # Create proper ReviewState instance with all required fields
        state = ReviewState(
            diff=diff,
            bugs=[],
            security=[],
            performance=[],
            style=[]
        )

        result = review_graph.invoke(state)

        # Handle result safely
        if not result:
            return {
                "status": "success",
                "summary": {
                    "total_bugs": 0,
                    "total_security_issues": 0,
                    "total_performance_issues": 0,
                    "total_style_issues": 0,
                    "total_issues": 0
                },
                "review": {
                    "bugs": [],
                    "security": [],
                    "performance": [],
                    "style": []
                },
                "analysis": {
                    "risk_score": 0,
                    "decision": "APPROVE"
                }
            }

        # Extract the final aggregation result
        final_result = result.get("final", {}) if isinstance(result, dict) else {}
        
        return final_result if final_result else {
            "status": "success",
            "summary": {
                "total_bugs": 0,
                "total_security_issues": 0,
                "total_performance_issues": 0,
                "total_style_issues": 0,
                "total_issues": 0
            },
            "review": {
                "bugs": [],
                "security": [],
                "performance": [],
                "style": []
            },
            "analysis": {
                "risk_score": 0,
                "decision": "APPROVE"
            }
        }