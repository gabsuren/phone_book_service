from . import db


class PhoneNumber(db.Model):
    __tablename__ = 'PhoneNumber'
    id = db.Column(db.Integer, primary_key=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('Contact.id'))
    phone_number = db.Column(db.String(128))

    def __init__(self, contact_id=None, phone_number=None):
        self.contact_id = contact_id
        self.phone_number = phone_number