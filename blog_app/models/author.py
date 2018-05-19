from blog_app.helpers.database import Database
from typing import Dict, List
import uuid


class Author(object):

    def __init__(self, author: str, author_id: str) -> None:
        self.author = author
        self.author_id = author_id if author_id is not None else uuid.uuid4().hex

    def get_dict(self):
        return self.__dict__

    def post_to_db(self, uri: str, db_name: str, collection_name: str) -> None:
        db = Database(uri=uri, db_name=db_name)
        db.insert(collection_name=collection_name, data=self.get_dict())

    @staticmethod
    def find_authors(uri: str, db_name: str, collection_name: str, query: Dict) -> List['Author']:
        db = Database(uri=uri, db_name=db_name)
        results = db.find(collection_name=collection_name, query=query)
        results = [Author.wrap_result(result) for result in results]
        return results

    @staticmethod
    def find_author(uri: str, db_name: str, collection_name: str, query: Dict) -> 'Author':
        db = Database(uri=uri, db_name=db_name)
        result = db.find_one(collection_name=collection_name, query=query)
        result = Author.wrap_result(result)
        return result

    @classmethod
    def wrap_result(cls, result):
        return cls(author=result['author'], author_id=result['author_id'])
