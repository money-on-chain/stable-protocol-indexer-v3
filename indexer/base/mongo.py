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

        # Match by key pattern, not name: index_information() keys are index NAMES
        # (e.g. "recipient_ci" or the auto-generated "params.recipient_1"), which
        # never equal a bare field name, so a name-string check never detects an
        # existing index and every restart re-attempts creation. Mongo itself then
        # rejects that as IndexOptionsConflict (code 85) whenever the existing index
        # happens to carry a different (often hand-picked) name than the one we'd
        # auto-generate, even though the key spec is identical - which is exactly
        # what was crashing startup here.
        target_key = list(index_map)
        create = not any(
            info.get("key") == target_key for info in collection.index_information().values()
        )

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
            log.info("Index on {0}.{1} already exists, skipping.".format(collection_name, target_key))


mongo_manager = MongoManager()
