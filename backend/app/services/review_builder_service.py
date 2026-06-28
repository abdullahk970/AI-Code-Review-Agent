class ReviewBuilderService:

    def build_comment(self, mapped_issue, category):

        severity = {
            "security": "HIGH",
            "bugs": "MEDIUM",
            "performance": "MEDIUM",
            "style": "LOW"
        }

        body = (
            f"⚠️ {category.upper()} ISSUE\n\n"
            f"{mapped_issue['issue']}\n\n"
            f"Severity: {severity[category]}"
        )

        return {
            "path": mapped_issue["path"],
            "line": mapped_issue["line"],
            "body": body
        }

    def build_review(self, state, mapped_comments):

        comments = []

        for item in mapped_comments:

            comments.append(
                self.build_comment(
                    item,
                    item["category"]
                )
            )

        return {
            "body": state["summary"],
            "event": "COMMENT",
            "comments": comments
        }