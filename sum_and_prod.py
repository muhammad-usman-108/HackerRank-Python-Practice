import numpy

n = input().split()
my_array = []
for i in range(0,int(n[0])):
    temp = input().split()
    temp = [int(i) for i in temp]
    my_array.append(temp)

print(numpy.prod(numpy.sum(my_array, axis = 0)))
