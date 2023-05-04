from flask import Flask
from dotenv import load_dotenv
from app.extenctions import db
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

    from app.controllers import api

    app.register_blueprint(api, url_prefix="/user")

    return app

app = start_app()
