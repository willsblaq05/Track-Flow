from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[3]
ENV_FILE = BASE_DIR / ".env"

class Settings(BaseSettings):
    app_name: str = "TrackFlow API"
    api_v1_prefix: str = "/api/v1"
    database_url: str
    secret_key: str
    jwt_algorithm: str
    access_token_expire_minutes: int
    frontend_origin: str = "http://localhost:5173"
    model_config = SettingsConfigDict(
        env_file=str(ENV_FILE),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def cors_origins(self) -> list[str]:
        return [origin.strip() for origin in self.frontend_origin.split(",") if origin.strip()]
   

settings = Settings()   