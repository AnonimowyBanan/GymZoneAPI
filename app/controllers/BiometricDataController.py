from flask                          import jsonify, request, make_response
from .                              import biometric_data
from app.db.BiometricDataCollection import BiometricDataCollection

@biometric_data.route('/get-all', methods=['GET'])
def get_all_biometric_datas():
    
    result = []

    biometric_datas = BiometricDataCollection.all()

    if result is None:
        return make_response({'error': 'biometric datas not found'}, 204)
    
    for biometric_data in biometric_datas:
        result.append(put_biometric_datas_to_json(biometric_data))
    
    return make_response(jsonify(result), 200)

# @biometric_data.route('/get', methods=['GET'])
# @biometric_data.route('/delete', methods=['DELETE'])
# @biometric_data.route('/edit', methods=['PUT', 'POST'])
# @biometric_data.route('/add', methods=['POST'])

def put_biometric_datas_to_json(data):

    result = {
        'id'        : data.id,
        'id_user'   : data.id_user,
        'age'       : data.age,
        'height'    : data.height,
        'weight'    : data.weight,
        'BMI'       : data.BMI,
        'BMR'       : data.BMR,
        'PBF'       : data.PBF,
        'FFM'       : data.FFM,
        'fit_score' : data.fit_score,
        'timestamp' : data.timestamp
    }

    return result


