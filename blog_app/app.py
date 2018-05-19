from blog_app.models.blog import Blog
from blog_app.configurations.blog_config import BlogConfig
import pprint as pp


def main():
    uri = 'mongodb://127.0.0.1:27017'
    db_name = 'blog_db'
    collection_name = 'blog_posts'

    blog_config = BlogConfig(uri=uri, db_name=db_name, collection_name=collection_name)
    blog = Blog(blog_config=blog_config, title='Frivolous logs', author='Enigma')
    blog.create_post()
    results = blog.get_posts()
    print('Current blog posts:')
    pp.pprint([result.get_dict() for result in results])


if __name__ == '__main__':
    main()
