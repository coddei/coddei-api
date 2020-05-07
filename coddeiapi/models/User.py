class User():

    @classmethod
    def handle_user(cls, user):
        user['_id'] = str(user['_id'])
        user['created_at'] = str(user['created_at'])

        if 'discord' in user:
            user['discord']['id'] = str(user['discord']['id'])
            for i, role in enumerate(user['discord'].get('roles', [])):
                user['discord']['roles'][i]['role_id'] = str(user['discord']['roles'][i]['role_id'])
                user['discord']['roles'][i]['category_id'] = str(user['discord']['roles'][i]['category_id'])

        return user
