from app.extenctions import db
from app.models.training import Training
from app.models.exercise import Exercise


class TrainingExercise(db.Model):
    __tablename__ = 'training_exercise'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_training = db.Column(db.Integer, db.ForeignKey('trainings.id'), nullable=False)
    id_exercise = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    sets = db.Column(db.Integer, nullable=True)
    reps = db.Column(db.Integer, nullable=True)
    time = db.Column(db.Time, nullable=True)
    load = db.Column(db.Double, nullable=True)

    def __init__(self):
        self.id_training = None
        self.id_exercise = None
        self.sets = None
        self.reps = None
        self.time = None
        self.load = None

    def set_id_training(self, id_training: int):
        self.id_training = id_training

    def set_id_exercise(self, id_exercise: int):
        self.id_exercise = id_exercise

    def set_sets(self, sets: int):
        self.sets = sets

    def set_reps(self, reps: int):
        self.reps = reps

    def set_time(self, time: str):
        self.time = time

    def set_load(self, load: float):
        self.load = load
