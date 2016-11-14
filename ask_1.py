#! /usr/bin/python
# -*- coding: utf-8-*-

import nltk 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import createTokens

if __name__ == '__main__':
	
	stop_words=stopwords.words('english')

	"""createTokens.createFileUTF()"""

	while True:
		fname=raw_input("File name is, otherwise give 0: ")
		if fname=='0':
			break	
		"""contentList=createTokens.createContentList(fname)"""
	
		wordsList=createTokens.createTokensFromFile(fname)
		
		numberDict=createTokens.createDict(fname,wordsList)

		print "number of Tokens: ", numberDict

		
			
				

		

