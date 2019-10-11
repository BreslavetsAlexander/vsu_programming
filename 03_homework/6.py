def is_simple(a):
    simple = True
    for i in range(2, a):
        if not a % i:
            simple = False
            break
    return simple


x = int(input('x = '))
print(is_simple(x))
