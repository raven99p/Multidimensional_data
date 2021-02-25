from bitarray import bitarray 
import mmh3
import numpy as np
import progress.bar as br
import randomWordGen as r
import time
class bloom:
	def __init__(self,size):
		self.size = size



	def hashing(self,input,funcs):
		hashed = []
		hashed.append(mmh3.hash(str(input))%self.size)
		for i in range(1,funcs):
			hashed.append(mmh3.hash(str(hashed[i-1]))%self.size)
		return hashed

	def add(self,input):
		num = self.hashing(input,k)
		for i in num:
			a[i]=True

	def check(self,input):
		num = self.hashing(input,k)
		counter=0
		for i in num:
			if a[i] == True:
				counter+=1
		if counter != k:
			return False
		elif counter == k:
			return True
def main(numOfQueries):
	p = 10**(-7)
	with open("words.txt") as f:
		cont = f.read()
	cont = cont.split()
	n = int(len(cont))
	m = (-(n * np.log(p))/(np.log(2)**2))
	m = int(round(m))
	global k
	k = round((m/n) * np.log(2)) 
	global a
	print("p:",p,"n:",n,"m:",m,"k:",k)
	a = bitarray(m)
	bloom1 = bloom(m)
	bar = br.Bar('Read Words',max = n)
	for elem in cont:
		bloom1.add(str(elem))
		bar.next()
	bar.finish()
	print("\nFile read...\n")
	print("The number of words stored is: %d \nThe probability of a false positive occurence is: %f\nThe size of the bitarray is: %d positions"%(n,p,m))
	wordsToCheck = r.generate(numOfQueries)
	timeStart = time.time()
	for x in wordsToCheck:
		bloom1.check(x)
	timeEnd = time.time()
	return timeEnd - timeStart

if __name__ == '__main__':
	
	with open("words.txt") as f:
		cont = f.read()
	cont = cont.split()
	print(len(cont))
	p = 10**(-7)
	n = int(len(cont))
	m = (-(n * np.log(p))/(np.log(2)**2))
	m = int(round(m))
	print(m)
	print(p)
	bloom1 = bloom(m)
	bar = br.Bar('Read Words',max = n)
	for elem in cont:
		bloom1.add(str(elem))
		bar.next()
	print("\nFile read...\n")
	print("The number of words stored is: %d \nThe probability of a false positive occurence is: %f\nThe size of the bitarray is: %d positions"%(n,p,m))
	choice = 0
	while choice!=3:
		try:
			choice = int(input("What would you like to do now ? :\n1) Add another Element \n2) Check if word is in the filter \n3) Exit \n"))
		except:
			continue	
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
		
		print("=============================================================================")		
		pass


