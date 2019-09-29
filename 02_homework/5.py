n = int(input('num: '))

i = len(str(n))

for x in range(i, 0, -1):
    n = n % 10**x
    print(n // 10**(x - 1))
