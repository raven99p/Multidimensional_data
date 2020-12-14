from bitarray import bitarray 
import mmh3
k = 4 
m = 2415459
p = 0.1
a = bitarray(m)
class bloom:
	def __init__(self,size):
		self.size = size



	def hashing(self,input):
		hashed = []
		hashed.append(mmh3.hash(str(input))%self.size)
		hashed.append(mmh3.hash(str(hashed[0]))%self.size)
		hashed.append(mmh3.hash(str(hashed[1]))%self.size)
		hashed.append(mmh3.hash(str(hashed[2]))%self.size)
		return hashed

	def add(self,input):
		num = self.hashing(input)
		for i in num:
			a[i]=True

	def check(self,input):
		num = self.hashing(input)
		counter=0
		for i in num:
			if a[i] == True:
				counter+=1
		if counter != k:
			return False
		elif counter == k:
			return True

bloom1 = bloom(2415459)
bloom1.add("paulinho")
print(bloom1.check("paulisdf"))
