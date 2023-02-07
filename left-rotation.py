#!/bin/python3

import math
import os
import random
import re
import sys


def rotateLeft(d, arr):
    # Write your code here
    x = len(arr)
    fla=0
    for i in range(d):
        fla=1
        while(fla==1):
            for j in range(x-1):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            fla=0
    
    return(arr)

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

