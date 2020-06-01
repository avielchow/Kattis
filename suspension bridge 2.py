import math
d, s = [int(x) for x in input().split()]


def calculate_a(a):
    ans = (a * math.cosh(d / (2 * a))) - a
    return ans

def get_a():
    min = 0
    max = d ** 2
    mid = (min + max) / 2
    count = 0
    calc_a = calculate_a(mid)
    while s != round(calc_a,5):
        mid = (min + max) / 2
        calc_a = calculate_a(mid)
        if s < calc_a:
            min = mid
            count += 1
        elif s > calc_a:
            max = mid
            count +=1
        else:
            return mid
    return mid

a = get_a()
print (2*a * math.sinh(d/(2*a)))
