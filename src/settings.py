from pydantic import BaseSettings


class DbSettings(BaseSettings):
    db_name : str
    db_user : str
    db_password : str
    db_host : str

    class Config:
        env_file = ".env"