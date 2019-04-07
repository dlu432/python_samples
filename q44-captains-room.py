# Use getattr to get set method
# Find a unique number in this list
m = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]
n = int(input())
m = list(map(int,input().split()))
unique_room = set()
family_room = set()
for x in m:
    if x not in unique_room:
        unique_room.add(x)
    else:
        family_room.add(x)
print(unique_room.difference(family_room).pop())
