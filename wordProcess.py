#! /usr/bin/python
# -*- coding: utf-8-*-

import nltk 
"""from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords"""
import __init__
import collections
import createTokens
import createCollect
import calcWeightWords
import codecs


def mostCommonFiles(word_dict,filename):

	fname="commonFile_"+filename

	fh=codecs.open(fname,"w","latin-1")
	
	words=[(val,key) for key,val in word_dict.items()]
	words=sorted(words,reverse=True)
	"""for w in words:"""
	for val,key in words:
		fh.write(key+":"+str(val)+"\n")
			
	fh.close()
	
	

if __name__ == '__main__':
	

	

	while True:
		print "1. Συχνότερα λεκτικά σύμβολα."
		print "2. Νόμος του Heap"
		print "3. Σημαντικοί όροι συλλογών"
		print "0. Έξοδος"
		epilogi=input()
		if epilogi==0:
			break
		if epilogi==1:
			while True:
				fname=raw_input("File name is, otherwise press enter: ")
				if fname=='' or fname==' ':
					break
				else:
					print "creating word list for file ..................."
					wordsList=createTokens.createTokensFromFile(fname)					
					collection=collections.Counter(wordsList)
					print "in a word list of : ",len(wordsList) ," we have a word dictionary of a:",len(collection)," words"
					
					common100=collection.most_common(100)
					common500=collection.most_common(500)
					common1000=collection.most_common(1000)
					
					mostCommonFiles(collection,fname)
					
					print "printing most 100 common words............"
					for key,val in common100:
						print key,val
					
					print "printing most 500 common words............"
					for key,val in common500:
						print key,val
					
					print "printing most 1000 common words............"
					for key,val in common1000:
						print key,val
					
					del wordsList,collection,common100,common1000,common500
					
		elif epilogi==2:
			
			createCollect.menuCollection()
						
		else:
		
			calcWeightWords.weightFunction()
			
		

		
			
				

		

