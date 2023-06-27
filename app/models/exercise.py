from app.extenctions import db
from app.models import body_part


class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_muscle = db.Column(db.Integer, db.ForeignKey('body_parts.id'), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self):
        self.description = None
        self.name = None

    def set_id(self, id: int):
        self.id = id

    def set_id_muscle(self, muscle_id: int):
        self.id_muscle = muscle_id

    def set_name(self, name: str):
        self.name = name

    def set_description(self, description: str):
        self.description = description

    def get(self):
        exercise = Exercise.query.filter_by(id=self.exercise_ID).first()

        return exercise if exercise else None

    def all(self):
        exercises = Exercise.query.all()

        return exercises if exercises else []
