#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    u=0
    d=0
    n=[0] * steps
    for i in  range (steps):
        direction=path[i]
        if  direction=='U':
            u=u+1
        elif direction=='D':
            u=u-1
        n[i] = u
        
    valley=0
    for j in range(steps-1):
        if n[j] == -1 and n[j+1] == 0:
            valley = valley+1
            
        
  #  print ("numers are " + str(n))
    
    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
