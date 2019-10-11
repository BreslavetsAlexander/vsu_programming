def is_simple(a):
    for i in range(2, a):
        if not a % i:
            return False
    return True


x = int(input('x = '))
print(is_simple(x))
