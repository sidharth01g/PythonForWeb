import pymongo


class Database(object):

    def __init__(self, uri: str='mongodb://127.0.0.1:27017', db_name: str=None):
        self.uri = uri
        self.db_name = db_name

        self.client = pymongo.MongoClient(self.uri)
        self.database = self.client[self.db_name]

    def insert(self, collection_name: str, data: dict):
        try:
            self.database[collection_name].insert(data)
        except Exception as error:
            print('ERROR: ', error)
            raise error
