import sys, requests, base64, mmh3

response = requests.get('https://www.juul.com/favicon.ico')
data = response.content
#data = binascii.b2a_base64(data)
data = base64.encodebytes(data)
data = mmh3.hash(data)
#sys.stdout.buffer.write(data)
print(data)
