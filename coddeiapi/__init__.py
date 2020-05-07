from pyramid.config import Configurator
from pymongo import MongoClient

from coddeiapi.models.Snowflake import Snowflake

import os


def main(global_config, **settings):

    api_version = 'v1'

    config = Configurator(
        settings=settings
    )

    mongo_url = settings['mongodburl']
    mongo_port = settings['mongodbport']

    db_name = os.environ.get('MONGODB_NAME', 'coddei')

    def get_db(request):
        return MongoClient(mongo_url, int(mongo_port))[db_name]

    config.add_request_method(get_db, 'db', reify=True)
    config.include('.routes', route_prefix='api/{}'.format(api_version))

    config.include('pyramid_services')
    config.register_service(Snowflake().generator(1, 1), name='snowflake')

    config.scan()

    return config.make_wsgi_app()
