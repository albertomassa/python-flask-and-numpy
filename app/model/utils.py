
from functools import wraps

from flask import request

def map_json_to_class(class_):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            obj = class_(**request.get_json())
            return fn(obj)
        return decorator
    return wrapper