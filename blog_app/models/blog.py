import datetime
from typing import Union
from blog_app.configurations.blog_config import BlogConfig
from blog_app.models.post import BlogPost


class Blog(object):

    def __init__(self, blog_config: BlogConfig, title: str, author: str,
                 creation_date: Union[datetime.datetime, str, None] = None):

        self.blog_config = blog_config
        self.title = title
        self.author = author

        if not creation_date:
            self.creation_date = datetime.datetime.utcnow()
        elif type(creation_date) is str:
            self.creation_date = datetime.datetime.strptime(creation_date, '%d%m%Y')
        elif type(creation_date) is datetime.datetime:
            self.creation_date = creation_date
        else:
            raise TypeError('Blog creation date is of invalid type or format')

    def create_post(self):

        title = input('Post title: ')
        content = input('Post content: ')
        blog_id = int(input('Blog ID: '))

        blog_post = BlogPost(title=title, content=content, author=self.author, blog_id=blog_id)
        blog_post.post_to_db(uri=self.blog_config.uri, db_name=self.blog_config.db_name,
                             collection_name=self.blog_config.collection_name)
