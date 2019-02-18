from itertools import permutations

s,n = input().split()
#option 1
for perm in permutations(sorted(s),int(n)):
    print(*perm,sep="")

#option 2
#print( *["".join(i) for i in permutations(sorted(s),int(n))],sep="\n")
