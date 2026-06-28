import json
from app.services.llm_service import LLMService


class BugAgent:

    def __init__(self):
        self.llm = LLMService()

    def review(self, diff: str):

        result = self.llm.analyze_chunk({
            "filename": "test_diff.py",
            "code": diff
        })

        print("\n[BUG RAW OUTPUT]")
        print(result)

        if isinstance(result, str):
            try:
                result = json.loads(result)
            except:
                return {"bugs": []}

        if not isinstance(result, dict):
            return {"bugs": []}

        return {
            "bugs": result.get("bugs", [])
        }