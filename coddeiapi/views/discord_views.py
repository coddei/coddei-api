from pyramid.view import view_config
from coddeiapi.models.User import User
import copy
import re
import datetime


@view_config(route_name='get_member', renderer='json', request_method="GET")
def get_member(request):
    db = request.db
    member_id = request.matchdict.get('member_id')

    user = db.users.find_one({'discord.id': int(member_id)})

    if not user:
        return {'success': False, 'message': 'Couldn\'t find user.'}

    return {'success': True, 'user': User.handle_user(user)}


@view_config(route_name='members', renderer='json', request_method="POST")
def add_member(request):
    db = request.db
    snowflake = request.find_service(name='snowflake')

    if not request.body:
        return {'success': False}

    data = request.json_body

    language_roles = [
        {
            'category_id': int(x['categoryID']),
            'role_id': int(x['id'])
        }
    for x in data['languages']]

    english_role = {
        'category_id': int(data['english']['categoryID']),
        'role_id': int(data['english']['id'])
    }

    roles = [english_role] + language_roles

    discord_data = data.get('user', {})
    discord_data.pop('avatar', None)
    discord_data.pop('lastMessageChannelID', None)
    discord_data.pop('createdTimestamp', None)
    discord_data.pop('defaultAvatarURL', None)

    discord_data['id'] = int(discord_data['id'])
    discord_data['roles'] = roles

    username = data['nick']
    if len(username.split()) > 1:
        username = '_'.join(username.split())

    url_regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    portfolio_url = re.findall(url_regex, data['portfolio'])
    github_url = re.findall(url_regex, data['github'])

    insert_dict = {
        '_id': next(snowflake),
        'name': data['name'].title(),
        'nickname': data['nick'],
        'username': username,
        'description': data['bio'],
        'portfolio_url': portfolio_url[0] if portfolio_url else None,
        'github_url': github_url[0] if github_url else None,
        'discord': discord_data,
        'created_at': datetime.datetime.now()
    }

    user = db.users.insert_one(copy.deepcopy(insert_dict))

    if user.inserted_id:
        return {'success': True, 'user': User.handle_user(insert_dict)}

    return {'success': False}
