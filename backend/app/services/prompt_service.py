class PromptService:

    def build_review_prompt(self, chunk):

        return f"""
You are an expert Senior Code Reviewer and Security Engineer.

YOU MUST DETECT ISSUES.

Even if code is small, ALWAYS analyze it deeply.

If you see:
- hardcoded password
- insecure login
- missing validation
- bad practices

YOU MUST REPORT THEM.

DO NOT return empty arrays if issues exist.

Return ONLY valid JSON:

{{
  "bugs": [],
  "security": [],
  "performance": [],
  "style": []
}}

CODE TO ANALYZE:

File: {chunk.get('filename', '')}
Language: {chunk.get('language', 'python')}

CODE:
{chunk.get('code', '')}
"""