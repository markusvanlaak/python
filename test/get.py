import http.client

conn = http.client.HTTPConnection("localhost:5000")
conn.request("GET", "/read?user=markus")

res = conn.getresponse()

data = res.read()

print(data)


