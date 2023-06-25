from flask import Flask
from dotenv import load_dotenv
from app.extenctions import db
from flask_restful import Api
import os

def start_app():

    app = Flask(__name__)
    
    load_dotenv()
    app.config.update(
        SECRET_KEY                  = os.getenv('SECRET_KEY'),
        CSRF_ENABLED                = os.getenv('CSRF_ENABLED'),
        CSRF_SECRET_KEY             = os.getenv('CSRF_SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI     = os.getenv('SQLALCHEMY_DATABASE_URI')
    )

    db.init_app(app)
    api = Api(app)
    
    from app.controllers import user, exercise, biometric_data

    app.register_blueprint(user, url_prefix="/user")
    app.register_blueprint(exercise, url_prefix="/exercise")
    app.register_blueprint(biometric_data, url_prefix="/biometric-data")

    return app


def create_database():

        from app.models.User            import User
        from app.models.BiometricData   import BiometricData
        from app.models.BiometricScore  import BiometricScore
        from app.models.BodyPart        import BodyPart

        db.create_all()

        # users = [
        #     User(
        #         email='john@example.com',
        #         login='johndoe',
        #         password='password123',
        #         first_name='John',
        #         last_name='Doe',
        #         gender='Male',
        #         user_picture_file_name='john.jpg',
        #         user_description='Lorem ipsum dolor sit amet.',
        #         birthday='1990-01-01'
        #     ),
        #     User(
        #         email='jane@example.com',
        #         login='janesmith',
        #         password='password456',
        #         first_name='Jane',
        #         last_name='Smith',
        #         gender='Female',
        #         user_picture_file_name='jane.jpg',
        #         user_description='Lorem ipsum dolor sit amet.',
        #         birthday='1995-02-15'
        #     ),
        #     User(
        #         email='bob@example.com',
        #         login='bobjohnson',
        #         password='password789',
        #         first_name='Bob',
        #         last_name='Johnson',
        #         gender='Male',
        #         user_picture_file_name='bob.jpg',
        #         user_description='Lorem ipsum dolor sit amet.',
        #         birthday='1985-12-10'
        #     )
        # ]

        # db.session.add_all(users)
        # db.session.commit()

        # biometric_data = [
        #     BiometricData(id_user=1, age=30, height=180.5, weight=75.2),
        #     BiometricData(id_user=2, age=25, height=165.2, weight=55.8),
        #     BiometricData(id_user=3, age=35, height=175.9, weight=85.0)
        # ]


        # db.session.add_all(biometric_data)
        # db.session.commit()

        # biometric_scores = [
        #     BiometricScore(
        #         id_biometric_data=biometric_data.id,
        #         BMI=24.5,
        #         BMR=1500.2,
        #         PBF=20.3,
        #         fit_score=85
        #     )
        # ]

        # db.session.add_all(biometric_scores)
        # db.session.commit()

        # body_parts = [
        #     BodyPart(name='Arms', picture='arms.jpg'),
        #     BodyPart(name='Torso', picture='torso.jpg'),
        #     BodyPart(name='Legs', picture='legs.jpg')
        # ]

        # db.session.add_all(body_parts)
        # db.session.commit()


app = start_app()