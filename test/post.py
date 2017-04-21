import http.client
import urllib.parse


params = urllib.parse.urlencode({'user' : 'markus', 'message': 'bla'})
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}


conn = http.client.HTTPConnection("localhost:5000")
conn.request("POST", "/post", params, headers)

res = conn.getresponse()

assert isinstance(res.status, object)
print(res.status, res.reason)

