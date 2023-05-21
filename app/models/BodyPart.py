from app.extenctions import db

class BodyPart(db.Model):
    
    __tablename__   = 'body_parts'

    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name        = db.Column(db.String(48), nullable=True)
    picture     = db.Column(db.String(48), nullable=True)