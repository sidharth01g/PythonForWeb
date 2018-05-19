from blog_app.models.post import BlogPost
from blog_app.models.blog import Blog
from blog_app.configurations.blog_config import BlogConfig


def main():
    uri = 'mongodb://127.0.0.1:27017'
    db_name = 'blog_db'
    collection_name = 'blog_posts'

    blog_config = BlogConfig(uri=uri, db_name=db_name, collection_name=collection_name)
    blog = Blog(blog_config=blog_config, title='Frivolous logs', author='Enigma')
    blog.create_post()


    results = [result for result in
               BlogPost.find_posts(uri=uri, db_name=db_name, collection_name=collection_name, query={})]
    print('Query results: ', results)

    result = BlogPost.find_post(uri=uri, db_name=db_name, collection_name=collection_name, query={})
    print('Query result:', result)


if __name__ == '__main__':
    main()
