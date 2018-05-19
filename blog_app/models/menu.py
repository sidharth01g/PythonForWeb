from blog_app.models.author import Author
from blog_app.configurations.blog_config import BlogConfig


class Menu(object):

    def __init__(self, blog_config: BlogConfig) -> None:
        self.blog_config = blog_config
        self.authorname = input('Author: ')

        if self._has_account():  # Existing author
            print('Welcome back, {authorname}!'.format(authorname=self.authorname))
        else:  # New author
            a = Author(self.authorname)
            a.post_to_db(uri=self.blog_config.uri, db_name=self.blog_config.db_name,
                         collection_name=self.blog_config.collection_name_authors)
            print('Hello, {authorname}, great to see you here!'.format(authorname=self.authorname))

    def _has_account(self):
        results = Author.find_authors(uri=self.blog_config.uri, db_name=self.blog_config.db_name,
                                      collection_name=self.blog_config.collection_name_authors,
                                      query={"author": self.authorname})
        return len(results) > 0
