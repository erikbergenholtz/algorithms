#!/usr/bin/env python

import sys

class Node:
	c=''
	freq=0
	left=None
	right=None
	def __init__(self,freq=float("INF"),c=''):
		self.c = c
		self.freq = freq
	def dump(self,n):
		for i in range(0,n):
			sys.stdout.write("   ")
		print self.c + "," + str(self.freq)
		if self.left != None:
			self.left.dump(n+1)
		if self.right != None:
			self.right.dump(n+1)

	def isLeaf(self):
		return self.c != ''

def getLowestFreq(nList):
	lowest = Node('',float("INF"))
	lIndex = -1
	for i in range(0,len(nList)):
		if nList[i].freq < lowest.freq:
			lowest = nList[i]
			lIndex = i
	del nList[lIndex]
	return lowest,nList

def buildTree(nList):
	while len(nList) > 1:
		l, nList = getLowestFreq(nList)
		r,nList = getLowestFreq(nList)
		p = Node(l.freq+r.freq)
		p.left = l
		p.right = r
		nList.append(p)
	return nList[0]

def getFrequencies(str):
	fList = {}
	for c in str:
		c = c.lower()
		if c not in fList:
			fList[c] = 0
		fList[c] = fList[c] + 1
	nList = []
	for k,v in fList.iteritems():
		nList.append(Node(v,k))
	return nList

def getCode(node,c):
	cList = {}
	if node != None and not node.isLeaf():
		cList = getCode(node.left,c+'0')
		cList.update(getCode(node.right,c+'1'))
	else:
		cList[node.c] = c
	return cList

def main():
	#str = "Pack my box with five dozen liquor jugs"
	str = "a dead dad ceded a bad babe a beaded abaca bed"
	print str + '\n'
	nList = getFrequencies(str)
	hTree = buildTree(nList)
	cList = getCode(hTree,'')
	for k,v in cList.iteritems():
		print k + ": " + v

if __name__ == '__main__':
	main()
