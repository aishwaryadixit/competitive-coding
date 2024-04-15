#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    pair=sys.maxsize
    flag=0
    minm=sys.maxsize
    j=0
    i=0
    arr=sorted(arr)
    for i in range(len(arr)-1): 
        pair= abs (arr[i] - arr[i+1])
        if pair<minm:
            minm=pair 
        
            
                
    return minm
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
