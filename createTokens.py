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


def strHasNum(myLine):
	return any(c.isdigit() for c in myLine)
	
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
				temp=word
									
				for c in temp:
					if c in __init__.punctuation:
						word.remove(c)				
				if len(word)>0:	
					wordsList.append(''.join(word))
			else:
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

	
def createTokens(contents):
	
	words=[]
	i=0

	while i<len(contents):		
		line=contents[i]		
		words=tokenizeFile(line,words)
						
		i+=1

	return words


"""def createDict(fname,words):

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

	return len(words)"""



if __name__== '__main__':
	
	filename=raw_input("Give file name: ")
	createFileTokens(filename)
