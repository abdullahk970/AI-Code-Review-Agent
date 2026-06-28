class DiffService:


    def detect_language(

        self,

        filename

    ):

        extension = filename.split(".")[-1]


        mapping = {

            "py": "python",

            "js": "javascript",

            "ts": "typescript",

            "tsx": "typescript",

            "jsx": "javascript",

            "java": "java",

            "cpp": "cpp",

            "c": "c",

            "go": "go",

            "rs": "rust"

        }


        return mapping.get(

            extension,

            "text"

        )


    def extract_valid_files(

        self,

        files

    ):

        valid = []


        for file in files:


            if "patch" not in file:

                continue


            valid.append(

                {

                    "filename":

                    file["filename"],


                    "patch":

                    file["patch"],


                    "language":

                    self.detect_language(

                        file["filename"]

                    )

                }

            )


        return valid


    def chunk_code(

        self,

        code,

        size=1200

    ):

        chunks = []


        for i in range(

            0,

            len(code),

            size

        ):


            chunks.append(

                code[i:i+size]

            )


        return chunks


    def prepare_chunks(

        self,

        files

    ):

        output = []


        for file in files:


            chunks = self.chunk_code(

                file["patch"]

            )


            total = len(chunks)


            for index, chunk in enumerate(chunks):


                output.append(

                    {

                        "filename":

                        file["filename"],


                        "language":

                        file["language"],


                        "chunk_number":

                        index+1,


                        "total_chunks":

                        total,


                        "code":

                        chunk

                    }

                )


        return output


    def build_ai_input(

        self,

        files

    ):

        valid_files = self.extract_valid_files(

            files

        )


        chunks = self.prepare_chunks(

            valid_files

        )


        return chunks