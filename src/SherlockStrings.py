#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    match = {}
    i=0
    for char in s:
        if char in match.keys():
            match[char] = match[char]+1 #increase the value by 1 for that char
        else: match[char] = 1 #else for first occurrence allocate value as 1
    
    print (match)        
    flag=0
    baseline = -1
    for char, freq in match.items():
        if baseline==-1:
            baseline=freq
        if abs(baseline-freq)>1 and freq!=1:
            flag=flag+1
            print (baseline,freq)
            return "NO"
        if baseline!=freq and flag<2:
            flag=flag+1
            print (baseline,freq,flag)
        if flag>=2:
            print (baseline,freq, flag)
            return "NO"
        
        
        
        
    return "YES"
    
       
    
    
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
