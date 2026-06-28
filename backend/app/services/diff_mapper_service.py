import re


class DiffMapperService:

    def extract_added_lines(self, patch):

        lines = []
        current_line = 0

        for row in patch.splitlines():

            if row.startswith("@@"):

                match = re.search(r"\+(\d+)", row)

                if match:
                    current_line = int(match.group(1)) - 1

                continue

            if row.startswith("+"):

                current_line += 1

                lines.append({
                    "line": current_line,
                    "code": row[1:]
                })

            elif row.startswith("-"):
                continue

            else:
                current_line += 1

        return lines
    
    def find_line(self, patch, keyword):

        lines = self.extract_added_lines(patch)

        for row in lines:

            if keyword.lower() in row["code"].lower():
                return row["line"]

        return 1
    
    def map_issue(self, file, issue):

        patch = file.get("patch", "")
        filename = file.get("filename", "")

        keyword = issue.split()[0]

        line = self.find_line(patch, keyword)

        return {
            "path": filename,
            "line": line,
            "issue": issue
        }