def includeme(config):
    config.include('coddeiapi.views.main_routes')
    config.include('coddeiapi.views.discord_routes', route_prefix='discord')
