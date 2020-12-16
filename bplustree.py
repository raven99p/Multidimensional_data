Max_degree = 3
Max_contents = 2
Max_children = 3
order = 3
class Node:

	def __init__(self,is_leaf=False):
		self.keys = []
		self.pointers = []
		self.parent = None
		self.is_leaf = is_leaf

	def insert_at_leaf(self,leaf,key,pointer):
		if self.keys:
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
		print('inserted key',key,'inserted pointer',pointer)






class B:
	def __init__(self):
		self.root = Node()
		self.root.is_leaf = True


	def insert(self,key,pointer):
		old_node = self.search(key)
		old_node.insert_at_leaf(old_node,key,pointer)

		


	def search(self,key):
		cur_node = self.root
		print("This is the current node :) ")
		print(cur_node.keys)
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




tree = B()



tree.insert(6,16)
tree.insert(4,14)



tree.search(4)
