class BlogConfig(object):

    def __init__(self, uri: str, db_name: str, collection_name: str) -> None:
        self.uri = uri
        self.db_name = db_name
        self.collection_name = collection_name
