from app.services.diff_service import DiffService
from app.services.llm_service import LLMService

print("STEP 1: Script started")

diff = DiffService()
print("STEP 2: DiffService created")

llm = LLMService()
print("STEP 3: LLMService created")

files = [
    {
        "filename": "auth.py",
        "language": "python",
        "code": """
password = ""

def login(user_pass):
    if user_pass == password:
        print("Login success")
"""
    }
]

print("STEP 4: Files prepared")

chunks = diff.build_ai_input(files)

print("STEP 5: Chunks generated")
print("Chunks =", chunks)
print("Count =", len(chunks))

for chunk in chunks:
    print("STEP 6: Analyzing chunk")
    result = llm.analyze_chunk(chunk)
    print("STEP 7: Result received")
    print(result)

print("STEP 8: Script finished")