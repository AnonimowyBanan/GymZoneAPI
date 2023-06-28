from flask import jsonify, request, make_response
from app.extenctions import db
from app.models.biometric_data import BiometricData
from flask_jwt_extended import jwt_required
from . import biometric_data


@biometric_data.route('/get-all', methods=['GET'])
@jwt_required()
def get_all_biometric_datas():
    biometric_data_obj = BiometricData()
    biometric_datas = biometric_data_obj.all()

    if biometric_datas is None:

        return make_response({'response': 'ERROR', 'description': 'Biometric datas not found'}, 204)
    else:
        result = []
        for data in biometric_datas:
            result.append(put_biometric_datas_to_json(data))

        return make_response(jsonify(result), 200)


@biometric_data.route('/get', methods=['GET'])
@jwt_required()
def get_biometric_data():
    biometric_data_obj = BiometricData()

    biometric_data_obj.set_id(int(request.form.get('biometric_data_ID')))
    data = biometric_data_obj.get()

    if data is None:
        return make_response({'response': 'ERROR', 'description': 'Biometric data not found'}, 204)
    else:
        return make_response(put_biometric_datas_to_json(data))


@biometric_data.route('/delete', methods=['DELETE'])
@jwt_required()
def delete_biometric_data():
    biometric_data_obj = BiometricData()

    biometric_data_obj.set_id(int(request.form.get('biometric_data_ID')))
    biometric_data_to_delete = biometric_data_obj.get()

    if biometric_data_to_delete is None:

        return make_response({'response': 'ERROR', 'description': 'Biometric data not found'}, 204)
    else:
        try:
            db.session.delete(biometric_data_to_delete)
            db.session.commit()

            return make_response({'response': 'OK'}, 200)

        except Exception as e:

            return make_response({'response': 'ERROR', 'description': str(e)}, 500)


@biometric_data.route('/edit', methods=['PUT', 'POST'])
@jwt_required()
def edit_biometric_data():
    biometric_data_obj = BiometricData()
    biometric_data_obj.set_id(int(request.form.get('biometric_data_ID')))
    biometric_data = biometric_data_obj.get()

    if biometric_data is None:
        return make_response({'response': 'ERROR', 'description': 'Biometric data not found'}, 204)


    biometric_data.age = int(request.form.get('age'))
    biometric_data.height = float(request.form.get('height'))
    biometric_data.weight = float(request.form.get('weight'))

    try:
        db.session.commit()

        return make_response({'response': 'OK', 'biometric_data': put_biometric_datas_to_json(biometric_data)}, 200)
    except Exception as e:
        return make_response({'response': 'OK', 'description': f'{e}'}, 500)


@biometric_data.route('/add', methods=['POST'])
@jwt_required()
def add_biometric_data():
    biometric_data_object = BiometricData()
    user_id = request.form.get('user_ID')

    if user_id is None:
        return make_response({'response': 'ERROR', 'description': 'User not found'}, 204)

    biometric_data_object.set_id_user(int(request.form.get('user_ID')))
    biometric_data_object.set_age(int(request.form.get('age')))
    biometric_data_object.set_height(float(request.form.get('height')))
    biometric_data_object.set_weight(float(request.form.get('weight')))

    db.session.add(biometric_data_object)

    try:
        db.session.flush()
        new_biometric_data_object = biometric_data_object
        db.session.commit()

        return make_response({'response': 'OK', 'biometric_data': put_biometric_datas_to_json(new_biometric_data_object)}, 200)
    except Exception as e:

        return make_response({'response': 'ERROR', 'description': str(e)}, 500)


def put_biometric_datas_to_json(data):
    result = {
        'id': data.id,
        'id_user': data.id_user,
        'age': data.age,
        'height': data.height,
        'weight': data.weight,
        'timestamp': data.timestamp
    }

    return result
