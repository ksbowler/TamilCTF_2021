f = open("pj_jp.txt")
a = f.readlines()
enc = a[-3].split()

for i in range(0,len(enc),8):
	temp = enc[i:i+8]
	val = 0
	#print(temp)
	val = ""
	for j in range(len(temp)):
		if temp[j] == "pj": val += "1"
		else: val += "0"
	#print(val)
	print(chr(int(val,2)),end="")
print()
