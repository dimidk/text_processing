#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

def plotCommonWords(fname,number):
	
	filename="commonFile_"+fname
	
	with open(filename,"r") as fh:
		line=fh.read()
	data=line.split('\n')
	y=[]
	x=[]
	counter=1
	for d in data:
		num=d.split(':')
		x.append(counter)
		y.append(int(num[1]))
		counter+=1
		if counter==number:
			break
	
	plt.plot(x,y)
	plt.title("Frequency Diagram")
	plt.xlabel('Word Rank')
	plt.ylabel('Word Frequency')
	plt.show()
			

def plotHeapDiagram(fname):
	
	y=[]
	x=[]
	
	with open(fname,"r") as fh:
		lines=fh.readlines()
		
	for line in lines:
		if line.startswith('File') or line.startswith('Number'):
			continue
		line=line.split('\t')
		x.append(int(line[1]))
		y.append(int(line[0]))
	
	x.pop(len(x)-1)
	y.pop(len(x)-1)				
	plt.plot(x,y)
	plt.title("Heaps Diagram")
	plt.xlabel('Word List in Document	')
	plt.ylabel('Unique Word in Dictionary')
	plt.show()
	
if __name__== '__main__':

	
	"""plotCommonWords(fname,number)"""
	plotHeapDiagram("results.txt")
	
