from app.extenctions import db

class BiometricScore(db.Model):

    __tablename__   = 'biometric_scores'

    BMI                     = db.Column(db.Double, nullable=False)
    BMR                     = db.Column(db.Double, nullable=False)
    PBF                     = db.Column(db.Double, nullable=True)
    FFM                     = db.Column(db.Double, nullable=False)
    waist_circumference     = db.Column(db.Double, nullable=True)
    hip_circumference       = db.Column(db.Double, nullable=True)
    neck_circumference      = db.Column(db.Double, nullable=True)
    fit_score               = db.Column(db.Integer, nullable=False)