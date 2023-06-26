from flask import Blueprint

user            = Blueprint('user',__name__)
exercise        = Blueprint('exercise',__name__)
biometric_data  = Blueprint('biometric_data', __name__)

from . import User
from . import Exercise
from . import BiometricDataController
