from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="forbid",
    )

    api_key: str
    database_url: str = Field(alias="DATABASE_URL")

settings = Settings()
