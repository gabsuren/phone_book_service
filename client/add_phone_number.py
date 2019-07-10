from urllib2 import Request, urlopen
import base64
import json
import sys


if len(sys.argv) < 2:
    print "Please specify token"
    exit(1)
token = sys.argv[1]

# Add Phone number
headers = {
 'Content-Type': 'application/json',
  'Token': token }

values = """
  {
    "phone": "+1 (555) 0000-0000"
  }
"""
request = Request('http://127.0.0.1:5000/contacts/1/entries', data=values, headers=headers)


#print "request json", request.text
response_body = urlopen(request)
print response_body.headers
print response_body.getcode()
print response_body.read()
