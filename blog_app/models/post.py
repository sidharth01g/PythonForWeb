from blog_app.helpers.database import Database
from typing import Dict, List


class BlogPost(object):

    def __init__(self, post_id: int, title: str, content: str, author: str, blog_id: int) -> None:
        self.post_id = post_id
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
    p = BlogPost(post_id=1, title='Majestic maneuver', content='They pulled off a coup', author='Enigma', blog_id=223)
    print(p.get_dict())


if __name__ == '__main__':
    main()
