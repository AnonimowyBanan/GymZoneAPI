from app.extenctions import db
from flask import jsonify, request, make_response
from . import auth
from app.models.User import User
from flask_bcrypt import check_password_hash
from flask_jwt_extended import create_access_token


@auth.route('/login', methods=['POST'])
def login():
    user_obj = User()

    email = request.form.get('email')
    password = request.form.get('password')
    user_obj.set_email(email)
    user = user_obj.get_user_by_email()

    if user is None:
        return make_response({'response': 'ERROR', 'description': 'User not found'}, 204)

    if check_password_hash(user.password, password):
        access_token = create_access_token(identity=email)
        return make_response({'response': 'OK', 'api-token': access_token}, 200)
    else:
        return make_response({'response': 'ERROR', 'description': 'Password or Email is incorrect'}, 200)
