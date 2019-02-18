from itertools import combinations

s,n = input().split()
#option 1
#for i in range(1,int(n)+1):
#    for comb in combinations(sorted(s),i):
#        print(*comb,sep="")

# option 2
print(*[''.join(j) for i in range(1,int(n)+1) for j in combinations(sorted(s),i)],sep="\n")
