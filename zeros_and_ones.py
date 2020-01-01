import numpy

n = input().split()
if len(n) == 2:
    print(numpy.zeros((int(n[0]),int(n[1])), dtype = numpy.int))
    print(numpy.ones((int(n[0]),int(n[1])), dtype = numpy.int))
if len(n) == 3:
    print(numpy.zeros((int(n[0]),int(n[1]),int(n[2])), dtype = numpy.int))
    print(numpy.ones((int(n[0]),int(n[1]),int(n[2])), dtype = numpy.int))
if len(n) == 4:
    print(numpy.zeros((int(n[0]),int(n[1]),int(n[2]),int(n[3])), dtype = numpy.int))
    print(numpy.ones((int(n[0]),int(n[1]),int(n[2]),int(n[3])), dtype = numpy.int))
if len(n) == 5:
    print(numpy.zeros((int(n[0]),int(n[1]),int(n[2]),int(n[3]),int(n[4])), dtype = numpy.int))
    print(numpy.ones((int(n[0]),int(n[1]),int(n[2]),int(n[3]),int(n[4])), dtype = numpy.int))
