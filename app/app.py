#! ../env/bin/python

from flask import Flask

from flask_jwt_extended import JWTManager

from app.controllers.auth import auth
from app.controllers.vectors import vectors
from app.controllers.matrices import matrices

def create_app():

    app = Flask(__name__, static_url_path='')

    app.testing = True
    app.debug = 1

    app.config['ENV'] = "dev"
    app.config['SECRET_KEY'] = '\xc5\xd9E\x04Bk\xb4*\x92\xb6\xc9MdZ3$w\x0c\xc3\x95\xaf\xb7U' #change this
    app.config["JWT_SECRET_KEY"] = "super-secret" #change this

    # register blueprints
    app.register_blueprint(auth)
    app.register_blueprint(vectors)
    app.register_blueprint(matrices)

    jwt = JWTManager(app)

    return app
