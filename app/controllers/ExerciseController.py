from flask              import jsonify, request, make_response
from .                  import exercise
from ..models.Exercise  import Exercise
from app.extenctions    import db

@exercise.route('/get-all', methods=['GET'])
def get_all_exercises():

    result = []

    try:
        exercises = Exercise.query.all()

        if exercises == None:
            return make_response({'error': 'exercises not found'}, 204)
        
        for exercise in exercises:
            result.append(put_exercise_data_to_json(exercise))

        return make_response(jsonify(result), 200)

    except Exception as e:

            return make_response({'error': str(e)}, 500)

@exercise.route('/get', methods=['GET'])
def get_exercise_data():
    
    try:
        exercise = Exercise.query.filter_by(id=request.form.get('exercise_ID')).first()

        if exercise == None:
            return make_response({'error': 'exercise not found'}, 204)
        
        result = put_exercise_data_to_json(exercise)

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
            'name'          : data.body_part_id_muscle.name,
            'picture'       : data.body_part_id_muscle.picture
        }
    }

    return result
