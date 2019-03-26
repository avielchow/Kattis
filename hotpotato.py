a,b = input().split()
children = int(a)
directions = []

for x in b:
    directions.append(x)

circle = [int(x) for x in range(children)]

location = 0
for x in directions:
    if x == "L":
        location += 1
        if location > (children-1):
            location = 0

    elif x == "R":
        location -= 1
        if location < 0:
            location = (children-1)

            
print (location)