def includeme(config):
    config.include('coddeiapi.routes.main_routes')
    config.include('coddeiapi.routes.discord_routes', route_prefix='discord')
