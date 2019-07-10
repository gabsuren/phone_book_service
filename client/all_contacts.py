from urllib2 import Request, urlopen
import base64
import json
import sys

# List All Contacts
if len(sys.argv) < 2:
    print "Please specify token"
    exit(1)

token = sys.argv[1]
headers = {
'Token': token
}
request = Request('http://127.0.0.1:5000/contacts', headers=headers)
#request = Request('http://127.0.0.1:5000/contacts')


#print "request json", request.text
response_body = urlopen(request).read()
print response_body
