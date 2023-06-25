from app.models.User    import User
from flask_bcrypt       import generate_password_hash


class User_collection(User):

    def __init__(self, user_ID=0):
        self._user_ID = user_ID

    def set_id(self, user_ID: int):
        self._user_ID = user_ID
        
    def set_email(self, email: str):
        self.email = email

    def set_login(self, login: str):
        self.login = login
    
    def set_password(self, password: str):
        self.password = generate_password_hash(password).decode('utf-8')

    def set_first_name(self, first_name: str):
        self.first_name = first_name

    def set_last_name(self, last_name: str):
        self.last_name = last_name

    def set_gender(self, gender: str):
        self.gender = gender

    def set_user_picture_file_name(self, user_picture_file_name: str):
        self.user_picture_file_name = user_picture_file_name

    def set_user_description(self, user_description: str):
        self.user_description = user_description

    def set_birthday(self, birthday: str):
        self.birthday = birthday
    
    def all():

        users = User.query.all()

        return users if users else []
    
    def get(self):

        user = User.query.filter_by(id=self._user_ID).first()

        return user if user else None
    
    def check_if_email_exist(self):
        
        count = User.query.filter_by(email=self.email).count()

        return True if count > 0 else False
    
    def get_user_by_email(self):

        user = User.query.filter_by(email=self.email).first()

        return user if user else None