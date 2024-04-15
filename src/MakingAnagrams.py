#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    total=0
    # Write your code here
    for element in a:
        i=0
        j=0
        flag=0
        
        for compare in b:
            if element==compare:
                flag=1
                a=a[:i]+a[i+1:]
                b=b[:j]+b[j+1:]
                break;
            
            
            else:
                j=j+1
    print (a,b)
    total = len(a)+len(b)
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
