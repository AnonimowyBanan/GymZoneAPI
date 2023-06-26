from flask import Flask, request, redirect
from dotenv import load_dotenv
from app.extenctions import db
from flask_restful import Api
import os
from flask_jwt_extended import JWTManager


def start_app():
    app = Flask(__name__)

    load_dotenv()
    app.config.update(
        SECRET_KEY=os.getenv('SECRET_KEY'),
        CSRF_ENABLED=os.getenv('CSRF_ENABLED'),
        CSRF_SECRET_KEY=os.getenv('CSRF_SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI'),
        JWT_SECRET_KEY=os.getenv('SECRET_KEY')
    )

    db.init_app(app)
    api = Api(app)

    jwt = JWTManager(app)

    from app.routes import user as user_bp
    from app.routes import exercise as exercise_bp
    from app.routes import biometric_data as biometric_data_bp
    from app.routes import auth as auth_bp

    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(exercise_bp, url_prefix="/exercise")
    app.register_blueprint(biometric_data_bp, url_prefix="/biometric-data")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app

app = start_app()
