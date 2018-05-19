import pymongo
from blog_app.models import post


class DBSettings:
    uri = "mongodb://127.0.0.1:27017"


def show_results(results):
    print('Results:')
    for result in results:
        print(result)


def main():
    client = pymongo.MongoClient(DBSettings.uri)
    database = client['testapp']
    collection = database['purchaseitems']
    results = collection.find({})
    show_results(results)
    results_list = [result['itemname'] for result in collection.find({})]
    print(results_list)


if __name__ == '__main__':
    main()
