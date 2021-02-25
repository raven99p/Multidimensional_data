
import bloomfilter
import bplustree
from RandomWordGenerator import RandomWord
import randomWordGen as rndmW
import CosineSimilarity
import LSH
import math
# import lsh
if __name__ == '__main__':
	choice = 0
	print("""
 __       __  __    __  __     ________  ______        _______   ______  __       __  ________  __    __   ______   ______   ______   __    __   ______   __                                _______    ______
/  \     /  |/  |  /  |/  |   /        |/      |      /       \ /      |/  \     /  |/        |/  \  /  | /      \ /      | /      \ /  \  /  | /      \ /  |                              /       \  /      \
$$  \   /$$ |$$ |  $$ |$$ |   $$$$$$$$/ $$$$$$/       $$$$$$$  |$$$$$$/ $$  \   /$$ |$$$$$$$$/ $$  \ $$ |/$$$$$$  |$$$$$$/ /$$$$$$  |$$  \ $$ |/$$$$$$  |$$ |                              $$$$$$$  |/$$$$$$  |
$$$  \ /$$$ |$$ |  $$ |$$ |      $$ |     $$ | ______ $$ |  $$ |  $$ |  $$$  \ /$$$ |$$ |__    $$$  \$$ |$$ \__$$/   $$ |  $$ |  $$ |$$$  \$$ |$$ |__$$ |$$ |                              $$ |  $$ |$$ \__$$/
$$$$  /$$$$ |$$ |  $$ |$$ |      $$ |     $$ |/      |$$ |  $$ |  $$ |  $$$$  /$$$$ |$$    |   $$$$  $$ |$$      \   $$ |  $$ |  $$ |$$$$  $$ |$$    $$ |$$ |                              $$ |  $$ |$$      \
$$ $$ $$/$$ |$$ |  $$ |$$ |      $$ |     $$ |$$$$$$/ $$ |  $$ |  $$ |  $$ $$ $$/$$ |$$$$$/    $$ $$ $$ | $$$$$$  |  $$ |  $$ |  $$ |$$ $$ $$ |$$$$$$$$ |$$ |                              $$ |  $$ | $$$$$$  |
$$ |$$$/ $$ |$$ \__$$ |$$ |_____ $$ |    _$$ |_       $$ |__$$ | _$$ |_ $$ |$$$/ $$ |$$ |_____ $$ |$$$$ |/  \__$$ | _$$ |_ $$ \__$$ |$$ |$$$$ |$$ |  $$ |$$ |_____                         $$ |__$$ |/  \__$$ |
$$ | $/  $$ |$$    $$/ $$       |$$ |   / $$   |      $$    $$/ / $$   |$$ | $/  $$ |$$       |$$ | $$$ |$$    $$/ / $$   |$$    $$/ $$ | $$$ |$$ |  $$ |$$       |                        $$    $$/ $$    $$/
$$/      $$/  $$$$$$/  $$$$$$$$/ $$/    $$$$$$/       $$$$$$$/  $$$$$$/ $$/      $$/ $$$$$$$$/ $$/   $$/  $$$$$$/  $$$$$$/  $$$$$$/  $$/   $$/ $$/   $$/ $$$$$$$$/                         $$$$$$$/   $$$$$$/



""")

	while choice!=3:
		print("Please choose which part of the project you'd like to view")
		print("""1.Bloom Filters vs B+ Trees\n2.Min-Hash LSH vs Cosine LSH""")
		choice = int(input())
		if choice == 1:
			num = int(input("How many words do you wish to insert?\n"))
			rndmW.generate(num, 1)
			numOfQueries = int(input("how many queries do you wish to perform?\n"))
			bloomTime = bloomfilter.main(numOfQueries)
			print("Time for %d membership queries in a Bloom Filter is: %.7f" %(numOfQueries, bloomTime))
			rndmW.generateCSV( num)
			bplusTime = bplustree.main(numOfQueries)
			print("Time for %d membership queries in b+ Trees is: %.7f" % (numOfQueries, bplusTime))

		if choice == 2:
			#########################################################
			"""now we start with the b+ tree"""
			numOfArticles = int(input("How many articles do you wish to compare ? \n"))
			SimilarityMatrix1 = LSH.main(numOfArticles)
			cosine_similarity_matrix = CosineSimilarity.main(numOfArticles)
			print("The Cosine Similarity Method suggests: ")
			"""
			for x in range(len(cosine_similarity_matrix)):
				for y in range(len(cosine_similarity_matrix[x])):

					print("%.5f" % (cosine_similarity_matrix[x][y]), end=" ")
				pass
				print("")
			"""
			for x in range(0, len(cosine_similarity_matrix)):
				for y in range(1, len(cosine_similarity_matrix[x])):
					if(y<=x):
						print("     ", end=" ")
					else:
						print("%.3f"%(cosine_similarity_matrix[x][y]), end=" ")
				pass
				print("")
			print("While the LSH method:")
			for x in range(0, len(SimilarityMatrix1)):
				for y in range(1, len(SimilarityMatrix1[x])):
					if(SimilarityMatrix1[x][y] == math.inf):
						print("     ", end=" ")
					else:
						print(SimilarityMatrix1[x][y], end=" ")
				pass
				print("")
			print("The first Value of This matrix signifies the similarity between the first and second document, \nthe second one the similarity between the the first and the 3rd document and so on..\nValues that do not appear are articles that are not corelated\n")
			
		if choice==3:
			print("Goodbye!!!")


