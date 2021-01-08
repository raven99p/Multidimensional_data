from bitarray import bitarray 
import mmh3
import numpy as np
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


with open("words.txt") as f:
	cont = f.read()
cont = cont.split()
print(len(cont))
n = int(len(cont))
m = (-(n * np.log(p))/(np.log(2)**2))
m = int(round(m))
print(m)
#(1 - (1 - (1/m))**(k*n))**k
print(p)
bloom1 = bloom(m)
for elem in cont:
	bloom1.add(str(elem))
print("File read...\n")

choice = 0
while choice!=3:
	choice = int(input("What would you like to do now ? :\n 1) Add another Element \n2) Check if word is in the filter \n3) Exit \n"))
	if choice == 1:
		word = str(input("Please give me the word you want to store :\n"))
		bloom1.add(word)
		n = n + 1
		print("The word has been added!")
		pass
	if choice == 2:
		word = str(input("Please give me the word you want to search for :\n"))
		if bloom1.check(word):
			print("The word is contained in the filter with a probability of p = %f \n"%((1 - (1 - (1/m))**(k*n))**k))
		else:
			print("The word is definetly not contained in the filter \n")
	if choice == 3:
		print("Thanks for playing!! \n")
		pass

	pass


