from flask import Blueprint

vectors = Blueprint('vectors',  __name__)

@vectors.route('/vectors', methods=('GET', 'POST'))
def findAll():
    return "welcome to vectors"