## Phonebook Service

### INTRODUCTION<br />
    Phonebook service provides simple APIs allowing users to login and manage contacts.
 All contact management calls are authenticated.
 
 #### SETUP AND RUN<br />
    1. ./setup
    2. python main.py
    
### API ENDPOINTS
 #### User API
 - User registration <br> 
 `/user/register method POST`
 
    ##### Required parameters
    ```json
    {
      "username": "my-username",
      "password": "my-password"
    }
    ```
     Registers new user to the system.
 
 - User Login <br>
 `/user/login method POST`
 
     ##### Required parameters
    ```json
    {
      "username": "my-username",
      "password": "my-password"
    }
    ```
     Allows a user to login returning a session token that should be sent in all 
     authenticated calls.
 
 ####Contacts API
 - List Contacts <br>
 `/contacts`<br>
 Returns all contacts of the current user
 
 - Create Contact <br>
 `/contacts', methods=['POST']`
    ##### Required parameters
    ```json
    {
      "first_name": "contact-first-name",
      "last_name": "contact-last-name"
    }
    ```
    
    Allows a user to create contact with the given first_name and last_name
 
 - Update a Contact's name <br>
 `/contacts/<int:contact_id>', methods=['POST']`
    ##### Required parameters
    ```json
    {
      "first_name": "new-first-name",
      "last_name": "new-last-name"
    }
    ```
    
    Allows a user to update contact's first_name and last_name
    
 - Delete a Contact <br>
 `/contacts/<int:contact_id>, methods=['DELETE']`
 
    Allows a user to delete contacts with the specified contact id
 
  - Add a Phone number <br>
 `/contacts/<int:contact_id>/entries,  methods=['POST']`
 
    ##### Required parameters
    ```json
    {
      "phone": "+1 (555) 123-456"
    }
    ```
    Allows a user to add phone number to contact
