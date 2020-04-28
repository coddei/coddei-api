from pyramid.view import view_config
import copy
import re

@view_config(route_name='recommendations', renderer='json', request_method="POST")
def add_recommendation(request):
    db = request.db
    data = request.json_body

    url_regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    url = re.findall(url_regex, data['url'])

    if not url:
        return {'success': False}

    user = db.users.find_one({'discord.id': data['author']['id']})

    if not user:
        return {'success': False}

    insert_dict = {
        'author_id': user['_id'],
        'title': data['title'],
        'url': url[0],
        'description': data['description']
    }

    recommendation = db.recommendations.insert_one(copy.deepcopy(insert_dict))

    if recommendation.inserted_id:
        insert_dict['author'] = {'username': user.get('username')}
        insert_dict.pop('author_id', None)

        return {'success': True, 'recommendation': insert_dict}

    return {'success': False}
