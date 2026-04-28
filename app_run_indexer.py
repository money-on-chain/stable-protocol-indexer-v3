import os
import json

from indexer.tasks import StableIndexerTasks


def options_from_config(filename=None):
    """ Options from file config.json """

    if not filename:
        filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.json')

    with open(filename) as f:
        options = json.load(f)

    return options


if __name__ == '__main__':

    config = options_from_config()

    # override config default
    if 'APP_CONFIG' in os.environ:
        try:
            config = json.loads(os.environ['APP_CONFIG'])
        except json.JSONDecodeError as e:
            raise ValueError("APP_CONFIG contains invalid JSON: {}".format(e))

    # override mongo uri from env
    if 'APP_MONGO_URI' in os.environ:
        mongo_uri = os.environ.pop('APP_MONGO_URI')
        if '@' not in mongo_uri:
            raise ValueError(
                "APP_MONGO_URI must include credentials (mongodb://user:pass@host/db)."
            )
        config['mongo']['uri'] = mongo_uri

    # override mongo db from env
    if 'APP_MONGO_DB' in os.environ:
        config['mongo']['db'] = os.environ['APP_MONGO_DB']

    # override connection uri from env
    if 'APP_CONNECTION_URI' in os.environ:
        config['uri'] = os.environ['APP_CONNECTION_URI']

    if config.get('mongo', {}).get('uri') == 'SET_VIA_APP_MONGO_URI_ENV':
        raise RuntimeError(
            "MongoDB URI is not configured. Set the APP_MONGO_URI environment variable."
        )

    indexer_tasks = StableIndexerTasks(config)
    indexer_tasks.start_loop()
