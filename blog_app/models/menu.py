from blog_app.models.author import Author
from blog_app.configurations.blog_config import BlogConfig
from blog_app.models.blog import Blog
import pprint as pp


class Menu(object):

    def __init__(self, blog_config: BlogConfig) -> None:
        self.blog_config = blog_config
        self.authorname = input('Author: ')

        if self._has_account():  # Existing author
            print('Welcome back, {authorname}!'.format(authorname=self.authorname))

        else:  # New author signup
            a = Author(self.authorname)
            a.post_to_db(uri=self.blog_config.uri, db_name=self.blog_config.db_name,
                         collection_name=self.blog_config.collection_name_authors)
            print('Hello, {authorname}, great to see you here!'.format(authorname=self.authorname))

    def _has_account(self) -> bool:
        results = Author.find_authors(uri=self.blog_config.uri, db_name=self.blog_config.db_name,
                                      collection_name=self.blog_config.collection_name_authors,
                                      query={"author": self.authorname})
        return len(results) > 0

    def run_menu(self) -> None:
        print('Existing blogs:')
        self._list_blogs()

        print('\n')
        self._write_or_read()
        pass

    def _write_or_read(self) -> None:

        choice = input('Would you like to write(W) or read(R) blogs?: ')
        choice = choice.lower()

        if choice in ['write', 'w']:
            self._write_blog()
            pass
        elif choice in ['read', 'r']:
            self._read_blogs()
            pass

    def _write_blog(self) -> None:
        blog_title = input('Blog title: ')
        blog = Blog(title=blog_title, author=self.authorname)
        blog.create_post(blog_config=self.blog_config)

    def _list_blogs(self) -> None:
        results = Blog.find_blogs(blog_config=self.blog_config, query={})
        pp.pprint([result.__dict__ for result in results])

    def _read_blogs(self) -> None:
        blog_id = input('ID  of the blog to view: ')
        blog = Blog.find_blog(blog_config=self.blog_config, query={'blog_id': blog_id})
        if not blog:
            print('No blogs found for this ID')
        else:
            posts = blog.get_posts(blog_config=self.blog_config)
            output_list = [post.__dict__ for post in posts]
            print('Showing posts for blog id {}'.format(blog_id))
            pp.pprint(output_list)
