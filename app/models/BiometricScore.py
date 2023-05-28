from app.extenctions import db

class BiometricScore(db.Model):

    __tablename__   = 'biometric_scores'

    id                      = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_biometric_data       = db.Column(db.Integer, db.ForeignKey('biometric_datas.id'), nullable=False)
    BMI                     = db.Column(db.Double, nullable=False)
    BMR                     = db.Column(db.Double, nullable=False)
    PBF                     = db.Column(db.Double, nullable=True)
    FFM                     = db.Column(db.Double, nullable=False)
    fit_score               = db.Column(db.Integer, nullable=False)