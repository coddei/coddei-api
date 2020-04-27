def includeme(config):
    config.add_route('members', '/members')
    config.add_route('get_member', '/members/{member_id}')