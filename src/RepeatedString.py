#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#


def repeatedString(s, n):
    # Write your code here
    i=0
    #form the string   
  
    i=1
    count = 0
    
    for element in s:
        #print (element)
        if i <= n and element == 'a':
            count = count+1
        elif i>n:
            break
        i=i+1
   
    rem = 0
    left = n%len(s)
    print (left)
    for element in s[0:left]:
        if element == 'a':
            rem = rem+1   
                 
    print (count)
    strings = n//len(s)
    
    print (count, strings)
    x = count*strings
    
            
    return x+rem
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
