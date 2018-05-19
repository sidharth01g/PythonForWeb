from blog_app.models.author import Author
from blog_app.configurations.blog_config import BlogConfig


class Menu(object):

    def __init__(self, blog_config: BlogConfig) -> None:
        self.blog_config = blog_config
        self.author = input('Author: ')
        results = Author.find_authors(uri=self.blog_config.uri, db_name=self.blog_config.db_name,
                                      collection_name=self.blog_config.collection_name_authors,
                                      query={"author": self.author})
        print(results)
