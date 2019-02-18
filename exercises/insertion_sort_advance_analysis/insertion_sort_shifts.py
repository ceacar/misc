#!/bin/python3 
import math
import os
import random
import re
import sys

class BinaryIndexedTree():
    def __init__(self, sz):
        self.sz = sz
        self.tree = [0] * sz
         
    def update(self, idx, val):
        while (idx <= self.sz):
               self.tree[idx] += val
               idx += (idx & -idx)
    def read(self, idx):
        sum = 0
        while (idx > 0):
            sum += self.tree[idx]
            idx -= (idx & -idx)
        return sum

# Complete the insertionSort function below.
def insertionSort(arr):
    """
    Take elements from the list in reverse and insert a one into their sorted position in a BIT. For element x, the number of elements less than x so far inserted into the BIT is number of inversions
    so far. By "sorted position" I mean the index that the element would be at if the list were sorted.
    [5,3,4,1] --> bit array 
    feed "1" into it first, then you have [0,1,0,0,0,0,...], prefix_query for (1) is 0
    feed "4" into it first, then you have [0,1,0,0,1,0,...], prefix_query for (1) is 1
    feed "3" into it first, then you have [0,1,0,1,1,0,...], prefix_query for (1) is 1
    feed "5" into it first, then you have [0,1,0,1,1,1,...], prefix_query for (1) is 3
    so total shift is 1+1+3=5
    """
    cnt = 0
    bit = BinaryIndexedTree(10**7+1)
    for val in reversed(arr):
        bit.update(val, 1)
        cnt += bit.read(val-1)
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

