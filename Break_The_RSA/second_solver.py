from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.number import *
import base64
b2 = b"MDgwDQYJKoZIhvcNAQEBBQADJwAwJAIdDVZLl4+dIzUElY7ti3RDcyge0UGLKfHs+oCT2M8CAwEAAQ=="
v2 = base64.b64decode(b2)
cipher = RSA.importKey(v2)
print(cipher)
# RsaKey(n=359567260516027240236814314071842368703501656647819140843316303878351, e=65537)

# nを素因数分解すると、p,q= 17963604736595708916714953362445519,20016431322579245244930631426505729
p,q= 17963604736595708916714953362445519,20016431322579245244930631426505729
n = 359567260516027240236814314071842368703501656647819140843316303878351
assert n == p*q
e = 65537
ct2 = b"C1qKLBtrUwLkebPf+JKX6ie1bKEdUGmzkYwBJWQ="
ct2 = bytes_to_long(base64.b64decode(ct2))
phi = (p-1)*(q-1)
d = inverse(e,phi)
m = pow(ct2,d,n)
print(long_to_bytes(m))
