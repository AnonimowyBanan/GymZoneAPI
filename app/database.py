from app.extenctions import db
from app.models.user import User
from app.models.biometric_data import BiometricData
from app.models.exercise import Exercise
from app.models.biometric_score import BiometricScore
from app.models.body_part import BodyPart
from app.models.dictionary import Dictionary
from app.models.training import Training
from app.models.training_exercise import Exercise

# Python flask, SQLalchemy
def database_initialization():

    db.create_all()

    for i in range(10):

        user = User()
        user.set_email(f'email{i}@test.com')
        user.set_login(f'user{i}')
        user.set_password('password123')
        user.set_first_name(f'User{i}')
        user.set_last_name(f'Lastname{i}')
        user.set_gender('male')
        user.set_user_picture_file_name(f'user{i}.jpg')
        user.set_user_description(f'Description for user {i}')
        user.set_birthday(f'2023-06-{i}')

        db.session.add(user)
        db.session.flush()

        biometric_data = BiometricData()
        biometric_data.set_id_user(user.id)
        biometric_data.set_age(18 + i)
        biometric_data.set_height(170 + i)
        biometric_data.set_weight(60 + i)

        db.session.add(biometric_data)

        body_part = BodyPart()
        body_part.set_name(f'Exercise {i} name')
        body_part.set_picture(f'exercise_pic{i}.jpg')

        db.session.add(body_part)
        db.session.flush()

        exercise = Exercise()
        exercise.set_id_muscle(body_part.id)
        exercise.set_name(f'Exercise {i} name')
        exercise.set_description(f'Exercise {i} description')

        db.session.add(exercise)


    db.session.commit()