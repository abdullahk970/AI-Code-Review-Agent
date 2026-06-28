from pydantic import BaseModel


class DiffChunk(BaseModel):

    filename: str

    language: str

    chunk_number: int

    total_chunks: int

    code: str