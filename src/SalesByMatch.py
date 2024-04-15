#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    ar.sort()
    print(ar)
    prev = None
    freq = 1
    pair=0
    for item in ar:
        
        if prev is not None:
            if prev == item:
                freq = freq+1
                if freq % 2 == 0:
                    pair=pair+1
            else:
                freq = 1
        
        prev=item
    
                    
    return pair
                
                
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
