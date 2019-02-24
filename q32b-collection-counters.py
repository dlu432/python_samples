from collections import Counter
"""
num_shoes, stock = int(input()), Counter(map(int,input().split(" ")))
earned = 0

for size, price in [map(int, input().split()) for _ in range(int(input()))]:
    if (stock.get(size,0)>0):
        stock.get(size) -= 1
        earned += price
print(earned)
"""

stock = { 1:2, 2:5, 3:6}
print(stock)
list = [1,2,4]
for i in list:
    if stock.get(i,0)>0:
        print(stock.get(i))
print(stock)
