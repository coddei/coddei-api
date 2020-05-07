from pyramid.view import view_config
from coddeiapi.models.Recommendation import Recommendation
import copy
import re
import datetime


@view_config(route_name='recommendations', renderer='json', request_method="POST")
def add_recommendation(request):
    db = request.db

    if not request.body:
        return {'success': False}

    data = request.json_body
    snowflake = request.find_service(name='snowflake')

    url_regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    url = re.findall(url_regex, data['url'])

    if not url:
        return {'success': False}

    user = db.users.find_one({'discord.id': int(data['author']['id'])})

    if not user:
        return {'success': False}

    insert_dict = {
        '_id': next(snowflake),
        'author_id': user['_id'],
        'title': data['title'],
        'url': url[0],
        'description': data['description'],
        'created_at': datetime.datetime.now()
    }

    recommendation = db.recommendations.insert_one(copy.deepcopy(insert_dict))

    if recommendation.inserted_id:
        insert_dict['author'] = {'username': user.get('username')}
        insert_dict.pop('author_id', None)

        return {'success': True, 'recommendation': Recommendation.handle_recommendation(insert_dict)}

    return {'success': False}


# Just returning all for now, make pagination later
@view_config(route_name='recommendations', renderer='json', request_method="GET")
def get_recommendations(request):
    db = request.db

    recommendations = list(db.recommendations.find({}))
    recommendations = [Recommendation.handle_recommendation(x) for x in recommendations]

    return {'success': True, 'recommendations': recommendations}
