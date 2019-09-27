n = int(input('num: '))

i = len(str(n))  # работает не только для 5-значного числа
while i:
    n = (n % 10**i)
    i -= 1
    print(int(n / 10**i))
