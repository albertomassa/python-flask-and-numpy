
from functools import wraps

from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt

def auth_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["is_authenticated"]:
                return fn(*args, **kwargs)
            else:
                return jsonify(code=403, message="only protected users"), 403
        return decorator
    return wrapper

#change this
def user_login(loginRequest): 
    if(loginRequest.username == 'user' and loginRequest.password == 'password'):
        return True
    return False