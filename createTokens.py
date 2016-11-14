#!/usr/bin/python
# -*- coding: utf-8-*-

"""do stemming 'cause have strings meaningless, so create first lists, and then dictionaries
using first default encoding utf-8 and then encoding latin-1 """

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
import __init__
import codecs
import time

"""def createFileUTF():
	BLOCKSIZE=1048576
	sourceFile=codecs.open("tweets.txt","r","latin-1")
	targetFile=codecs.open("tweetsUTF","w","utf-8")
	while True:
		contents=sourceFile.read(BLOCKSIZE)
		if not contents:
			break
		targetFile.write(contents)"""

def strHasNum(myLine):
	return any(c.isdigit() for c in myLine)

def createContentList(fname):

	contents=[]	
	fh=codecs.open(fname,"r","latin-1")
	lines=fh.readlines()
	for line in lines:
		if line.startswith("<http"):
			line=line.split('>')
			line=line[len(line)-1].split('@en')[0]

			"""content=line.rsplit('\n')
			contents.append(content)"""

			contents.append(line)
		else:
			line=line.split('http')
			i=0
			while i<len(line):
				if line[i].find('s://')!=-1:
					line.pop(i)
				i+=1
			line=' '.join(line)

			"""content=line.rsplit('\n')
			contents.append(content)"""

			contents.append(line)

	"""while True:
		line=fh.readline()
		if line.startswith("<http"):
			
			line=line.split('>')
			line=line[len(line)-1].split('@en')[0]
			print line
			contents.append(line)
	
		else:
			
			line=line.split('http')
			i=0
			while i<len(line):
				if line[i].find('s://')!=-1:
					line.pop(i)
				i+=1
			print ' '.join(line)
			contents.append(' '.join(line))

		if line=="":
			break"""

	fh.close()
	return contents
	
def createTokensFromFile(fname):

	fh=codecs.open(fname,"r","latin-1")
	words=[]
	while True:
		line=fh.readline()
		if line.startswith("<http"):
			
			line=line.split('>')
			line=line[len(line)-1].split('@en')[0]
	
			tokens=word_tokenize(line)
			for w in tokens:
				w=w.lower()
				if (w.find('\u')!=-1 or w.isdigit()==True):
					continue
				if w in __init__.stixis:
					continue
				if (strHasNum(w)==True):
					continue
				words.append(w)
		else:
			
			line=line.split('http')
			i=0
			while i<len(line):
				if line[i].find('s://')!=-1:
					line.pop(i)
				i+=1
			line=' '.join(line)
			tokens=word_tokenize(line)
			for w in tokens:
				w=w.lower()
				if (w.find('\u')!=-1 or w.isdigit()==True):
					continue
				if w in __init__.stixis:
					continue
				if (strHasNum(w)==True):
					continue
				words.append(w)

		if line=="":
			break

	fh.close()
	return words

	
def createTokens(contents):
	
	words=[]
	i=0

	while i<len(contents):		
		line=contents[i]		
		tokens=word_tokenize(line)
		for w in tokens:
			w=w.lower()
			if (w.find('\u')!=-1 or w.isdigit()==True):
				continue
			if w in __init__.stixis:
				continue
			if (strHasNum(w)==True):
				continue
			words.append(w)		
		i+=1

	return words


def createDict(fname,words):

	if words==None:
		words=createTokensFromFile(fname)

	words.sort()
	words_dict={}
	
	prcFile=open(fname+'.prc','w')

	for key in words:
		words_dict[key]=words_dict.get(key,0)+1

	for key,val in words_dict.items():
		print key,val
		prcFile.write(key.encode('utf-8')+' ')
		prcFile.write(str(val).encode('utf-8')+'\n')
		
	prcFile.close()

	return len(words)



"""if __name__== '__main__':
	
	filename=raw_input("Give file name: ")
	createFileTokens(filename)"""
