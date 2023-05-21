from app.extenctions import db
from app.models import BodyPart

class Exercise(db.Model):

    __tablename__       = 'exercises'

    id                  = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_muscle           = db.Column(db.Integer, db.ForeignKey('body_parts.id'), nullable=False)
    name                = db.Column(db.String(64), nullable=False)
    description         = db.Column(db.String(512), nullable=False)

    body_part_id_muscle = db.relationship('BodyPart', foreign_keys=[id_muscle])