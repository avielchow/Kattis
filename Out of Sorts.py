n, m, a, c, x = [int(x) for x in input().split()]


def create_sequence(n, m, a, c, x):
    sequence = []
    last_number = (((x*a) + c) % m)
    sequence.append(last_number)
    for number in range(n-1):
        xi = ((last_number * a) + c) % m
        last_number = xi
        sequence.append(xi)
    return sequence

def binary_search(seq, low, high, number):
    if high >= low:
        mid = int((low + high) / 2)
        if seq[mid] == number:
            return True
        elif seq[mid] > number:
            return binary_search(seq, low, mid-1, number)
        else:
            return binary_search(seq, mid + 1, high, number)
    else:
        return False


sequence = create_sequence(n, m, a, c, x)
count = 0
high = len(sequence) -1
for number in sequence:
    if binary_search(sequence, int(0), high, number) == True:
        count += 1

print(count)
