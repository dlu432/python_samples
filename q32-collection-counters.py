from collections import Counter

num_shoes, stock = int(input()), Counter(map(int,input().split(" ")))
earned = 0

for size, price in [map(int, input().split()) for _ in range(int(input()))]:
    if (stock[size]>0):
        stock[size] -= 1
        earned += price
print(earned)
