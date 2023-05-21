from flask              import jsonify, request, make_response
from .                  import exercise
# from ..models.Exercise  import Exercise
from app.extenctions    import db

@exercise.route('/get-all', methods=['GET'])
def get_all_exercises():
    return "Xd"
