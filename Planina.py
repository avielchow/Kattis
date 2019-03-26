side = [3]
for x in range(15):
    side.append((side[-1]*2) -1)
    
N = int(input().strip())
point = side[N-1]
print (point**2)

    