import base64
from Crypto.Util.number import *
import urllib.parse

megan35 = b"3GHIJKLMNOPQRSTUb=cdefghijklmnopWXYZ/12+406789VaqrstuvwxyzABCDEF5"
b = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
dec_dict = dict(zip(megan35, b))

# megan 35 decode
enc = b"bwDVjxOXnMR1RZGjlxe1RZGMlxb1RZG0nHesRHesRceqbgy1RZ31Rub1RZ3wSZm1RJK/OdNqOdSJOdNqRd3sSseqbge1RZ31Rub1RZ3tOdGGjLfZm+1qnHesRL1u="
dec = b""
for e in enc:
	v = dec_dict[e]
	dec += long_to_bytes(v)
msg = base64.b64decode(dec[:-1])
print(urllib.parse.unquote(msg.decode()))


# decode RSA

n = 667
d = 1027
e = 3

ct = [408,217,382,380,416,613,408,162,604,9,537,146,280]
for c in ct:
	m = pow(c,d,n)
	print(chr(m),end="")
print()
