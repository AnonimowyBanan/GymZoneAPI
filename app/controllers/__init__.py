from flask import Blueprint

user = Blueprint('api',__name__)
api = Blueprint('api',__name__)

from . import UserController
