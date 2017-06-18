#!/usr/bin/env python

# stoogesort.py
# Avg.:  O(n^(log(3)/log(1.5)))
# Worst: O(n^(log(3)/log(1.5)))
# Author: Erik Bergenholtz

from random import randint

def stooge(arr,l,h):
	if arr[l] < arr[h]:
		arr[l],arr[h] = arr[h],arr[l]
	if h-l+1 > 2:
		t=(h-l+1)/3
		arr = stooge(arr,l,h-t)
		arr = stooge(arr,l+t,h)
		arr = stooge(arr,l,h-t)
	return arr

def main():
	arr = []
	while len(arr) < 10:
		arr.append(randint(0,100))
	print arr
	print stooge(arr,0, len(arr)-1)

if __name__ == '__main__':
	main()
