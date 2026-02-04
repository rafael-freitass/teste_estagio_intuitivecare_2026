import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_NAME: str = os.getenv("DB_NAME")

    DATABASE_URL: str = os.getenv("DATABASE_URL")

    @classmethod
    def get_database_url(cls):

        if cls.DATABASE_URL:
            return cls.DATABASE_URL

        return (
            f"postgresql://{cls.DB_USER}:"
            f"{cls.DB_PASSWORD}@"
            f"{cls.DB_HOST}:{cls.DB_PORT}/"
            f"{cls.DB_NAME}"
        )


settings = Settings()