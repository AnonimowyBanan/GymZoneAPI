from ..models.Exercise import Exercise

class ExerciseCollection(Exercise):

    def __init__(self, exercise_ID=0):
        self._exercise_ID = exercise_ID

    def set_exercise_id(self, exercise_ID: int):
        self._exercise_ID = exercise_ID
    
    def get_exercise_id(self):
        return self._exercise_ID

    def get(self):
        exercise = Exercise.query.filter_by(id=self._exercise_ID).first()

        return exercise if exercise else None

    def all():
        exercises = Exercise.query.all()

        return exercises if exercises else []
