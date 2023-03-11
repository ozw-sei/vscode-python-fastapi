from pydantic import BaseSettings, Field


class PSQLConfig(BaseSettings):
    postgres_user: str = Field(default="")
    postgres_password: str = Field(default="")
    postgres_server: str = Field(default="")
    postgres_port: str = Field(default="")
    postgres_db: str = Field(default="")

    class Config:
        case_sensitive = False

    @property
    def dsn(self):
        return f"postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_server}:{self.postgres_port}/{self.postgres_db}"
