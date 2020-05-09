def includeme(config):
    config.add_route('members', '/members')
    config.add_route('member', '/members/{member_id}')
