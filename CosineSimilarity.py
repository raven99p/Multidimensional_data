from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.datasets import fetch_20newsgroups
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import math
categories = ['alt.atheism']
""", 'soc.religion.christian',
              'comp.graphics', 'sci.med']"""
temp = fetch_20newsgroups(
    subset='train', categories=categories, shuffle=False, random_state=42)

def main(numOfArticles):
	documents = [temp.data[i] for i in range(numOfArticles)]
	# Create the Document Term Matrix
	count_vectorizer = CountVectorizer(stop_words='english')
	count_vectorizer = CountVectorizer()
	sparse_matrix = count_vectorizer.fit_transform(documents)

	# OPTIONAL: Convert Sparse Matrix to Pandas Dataframe if you want to see the word frequencies.
	doc_term_matrix = sparse_matrix.todense()


	cosine_similarity_matrix = []
	#print(cosine_similarity_matrix)
	res = 0
	res2 = 0




	#print(str(doc_term_matrix[0]).split(),doc_term_matrix[1])
	for x in range(len(doc_term_matrix)):
		listone = doc_term_matrix[x].tolist()
		res = 0
		for i in range(len(listone[0])):
				res += int(listone[0][i])**2
		set_list=[]
		for y in range(len(doc_term_matrix)):
			dot = doc_term_matrix[x].dot(doc_term_matrix[y].T)
			listtwo = doc_term_matrix[y].tolist()
			res2 = 0
			for i in range(len(listtwo[0])):
				res2 += int(listtwo[0][i])**2
				pass
			sim = int(dot)/(math.sqrt(int(res))*math.sqrt(int(res2)))
			set_list.append(sim)
		cosine_similarity_matrix.append(set_list)
		pass
	return cosine_similarity_matrix
	"""
	for x in range(len(cosine_similarity_matrix)):
		for y in range(len(cosine_similarity_matrix[x])):
			
			print("%.5f"%(cosine_similarity_matrix[x][y]),end=" ")
		pass
		print("")
	
	#print(cosine_similarity(doc_term_matrix,doc_term_matrix))

	for x in range(0,len(cosine_similarity_matrix)):
		for y in range(0,x):
			print(cosine_similarity_matrix[x][y],end=" ")
			pass
		print("")
"""

                