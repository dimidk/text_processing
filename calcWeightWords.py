#!/usr/bin/python
# -*- coding:utf-8-**

	
import nltk
import string
from nltk import word_tokenize
from nltk.corpus import stopwords
import codecs
import __init__
import createTokens


stop_words=set(stopwords.words('english'))
punctuation=list(string.punctuation)

def createWordsList(fname):
	
	word_list=[]	
	fh=codecs.open(fname,"r","latin-1")
	lines=fh.readlines()
	for line in lines:
		
		if line.startswith("<http"):
			line=line.split('>')
			line=line[len(line)-1].split('@en')[0]
			line=line.split()
			i=0
			while i<len(line):
				if line[i].find('\u')!=-1 or line[i].find('//')!=-1:
					line.pop(i)
				i+=1
			line=' '.join(line)
			"""print line"""
			for w in word_tokenize(line):
				if w not in stop_words and not createTokens.strHasNum(w) and not w.isdigit() and w not in punctuation:
					word_list.append(w)
			"""word_list.append([w.lower() for w in word_tokenize(line) if w not in stop_words and not createTokens.strHasNum(w) and not w.isdigit() and w not in punctuation])"""
		else:
			line=line.split('http')
			i=0
			while i<len(line):
				if line[i].find('\u')!=-1 or line[i].find('//')!=-1:
					line.pop(i)
				i+=1
			line=' '.join(line)
			
			"""print line"""
			for w in word_tokenize(line):
				if w not in stop_words and not createTokens.strHasNum(w) and not w.isdigit() and w not in punctuation:
					word_list.append(w)

			"""word_list.append([w.lower() for w in word_tokenize(line) if w not in stop_words and not createTokens.strHasNum(w) and not w.isdigit() and w not in punctuation])"""

	fh.close()


	return word_list
	
			

if __name__ == '__main__':

	while True:
		fname=raw_input("Give filename, or 0: ")	
		if fname=="0":
			break
		
		words=createWordsList(fname)
		print words
