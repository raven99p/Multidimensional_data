from RandomWordGenerator import RandomWord
import progress.bar as br
import random
def generate(numOfWords,write=0):
	r = RandomWord()
	words = r.getList(numOfWords)
	copy = words
	if write ==1:
		bar = br.Bar('Generating Words',max = numOfWords)
		words = map(lambda x:x+'\n',words)
		with open("words.txt","w") as f:
			for x in words:
				f.write(x)
				bar.next()
		bar.finish()
	return copy
def generateW():
	r = RandomWord()
	return r.generate()
def generateCSV(numOfWords,write=0):
	generated=[]
	with open('words_csv.csv','w') as file:
		for x in range(numOfWords):
			key = random.randint(0,25000)
			value = random.randint(0,25000)
			generated.append([key,value])
			if write==1:
				file.write("%d,%d\n"%(key,value))
	return generated


generateCSV(10)