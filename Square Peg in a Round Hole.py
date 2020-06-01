import math
from collections import deque

N, M, K = [int(x) for x in input().split()]
plot_radius = [round(int(x)*math.sqrt(2),2) for x in input().split()]
#convert house_radius to side length
house_radius = [round(int(x)*math.sqrt(2),2) for x in input().split()]
house = [int(x) for x in input().split()]

house.extend(house_radius)
house.sort()
plot_radius.sort()

house = deque(house)
plot = deque(plot_radius)

ans = 0
while house and plot:
    if plot.popleft() > house[0]:
        ans += 1
        house.popleft()
print(ans)

