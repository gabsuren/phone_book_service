from model.phone_number import PhoneNumber
from model import db


class PhoneService(object):
    @staticmethod
    def add_phone_number(contact_id, phone_number):
        """
        Adds phone number to the given contact
        :param contact_id: id of the contact
        :param phone_number: phone number to be added to contact
        :return: phone_number
        """

        phone_number = PhoneNumber(contact_id=contact_id, phone_number=phone_number)
        db.session.add(phone_number)
        db.session.commit()
        return phone_number

