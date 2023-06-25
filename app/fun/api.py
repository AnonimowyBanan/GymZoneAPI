from flask      import jsonify, request, make_response
from functools  import wraps
import os

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None

        if 'api-token' in request.headers:
                token = request.headers.get('api-token')

        if not token:
                return make_response(jsonify({'response': 'ERROR', 'description' : 'Token is missing'}), 401)
        
        if token == os.getenv('API_KEY'):
            return func(*args, **kwargs)
        else:
            return make_response(jsonify({'response': 'ERROR', 'description' : 'The token is invalid'}), 401)

    return decorated