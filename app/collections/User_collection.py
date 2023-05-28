from app.models.User import User

class User_collection(User):

    def __init__(self, user_ID=0):
        self._user_ID = user_ID

    def set_user_id(self, user_ID: int):
        self._user_ID = user_ID
    
    def get_user_id(self):
        return self._user_ID
    
    def all():

        users = User.query.all()

        return users if users else []
    
    def get(self):

        user = User.query.filter_by(id=self._user_ID).first()

        return user if user else None