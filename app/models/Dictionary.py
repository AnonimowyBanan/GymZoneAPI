from app.extenctions import db

class Dictionary(db.Model):

    __tablename__   = 'dictionary'

    id              = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type            = db.Column(db.String(48), nullable=False)
    code            = db.Column(db.String(48), nullable=False)
    dcd_id          = db.Column(db.Integer, db.ForeignKey('dictionary.id'), nullable=True)
    description     = db.Column(db.String(300), nullable=True)
    isActive        = db.Column(db.Boolean, default=True, nullable=False)
    order           = db.Column(db.Integer, nullable=False)
    creationDate    = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)