#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    #s = "132 456 Wq  m e"
    a = s.split(" ")
    print(a)
    for i in range(0,len(a)):
        if(a[i]!=""):
            if (a[i][0].islower() and a[i][0].isdigit()==False):
                a[i] = a[i][0].upper() + a[i][1:len(a[i])]
    return ' '.join(a)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
