from urllib2 import Request, urlopen
import base64
import json

headers = {
  'Content-Type': 'application/json',
}
values ={
    "username": "user4",
    "password": "pass1"
  }
request = Request('http://127.0.0.1:5000/user/login', data=json.dumps(values), headers=headers)
#response_body = request.post('http://127.0.0.1:5000/user/login', data=json.dumps(values), headers=headers)
response_body = urlopen(request)
print response_body.headers
print response_body.getcode()
