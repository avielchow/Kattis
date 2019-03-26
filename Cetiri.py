a = []

def cetiri(numbers):
    numbers = sorted(numbers)
    a = numbers[1]- numbers[0]
    b = numbers[2]- numbers[1]
    if a < b:
        difference = a
    else:
        difference = b
        
    if a == b:
        return (numbers[2] + difference)
    elif a > b:
        return (numbers[0] + difference)
    elif b > a: 
        return (numbers[1] + difference)
    
numbers = input().split(" ")
for x in numbers:
    if x != " ":
        a.append(int(x))

print (cetiri(a))