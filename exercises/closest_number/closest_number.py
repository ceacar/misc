#!/bin/python3

import math
import os
import random
import re
import sys


def closestNumbers(arr):
    #arr = [5,4,3,2]
    #expect output of [2,3], [3,4], [4,5] -->2 3 3 4 4 5
    arr = sorted(arr)
    #print("sorted {0}".format(arr))
    length = len(arr)
    lookup = {}
    current_min = sys.maxsize
    cache = []

    for i in range(1, length):
        j = i-1
        #print("comparing {0} {1}".format(arr[i], arr[j]))
        diff = abs(arr[i] - arr[j])
        if diff == 0:
            continue
        list_to_append = [arr[j],arr[i]]

        if diff == current_min:
            cache.append(list_to_append)
            #print("cache list updated:", current_min, cache)
        elif diff < current_min:
            current_min = diff
            #new low has been found, truncate previous
            cache = [list_to_append]
            #print("new cache:", current_min, cache)

    output_list = []
    for sub_list in cache:
        for ele in sub_list:
            output_list.append(ele)

    return output_list

if __name__ == '__main__':
    f = open("input.txt", 'r')
    n = int(f.readline().rstrip())
    lines = [line.rstrip() for line in f.readlines()]
    joined_lines = ' '.join(lines)
    arr = list(map(int, joined_lines.split()))
    #print("input arr:",arr)

    result = closestNumbers(arr)
    print(result)


