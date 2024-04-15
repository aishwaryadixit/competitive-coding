#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rotLeft(a, d):
    # Write your code here
    k=0
    n=len(a)
    b=[None] * n
    j=d
    i=0
    
    while (j<n and i<j):
        b[i]=a[j]
        j=j+1
        i=i+1
        
    j=0
    while (j<d and j<n):
        b[i]=a[j]
        i=i+1
        j=j+1
    
   
    return b
        
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
