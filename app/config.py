from pydantic import BaseSettings


class Settings(BaseSettings):
    # Takes the list of all env varibales that needs to be set and their data type
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"

settings = Settings()