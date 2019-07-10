from . import db


class Contact(db.Model):
    __tablename__ = 'Contact'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    phone_numbers = db.relationship('PhoneNumber')

    def __init__(self, user_id=None, first_name=None, last_name=None):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
