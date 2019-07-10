from model import db
from model.contact import Contact


class ContactService(object):

    @staticmethod
    def create_contact(user_id, first_name, last_name):
        """
        Cretes contact for the given user
        :param user_id: id of the user whose created contact should belong to
        :param first_name: First Name of the contact
        :param last_name: last Name of the contact
        :return: created contact
        """

        contact = Contact(user_id, first_name, last_name)
        db.session.add(contact)
        db.session.commit()
        return contact

    @staticmethod
    def get_all_contacts_by_user_id(user_id):
        """
        Returns contacts for the given user
        :param user_id: id of the user whose contacts should be returned
        :return: Contacts queryset
        """

        return Contact.query.\
           filter_by(user_id=user_id).all()

    @staticmethod
    def update_contact_name(contact_id, first_name, last_name):
        """
        Updates given contact's name
        :param contact_id: id of the contact whose name should be updated
        :param first_name: first name of the contact
        :param last_name: last name of the contact
        :return: updated contact for a given contact_id
        """

        contact = Contact.query.filter_by(id=contact_id).first()
        if contact is None:
            return None
        contact.first_name = first_name
        contact.last_name = last_name
        db.session.commit()
        return contact

    @staticmethod
    def delete_contact(contact_id):
        """
        Deletes contact for the given contact id
        :param contact_id: id of the contact that should be deleted
        :return: contact_id
        """

        cont_id = Contact.query.filter_by(id=contact_id).delete()
        db.session.commit()
        return cont_id
