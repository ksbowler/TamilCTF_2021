from Crypto.Util.number import *
from Crypto.Cipher import AES
ct = "68e934aa25be2c5f1674e101b31c25672400d69f9cf910a9f64071cea79f2de01d01bcf140105e5f7a3db66fffe64694"
enc = "030e150a0b0415110618111c001b0d1c"
iv = "1cb7942bf4ae14947150f9f196f92b2c"
ct = long_to_bytes(int(ct,16))
iv = long_to_bytes(int(iv,16))
ok = "okay"
key = b""
for i in range(0,len(enc),2):
	v = int(enc[i:i+2],16)^ord(ok[(i//2)%4])
	key += long_to_bytes(v)





cipher = AES.new(key,AES.MODE_CBC,iv)
flag = cipher.decrypt(ct)
if b"Tamil" in flag: print("CBC",flag)
cipher = AES.new(key,AES.MODE_CFB,iv)
flag = cipher.decrypt(ct)
if b"Tamil" in flag: print("CFB",flag)
cipher = AES.new(key,AES.MODE_OFB,iv)
flag = cipher.decrypt(ct)
if b"Tamil" in flag: print("OFB",flag)
cipher = AES.new(key,AES.MODE_OPENPGP,iv)
flag = cipher.decrypt(ct)
if b"Tamil" in flag: print("OPENPGP",flag)
cipher = AES.new(key,AES.MODE_EAX,iv)
flag = cipher.decrypt(ct)
if b"Tamil" in flag: print("EAX",flag)
cipher = AES.new(key,AES.MODE_GCM,iv)
flag = cipher.decrypt(ct)
if b"Tamil" in flag: print("GCM",flag)
