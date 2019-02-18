from itertools import product

l1 = map(int, input().split())
l2 = map(int, input().split())
#print(*(product(l1,l2)))
for x in product(l1,l2):
    print(x, end=" ")
