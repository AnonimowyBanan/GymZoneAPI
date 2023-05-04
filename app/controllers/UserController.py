from flask import jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from . import api
from ..models.User import User
from app.extenctions import db

@api.route('/get-all', methods=['GET'])
def get_all_users():
    result = []

    try:
        users = User.query.all()

        if users == None:
            return make_response({'error': 'users not found'}, 204)
        
        for user in users:
            result.append(put_user_data_to_json(user))
            
        return make_response(jsonify(result), 200)

    except Exception as e:

        return make_response({'error': str(e)}, 500)


@api.route('/get', methods=['GET'])
def get_user_data():

    try:
        user = User.query.filter_by(id=int(request.args.get('user_ID'))).first()

        if user == None:

            return make_response({'error': 'user not found'}, 204)

        return make_response(jsonify(put_user_data_to_json(user)), 200)
    
    except Exception as e:

        return make_response({'error': str(e)}, 500)

@api.route('/delete', methods=['DELETE'])
def delete_user():

    try:
        user_to_delete = User.query.filter_by(id=request.args.get('user_ID')).first()

        if user_to_delete is None:

            return make_response({'error': 'user not found'}, 204)
        else:
            db.session.delete(user_to_delete)
            db.session.commit()

            return make_response(200)

    except Exception as e:

        return make_response({'error': str(e)}, 500)

@api.route('/edit', methods=['PUT'])
def edit_user():
     
    return 'xd'

@api.route('/add', methods=['PUT'])
def add_user():
     
    return 'xd'

def put_user_data_to_json(data):
     result = {
                    'id'                        : data.id,
                    'email'                     : data.email,
                    'login'                     : data.login,
                    'password'                  : data.password,
                    'first_name'                : data.first_name,
                    'last_name'                 : data.last_name,
                    'sex'                       : data.sex,
                    'user_picture_file_name'    : data.user_picture_file_name,
                    'user_description'          : data.user_description,
                    'birthday'                  : data.birthday,
                    'register_timestamp'        : data.register_timestamp
                }
     return result
     