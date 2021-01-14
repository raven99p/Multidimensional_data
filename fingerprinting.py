import hashlib as hlb
from sklearn.datasets import fetch_20newsgroups
import mmh3
dochash = []

"""
	for word in cont.split():

		dochash.append(bin(int(hlb.md5(word.encode()).hexdigest(),16))[2:])
for x in range(len(dochash)):
	print("Place i= %d with num %s whose length is %d"%(x,dochash[x],len(dochash[x])))
for x in range(127):
	colsum = 0
	for y in dochash:
		colsum = colsum + int(y[x])
	pass
"""
"""
a = hashlib.md5('alsdkfjasldfjkasdlf')
b = a.hexdigest()
as_int = int(b, 16)
print bin(as_int)[2:]
# 1111000011001000110011101011100101101010101111000101000001101001001010011110
"""
cont = open("test.txt","r").read()
categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
print("fetching")
temp = fetch_20newsgroups(subset='train',categories=categories, shuffle=False, random_state=42)
#cont = temp.data[10]
cont = cont.split()
shingles = []
for x in range(len(cont)-9):
	string = ""
	for y in range(9):
		string = string + cont[x+y] + " "
	shingles.append(string)
print("any")
print(*shingles,sep="\n")

