#!/usr/bin/python
#-*- coding: utf-8-*-

from nltk import *
import nltk.text
"""from nltk.tokenize import word_tokenize
from nltk.corpus import stop_words"""
import __init__
import random
import codecs
import collections
import createTokens
import math
import time


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


def writeFile(Filename,contentList):
	
	fh=codecs.open(Filename,"w","latin-1")
	for w in contentList:
		fh.write(w +'\n')		
	
	fh.close()


def writeFileDict(Filename,wordDict):
	
	fh=codecs.open(Filename,"w","latin-1")
	for w,val in wordDict.items():
		fh.write(w + ":" + str(val) + '\n')		
	
	fh.close()


"""def make_Dictionary(collection,wordsList):
	
	wordsList=createTokens.createTokens(collection)
	time.sleep(0.2)
	
	word_dict={}
	for w in wordsList:
		word_dict[w]=word_dict.get(w,0)+1
	
	for key,value in word_dict.items():
		print key,value
	
	return word_dict,wordsList"""



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
				continue
			print "making contentList of file................................"
			contentList=createTokens.createContentList(fname)
			time.sleep(0.2)
			
			print "content list length:",len(contentList)
			print "content file created"
			time.sleep(0.2)
			print "end sleeping"
			
			fh.write("File with " + str(len(contentList)) + " contents" + "\n") 
			fh.write("Number of words in Vocabulary" + "\t" + "Number of words in content List" + "\n")
	
			for i in range(1,51):
				collection_10=make_Collection(contentList,10000)
				writeFile("coll10_"+str(i)+".txt",collection_10)
				wordsList=[]
				
				wordsList=createTokens.createTokens(collection_10)
				del collection_10
				words_dict=collections.Counter(wordsList)
				"""words_dict,wordsList=make_Dictionary(collection_10,wordsList)"""
				
				writeFile("coll10WordList_"+str(i)+".txt",wordsList)
				writeFileDict("coll10WordDict_"+str(i)+".txt",words_dict)
				
				print len(words_dict)," and number of words: ", len(wordsList)			
				fh.write(str(len(words_dict)) + "\t" + str(len(wordsList)) + "\n")				
				del words_dict,wordsList
				print "relaxing.............."
				time.sleep(0.5)
				
				collection_20=make_Collection(contentList,20000)
				writeFile("coll20_"+str(i)+".txt",collection_20)
				
				wordsList=[]
				wordsList=createTokens.createTokens(collection_20)
				words_dict=collections.Counter(wordsList)
				del  collection_20
				
				writeFile("coll20WordList_"+str(i)+".txt",wordsList)
				writeFileDict("coll20WordDict_"+str(i)+".txt",words_dict)
				
				print len(words_dict)," and number of words: ", len(wordsList)
				fh.write(str(len(words_dict)) + "\t" + str(len(wordsList)) +"\n")
				
				del wordsList,words_dict
				print "relaxing.............."
				time.sleep(0.5)

			collection_100=make_Collection(contentList,100000)
			writeFile("coll100.txt",collection_100)
			wordsList=[]
			
			wordsList=createTokens.createTokens(collection_100)
			words_dict=collections.Counter(wordsList)
			del collection_100
			writeFile("coll100WordList.txt",wordsList)
			writeFileDict("coll100WordDict.txt",words_dict)
			
			print len(words_dict), " and number of words: ", len(wordsList)
			fh.write(str(len(words_dict)) + "\t" + str(len(wordsList)) +"\n")
			
			del wordsList,words_dict
			fh.close()
			
			del contentList
			print "Relaxing a sec..............."
			time.sleep(1)
		else:
			print "read results.txt for calculating Heaps' Law"
			findHeapsLaw("results.txt")

		if num==0:
			break
	"""v v=K*n**b"""

