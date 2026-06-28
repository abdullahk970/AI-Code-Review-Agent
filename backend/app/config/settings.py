from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GITHUB_TOKEN: str
    GITHUB_WEBHOOK_SECRET: str
    OLLAMA_MODEL: str = ""
    DATABASE_URL: str = "sqlite:///./review.db"
    BASE_URL: str = ""
    DEBUG: bool = ""

    model_config = SettingsConfigDict(
        env_file=".env"
    )


settings = Settings()