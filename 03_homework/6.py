from math import sqrt


def is_simple(a):
    for i in range(2, int(sqrt(a)) + 1):
        if not a % i:
            return False
    return True


x = int(input('x = '))
print(is_simple(x))
