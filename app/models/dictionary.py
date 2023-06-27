from app.extenctions import db


class Dictionary(db.Model):
    __tablename__ = 'dictionary'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(48), nullable=False)
    code = db.Column(db.String(48), nullable=False)
    dcd_id = db.Column(db.Integer, db.ForeignKey('dictionary.id'), nullable=True)
    description = db.Column(db.Text, nullable=True)
    active = db.Column(db.Boolean, default=True, nullable=False)
    order = db.Column(db.Integer, nullable=False)
    creationDate = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

    def __init__(self):
        self.type = None
        self.code = None
        self.dcd_id = None
        self.description = None
        self.active = None

    def set_type(self, type: str):
        self.type = type

    def set_code(self, code: str):
        self.code = code

    def set_dcd_id(self, dcd_id: int):
        self.dcd_id = dcd_id

    def set_description(self, description: str):
        self.description = description

    def set_active(self, active: bool):
        self.active = active

    def set_order(self, order: int):
        self.order = order

