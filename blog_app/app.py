from blog_app.models.post import BlogPost


def main():
    # db = Database(uri='mongodb://127.0.0.0:27017', db='blog_db')
    uri = 'mongodb://127.0.0.1:27017'
    db = 'blog_db'
    collection = 'blog_posts'
    post1 = BlogPost(
        post_id=1, title='Libelous claim', content='Slander is the word', author='Enigma', blog_id=223)
    post1.post_to_db(uri=uri, db_name=db, collection_name=collection)
    post2 = BlogPost(
        post_id=2, title='Majestic maneuver', content='They pulled off a coup', author='Enigma', blog_id=223)
    post2.post_to_db(uri=uri, db_name=db, collection_name=collection)



if __name__ == '__main__':
    main()
