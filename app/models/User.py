from app.extenctions import db
from app.models import Dictionary

class User(db.Model):

    __tablename__   = 'users'

    id                  = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email               = db.Column(db.String(45), nullable=False)
    login               = db.Column(db.String(45), nullable=False)
    password            = db.Column(db.String(45), nullable=False)
    first_name          = db.Column(db.String(45), nullable=True)
    last_name           = db.Column(db.String(45), nullable=True)
    sex                 = db.Column(db.Integer, db.ForeignKey('dictionary.id'), nullable=False)
    user_picture        = db.Column(db.String(128), nullable=True)
    user_description    = db.Column(db.String(256), nullable=True)
    birthday            = db.Column(db.Date, nullable=True)
    register_timestamp  = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

    dcd         = db.relationship('Dictionary', backref='trip', cascade="all,delete", lazy=True)