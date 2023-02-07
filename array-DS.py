#!/bin/python3

import math
import os
import random
import re
import sys


def reverseArray(a):
    # Write your code here
    a1 = []
    x = len(a)
    for i in range(x):
        a1.append(a[x-1-i])
    return a1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

