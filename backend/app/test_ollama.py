from app.services.llm_service import LLMService

print("STEP 1: Creating LLM Service")

llm = LLMService()

print("STEP 2: LLM Service Created")

chunk = {
    "filename": "auth.py",
    "language": "python",
    "code": """
password = ""

def login(user_pass):
    if user_pass == password:
        print("Login success")
"""
}

print("STEP 3: Calling AI")

result = llm.analyze_chunk(chunk)

print("STEP 4: AI Result")
print(result)