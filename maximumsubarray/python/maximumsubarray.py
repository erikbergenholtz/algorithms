#!/usr/bin/env python3

# Erik Bergenholtz (c) 2018
#
# This is a divide&conquer solution to the maximum subarray problem.
# It is adapted from the explanation of the solution in *Introduction to
# Algorithms by Cormen et al.
#
# The apporach divides the array into two equally long (if possible) subarrays
# A[low..mid] and A[mid+1..high]. When this division is performed, the maximum
# must be in one of three places:
#
# * Entirely in A[low..mid]
# * Entirely in A[mid+1..high]
# * Crossing the midpoint such that low <= i <= mid <= j <= high
#
# Finding the maximum subarray of the first two cases can be done recursively.
# Because of this, the problem is reduced to finding a maximum subarray that
# crosses the midpoint and picking the one with the larges sum of the three.
# Finding this midcrossing subarray can be done linearly. It consists of two
# subarrays, A[i..mid] and A[mid+1..j], thus finding these two and combining
# them solves this problem.


import sys
import math
import random

def getMidcrossingSubarray(arr, l, h, m):
    lSum = -float("inf")
    rSum = -float("inf")
    tSum = 0
    for i in range(m, l-1, -1):
        tSum += arr[i]
        if tSum > lSum:
            lSum = tSum
            lMax = i
    tSum = 0
    for i in range(m+1, h+1):
        tSum += arr[i]
        if tSum > rSum:
            rSum = tSum
            rMax = i
    return (lMax, rMax, lSum+rSum)

def getMaxSubarray(arr, l, h):
    if l == h:
        return (l,h,arr[l])
    else:
        m = math.floor((l+h)/2)
        lr = (lLow, lHigh, lSum) = getMaxSubarray(arr, l, m)
        rr = (rLow, rHigh, rSum) = getMaxSubarray(arr, m+1, h)
        cr = (cLow, cHigh, cSum) = getMidcrossingSubarray(arr, l, h, m)
        if lSum >= rSum and lSum >= cSum:
            return lr
        elif rSum >= lSum and rSum >= cSum:
            return rr
        else:
            return cr

def trivial(arr):
    lMax = rMax = 0
    mSum = -float("inf")
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if sum(arr[i:j+1]) > mSum:
                mSum = sum(arr[i:j+1])
                lMax = i
                rMax = j
    return (lMax, rMax, mSum)

def main():
    arr = [random.randint(-15,15) for _ in range(30)]
    #arr = [-9, -7, -6, 10, -2, 3, -8, 10, -6, -10, 4, -8, 13, -5, -1, -10, 12, -7, 11, 8, -14, -14, -13, 9, -12, 1, 14, 2, 7, -11]
    print(arr)
    l,h,s = getMaxSubarray(arr, 0, len(arr)-1)
    print("Maximum subarray with a sum of {}:\n{}".format(s,arr[l:h+1]))
    l,h,s = trivial(arr)
    print("Maximum subarray with a sum of {}:\n{}".format(s,arr[l:h+1]))
    return 0

if __name__ == '__main__':
    sys.exit(main())
