from Crypto.Util.number import *
from Crypto.Cipher import AES
import base64
enc = open("dec_key","rb").read()
x = ""
for i in range(0,len(enc),5):
	v = bytes_to_long(enc[i:i+5])
	t = bin(v)[2:]
	if len(t) < 30: break
	x += t[21] + t[27] + t[33] + t[39]

key = long_to_bytes(int(x,2))
ct = open("cipher","rb").read().strip()
print(ct)
cipher = AES.new(key, AES.MODE_ECB)
print(cipher.decrypt(base64.b64decode(ct)))
