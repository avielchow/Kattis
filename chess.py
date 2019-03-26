numbers = []
for line in range(10):
    numbers.append(input())

numbers = [int(x) for x in numbers]

modulo = set()
for x in numbers:
    modulo.add(x%42)

print(len(modulo))