from app.services.diff_mapper_service import DiffMapperService


mapper = DiffMapperService()

file = {
    "filename": "auth.py",

    "patch": """
@@ -1,2 +1,4 @@
+password="1234"
+print(password)
"""
}

result = mapper.map_issue(file, "password vulnerability")

print(result)