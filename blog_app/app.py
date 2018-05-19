from blog_app.models.post import BlogPost



def main():
    uri = 'mongodb://127.0.0.1:27017'
    db_name = 'blog_db'
    collection_name = 'blog_posts'
    post1 = BlogPost(title='Libelous claim', content='Slander is the word', author='Enigma', blog_id=223)
    post1.post_to_db(uri=uri, db_name=db_name, collection_name=collection_name)
    post2 = BlogPost(title='Majestic maneuver', content='They pulled off a coup', author='Enigma', blog_id=223)
    post2.post_to_db(uri=uri, db_name=db_name, collection_name=collection_name)

    results = [result for result in
               BlogPost.find_posts(uri=uri, db_name=db_name, collection_name=collection_name, query={})]
    print('Query results: ', results)

    result = BlogPost.find_post(uri=uri, db_name=db_name, collection_name=collection_name, query={})
    print('Query result:', result)


if __name__ == '__main__':
    main()
