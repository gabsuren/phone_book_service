from . import db

from passlib.apps import custom_app_context as pwd_context


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, username=None, password_hash=None):
        self.username = username
        self.password_hash = password_hash

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)