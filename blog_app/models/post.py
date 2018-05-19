from blog_app.helpers.database import Database
from typing import Optional, Dict, List
import uuid


class BlogPost(object):

    def __init__(self, title: str, content: str, author: str, blog_id: int, post_id: Optional[int]=None) -> None:
        self.post_id = post_id if post_id is not None else uuid.uuid4().hex
        self.title = title
        self.content = content
        self.author = author
        self.blog_id = blog_id
        pass

    def get_dict(self):
        return self.__dict__

    def post_to_db(self, uri: str, db_name: str, collection_name: str) -> None:
        db = Database(uri=uri, db_name=db_name)
        db.insert(collection_name=collection_name, data=self.get_dict())

    @staticmethod
    def find_posts(uri: str, db_name: str, collection_name: str, query: Dict) -> List[Dict]:
        db = Database(uri=uri, db_name=db_name)
        results = db.find(collection_name=collection_name, query=query)
        return results

    @staticmethod
    def find_post(uri: str, db_name: str, collection_name: str, query: Dict) -> Dict:
        db = Database(uri=uri, db_name=db_name)
        result = db.find_one(collection_name=collection_name, query=query)
        return result


def main():
    p = BlogPost(title='Majestic maneuver', content='They pulled off a coup', author='Enigma', blog_id=223, post_id=1)
    print(p.get_dict())


if __name__ == '__main__':
    main()
