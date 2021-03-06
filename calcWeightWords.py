#!/usr/bin/python
# -*- coding:utf-8-**
	
import nltk
import string
import math
from nltk import word_tokenize
from nltk import text
import collections
from nltk.corpus import stopwords
from nltk.stem.porter import *
import codecs
import __init__
import createTokens
import time


"""using class TextCollection and tf, idf, tf_idf methods"""
""" testing github"""

stop_words=set(stopwords.words('english'))

""" !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ """

"""create a list of dictionaries containing the tf's for each word in 
each document. consider that the document is each new paragraph in file 
ending by @"""

def createStemmed(fname,stemmer):
	

	word_list=createTokens.createTokensFromFile(fname)
			
	words=[w for w in word_list if w not in stop_words ]
	
	stemmed=[]
	for item in words:
		stemmed.append(stemmer.stem(item))
	
	return stemmed
	


def createFiles1(tf_list,idf_words,filename):
	
	fname="tfidf_dict_"+filename
	
	fh=codecs.open(fname,"w","latin-1")
	fh.write("write the tfidf, tf and idf values in dictionary\n")
	for val,key in tf_list:
		"""print key,val"""
		fh.write(key+"\t"+str(val[0])+"\t"+str(val[1])+"\t")
		fh.write(str(idf_words[key])+"\n")
	
	fh.close()
	
	
def printMostImportant(tfidf_dict,number):
	
	counter=0
	if type(tfidf_dict) is list:
		print "Term \t tfidf value \t tf value\n"
		for val,key in tfidf_dict:
			if counter==number:
				break
			print key,"\t",val[0],"\t",val[1]
			counter+=1
						
	else:
		print "Term \t tfidf value \t tf value\n"		
		for val,key in tfidf_dict.items():			
			if counter==number:
				break
			print key,"\t",val[0],"\t",val[1]
			counter+=1

def mostImportant(tfidf_dict):
	
	tfidf_dictList=[]
	
	if type(tfidf_dict) is list:
		for t in tfidf_dict:
			for key,val in t.items():
				tfidf_dictList.append((val,key))
						
	else:
					
		tfidf_dictList=[(val,key) for key,val in tfidf_dict.items()]
		
	tfidf_dictList=sorted(tfidf_dictList,reverse=True)
	
	return tfidf_dictList




"""if __name__ == '__main__':"""


def weightFunction():

	
	stemmer=PorterStemmer()
	counter=0
	while True:
		print "Give file names for calculating tf-idf values, or press 0 or enter:\n"
		fname=raw_input("Give file name:")
		
		if fname=='0' or fname=='':
			break
	
		if fname=='darwin.txt':
			fname1=fname
			stem_words=createStemmed(fname,stemmer)
			
		
		if fname=='wikipedia.txt':
			fname2=fname
			wordsList_wiki=createTokens.createContentList(fname)
			stemmed_wiki=createStemmed(fname,stemmer)
			
			
		if fname=='tweets.txt':
			fname3=fname
			wordsList_tweets=createTokens.createContentList(fname)
			stemmed_tweets=createStemmed(fname,stemmer)
						
	collection=stem_words+stemmed_tweets+stemmed_wiki
	collection_length=len(wordsList_tweets)+len(wordsList_wiki)+1
	
	print "length of stem collection:", len(collection)
	print "length of each stemmed file wiki,tweets,darwin:",len(stemmed_wiki),len(stemmed_tweets),len(stem_words)

	time.sleep(2)
	print "making idf for each term............."
	idf_words=createTokens.idf_word(collection,collection_length)
	del stemmed_tweets,stemmed_wiki,collection
	
	
	print "making tf and tfidf list for ",fname1
	tf_list_fname1=createTokens.tf_idf_word(stem_words,idf_words)
	
	print "make list in descending order for ",fname1
	tfidfListR=mostImportant(tf_list_fname1)

	del tf_list_fname1,stem_words

	print "printing the 10 important words in ", fname1
	print "Term : tf-idf Value\n"
	printMostImportant(tfidfListR,10)
	"""print tfidfListR[:10]"""
	
	print "printing the 100 important words in ", fname1
	print "Term : tf-idf Value\n"
	printMostImportant(tfidfListR,100)
	"""print tfidfListR[:100]"""
	
	createFiles1(tfidfListR,idf_words,fname1)
	
	print "making tf and tfidf list for ",fname2
	tf_list_fname2=createTokens.createTokens(wordsList_wiki,idf_words,fname2,True)
	del wordsList_wiki,tfidfListR
	
	print "make list in descending order for ",fname2
	tfidfListR=mostImportant(tf_list_fname2)
	
	del tf_list_fname2

	print "printing the 10 important words in ", fname2
	print "Term : tf-idf Value\n"
	printMostImportant(tfidfListR,10)
	"""print tfidfListR[:10]"""
	
	print "printing the 100 important words in ", fname2
	print "Term : tf-idf Value\n"
	printMostImportant(tfidfListR,100)
	"""print tfidfListR[:100]"""
	createFiles1(tfidfListR,idf_words,fname2)
	
	del tfidfListR
	
	print "making tf and tfidf list for ",fname3
	tf_list_fname3=createTokens.createTokens(wordsList_tweets,idf_words,fname3,True)
	del wordsList_tweets
	
	print "make list in descending order for ",fname3
	tfidfListR=mostImportant(tf_list_fname3)
	
	
	del tf_list_fname3

	print "printing the 10 important words in ", fname3
	print "Term : tf-idf Value\n"
	printMostImportant(tfidfListR,10)
	"""print tfidfListR[:10]"""
	
	print "printing the 100 important words in ", fname3
	print "Term : tf-idf Value\n"
	printMostImportant(tfidfListR,100)
	"""print tfidfListR[:100]"""
	createFiles1(tfidfListR,idf_words,fname3)
	
	del tfidfListR,idf_words
			
	
