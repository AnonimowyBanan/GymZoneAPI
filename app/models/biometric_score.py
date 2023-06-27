from app.extenctions import db
from app.models.biometric_data import BiometricData


class BiometricScore(db.Model):
    __tablename__ = 'biometric_scores'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_biometric_data = db.Column(db.Integer, db.ForeignKey('biometric_datas.id'), nullable=False)
    BMI = db.Column(db.Double, nullable=False)
    BMR = db.Column(db.Double, nullable=False)
    PBF = db.Column(db.Double, nullable=True)
    # FFM                     = db.Column(db.Double, nullable=False)
    fit_score = db.Column(db.Integer, nullable=False)

    def __init__(self, gender: str, height: float, weight: float):
        self.id = 0
        self.id_biometric_data = None
        self.BMI = None
        self.BMR = None
        self.PBF = None
        self.fit_score = None
        self.gender = gender
        self.height = height
        self.height_m = height / 100
        self.weight = weight

    def set_id(self, id: int):
        self.id = id

    def set_id_biometric_data(self, id_biometric_data: int):
        self.id_biometric_data = id_biometric_data

    def set_BMI(self, BMI: float):
        if BMI is not None:
            self.BMI = BMI
        else:
            bmi = self.weight / (self.height_m ** 2)

            self.BMI = round(bmi, 2)

    def set_BMR(self, BMR: float):
        self.BMR = BMR

    def set_PBF(self, PBF: float):
        self.PBF = PBF

    def set_fit_score(self, fit_score: float):
        self.fit_score = fit_score

    def get(self):
        result = BiometricScore.query.filter_by(id_biometric_data=self._biometric_data_ID).first()

        return result if result else None
