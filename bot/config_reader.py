from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    bot_token: SecretStr
    llm_base_url: str
    llm_api_key: SecretStr
    llm_model: str
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


config = Settings()
