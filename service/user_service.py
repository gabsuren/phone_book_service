from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

from model import db
from model.user import User
from .ex import ServiceException


class UserService(object):

    @staticmethod
    def add_user(username, password):
        """
        Adds user with the given username and password.
            If User with the following username exists raises a ServiceException
        :param username: username of the added user
        :param password: password of the added user
        :return: created user
        """

        if User.query.filter_by(username=username).first() is not None:
            error_message = "User with the following username already exists"
            error_code = 400
            raise ServiceException(error_message, error_code)

        user = User(username=username)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user_by_id(id):
        """
        Returns user for the given id if exists otherwise None.
        :param id: id of the user
        :return: user object
        """

        return User.query.get(id)

    @staticmethod
    def get_user_by_username(username):
        """
        Returns user for the given username if exists otherwise None.
        :param username: username of the user
        :return: user object
        """

        return User.query.filter_by(username=username).first()

    @staticmethod
    def generate_auth_token(user_id, expiration=1500):
        """
        Generates auth token for the given user
        :param user_id: id of the user
        :param expiration: expiration time in seconds.
        :return: token
        """

        s = Serializer(db.get_app().config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': user_id})

    @staticmethod
    def verify_auth_token(token):
        """
        Verifies auth token and returns corresponding user
            if token is verified, otherwise None
        :param token: given token which should be verified
        :return: corresponding user in case of valid token, otherwise None
        """

        s = Serializer(db.get_app().config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['id'])
        return user


