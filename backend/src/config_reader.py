import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Config(BaseSettings):
    BOT_TOKEN: SecretStr
    DB_URL: SecretStr

    WEBHOOK_URL: str = "https://409284db5424.ngrok.app/"
    WEBAPP_URL: str = " http://localhost:5173/"

    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",
        env_file=os.path.join(os.path.dirname(__file__), ".env")
    )

config = Config()