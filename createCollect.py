#!/usr/bin/python
#-*- coding: utf-8-*-

"""read lines from file and make a list. Then choose contents from the list randomly 10000 and 20000 contents
how to throw out https which is meaningless and # to keep after the #
one idea is to process file at once and throw out these, the other to process list of lines.
This must be done in the first procession too."""

import nltk
"""from nltk.tokenize import word_tokenize
from nltk.corpus import stop_words"""
import __init__
import random
import codecs
import createTokens
import math


def make_Collection(contentsList,number):
	
	makeCollection=random.sample(contentList,number)
	
	return makeCollection


def findHeapsLaw(resultsName):
	
	fh=codecs.open(resultsName,"r")
	lines=fh.readlines()
	for line in lines:
		numbers=line.split('\t')
		if not numbers[0].isdigit():
			continue

		numbers=line.split('\t')
		print numbers
		v=float(numbers[0])
		n=float(numbers[1])

		"""v=k*n**b"""
		
		b=random.random()
		print "random b: ",b
		k=v/math.pow(n,b)
		print "for v", v , " have a K:",k, " for a n**b:",math.pow(n,b)," and a b:",b," \n"
		
	fh.close()

		

def make_Dictionary(collection,wordsList):
	
	wordsList=createTokens.createTokens(collection)
	word_dict={}
	for w in wordsList:
		word_dict[w]=word_dict.get(w,0)+1
	
	return word_dict,wordsList



if __name__=='__main__':
		
	while True:
		print "1.create collection"
		print "2. calculate V=Kn**b"
		print "0. exit"

		num=input()
		if num==1:
			fh=open("results.txt","w")
			fname=raw_input("give file name, otherwise 0:")
			if fname=='0':
				break
			print "making contentList of file................................"
			contentList=createTokens.createContentList(fname)
			print len(contentList)
			fh.write("File with " + str(len(contentList)) + " contents" + "\n") 
			fh.write("Number of words in Vocabulary" + "\t" + "Number of words in content List" + "\n")
	
			for i in range(1,50):
				collection_10=make_Collection(contentList,10000)
				wordsList=[]
				words_dict,wordsList=make_Dictionary(collection_10,wordsList)
				print len(words_dict)," and number of words: ", len(wordsList)			
				fh.write(str(len(words_dict)) + "\t" + str(len(wordsList)) + "\n")				

				collection_20=make_Collection(contentList,20000)
				wordsList=[]
				words_dict,wordsList=make_Dictionary(collection_20,wordsList)
				print len(words_dict)," and number of words: ", len(wordsList)
				fh.write(str(len(words_dict)) + "\t" + str(len(wordsList)) +"\n")

			collection_100=make_Collection(contentList,100000)
			wordsList=[]
			words_dict,wordsList=make_Dictionary(collection_100,wordsList)
			print len(words_dict), " and number of words: ", len(wordsList)
			fh.write(str(len(words_dict)) + "\t" + str(len(wordsList)) +"\n")
		
			fh.close()
		else:
			print "read results.txt for calculating Heaps' Law"
			findHeapsLaw("results.txt")

		if num==0:
			break
	"""v v=K*n**b"""

