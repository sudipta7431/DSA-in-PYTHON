#!/bin/python3

import math
import os
import random
import re
import sys

def hourglassSum(arr):
    # Write your code here
    fal = 1
    sum1 = 0
    for i in range(1,5):
        for j in range(1,5):
            sum2 = arr[i][j]+arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1]+arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1]
            if fal==1:
                sum1 = sum2
                fal = 0
            if sum1 < sum2:
                sum1 = sum2
    return sum1
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

