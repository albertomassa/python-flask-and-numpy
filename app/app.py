#! ../env/bin/python

from flask import Flask

from app.controllers.vector import vectors

def create_app(env="dev"):

    app = Flask(__name__, static_url_path='')

    app.config['ENV'] = env

    # register our blueprints
    app.register_blueprint(vectors)

    return app
