N = int(input())
worlds = input().split()
worlds = [int(x) for x in worlds] 


def validity():
    count = 0
    for x in range(N-1):
        currentworld = (worlds[-(x+1)])
        previousworld = (worlds[-(x+2)])
        if currentworld <= previousworld:
            worlds[-(x+2)] = currentworld - 1
            if currentworld - 1 < 0:
                return 1
            else:    
                count += ((previousworld - currentworld) + 1)
        else: 
            pass
    return (count)

print (validity())


