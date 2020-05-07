import json
from bson import ObjectId

from coddeiapi.models.Snowflake import Snowflake


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


def snowflake_to_timestamp(_id):
    s = Snowflake()

    _id = _id >> 22   # strip the lower 22 bits
    _id += s.cepoch   # adjust for coddei epoch
    _id = _id / 1000  # convert from milliseconds to seconds
    return _id
