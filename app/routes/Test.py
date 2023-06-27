from flask import jsonify, request, make_response
from . import test


@test.route('/', methods=["GET"])
def test():
    return 'test'
