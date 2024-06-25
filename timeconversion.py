#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hr=int(s[0:2])%12
    if hr!=0 and s.endswith('PM'):
        hr+=12
        time=str(hr)+s[2:-2]
        return time
    elif hr==0 and s.endswith('AM'):
        return '00'+s[2:-2]
    return s[:-2]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
