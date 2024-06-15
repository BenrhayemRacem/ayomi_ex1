import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.init_config()
        return cls._instance

    def init_config(self):
        self.DATABASE_URI = os.getenv("DATABASE_URI")
