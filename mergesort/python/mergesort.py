#!/usr/bin/env python

# mergesort.py
# Avg.   O(n log(n))
# Worst: O(n log(n))
# Author: Erik Bergenholtz

from random import randint

def merge(left, right):
    merged = []
    while len(left) != 0 and len(right) != 0:
        if left[0] >= right[0]:
            merged.append(left[0])
            left = left[1:]
        else:
            merged.append(right[0])
            right = right[1:]
    for i in left:
        merged.append(i)
    for i in right:
        merged.append(i)
    return merged


def mergesort(arr):
    if len(arr) == 1:
        return arr
    return merge(mergesort(arr[:len(arr)/2]),mergesort(arr[len(arr)/2:]))

def main():
    arr = []
    while len(arr) < 100:
        arr.append(randint(0,100))
    print arr
    print mergesort(arr)

if __name__ == '__main__':
    main()
