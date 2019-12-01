#!/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())


if (N%2 == 1):
    print("Weird")
if (N%2 == 0 and N>=2 and N<=5):
    print("Not Weird")
if (N%2 == 0 and N>=6 and N<=20):
    print("Weird")
if (N%2 == 0 and N>20):
    print("Not Weird")
