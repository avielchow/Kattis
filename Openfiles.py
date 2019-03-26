dir = "C:\\Users\\aviel\\Desktop\\Coding\\Kattis"
path = dir + "\\twostones\\1.in"
file = open(path, "r")


for line in file:
    N = int(line)

if N%2 == 0:
    print("Bob")
else:
    print("Alice")

'''1,2,3,4,5,6,7,8
Stones left - even or 0


1,2,3,4,5,6,7
stones left - odd
'''


