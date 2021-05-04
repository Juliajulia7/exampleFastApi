from pydantic import BaseSettings

class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port:int = 8080
    database_url: str = 'sqlite:///.datebase.sqlite3'

settings = Settings()