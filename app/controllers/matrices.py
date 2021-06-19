from flask import Blueprint
from flask import jsonify

import numpy as np
import json 

from app.services.authService import auth_required

from app.model.vectorsModel import VectorsDTO
from app.model.utils import map_json_to_class

matrices = Blueprint('matrices',  __name__)

@matrices.route('/protected/matrices', methods=['GET'])
@auth_required()
def get():
    return "welcome to matrices API"

@matrices.route('/protected/matrices:sum', methods=['POST'])
@auth_required()
@map_json_to_class(VectorsDTO)
def sum(dto): 
    m1 = dto.getM1Matrix()
    m2 = dto.getM2Matrix()
    response = json.dumps(np.add(m1,m2).tolist())
    return jsonify(code=200, value=response), 200
