import etcd

client = etcd.Client(host='localhost', port=2379)

client.write('/nodes/n1', 1)

value = client.read('/nodes', recursive = True)

print(value)