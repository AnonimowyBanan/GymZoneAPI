from flask import jsonify, request, make_response
from . import exercise
from app.models.exercise import Exercise
from app.extenctions import db
from flask_jwt_extended import jwt_required


@exercise.route('/get-all', methods=['GET'])
@jwt_required()
def get_all_exercises():
    exercise_obj = Exercise()

    exercises = exercise_obj.all()

    if exercises is None:
        return make_response({'response': 'ERROR', 'description': 'Exercises not found'}, 204)

    result = []
    for exercise in exercises:
        result.append(put_exercise_data_to_json(exercise))

    return make_response(jsonify(result), 200)


@exercise.route('/get', methods=['GET'])
@jwt_required()
def get_exercise_data():
    exercise_obj = Exercise()

    exercise_obj.set_id(int(request.form.get('exercise_ID')))
    exercise = exercise_obj.get()

    if exercise is None:
        return make_response({'response': 'ERROR', 'description': 'Exercise not found'}, 204)
    else:
        return make_response({'response': 'OK', 'exercise': put_exercise_data_to_json(exercise)}, 200)


@exercise.route('/delete', methods=['DELETE'])
@jwt_required()
def delete_exercise():
    exercise_obj = Exercise()

    exercise_obj.set_id(int(request.form.get('exercise_ID')))
    exercise_to_delete = exercise_obj.get()

    if exercise_to_delete is None:
        return make_response({'response': 'ERROR', 'description': 'Exercise not found'}, 204)

    try:

        db.session.delete(exercise_to_delete)
        db.session.commit()

        return make_response({'response': 'OK'}, 200)

    except Exception as e:

        return make_response({'error': str(e)}, 500)


@exercise.route('/edit', methods=['PUT', 'POST'])
@jwt_required()
def edit_exercise():
    exercise_obj = Exercise()

    exercise_obj.set_id(int(request.form.get('exercise_ID')))
    exercise_to_edit = exercise_obj.get()

    if exercise_to_edit is None:

        return make_response({'response': 'ERROR', 'description': 'Exercise not found'}, 204)
    else:
        exercise_to_edit.id_muscle = int(request.form.get('id_muscle'))
        exercise_to_edit.name = request.form.get('name')
        exercise_to_edit.description = request.form.get('description')

    try:

        db.session.commit()

        return make_response({'response': 'OK', 'exercise': put_exercise_data_to_json(exercise_to_edit)}, 200)

    except Exception as e:

        return make_response({'response': 'ERROR', 'description': str(e)}, 500)


@exercise.route('/add', methods=['POST'])
@jwt_required()
def add_exercise():
    exercise_obj = Exercise()

    exercise_obj.set_id_muscle(int(request.form.get('id_muscle')))
    exercise_obj.set_name(request.form.get('name'))
    exercise_obj.set_description(request.form.get('description'))

    try:
        db.session.add(exercise_obj)
        db.session.commit()

        return make_response({'response': 'OK', 'exercise': put_exercise_data_to_json(exercise_obj)}, 200)

    except Exception as e:
        db.session.rollback()

        return make_response({'response': 'ERROR', 'description': str(e)}, 500)


def put_exercise_data_to_json(data):
    result = {
        'exercise': {
            'id': data.id,
            'id_muscle': data.id_muscle,
            'name': data.name,
            'description': data.description
        },
        'body_part': {
            'id': data.bodyPart.id,
            'name': data.bodyPart.name,
            'picture': data.bodyPart.picture
        }
    }

    return result
