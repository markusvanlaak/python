import http.client

conn = http.client.HTTPConnection("localhost:5000")
conn.request("GET", "/read?user=markus")
#conn.request("GET", "/")


res = conn.getresponse()

data = res.read()

print(data)


