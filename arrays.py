import numpy

def arrays(arr):
    b = numpy.array(arr,float)
    return b[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)