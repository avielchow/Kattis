a = input().split()
stairs = int(a[0])
room = int(a[1])
order = input().split()
order = [int(x) for x in order]

def locateroom(a):
    locator = 0
    for x in a:
        if locator == room:
            return locator
        else:
            locator += 1

location = locateroom(order)


''' 0 to locator'''
def sumclockwise(a):
    count = 0
    for x in range(location):
        currentfloor = a[x]
        nextfloor = a[x+1]
        if nextfloor > currentfloor:
            count += nextfloor - currentfloor
    return count
            
    
''' 0 to - (locator + 1)'''
def sumcounterclockwise(a):
    count = 0
    for x in range(stairs - location):
        currentfloor = a[-(x)]
        nextfloor = a[-(x+1)]
        if nextfloor > currentfloor:
            count += nextfloor - currentfloor
    return count

clockwise = sumclockwise(order)
counterclockwise = sumcounterclockwise(order)


if clockwise < counterclockwise:
    print (clockwise)
else:
    print (counterclockwise)
    