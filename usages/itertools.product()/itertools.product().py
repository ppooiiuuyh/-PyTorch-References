import itertools

for i, j in itertools.product(range(2), range(3)):
    print(i,j)

''' result
0 0
0 1
0 2
1 0
1 1
1 2
'''