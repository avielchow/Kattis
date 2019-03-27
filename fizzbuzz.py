line = raw_input().split()
line = [int(x) for x in line]
x = line[0]
y = line[1]
N = line[2]

for number in range(1, N + 1):
    if number % x == 0 and number % y == 0:
        print ("FizzBuzz")
    elif number % x == 0:
        print ("Fizz")
    elif number % y == 0:
        print ("Buzz")
    else:
        print (number)
