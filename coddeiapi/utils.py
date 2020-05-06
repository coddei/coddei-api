import json
from bson import ObjectId


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
