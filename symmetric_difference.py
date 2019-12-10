n1 = int(input())
A = input().split()
n2 = int(input())
B = input().split()

Aset = set()
Bset = set()
for i in A:
    Aset.add(int(i))

for i in B:
    Bset.add(int(i))

output = list(Aset.difference(Bset).union(Bset.difference(Aset)))
for i in sorted(output):
    print(i)