from app.extenctions import db
from sqlalchemy.orm import relationship
from app.models.user import User


class BiometricData(db.Model):
    __tablename__ = 'biometric_datas'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Double, nullable=False)
    weight = db.Column(db.Double, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)


    def __init__(self):
        self.id_user = None
        self.age = None
        self.height = None
        self.weight = None

    def set_id(self, id: int):
        self.id = id

    def set_id_user(self, user_ID: int):
        self.id_user = user_ID

    def set_age(self, age: int):
        self.age = age

    def set_height(self, height: float):
        self.height = height

    def set_weight(self, weight: float):
        self.weight = weight

    def get(self):
        biometric_data = BiometricData.query.filter_by(id=self.id).first()

        return biometric_data if biometric_data else None

    def all(self):
        biometric_datas = BiometricData.query.all()

        return biometric_datas if biometric_datas else None
