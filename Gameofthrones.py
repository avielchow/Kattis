line = [int(x) for x in input().split()]
n = line[0]
k = line[1]

''' n = number of children, k = number of instructions'''
commands = input().split()
directions = []

for index, command in enumerate(commands):
    if command != "undo":
        directions.append(command)
    else:
        undo = int((commands.pop(index + 1))) * -1
        directions = (directions[:undo])


directions = [int(x) for x in directions]

currentlocation = 0
    
for x in directions:
    if x > 0:
        currentlocation += x
        currentlocation = currentlocation % n
        if currentlocation == n:
            currentlocation = 0
    elif x < 0: 
        if currentlocation == 0:
            currentlocation = n
        currentlocation += x
        currentlocation = currentlocation % n
    else:
        pass

print(currentlocation)