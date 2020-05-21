import math

n, m = [int(x) for x in input().split()]
shop = []
joe = []
for x in range(n):
    shop.append(int(input()))

for x in range(m):
    joe.append(int(input()))

shop.sort()
joe.sort()

def binary_search(low,high,number,extra):

    mid = math.floor((low+high)/2)

    if high >= low:
        if number == shop[mid]:
            return 0
        elif abs(number - shop[mid]) < extra:
            extra = abs(number-shop[mid])

        if number > shop[mid]:
            return binary_search(mid+1, high, number, extra)
        else:
            return binary_search(low, mid-1, number, extra)
    return extra

total = 0
extra_max = max(joe) + max(shop)

for x in joe:
    total += (binary_search(int(0),len(shop)-1,x,extra_max))
print(total)
