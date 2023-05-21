from flask              import jsonify, request, make_response
from .                  import exercise
from ..models.Exercise  import Exercise
from app.extenctions    import db

@exercise.route('/get-all', methods=['GET'])
def get_all_exercises():

    result = []

    exercises = Exercise.query.all()

    try:
        exercises = Exercise.query.all()

        if exercises == None:
            return make_response({'error': 'exercises not found'}, 204)
        
        for exercise in exercises:
            result.append(put_exercise_data_to_json(exercise))

        return make_response(jsonify(result), 200)

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
            'picture'       : data.body_part_id_muscle.picture
        }
    }

    return result
