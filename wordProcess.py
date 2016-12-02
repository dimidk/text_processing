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
import testDiagram


def mostCommonFiles(word_dict,filename):

	fname="commonFile_"+filename

	fh=codecs.open(fname,"w","latin-1")
	
	words=[(val,key) for key,val in word_dict.items()]
	words=sorted(words,reverse=True)

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
				fname=raw_input("File name process to find common words is, otherwise press enter: ")
				try:
					fh=codecs.open(fname,"r",encoding='utf-8')
				except IOError as e:
					print "I/O ({0}):{1}".format(e.errno,e.strerror)
					break
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
					
					while True:
						print "Show most common words in file and diagram. Show 100 most common, or 500 or 1000 most common"
						num=input("Give maximun of words number:")
						if num==100:
							print "printing diagram with 100 most common..."
							testDiagram.plotCommonWords(fname,num)	
						elif num==500:
							print "printing diagram with 500 most common..."
							testDiagram.plotCommonWords(fname,num)
						elif num==1000:
							print "printing diagram with 1000 most common..."
							testDiagram.plotCommonWords(fname,num)
						else:
							break
					
					del wordsList,collection,common100,common1000,common500
					
		elif epilogi==2:
			
			createCollect.menuCollection()
						
		else:
		
			calcWeightWords.weightFunction()
			
		

		
			
				

		

