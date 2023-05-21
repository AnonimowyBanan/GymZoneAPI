from flask import Blueprint

user = Blueprint('api',__name__)
exercise = Blueprint('exercise',__name__)

from . import UserController
from . import ExerciseController
