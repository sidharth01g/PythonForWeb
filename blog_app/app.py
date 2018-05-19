from blog_app.models.post import BlogPost
from blog_app.helpers.database import Database


def main():
    uri = 'mongodb://127.0.0.1:27017'
    db_name = 'blog_db'
    collection_name = 'blog_posts'
    post1 = BlogPost(
        post_id=1, title='Libelous claim', content='Slander is the word', author='Enigma', blog_id=223)
    post1.post_to_db(uri=uri, db_name=db_name, collection_name=collection_name)
    post2 = BlogPost(
        post_id=2, title='Majestic maneuver', content='They pulled off a coup', author='Enigma', blog_id=223)
    post2.post_to_db(uri=uri, db_name=db_name, collection_name=collection_name)

    db = Database(uri=uri, db_name=db_name)
    results = [result for result in db.find(collection_name=collection_name, query={})]
    print('Query results: ', results)

    result = db.find_one(collection_name=collection_name, query={})
    print('Query result:', result)


if __name__ == '__main__':
    main()
