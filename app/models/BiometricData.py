from app.extenctions import db

class BiometricData(db.Model):

    __tablename__   = 'biometric_datas'

    id                      = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user                 = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    age                     = db.Column(db.Integer, nullable=False)
    height                  = db.Column(db.Double, nullable=False)
    weight                  = db.Column(db.Double, nullable=False)
    timestamp               = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

    user                    = db.relationship('User', backref='BiometricData', cascade="all,delete", lazy=True)
    biometric_data          = db.relationship('BiometricScore', backref='BiometricData', cascade="all,delete", lazy=True)