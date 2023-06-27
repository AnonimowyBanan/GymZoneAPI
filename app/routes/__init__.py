from flask import Blueprint

user = Blueprint('user', __name__)
exercise = Blueprint('exercise', __name__)
biometric_data = Blueprint('biometric_data', __name__)
auth = Blueprint('auth', __name__)

from . import user
from . import exercise
from . import biometric_data
from . import auth

