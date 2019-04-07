# Use getattr to get set method
n = int(input())
m = set(map(int,input().split()))
for x in range(int(input())):
    method, n = input().split()
    o = set(map(int, input().split()))
    getattr(m,method)(o)
print(sum(m))
