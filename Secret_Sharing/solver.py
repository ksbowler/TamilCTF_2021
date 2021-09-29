import base64
from Crypto.Util.number import *

p = b"AQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEp"
p = bytes_to_long(base64.b64decode(p))

rs = 2

shares = [b"MEwx7cz+C01rL8H0Hhz2EIgHjWYXVcL81uITmRha674=",b"YJhj22+ntS1s80CT9b6Y7ayc52baTFGNRpPUyLxtaf8=",b"kOSVyRJRXw1utr8zzWA7ytEyQWedQuAdtkWV+GB/6EA=",b"wTDHtrT7CO1wej3TpQHep/XHm2hgOW6uJfdXKASSZoE=",b"8Xz5pFekss1yPbxzfKOBhRpc9WkjL/0+lakYV6ik5MI="]

#f(1) = a1+a0 mod p
#f(2) = 2*a1+a0	mod p
f1 = bytes_to_long(base64.b64decode(shares[0]))
f2 = bytes_to_long(base64.b64decode(shares[1]))
a1 = (f2-f1)%p
flag = (f1-a1)%p
print(long_to_bytes(flag))
