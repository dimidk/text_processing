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
							
				mostCommonFiles(collection,fname)
			
				del wordsList,collection
			
		elif epilogi==2:
			while True:
										
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
			
		

		
			
				

		

