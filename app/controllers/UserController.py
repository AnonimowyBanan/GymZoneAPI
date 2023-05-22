from flask                  import jsonify, request, make_response
from .                      import user
from ..models.User          import User
from app.db.UserCollection  import UserCollection
from app.extenctions        import db

@user.route('/get-all', methods=['GET'])
def get_all_users():

    result = []

    try:
        users = UserCollection.all()

        if users == None:
            return make_response({'error': 'users not found'}, 204)
        
        for user in users:
            result.append(put_user_data_to_json(user))
            
        return make_response(jsonify(result), 200)

    except Exception as e:

        return make_response({'error': str(e)}, 500)

@user.route('/get', methods=['GET'])
def get_user_data():

    user_obj = UserCollection()

    try:
        user_obj.set_user_id(request.form.get('user_ID'))
        user = user_obj.get()

        if user is None:

            return make_response({'error': 'user not found'}, 204)

        return make_response(jsonify(put_user_data_to_json(user)), 200)
    
    except Exception as e:

        return make_response({'error': str(e)}, 500)

@user.route('/delete', methods=['DELETE'])
def delete_user():

    user_obj = UserCollection()

    try:
        user_obj.set_user_id(request.form.get('user_ID'))
        user_to_delete = user_obj.get()

        if user_to_delete is None:

            return make_response({'error': 'user not found'}, 204)
        else:
            db.session.delete(user_to_delete)
            db.session.commit()

            return make_response({'response': 'OK'}, 200)

    except Exception as e:

        return make_response({'error': str(e)}, 500)

@user.route('/edit', methods=['PUT', 'POST'])
def edit_user():

    user_obj = UserCollection()
    user_obj.set_user_id(request.form.get('user_ID'))
    
    user_to_edit = user_obj.get()

    user_to_edit.email                      = request.form.get('email')
    user_to_edit.login                      = request.form.get('login')
    user_to_edit.password                   = request.form.get('password')
    user_to_edit.first_name                 = request.form.get('first_name')
    user_to_edit.last_name                  = request.form.get('last_name')
    user_to_edit.sex                        = request.form.get('sex')
    user_to_edit.user_picture_file_name     = request.form.get('user_picture_file_name')
    user_to_edit.user_description           = request.form.get('user_description')
    user_to_edit.birthday                   = request.form.get('birthday')

    try:

        db.session.add(user_to_edit)
        db.session.commit()

        return make_response({'response': 'OK', 'user': put_user_data_to_json(user_to_edit)}, 200)
    
    except Exception as e:

        return make_response({'error': str(e)}, 500)

@user.route('/add', methods=['POST'])
def add_user():
    
    user = User()

    user.email                      = request.form.get('email')
    user.login                      = request.form.get('login')
    user.password                   = request.form.get('password')
    user.first_name                 = request.form.get('first_name')
    user.last_name                  = request.form.get('last_name')
    user.sex                        = request.form.get('sex')
    user.user_picture_file_name     = request.form.get('user_picture_file_name')
    user.user_description           = request.form.get('user_description')
    user.birthday                   = request.form.get('birthday')

    try:
    
        db.session.add(user)
        db.session.commit()

        return make_response({'response': 'OK'}, 200)
    
    except Exception as e:

        return make_response({'error': str(e)}, 500)

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
     