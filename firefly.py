import bisect

N,H = [int(x) for x in input().split()]
# stalagmite rises from the floor
stalagmite = []
stalacite = []

for x in range(N):
    if x%2 == 0:
        stalagmite.append(int(input()))
    else:
        stalacite.append(H-int(input()))

stalacite.sort()
stalagmite.sort()

len_stalacite = len(stalacite)
len_stalagmite = len(stalagmite)

min = N
count =0
for x in range(1,H+1):
    ans = (len_stalagmite - bisect.bisect_left(stalagmite,x)) + (bisect.bisect_left(stalacite,x))
    if ans == min:
           count += 1
    if ans < min:
           min = ans
           count = 1


print (min, count)
