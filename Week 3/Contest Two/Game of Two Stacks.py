#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

def twoStacks(maxSum, a, b):
    # Write your code here
    a.reverse()
    b.reverse()
    stack = []
    tot=0
    counter = 0

    while a:
        x = a.pop()
        if (tot + x) <= maxSum:
            tot += x
            counter += 1
            stack.append(x)
        else: break
    
    maxCount = counter

    while b:
        x = b.pop()
        tot += x
        counter += 1
        while tot > maxSum and stack:
            tot -= stack.pop()
            counter -= 1
        if tot <= maxSum and counter > maxCount:
            maxCount = counter
    
    return maxCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
