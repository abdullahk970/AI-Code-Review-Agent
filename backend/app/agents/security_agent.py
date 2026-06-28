from app.services.llm_service import LLMService
import json


class SecurityAgent:

    def __init__(self):
        self.llm = LLMService()

    def review(self, diff: str):

        result = self.llm.analyze_chunk({
            "filename": "test_diff.py",
            "code": diff
        })

        print("\n[SECURITY AGENT RAW OUTPUT]")
        print(result)

        if isinstance(result, str):
            try:
                result = json.loads(result)
            except:
                return {"security": []}

        if not isinstance(result, dict):
            return {"security": []}

        return {
            "security": result.get("security", [])
        }