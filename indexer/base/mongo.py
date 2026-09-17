import pymongo
import logging


__all__ = ["mongo_manager"]


log = logging.getLogger()


class MongoManager:

    def __init__(self, uri='mongodb://localhost:27017/', db='db_example'):

        self.uri = uri
        self.db = db

    def set_connection(self, uri='mongodb://localhost:27017/', db='db_example'):

        self.uri = uri
        self.db = db

    def connect(self):

        uri = self.uri
        client = pymongo.MongoClient(uri)

        return client

    def get_collection(self, client, collection_name):
        mongo_db = self.db
        db = client[mongo_db]
        collection = db[collection_name]

        return collection

    def create_index(self, client, collection_name, index_map, unique=False, collation=None):
        # index_map: [("field_to_index", ASCENDING)]

        collection = self.get_collection(client, collection_name)
        create = True
        for index in index_map:
            if index[0] in collection.index_information():
                create = False
                break

        if create:
            kwargs = dict(unique=unique)
            if collation:
                kwargs["collation"] = collation
            try:
                collection.create_index(index_map, **kwargs)
            except pymongo.errors.OperationFailure as exc:
                # code 85 IndexOptionsConflict / 86 IndexKeySpecsConflict: an index on
                # the same key(s) already exists with different options (e.g. a prior
                # index created without this collation). Creating an index is setup,
                # not a request that should be able to take the whole service down;
                # log it and move on so one stale/conflicting index doesn't block
                # every other collection's indexing and the rest of startup.
                if exc.code in (85, 86):
                    log.error(
                        "Index on {0}.{1} conflicts with an existing index (code {2}): {3}. "
                        "Skipping - drop the conflicting index manually if you want this "
                        "definition applied.".format(collection_name, index_map, exc.code, exc)
                    )
                else:
                    raise
        else:
            log.error("Cannot create index already exist collection indexing!")


mongo_manager = MongoManager()
