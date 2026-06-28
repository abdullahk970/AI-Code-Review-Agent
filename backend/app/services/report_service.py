from pathlib import Path
from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


class ReportService:

    def __init__(self):

        self.output_folder = Path("reports")
        self.output_folder.mkdir(exist_ok=True)

    def generate_report(self, review):

        filename = f"AI_Code_Review_{review['id']}.pdf"

        filepath = self.output_folder / filename

        styles = getSampleStyleSheet()

        doc = SimpleDocTemplate(str(filepath))

        story = []

        # =====================================
        # TITLE
        # =====================================

        story.append(
            Paragraph(
                "<b>AI Code Review Report</b>",
                styles["Title"]
            )
        )

        story.append(Spacer(1, 20))

        # =====================================
        # BASIC INFORMATION
        # =====================================

        story.append(
            Paragraph(
                f"<b>Repository:</b> {review['repository']}",
                styles["BodyText"]
            )
        )

        story.append(
            Paragraph(
                f"<b>Pull Request:</b> #{review['pr_number']}",
                styles["BodyText"]
            )
        )

        story.append(
            Paragraph(
                f"<b>Decision:</b> {review['decision']}",
                styles["BodyText"]
            )
        )

        story.append(
            Paragraph(
                f"<b>Risk Score:</b> {review['risk_score']}",
                styles["BodyText"]
            )
        )

        story.append(Spacer(1, 20))

        # =====================================
        # SUMMARY
        # =====================================

        story.append(
            Paragraph(
                "<b>Summary</b>",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                str(review["summary"]),
                styles["BodyText"]
            )
        )

        story.append(Spacer(1, 20))

        # =====================================
        # ISSUE SUMMARY
        # =====================================

        issues = review.get("issues", [])

        total = len(issues)

        bugs = len([i for i in issues if i.category == "bugs"])
        security = len([i for i in issues if i.category == "security"])
        performance = len([i for i in issues if i.category == "performance"])
        style = len([i for i in issues if i.category == "style"])

        story.append(
            Paragraph(
                "<b>Issue Summary</b>",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(f"Total Issues : {total}", styles["BodyText"])
        )

        story.append(
            Paragraph(f"Bug Issues : {bugs}", styles["BodyText"])
        )

        story.append(
            Paragraph(f"Security Issues : {security}", styles["BodyText"])
        )

        story.append(
            Paragraph(f"Performance Issues : {performance}", styles["BodyText"])
        )

        story.append(
            Paragraph(f"Style Issues : {style}", styles["BodyText"])
        )

        story.append(Spacer(1, 20))

        # =====================================
        # ISSUE DETAILS
        # =====================================

        story.append(
            Paragraph(
                "<b>Detected Issues</b>",
                styles["Heading2"]
            )
        )

        if total == 0:

            story.append(
                Paragraph(
                    "No issues detected by the AI Reviewer.",
                    styles["BodyText"]
                )
            )

        else:

            for index, issue in enumerate(issues, start=1):

                story.append(
                    Paragraph(
                        f"<b>{index}. {issue.category.upper()}</b>",
                        styles["Heading3"]
                    )
                )

                story.append(
                    Paragraph(
                        f"<b>Severity:</b> {issue.severity}",
                        styles["BodyText"]
                    )
                )

                story.append(
                    Paragraph(
                        f"<b>Message:</b> {issue.message}",
                        styles["BodyText"]
                    )
                )

                story.append(
                    Paragraph(
                        f"<b>File:</b> {issue.file_path}",
                        styles["BodyText"]
                    )
                )

                story.append(
                    Paragraph(
                        f"<b>Line:</b> {issue.line_number}",
                        styles["BodyText"]
                    )
                )

                story.append(Spacer(1, 12))

        # =====================================
        # FOOTER
        # =====================================

        story.append(Spacer(1, 20))

        story.append(
            Paragraph(
                f"Generated on {datetime.now()}",
                styles["Italic"]
            )
        )

        doc.build(story)

        return filepath