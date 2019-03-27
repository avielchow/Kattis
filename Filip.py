line = raw_input().split()
line = [int(x) for x in line]

def flip(number):
    num = []
    while number > 0:
        num.append(number%10)
        number = number/10
    num = int(''.join([str(x) for x in num]))
    return num
    
number = flip(line[0])
number1 = flip(line[1])

if number > number1:
    print (number)
else:
    print(number1)
