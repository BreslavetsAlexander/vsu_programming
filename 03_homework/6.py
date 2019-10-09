def is_simple(a):
    if a == 2 or a == 3 or a == 5 or a == 7:
        return True
    return bool(a % 2 and a % 3 and a % 5 and a % 7)


x = int(input('x = '))
print(is_simple(x))
