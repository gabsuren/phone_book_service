from flask import Blueprint, abort
from flask import request, jsonify

from api.utils import require_auth
from service.contact_service import ContactService
from service.phone_service import PhoneService

contact_api = Blueprint('contact_api', __name__)
contact_service = ContactService()
phone_service = PhoneService()


@contact_api.route('/contacts', methods=['POST'])
@require_auth
def create_contact(*args, **kwargs):
    """
    Create contact API endpoint. Required parameters are
        first_name and last_name. Returns new created contact
    """

    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    contact = contact_service.create_contact(user_id=kwargs['user_id'],
                                             first_name=first_name,
                                             last_name=last_name)
    if not contact:
        abort(400)

    response = jsonify(id=contact.id)
    response.status_code = 201
    return response


@contact_api.route('/contacts/<int:contact_id>', methods=['POST'])
@require_auth
def update_contact_name(contact_id, **kwargs):
    """
    Update contact API endpoint.
    """

    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    contact = contact_service.\
        update_contact_name(contact_id, first_name, last_name)
    if not contact:
        abort(400)

    return jsonify(id=contact.id)


@contact_api.route('/contacts/<int:contact_id>/entries',  methods=['POST'])
@require_auth
def add_phone_number(contact_id, *args, **kwargs):
    """
    Add Phone number API endpoint. Required parameter is phone
    """

    phone_number = request.json.get('phone')
    phone_number_obj = phone_service.add_phone_number(contact_id, phone_number)
    if not phone_number_obj:
        abort(400)
    response = jsonify(id=contact_id)
    response.status_code = 201
    return response


# List All Contacts
@contact_api.route('/contacts')
@require_auth
def list_all_contacts(*args, **kwargs):
    """
    List contacts API endpoint
    """

    contacts = contact_service.get_all_contacts_by_user_id(kwargs['user_id'])
    result = []
    for contact in contacts:
        result.append({
            'id': contact.id,
            'first_name': contact.first_name,
            'last_name': contact.last_name,
            'phones': [phone.phone_number for phone in contact.phone_numbers]
        })
    print result
    return jsonify(result)


@contact_api.route('/contacts/<int:contact_id>', methods=['DELETE'])
@require_auth
def delete_contact(contact_id, **kwargs):
    """
    Delete contact API endpoint
    """

    contact_service.delete_contact(contact_id)
    return jsonify(id=contact_id)

