from flask import Blueprint, jsonify
import numpy as np
import json 

from app.services.authService import auth_required

from app.model.vectorsModel import VectorsDTO
from app.model.utils import map_json_to_class

vectors = Blueprint('vectors',  __name__)

@vectors.route('/protected/vectors', methods=['GET'])
@auth_required()
def get():
    return "welcome to vectors API"

@vectors.route('/protected/vectors:sum', methods=['POST'])
@auth_required()
@map_json_to_class(VectorsDTO)
def sum(dto): 
    response = json.dumps((dto.getV1Vector()+dto.getV2Vector()).tolist())
    return jsonify(code=200, value=response), 200

@vectors.route('/protected/vectors:dotProduct', methods=['POST'])
@auth_required()
@map_json_to_class(VectorsDTO)
def dotProduct(dto): 
    response = np.dot(dto.getV1Vector(),dto.getV2Vector())
    return jsonify(code=200, value=float(response)), 200

@vectors.route('/protected/vectors:sort', methods=['POST'])
@auth_required()
@map_json_to_class(VectorsDTO)
def sort(dto): 
    v1Response = json.dumps(np.sort(dto.getV1Vector()).tolist())
    v2Response = json.dumps(np.sort(dto.getV2Vector()).tolist())
    return jsonify(code=200, v1=v1Response, v2=v2Response), 200

@vectors.route('/protected/vectors:max', methods=['POST'])
@auth_required()
@map_json_to_class(VectorsDTO)
def max(dto): 
    v1Response = float(np.max(dto.getV1Vector()))
    v2Response = float(np.max(dto.getV2Vector()))
    return jsonify(code=200, v1=v1Response, v2=v2Response), 200

@vectors.route('/protected/vectors:mean', methods=['POST'])
@auth_required()
@map_json_to_class(VectorsDTO)
def mean(dto): 
    v1Response = float(np.mean(dto.getV1Vector()))
    v2Response = float(np.mean(dto.getV2Vector()))
    return jsonify(code=200, v1=v1Response, v2=v2Response), 200