from blog_app.configurations.blog_config import BlogConfig
from blog_app.models.menu import Menu


def main() -> None:
    uri = 'mongodb://127.0.0.1:27017'
    db_name = 'blog_db'
    collection_name_posts = 'blog_posts'
    collection_name_authors = 'blog_authors'
    collection_name_blogs = 'blog_blogs'

    blog_config = BlogConfig(uri=uri, db_name=db_name, collection_name_posts=collection_name_posts,
                             collection_name_authors=collection_name_authors,
                             collection_name_blogs=collection_name_blogs)

    menu = Menu(blog_config=blog_config)
    menu.run_menu()


if __name__ == '__main__':
    main()
