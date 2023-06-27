from app.extenctions import db

class BodyPart(db.Model):
    __tablename__ = 'body_parts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(48), nullable=True)
    picture = db.Column(db.String(48), nullable=True)

    exercise = db.relationship('Exercise', backref='bodyPart', cascade="all,delete", lazy=True)

    def __init__(self):
        self.name = None
        self.picture = None

    def set_name(self, name: str):
        self.name = name

    def set_picture(self, picture: str):
        self.picture = picture
