#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    # Write your code here
    part = ""
    i=0
    count = 0
    print ("s given is ", s)
    while (i<len(s)-1):
        if s[i] == s[i+1]:
            print ("first is ", i, " second is ", i+1)
            i=i+1
            #print (" s is now ", s)
            
            count = count+1
        else:
            i=i+1
    
                
    return count
            
         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
