from sklearn.datasets import fetch_20newsgroups
import numpy as np # to get unique shhingles of list
import random # to get permutations of Matrix
import math # infinity
import collections # check if signature parts, contain same elements
Doc_ready = 40
shingle_size = 5


# SHINGLES CREATION
categories = ['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med']

temp = fetch_20newsgroups(
    subset='train', categories=categories, shuffle=False, random_state=42)
Doc = []


for i in range(Doc_ready): # for every document
    File = temp.data[i].replace('\n','')
    File = File.replace('\t', '')
    shingles = []
    sets = ''
    for x in range(len(File)-shingle_size):
        for y in range(shingle_size):
            sets= sets + File[x+y]
        shingles.append(sets)
        sets = ''    
    Doc.append(shingles)

# Now Doc contains in every cell, the shingles of every file. #
# Doc[]=Shingles of single document, 
#    [][]=Shingle of shingles of single document
#first index is also the id of the document


###########################################


def unique(list_arg): #get unique elements from List
    x = np.array(list_arg)
    return np.unique(x)

#Create Universe of Sets

#print('Creating Universe')
U = []
for i in range(Doc_ready):
    Doc[i] = unique(Doc[i])
    temp = unique(Doc[i])
    U.extend(temp)
#print("length of U before unique",len(U))
U = unique(U)
print("length of U after unique",len(U))

###########################################

#Create Matrix 

M = [[0 for x in range(Doc_ready)] for y in range(len(U))] 
#print("Dimensions of M: ",len(M),"x",len(M[0]))

for i in range(Doc_ready):
    for j in range(len(U)):
        if U[j] in Doc[i]:
            #print("---",U[j],"is in Doc[",i,"]")
            M[j][i] = 1;
            #print("M[",j,"][",i,"]->",M[j][i])
            continue
        else:
            #print("---",U[j],"is not in Doc[",i,"]->")
            M[j][i] = 0;
            #print("M[",j,"][",i,"]->",M[j][i])
            continue
"""
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
    for row in M]))"""

print("Characteristic Matrix create")

####################
#Creating the Hash functions

#Find first prime greater than the number of unique shingles

def findPrime(N):
    while True:
        if isPrime(N):
            return N
        else:
            N = N + 1
            
def isPrime(n):
    d = n - 1
    s = 0
    while not d & 1:
        s += 1
        d >>= 1
    for a in (2, 13, 23, 1662803):
        if pow(a, d, n) != 1 and all(pow(a, (1 << r) * d, n) != n - 1 for r in range(0, s)):
            return False
    return True

#####



hash_number = 200 # number of hash functions

hash_table = [[0 for x in range(2)] for y in range(hash_number)] 

size_of_U = 4604

p = findPrime(size_of_U) # prime number

# Filling hash_table with random numbers from [-100.000,100.000] 

print("this is p",p)
for i in range(2):
    for j in range(hash_number):
        hash_table[j][i]= random.randint(-100000,100000)

#hi(x) = (ai*x + bi) % p

def hashF(r,c,sig): 
    for i in range(hash_number):
        h = ( hash_table[i][0] * r + hash_table[i][1] ) % p 
        if h < sig[i][c]:
            sig[i][c] = h 

################################

# Creating Signature Matrix 


Sig = [[math.inf for x in range(Doc_ready)] for y in range(hash_number)] 



print("Created Signature Matrix")

for i in range(Doc_ready):
    for j in range(len(U)):
        if M[j][i]==1 :
            hashF(j,i,Sig)

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
    for row in Sig]))



#####################


# LSH 

b=50
r = len(Sig)//b



k = [[0 for x in range(Doc_ready)] for y in range(Doc_ready)]


def hash(temp_list):
    h = 0
    #print("this is the temp list",temp_list,h)
    for i in range(0,r):
        h = h + (i+1)*temp_list[i]
    h = h%len(k)
    #print(h)
    return h


def getC( start, col, sig ):
    temp = []
    for i in range(start, start + r):
        temp.append(sig[i][col])
    #print(temp)
    return temp

for j in range(b):
    start=0
    while start<Doc_ready:
        
        curr = getC(r*j,start,Sig)
        #print("this is the current column",curr)
        
        for i in range(start,Doc_ready):
            #print("compairing current column with:",getC(3*j,i,Sig),"-->",collections.Counter(curr) == collections.Counter(getC(3*j,i,Sig)))
            if collections.Counter(curr) == collections.Counter(getC(r*j,i,Sig)):
                k[start][i]=1
        start=start+1

print("------------------------------------------------------------")
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
    for row in k]))




