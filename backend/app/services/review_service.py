from app.services.llm_service import LLMService


class ReviewService:


    def __init__(self):

        self.llm = LLMService()


    def analyze_security(self, chunk):

        result = self.llm.analyze_chunk(chunk)

        return result.get("security", [])


    def analyze_bugs(self, chunk):

        result = self.llm.analyze_chunk(chunk)

        return result.get("bugs", [])


    def analyze_performance(self, chunk):

        result = self.llm.analyze_chunk(chunk)

        return result.get("performance", [])


    def analyze_style(self, chunk):

        result = self.llm.analyze_chunk(chunk)

        return result.get("style", [])