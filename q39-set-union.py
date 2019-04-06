#sample input
# 9
# 1 2 3 4 5 6 7 8 9
# 2
# 5 10


m,n = [set(map(int,input().split())) for _ in range(4)][1::2]
print(len(m.union(n)))
