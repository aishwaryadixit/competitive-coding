#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    count = 0
    
    for i in range(n):
        count += 1
        curr = s[i]
        runlength = 1
        for j in range(i + 1, n):
            if curr == s[j]:   
                runlength += 1
                count += 1
            else:
                matchlength=0
                for k in range(j + 1, n):
                    if curr !=s[k]:
                        break;
                        
                       # print("comparing 2",curr,"==",s[j])
                    matchlength+=1
                    if matchlength == runlength:
                        count+=1
                        break
                break
            
                                            
    return count
                            
                    
                

"""
    count=0
    match=0
    temp=""
    i=0
    matchedlength=0
    for i in range (n):
        temp=s[i]
        if s[i]!=s[i+1]:
            matchedlength=matchedlength+1
        if s[i]!=s[i+1]:
            j=i+2
            k=0
            while j<len(temp)+j:
                if s[j]!=temp[k]:
                    flag=1
                    break
                else:
                     flag=0
        if flag==0:
            count=count+1
            
    return count+n
"""

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
