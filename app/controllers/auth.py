from flask import Blueprint

from flask import request
from flask import jsonify

from flask_jwt_extended import create_access_token

from app.services.authService import auth_required
from app.services.authService import user_login

from app.model.authModel import LoginDTO
from app.model.utils import map_json_to_class

auth = Blueprint('auth',  __name__)

@auth.route("/auth/login", methods=["POST"])
@map_json_to_class(LoginDTO)
def login(dto):
    if(user_login(dto)):
        access_token = create_access_token(
            "user", additional_claims={"is_authenticated": True}
        )
        return jsonify(code=200, access_token=access_token), 200
    return jsonify(code=401, message="Wrong credentials!"), 401

@auth.route("/protected/foo", methods=["GET"])
@auth_required()
def protected():
    return jsonify(code=200, message="welcome to protected API"), 200