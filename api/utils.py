from functools import wraps

from flask import request, abort

from service import UserService


def require_auth(f):
    """
    Decorator which is used for checking authorization.
    If username and password are exist in the request's body then tries to
    authorize with them, otherwise if looking token in the request headers
    and tries to authorize with that if its found.
    If authorization fails returns 401
    """

    @wraps(f)
    def decorated(*args, **kwargs):
        #res = f(*args, **kwargs)
        headers = request.headers
        body = request.json
        if body and 'username' in body and 'password' in body:
            username = body.get('username')
            password = body.get('password')
            user = UserService.get_user_by_username(username=username)
            if not user or not user.verify_password(password):
                abort(401)
            kwargs['user_id'] = user.id
        elif 'token' in headers:
            user = UserService.verify_auth_token(headers['token'])
            if user is None:
                abort(401)
            kwargs['user_id'] = user.id
        else:
            abort(401)
        return f(*args, **kwargs)
    return decorated
