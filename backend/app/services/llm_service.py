import json
import re

from langchain_ollama import ChatOllama
from app.config.settings import settings
from app.services.prompt_service import PromptService


class LLMService:

    def __init__(self):

        print("Initializing LLM...")

        self.model = ChatOllama(
            model=settings.OLLAMA_MODEL,
            temperature=0
        )

        self.prompt_service = PromptService()

        print("LLM Initialized Successfully")

    def analyze_chunk(self, chunk):

        # -----------------------------
        # PROMPT BUILD SAFETY
        # -----------------------------
        prompt = self.prompt_service.build_review_prompt(chunk)

        # 🔥 FIX: ensure prompt is always string
        if isinstance(prompt, dict):
            prompt = json.dumps(prompt)
        else:
            prompt = str(prompt)

        print("\n===== PROMPT SENT TO MODEL =====")
        print(prompt)
        print("================================\n")

        # -----------------------------
        # MODEL CALL
        # -----------------------------
        response = self.model.invoke(prompt)
        content = response.content

        print("\n===== RAW MODEL OUTPUT =====")
        print(content)
        print("===========================\n")

        # -----------------------------
        # CLEAN OUTPUT
        # -----------------------------
        cleaned = content.strip()

        cleaned = re.sub(r"```json", "", cleaned)
        cleaned = re.sub(r"```", "", cleaned)

        # extract JSON safely
        match = re.search(r"\{[\s\S]*\}", cleaned)

        if not match:
            print("No JSON found in response")
            return self._empty_response()

        json_str = match.group(0)

        try:
            result = json.loads(json_str)

            return {
                "bugs": result.get("bugs", []),
                "security": result.get("security", []),
                "performance": result.get("performance", []),
                "style": result.get("style", [])
            }

        except Exception as e:
            print("JSON Parse Error:", e)
            print("Cleaned Output:", cleaned)
            return self._empty_response()

    def _empty_response(self):

        return {
            "bugs": [],
            "security": [],
            "performance": [],
            "style": []
        }