#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    towin=1
    luckBalance=0
    contests.sort(reverse=True)
    print (contests)
    maxl=sys.maxsize
   
   
    for element in contests:
        l,t=element
        if towin<=k and t==1:
            towin=towin+1
            luckBalance=luckBalance+l
            print(l,t,"luck balanced up")
        elif t==1:
            luckBalance=luckBalance-l
            print(l,t,"luck used")
        else:
            luckBalance=luckBalance+l
            print(l,t,"luck balanced up 0")
            

    print(luckBalance)
    return luckBalance
            
        
        
            
            
    
        
         
       
       
       
   
            
            
            
            
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
