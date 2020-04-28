from pyramid.view import view_config

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

    user = db.recommendations.insert_one(copy.deepcopy(insert_dict))

    if user.inserted_id:
        insert_dict['author'] = {'username': user.get('username')}
        return {'success': True, 'user': insert_dict}

    return {'success': False}
