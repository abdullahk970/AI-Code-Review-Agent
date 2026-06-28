import json
from app.services.llm_service import LLMService


class PerformanceAgent:
    """
    AI Agent responsible ONLY for performance optimization analysis.
    """

    def __init__(self):
        self.llm = LLMService()

    def review(self, diff: str):
        """
        Analyze Git diff for performance issues only.
        Uses the standard LLM analysis flow with performance-specific prompting.
        """

        # Use standard analysis flow with performance context
        # The LLM service will handle prompt building
        result = self.llm.analyze_chunk({
            "filename": "performance_review.py",
            "code": diff,
            "context": "performance"  # Optional: helps guide the analysis
        })

        print("\n[PERFORMANCE AGENT RAW OUTPUT]")
        print(result)

        if isinstance(result, str):
            try:
                result = json.loads(result)
            except:
                return {"performance": []}

        if not isinstance(result, dict):
            return {"performance": []}

        return {
            "performance": result.get("performance", [])
        }