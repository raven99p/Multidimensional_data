import csv
Max_degree = 3
Max_contents = 2
Max_children = 3
order = 3


class Node:
    def __init__(self, is_leaf=True):
        self.keys = []
        self.pointers = []
        self.parent = None
        self.is_leaf = is_leaf
        self.next = None

    def insert_at_leaf(self, leaf, key, pointer):
        if self.keys:
            temp_keys = self.keys
            for i in range(len(temp_keys)):
                if(key == temp_keys[i]):
                    #print('they are equal, inserted at the right')
                    self.pointers.insert(i+1, pointer)
                    break
                elif(key < temp_keys[i]):
                    #print('key<temp key, inserted at the left')
                    self.keys.insert(i, key)
                    self.pointers.insert(i, pointer)
                    break
                elif(i+1 == len(temp_keys)):
                    #print('key is greater that all , inserted at the right')
                    self.keys.append(key)
                    self.pointers.append(pointer)
                    break
            #print('inserted key', key, 'inserted pointer', pointer)
            #print('to node ',temp_keys)
        else:
            self.keys.append(key)
            self.pointers.append(pointer)

    def show(self, counter=0):
        """Prints the keys at each level."""
        print(counter, str(self.keys))
        #print(counter, str(self.pointers))

        # Recursively print the key of child nodes (if these exist).
        if not self.is_leaf:
            for item in self.pointers:
                item.show(counter + 1)

    

        
class B:
    def __init__(self):
        self.root = Node()
        self.root.is_leaf = True

    def insert(self, key, pointer):
        old_node = self.search(key)
        old_node.insert_at_leaf(old_node, key, pointer)
        #print('BEFORE')
        #self.root.show()
        #print('-------------------------------')
        if (len(old_node.keys) == order):
            #print('CALLING SPLIT', old_node.keys)

            #if temp != None:
                #print('MERGING TO:', temp.keys)
            self.split(old_node)

            flag = 0
            while old_node.parent and not flag:
                cur_node = old_node.parent
                if cur_node.keys == order:
                    self.split(cur_node)
                    cur_node = cur_node.parent                     
                else:
                    flag = 1
                
            #print('AFTER')
            #self.root.show()
            #print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    def split(self, node):
        #print('SPLITTING')
        #print('CHILDREN KEYS',node.keys)
        #print('CHILDREN POINTERS',node.pointers)
        left = Node()
        right = Node()
        mid = order // 2
        left.keys = node.keys[:mid]
        left.pointers = node.pointers[:mid]
        
        #print('these are the left keys', left.keys)
        right.keys = node.keys[mid:]
        #print('these are the right keys', right.keys)
        right.pointers = node.pointers[mid:]

        if(node.is_leaf!=True):
            left.is_leaf=False
            right.is_leaf=False

        
        #print('LEFT',left)
        #print('LEFT KEYS',left.keys)
        #print('LEFT POINTERS',left.pointers)
        #print()
        #print('RIGHT',right)
        #print('RIGHT KEYS',right.keys)
        #print('RIGHT POINTERS',right.pointers)
        if node == self.root:
            left.parent = node
            right.parent = node
        else:
            left.parent = node.parent
            right.parent = node.parent
        # When the node is split, set the parent key to the left-most key of the right child node.
        node.keys = [right.keys[0]]
        #print('this the old node key',old_node.keys)
        node.pointers = [left, right]
        node.is_leaf = False
        # print(old_node.parent)
        if node.parent != None:
            self.merge(node)

            


            
    def merge(self, node):
        #print('ME:', node.keys)
        Parent = node.parent
        #print('MERGING TO :', Parent.keys)
        index = 0
        for i in range(len(Parent.keys)):
            if node.keys[0] < Parent.keys[i]:
                index = i
                #print('INSERTED AT THE LEFT OF',Parent.keys[i])
                break
            else:
                index = len(Parent.keys) - 1
        Parent.keys.insert(index, node.keys[0])
        #print('MERGED:',Parent.keys)
        Parent.pointers[index:index+1]=node.pointers
        #print('POINTERS',Parent.pointers)
        if Parent==self.root and len(Parent.keys)==order:
            #print('SPLITTING ROOT')
            #print('ROOTS CHILDREN BEFORE',Parent.pointers)
            self.split(Parent)
            #print('ROOTS CHILDREN AFTER',Parent.pointers)
            #print('CHILD',node)
            #print('GRAND CHILDREN',node.pointers)




    def search(self, key):
        cur_node = self.root
        #print('this is my parent status',cur_node.is_leaf)
        #print('this is the key:',key)
        i = 0
        #print("This is the current node:",cur_node.keys)
        while(cur_node.is_leaf == False):
           # print('this is the length of the keys----------------------:',len(cur_node.keys))
            #print('this is the length of the pointers------------------:',len(cur_node.pointers))
            temp2 = cur_node.keys
            for i in range(len(temp2)):
                if key < temp2[i]:
                    cur_node = cur_node.pointers[i]
                    break
                elif i+1 == len(temp2):
                    cur_node = cur_node.pointers[i+1]
                    break
        return cur_node


Tree = B()

with open("words_csv.csv") as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        Tree.insert(int(row[0]), row[1])
Tree.root.show()






