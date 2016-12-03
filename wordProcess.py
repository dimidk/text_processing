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


"""def findFile():
	
	tweetsFile=__init__.commonFilename+"tweets.txt"
	wikiFile=__init__.commonFilename+"wikipedia.txt"
	darwinFile=__init__.commonFilename+"darwin.txt"
	
	if os.path.isfile(tweetsFile):
		return tweetsFile
	elif os.path.isfile(wikiFile):
		return wikiFile
	elif os.path.isfile(darwinFile):
		return darwinFile
	else:
		return -1"""
	


def mostCommonFiles(word_dict,filename):

	
	fname=__init__.commonFilename+filename

	fh=codecs.open(fname,"w","latin-1")
	
	words=[(val,key) for key,val in word_dict.items()]
	words=sorted(words,reverse=True)

	for val,key in words:
		fh.write(key+":"+str(val)+"\n")
			
	fh.close()

	
def menuInFrequency():
	
	while True:
	
		print "1. File name to find common words"
		print "2. Show Diagram of most common words"
		print "3. Exit from frequency"
	
		epilogi=input()
		if epilogi==1:	
			fname=raw_input("File name is, otherwise press enter: ")
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
					
				"""common100=collection.most_common(100)
				common500=collection.most_common(500)
				common1000=collection.most_common(1000)"""
						
				mostCommonFiles(collection,fname)
			
				del wordsList,collection
			
		elif epilogi==2:
			while True:
				"""fname=raw_input("Δώσε το όνομα του αρχείου για την εκτύπωση του διαγράμματος:")"""
											
				num=input("Δώσε τον αριθμό των πιο συχνών λέξεων, διαφορετικά δώσε 0 :")
				filenum=__init__.findFile()
				if filenum[0]=='0' and filenum[1]=='0' and filenum[2]=='0':
					break
				if filenum[0]=='1' and filenum[1]=='0' and filenum[2]=='0':
					fname=__init__.tweetsFile
				elif filenum[0]=='0' and filenum[1]=='1' and filenum[2]=='0':
					fname=__init__.wikiFile
				elif filenum[0]=='0' and filenum[1]=='0' and filenum[2]=='1':
					fname=__init__.darwinFile
				else:
					print "more than one file for common words is created. Give file name:"
					fname=raw_input()
					fname=__init__.commonFilename+fname
					
				print "filenum is:", filenum
				print "you gave filename:",fname
				if num==0:
					break
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
		else:
			break
		
		"""del wordsList,collection,common100,common1000,common500"""
	

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
				
			menuInFrequency()
						
		elif epilogi==2:
			
			createCollect.menuCollection()
						
		else:
		
			calcWeightWords.weightFunction()
			
		

		
			
				

		

