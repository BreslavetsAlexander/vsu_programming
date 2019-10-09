s = input('s: ')
symbols = ['+', '-', '*', '/', '//', '**']
operation = ''
for i in s:
    if i in symbols:
        operation += i

x, y = s.replace(operation, ' ').split()
x = float(x)
y = float(y)
val = [x + y, x - y, x * y, x / y, x // y, x**y]
print(val[symbols.index(operation)])
