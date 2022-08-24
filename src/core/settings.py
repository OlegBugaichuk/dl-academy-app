from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'DL academy app'
    database_url: str
    secret_key: str
    hash_algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = '.env'


settings = Settings() 