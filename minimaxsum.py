#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # solution for the problem 
    arr=sorted(arr)
    minsum=0
    maxsum=0
    n=len(arr)
    for i in range(0,n):
        if i!=(n-1):
            minsum+=arr[i]
        if i!=0:
            maxsum+=arr[i]
    print(minsum,maxsum)
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
