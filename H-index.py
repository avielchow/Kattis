N = int(input())
citations = []

for x in range(N):
    citations.append(int(input()))

citations.sort()

max  = 0
for x in (range(N,0, -1)):
    ans = (min(x,citations[N-x]))
    if ans > max:
        max = ans
print (max)
