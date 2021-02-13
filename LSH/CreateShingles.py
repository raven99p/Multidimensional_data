from sklearn.datasets import fetch_20newsgroups
import numpy as np


Doc_ready = 2
shingle_size = 5


# SHINGLES CREATION
categories = ['alt.atheism', 'soc.religion.christian',
              'comp.graphics', 'sci.med']
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

print('Creating Universe')
U = []
for i in range(Doc_ready):
    temp = unique(Doc[i])
    U.extend(temp)
print("length of U before unique",len(U))
U = unique(U)
print("length of U after unique",len(U))
###########################################

#Create Matrix 

global M
M = [[0]*Doc_ready]*len(U) 
print("Dimensions of M: ",len(M),"x",len(M[0]))

print(type(Doc[0]))
  

for i in range(Doc_ready):
    for j in range(len(U)):
        if U[j] in Doc[i]:
            print("---",U[j],"is in Doc[",i,"]")
            M[j][i] = 1
            print("M[",j,"][",i,"]->",M[j][i])
        else:
            print("---",U[j],"is not in Doc[",i,"]->")
            M[j][i] = 0
            print("M[",j,"][",i,"]->",M[j][i])
            

      
        
print(M[0][0])
print(M[1][0])





print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
    for row in M]))






