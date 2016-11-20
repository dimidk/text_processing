#!/usr/bin/python
# -*- coding:utf-8-**

	
import nltk
import string
from nltk import word_tokenize
from nltk import text
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

stop_words=set(stopwords.words('english'))

""" !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ """


def removeUseless(line):
	
	print "line before x number:", lineinfo
	word=line.split('\\x')
	
	
def stopWordsRemoval(line,wordList):
	
	for w in word_tokenize(line):
				
		if w.lower() in stop_words:
			continue
		elif all(c in __init__.punctuation for c in w):
			continue
		elif createTokens.strHasNum(w) or w.isdigit():
			continue
		elif any(c in __init__.punctuation for c in w):
			word=list(w.lower())
			temp=word
			for c in temp:
				if c in __init__.punctuation:
					word.remove(c)

			if len(word)>0:	
				wordList.append(''.join(word))
		else:
			wordList.append(w.lower())
	
	return wordList


def createStemmed(fname,stemmer):
	
	
	word_list=createTokens.createTokensFromFile(fname)
	
	"""fh=codecs.open(fname,"r","latin-1")
	lines=fh.readlines()
	for line in lines:
		
		if line.startswith("<http"):
			line=line.split('>')
			line=line[len(line)-1].split('@en')[0]
		
			print line
			if line.find('http')!=-1 or line.find('www')!=-1 or line.find('https')!=-1:
				line=createTokens.removeUrl(line)
			
			word_list=createTokens.tokenizeFile(line,word_list)
			words=[w.lower() for w in word_list if w.lower() not in stop_words ]
			
			word_list=stopWordsRemoval(line,word_list)
	
		else:

			if line.find('http')!=-1 or line.find('www')!=-1 or line.find('https')!=-1:
				line=createTokens.removeUrl(line)
				
			word_list=createTokens.tokenizeFile(line,word_list)
			words=[w.lower() for w in word_list if w.lower() not in stop_words ]
			word_list=stopWordsRemoval(line,word_list)
			
	del lines
	fh.close()"""
	
	words=[w for w in word_list if w not in stop_words ]
	
	stemmed=[]
	for item in words:
		stemmed.append(stemmer.stem(item))
	
	return stemmed
	
	"""return word_list"""
	
			
def stem_words(word_list,stemmer):
	
	stemmed=[]
	for item in word_list:
		stemmed.append(stemmer.stem(item))
	
	return stemmed

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
		collection=nltk.text.TextCollection([text1,text2,text3])
		
		print "making tf-idf for each word in ",fname1
		tfidf_text1={word:collection.tf_idf(word,text1) for word in text1}
		print "relaxing......................"
		time.sleep(1)
		
		print "making tf-idf for each word in ",fname2
		tfidf_text2={word:collection.tf_idf(word,text2) for word in text2}
		print "relaxing......................"
		time.sleep(1)
		
		print "making tf-idf for each word in ",fname3
		tfidf_text3={word:collection.tf_idf(word,text3) for word in text3}
		print "relaxing......................"
		time.sleep(1)
		
		del text3,text2,text1,collection
		print "relaxing......................"
		time.sleep(1)
		
		tfidf_text1Reverse=[]
		for key,val in tfidf_text1.items():
			tfidf_text1Reverse.append((val,key))
		
		print "sorting the word weighted list................."
		tfidf_text1Reverse.sort(reverse=True)
		
		print "printing the most 10 important words......................."
		for val,key in tfidf_text1Reverse[:10]:
			print key,val
		
		
		
		"""freq1=nltk.FreqDist(text1)
		freq2=nltk.FreqDist(text2)
		freq3=nltk.FreqDist(text3)
				
		print "creating word list........................." """
		
		"""words=createWordsList(fname)"""
		
		print "creating word list after stemming..................."
		
		"""for word, count in freq1.iteritems():
			print word,count
		
		time.sleep(0.2)
		
		for word, count in freq2.iteritems():
			print word,count
		
		time.sleep(0.2)
		
		for word, count in freq3.iteritems():
			print word,count"""
				
		"""stemmed=stem_words(words,stemmer)"""
		"""stemmed=stem_words(words,stemmer)"""

		
		"""fh=codecs.open("weightFile.txt","w","latin-1")
		print "creating file ............................."
		
		for w in stemmed:
			fh.write(w)
			fh.write("\n")
				
		fh.close()
		
		print words"""
