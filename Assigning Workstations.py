#https://open.kattis.com/submissions/5754283
from collections import deque
n,m = [int(x) for x in input().split()]
starts = []
breaks = []


for x in range(n):
    a, s = [int(x) for x in input().split()]
    starts.append(a)
    if s != 0:
        breaks.append(a+s)

starts.sort()
breaks.sort()

starts = deque(starts)
breaks = deque(breaks)

def find_match(start, breaks):
    if breaks:
        if breaks[0] <= start <= breaks[0]+m:
            breaks.popleft()
            return 1
        elif breaks[0]+m < start:
            while breaks and breaks[0]+m < start:
                breaks.popleft()
                if breaks[0] <= start <= breaks[0] + m:
                    breaks.popleft()
                    return 1
            return 0
        elif breaks[0] > start:
            return 2
    else:
        return 0



ans = 0
temp= 0

while breaks and starts:
    remaining_starts = []
    for start in starts:
        temp = find_match(start, breaks)
        if temp == 1:
            ans += 1
        elif temp == 0:
            remaining_starts.append(start)

    starts = remaining_starts


if m == 0:
    print (0)
else:
    print(ans)
