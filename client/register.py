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
    "username": "user4",
    "password": "pass1"
  }
#request = Request('http://127.0.0.1:5000/user/login', data=json.dumps(values), headers=headers)
request = Request('http://127.0.0.1:5000/user/register', data=json.dumps(values), headers=headers)

# Create new contact

response_body = urlopen(request).read()
print response_body
