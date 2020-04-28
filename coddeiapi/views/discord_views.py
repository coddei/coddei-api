from pyramid.view import view_config
import copy
import re

@view_config(route_name='get_member', renderer='json')
def get_member(request):
    return {'member': 'a'}


@view_config(route_name='members', renderer='json', request_method="POST")
def add_member(request):
    db = request.db
    data = request.json_body

    language_roles = [
        {
            'category_id': x['categoryID'],
            'role_id': x['id']
        }
    for x in data['languages']]

    english_role = {
        'category_id': data['english']['categoryID'],
        'role_id': data['english']['id']
    }

    roles = [english_role] + language_roles

    discord_data = data.get('user', {})
    discord_data.pop('avatar', None)
    discord_data.pop('lastMessageChannelID', None)
    discord_data.pop('createdTimestamp', None)
    discord_data.pop('defaultAvatarURL', None)

    discord_data['roles'] = roles

    username = data['nick']
    if len(username.split()) > 1:
        '_'.join(username.split())

    url_regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    portfolio_url = re.findall(url_regex, data['portfolio'])
    github_url = re.findall(url_regex, data['github'])

    insert_dict = {
        'name': data['name'].title(),
        'username': username,
        'description': data['bio'],
        'portfolio_url': portfolio_url[0] if portfolio_url else None,
        'github_url': github_url[0] if github_url else None,
        'discord': discord_data
    }

    user = db.users.insert_one(copy.deepcopy(insert_dict))

    if user.inserted_id:
        return {'success': True, 'user': insert_dict}

    return {'success': False}
