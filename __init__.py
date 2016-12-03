#!/usr/bin/python
# -*- coding: utf-8-*-

import string
from nltk.corpus import stopwords
import os.path


punctuation=list(string.punctuation)
stop_words=set(stopwords.words('english'))
resultFile="results_"
commonFilename="commonFile_"

tweetsFile=commonFilename+"tweets.txt"
wikiFile=commonFilename+"wikipedia.txt"
darwinFile=commonFilename+"darwin.txt"
	
def findFile():
	
	filenum=[]
	
	
	heapFileTweets=resultFile+"tweets.txt"
	heapFileWiki=resultFile+"wikipedia.txt"
	
	if os.path.isfile(tweetsFile):
		filenum.append('1')
	else:
		filenum.append('0')
	
	if os.path.isfile(wikiFile):
		filenum.append('1')
	else:
		filenum.append('0')
	
	if os.path.isfile(darwinFile):
		filenum.append('1')
	else:
		filenum.append('0')
	
	return filenum
	
