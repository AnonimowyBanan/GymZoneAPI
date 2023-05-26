from flask                      import jsonify, request, make_response
from .                          import exercise
from app.db.ExerciseCollection  import ExerciseCollection
from app.extenctions            import db

@exercise.route('/get-all', methods=['GET'])
def get_all_exercises():

    result = []

    exercises = ExerciseCollection.all()

    if exercises is None:
        return make_response({'error': 'exercises not found'}, 204)
    
    for exercise in exercises:
        result.append(put_exercise_data_to_json(exercise))

    return make_response(jsonify(result), 200)

@exercise.route('/get', methods=['GET'])
def get_exercise_data():
    
    exercise_obj = ExerciseCollection()

    exercise_obj.set_exercise_id(request.form.get('exercise_ID'))
    exercise = exercise_obj.get()

    if exercise is None:
        return make_response({'error': 'exercise not found'}, 204)
    
    result = put_exercise_data_to_json(exercise)

    return make_response(jsonify(result), 200)


@exercise.route('/delete', methods=['DELETE'])
def delete_exercise():

    exercise_obj = ExerciseCollection()

    exercise_obj.set_exercise_id(request.form.get('exercise_ID'))
    exercise_to_delete = exercise_obj.get()

    if exercise_to_delete is None:

        return make_response({'error': 'user not found'}, 204)
    
    try:
    
        db.session.delete(exercise_to_delete)
        db.session.commit()

        return make_response({'response': 'OK'}, 200)
        
    except Exception as e:
        
        return make_response({'error': str(e)}, 500)

@exercise.route('/edit', methods=['PUT', 'POST'])
def edit_exercise():

    exercise_obj = ExerciseCollection()

    exercise_obj.set_exercise_id(request.form.get('exercise_ID'))
    exercise_to_edit = exercise_obj.get()

    if exercise_to_edit is None:

        return make_response({'error': 'user not found'}, 204)
    else:
        exercise_to_edit.id_muscle      = request.form.get('id_muscle')
        exercise_to_edit.name           = request.form.get('name')
        exercise_to_edit.description    = request.form.get('description')
    
    try:

        db.session.commit()

        return make_response({'response': 'OK', 'exercise': put_exercise_data_to_json(exercise_to_edit)}, 200)
        
    except Exception as e:

        return make_response({'error': str(e)}, 500)


@exercise.route('/add', methods=['POST'])
def add_exercise():

    exercise_obj = ExerciseCollection()

    exercise_obj.id_muscle      = request.form.get('id_muscle')
    exercise_obj.name           = request.form.get('name')
    exercise_obj.description    = request.form.get('description')

    try:
        db.session.add(exercise_obj)
        db.session.commit()

        return make_response({'response': 'OK', 'exercise': put_exercise_data_to_json(exercise_obj)}, 200)
    
    except Exception as e:

        return make_response({'error': str(e)}, 500)


def put_exercise_data_to_json(data):

    result = {
        'exercise'      : {
            'id'            : data.id,
            'id_muscle'     : data.id_muscle,
            'name'          : data.name,
            'description'   : data.description
        },
        'muscle'        : {
            'id'            : data.body_part_id_muscle.id,
            'name'          : data.body_part_id_muscle.name,
            'picture'       : data.body_part_id_muscle.picture
        }
    }

    return result
