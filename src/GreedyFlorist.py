#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):

    friends = k
    flowers = len(c)
    leftover = flowers-k
    c.sort(reverse=True)
    print(c)
    print("starting from 0 to ",k-1 )
    total=0
    i=0
    while(i<k):
        total = total + c[i]
        i=i+1
        
    print ("single sum = ", total)
    n=0
    if leftover>0:
        n=1
        print ("remaining flowers from ", i , "to", flowers-1 )
        while(i<flowers):
            j=1
            for j in range (1,k+1):
                if j < flowers:
                    print ("friend",j,"takes ",n,"th flower for ", i, "\ncalc = (", n,"+1)*",c[i] )
                    total = total + (n+1)*c[i]
                    i=i+1
                    if i==flowers:
                        break
                else:
                    break
                
            n=n+1
    return total
            
                    
            
        
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
