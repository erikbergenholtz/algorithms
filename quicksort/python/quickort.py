#!/usr/bin/env python

# quicsort.py
# Avg.:  O(n log(n))
# Worst: O(n log(n))
# Author: Erik Bergenholtz

from random import randint

def quicksort(arr):
    if len(arr) < 1:
        return arr
    p = arr[0]
    l = [x for x in arr[1:] if x<=p]
    r = [x for x in arr[1:] if x>p]
    return quicksort(l) + [p] + quicksort(r)

def main():
    arr = [randint(0,100) for i in range(0,10)]
    print(arr)
    print(quicksort(arr))

if __name__ == '__main__':
    main()
