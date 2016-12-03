#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import __init__


def plotCommonWords(fname,number):
	
	"""filename=__init__.commonFilename+fname"""
	
	with open(fname,"r") as fh:
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
	x_20=[]
	y_20=[]
	with open(fname,"r") as fh:
		lines=fh.readlines()
		
	lineNum=0
	for line in lines:
		if line.startswith('File') or line.startswith('Number'):
			continue
		line=line.split('\t')
		if lineNum%2==0:
			x.append(int(line[1]))
			y.append(int(line[0]))
		
		else:
			x_20.append(int(line[1]))
			y_20.append(int(line[0]))
		lineNum+=1
		
	x.pop(len(x)-1)
	y.pop(len(y)-1)
	x=x+x_20
	y=y+y_20
		
	plt.plot(x,y,label='10collection')
	plt.plot(x_20,y_20,marker='.',linestyle='--',color='red',label='20 collection')
	plt.title("Heaps Diagram")
	plt.xlabel('Word List in Document	')
	plt.ylabel('Unique Word in Dictionary')
	plt.show()
	
	"""plt.plot(x_20,y_20)
	plt.title("Heaps Diagram")
	plt.xlabel('Word List in Document	')
	plt.ylabel('Unique Word in Dictionary')"""
	plt.show()
	
if __name__== '__main__':

	
	"""plotCommonWords(fname,number)"""
	plotHeapDiagram("results.txt")
	
