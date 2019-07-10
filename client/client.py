from urllib2 import Request, urlopen
import base64
import json

#headers={

 #     'Authorization': 'Basic ' + base64.b64encode("user1" + \
 #     ":" + "pass1")
#}
headers = {
  'Content-Type': 'application/json',
}
values ={
    "username": "user6",
    "password": "pass1"
  }
#request = Request('http://127.0.0.1:5000/user/login', data=json.dumps(values), headers=headers)
#request = Request('http://127.0.0.1:5000/user/register', data=json.dumps(values), headers=headers)

# Create new contact
headers = {
  'Content-Type': 'application/json',
  'Token': 'eyJhbGciOiJIUzI1NiIsImV4cCI6MTQ5NzQzNTEwOSwiaWF0IjoxNDk3NDM0NTA5fQ.eyJpZCI6MX0.peUdpOWYYIMaGkaHcRFV8Nf-Flxp1cbIK3YDXlk_Wj8'
}

values = """
  {
    "first_name": "Alice",
    "last_name": "Cooper"
  }
"""
request = Request('http://127.0.0.1:5000/contacts', data=values, headers=headers)

# List All Contacts
headers = {
  'Token': 'eyJhbGciOiJIUzI1NiIsImV4cCI6MTQ5NzQzNTEwOSwiaWF0IjoxNDk3NDM0NTA5fQ.eyJpZCI6MX0.peUdpOWYYIMaGkaHcRFV8Nf-Flxp1cbIK3YDXlk_Wj8'
}
request = Request('http://127.0.0.1:5000/contacts', headers=headers)


#print "request json", request.text
response_body = urlopen(request).read()
print response_body
