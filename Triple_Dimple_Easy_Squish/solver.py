#from Crypto.Cipher import AES
from Crypto.Cipher import DES3
from Crypto.Util.number import *
f = open("chall")
a = f.readlines()
ct = a[0].split()[-1]
key = a[1].split()[-1]
iv = a[2].split()[-1]
ct = long_to_bytes(int(ct,16))
print(ct)
key = long_to_bytes(int(key,16))
print(key)
iv = long_to_bytes(int(iv,16))
print(iv)
IV = iv*2
print()
cipher = DES3.new(key, DES3.MODE_CBC,iv)
print(cipher.decrypt(ct))
print()
cipher = DES3.new(key, DES3.MODE_CFB,iv)
print(cipher.decrypt(ct))
print()
cipher = DES3.new(key, DES3.MODE_OFB,iv)
print(cipher.decrypt(ct))
print()




"""
cipher = AES.new(key,AES.MODE_ECB)
print("ECB",cipher.decrypt(ct))
print()
cipher = AES.new(key,AES.MODE_CBC,IV)
print("CBC",cipher.decrypt(ct))
print()
cipher = AES.new(key,AES.MODE_CFB,IV)
print("CFB",cipher.decrypt(ct))
print()
cipher = AES.new(key,AES.MODE_OFB,IV)
print("OFB",cipher.decrypt(ct))
print()
cipher = AES.new(key,AES.MODE_CTR)
print("CTR",cipher.decrypt(ct))
print()
cipher = AES.new(key,AES.MODE_OPENPGP,IV)
print("OPEN",cipher.decrypt(ct))
print()
cipher = AES.new(key,AES.MODE_CCM,iv)
print("CCM",cipher.decrypt(ct))
print()
cipher = AES.new(key,AES.MODE_EAX)
print("EAX",cipher.decrypt(ct))
print()
cipher = AES.new(key,AES.MODE_GCM,iv)
print("GCM",cipher.decrypt(ct))
print()

KEY = key*2
cipher = AES.new(KEY[:32],AES.MODE_SIV,iv)
print("SIV",cipher.decrypt_and_verify(ct))
print()

cipher = AES.new(key,AES.MODE_OCB,iv)
print("OCB",cipher.decrypt(ct))
print()
"""
