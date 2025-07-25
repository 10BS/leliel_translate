from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    bot_token: SecretStr
    gemini_api_key: SecretStr

    model_config = SettingsConfigDict(env_file=".env_", env_file_encoding="utf-8")


config = Settings()
