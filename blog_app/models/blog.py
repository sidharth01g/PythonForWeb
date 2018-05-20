import datetime
from typing import Union, Optional, List
from blog_app.configurations.blog_config import BlogConfig
from blog_app.models.post import BlogPost
import hashlib
from blog_app.helpers.database import Database


class Blog(object):

    def __init__(self, blog_config: BlogConfig, title: str, author: str,
                 creation_date: Union[datetime.datetime, str, None] = None, blog_id: Optional[str] = None):

        self.blog_config = blog_config
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

        query = {"blog_id": self.blog_id}
        results = Blog.find_blogs(blog_config=self.blog_config, query=query)
        if len(results) == 0:
            print("Creating new blog titled '{}'".format(self.title))
            self._create_blog()
        else:
            print('This blog exists already')

    def _create_blog(self):
        db = Database(uri=self.blog_config.uri, db_name=self.blog_config.db_name)
        db.insert(collection_name=self.blog_config.collection_name_blogs, data=self.__dict__())

    @staticmethod
    def find_blogs(blog_config: BlogConfig, query: dict):
        db = Database(uri=blog_config.uri, db_name=blog_config.db_name)
        results = db.find(collection_name=blog_config.collection_name_blogs, query=query)
        results = [Blog.wrap_result(result) for result in results]
        return results

    @staticmethod
    def find_blog(blog_config: BlogConfig, query: dict):
        db = Database(uri=blog_config.uri, db_name=blog_config.db_name)
        result = db.find_one(collection_name=blog_config.collection_name_blogs, query=query)
        result = Blog.wrap_result(result)
        return result

    @classmethod
    def wrap_result(cls, result):
        return cls(blog_config=result['blog_config'], title=result['title'], author=result['author'],
                   blog_id=result["blog_id"], creation_date=result['creation_date'])

    def create_post(self):

        title = input('Post title: ')
        content = input('Post content: ')

        blog_post = BlogPost(title=title, content=content, author=self.author, blog_id=self.blog_id)
        blog_post.post_to_db(uri=self.blog_config.uri, db_name=self.blog_config.db_name,
                             collection_name=self.blog_config.collection_name_posts)

    def get_posts(self) -> List[BlogPost]:
        results = BlogPost.find_posts(uri=self.blog_config.uri, db_name=self.blog_config.db_name,
                                      collection_name=self.blog_config.collection_name_posts,
                                      query={'blog_id': self.blog_id})
        return results
