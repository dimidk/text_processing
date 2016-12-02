#!/usr/bin/python
# -*- coding: utf-8-*-


import nltk
"""from nltk.corpus import stopwords"""
from nltk.tokenize import word_tokenize
import __init__
import codecs
import collections
import time
import math
from nltk.stem.porter import *
import unicodedata

stemmer=PorterStemmer()

def strHasNum(myLine):
	return any(c.isdigit() for c in myLine)



def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def removeUrl(line):
	
	word=line.split()
	temp=word
	for w in temp:
		if w.startswith('https') or w.startswith('www') or w.startswith('http'):
			word.remove(w)
				
	return ' '.join(word)


def createContentList(fname):

	contents=[]	
	fh=codecs.open(fname,"r","latin-1")
	wh=codecs.open("contentfile.txt","w","latin-1")
	line=fh.readline()
	while True:

		if line.startswith("<http"):
			line=line.split('>')
			line=line[len(line)-1].split('@en')[0]
			line=removeUrl(line)	
			
			contents.append(line)
			wh.write(line+"\n")
						
		else:
			
			line=removeUrl(line)			
			contents.append(line)
			wh.write(line+"\n")
		line=fh.readline()
		if line=='':
			break
			
	fh.close()
	wh.close()
	return contents
	

def tokenizeFile(line,wordsList):
	
	for w in word_tokenize(line):
	
			if all(c in __init__.punctuation for c in w):
				continue
			elif strHasNum(w) or w.isdigit():
				continue
			elif any(c in __init__.punctuation for c in w):

				word=list(w.lower())
				word=[c for c in word if c not in __init__.punctuation]
			
				if len(word)>2:	
					"""print "word to add:",word"""
					wordsList.append(''.join(word))
			else:
				"""print "word to add without punctuation:",w.lower()"""
				w=strip_accents(w)
				if len(w)>2:
					wordsList.append(w.lower())
				
	return wordsList

	
def createTokensFromFile(fname):

	fh=codecs.open(fname,"r","latin-1")
	words=[]
	line=fh.readline()
	while True:

		if line.startswith("<http"):
			line=line.split('>')
			line=line[len(line)-1].split('@en')[0]
			
			if line.find('http')!=-1 or line.find('www')!=-1 or line.find('https')!=-1:
				line=removeUrl(line)
			
			words=tokenizeFile(line,words)
	
		else:
			
			if line.find('http')!=-1 or line.find('www')!=-1 or line.find('https')!=-1:
				line=removeUrl(line)		
			
			words=tokenizeFile(line,words)
		
		line=fh.readline()
		if line=='':
			break
			
	fh.close()
	return words



def tf_idf_word(wordsList,idf_words):
	
	"""make tuple witf tfidf, tf values"""
	
	tf_idf_dict={}

	tempc=collections.Counter(wordsList)
	for key,val in tempc.items():
		tf=round(float(val)/float(len(wordsList)),6)
		idf_val=idf_words[key]
		tfidf=round(tf*idf_val,6)
		tf_idf_dict[key]=(tfidf,tf)
	
	return tf_idf_dict


def idf_word(collection,collection_length):
	
	idf_stemmed=collections.Counter(collection)
	print "length of idf collection meaning unique words:",len(idf_stemmed)
	
	
	idf_words={}
	for key,val in idf_stemmed.items():
		idf_words[key]=round(math.log10(float(collection_length)/float(val)),8)
	
	print "printing idf values for terms......................"	
	return idf_words


def stem_words(wordsList):
	
	stemmed=[]
	for item in wordsList:
		stemmed.append(stemmer.stem(item))
	
	return stemmed


def createTokens(contents):
	
	words=[]
	i=0
	while i<len(contents):		
		line=contents[i]		
		words=tokenizeFile(line,words)
						
		i+=1
	
	return words

	
def createTokens(contents,idf_words,filename,tf_true):
	
	words=[]
	i=0
	
	if tf_true:
		
		while i<len(contents):		
			line=contents[i]		
	
			words_line=[]
			words_line=tokenizeFile(line,words_line)
			words_nostop=[w for w in words_line if w not in __init__.stop_words]
			words_line=stem_words(words_nostop)

			words.append(tf_idf_word(words_line,idf_words))
			
			i+=1
		
	else:
		while i<len(contents):		
			line=contents[i]		
			words=tokenizeFile(line,words)
						
			i+=1
	
	
	return words



if __name__== '__main__':
	
	filename=raw_input("Give file name: ")
	words_last=createTokensFromFile(filename)
	
	print words_last
