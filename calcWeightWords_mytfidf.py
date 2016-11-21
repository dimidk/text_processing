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


"""for w in word:
			if w in punctuation:
				print True
			else:
				print False"""

"""using class TextCollection and tf, idf, tf_idf methods"""


stop_words=set(stopwords.words('english'))

""" !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ """


def removeUseless(line):
	
	print "line before x number:", lineinfo
	word=line.split('\\x')
	
	


def createStemmed(fname,stemmer):
	
	
	word_list=createTokens.createTokensFromFile(fname)
			
	words=[w for w in word_list if w not in stop_words ]
	
	stemmed=[]
	for item in words:
		stemmed.append(stemmer.stem(item))
	
	return stemmed
	
			
def tf_word(wordsList):
	
	tf_dict=collections.Counter(wordsList)
	wordsCount=len(tf_dict)
	for key,val in tf_dict.items():
		tf_dict[key]=val/wordsCount
	
	return tf_dict

def idf_word(collection):

	idf_dict=collections.Counter(collection)
	for key,val in idf_dict.items():
		idf_dict[key]=math.log10(len(collection)/val)
	
	return idf_dict

def tf_idfword(idf_dict,tf_dict):
	
	tfidf_dict={}
	for key,val in idf_dict.items():
		if tf_dict.has_key(key):
			tfValue=tf_dict[key]
			tfidf_dict[key]=tfValue*val
	
	return tfidf_dict	


if __name__ == '__main__':

	stemmer=PorterStemmer()

	while True:
		fname=raw_input("Give filename, or 0: ")
		
		if fname=='0':
			break
				
		if fname!='0':
			fname1=fname
			text1=createStemmed(fname,stemmer)
		else:
			continue
		time.sleep(0.5)
		
		fname=raw_input("Give filename, or 0: ")
		if fname!='0':
			fname2=fname
			text2=createStemmed(fname,stemmer)
		else:
			continue
		time.sleep(0.5)
		
		fname=raw_input("Give filename, or 0: ")
		if fname!='0':
			fname3=fname
			text3=createStemmed(fname,stemmer)
		else:
			continue
		time.sleep(0.5)
		
		print "making text collection...................."
		collection=[text1,text2,text3]
		
		print "making tf-idf for each word in ",fname1
		tf_text1=tf_word(text1)		
		"""tf_text1=collections.Counter(text1)"""
		print "relaxing......................"
		time.sleep(1)
		
		print "making tf-idf for each word in ",fname2
		tf_text2=tf_word(text2)
		print "relaxing......................"
		time.sleep(1)
		
		print "making tf-idf for each word in ",fname3
		tf_text3=tf_word(text3)
		print "relaxing......................"
		time.sleep(1)
		
		print "making idf for each word in collection"
		idf_collection=idf_word(collection)
		print "relaxing......................"
		time.sleep(1)
	
		del text3,text2,text1,collection
		print "relaxing......................"
		time.sleep(1)
		
		print "printing tf for: ",fname1
		for key,val in tf_text1.items():
			print key,val
		
