from flask                                      import jsonify, request, make_response
from .                                          import biometric_data
from app.collections.BiometricData_collection   import BiometricData_collection
from app.collections.BiometricScore_collection  import BiometricScore_collection
from app.collections.User_collection            import User_collection
from app.fun.fun_BiometricScores                import BiometricData
from app.extenctions                            import db

@biometric_data.route('/get-all', methods=['GET'])
def get_all_biometric_datas():
    
    result = []

    biometric_datas = BiometricData_collection.all()

    if result is None:
        return make_response({'error': 'biometric datas not found'}, 204)
    
    for biometric_data in biometric_datas:
        result.append(put_biometric_datas_to_json(biometric_data))
    
    return make_response(jsonify(result), 200)

@biometric_data.route('/get', methods=['GET'])
def get_biometric_data():

    biometric_data_obj = BiometricData_collection()

    biometric_data_obj.set_biometric_data_id(request.form.get('biometric_data_ID'))
    biometric_data = biometric_data_obj.get()

    if biometric_data is None:
        return make_response({'error': 'biometric data not found'}, 204)
    else:
        return make_response(put_biometric_datas_to_json(biometric_data))



# @biometric_data.route('/delete', methods=['DELETE'])
# @biometric_data.route('/edit', methods=['PUT', 'POST'])
@biometric_data.route('/add', methods=['POST'])
def add_biometric_data():

    biometric_data_obj  = BiometricData_collection()
    biometric_score_obj = BiometricScore_collection()
    user_obj            = User_collection()

    user_obj.set_user_id(request.form.get('user_ID'))
    gender = user_obj.get().gender

    age                 = request.form.get('age')
    height              = request.form.get('height')
    weight              = request.form.get('weight')

    biometric_data_obj.id_user              = request.form.get('user_ID')
    biometric_data_obj.age                  = age
    biometric_data_obj.height               = height
    biometric_data_obj.weight               = weight

    db.session.add(biometric_data_obj)
    db.session.flush()

    biometric_calc_obj = BiometricData(age, height, weight, gender)

    biometric_score_obj.id_biometric_data   = biometric_data_obj.id
    biometric_score_obj.BMI                 = biometric_calc_obj.calculate_BMI()
    biometric_score_obj.BMR                 = biometric_calc_obj.calculate_BMR()
    biometric_score_obj.PBF                 = biometric_calc_obj.calculate_PBF()
    biometric_score_obj.fit_score           = biometric_calc_obj.calculate_fit_score()

    db.session.add(biometric_score_obj)

    try:
        db.session.commit()

        return make_response({'response': 'OK', 'biometric_data': put_biometric_datas_to_json(biometric_data_obj)}, 200)
    
    except Exception as e:
        db.session.rollback()

        return make_response({'error': str(e)}, 500)

def put_biometric_datas_to_json(data):

    result = {
        'id'        : data.id,
        'id_user'   : data.id_user,
        'age'       : data.age,
        'height'    : data.height,
        'weight'    : data.weight,
        'timestamp' : data.timestamp
    }

    return result


