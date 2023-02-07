#!/bin/python3

import math
import os
import random
import re
import sys



def dynamicArray(n, queries):
    # Write your code here
    seq = [[] for _ in range(n)]
    ans = []
    lastAnswer = 0
    for i in queries:
        action, j, v = list(map(int, i))
        idx = (j^lastAnswer)%n
        if action == 1:
            seq[idx].append(v)
        else:
            temp = seq[idx]
            lastAnswer = seq[idx][v%len(temp)]
            ans.append(lastAnswer)
    return ans
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

