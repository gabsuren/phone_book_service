from flask import Blueprint, abort, make_response, request, jsonify

from api.utils import require_auth
from service.user_service import UserService
from service.ex import ServiceException

user_api = Blueprint('user_api', __name__)
user_service = UserService()


@user_api.route('/user/login', methods=['POST'])
@require_auth
def login(*args, **kwargs):
    """
    User login API endpoint. Requires parameters username and password.
    Stores generated token in response cookies
    """

    resp = make_response()
    token = user_service.generate_auth_token(kwargs['user_id'])
    if len(token) != 0:
        resp.set_cookie('token', token)
        resp.status_code = 201
    else:
        resp.status_code = 401
    return resp


@user_api.route('/user/register', methods=['POST'])
def new_user():
    """
    User register API endpoint. Required parameters are username and password.
    Creates new user with the given username and password
    """

    username = request.json.get('username')
    password = request.json.get('password')
    if not username or not password:
        abort(400)  # missing arguments

    try:
        user_service.add_user(username=username, password=password)
    except ServiceException as e:
        abort(e.error_code)  # existing user
    return jsonify(201)

