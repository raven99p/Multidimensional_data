import csv
import randomWordGen as r
import time
Max_degree = 3
Max_contents = 2
Max_children = 3
order = 3
class Node:

	def __init__(self,is_leaf=False):
		self.keys = []         #keys to be used for comparisons furing search and insertion
		self.pointers = []	   #pointers to the child nodes or the actual data
		self.parent = None     #parent pointer for backtracking
		self.is_leaf = is_leaf #is_leaf boolean that is true only for the leafs of the b+ Tree

	def insert_at_leaf(self,leaf,key,pointer):    #This function compares keys and inserts a new value 
		if self.keys:                             #in the right place in the leaf by appending it.
			temp_keys = self.keys
			for i in range(len(temp_keys)):
				if(key == temp_keys[i]):
					self.pointers.insert(i+1,pointer)
					break
				elif(key<temp_keys[i]):
					self.keys.insert(i,key)
					self.pointers.insert(i,pointer)
					break
				elif(i+1 == len(temp_keys)):
					self.keys.append(key)
					self.pointers.append(pointer)
					break
		else:
			self.keys.append(key)
			self.pointers.append(pointer)
		






class B:
	def __init__(self):
		self.root = Node()    #keep track of the root of the Tree
		self.root.is_leaf = True #Initialised because root is leaf when created


	def insert(self,key,pointer): #Using the search function to get the node at which we should insert
		old_node = self.search(key)#The given value
		
		old_node.insert_at_leaf(old_node,key,pointer)

		


	def search(self,key): #Search returns the leaf node which contains the key or the node that the key
		cur_node = self.root#should be inserted
		
		while(cur_node.is_leaf == False):
			temp2 = cur_node.keys
			for i in range(len(temp2)):
				if key == temp2[i]:
					cur_node = cur_node.pointers[i+1]
					break
				elif key < temp2[i]:
					cur_node = cur_node.pointers[i]
					break
				elif i+1 == len(temp2):
					cur_node = cur_node.pointers[i+1]
					break
		return cur_node

	def check(self,key,value): #This function uses search to check if the value exists inside the Tree
		old_node = self.search(key)
		if key in old_node.keys:
			return True
		else:
			return False

def main(numOfQueries):
	keys = []
	pointers = []
	with open('words_csv.csv') as csv_file:#we read the csv file and for every key,value pair we insert
	    csv_reader = csv.reader(csv_file, delimiter=',')
	    line_count = 0
	    for row in csv_reader:
	        if line_count == 0:
	            print(f'Column names are {", ".join(row)}')
	            line_count += 1
	        else:
	            keys.append(int(row[0]))
	            pointers.append(row[1])
	            line_count += 1
	tree = B() #we create the Tree
	for i in range(len(keys)):
	    tree.insert(keys[i],pointers[i])  #and we insert
	timeStart = time.time() #start the timer for the membership queries
	numsToCheck = r.generateCSV(numOfQueries)
	for x,y in numsToCheck:
		tree.check(x,y)
	timeEnd = time.time() #stop the timer
	return timeEnd - timeStart #return the time elapsed


if __name__ == '__main__':	
	keys = []
	pointers = []
	with open('words_csv.csv') as csv_file:
	    csv_reader = csv.reader(csv_file, delimiter=',')
	    line_count = 0
	    for row in csv_reader:
	        if line_count == 0:
	            print(f'Column names are {", ".join(row)}')
	            line_count += 1
	        else:
	            keys.append(int(row[0]))
	            pointers.append(row[1])
	            line_count += 1
	    print(f'Processed {line_count} lines.')
	"""
	with open("numbers.txt") as f:
	    cont = f.read()
	cont = cont.split()
	keys = int(cont[0::2])
	pointers = cont[1::2]
	"""
	#creating tree and inserting content of text
	tree = B()
	for i in range(len(keys)):
	    tree.insert(keys[i],pointers[i])
	tree.search(4)
	print(tree.check(4,124))
