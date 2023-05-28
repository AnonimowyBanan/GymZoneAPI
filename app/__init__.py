from flask import Flask
from dotenv import load_dotenv
from app.extenctions import db
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
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

    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "GymZone API"})

    from app.controllers import user, exercise, biometric_data

    app.register_blueprint(swaggerui_blueprint, url_prefix="/swagger")
    app.register_blueprint(user, url_prefix="/user")
    app.register_blueprint(exercise, url_prefix="/exercise")
    app.register_blueprint(biometric_data, url_prefix="/biometric-data")

    return app

app = start_app()
