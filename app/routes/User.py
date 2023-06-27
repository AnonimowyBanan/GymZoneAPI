from flask import jsonify, request, make_response
from . import user
from app.models.User import User
from app.extenctions import db
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required


@user.route('/get-all', methods=['GET'])
@jwt_required()
def get_all_users():
    result = []
    
    try:
        user_obj = User()
        users = user_obj.all()

        if users is None:
            return make_response({'response': 'ERROR', 'description': 'Users not found'}, 204)

        for user in users:
            result.append(put_user_data_to_json(user))

        return make_response(jsonify(result), 200)

    except Exception as e:

        return make_response({'error': str(e)}, 500)


@user.route('/get', methods=['GET'])
@jwt_required()
def get_user_data():
    user_obj = User()

    user_obj.set_id(int(request.form.get('user_ID')))
    user = user_obj.get()

    try:
        if user is None:

            return make_response({'response': 'ERROR', 'description': 'User not found'}, 204)
        else:

            return make_response(jsonify(put_user_data_to_json(user)), 200)

    except Exception as e:

        return make_response({'error': str(e)}, 500)


@user.route('/delete', methods=['DELETE'])
@jwt_required()
def delete_user():
    user_obj = User()

    try:
        user_obj.set_id(int(request.form.get('user_ID')))
        user_to_delete = user_obj.get()

        if user_to_delete is None:

            return make_response({'response': 'ERROR', 'description': 'User not found'}, 204)
        else:
            db.session.delete(user_to_delete)
            db.session.commit()

            return make_response({'response': 'OK'}, 200)

    except Exception as e:

        return make_response({'error': str(e)}, 500)


@user.route('/edit', methods=['PUT', 'POST'])
@jwt_required()
def edit_user():
    user_obj = User()
    user_obj.set_id(int(request.form.get('user_ID')))

    user_to_edit = user_obj.get()

    if user_to_edit is None:
        return make_response({'response': 'ERROR', 'description': 'User not found'}, 204)

    user_to_edit.email = request.form.get('email')
    user_to_edit.login = request.form.get('login')
    user_to_edit.password = generate_password_hash(request.form.get('password'))
    user_to_edit.first_name = request.form.get('first_name')
    user_to_edit.last_name = request.form.get('last_name')
    user_to_edit.gender = request.form.get('gender')
    user_to_edit.user_picture_file_name = request.form.get('user_picture_file_name')
    user_to_edit.user_description = request.form.get('user_description')
    user_to_edit.birthday = request.form.get('birthday')

    try:

        db.session.add(user_to_edit)
        db.session.commit()

        return make_response({'response': 'OK', 'user': put_user_data_to_json(user_to_edit)}, 200)

    except Exception as e:

        return make_response({'response': 'ERROR', 'description': str(e)}, 500)


@user.route('/add', methods=['POST'])
def add_user():
    user_obj = User()
    user_obj.set_email(request.form.get('email'))

    if user_obj.check_if_email_exist():
        return make_response({'response': 'ERROR', 'description': 'Email is already in use'}, 500)
    else:
        user_obj.set_login(request.form.get('login'))
        user_obj.set_password(request.form.get('password'))
        user_obj.set_first_name(request.form.get('first_name'))
        user_obj.set_last_name(request.form.get('last_name'))
        user_obj.set_gender(request.form.get('gender'))
        user_obj.set_user_picture_file_name(request.form.get('user_picture_file_name'))
        user_obj.set_user_description(request.form.get('user_description'))
        user_obj.set_birthday(request.form.get('birthday'))

    try:

        db.session.add(user_obj)
        db.session.commit()

        return make_response({'response': 'OK'}, 200)

    except Exception as e:

        return make_response({'response': 'ERROR', 'description': str(e)}, 500)


@user.route('/check-login', methods=["POST"])
def check_login():
    user_obj = User()
    user_obj.set_email(request.form.get('email'))

    user_to_login = user_obj.get_user_by_email()

    if user_to_login is not None:
        is_password_valid = check_password_hash(user_to_login.password, request.form.get('password'))
        if is_password_valid:
            return make_response({'response': 'OK', 'user': put_user_data_to_json(user_to_login)}, 200)
        else:
            return make_response({'response': 'ERROR', 'description': 'Wrong password'}, 204)
    else:
        return make_response({'response': 'ERROR', 'description': 'User not found'}, 204)


def put_user_data_to_json(data):
    result = {
        'id': data.id,
        'email': data.email,
        'login': data.login,
        'password': data.password,
        'first_name': data.first_name,
        'last_name': data.last_name,
        'gender': data.gender,
        'user_picture_file_name': data.user_picture_file_name,
        'user_description': data.user_description,
        'birthday': data.birthday,
        'register_timestamp': data.register_timestamp
    }

    return result
