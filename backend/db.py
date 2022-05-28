from pydantic import BaseModel
import pymongo
from pymongo.database import Database

from config import Config

config = Config()


# @contextlib.contextmanager
def get_db():
    try:
        client = pymongo.MongoClient(config.MONGO_DB)
        db = client.__getattr__(config.MONGO_DB_NAME)
        yield db
    finally:
        if client:
            client.close()


class Base(BaseModel):
    async def save(self, db: Database) -> str:
        """Save model to DB and modify itself

        Args:
            db (Database): connection to DB

        Returns:
            str: id of created entity
        """
        collection = getattr(db, self.__collectionname__)
        if not hasattr(self, "__notsave__"):
            self.__notsave__ = []
        id = str(collection.insert_one(self.dict(exclude_unset=True, exclude=self.__notsave__)))
        self.id = id
        return id
