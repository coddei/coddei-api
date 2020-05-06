import json
from bson import ObjectId

import random
import string


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


def dump(data):
    try:
        return JSONEncoder().encode(data)
    except Exception as e:
        print('Error on dump', e)
        return False


def uid(prefix='C', colletion=None):

    _id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    uid = '{}{}'.format(prefix.upper(), _id)

    if colletion:
        while colletion.find_one({'id': uid}):
            _id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            uid = '{}{}'.format(prefix.upper(), _id)

    return uid
