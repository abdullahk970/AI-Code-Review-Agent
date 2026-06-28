import json
from app.services.llm_service import LLMService


class StyleAgent:
    """
    AI Agent responsible ONLY for code style and readability analysis.
    """

    def __init__(self):
        self.llm = LLMService()

    def review(self, diff: str):
        """
        Analyze Git diff for code style issues only.
        Uses the standard LLM analysis flow with style-specific prompting.
        """

        # Use standard analysis flow with style context
        # The LLM service will handle prompt building
        result = self.llm.analyze_chunk({
            "filename": "style_review.py",
            "code": diff,
            "context": "style"  # Optional: helps guide the analysis
        })

        print("\n[STYLE AGENT RAW OUTPUT]")
        print(result)

        if isinstance(result, str):
            try:
                result = json.loads(result)
            except:
                return {"style": []}

        if not isinstance(result, dict):
            return {"style": []}

        return {
            "style": result.get("style", [])
        }