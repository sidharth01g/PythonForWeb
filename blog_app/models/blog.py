import datetime
from typing import Union, Optional, List
from blog_app.configurations.blog_config import BlogConfig
from blog_app.models.post import BlogPost
import hashlib
from blog_app.helpers.database import Database


class Blog(object):

    def __init__(self, title: str, author: str, creation_date: Union[datetime.datetime, str, None] = None,
                 blog_id: Optional[str] = None):

        # self.blog_config = blog_config
        self.title = title
        self.author = author
        self.blog_id = blog_id if blog_id else hashlib.sha1((self.title + self.author).encode()).hexdigest()

        if not creation_date:
            self.creation_date = datetime.datetime.utcnow()
        elif type(creation_date) is str:
            self.creation_date = datetime.datetime.strptime(creation_date, '%d%m%Y')
        elif type(creation_date) is datetime.datetime:
            self.creation_date = creation_date
        else:
            raise TypeError('Blog creation date is of invalid type or format')

    def create_blog(self, blog_config: BlogConfig) -> None:
        query = {"blog_id": self.blog_id}
        results = Blog.find_blogs(blog_config=blog_config, query=query)
        if len(results) == 0:
            print("Creating new blog titled '{}'".format(self.title))
            db = Database(uri=blog_config.uri, db_name=blog_config.db_name)
            db.insert(collection_name=blog_config.collection_name_blogs, data=self.__dict__)
        else:
            print('This blog exists already')

    @staticmethod
    def find_blogs(blog_config: BlogConfig, query: dict) -> List['Blog']:
        db = Database(uri=blog_config.uri, db_name=blog_config.db_name)
        results = db.find(collection_name=blog_config.collection_name_blogs, query=query)
        results = [Blog.wrap_result(result) for result in results] if results else results
        return results

    @staticmethod
    def find_blog(blog_config: BlogConfig, query: dict) -> 'Blog':
        db = Database(uri=blog_config.uri, db_name=blog_config.db_name)
        result = db.find_one(collection_name=blog_config.collection_name_blogs, query=query)
        result = Blog.wrap_result(result) if result else result
        return result

    @classmethod
    def wrap_result(cls, result):
        return cls(title=result['title'], author=result['author'],
                   blog_id=result["blog_id"], creation_date=result['creation_date'])

    def create_post(self, blog_config: BlogConfig) -> None:

        title = input('Post title: ')
        content = input('Post content: ')
        self.create_blog(blog_config=blog_config)
        blog_post = BlogPost(title=title, content=content, author=self.author, blog_id=self.blog_id)
        blog_post.post_to_db(uri=blog_config.uri, db_name=blog_config.db_name,
                             collection_name=blog_config.collection_name_posts)

    def get_posts(self, blog_config: BlogConfig) -> List[BlogPost]:
        results = BlogPost.find_posts(uri=blog_config.uri, db_name=blog_config.db_name,
                                      collection_name=blog_config.collection_name_posts,
                                      query={'blog_id': self.blog_id})
        return results
