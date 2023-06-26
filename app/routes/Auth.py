from app.extenctions import db
from flask import jsonify, request, make_response
from . import auth
from app.models.User import User


@auth.route('/login', methods=['POST'])
def login():
    user_obj = User()

    email = request.form.get('email')
    user_obj.set_email(email)
    user = user_obj.get_user_by_email()

    if user is None:
        return make_response({'response': 'ERROR', 'description': 'User not found'}, 204)



    password = request.form.get('password')




    return 'xd'
