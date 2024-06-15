from sqlalchemy import create_engine
from ..config import Config

config = Config()


class DB:
    def __init__(self):
        db_uri = str(config.DATABASE_URI)
        self.engine = create_engine(db_uri)

    def __enter__(self):
        return self.engine

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.engine
