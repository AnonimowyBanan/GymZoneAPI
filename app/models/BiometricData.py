from app.extenctions import db
from app.models import User

class BiometricData(db.Model):

    __tablename__   = 'biometric_datas'

    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user     = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    age         = db.Column(db.Integer, nullable=False)
    height      = db.Column(db.Double, nullable=False)
    weight      = db.Column(db.Double, nullable=False)
    BMI         = db.Column(db.Double, nullable=False)
    BMR         = db.Column(db.Double, nullable=False)
    TBW         = db.Column(db.Double, nullable=False)
    PBF         = db.Column(db.Double, nullable=False)
    FFM         = db.Column(db.Double, nullable=False)
    fit_score   = db.Column(db.Integer, nullable=False)
    timestamp   = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

    user        = db.relationship('User', backref='trip', cascade="all,delete", lazy=True)