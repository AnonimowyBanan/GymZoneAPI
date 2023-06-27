from app.extenctions import db
from app.models.user import User


class Training(db.Model):
    __tablename__ = 'trainings'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    training_name = db.Column(db.String(64), nullable=False)
    time = db.Column(db.Time, nullable=True)
    public = db.Column(db.Boolean, nullable=False)
    create_timestamp = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

    def __init__(self):
        self.training_name = None
        self.time = None
        self.public = None

    def set_id_user(self, id_user: int):
        self.id_user = id_user

    def set_training_name(self, training_name: str):
        self.training_name = training_name

    def set_time(self, time: str):
        self.time = time

    def set_public(self, public: bool):
        self.public = public
