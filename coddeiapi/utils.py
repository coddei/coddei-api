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


def uid(prefix='C'):
    _id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return '{}{}'.format(prefix.upper(), _id)
